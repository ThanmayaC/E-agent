"""Provider abstraction: factory selection, JSON extraction, reasoning engine."""
import pytest

from app.core.config import Settings
from app.domain.entities import AIReport
from app.llm.base_provider import extract_json
from app.llm.mock_provider import MockProvider
from app.llm.ollama_provider import OllamaProvider
from app.llm.provider_factory import create_provider
from app.agents.reasoning import AIReasoningEngine


def _settings(**kw) -> Settings:
    return Settings(data_dir="data_test_tmp", **kw)


def test_factory_selects_by_configuration_only():
    assert create_provider(_settings(llm_provider="none")) is None
    assert isinstance(create_provider(_settings(llm_provider="mock")), MockProvider)
    assert isinstance(create_provider(_settings(llm_provider="ollama")), OllamaProvider)
    with pytest.raises(ValueError):
        create_provider(_settings(llm_provider="does-not-exist"))


def test_extract_json_tolerates_fences_prose_and_think_tags():
    assert extract_json('{"a": 1}') == {"a": 1}
    assert extract_json('```json\n{"a": 1}\n```') == {"a": 1}
    assert extract_json('Sure! Here you go: {"a": {"b": 2}} hope that helps') == {"a": {"b": 2}}
    assert extract_json('<think>reasoning...</think>{"a": 1}') == {"a": 1}
    assert extract_json("no json here") is None


def test_reasoning_engine_without_provider_marks_unavailable():
    engine = AIReasoningEngine(provider=None)
    report = engine.generate_report({"kpis": []})
    assert report.status == "unavailable"
    assert report.executive_summary == ""          # never template narrative
    answer = engine.answer("Why did growth slow?", {})
    assert answer["status"] == "unavailable"


def test_reasoning_engine_with_mock_returns_structured_report():
    engine = AIReasoningEngine(create_provider(_settings(llm_provider="mock")))
    report = engine.generate_report({"kpis": [{"name": "Revenue", "current": 10}]})
    assert isinstance(report, AIReport)
    assert report.status == "ok"
    assert report.executive_summary
    assert report.recommendations and isinstance(report.recommendations[0], dict)
    assert report.provider == "mock"


def test_validate_normalizes_string_items_to_dicts():
    raw = {"executive_summary": "s", "key_insights": ["plain string insight"],
           "recommendations": ["do the thing"], "priority_actions": [{"action": "act"}],
           "confidence": "0.7"}
    report = AIReasoningEngine._validate(raw)
    assert report.key_insights[0] == {"title": "plain string insight"}
    assert report.recommendations[0] == {"action": "do the thing"}
    assert report.priority_actions == ["act"]
    assert report.confidence == 0.7
