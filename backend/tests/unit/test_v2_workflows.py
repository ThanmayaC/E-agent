"""Version 2 — the autonomous workflow library, the approval engine's edit
path, and the communication adapters' configuration contract."""
from __future__ import annotations

import pytest

from app.communication.adapters import (
    OutlookEmailAdapter, SharePointDocumentAdapter, TeamsMessagingAdapter,
)
from app.communication.providers import ProviderNotConfigured
from app.documents.parser import DocumentParser
from app.documents.store import DocumentStore
from app.documents.pipeline import DocumentIntelligence
from app.runtime.events import EventBus
from app.runtime.queue import ActionQueue
from app.runtime.store import RuntimeStore
from app.workflows.library import V2Context, build_v2_workflows


# ------------------------------------------------------------------ fakes
class _Tasks:
    def __init__(self):
        self.created = []

    def create(self, title, **kwargs):
        self.created.append({"title": title, **kwargs})
        return {"task_id": f"t{len(self.created)}", "title": title}


class _Notifications:
    def __init__(self):
        self.sent = []

    def notify(self, kind, title, detail="", project_id="", ref=""):
        self.sent.append({"kind": kind, "title": title, "detail": detail})
        return self.sent[-1]


class _Knowledge:
    def __init__(self):
        self.insights = []

    def record_insight(self, insight, **kwargs):
        self.insights.append(insight)

    def recommendations(self, limit=6):
        return [{"action": "Grow Autopay"}]

    def record_learning_event(self, *a, **k): ...


class _Brief:
    def today(self):
        return {"date": "2026-07-17",
                "high_priority_issues": [{"title": "Autopay decline spike"}],
                "portfolio_changes": [], "recommendations": []}


@pytest.fixture()
def queue(tmp_path):
    store = RuntimeStore(tmp_path / "runtime")
    return ActionQueue(store, EventBus(store))


@pytest.fixture()
def context(tmp_path, queue):
    documents = DocumentIntelligence(
        store=DocumentStore(tmp_path / "docs"), parser=DocumentParser())
    return V2Context(documents=documents, knowledge=_Knowledge(),
                     tasks=_Tasks(), notifications=_Notifications(),
                     queue=queue, brief=_Brief(), portfolio=None,
                     reasoning=None, store=None,
                     default_recipients=["coo@example.com"])


def _ingest(context, category_kind, name, text, source="src"):
    kind_by_cat = {"rca": "rca_repository", "sop": "sop_repository",
                   "meeting": "meeting_notes"}
    store = context.documents._store  # test-only shortcut
    doc, _ = store.upsert(source, kind_by_cat[category_kind], name, name,
                          ".md", len(text), "", f"h{name}{len(text)}", text,
                          1, "text", False, [], "added")
    return doc


def _workflow(context, name):
    return next(w for w in build_v2_workflows(context) if w.name == name)


# ------------------------------------------------------------- workflows
def test_rca_summarization_writes_knowledge_and_notifies(context):
    _ingest(context, "rca", "outage.md",
            "The outage was caused by a certificate expiry. Rotation was "
            "manual. The fix automates renewal.")
    outcome = _workflow(context, "rca_summarization").runner("")

    assert outcome["documents"] == 1
    assert context.knowledge.insights, "the Brain learned the RCA summary"
    assert context.notifications.sent[0]["title"].startswith("RCA summary")
    # The same version is never summarized twice.
    assert _workflow(context, "rca_summarization").runner("")["documents"] == 0


def test_sop_change_detection_only_fires_on_changes(context):
    doc = _ingest(context, "sop", "refunds.md", "Original refund process.")
    assert _workflow(context, "sop_change_detection").runner("")["changes"] \
        == 0, "version 1 is an arrival, not a change"

    store = context.documents._store
    store.upsert("src", "sop_repository", "refunds.md", "refunds.md", ".md",
                 30, "", "h2", "Changed refund process.", 1, "text",
                 False, [], "changed")
    outcome = _workflow(context, "sop_change_detection").runner("")
    assert outcome["changes"] == 1
    assert any("Review the change" in t["title"]
               for t in context.tasks.created)


def test_action_items_become_executive_tasks(context):
    _ingest(context, "meeting", "standup.md",
            "# Standup\n- Action: Dana to review Q3 pricing\n"
            "- TODO: publish the RCA\nGeneral discussion followed.")
    outcome = _workflow(context, "action_item_extraction").runner("")

    assert outcome["action_items"] == 2
    titles = [t["title"] for t in context.tasks.created]
    assert "Dana to review Q3 pricing" in titles


def test_email_drafting_queues_for_approval_and_never_sends(context, queue):
    outcome = _workflow(context, "email_drafting").runner("")

    assert outcome["drafted"]
    action = queue.actions(kind="send_email")[0]
    assert action["status"] == "pending_approval"
    assert action["payload"]["to"] == ["coo@example.com"]
    assert "Autopay decline spike" in action["payload"]["body"]


def test_teams_drafting_queues_for_approval(context, queue):
    outcome = _workflow(context, "teams_message_drafting").runner("")

    assert outcome["drafted"]
    action = queue.actions(kind="send_message")[0]
    assert action["status"] == "pending_approval"
    assert "Daily update" in action["payload"]["text"]


