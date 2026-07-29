# V8.0 — Six-Month Evolution & Digital Twin

V8.0 extends the synthetic NPCI UPI enterprise from a 35-day demo into a
**continuous 180-day operating history** that behaves like a real organization
evolving over six months. It is purely **additive** — the Enterprise Brain,
Knowledge Graph, Analytics/Ecosystem cubes, Executive APIs, Dashboards and the
Synthetic Enterprise Generator are all extended, none replaced.

Everything below is **derived from the same ledger/KPI ground truth** the V7.0
cubes use — nothing random-walks independently — and every number reconciles
back to the transaction simulation.

## 1. 180-day simulation

`generate_enterprise.py --days 180 --seed 2026` produces one deterministic,
continuous six-month history (`--days` now accepts 1–180, default 180). Growth
is modelled as **compounding monthly rates** (`growth_mult(kpi, d) =
(1+rate)^(d/30)`, `MONTHLY_GROWTH = MONTH_GROWTH × 0.6`) instead of a fixed total
spread across the window, so six months of drift accumulates naturally — over
180 days transactions grow ~+42%, technical declines roughly halve, p95 latency
falls 735→528 ms, complaints drop, adoption climbs. No artificial spikes.

Incidents scale with the horizon: the anchor incident, **one Sev-2 major
incident per month** (some recurring on the same "repeat-offender" Tier-1 bank),
and ~1 Sev-3 issue per week. Campaign/festival peaks and maintenance windows are
seeded ~2 and ~1 per month respectively.

## 2. Evolution cubes

`build_evolution()` derives 13 flat cubes, written as CSV under
`enterprise_data/master/analytics/` and read by the backend exactly like the
V7.0 cubes:

| Cube | Grain | Contents |
|------|-------|----------|
| `customer_evolution` | daily | DAU/WAU/MAU, registered base, new/churned/returned, retention, churn, power vs dormant, stickiness, feature adopters |
| `feature_adoption` | monthly | txns, share, avg ticket, adopters, m/m growth, lifecycle stage |
| `merchant_evolution` | monthly | health, lifecycle stage, growth, satisfaction, status (Active/Declining/Churned) |
| `bank_evolution` | weekly | market share, success rate, p95 latency, incidents, health, w/w growth |
| `psp_evolution` | weekly | market share + change, success rate, satisfaction, market leader |
| `product_lifecycle` | monthly | stage, adoption, customer/merchant mix, revenue contribution, avg ticket, market share |
| `kpi_rollups` | weekly/monthly/quarterly | every KPI aggregated to period means with period-over-period deltas |
| `kpi_rolling` | daily | rolling 30- and 90-day means per KPI |
| `forecast_validation` | per KPI | backtest: predicted vs realised, accuracy, MAPE, direction hit, confidence |
| `forecast_forward` | per KPI | forward 30-day forecast with confidence band |
| `decision_tracking` | per decision | target KPI, expected vs actual impact, recovery %, success score, business value (₹cr), status |
| `cross_entity` | relationships | merchant↔PSP, PSP↔bank, feature↔product, entity↔region, feature↔growth |
| `storylines` | weekly | connected Signal → Impact → Discussion → Action → Outcome chain |

## 3. Backend — `EvolutionIntelligence`

`app/executive/evolution.py` reads the cubes (via the shared `EcosystemReader`,
cached by corpus mtime) and exposes the six-month analytics plus an executive
**Q&A router** (`ask()`) that answers the workspace questions deterministically:
*Why did transaction value increase? · Which banks are improving? · Which PSP is
losing market share? · Which feature is approaching saturation? · Where should
Product invest next? · Which decision generated measurable business value? · How
accurate were the forecasts?* Each answer carries the evidence cube(s) it drew
from.

Exposed as `container.evolution`; API under `/api/v1/executive/evolution/*`
(`overview`, `customers`, `merchants`, `banks`, `psps`, `products`, `features`,
`trends`, `trends/{kpi}`, `forecast-accuracy`, `forecast/{kpi}`, `decisions`,
`decisions/{id}`, `cross-entity`, `stories`, `stories/{week}`, `ask?q=`). If the
corpus is not generated, every surface degrades to empty, like the other
executive layers.

## 4. Frontend — `/evolution`

`pages/Evolution.jsx` replays the six months across tabs: **Overview** (user
base, improving banks, PSP share losers, saturating features, investment
targets), **Users** (DAU/WAU/MAU, retention/churn, power vs dormant charts),
**Banks & PSPs** (competition tables), **Products** (lifecycle + feature
adoption), **Forecasts** (backtest accuracy), **Decisions** (expected vs actual
impact + business value), **Storyline** (week-by-week narrative), and **Ask**
(the executive Q&A). Reached from the "Evolution" nav entry.

## Regenerating

```bash
python generate_enterprise.py --days 180 --seed 2026 --ledger-size 5000
```

The evolution / executive / ecosystem layers read the cubes directly, so they
pick up a regenerated corpus without any re-ingestion (cache keys on corpus
mtime). Only the Copilot's *document* Q&A and the Knowledge Graph need a
re-ingest — run with the backend stopped:

```bash
rm -rf backend/data/documents backend/data/sync backend/data/knowledge/enterprise_graph.json
cd backend && python scripts/bootstrap_enterprise_demo.py
```
