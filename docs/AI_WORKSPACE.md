# V9.0 — AI-first Enterprise Workspace

V9.0 reorients the platform around AI-first interaction — a workspace in the
spirit of ChatGPT Enterprise, Claude Enterprise, NotebookLM and Microsoft
Copilot — **without removing anything**. Every dashboard, API, the Enterprise
Brain and the Knowledge Graph remain; the AI surfaces are layered on top and the
navigation is additive.

## New backend — `app/workspace/`

A thin facade (`container.workspace`) that federates the layers the platform
already has. It adds no new intelligence; it orchestrates.

- **`understanding.py` — `FileUnderstanding`.** Turns any uploaded file into a
  structured understanding with no manual preprocessing: type detection, text /
  table / entity / date / KPI extraction, an extractive summary, tags, metadata,
  recommendations and Knowledge-Graph links. Reuses the platform
  `DocumentParser` (docx/xlsx/csv/text) and adds pypdf (PDF) and native JSON /
  XML / ZIP handling. Entities are matched against the enterprise's own
  vocabulary (banks, PSPs, merchants, products, KPIs). Images are stored with
  metadata — chart/figure vision extraction needs a vision model, which the
  local text-only Ollama setup does not provide (honest degradation, never
  invented content).
- **`search.py` — `EnterpriseSearch`.** One query across banks, PSPs, merchants,
  products, features, KPIs, decisions, uploaded files and Knowledge-Graph
  nodes, ranked by match quality.
- **`artifacts.py` — `ArtifactGenerator`.** Builds a neutral document model and
  renders it to Excel (openpyxl), Word (python-docx), or a styled printable HTML
  fallback for PDF / PowerPoint (whose writers are not installed), plus
  markdown/text for emails. Executive reports, RCAs, minutes, action items,
  roadmaps and business cases auto-compose from the executive / evolution /
  ecosystem layers when no content is supplied.
- **`workspace.py` — `Workspace`.** Upload store + understanding store,
  artifact store, pins / saved items, and the conversational **home feed**.

### API (`/api/v1/workspace/*`)

`GET /workspace` (status), `GET /workspace/home`, `POST /workspace/upload`
(multi-file, drag-drop/folder), `GET /workspace/files[/{id}]`,
`DELETE /workspace/files/{id}`, `GET /workspace/search?q=`,
`POST /workspace/artifacts` (generate) + `GET /workspace/artifacts` (list) +
`GET /workspace/artifacts/{name}` (download), `GET|POST|DELETE /workspace/pins`,
`GET /workspace/context`.

## New frontend

- **AI Home (`/`)** — the conversational landing: a large prompt box (routes
  into the Enterprise Chat), suggested prompts, and recent conversations, files,
  reports, recommendations, pins and generated artifacts.
- **Enterprise Chat (`/assistant`)** — the existing copilot chat, which already
  answers with evidence (`cited_facts`), confidence, recommended actions and
  related reports. Reused as the full-screen chat.
- **Files (`/files`)** — universal drag-and-drop upload with instant AI
  understanding (summary, entities, KPIs, dates, tables, tags, recommendations),
  plus an artifact generator with one-click download.
- **Search (`/search`)** — the unified enterprise search UI; the header search
  box routes here on Enter.
- **AI Sidebar** — a persistent, page-aware ✦ panel on every page. It frames the
  current page into the question so answers are situation-aware, and shows the
  evidence behind each answer. Mounted once in the executive shell.

Navigation is additive: the new AI Home / Chat / Files / Search entries sit
alongside the existing Dashboard, Reports, Products, Ecosystem, Evolution,
Decisions and Timeline — nothing was removed (the former landing page is kept at
`/pm-home`).

## Notes & constraints

- **Performance:** `executive.reports()` parses every report/RCA and is slow on
  the 180-day corpus; the home feed and search deliberately avoid it (the home
  feed lists recent reports straight from the filesystem instead). Optimising
  that endpoint is tracked separately.
- **Artifacts:** PDF and PowerPoint render as printable HTML because
  `reportlab` / `python-pptx` are not installed; Excel and Word are native.
- **Vision:** image/chart extraction is metadata-only without a vision model.
