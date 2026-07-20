"""Tool layer — capabilities agents can invoke.

A Tool is a named, described, schema-light callable. Agents (and eventually
the LLM itself, through tool-choice prompting) decide which tools to run;
tools never decide anything. Tools that need missing dependencies or
integrations register as unavailable with an explanation instead of failing.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ToolNotAvailable(RuntimeError):
    """Raised when an unavailable tool is invoked."""


class Tool(ABC):
    name: str = "tool"
    description: str = ""

    @property
    def available(self) -> bool:
        return True

    @property
    def unavailable_reason(self) -> str:
        return ""

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Execute the tool. Raise ToolNotAvailable if not available."""

    def describe(self) -> dict:
        return {"name": self.name, "description": self.description,
                "available": self.available,
                "unavailable_reason": self.unavailable_reason}


# The registry lives in ``app.tools.registry`` (V2.2): it grew specs,
# permissions, input/output schemas, and execution status, and importing it
# here would be circular. ``from app.tools.registry import ToolRegistry``.
