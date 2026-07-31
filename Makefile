# Enterprise Decision Intelligence Platform — developer shortcuts

.PHONY: install dev-backend dev-frontend test lint samples docker docker-down \
        data data-warehouse data-cubes data-reports data-check

install:
	cd backend && pip install -r requirements.txt -r requirements-dev.txt
	cd frontend && npm install

dev-backend:
	cd backend && uvicorn app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

test:
	cd backend && pytest

lint:
	cd backend && ruff check app tests

samples:
	cd backend && python scripts/generate_sample_data.py

# ---------------------------------------------------------------------------
# Data regeneration. ORDER MATTERS — the transaction corpus is the only source
# of truth and everything else is a projection of it, so each step below reads
# what the step above produced. Running them out of order (in particular
# running generate_enterprise.py *after* the reports) reintroduces the
# two-truth problem this pipeline exists to prevent.
# ---------------------------------------------------------------------------
data: data-warehouse data-cubes data-reports data-check

data-warehouse:            ## 1. simulate the raw transaction corpus
	cd backend && python -m app.warehouse.generator.build

data-cubes:                ## 2. project every cube + the KPI workbook off it
	cd backend && python -m app.warehouse.project_cubes --forecasts

data-reports:              ## 3. write the daily reports from the same corpus
	cd backend && python -m app.warehouse.reporting.daily

data-check:                ## 4. fail if any published number drifts from the corpus
	cd backend && python -m app.warehouse.project_cubes --check

docker:
	docker compose up --build -d

docker-down:
	docker compose down
g