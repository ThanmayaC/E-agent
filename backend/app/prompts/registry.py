"""Prompt Registry (Version 2.2).

Every prompt the platform sends to a language model is declared here, not
embedded in the code that happens to need it. That matters for three reasons
an enterprise actually cares about:

    ownership   a prompt is a policy artifact — somebody owns its wording
    versions    changing a prompt changes every downstream output; the old
                version must remain readable and the change must be recorded
    review      a compliance reviewer must be able to read every instruction
                the platform gives a model without reading Python

A prompt is a **template plus a contract**: declared variables, an owner, a
version, tags, and a change history. Rendering with a missing variable is an
error at the boundary rather than an f-string that silently produces the word
"None" inside an executive report.

Templates are declared in ``app.prompts.domains`` — one module per domain, as
the SDS organizes them. The registry loads them at construction and, when a
data directory is configured, records every version change to disk so the
history survives a restart.
"""
from __future__ import annotations

import json
import re
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

DOMAINS = ("executive", "reports", "meetings", "communications", "analytics",
           "rca", "sop", "forecast", "copilot")

VARIABLE = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")
MAX_HISTORY = 500


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class PromptNotFound(KeyError):
    """No prompt is registered under this id."""


class PromptVariablesMissing(ValueError):
    """A render call did not supply every declared variable."""


@dataclass
class PromptTemplate:
    """One versioned prompt.

    ``variables`` is derived from the template body when not given, so a
    declaration cannot drift from what the text actually interpolates.
    """
    prompt_id: str                     # "reports.evidence_narrator"
    domain: str
    template: str
    version: int = 1
    owner: str = "platform"
    description: str = ""
    tags: tuple[str, ...] = ()
    variables: tuple[str, ...] = ()
    # Prompts whose wording is a compliance statement, not a convenience.
    # Changing one is a governed action; the Admin console flags them.
    governed: bool = False

    def __post_init__(self) -> None:
        if self.domain not in DOMAINS:
            raise ValueError(
                f"Prompt {self.prompt_id}: unknown domain {self.domain!r} "
                f"(known: {', '.join(DOMAINS)})")
        if not self.prompt_id.startswith(f"{self.domain}."):
            raise ValueError(
                f"Prompt {self.prompt_id}: id must start with its domain "
                f"('{self.domain}.')")
        found = tuple(dict.fromkeys(VARIABLE.findall(self.template)))
        if not self.variables:
            self.variables = found
        else:
            undeclared = set(found) - set(self.variables)
            if undeclared:
                raise ValueError(
                    f"Prompt {self.prompt_id}: template uses undeclared "
                    f"variables {', '.join(sorted(undeclared))}")

    def render(self, **values: Any) -> str:
        """Fill the template. Missing variables raise rather than render the
        string "None" into something an executive will read."""
        missing = [v for v in self.variables if v not in values]
        if missing:
            raise PromptVariablesMissing(
                f"Prompt '{self.prompt_id}' needs {', '.join(missing)}")
        rendered = self.template
        for name in self.variables:
            rendered = rendered.replace("{" + name + "}", str(values[name]))
        return rendered

    def describe(self) -> dict:
        return {"id": self.prompt_id, "domain": self.domain,
                "version": self.version, "owner": self.owner,
                "description": self.description, "tags": list(self.tags),
                "variables": list(self.variables), "governed": self.governed,
                "characters": len(self.template)}


