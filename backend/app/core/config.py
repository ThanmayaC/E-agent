"""Application configuration. Everything is environment-driven — no hardcoded values."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="EDIP_", extra="ignore")

    # --- Application ---
    app_name: str = "Enterprise Autonomous Product Intelligence Platform"
    app_version: str = "2.0.0"
    environment: str = "development"
    debug: bool = True
    api_prefix: str = "/api/v1"
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    # --- Storage ---
    data_dir: Path = Path("data")
    max_upload_mb: int = 200
    # Which of these can actually be ingested is decided by the connector
    # registry at runtime (optional connectors may be unavailable).
    allowed_extensions: list[str] = [
        ".xlsx", ".xlsm", ".xls", ".csv", ".tsv", ".pdf", ".docx",
        ".sqlsource.json", ".apisource.json",
    ]

    # --- Database (control plane: runs, evidence, statements, audit) ---
    # Empty = SQLite file under data_dir (lite profile). Set to a
    # postgresql:// URL for the full enterprise profile.
    database_url: str = ""

    # --- Vector store ---
    vector_backend: str = "memory"  # memory | pgvector
    pgvector_url: str = ""
    embedding_model: str = "hash"  # hash | sentence-transformers model name
    embedding_dim: int = 256

    # --- Cache / queue ---
    redis_url: str = "redis://localhost:6379/0"
    use_celery: bool = False

    # --- LLM layer (provider-agnostic; swap via config only) ---
    # none | ollama | openai | azure-openai | anthropic | gemini | enterprise | mock
    llm_provider: str = "ollama"
    llm_model: str = ""  # empty + ollama -> first installed model
    llm_api_key: str = ""
    llm_base_url: str = ""
    llm_max_tokens: int = 4096
    llm_temperature: float = 0.2
    llm_timeout_s: float = 180.0
    llm_retries: int = 2
    llm_extra: dict = {}  # provider-specific, e.g. {"api_version": "..."} for Azure
    # Optional secondary provider tried when the primary fails after retries.
    # Same vocabulary as llm_provider; empty = no fallback.
    llm_fallback_provider: str = ""
    llm_fallback_model: str = ""
    llm_fallback_api_key: str = ""
    llm_fallback_base_url: str = ""

    # --- Orchestration (v3 Phase C: strangler flag) ---
    # langgraph: checkpointed multi-agent analysis graph (pause/resume,
    # repair loops, evidence ledger). legacy: the v2 imperative workflow.
    # langgraph silently falls back to legacy when the library is absent,
    # so the lite install keeps working unchanged.
    orchestrator: str = "langgraph"  # langgraph | legacy
    max_passes: int = 2                       # supervisor-ordered analysis passes
    max_repair_attempts: int = 1              # verifier → report regeneration loops
    # Above this unverified-statement rate the report agent is asked to
    # regenerate (bounded by max_repair_attempts).
    verification_repair_threshold: float = 0.5

    # --- Enterprise Brain (continuous organizational learning) ---
    brain_enabled: bool = True
    # Optional Neo4j mirror for the enterprise knowledge graph. Empty = the
    # persistent NetworkX graph under knowledge_dir remains the only store.
    neo4j_uri: str = ""       # e.g. bolt://localhost:7687
    neo4j_user: str = "neo4j"
    neo4j_password: str = ""

    # --- Autonomous execution layer (scheduler, queue, goals, triggers) ---
    # The runtime is always built (its APIs and state are always readable);
    # this flag decides whether the heartbeat actually ticks. Off = every
    # autonomous surface still works on demand, nothing runs by itself.
    autonomy_enabled: bool = True
    autonomy_tick_seconds: float = 30.0        # scheduler heartbeat
    autonomy_queue_interval_seconds: float = 60.0
    autonomy_refresh_interval_seconds: float = 900.0    # background: 15 min
    autonomy_planning_interval_seconds: float = 300.0   # plan advance: 5 min
    # 5-field cron (minute hour day-of-month month day-of-week), UTC.
    autonomy_daily_cycle_cron: str = "0 6 * * *"        # 06:00 daily
    autonomy_monitoring_cron: str = "0 * * * *"         # hourly
    # Below this confidence the Decision Engine routes to a human whatever
    # the action kind is — autonomy is bounded by evidence.
    autonomy_confidence_threshold: float = 0.7
    # Action kinds that always require human approval. Anything with an
    # external effect belongs here; internal, reversible work does not.
    autonomy_requires_approval: list[str] = [
        "send_email", "create_meeting", "send_message",
        "update_business_rule", "execute_automation",
    ]

    # --- Enterprise Knowledge Synchronization Layer ---
    # Once enterprise systems are connected, organizational knowledge updates
    # continuously. Off = the registry, model, and search still answer; only
    # the automatic refresh stops.
    sync_enabled: bool = True
    sync_refresh_interval_seconds: float = 900.0   # knowledge refresh: 15 min
    sync_health_interval_seconds: float = 300.0    # source health: 5 min
    sync_sweep_cron: str = "30 3 * * *"            # nightly organization sweep

    # --- Product Intelligence & Strategic Decision Layer ---
    # The Enterprise Product Manager: continuous product health, growth
    # intelligence, strategy, KPI monitoring, scenarios, and executive briefs
    # over the Enterprise Brain. Off = every surface still answers on demand;
    # only the automatic recalculation stops.
    product_enabled: bool = True
    product_health_interval_seconds: float = 900.0     # re-score: 15 min
    product_refresh_interval_seconds: float = 1800.0   # growth/strategy: 30 min
    product_kpi_interval_seconds: float = 900.0        # KPI watch: 15 min
    product_brief_cron: str = "0 7 * * 1"              # board brief: Mon 07:00

    # --- Enterprise Copilot Layer ---
    # The executive's primary interaction point: intent → plan → context →
    # evidence → prompt → LLM → validation. Off = the /copilot surface is
    # disabled; every other surface is unaffected.
    copilot_enabled: bool = True
    copilot_keep_conversations: int = 200   # pinned threads are never pruned
    copilot_prune_cron: str = "0 4 * * *"   # nightly maintenance

    # --- V2: Document Intelligence (unified document pipeline) ---
    # Consumes document-source sync deltas: metadata → parse (+OCR fallback)
    # → chunk → embed → Brain update → version tracking. Off = document
    # sources degrade to catalog-only synchronization.
    documents_enabled: bool = True
    document_chunk_chars: int = 1600
    document_chunk_overlap: int = 200
    document_ocr_enabled: bool = True   # used only when the OCR stack exists

    # --- V2.1: Enterprise Connector Framework ---
    # Administrators configure enterprise data sources once; the Runtime keeps
    # them synchronized and every change becomes organizational knowledge.
    # Off = the registry and catalogue still answer and manual sync still
    # works; only the automatic synchronization stops.
    connectors_enabled: bool = True
    connector_sync_interval_seconds: float = 900.0   # due sources: 15 min
    connector_health_interval_seconds: float = 300.0  # source health: 5 min
    connector_sweep_cron: str = "15 2 * * *"         # nightly full re-read

    # --- V2.2: Enterprise AI Operating Layer ---
    # Evaluation: every AI-generated output can pass a panel of evaluators
    # before it reaches an executive. Off = the V1 guards (evidence
    # verification, response validation) remain the only gate, exactly as
    # V2.1 behaved.
    evaluation_enabled: bool = True
    # Governance: RBAC, connector permissions, approval and retention
    # policies, audit and model-usage logs. Off = every gate is open and the
    # platform behaves exactly as V2.1 did.
    governance_enabled: bool = True
    # What an unidentified caller is treated as. The default preserves V2.1
    # behaviour; a governed deployment narrows this and assigns principals.
    governance_default_role: str = "administrator"
    # Observability is Admin-only and always available; this flag only
    # controls whether latency is sampled on the hot path.
    observability_latency_enabled: bool = True

    # --- V2: Autonomous workflow library (drafting cadences) ---
    # Document workflows (RCA/SOP/meeting/action items) run on document
    # change events; drafting workflows run on these crons. Every draft with
    # an external effect queues for approval — nothing sends by itself.
    v2_email_draft_cron: str = "30 6 * * *"       # daily status email draft
    v2_teams_update_cron: str = "45 6 * * *"      # daily Teams update draft
    v2_presentation_cron: str = "0 7 * * 1"       # weekly deck outline, Mon
    # Default recipients for drafted email, comma-separated. Empty = the
    # manager fills recipients while editing the queued draft.
    v2_email_recipients: str = ""

    # --- ML platform (model selection framework) ---
    ml_enabled: bool = True
    # A challenger must beat the deterministic baseline by at least this
    # relative margin in rolling-origin backtests to be admitted.
    ml_min_beat_margin: float = 0.05
    # Optional MLflow mirror for registered models (EDIP_MLFLOW_URI);
    # empty = the file registry + Evidence Ledger remain the only record.
    mlflow_uri: str = ""

    # --- Inference thresholds (tunable, not hardcoded in engines) ---
    header_scan_rows: int = 15
    sample_rows_for_profiling: int = 50000
    pk_uniqueness_threshold: float = 0.99
    fk_overlap_threshold: float = 0.60
    fuzzy_match_threshold: float = 0.82
    semantic_similarity_threshold: float = 0.60
    duplicate_schema_similarity: float = 0.90
    outlier_zscore: float = 3.0
    min_confidence_to_report: float = 0.30
    # Below this understanding confidence the pipeline pauses and asks the
    # user clarification questions instead of guessing.
    clarification_confidence_threshold: float = 0.55

    @property
    def control_db_url(self) -> str:
        """Control-plane connection string: explicit database_url when set,
        else an SQLite file under data_dir (respects test/env overrides)."""
        if self.database_url:
            return self.database_url
        return f"sqlite:///{(self.data_dir / 'control.db').as_posix()}"

    @property
    def projects_dir(self) -> Path:
        return self.data_dir / "projects"

    @property
    def knowledge_dir(self) -> Path:
        """Organization-wide persistent knowledge (outlives any project)."""
        return self.data_dir / "knowledge"

    @property
    def runtime_dir(self) -> Path:
        """Autonomous runtime state: goals, actions, triggers, plans."""
        return self.data_dir / "runtime"

    @property
    def sync_dir(self) -> Path:
        """Synchronization state: sources, entities, relationships, runs."""
        return self.data_dir / "sync"

    @property
    def prompts_dir(self) -> Path:
        """Prompt registry state: version change history."""
        return self.data_dir / "prompts"

    @property
    def connectors_dir(self) -> Path:
        """Connector framework state: data sources, cursors, runs, packages."""
        return self.data_dir / "connectors"

    @property
    def product_dir(self) -> Path:
        """Product intelligence: catalogue, health, reviews, strategy."""
        return self.data_dir / "product"

    @property
    def copilot_dir(self) -> Path:
        """Enterprise conversations: threads, messages, preferences."""
        return self.data_dir / "copilot"

    def ensure_dirs(self) -> None:
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        self.knowledge_dir.mkdir(parents=True, exist_ok=True)


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.ensure_dirs()
    return settings
