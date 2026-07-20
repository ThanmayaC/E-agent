"""Enterprise Knowledge Store — persistent, organization-wide learning.

Everything the platform learns that outlives a single project lives here:
business terminology, schema aliases, entity definitions (products, merchants,
customers, ...), business rules, user clarifications, decision history, and
report history. The store makes the system smarter over time: a clarification
answered once is never asked again for a similar dataset.

Persistence is a JSON document per section under ``data/knowledge`` — simple,
inspectable, and swappable for a database later without touching callers.

Every mutation is additionally journaled to ``knowledge_versions`` — an
append-only version history carrying timestamp, source, confidence, version
number, and project origin — so knowledge is never overwritten blindly and
its evolution stays auditable (SDS: Enterprise Brain / Knowledge Versioning).
"""
from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SECTIONS = (
    "terminology",        # term -> {definition, aliases, added_by}
    "schema_aliases",     # raw column/table name -> canonical business name
    "entity_definitions", # entity name -> {kind: product|merchant|customer|..., definition}
    "business_rules",     # [{rule, scope, added_at}]
    "clarifications",     # [{question, answer, signature, project_id, answered_at}]
    "decisions",          # [{decision, context, project_id, decided_at}]
    "report_history",     # [{project_id, title, health_score, generated_at}]
    "learning_events",    # [{event, source, project_id, details, recorded_at}]
    "strategic_insights", # [{insight, horizon, project_id, added_at}]
    "insights",           # [{insight, statement_type, project_id, ...}] extracted from reports
    "recommendations",    # [{action, priority, project_id, ...}] extracted from reports
    "knowledge_versions", # append-only version journal for every mutation
)

# sections stored as key -> entry mappings (the rest are ordered lists)
_DICT_SECTIONS = ("terminology", "schema_aliases", "entity_definitions")