class PromptRegistry:
    """Every prompt, by id, with its versions and change history."""

    def __init__(self, prompts_dir: Path | None = None, load_defaults: bool = True):
        self._current: dict[str, PromptTemplate] = {}
        self._versions: dict[str, list[PromptTemplate]] = {}
        self._history: list[dict] = []
        self._dir = prompts_dir
        self._lock = threading.RLock()
        if prompts_dir is not None:
            prompts_dir.mkdir(parents=True, exist_ok=True)
            self._history = self._read_history()
        if load_defaults:
            self.load_defaults()

    # ------------------------------------------------------------ loading
    def load_defaults(self) -> int:
        """Load every declared template from the domain modules."""
        from app.prompts.domains import all_templates
        count = 0
        for template in all_templates():
            self.register(template, record=False)
            count += 1
        logger.debug("Prompt registry loaded %d templates", count)
        return count

    def register(self, template: PromptTemplate, actor: str = "platform",
                 record: bool = True) -> PromptTemplate:
        """Register a prompt, or a new version of one.

        A new version never overwrites its predecessor: the old template stays
        readable under ``versions()``, because "what exactly did we ask the
        model in March" is a question an auditor is entitled to ask.
        """
        with self._lock:
            existing = self._current.get(template.prompt_id)
            if existing is not None and existing.version == template.version \
                    and existing.template != template.template:
                raise ValueError(
                    f"Prompt '{template.prompt_id}' version {template.version} "
                    f"already exists with different text — bump the version")
            self._versions.setdefault(template.prompt_id, [])
            if existing is None or template.version >= existing.version:
                self._current[template.prompt_id] = template
            if not any(v.version == template.version
                       for v in self._versions[template.prompt_id]):
                self._versions[template.prompt_id].append(template)
                self._versions[template.prompt_id].sort(key=lambda t: t.version)
        if record:
            self._record({"prompt_id": template.prompt_id,
                          "version": template.version, "action": "registered",
                          "actor": actor, "owner": template.owner,
                          "at": now_iso()})
        return template

    # ------------------------------------------------------------- access
    def get(self, prompt_id: str, version: int | None = None) -> PromptTemplate:
        with self._lock:
            if prompt_id not in self._current:
                raise PromptNotFound(f"No prompt registered as '{prompt_id}'")
            if version is None:
                return self._current[prompt_id]
            for template in self._versions.get(prompt_id, []):
                if template.version == version:
                    return template
        raise PromptNotFound(f"Prompt '{prompt_id}' has no version {version}")

    def render(self, prompt_id: str, version: int | None = None,
               **values: Any) -> str:
        """The call site every piece of business logic uses."""
        return self.get(prompt_id, version).render(**values)

    def has(self, prompt_id: str) -> bool:
        with self._lock:
            return prompt_id in self._current

    def versions(self, prompt_id: str) -> list[PromptTemplate]:
        with self._lock:
            return list(self._versions.get(prompt_id, []))

    def domain(self, domain: str) -> list[PromptTemplate]:
        with self._lock:
            return [t for t in self._current.values() if t.domain == domain]

    # ------------------------------------------------------------ history
    def _record(self, entry: dict) -> None:
        with self._lock:
            self._history.append(entry)
            del self._history[:-MAX_HISTORY]
            if self._dir is not None:
                try:
                    (self._dir / "history.json").write_text(
                        json.dumps(self._history, ensure_ascii=False, indent=2),
                        encoding="utf-8")
                except OSError:  # history is observability, not truth
                    logger.warning("Prompt history persistence failed")

    def _read_history(self) -> list[dict]:
        path = (self._dir / "history.json") if self._dir else None
        if path is None or not path.exists():
            return []
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001 — a corrupt log never blocks startup
            return []

    def history(self, prompt_id: str = "", limit: int = 50) -> list[dict]:
        with self._lock:
            items = list(self._history)
        if prompt_id:
            items = [h for h in items if h["prompt_id"] == prompt_id]
        return list(reversed(items))[:limit]

    # --------------------------------------------------------- inspection
    def describe(self) -> list[dict]:
        with self._lock:
            templates = list(self._current.values())
        return sorted((t.describe() for t in templates), key=lambda t: t["id"])

    def status(self) -> dict:
        with self._lock:
            templates = list(self._current.values())
        by_domain: dict[str, int] = {}
        for t in templates:
            by_domain[t.domain] = by_domain.get(t.domain, 0) + 1
        return {"total": len(templates), "by_domain": by_domain,
                "governed": sum(1 for t in templates if t.governed),
                "versioned": sum(1 for pid in self._versions
                                 if len(self._versions[pid]) > 1),
                "owners": sorted({t.owner for t in templates}),
                "changes": len(self._history)}
