"""FastAPI application entrypoint."""
import hmac
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.v1 import (
    analyst, artifacts, brain, communication, connectors, copilot, documents,
    executive, knowledge, manager, operating, platform, product, projects,
    runtime, sync, workspace,
)
from app.core.config import get_settings
from app.core.logging import configure_logging, get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Build the container at startup (not on first request) so the
    Enterprise Brain loads memory, knowledge, the knowledge graph, learning
    history, business rules, and clarifications, verifies consistency, and
    is READY before traffic arrives.

    Then start the autonomy runtime: from here the platform observes,
    learns, plans, executes, monitors, and improves on its own heartbeat —
    it does not wait for the manager to ask.
    """
    from app.core.container import get_container
    container = get_container()  # __init__ runs brain.startup() when enabled
    settings = get_settings()
    # V3.1: expand the knowledge graph into a business-entity graph from the
    # ingested enterprise (idempotent; no-op when no enterprise is generated).
    try:
        edges = container.executive.build_business_graph(
            container.enterprise_graph)
        if edges:
            logger.info("Executive layer: business graph linked (%d edges)",
                        edges)
    except Exception:  # noqa: BLE001 — never block startup on graph enrichment
        logger.exception("Executive layer: business graph build failed")
    if settings.autonomy_enabled:
        container.runtime.start()  # startup jobs, then the scheduler ticks
    try:
        yield
    finally:
        container.runtime.stop()  # in-flight jobs finish, the thread joins


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.debug)

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs",
        openapi_url=f"{settings.api_prefix}/openapi.json",
        lifespan=lifespan,
    )
    # Desktop mode (v4 Phase 0): the Core is bound to loopback by the shell,
    # which passes a per-launch bearer token. Enforce it on every request.
    # Registered BEFORE CORS so the CORS middleware remains outermost and still
    # attaches its headers to the 401 responses this guard returns. Additive
    # and reversible: with desktop_mode off (default) no guard is installed and
    # the platform behaves exactly as the web deployment did.
    if settings.desktop_mode and settings.desktop_token:
        expected_token = settings.desktop_token

        @app.middleware("http")
        async def _require_desktop_token(request: Request, call_next):
            # CORS preflight (OPTIONS) carries no Authorization header by design.
            if request.method != "OPTIONS":
                header = request.headers.get("authorization", "")
                presented = header[7:] if header[:7].lower() == "bearer " else ""
                if not (presented and hmac.compare_digest(presented, expected_token)):
                    return JSONResponse({"detail": "unauthorized"}, status_code=401)
            return await call_next(request)

    # In desktop mode the UI is served from the Tauri webview origin
    # (tauri://localhost or http(s)://tauri.localhost on Windows); allow it in
    # addition to the configured web origins.
    cors_kwargs: dict = dict(
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if settings.desktop_mode:
        cors_kwargs["allow_origin_regex"] = r"^(tauri://localhost|https?://tauri\.localhost)$"
    app.add_middleware(CORSMiddleware, **cors_kwargs)

    app.include_router(projects.router, prefix=settings.api_prefix)
    app.include_router(artifacts.router, prefix=settings.api_prefix)
    app.include_router(knowledge.router, prefix=settings.api_prefix)
    app.include_router(platform.router, prefix=settings.api_prefix)
    app.include_router(brain.router, prefix=settings.api_prefix)
    app.include_router(manager.router, prefix=settings.api_prefix)
    app.include_router(runtime.router, prefix=settings.api_prefix)
    app.include_router(sync.router, prefix=settings.api_prefix)
    app.include_router(product.router, prefix=settings.api_prefix)
    app.include_router(copilot.router, prefix=settings.api_prefix)
    app.include_router(documents.router, prefix=settings.api_prefix)
    app.include_router(connectors.router, prefix=settings.api_prefix)
    app.include_router(operating.router, prefix=settings.api_prefix)
    app.include_router(executive.router, prefix=settings.api_prefix)
    app.include_router(workspace.router, prefix=settings.api_prefix)
    app.include_router(analyst.router, prefix=settings.api_prefix)
    app.include_router(communication.router, prefix=settings.api_prefix)

    @app.get("/health")
    def health():
        return {"status": "ok", "app": settings.app_name, "version": settings.app_version}

    return app


app = create_app()
