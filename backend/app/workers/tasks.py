from app.core.container import get_container
from app.workers.celery_app import celery_app


@celery_app.task(name="edip.run_pipeline")
def run_pipeline(project_id: str) -> str:
    get_container().workflows.run("full_analysis", project_id)
    return project_id
