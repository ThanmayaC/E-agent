"""Enterprise Search — one question, every surface the platform holds.

    knowledge · memory · projects · reports · tasks · portfolio
    business rules · clarifications · recommendations · organization

Each surface is searched by the component that owns it — the Knowledge Store
searches knowledge, the task manager owns tasks — and this module composes the
answers. It reindexes nothing and duplicates nothing: a search layer with its
own copy of the truth is a second truth to keep current.

Ranking is deterministic and explainable: every hit says which surface it came
from, why it matched, and how strongly. Exact matches beat prefix matches beat
substring matches; a term appearing in a title beats the same term buried in a
body. When embeddings are available the organizational model is *also* searched
by meaning, and semantic hits are merged in rather than replacing keyword hits
— an executive searching "merchant fees" should not lose the rule that says
"Merchant Fee" because a vector was fashionable.

A surface that fails is reported as unavailable and the rest of the search
still answers. Search degrades; it does not go dark.
"""
from __future__ import annotations

import json
import re
from typing import Any, Callable

from app.core.logging import get_logger

logger = get_logger(__name__)

SURFACES = ("knowledge", "memory", "projects", "reports", "tasks",
            "portfolio", "business_rules", "clarifications",
            "recommendations", "organization", "documents")

MAX_PER_SURFACE = 10
MIN_TERM_LENGTH = 2
# The chunk vector collection Document Intelligence embeds into. Searching it
# is what lets an enterprise question reach SOPs, RCAs, meeting notes,
# policies, reports, and the synthetic email/Teams corpus — the document body,
# not just its title.
DOCUMENT_COLLECTION = "_documents"
DOCUMENT_CHUNK_KIND = "document_chunk"