# -------------------------------------------------------- approval engine
def test_the_manager_can_edit_a_draft_before_approving(queue):
    action = queue.submit("send_email", "Daily status email",
                          payload={"to": [], "subject": "Status",
                                   "body": "draft"})
    edited = queue.edit(action["action_id"],
                        payload={"to": ["ceo@example.com"],
                                 "body": "final wording"},
                        by="executive")

    assert edited["payload"]["to"] == ["ceo@example.com"]
    assert edited["payload"]["body"] == "final wording"
    assert edited["payload"]["subject"] == "Status", "unedited keys survive"
    assert edited["edits"][0]["by"] == "executive"

    queue.approve(action["action_id"], by="executive")
    with pytest.raises(ValueError):
        queue.reject(action["action_id"])  # already approved


def test_an_executed_action_can_no_longer_be_edited(queue):
    action = queue.submit("notify", "Heads up")  # auto-approved kind
    queue.register_executor("notify", lambda a: {"ok": True})
    queue.execute(action["action_id"])

    with pytest.raises(ValueError, match="edited"):
        queue.edit(action["action_id"], title="too late")


# --------------------------------------------------- communication layer
def test_unconfigured_adapters_report_what_is_missing(monkeypatch):
    for var in ("EDIP_MS_GRAPH_AUTH", "EDIP_TEAMS_WEBHOOK_URL",
                "EDIP_SP_DRIVE_ID"):
        monkeypatch.delenv(var, raising=False)

    for adapter in (OutlookEmailAdapter(), TeamsMessagingAdapter(),
                    SharePointDocumentAdapter()):
        assert adapter.available is False
        assert adapter.unavailable_reason


def test_configured_adapters_report_available(monkeypatch):
    monkeypatch.setenv("EDIP_MS_GRAPH_AUTH", "token")
    monkeypatch.setenv("EDIP_TEAMS_WEBHOOK_URL", "https://example.com/hook")
    monkeypatch.setenv("EDIP_SP_DRIVE_ID", "drive1")

    assert OutlookEmailAdapter().available
    assert TeamsMessagingAdapter().available
    assert SharePointDocumentAdapter().available


# ------------------------------------------- Outlook / Teams read (V2.3)
class _FakeGraph:
    """A Microsoft Graph client that returns canned records — no network."""
    def __init__(self, messages=None, channels=None):
        self._messages = messages or []
        self._channels = channels or []

    def get_all(self, path, params=None, limit=500):
        return self._messages if path.endswith("/messages") else self._channels

    def get(self, path, params=None):
        return {"id": "m1", "subject": "Settlement delay",
                "from": {"emailAddress": {"address": "ops@skypay.com"}},
                "receivedDateTime": "2026-03-11", "bodyPreview": "payout delayed",
                "body": {"content": "The full email body."}}


def test_outlook_read_and_search_normalize_messages(monkeypatch):
    monkeypatch.setenv("EDIP_MS_GRAPH_AUTH", "token")
    fake = _FakeGraph(messages=[{
        "id": "m1", "subject": "Settlement delay",
        "from": {"emailAddress": {"address": "ops@skypay.com"}},
        "receivedDateTime": "2026-03-11", "bodyPreview": "payout delayed"}])
    monkeypatch.setattr("app.communication.adapters._graph_client",
                        lambda: fake)
    adapter = OutlookEmailAdapter()

    inbox = adapter.read_messages()
    assert inbox[0]["subject"] == "Settlement delay"
    assert inbox[0]["from"] == "ops@skypay.com"
    assert inbox[0]["channel"] == "outlook"

    found = adapter.search_messages("settlement")
    assert found and found[0]["id"] == "m1"

    full = adapter.get_message("m1")
    assert full["body"] == "The full email body."


def test_outlook_read_is_unavailable_without_credentials(monkeypatch):
    monkeypatch.delenv("EDIP_MS_GRAPH_AUTH", raising=False)
    with pytest.raises(ProviderNotConfigured):
        OutlookEmailAdapter().read_messages()


def test_teams_read_channels_and_messages(monkeypatch):
    monkeypatch.setenv("EDIP_MS_GRAPH_AUTH", "token")
    fake = _FakeGraph(
        channels=[{"id": "c1", "displayName": "payments-incidents",
                   "description": "incident bridge"}],
        messages=[{"id": "t1", "from": {"user": {"displayName": "Tom"}},
                   "createdDateTime": "2026-03-12",
                   "body": {"content": "Declaring Sev-2 on settlement."}}])
    monkeypatch.setattr("app.communication.adapters._graph_client",
                        lambda: fake)
    adapter = TeamsMessagingAdapter()

    channels = adapter.read_channels("T1")
    assert channels[0]["name"] == "payments-incidents"

    messages = adapter.read_messages("T1", "c1")
    assert messages[0]["from"] == "Tom"
    assert "Sev-2" in messages[0]["text"]


def test_teams_read_is_unavailable_without_credentials(monkeypatch):
    monkeypatch.delenv("EDIP_MS_GRAPH_AUTH", raising=False)
    with pytest.raises(ProviderNotConfigured):
        TeamsMessagingAdapter().read_channels("T1")


def test_approved_communications_wait_without_an_executor(queue):
    action = queue.submit("send_message", "Announcement",
                          payload={"text": "hi"})
    queue.approve(action["action_id"])
    drained = queue.execute_ready()

    assert drained["executed"] == 0
    assert queue.actions(status="approved"), \
        "the approved message waits for its channel, it is not lost"
