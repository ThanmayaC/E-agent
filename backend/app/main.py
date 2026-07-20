"""FastAPI application entrypoint."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import (
    artifacts, brain, connectors, copilot, documents, knowledge, manager,
    operating, platform, product, projects, runtime, sync,
)
from app.core.config import get_settings
from app.core.logging import configure_logging


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
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
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

    @app.get("/health")
    def health():
        return {"status": "ok", "app": settings.app_name, "version": settings.app_version}

    return app


app = create_app()
