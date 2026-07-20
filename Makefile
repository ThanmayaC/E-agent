# Enterprise Decision Intelligence Platform — developer shortcuts

.PHONY: install dev-backend dev-frontend test lint samples docker docker-down

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

docker:
	docker compose up --build -d

docker-down:
	docker compose down
