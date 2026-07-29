# Synthetic Enterprise Generator (V7.0 — NPCI UPI Ecosystem Simulation)

V7.0 generates **one coherent synthetic organization** — NPCI (Synthetic
Demonstration), the UPI Products department — and **35 continuous days of a
complete UPI ecosystem simulation at transaction grain**. A synthetic customer
population and merchant base with behaviour models drive a large **sampled
transaction ledger**; every daily metric, feature/bank/PSP/city analytic, trend,
forecast and business-intelligence signal is rolled up *from that ledger*, and
every meeting/RCA/decision is triggered by a measurable trend. Nothing is
launched — the existing UPI stack is only operated.

The generator is a single deterministic script; its output ingests through the
existing pipeline with no backend change, and a full-stack **UPI Ecosystem**
dashboard renders the analytics.

```bash
python generate_enterprise.py --days 35 --seed 2026 --ledger-size 10000
cd backend && python scripts/bootstrap_enterprise_demo.py
```

## The organization

- **Organization:** NPCI (Synthetic Demonstration) — fictional. **Department:** UPI Products.
- **Teams:** product squads (UPI Core/Autopay/Lite/Lite X/Credit/International,
  Merchant Products, QR Payments) plus operating functions (Operations,
  Technology, Engineering, Business, Merchant Success, Customer Experience, Risk
  & Compliance, Compliance, Product Analytics/Operations/Strategy, PSP
  Integration, AI & Innovation).
- **Ecosystem:** ~70 employees, 8 products, 11 UPI features, 15 merchants (with
  size/behaviour), **15 banks** (issuer + acquirer roles), **14 PSPs**, **~4,000
  synthetic customers** with behaviour profiles, and 25 cities across states.

Everything is fictional and synthetic. It follows realistic patterns but copies
no production numbers, and represents no real person, company, or system.

## How the month is simulated

1. **`TransactionEngine`** derives the 15 headline KPIs + per-bank/PSP/feature
   health from a growth trend modulated by weekday, month-end and seeded
   high-volume campaign days, perturbed by seeded operational **issues** (bank
   timeouts, PSP latency, settlement delays, fraud spikes, merchant declines,
   feature degradations).
2. **`Ledger`** samples ~10,000 transactions/day (~350k rows over 35 days) from
   the customer/merchant behaviour models, **reconciled to the engine's daily
   success/decline rates** (the ledger's success rate equals the workbook's ±
   rounding). Each row carries ~25 fields: timestamp, issuer/beneficiary bank,
   payer/payee PSP, merchant + category, customer + profile, feature, payment
   type, amount, status, failure reason, response code, latency, processing
   time, device, channel, city, state, hour/day/week/month. Rows are written per
   day under `day_XX/ledger/` as data (not embedded).
3. **Aggregate cubes** (CSV, in `master/analytics/`) roll up from the ledger:
   `daily_metrics`, `feature_daily`, `bank_daily`, `psp_daily`, `merchant_daily`,
   `city_daily`, `hourly_distribution`, `transaction_mix`, `customer_activity`.
4. **Trend engine** computes today / yesterday / 7d / 30d / WoW / MTD / moving &
   rolling averages / growth% / **forecast** per series (`trends.csv`,
   `forecasts.csv`). Features evolve independently (e.g. UPI Lite X grows
   fastest, Collect Requests declines).
5. **BI layer** detects growing/declining features, fastest-growing banks/PSPs,
   high-risk banks, PSP share loss, regional growth and success-rate anomalies
   (`bi_findings.csv`).
6. **Trend-triggered events**: the incident lifecycle (detect → bridge →
   investigate → RCA → decision → SOP → recovery) and the ingestible analytics
   documents (weekly BI notes; month-close feature/bank/PSP/market-share/mix/
   forecast/exec-KPI packs) are emitted from the simulated behaviour so the Brain
   can answer the V7.0 question set.

## Design guarantees

- **Ledger is ground truth**; cubes and analytics documents roll up from it, so
  numbers reconcile (ledger success rate ≈ workbook, max ≈ 0.01 pts).
- **One roster / one KPI spine.** The 15-KPI workbook and incident flags are
  preserved, so the existing executive layer is unchanged.
- **No orphans.** Every narrative/analytics artifact declares `Refs:` to ≥ 3
  others; the build fails on any dangling reference.
- **Deterministic.** `--seed` fully determines the roster, the ledger and every
  event; the same seed yields a byte-identical corpus.

## Output layout

```
enterprise_data/
├── master/
│   ├── *.csv                 employees, teams, products, features, merchants,
│   │                         banks, psps, customers, cities, ...
│   ├── analytics/*.csv       daily_metrics, feature/bank/psp/merchant/city_daily,
│   │                         hourly_distribution, transaction_mix,
│   │                         customer_activity, trends, bi_findings, forecasts
│   ├── ORG-OVERVIEW.md
│   └── upi_kpis_month.xlsx    Monthly KPIs + Bank/PSP/Merchant + Feature Volume
├── day_01/ … day_35/
│   ├── ledger/txns_day_XX.csv   sampled transaction ledger (data; not embedded)
│   ├── analytics/               weekly BI + month-close analytics docs (ingested)
│   ├── outlook/ teams/ meetings/ decisions/ incidents/ docs/ reports/ tasks/ excel/
├── scenarios/                STORYLINE.md + CROSS_REFERENCE_INDEX.md
├── INGEST_MANIFEST.json
└── CROSSREF.json
```

## Backend & frontend

- **`backend/app/executive/ecosystem.py`** — `EcosystemReader` loads the cubes
  (cached by corpus mtime); `EcosystemIntelligence` answers `overview`,
  `compare_features`, `feature_analytics`, `compare_banks`, `compare_psps`,
  `market_share`, `growth_leaders`, `city_trends`, `hourly_distribution`,
  `transaction_mix`, `anomalies`, `forecasts`, `executive_kpis`. Wired into the
  container as `container.ecosystem`.
- **API:** `GET /api/v1/executive/ecosystem[/…]` (overview, features,
  features/{id}, banks, psps, market-share, growth, cities, hourly, mix,
  anomalies, forecasts, kpis).
- **Frontend:** the **UPI Ecosystem** page (`/ecosystem`, in the Executive
  Workspace nav) — tabs for Overview, Features, Banks, PSPs, Cities, Trends &
  Forecast, and BI/Anomalies, rendered with ECharts.

## AI-ready questions

The ingested analytics documents let the Enterprise Brain answer, e.g.: which
UPI feature is growing fastest; compare P2P vs P2M / QR vs Intent / Lite vs
Autopay; which PSP lost share; which merchant category is growing; which feature
has the highest average ticket; market-share trend; which cities are growing;
and next-month directional forecasts.

## CLI

```
python generate_enterprise.py [--days 35] [--seed 2026] [--out enterprise_data]
                              [--week-start 2026-06-22] [--ledger-size 10000]
                              [--no-clean]
```

The generator writes master data, the 35 days, the ledger + cubes + analytics
docs, validates cross-reference integrity, and prints a summary (artifacts,
files, incidents, sampled transactions, cubes, trend series, BI findings). A
non-zero exit means an integrity problem.
