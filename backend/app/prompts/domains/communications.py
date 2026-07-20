"""Communication prompts — drafted email and Teams updates.

Every template here produces a *draft*. Nothing these prompts generate leaves
the platform without passing through the Action Queue's approval layer, which
is why they are marked governed: their wording is what an executive's name
would go on.

Moved out of ``app/workflows/library.py`` in V2.2.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

EMAIL_BODY = ("Write a short executive status email body (plain text, no "
              "salutation placeholders) from this daily brief.")

TEAMS_UPDATE = ("Write a brief Teams channel update (2-3 sentences, plain "
                "text) summarizing today's executive brief for the team.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="communications.email_body", domain="communications",
        template=EMAIL_BODY, version=1, owner="executive-office",
        description="Daily executive status email body, drafted for approval.",
        tags=("drafting", "email"), governed=True),
    PromptTemplate(
        prompt_id="communications.teams_update", domain="communications",
        template=TEAMS_UPDATE, version=1, owner="executive-office",
        description="Daily Teams announcement, drafted for approval.",
        tags=("drafting", "teams"), governed=True),
]
