---
id: RPT-D82-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 27 Mar 2026)

**Report ID:** RPT-D82-DAILY · **Day 82 of 206** · **Derived from:** 12,257 transaction rows queried live from the warehouse

## Summary

The rail took **12,257 payment attempts** on Friday 27 March 2026 (Ram Navami) and settled **₹1.49 Cr** across 11,727 successful payments. Volume was +19.2% on yesterday and −8.3% on the same weekday last week. Success closed at **95.68%**, in line with the trailing 28-day median of 95.79%.

Retries reached 356 attempts (2.90% of the day, 8.5 sigma above normal). 71.3% of re-presented payments recovered, so the retry path was doing its job. 49 auto-reversals were raised, 4.2 sigma above the trailing median of 24.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,257 | +19.2% | −8.3% | 12,430 |
| Successful payments | 11,727 | +26.6% | −8.6% | 11,883 |
| Success rate | 95.68% | +5.56pp | −0.38pp | 95.53% |
| Settled value | ₹1.49 Cr | +16.3% | +4.8% | ₹1.41 Cr |
| Average ticket | ₹1,272 | −8.1% | +14.7% | ₹1,192 |
| Technical declines | 0.302% | −1.36pp | −0.11pp | 0.482% |
| Business declines | 3.525% | −0.58pp | +0.64pp | 3.314% |
| Risk declines | 0.073% | −0.09pp | −0.11pp | 0.123% |
| Timeout declines | 0.326% | −3.45pp | −0.04pp | 0.449% |
| Retry share | 2.90% | −1.97pp | +1.87pp | 1.45% |
| Latency p95 | 1,329 ms | −42.4% | +8.3% | 1,288 ms |
| Active customers | 10,249 | +20.8% | −7.4% | 10,298 |
| Active merchants | 1,336 | +5.2% | −0.1% | 1,319 |

## What moved

- Product UPI International is compounding — attempts up 38% across the trailing window to 109 today, with success holding, so the growth is healthy and worth funding.
- Category Bills carried 1,024 attempts, 47% up its trailing median and 13.3% of the day's volume.
- Product UPI QR Payments ran at 97.45% success on 1,963 attempts (16.0% of the day), 0.93pp up its own 28-day median.
- Category Bills ran at 93.55% success on 1,024 attempts (13.3% of the day), 2.16pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,578 | 37.4% | 95.30% | ₹49.15 L | +2.6% |
| UPI Person to Merchant | 3,454 | 28.2% | 95.83% | ₹33.01 L | −1.0% |
| UPI QR Payments | 1,963 | 16.0% | 97.45% | ₹8.66 L | −9.2% |
| UPI Lite | 823 | 6.7% | 99.27% | ₹78,877 | −10.1% |
| UPI AutoPay | 337 | 2.7% | 86.35% | ₹5.06 L | +7.2% |
| RuPay Credit on UPI | 245 | 2.0% | 96.73% | ₹13.68 L | +8.6% |
| Credit on UPI | 234 | 1.9% | 97.01% | ₹18.24 L | +50.0% |
| UPI Circle | 226 | 1.8% | 96.46% | ₹1.92 L | +24.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,011 | 95.94% | 95.72% | ₹47.79 L | normal |
| HDFC Bank | 1,261 | 95.24% | 95.71% | ₹15.38 L | normal |
| Bank of Baroda | 950 | 94.74% | 95.64% | ₹14.23 L | normal |
| Union Bank of India | 801 | 95.88% | 95.43% | ₹8.40 L | normal |
| Punjab National Bank | 758 | 96.44% | 95.41% | ₹8.89 L | normal |
| Axis Bank | 740 | 95.81% | 96.12% | ₹6.80 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,855 | 95.83% | 95.95% | ₹75.63 L | normal |
| Google Pay | 3,938 | 95.53% | 95.71% | ₹44.85 L | normal |
| Paytm | 1,014 | 95.66% | 95.65% | ₹11.29 L | normal |
| Navi | 464 | 95.26% | 95.68% | ₹5.61 L | normal |
| SuperMoney | 230 | 95.22% | 95.43% | ₹3.38 L | normal |
| BHIM | 130 | 96.15% | 95.45% | ₹1.21 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,178 | 96.60% | ₹34.31 L |
| Food & Beverage | 1,706 | 96.78% | ₹8.51 L |
| Bills | 1,024 | 93.55% | ₹10.89 L |
| Mobility | 749 | 98.13% | ₹4.61 L |
| Healthcare | 353 | 97.73% | ₹5.73 L |
| Digital | 280 | 90.71% | ₹1.33 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,596 | 29.3% | 95.94% | ₹47.82 L |
| North | 3,138 | 25.6% | 95.63% | ₹36.37 L |
| West | 2,975 | 24.3% | 95.26% | ₹35.90 L |
| East | 1,513 | 12.3% | 96.10% | ₹19.12 L |
| Central | 1,035 | 8.4% | 95.46% | ₹10.00 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 67 | 97.01% | ₹2.12 L |
| Vega Electronics | Large | Retail | 30 | 86.67% | ₹1.97 L |
| Rapid Bazaar | Key Account | Retail | 296 | 97.64% | ₹1.69 L |
| Hampi Styles | Key Account | Retail | 27 | 92.59% | ₹92,667 |
| Girnar Connect | Key Account | Bills | 173 | 94.80% | ₹86,605 |
| Ujjwal Water Board | Key Account | Bills | 62 | 90.32% | ₹86,149 |
| Zenith Diner | Large | Food & Beverage | 25 | 96.00% | ₹80,873 |
| Hampi Stores 2298 | Key Account | Retail | 106 | 95.28% | ₹79,515 |

