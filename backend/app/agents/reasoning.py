"""AI Reasoning Engine.

Business context JSON → generated prompt → LLM provider → validated
structured output. Prompts are produced by the PromptGenerationAgent (never
hardcoded here); when no provider is configured or the call fails, the result
is explicitly marked unavailable — the platform never substitutes template
narrative.
"""
from __future__ import annotations

from typing import Any

from app.agents.prompt_generator import PromptGenerationAgent
from app.core.logging import get_logger
from app.domain.entities import AIReport
from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMError

logger = get_logger(__name__)

AI_UNAVAILABLE = (
    "AI reasoning is not available: no LLM provider is configured or the provider "
    "is unreachable. Deterministic analytics remain fully available. Configure "
    "EDIP_LLM_PROVIDER (ollama / openai / azure-openai / anthropic / gemini / enterprise)."
)


class AIReasoningEngine:
    def __init__(self, provider: BaseLLMProvider | None,
                 prompt_agent: PromptGenerationAgent | None = None,
                 fallback: BaseLLMProvider | None = None):
        self.provider = provider
        self.fallback = fallback
        self.prompt_agent = prompt_agent or PromptGenerationAgent()

    # ------------------------------------------------------------- report
    def generate_report(self, context: dict[str, Any]) -> AIReport:
        if self.provider is None:
            return AIReport(status="unavailable", error=AI_UNAVAILABLE)
        prompt = self.prompt_agent.report_prompt(context)
        messages = [ChatMessage("system", prompt.system),
                    ChatMessage("user", prompt.user)]
        last_error = ""
        # primary (with its own retries), then the configured fallback —
        # never a fabricated report
        for provider in [p for p in (self.provider, self.fallback) if p]:
            try:
                raw = provider.chat_json(messages)
                report = self._validate(raw)
                self._verify_evidence(report, self._collect_evidence_ids(context))
                report.provider = provider.name
                report.model = getattr(provider, "model", provider.config.model)
                report.prompt_confidence = prompt.confidence
                report.clarification_questions = prompt.clarification_questions
                return report
            except (LLMError, Exception) as exc:  # noqa: BLE001 — must degrade gracefully
                logger.exception("AI reasoning failed on provider %s", provider.name)
                last_error = f"{provider.name}: {str(exc)[:400]}"
        return AIReport(status="failed", error=last_error,
                        provider=self.provider.name)

    # ------------------------------------------------------------ copilot
    def answer(self, question: str, context: dict[str, Any],
               conversation: list[dict] | None = None) -> dict[str, Any]:
        if self.provider is None:
            return {"status": "unavailable", "answer": AI_UNAVAILABLE,
                    "cited_facts": [], "confidence": 0.0}
        prompt = self.prompt_agent.copilot_prompt(question, context, conversation)
        try:
            raw = self.provider.chat_json([
                ChatMessage("system", prompt.system),
                ChatMessage("user", prompt.user),
            ])
            return {
                "status": "ok",
                "answer": str(raw.get("answer", "")).strip() or "(empty answer)",
                "cited_facts": [str(f) for f in raw.get("cited_facts", [])][:10],
                "confidence": float(raw.get("confidence") or 0.0),
                "provider": self.provider.name,
                "model": getattr(self.provider, "model", self.provider.config.model),
            }
        except (LLMError, Exception) as exc:  # noqa: BLE001
            logger.exception("Copilot reasoning failed")
            return {"status": "failed", "answer": f"AI reasoning failed: {exc}",
                    "cited_facts": [], "confidence": 0.0}

    # ------------------------------------------------- evidence verification
    STATEMENT_TYPES = {"fact", "statistical_finding", "hypothesis", "unknown"}

    @classmethod
    def _collect_evidence_ids(cls, node: Any) -> set[str]:
        """Every citable id present in the structured evidence: KPI ids,
        signal ids, forecast:<kpi_id>, quality ids, ..."""
        ids: set[str] = set()
        if isinstance(node, dict):
            v = node.get("id")
            if isinstance(v, str) and v:
                ids.add(v)
            for child in node.values():
                ids |= cls._collect_evidence_ids(child)
        elif isinstance(node, list):
            for child in node:
                ids |= cls._collect_evidence_ids(child)
        return ids

    @classmethod
    def _verify_evidence(cls, report: AIReport, valid_ids: set[str]) -> None:
        """Deterministic guardrail: every generated statement is checked
        against the evidence it cites. Citations that do not exist in the
        supplied evidence are removed; a 'fact' or 'statistical_finding' left
        without any verified citation is downgraded to a labelled hypothesis —
        an unsupported claim can never be presented as fact."""
        for item in report.key_insights:
            cls._check_item(item, valid_ids)
        for item in report.root_causes:
            cls._check_item(item, valid_ids)
            item["statement_type"] = "hypothesis"  # causes are never facts
            item.setdefault("missing_evidence", "Not specified by the model.")
        for section in (report.risks, report.opportunities, report.recommendations):
            for item in section:
                cls._check_item(item, valid_ids, default_type=None)

    @classmethod
    def _check_item(cls, item: dict, valid_ids: set[str],
                    default_type: str | None = "hypothesis") -> None:
        if not isinstance(item, dict):
            return
        cited = item.get("evidence_ids")
        cited = [str(e) for e in cited] if isinstance(cited, list) else []
        verified = [e for e in cited if e in valid_ids]
        rejected = [e for e in cited if e not in valid_ids]
        item["evidence_ids"] = verified
        if rejected:
            item["rejected_evidence_ids"] = rejected
        item["verification"] = "evidence_verified" if verified else "unverified"
        if default_type is None:
            return  # sections without statement_type semantics
        stype = str(item.get("statement_type", "")).strip().lower().replace(" ", "_")
        if stype == "statistical":
            stype = "statistical_finding"
        if stype not in cls.STATEMENT_TYPES:
            stype = default_type
        # an unverified claim may only exist as hypothesis or unknown
        if not verified and stype in ("fact", "statistical_finding"):
            stype = "hypothesis"
            try:
                item["confidence"] = min(float(item.get("confidence") or 0.4), 0.4)
            except (TypeError, ValueError):
                item["confidence"] = 0.4
        item["statement_type"] = stype

    # ----------------------------------------------------------- validate
    @staticmethod
    def _validate(raw: dict[str, Any]) -> AIReport:
        def as_str(v: Any) -> str:
            return v if isinstance(v, str) else str(v or "")

        def as_dicts(v: Any, primary_key: str) -> list[dict]:
            """Normalize a section to a list of dicts so the UI/markdown can
            rely on a uniform shape whatever the model emitted."""
            if not isinstance(v, list):
                v = [v] if v else []
            out = []
            for item in v:
                if isinstance(item, dict):
                    out.append(item)
                elif item:
                    out.append({primary_key: str(item)})
            return out

        def as_strs(v: Any, limit: int = 8) -> list[str]:
            if not isinstance(v, list):
                v = [v] if v else []
            return [a if isinstance(a, str)
                    else str(a.get("action", a)) if isinstance(a, dict) else str(a)
                    for a in v if a][:limit]

        priority_actions = as_strs(raw.get("priority_actions"))

        return AIReport(
            status="ok",
            executive_summary=as_str(raw.get("executive_summary")),
            portfolio_health=as_str(raw.get("portfolio_health")),
            key_insights=as_dicts(raw.get("key_insights"), "title"),
            root_causes=as_dicts(raw.get("root_causes"), "problem"),
            risks=as_dicts(raw.get("risks"), "risk"),
            opportunities=as_dicts(raw.get("opportunities"), "opportunity"),
            recommendations=as_dicts(raw.get("recommendations"), "action"),
            priority_actions=priority_actions,
            data_limitations=as_strs(raw.get("data_limitations"), limit=12),
            management_commentary=as_str(raw.get("management_commentary")),
            next_investigation_areas=as_strs(raw.get("next_investigation_areas")),
            confidence_explanation=as_str(raw.get("confidence_explanation")),
            confidence=float(raw.get("confidence") or 0.0),
        )
