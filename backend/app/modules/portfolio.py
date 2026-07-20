"""Portfolio Module (SDS §2.2) — status: implemented.

Two portfolio views over the same facts, at different altitudes:

- ``PortfolioWorkspace`` (executive): portfolio health, per-project trends,
  historical comparison, risks, opportunities, business performance, and
  recommended priorities — composed from business contexts, organizational
  report memory, and strategic memory.
- ``PortfolioIntelligence`` (product): the *product* portfolio — health,
  risk, growth, ranking, and investment priority across products, composed
  from the Product Health and Growth engines.

Neither computes analytics; both read what the platform already produced.
``PortfolioAgent`` remains the agent-loop entry point over the same facts.
"""
from app.agents.specialists import PortfolioAgent
from app.manager.portfolio import PortfolioWorkspace
from app.product.portfolio import PortfolioIntelligence

__all__ = ["PortfolioAgent", "PortfolioIntelligence", "PortfolioWorkspace"]
