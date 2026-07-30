"""Engine Router — decides which engines run, and runs them together.

Given a classified query, the router asks each engine whether it can handle the
request and executes the ones that can **in parallel** (Phase 4, 15). Parallel
because the engines are independent: the Analytics query, the RAG retrieval, and
the ML models share no state, so waiting for them one after another only adds
latency to a hybrid answer.

The router is deliberately thin. It holds the engine set and the concurrency;
the decision of relevance lives in each engine's ``can_handle`` and the shape of
an answer lives in the orchestrator. That separation is what lets a new engine
be added by registering it here and nowhere else.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from app.core.logging import get_logger
from app.orchestrator.base import Engine, EngineRequest, EngineResult

logger = get_logger(__name__)


class EngineRouter:
    """Selects and executes the engines relevant to a request."""

    def __init__(self, engines: list[Engine], parallel: bool = True,
                 max_workers: int = 6):
        self._engines = engines
        self._parallel = parallel
        self._max_workers = max_workers

    @property
    def engines(self) -> list[Engine]:
        return self._engines

    def select(self, request: EngineRequest) -> list[Engine]:
        """The engines that will run: those that declare they can handle the
        request. Nothing runs speculatively — an engine off the route is not
        executed, which is the point of routing."""
        chosen: list[Engine] = []
        for engine in self._engines:
            try:
                if engine.can_handle(request):
                    chosen.append(engine)
            except Exception:  # noqa: BLE001
                logger.exception("Engine %s can_handle failed", engine.key)
        # A request that matched nothing still gets the knowledge engine, so the
        # copilot always has *some* grounded evidence to reason over.
        if not chosen:
            chosen = [e for e in self._engines if e.key == "knowledge"]
        return chosen

    def route(self, request: EngineRequest) -> list[EngineResult]:
        chosen = self.select(request)
        if not chosen:
            return []
        if self._parallel and len(chosen) > 1:
            with ThreadPoolExecutor(max_workers=self._max_workers) as pool:
                results = list(pool.map(lambda e: e.timed(request), chosen))
        else:
            results = [engine.timed(request) for engine in chosen]
        return results

    def describe(self) -> list[dict]:
        return [engine.describe() for engine in self._engines]