class KnowledgeStore:
    def __init__(self, knowledge_dir: Path):
        self._dir = knowledge_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    # ----------------------------------------------------------- raw I/O
    def _path(self, section: str) -> Path:
        if section not in SECTIONS:
            raise ValueError(f"Unknown knowledge section: {section}")
        return self._dir / f"{section}.json"

    def _read(self, section: str) -> Any:
        path = self._path(section)
        if not path.exists():
            return {} if section in _DICT_SECTIONS else []
        return json.loads(path.read_text(encoding="utf-8"))

    def _write(self, section: str, payload: Any) -> None:
        self._path(section).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8")

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    # -------------------------------------------------- version journal
    def _journal(self, section: str, key: str, payload: Any,
                 previous: Any = None, source: str = "user",
                 confidence: float | None = None, project_id: str = "") -> None:
        """Append one version entry for a knowledge mutation. Must be called
        while holding the lock. History is never rewritten — an update
        produces a new version that records what it superseded."""
        journal = self._read("knowledge_versions")
        version = 1 + sum(1 for e in journal if e.get("key") == key)
        journal.append({
            "key": key, "section": section, "version": version,
            "action": "updated" if previous is not None else "created",
            "payload": payload,
            **({"previous": previous} if previous is not None else {}),
            "source": source,
            **({"confidence": confidence} if confidence is not None else {}),
            "project_id": project_id, "recorded_at": self._now(),
        })
        self._write("knowledge_versions", journal)

    def versions(self, key: str) -> list[dict]:
        """Full version history of one knowledge key, oldest first."""
        return [e for e in self._read("knowledge_versions")
                if e.get("key") == key]

    def history(self, limit: int = 50, section: str = "") -> list[dict]:
        """Most recent knowledge mutations across every section."""
        journal = self._read("knowledge_versions")
        if section:
            journal = [e for e in journal if e.get("section") == section]
        return journal[-limit:]

    # ------------------------------------------------------- terminology
    def add_term(self, term: str, definition: str, aliases: list[str] | None = None,
                 added_by: str = "user", confidence: float | None = None,
                 project_id: str = "") -> None:
        with self._lock:
            terms = self._read("terminology")
            key = term.strip().lower()
            previous = terms.get(key)
            entry = {
                "term": term.strip(), "definition": definition,
                "aliases": [a.strip().lower() for a in (aliases or [])],
                "added_by": added_by, "added_at": self._now(),
            }
            if previous:  # merge, never blindly overwrite: aliases accumulate
                if previous.get("definition") == definition and \
                        set(entry["aliases"]) <= set(previous.get("aliases", [])):
                    return  # nothing new learned — no version churn
                entry["aliases"] = sorted(set(previous.get("aliases", []))
                                          | set(entry["aliases"]))
                entry["first_added_at"] = previous.get("first_added_at",
                                                       previous.get("added_at"))
            terms[key] = entry
            self._write("terminology", terms)
            self._journal("terminology", f"term:{key}", entry, previous,
                          source=added_by, confidence=confidence,
                          project_id=project_id)

    def resolve_term(self, text: str) -> dict | None:
        needle = text.strip().lower()
        terms = self._read("terminology")
        if needle in terms:
            return terms[needle]
        for entry in terms.values():
            if needle in entry.get("aliases", []):
                return entry
        return None

    # ----------------------------------------------------- schema aliases
    def add_schema_alias(self, raw_name: str, canonical: str,
                         source: str = "user", confidence: float | None = None,
                         project_id: str = "") -> None:
        with self._lock:
            aliases = self._read("schema_aliases")
            key = raw_name.strip().lower()
            previous = aliases.get(key)
            if previous == canonical.strip():
                return
            aliases[key] = canonical.strip()
            self._write("schema_aliases", aliases)
            self._journal("schema_aliases", f"alias:{key}", canonical.strip(),
                          previous, source=source, confidence=confidence,
                          project_id=project_id)

    def resolve_schema_alias(self, raw_name: str) -> str | None:
        return self._read("schema_aliases").get(raw_name.strip().lower())

    # -------------------------------------------------- entity definitions
    def define_entity(self, name: str, kind: str, definition: str,
                      source: str = "user", confidence: float | None = None,
                      project_id: str = "") -> None:
        with self._lock:
            entities = self._read("entity_definitions")
            key = name.strip().lower()
            previous = entities.get(key)
            entry = {"name": name.strip(), "kind": kind, "definition": definition,
                     "added_at": self._now()}
            if previous:
                if previous.get("kind") == kind and \
                        previous.get("definition") == definition:
                    return  # already known
                entry["first_added_at"] = previous.get("first_added_at",
                                                       previous.get("added_at"))
            entities[key] = entry
            self._write("entity_definitions", entities)
            self._journal("entity_definitions", f"entity:{key}", entry, previous,
                          source=source, confidence=confidence,
                          project_id=project_id)

    # ------------------------------------------------------ business rules
    def add_rule(self, rule: str, scope: str = "global", source: str = "user",
                 confidence: float | None = None, project_id: str = "") -> None:
        with self._lock:
            rules = self._read("business_rules")
            if any(r.get("rule") == rule and r.get("scope") == scope
                   for r in rules):
                return  # already known
            rules.append({"rule": rule, "scope": scope, "added_at": self._now()})
            self._write("business_rules", rules)
            self._journal("business_rules", f"rule:{rule[:80].strip().lower()}",
                          rules[-1], None, source=source, confidence=confidence,
                          project_id=project_id)

    # ------------------------------------------------------ clarifications
    def remember_clarification(self, question: str, answer: str,
                               signature: str = "", project_id: str = "",
                               kind: str = "", dataset: str = "",
                               confidence_before: float | None = None,
                               aliases: list[str] | None = None) -> None:
        """Store a user clarification so it is never asked again for a
        similar dataset (matched by signature or question similarity).
        Optional metadata records the learning context: the ambiguity kind,
        dataset/business domain, understanding confidence at the time of
        asking, and column aliases the answer establishes for the future."""
        with self._lock:
            items = self._read("clarifications")
            entry = {"question": question, "answer": answer,
                     "signature": signature, "project_id": project_id,
                     "answered_at": self._now()}
            if kind:
                entry["kind"] = kind
            if dataset:
                entry["dataset"] = dataset
            if confidence_before is not None:
                entry["confidence_before"] = confidence_before
            if aliases:
                entry["aliases"] = aliases
            items.append(entry)
            self._write("clarifications", items)
            self._journal("clarifications",
                          f"clarification:{(signature or question)[:80].strip().lower()}",
                          entry, None, source="user",
                          confidence=confidence_before, project_id=project_id)

    def find_clarification(self, question: str, signature: str = "") -> dict | None:
        needle = set(question.lower().split())
        best, best_overlap = None, 0.0
        for item in self._read("clarifications"):
            if signature and item.get("signature") == signature \
                    and item["question"].lower() == question.lower():
                return item
            words = set(item["question"].lower().split())
            overlap = len(needle & words) / max(len(needle | words), 1)
            if overlap > best_overlap:
                best, best_overlap = item, overlap
        return best if best_overlap >= 0.6 else None

    # ------------------------------------------------------------ history
    def record_decision(self, decision: str, context: str = "",
                        project_id: str = "", source: str = "user") -> None:
        with self._lock:
            items = self._read("decisions")
            entry = {"decision": decision, "context": context,
                     "project_id": project_id, "decided_at": self._now()}
            items.append(entry)
            self._write("decisions", items)
            self._journal("decisions", f"decision:{decision[:80].strip().lower()}",
                          entry, None, source=source, project_id=project_id)

    def decisions(self, limit: int = 20) -> list[dict]:
        return self._read("decisions")[-limit:]

    def record_report(self, project_id: str, title: str, health_score: float) -> None:
        with self._lock:
            items = self._read("report_history")
            entry = {"project_id": project_id, "title": title,
                     "health_score": health_score, "generated_at": self._now()}
            items.append(entry)
            self._write("report_history", items)
            self._journal("report_history", f"report:{project_id}", entry, None,
                          source="report_generation", project_id=project_id)

    def report_history(self, limit: int = 20) -> list[dict]:
        return self._read("report_history")[-limit:]

    # --------------------------------------------------- learning memory
    def record_learning_event(self, event: str, source: str = "pipeline",
                              project_id: str = "",
                              details: dict | None = None) -> None:
        """One continuous-learning execution (what was learned, from where)."""
        with self._lock:
            items = self._read("learning_events")
            items.append({"event": event, "source": source,
                          "project_id": project_id, "details": details or {},
                          "recorded_at": self._now()})
            self._write("learning_events", items)

    def learning_history(self, limit: int = 50) -> list[dict]:
        return self._read("learning_events")[-limit:]

    # -------------------------------------------------- strategic memory
    def add_strategic_insight(self, insight: str, horizon: str = "long_term",
                              project_id: str = "",
                              source: str = "pipeline") -> None:
        with self._lock:
            items = self._read("strategic_insights")
            if any(i.get("insight") == insight for i in items):
                return
            entry = {"insight": insight, "horizon": horizon,
                     "project_id": project_id, "added_at": self._now()}
            items.append(entry)
            self._write("strategic_insights", items)
            self._journal("strategic_insights",
                          f"strategic:{insight[:80].strip().lower()}", entry,
                          None, source=source, project_id=project_id)

    def strategic_insights(self, limit: int = 20) -> list[dict]:
        return self._read("strategic_insights")[-limit:]

    # ------------------------------------- extracted insights / actions
    def record_insight(self, insight: str, statement_type: str = "",
                       project_id: str = "", confidence: float | None = None,
                       evidence_ids: list[str] | None = None,
                       source: str = "report") -> None:
        with self._lock:
            items = self._read("insights")
            if any(i.get("insight") == insight and
                   i.get("project_id") == project_id for i in items):
                return
            entry = {"insight": insight, "statement_type": statement_type,
                     "project_id": project_id,
                     **({"confidence": confidence} if confidence is not None else {}),
                     "evidence_ids": evidence_ids or [],
                     "recorded_at": self._now()}
            items.append(entry)
            self._write("insights", items)
            self._journal("insights", f"insight:{insight[:80].strip().lower()}",
                          entry, None, source=source, confidence=confidence,
                          project_id=project_id)

    def insights(self, limit: int = 20) -> list[dict]:
        return self._read("insights")[-limit:]

    def record_recommendation(self, action: str, priority: int | None = None,
                              project_id: str = "", source: str = "report",
                              evidence_ids: list[str] | None = None) -> None:
        with self._lock:
            items = self._read("recommendations")
            if any(r.get("action") == action and
                   r.get("project_id") == project_id for r in items):
                return
            entry = {"action": action,
                     **({"priority": priority} if priority is not None else {}),
                     "project_id": project_id, "evidence_ids": evidence_ids or [],
                     "recorded_at": self._now()}
            items.append(entry)
            self._write("recommendations", items)
            self._journal("recommendations",
                          f"recommendation:{action[:80].strip().lower()}",
                          entry, None, source=source, project_id=project_id)

    def recommendations(self, limit: int = 20) -> list[dict]:
        return self._read("recommendations")[-limit:]

    # ------------------------------------------------------------- search
    def search(self, query: str, limit: int = 10) -> list[dict]:
        """Naive keyword search across every section (good enough until the
        knowledge base is large enough to warrant embeddings)."""
        words = [w for w in query.lower().split() if len(w) > 2]
        hits: list[dict] = []
        for section in SECTIONS:
            if section == "knowledge_versions":  # journal would only duplicate
                continue
            payload = self._read(section)
            items = list(payload.values()) if isinstance(payload, dict) else payload
            for item in items:
                text = json.dumps(item, default=str).lower()
                if any(w in text for w in words):
                    hits.append({"section": section, **item})
        return hits[:limit]

    def snapshot(self) -> dict[str, Any]:
        """Full knowledge dump for the Knowledge Explorer UI."""
        return {section: self._read(section) for section in SECTIONS}

    def stats(self) -> dict[str, int]:
        """Per-section entry counts (Enterprise Brain statistics)."""
        out: dict[str, int] = {}
        for section in SECTIONS:
            payload = self._read(section)
            out[section] = len(payload)
        return out

    def context_for_reasoning(self, max_items: int = 15) -> dict[str, Any]:
        """Compact slice of enterprise knowledge injected into prompts."""
        terms = self._read("terminology")
        return {
            "terminology": list(terms.values())[:max_items],
            "business_rules": self._read("business_rules")[-max_items:],
            "clarifications": [
                {"question": c["question"], "answer": c["answer"]}
                for c in self._read("clarifications")[-max_items:]
            ],
        }
