"""FastAPI dependencies."""
from fastapi import HTTPException

from app.core.container import Container, get_container


def container() -> Container:
    return get_container()


def require_project(c: Container, project_id: str) -> None:
    if not c.store.exists(project_id, "state"):
        raise HTTPException(status_code=404, detail=f"Project '{project_id}' not found")
