"""Email intelligence — turn a mailbox into enterprise knowledge (Phase 2 #12).

Given email summaries from *any* :class:`EmailProvider` (Gmail, Outlook, …) this
service extracts the structured signal an analyst would: category, the business
entities named (banks, PSPs, products, merchants, incident/RCA ids), action
items, decisions, approvals, blockers and deadlines. Extraction is deterministic
and evidence-based — it only reports what the text actually contains, so nothing
is fabricated (Phase 2 "never hallucinate"). The matched entities are the hook
that links an email to the rest of the Brain (reports, incidents, the knowledge
graph).

It also drafts email *from business context* rather than from a fixed template:
:meth:`draft` composes a professional message out of the real figures/evidence
it is given, so a generated email always references actual data.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Lightweight, explainable classifiers. Each category is a set of trigger terms;
# the winner is the category with the most hits (ties broken by declaration
# order, most operationally urgent first).
# ---------------------------------------------------------------------------
_CATEGORY_TERMS: list[tuple[str, tuple[str, ...]]] = [
    ("incident", ("incident", "outage", "sev-1", "sev-2", "sev 1", "sev 2",
                  "down", "degradation", "rca", "postmortem", "bridge")),
    ("escalation", ("escalate", "escalation", "urgent", "critical",
                    "immediate", "asap", "priority")),
    ("risk_compliance", ("risk", "fraud", "compliance", "breach", "audit",
                         "regulatory", "rbi", "npci circular", "chargeback")),
    ("approval", ("approve", "approval", "sign-off", "sign off", "go-ahead",
                  "authorised", "authorized", "approved")),
    ("settlement", ("settlement", "settle", "reconciliation", "recon",
                    "payout", "nodal")),
    ("merchant", ("merchant", "onboarding", "soundbox", "mid ", "gmv")),
    ("report", ("report", "review", "summary", "kpi", "dashboard", "metrics",
                "weekly", "monthly", "quarterly")),
    ("meeting", ("meeting", "call", "sync", "agenda", "minutes", "invite",
                 "calendar", "reschedule")),
]

# Action / decision / deadline cue phrases, matched at sentence granularity.
_ACTION_CUES = ("please", "kindly", "action item", "action:", "to do", "todo",
                "need to", "needs to", "we should", "can you", "could you",
                "follow up", "follow-up", "ensure", "make sure", "required to",
                "let's", "lets ", "await", "awaiting", "pending")
_DECISION_CUES = ("approved", "we decided", "decision", "agreed", "sign-off",
                  "signed off", "go-ahead", "green light", "confirmed",
                  "will proceed", "rejected", "declined")
_BLOCKER_CUES = ("blocked", "blocker", "stuck", "waiting on", "dependency",
                 "cannot proceed", "held up", "at risk", "delayed")
_RISK_CUES = ("risk", "fraud", "breach", "sla", "outage", "penalty", "exposure",
              "non-compliance", "vulnerability", "escalating")
_DEADLINE_RE = re.compile(
    r"\b(?:by|before|due|eod|eob|no later than)\b[^.\n]{0,40}"
    r"(?:today|tomorrow|tonight|"
    r"mon(?:day)?|tue(?:sday)?|wed(?:nesday)?|thu(?:rsday)?|fri(?:day)?|"
    r"sat(?:urday)?|sun(?:day)?|"
    r"\d{1,2}(?:st|nd|rd|th)?\s*(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|"
    r"nov|dec)[a-z]*|\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?)",
    re.IGNORECASE)
_ID_RE = re.compile(r"\b(?:INC|RCA|DEC|TASK|SOP|MID|PRD|EMP)-[A-Z0-9-]+\b")
_URGENCY_TERMS = ("urgent", "critical", "asap", "immediate", "sev-1", "sev-2",
                  "escalate", "outage", "breach")


def _sentences(text: str) -> list[str]:
    # Unwrap hard-wrapped prose: a newline that continues a lowercase sentence
    # (no sentence punctuation before it) is joined, so word-wrapped email
    # bodies aren't fragmented — while list items (blank lines, bullets, a new
    # capitalised line) still break into separate sentences.
    unwrapped = re.sub(r"([^.!?:•\n])\n(?=[a-z0-9])", r"\1 ", text or "")
    parts = re.split(r"(?<=[.!?])\s+|\n+", unwrapped)
    return [s.strip() for s in parts if len(s.strip()) > 3]


@dataclass
class EmailInsight:
    email_id: str
    subject: str
    sender: str
    received: str
    channel: str
    category: str
    priority: str
    entities: list[str] = field(default_factory=list)
    action_items: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    deadlines: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return self.__dict__.copy()


class EmailIntelligence:
    """Deterministic, evidence-based analysis of email as enterprise knowledge.

    ``vocabulary`` is an optional iterable of known business-entity names (banks,
    PSPs, products, merchants) — when provided, the analyzer links emails to
    those entities. It is injected from the container so the same names the rest
    of the Brain uses drive the linking; the service works without it too.
    """

    def __init__(self, vocabulary: list[str] | None = None):
        self._vocab = sorted({v for v in (vocabulary or []) if v},
                             key=len, reverse=True)

    # -- single email ----------------------------------------------------
    def analyze(self, email: dict) -> dict:
        subject = str(email.get("subject", ""))
        body = str(email.get("body") or email.get("preview") or "")
        text = f"{subject}\n{body}"
        low = text.lower()

        category = self._categorize(low)
        entities = self._entities(text)
        actions = self._match_sentences(text, _ACTION_CUES)
        decisions = self._match_sentences(text, _DECISION_CUES)
        blockers = self._match_sentences(text, _BLOCKER_CUES)
        deadlines = sorted({m.group(0).strip()
                            for m in _DEADLINE_RE.finditer(text)})
        risks = self._match_sentences(text, _RISK_CUES)
        priority = self._priority(low, category, bool(deadlines))

        return EmailInsight(
            email_id=str(email.get("id", "")),
            subject=subject, sender=str(email.get("from", "")),
            received=str(email.get("received", "")),
            channel=str(email.get("channel", "")),
            category=category, priority=priority, entities=entities,
            action_items=actions, decisions=decisions, blockers=blockers,
            deadlines=deadlines, risks=risks,
        ).to_dict()

    def analyze_many(self, emails: list[dict]) -> list[dict]:
        return [self.analyze(e) for e in emails]

    # -- helpers ---------------------------------------------------------
    def _categorize(self, low: str) -> str:
        best, best_hits = "general", 0
        for name, terms in _CATEGORY_TERMS:
            hits = sum(1 for t in terms if t in low)
            if hits > best_hits:
                best, best_hits = name, hits
        return best

    def _entities(self, text: str) -> list[str]:
        found: list[str] = []
        low = text.lower()
        for name in self._vocab:
            if name.lower() in low and name not in found:
                found.append(name)
        for m in _ID_RE.finditer(text):
            if m.group(0) not in found:
                found.append(m.group(0))
        return found

    @staticmethod
    def _match_sentences(text: str, cues: tuple[str, ...]) -> list[str]:
        out: list[str] = []
        for s in _sentences(text):
            sl = s.lower()
            if any(cue in sl for cue in cues):
                clean = s.strip(" -•\t")
                if clean and clean not in out:
                    out.append(clean[:240])
        return out[:8]

    @staticmethod
    def _priority(low: str, category: str, has_deadline: bool) -> str:
        if category in ("incident", "escalation") or \
                any(t in low for t in _URGENCY_TERMS):
            return "high"
        if category in ("risk_compliance", "settlement") or has_deadline:
            return "medium"
        return "low"

    # -- drafting from business context ---------------------------------
    def draft(self, kind: str, context: dict) -> dict:
        """Compose a professional email grounded in ``context`` (real figures,
        entities, next steps) — never a generic template. Returns a
        ``{to, subject, body}`` draft ready for the approval queue.

        ``context`` keys are all optional: ``recipient_name``, ``entity``,
        ``summary``, ``metrics`` (list of "Label: value"), ``evidence`` (list of
        ref ids), ``actions`` (list), ``sender_name``, ``sender_title``.
        """
        entity = context.get("entity", "the affected service")
        recipient = context.get("recipient_name", "team")
        summary = context.get("summary", "").strip()
        metrics = [str(m) for m in context.get("metrics", []) if str(m).strip()]
        evidence = [str(e) for e in context.get("evidence", []) if str(e).strip()]
        actions = [str(a) for a in context.get("actions", []) if str(a).strip()]
        sender = context.get("sender_name", "")
        title = context.get("sender_title", "")

        subject = _SUBJECTS.get(kind, "{entity} — update").format(entity=entity)
        lines = [f"Hi {recipient},", ""]
        if summary:
            lines += [summary, ""]
        if metrics:
            lines.append("Key figures:")
            lines += [f"  • {m}" for m in metrics]
            lines.append("")
        if actions:
            lines.append("Proposed next steps:")
            lines += [f"  {i}. {a}" for i, a in enumerate(actions, 1)]
            lines.append("")
        if evidence:
            lines.append("Supporting evidence: " + ", ".join(evidence))
            lines.append("")
        lines.append(_CLOSERS.get(kind, "Happy to discuss."))
        lines.append("")
        if sender:
            lines.append(sender + (f"\n{title}" if title else ""))

        body = "\n".join(lines)
        return {
            "to": [r for r in context.get("to", []) if r],
            "subject": subject,
            "body": body,
            "kind": kind,
            "grounded_in": evidence or [e for e in (context.get("entity"),) if e],
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }


_SUBJECTS = {
    "incident_escalation": "[Escalation] {entity} — incident update & next steps",
    "merchant_followup": "{entity} — follow-up on your recent query",
    "management_update": "{entity} — status update for leadership",
    "risk_notification": "[Risk] {entity} — risk notification",
    "weekly_status": "Weekly status — {entity}",
    "meeting_followup": "Follow-up & actions — {entity}",
}
_CLOSERS = {
    "incident_escalation": "We'll keep this thread updated until recovery is "
                           "confirmed.",
    "risk_notification": "Please advise if you'd like to convene a review.",
    "management_update": "Happy to walk through any of this in more detail.",
}
