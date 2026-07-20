# Installation Guide

## Option A — Docker (recommended)

```bash
cp .env.example .env          # optionally configure LLM / pgvector
docker compose up --build -d
```

- Frontend: http://localhost:3000
- API + Swagger: http://localhost:8000/docs
- Postgres (pgvector image) on 5432, Redis on 6379
- Celery workers: `docker compose --profile workers up -d`

## Option B — Local development

Requirements: Python 3.11+, Node 18+.

```bash
# backend
cd backend
python -m venv .venv && . .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000

# frontend (second terminal)
cd frontend
npm install
npm run dev                                       # http://localhost:5173 (proxies /api)
```

For local development the default AI provider is **Ollama**
(`EDIP_LLM_PROVIDER=ollama`): install [Ollama](https://ollama.com), run
`ollama pull qwen3` (or llama3 / gemma3 / mistral / deepseek — any model), and
the platform auto-selects the first installed model unless `EDIP_LLM_MODEL` is
set. All other infrastructure defaults need zero setup: SQLite artifacts,
per-project DuckDB warehouse, in-memory vector store, hashing embedder.
Everything swaps via configuration:

| Capability | Default | Upgrade |
|---|---|---|
| AI reasoning | Ollama (local) | `EDIP_LLM_PROVIDER=openai / azure-openai / anthropic / gemini / enterprise` + key/base URL — no code changes |
| Vector store | in-memory (JSON persisted) | `EDIP_VECTOR_BACKEND=pgvector` + `EDIP_PGVECTOR_URL` |
| Embeddings | built-in hashing | `EDIP_EMBEDDING_MODEL=all-MiniLM-L6-v2` (+ `pip install sentence-transformers`) |
| Pipeline execution | FastAPI BackgroundTasks | `EDIP_USE_CELERY=true` + Redis (+ `pip install celery redis`) |

If no provider is reachable, AI narrative sections report `unavailable` and
every deterministic artifact (KPIs, signals, forecasts, quality, graph) still
works.

## Sample data

```bash
cd backend
python scripts/generate_sample_data.py            # writes ../sample_data/*.xlsx
```

Generates 5 deliberately messy fintech workbooks (~35k transactions across
partitioned files, merged title cells, a hidden sheet, missing values,
outliers, different naming conventions) that exercise every pipeline stage.
Upload them on the home screen and click **Upload & Analyze**.

## Tests

```bash
cd backend
pytest tests/unit           # engine unit tests
pytest tests/integration    # full upload → pipeline → report → copilot flow
```

## Troubleshooting

- **Analysis 'failed'** — open Settings & Admin in the UI; the failing stage
  shows its error detail. Corrupt sheets are skipped, not fatal.
- **Large uploads rejected** — raise `EDIP_MAX_UPLOAD_MB`.
- **Windows paths** — run uvicorn from the `backend/` directory so the relative
  `data/` directory resolves next to the app (or set an absolute `EDIP_DATA_DIR`).