class EnterpriseSearch:
    """Unified search across everything the enterprise knows."""

    def __init__(self, knowledge, artifacts, organization, relationships,
                 tasks=None, portfolio=None, embedder=None,
                 vector_store_for=None, documents=None):
        self._knowledge = knowledge
        self._artifacts = artifacts
        self._org = organization
        self._relationships = relationships
        self._tasks = tasks
        self._portfolio = portfolio
        self._embedder = embedder
        self._vector_store_for = vector_store_for
        # Document Intelligence, when wired: gives the documents surface a
        # ready-made semantic search over the chunk collection. Absent, the
        # surface falls back to embedding here directly. Either way it degrades
        # rather than failing.
        self._documents = documents

    # -------------------------------------------------------------- search
    def search(self, query: str, surfaces: list[str] | None = None,
               limit: int = 30, semantic: bool = True) -> dict[str, Any]:
        """Search every surface (or the named ones) and return ranked hits."""
        terms = _terms(query)
        if not terms:
            return {"query": query, "results": [], "total": 0,
                    "surfaces_searched": [], "unavailable": [],
                    "note": "a search needs a term of at least "
                            f"{MIN_TERM_LENGTH} characters"}

        wanted = [s for s in (surfaces or SURFACES) if s in SURFACES]
        searchers: dict[str, Callable[[list[str]], list[dict]]] = {
            "knowledge": self._search_knowledge,
            "memory": self._search_memory,
            "projects": self._search_projects,
            "reports": self._search_reports,
            "tasks": self._search_tasks,
            "portfolio": self._search_portfolio,
            "business_rules": self._search_rules,
            "clarifications": self._search_clarifications,
            "recommendations": self._search_recommendations,
            "organization": self._search_organization,
            "documents": self._search_documents,
        }

        results: list[dict] = []
        searched, unavailable = [], []
        for surface in wanted:
            try:
                hits = searchers[surface](terms)
                results.extend(hits[:MAX_PER_SURFACE])
                searched.append(surface)
            except Exception as exc:  # noqa: BLE001 — one surface never darkens search
                logger.exception("Enterprise search failed on surface %s",
                                 surface)
                unavailable.append({"surface": surface,
                                    "reason": str(exc)[:150]})

        if semantic and "organization" in wanted:
            semantic_hits, note = self._search_semantic(query, terms)
            results = _merge(results, semantic_hits)
        else:
            note = ""

        results.sort(key=lambda hit: hit["score"], reverse=True)
        by_surface: dict[str, int] = {}
        for hit in results:
            by_surface[hit["surface"]] = by_surface.get(hit["surface"], 0) + 1

        return {"query": query, "terms": terms, "total": len(results),
                "results": results[:limit], "by_surface": by_surface,
                "surfaces_searched": searched, "unavailable": unavailable,
                **({"note": note} if note else {})}

    # ------------------------------------------------------------ surfaces
    def _search_knowledge(self, terms: list[str]) -> list[dict]:
        """Terminology, aliases, and entity definitions — the Knowledge Store
        owns this search; we rank and label what it returns."""
        hits = []
        for item in self._knowledge.search(" ".join(terms), limit=40):
            section = item.get("section", "knowledge")
            if section in ("business_rules", "clarifications",
                           "recommendations"):
                continue  # those surfaces answer for themselves, below
            title = (item.get("term") or item.get("name")
                     or item.get("insight") or item.get("decision") or "")
            hits.append(_hit("knowledge", title,
                             item.get("definition") or item.get("kind", ""),
                             terms, item, ref=section))
        return hits

    def _search_memory(self, terms: list[str]) -> list[dict]:
        hits = []
        for decision in self._knowledge.decisions(50):
            hits.append(_hit("memory", decision.get("decision", ""),
                             decision.get("context", ""), terms, decision,
                             ref="decision"))
        for insight in self._knowledge.strategic_insights(50):
            hits.append(_hit("memory", insight.get("insight", ""),
                             insight.get("horizon", ""), terms, insight,
                             ref="strategic_insight"))
        for insight in self._knowledge.insights(50):
            hits.append(_hit("memory", insight.get("insight", ""),
                             insight.get("statement_type", ""), terms, insight,
                             ref="insight"))
        return [h for h in hits if h["score"] > 0]

    def _search_projects(self, terms: list[str]) -> list[dict]:
        hits = []
        for pid in self._artifacts.list_projects():
            state = self._artifacts.load(pid, "state") or {}
            if not state:
                continue
            hits.append(_hit("projects", state.get("name", pid),
                             f"status {state.get('status', 'unknown')}", terms,
                             {"project_id": pid, **state}, ref=pid))
        return [h for h in hits if h["score"] > 0]

    def _search_reports(self, terms: list[str]) -> list[dict]:
        hits = []
        for report in self._knowledge.report_history(100):
            hits.append(_hit("reports", report.get("title", ""),
                             f"health {report.get('health_score')}", terms,
                             report, ref=report.get("project_id", "")))
        return [h for h in hits if h["score"] > 0]

    def _search_tasks(self, terms: list[str]) -> list[dict]:
        if self._tasks is None:
            return []
        hits = []
        for task in self._tasks.tasks(limit=300):
            hits.append(_hit("tasks", task.get("title", ""),
                             task.get("detail", ""), terms, task,
                             ref=task.get("task_id", "")))
        return [h for h in hits if h["score"] > 0]

    def _search_portfolio(self, terms: list[str]) -> list[dict]:
        if self._portfolio is None:
            return []
        overview = self._portfolio.overview()
        hits = []
        for project in overview["projects"]:
            hits.append(_hit("portfolio", project.get("name", ""),
                             f"health {project.get('health_score')}", terms,
                             project, ref=project.get("project_id", "")))
        for risk in overview["risks"]:
            hits.append(_hit("portfolio", risk.get("insight", ""), "risk",
                             terms, risk, ref="risk"))
        for opportunity in overview["opportunities"]:
            hits.append(_hit("portfolio", opportunity.get("insight", ""),
                             "opportunity", terms, opportunity,
                             ref="opportunity"))
        return [h for h in hits if h["score"] > 0]

    def _search_rules(self, terms: list[str]) -> list[dict]:
        hits = []
        for rule in self._knowledge.snapshot().get("business_rules", []):
            hits.append(_hit("business_rules", rule.get("rule", ""),
                             f"scope {rule.get('scope', 'global')}", terms,
                             rule, ref=rule.get("scope", "")))
        return [h for h in hits if h["score"] > 0]

    def _search_clarifications(self, terms: list[str]) -> list[dict]:
        hits = []
        for item in self._knowledge.snapshot().get("clarifications", []):
            hits.append(_hit("clarifications", item.get("question", ""),
                             item.get("answer", ""), terms, item,
                             ref=item.get("project_id", "")))
        return [h for h in hits if h["score"] > 0]

    def _search_recommendations(self, terms: list[str]) -> list[dict]:
        hits = []
        for rec in self._knowledge.recommendations(100):
            hits.append(_hit("recommendations", rec.get("action", ""),
                             f"priority {rec.get('priority', '—')}", terms,
                             rec, ref=rec.get("project_id", "")))
        return [h for h in hits if h["score"] > 0]

    def _search_organization(self, terms: list[str]) -> list[dict]:
        hits = []
        for entity in self._org.entities(limit=500):
            detail = entity["kind"]
            if entity["owner"]:
                detail += f" · owned by {entity['owner']}"
            hit = _hit("organization", entity["name"], detail, terms,
                       {"entity_id": entity["entity_id"],
                        "kind": entity["kind"], "owner": entity["owner"],
                        "aliases": entity["aliases"],
                        "sources": entity["sources"]},
                       ref=entity["entity_id"])
            # An alias IS an identity, so an alias match is as strong as a
            # name match — the whole point of identity is that searching
            # "M001" finds the merchant. Ranked here rather than left to the
            # generic scorer, which would see the alias only as text buried in
            # the record and score it as a weak content match.
            if any(_canonical_term(term) == alias
                   for alias in entity["aliases"] for term in terms):
                hit["score"] = max(hit["score"], 8)
                hit["matched"] = "alias"
            hits.append(hit)
        return [h for h in hits if h["score"] > 0]

    def _search_documents(self, terms: list[str]) -> list[dict]:
        """Semantic search over document chunks — SOPs, RCAs, meeting notes,
        policies, reports, and the email/Teams corpus. This is the surface that
        lets a question reach the *contents* of the enterprise's documents, not
        just their titles. Each hit carries the matched chunk text so the
        copilot can cite the passage it stood on."""
        query = " ".join(terms)
        # Prefer Document Intelligence's own search (it owns the collection and
        # its embedder); fall back to embedding here when it is not wired.
        matches: list[dict] = []
        if self._documents is not None:
            try:
                matches = self._documents.search(query, limit=MAX_PER_SURFACE)
            except Exception:  # noqa: BLE001 — degrade to the direct path
                logger.exception("Document Intelligence search failed")
                matches = []
        if not matches and self._embedder is not None \
                and self._vector_store_for is not None:
            try:
                vector = self._embedder.embed([query])[0]
                store = self._vector_store_for(DOCUMENT_COLLECTION)
                matches = store.search(vector, top_k=MAX_PER_SURFACE,
                                       kind=DOCUMENT_CHUNK_KIND)
            except Exception:  # noqa: BLE001 — documents are one surface, never all
                logger.exception("Direct document chunk search failed")
                return []

        hits = []
        for match in matches:
            payload = match.get("payload") or match
            score = float(match.get("score") or 0)
            text = str(payload.get("text") or "")
            if score <= 0 or not text:
                continue
            title = str(payload.get("document") or "").strip()
            category = str(payload.get("category") or "document")
            hits.append({
                "surface": "documents",
                "title": (title or "document")[:200],
                "detail": f"[{category}] {text}"[:200],
                "ref": str(payload.get("document_id") or ""),
                "matched": "meaning", "score": round(3 + score * 5, 3),
                "item": {"document_id": payload.get("document_id"),
                         "document": title, "category": category,
                         "source": payload.get("source"),
                         "chunk": payload.get("chunk"), "text": text[:1200]}})
        return hits

    def _search_semantic(self, query: str, terms: list[str]
                         ) -> tuple[list[dict], str]:
        """Vector search over the organizational model, when embeddings are
        configured. Additive: it can only find things keyword search missed."""
        if self._embedder is None or self._vector_store_for is None:
            return [], ""
        try:
            vector = self._embedder.embed([query])[0]
            store = self._vector_store_for("_organization")
            matches = store.search(vector, top_k=MAX_PER_SURFACE,
                                   kind="organization_entity")
        except Exception as exc:  # noqa: BLE001 — semantic is a bonus, never a requirement
            logger.exception("Semantic organization search failed")
            return [], f"semantic search unavailable: {str(exc)[:100]}"

        hits = []
        for match in matches:
            payload = match.get("payload") or match
            score = float(match.get("score") or 0)
            if score <= 0:
                continue
            hits.append({
                "surface": "organization", "title": payload.get("name", ""),
                "detail": payload.get("entity_kind", ""),
                "ref": payload.get("entity_id", ""),
                "matched": "meaning", "score": round(3 + score * 5, 3),
                "item": payload})
        return hits, ""

    # ---------------------------------------------------------------- meta
    def surfaces(self) -> list[dict]:
        """What a query searches, and whether each surface is answering."""
        return [
            {"surface": "knowledge", "available": True,
             "description": "terminology, aliases, entity definitions"},
            {"surface": "memory", "available": True,
             "description": "decisions, strategic insights, verified insights"},
            {"surface": "projects", "available": True,
             "description": "every analysis project"},
            {"surface": "reports", "available": True,
             "description": "report history with health scores"},
            {"surface": "tasks", "available": self._tasks is not None,
             "description": "executive tasks"},
            {"surface": "portfolio", "available": self._portfolio is not None,
             "description": "projects, risks, opportunities"},
            {"surface": "business_rules", "available": True,
             "description": "the rules the business runs on"},
            {"surface": "clarifications", "available": True,
             "description": "answers the business taught the platform"},
            {"surface": "recommendations", "available": True,
             "description": "open recommendations"},
            {"surface": "organization", "available": True,
             "description": "enterprise entities, aliases, and owners",
             "semantic": self._embedder is not None},
            {"surface": "documents",
             "available": self._documents is not None
             or self._embedder is not None,
             "description": "document contents: SOPs, RCAs, meetings, "
                            "policies, reports, emails, Teams",
             "semantic": True},
        ]


