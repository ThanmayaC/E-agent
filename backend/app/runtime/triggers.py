"""Trigger Engine — configurable rules over the event bus.

A rule reads "when <event> and <conditions> then <action>". Rules are data,
not code: they persist as JSON, arrive over the API, and are evaluated
against event payloads by a small, deliberately non-Turing-complete
condition language. That is the point — a business user can add a trigger
without a deploy, and no trigger can execute arbitrary code.

    condition:  {"field": "health_change", "op": "lt", "value": -5}
    fields address the event payload by dotted path ("risk.severity").
    ops: eq ne gt gte lt lte contains in exists not_exists changed_by

Actions are declarative too — each names an action kind the Action Queue
already understands, so a trigger cannot bypass the approval layer.
"""
from __future__ import annotations

import threading
from typing import Any, Callable

from app.core.logging import get_logger
from app.runtime.events import EVENT_KINDS, Event, EventBus
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

OPERATORS: dict[str, Callable[[Any, Any], bool]] = {
    "eq": lambda actual, expected: actual == expected,
    "ne": lambda actual, expected: actual != expected,
    "gt": lambda actual, expected: _numeric(actual) > _numeric(expected),
    "gte": lambda actual, expected: _numeric(actual) >= _numeric(expected),
    "lt": lambda actual, expected: _numeric(actual) < _numeric(expected),
    "lte": lambda actual, expected: _numeric(actual) <= _numeric(expected),
    "contains": lambda actual, expected: str(expected).lower() in str(actual).lower(),
    "in": lambda actual, expected: actual in (expected or []),
    "exists": lambda actual, expected: actual is not None,
    "not_exists": lambda actual, expected: actual is None,
    "abs_gte": lambda actual, expected: abs(_numeric(actual)) >= _numeric(expected),
}

MISSING = object()


def _numeric(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return float("nan")  # comparisons against nan are False — a missing
        # number never fires a threshold rule


def _resolve(payload: dict, path: str) -> Any:
    """Dotted-path lookup into an event payload; None when absent."""
    current: Any = payload
    for part in path.split("."):
        if isinstance(current, dict):
            current = current.get(part)
        elif isinstance(current, list) and part.isdigit():
            index = int(part)
            current = current[index] if index < len(current) else None
        else:
            return None
        if current is None:
            return None
    return current


class TriggerEngine:
    """Rule-based automation: events in, queued actions out."""

    def __init__(self, store: RuntimeStore, bus: EventBus, queue,
                 workflows=None):
        self._store = store
        self._bus = bus
        self._queue = queue
        self._workflows = workflows
        self._lock = threading.RLock()
        self._fired = 0
        self._handlers: dict[str, Callable[[dict, Event], Any]] = {}
        bus.subscribe("*", self._on_event, name="trigger_engine")

    # --------------------------------------------------------------- rules
    def register_handler(self, name: str,
                         handler: Callable[[dict, Event], Any]) -> None:
        """Bind a rule action name to platform work. Rules reference handlers
        by name only, so a stored rule can never name arbitrary code."""
        self._handlers[name] = handler

    def add_rule(self, name: str, event: str, action: str,
                 conditions: list[dict] | None = None,
                 params: dict | None = None, description: str = "",
                 enabled: bool = True) -> dict:
        if event not in EVENT_KINDS:
            raise ValueError(f"Unknown event kind: {event}")
        for condition in conditions or []:
            if condition.get("op") not in OPERATORS:
                raise ValueError(f"Unknown operator: {condition.get('op')!r}")
            if not condition.get("field"):
                raise ValueError("Every condition needs a field")
        rule = {"rule_id": new_id("rule"), "name": name, "event": event,
                "action": action, "conditions": conditions or [],
                "params": params or {}, "description": description,
                "enabled": enabled, "fires": 0, "last_fired_at": "",
                "last_error": "", "created_at": now_iso(),
                "updated_at": now_iso()}
        return self._store.append("triggers", rule)

    def set_enabled(self, rule_id: str, enabled: bool) -> dict | None:
        return self._store.update("triggers", "rule_id", rule_id,
                                  {"enabled": enabled})

    def delete_rule(self, rule_id: str) -> bool:
        with self._lock:
            rules = self._store.read("triggers")
            remaining = [r for r in rules if r["rule_id"] != rule_id]
            if len(remaining) == len(rules):
                return False
            self._store.write("triggers", remaining)
            return True

    def rules(self, event: str = "", enabled_only: bool = False) -> list[dict]:
        items = self._store.read("triggers")
        if event:
            items = [r for r in items if r["event"] == event]
        if enabled_only:
            items = [r for r in items if r["enabled"]]
        return items

    def ensure_defaults(self, defaults: list[dict]) -> int:
        """Install the SDS default rules once. A rule the operator deleted or
        disabled stays that way — defaults seed, they do not enforce."""
        existing = {r["name"] for r in self._store.read("triggers")}
        created = 0
        for spec in defaults:
            if spec["name"] in existing:
                continue
            self.add_rule(**spec)
            created += 1
        return created

    # ---------------------------------------------------------- evaluation
    def _on_event(self, event: Event) -> None:
        for rule in self.rules(event=event.kind, enabled_only=True):
            try:
                if self.evaluate(rule, event):
                    self._fire(rule, event)
            except Exception as exc:  # noqa: BLE001 — a bad rule never breaks the bus
                logger.exception("Trigger rule %s failed", rule["name"])
                self._store.update("triggers", "rule_id", rule["rule_id"],
                                   {"last_error": str(exc)[:200]})

    def evaluate(self, rule: dict, event: Event) -> bool:
        """All conditions must hold (AND). No conditions = fires on the event
        alone."""
        for condition in rule.get("conditions", []):
            actual = _resolve(event.payload, condition["field"])
            operator = OPERATORS[condition["op"]]
            if not operator(actual, condition.get("value")):
                return False
        return True

    def _fire(self, rule: dict, event: Event) -> None:
        handler = self._handlers.get(rule["action"])
        if handler is None:
            logger.warning("Trigger %s names unknown action %r — ignored",
                           rule["name"], rule["action"])
            self._store.update("triggers", "rule_id", rule["rule_id"],
                               {"last_error":
                                f"no handler for action {rule['action']!r}"})
            return
        handler(rule, event)
        with self._lock:
            self._fired += 1
        self._store.update("triggers", "rule_id", rule["rule_id"],
                           {"fires": rule["fires"] + 1,
                            "last_fired_at": now_iso(), "last_error": ""})
        logger.info("Trigger fired: %s (%s → %s)", rule["name"], event.kind,
                    rule["action"])

    # ---------------------------------------------------------------- read
    def stats(self) -> dict:
        rules = self._store.read("triggers")
        return {"rules": len(rules),
                "enabled": sum(1 for r in rules if r["enabled"]),
                "fired_this_session": self._fired,
                "total_fires": sum(r.get("fires", 0) for r in rules),
                "handlers": sorted(self._handlers),
                "failing": [r["name"] for r in rules if r.get("last_error")]}
