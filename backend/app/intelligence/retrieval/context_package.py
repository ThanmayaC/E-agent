"""Context package assembly — the last mile of the RAG path.

Retrieval returns ranked chunks; a language model needs a *prompt*. This module
is the bridge, and it is where most naive RAG implementations lose their
accuracy. It does five things a plain ``"\\n".join(chunks)`` does not:

1. **Token budgeting** — the package is built to fit a caller-supplied budget.
   Passages are admitted whole where possible and truncated on a sentence
   boundary when partially admitted, so the model never reads half a number.
2. **Near-duplicate suppression** — enterprise corpora repeat themselves (a
   daily report restates yesterday's incident). Duplicate passages burn budget
   and bias the model by sheer repetition; they are dropped by Jaccard overlap.
3. **Per-source diversity caps** — one long document can otherwise occupy the
   whole window and crowd out the corroborating source.
4. **Lost-in-the-middle ordering** — models attend most strongly to the start
   and end of a long context, so the strongest passages are placed at the edges
   and the weakest in the middle.
5. **Stable numbered citations** — every passage is labelled ``[n]`` and mapped
   back to its source, so a claim can be traced and the answer validated
   against what was actually retrieved.

The output is provider-agnostic: a prompt-ready string plus the structures the
governance and validation layers need. Nothing here calls an LLM.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Iterable

from app.intelligence.retrieval.bm25 import tokenize
from app.intelligence.retrieval.hybrid import RetrievedChunk

# Average characters per token across English business prose. Deliberately a
# conservative estimate: over-estimating tokens keeps the package inside the
# real window, and callers with a true tokenizer can override it.
CHARS_PER_TOKEN = 4.0

_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def estimate_tokens(text: str, chars_per_token: float = CHARS_PER_TOKEN) -> int:
    """Cheap, dependency-free token estimate."""
    return int(len(text) / chars_per_token) + 1


@dataclass
class ContextPassage:
    """One cited passage admitted into the package."""
    marker: int                 # the [n] the model sees
    chunk_id: str
    title: str
    kind: str
    ref: str
    text: str
    tokens: int
    truncated: bool = False
    score: float = 0.0

    def citation(self) -> dict[str, Any]:
        return {"marker": self.marker, "id": self.chunk_id, "title": self.title,
                "kind": self.kind, "ref": self.ref, "truncated": self.truncated,
                "score": round(self.score, 4)}


@dataclass
class ContextPackage:
    """Everything the model — and the auditor — needs about one retrieval."""
    prompt: str
    passages: list[ContextPassage] = field(default_factory=list)
    diagnostics: dict[str, Any] = field(default_factory=dict)

    @property
    def tokens(self) -> int:
        return sum(p.tokens for p in self.passages)

    @property
    def is_empty(self) -> bool:
        return not self.passages

    def citations(self) -> list[dict[str, Any]]:
        return [p.citation() for p in self.passages]

    def source_for(self, marker: int) -> ContextPassage | None:
        """Resolve a ``[n]`` the model emitted back to its source passage."""
        return next((p for p in self.passages if p.marker == marker), None)

    def cited_markers(self, answer: str) -> list[int]:
        """Markers the answer actually cites — the basis for a grounding check."""
        found = {int(m) for m in re.findall(r"\[(\d{1,3})\]", answer or "")}
        return sorted(m for m in found if self.source_for(m))

    def to_dict(self) -> dict[str, Any]:
        return {"prompt": self.prompt, "tokens": self.tokens,
                "citations": self.citations(), "diagnostics": self.diagnostics}


class ContextAssembler:
    """Assembles retrieved chunks into a budgeted, cited context package.

    ``token_budget`` is the space reserved for evidence only — the caller keeps
    its own room for the system prompt, question and answer.
    """

    def __init__(self, token_budget: int = 3000, *,
                 max_per_source: int = 3,
                 dedupe_threshold: float = 0.85,
                 min_passage_tokens: int = 40,
                 chars_per_token: float = CHARS_PER_TOKEN):
        self.token_budget = token_budget
        self.max_per_source = max_per_source
        self.dedupe_threshold = dedupe_threshold
        self.min_passage_tokens = min_passage_tokens
        self.chars_per_token = chars_per_token

    # ------------------------------------------------------------- assemble
    def assemble(self, chunks: Iterable[RetrievedChunk], *,
                 query: str = "",
                 retrieval_diagnostics: dict[str, Any] | None = None,
                 header: str = "") -> ContextPackage:
        admitted: list[ContextPassage] = []
        seen_tokens: list[set[str]] = []
        per_source: dict[str, int] = {}
        used = 0
        dropped_duplicate = dropped_source_cap = dropped_budget = 0

        for chunk in chunks:
            text = _clean(chunk.text)
            if not text:
                continue

            source = str(chunk.payload.get("ref") or chunk.payload.get("title")
                         or chunk.id)
            if per_source.get(source, 0) >= self.max_per_source:
                dropped_source_cap += 1
                continue

            terms = set(tokenize(text))
            if any(_jaccard(terms, prev) >= self.dedupe_threshold
                   for prev in seen_tokens):
                dropped_duplicate += 1
                continue

            remaining = self.token_budget - used
            if remaining < self.min_passage_tokens:
                dropped_budget += 1
                continue

            tokens = estimate_tokens(text, self.chars_per_token)
            truncated = False
            if tokens > remaining:
                text = _truncate_to_tokens(text, remaining, self.chars_per_token)
                if not text:
                    dropped_budget += 1
                    continue
                tokens = estimate_tokens(text, self.chars_per_token)
                truncated = True

            admitted.append(ContextPassage(
                marker=0,  # assigned after ordering
                chunk_id=chunk.id,
                title=str(chunk.payload.get("title", "")),
                kind=str(chunk.payload.get("kind", "")),
                ref=str(chunk.payload.get("ref", "")),
                text=text, tokens=tokens, truncated=truncated,
                score=(chunk.rerank_score if chunk.rerank_score is not None
                       else chunk.fused_score)))
            seen_tokens.append(terms)
            per_source[source] = per_source.get(source, 0) + 1
            used += tokens

        ordered = _edge_weighted(admitted)
        for i, passage in enumerate(ordered, start=1):
            passage.marker = i

        diagnostics = {
            "query": query,
            "passages": len(ordered),
            "tokens_used": used,
            "token_budget": self.token_budget,
            "budget_utilisation": (round(used / self.token_budget, 3)
                                   if self.token_budget else 0.0),
            "dropped_duplicate": dropped_duplicate,
            "dropped_source_cap": dropped_source_cap,
            "dropped_budget": dropped_budget,
            "truncated_passages": sum(1 for p in ordered if p.truncated),
            "distinct_sources": len(per_source),
            "ordering": "edge_weighted",
        }
        if retrieval_diagnostics:
            diagnostics["retrieval"] = retrieval_diagnostics

        return ContextPackage(prompt=_render(ordered, header),
                              passages=ordered, diagnostics=diagnostics)


# ------------------------------------------------------------------ helpers
def _clean(text: str) -> str:
    return re.sub(r"[ \t]*\n[ \t]*", "\n", (text or "").strip())


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


_ELLIPSIS = " […]"


def _truncate_to_tokens(text: str, budget_tokens: int,
                        chars_per_token: float) -> str:
    """Cut to the last complete sentence that fits, so a passage never ends
    mid-figure. Falls back to a hard character cut when there is no sentence
    boundary inside the budget.

    Guarantees ``estimate_tokens(result) <= budget_tokens``: the character
    limit reserves room for both the ellipsis marker and the rounding-up term
    in :func:`estimate_tokens`, without which a truncated passage could push
    the package a token or two over its budget."""
    limit = int((budget_tokens - 1) * chars_per_token) - len(_ELLIPSIS)
    if limit <= 0:
        return ""
    if len(text) <= limit:
        return text
    head = text[:limit]
    sentences = _SENTENCE_END.split(head)
    if len(sentences) > 1:
        kept = " ".join(sentences[:-1]).strip()
        if kept:
            return kept + _ELLIPSIS
    return head.rstrip() + _ELLIPSIS


def _edge_weighted(passages: list[ContextPassage]) -> list[ContextPassage]:
    """Mitigate lost-in-the-middle: strongest passages at the start and end,
    weakest buried in the middle. Input is assumed relevance-ordered."""
    if len(passages) < 3:
        return list(passages)
    front: list[ContextPassage] = []
    back: list[ContextPassage] = []
    for i, p in enumerate(passages):
        (front if i % 2 == 0 else back).append(p)
    back.reverse()
    return front + back


def _render(passages: list[ContextPassage], header: str) -> str:
    if not passages:
        return ""
    lines = [header.strip()] if header.strip() else []
    for p in passages:
        label = p.title or p.ref or p.chunk_id
        meta = " · ".join(x for x in (p.kind, p.ref) if x)
        lines.append(f"[{p.marker}] {label}" + (f"  ({meta})" if meta else ""))
        lines.append(p.text)
        lines.append("")
    return "\n".join(lines).strip()


DEFAULT_HEADER = (
    "Evidence retrieved from enterprise sources. Each passage is numbered; "
    "cite the passages you rely on as [n]. If the evidence does not support an "
    "answer, say so — do not infer beyond it."
)