## Failure analysis

Of 518 declined attempts, 432 were business declines (3.525% of attempts — balances, PINs and limits), 37 technical (0.302%), 40 timeouts (0.326%) and 9 risk declines (0.073%).

356 attempts were re-presentations of an earlier failure (2.90% of the day); 71.3% of them succeeded.

- Retries reached 356 attempts (2.90% of the day, 8.5 sigma above normal). 71.3% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 192 | 1.566% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 144 | 1.175% | 1.082% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.351% | 0.391% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.220% | 0.224% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.155% | 0.158% |
| UX | Mandate execution outside permitted window | business | PSP | 18 | 0.147% | 0.089% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.131% | 0.118% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.106% | 0.101% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 73 | 78 |
| Auto-reversals | 49 | 24 |
| Disputes / chargebacks | 8 | 10 |
| Value returned | ₹1.30 L | ₹1.26 L |

## Customer behaviour

10,249 distinct customers transacted (+1.5% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,105 | 3,514 | 1.13 | 95.90% | ₹1,216 |
| power | 2,201 | 2,917 | 1.33 | 95.99% | ₹1,765 |
| merchant_heavy | 2,316 | 2,788 | 1.20 | 95.09% | ₹1,112 |
| small_ticket | 1,549 | 1,895 | 1.22 | 95.36% | ₹550 |
| occasional | 836 | 883 | 1.06 | 96.26% | ₹1,302 |
| new | 215 | 233 | 1.08 | 95.71% | ₹700 |
| dormant_returning | 27 | 27 | 1.00 | 96.30% | ₹1,727 |

## Operational events

- **INC-NET-0035** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 19:00 and 24:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 49 auto-reversals were raised, 4.2 sigma above the trailing median of 24.
- Category Bills ran at 93.55% success on 1,024 attempts (13.3% of the day), 2.16pp down its own 28-day median.
- Product UPI AutoPay ran at 86.35% success on 337 attempts (2.7% of the day), 4.46pp down its own 28-day median.
- Product Recurring Payments ran at 80.00% success on 110 attempts (0.9% of the day), 8.48pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 38% across the trailing window to 109 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

27 March was an incident day: INC-NET-0035 was live and the rail closed at 95.68% success against a 95.79% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,257, successes=11,727, failed=518, pending=12, settled_value_inr=14,921,862.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=356; retry_share_pct=2.9; recovery_pct=71.35; z=8.48
- incidents: event_id=INC-NET-0035; kind=network_latency; severity=Sev-1; window=2026-03-26 to 2026-03-27; success_impact_pp=-13.9; volume_impact_pct=-12.83
- adjustments: reversals=49; trailing_median=24; z=4.22
- products: product_name=UPI International; attempts=109; window_growth_pct=37.8; success_rate=94.5
- categories: mcc_category=Bills; attempts=1,024; own_median=694.5; z=3.7
- products: product_name=UPI QR Payments; attempts=1,963; success_rate=97.45; own_median=96.52; z=2.42
- categories: mcc_category=Bills; attempts=1,024; success_rate=93.55; own_median=95.71; z=-2.12
- products: product_name=UPI AutoPay; attempts=337; success_rate=86.35; own_median=90.81; z=-2.77
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- incidents: event_id=CMP-0057; kind=merchant_campaign; severity=Sev-3; window=2026-03-25 to 2026-04-01; success_impact_pp=-0.07; volume_impact_pct=28.96

Refs: enterprise_data/warehouse/transactions, RPT-D81-DAILY, enterprise_data/warehouse/reference/incidents.parquet