# --------------------------------------------------------------- utilities
def _terms(query: str) -> list[str]:
    return [t for t in str(query).lower().split() if len(t) >= MIN_TERM_LENGTH]


def _canonical_term(term: str) -> str:
    """A search term in the same shape the organizational model stores
    aliases in, so "MID-1" and "mid_1" are the same identifier."""
    return re.sub(r"[^0-9a-z]+", "_", term.strip().lower()).strip("_")


def _hit(surface: str, title: str, detail: str, terms: list[str],
         item: dict, ref: str = "") -> dict:
    """Score one candidate. Explainable by construction: the hit carries what
    matched and why it ranked where it did."""
    title_text = str(title or "").lower()
    detail_text = str(detail or "").lower()
    body = json.dumps(item, default=str).lower()

    score, matched = 0, ""
    for term in terms:
        if title_text == term:
            score += 10
            matched = matched or "exact title"
        elif title_text.startswith(term):
            score += 6
            matched = matched or "title prefix"
        elif term in title_text:
            score += 4
            matched = matched or "title"
        elif term in detail_text:
            score += 2
            matched = matched or "detail"
        elif term in body:
            score += 1
            matched = matched or "content"
    if len(terms) > 1 and all(t in body for t in terms):
        score += 2  # every term present beats any one term present

    return {"surface": surface, "title": str(title or "")[:200],
            "detail": str(detail or "")[:200], "ref": ref,
            "matched": matched, "score": score, "item": item}


def _merge(keyword_hits: list[dict], semantic_hits: list[dict]) -> list[dict]:
    """Semantic hits enrich keyword hits for the same thing rather than
    duplicating them; genuinely new ones are appended."""
    by_ref = {h["ref"]: h for h in keyword_hits if h["ref"]}
    for hit in semantic_hits:
        existing = by_ref.get(hit["ref"])
        if existing is None:
            keyword_hits.append(hit)
            continue
        if hit["score"] > existing["score"]:
            existing["score"] = hit["score"]
        existing["matched"] = f"{existing['matched']} + meaning"
    return keyword_hits
