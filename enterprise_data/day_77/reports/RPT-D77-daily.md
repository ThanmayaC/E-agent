---
id: RPT-D77-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 22 Mar 2026)

**Report ID:** RPT-D77-DAILY · **Day 77 of 206** · **Derived from:** 11,312 transaction rows queried live from the warehouse

## Summary

The rail took **11,312 payment attempts** on Sunday 22 March 2026 (Weekend) and settled **₹1.07 Cr** across 10,853 successful payments. Volume was −27.0% on yesterday and +9.1% on the same weekday last week. Success closed at **95.94%**, in line with the trailing 28-day median of 95.79%.

Product UPI Circle is compounding — attempts up 91% across the trailing window to 251 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,312 | −27.0% | +9.1% | 12,822 |
| Successful payments | 10,853 | −26.9% | +10.3% | 12,284 |
| Success rate | 95.94% | +0.05pp | +0.99pp | 95.78% |
| Settled value | ₹1.07 Cr | −33.0% | +1.4% | ₹1.44 Cr |
| Average ticket | ₹983 | −8.4% | −8.0% | ₹1,172 |
| Technical declines | 0.380% | −0.13pp | −0.10pp | 0.453% |
| Business declines | 3.324% | +0.23pp | −0.64pp | 3.213% |
| Risk declines | 0.053% | −0.09pp | −0.03pp | 0.121% |
| Timeout declines | 0.203% | −0.10pp | −0.18pp | 0.332% |
| Retry share | 1.03% | +0.01pp | −0.54pp | 1.25% |
| Latency p95 | 1,216 ms | +2.0% | −0.8% | 1,240 ms |
| Active customers | 9,562 | −23.3% | +8.9% | 10,578 |
| Active merchants | 1,273 | −7.4% | +1.5% | 1,325 |

## What moved

- Product UPI Circle is compounding — attempts up 91% across the trailing window to 251 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 47% across the trailing window to 1,007 today, with success holding, so the growth is healthy and worth funding.
- Region West ran at 96.80% success on 2,750 attempts (24.3% of the day), 1.14pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,895 | 34.4% | 94.94% | ₹38.84 L | −12.7% |
| UPI Person to Merchant | 3,173 | 28.0% | 96.44% | ₹29.84 L | −9.1% |
| UPI QR Payments | 2,164 | 19.1% | 96.44% | ₹7.81 L | +0.9% |
| UPI Lite | 1,007 | 8.9% | 98.91% | ₹82,155 | +14.3% |
| UPI AutoPay | 316 | 2.8% | 91.14% | ₹5.83 L | +1.4% |
| UPI Circle | 251 | 2.2% | 96.81% | ₹1.89 L | +44.7% |
| RuPay Credit on UPI | 118 | 1.0% | 97.46% | ₹4.48 L | −46.7% |
| Recurring Payments | 94 | 0.8% | 91.49% | ₹5.14 L | +1.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,553 | 96.14% | 95.59% | ₹35.74 L | normal |
| HDFC Bank | 1,205 | 94.77% | 95.79% | ₹11.06 L | normal |
| Bank of Baroda | 849 | 95.29% | 95.58% | ₹8.78 L | normal |
| Union Bank of India | 804 | 96.39% | 95.30% | ₹7.35 L | normal |
| ICICI Bank | 720 | 95.00% | 95.94% | ₹5.39 L | normal |
| Axis Bank | 701 | 96.43% | 95.98% | ₹7.51 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,247 | 95.92% | 95.87% | ₹50.00 L | normal |
| Google Pay | 3,790 | 95.88% | 95.71% | ₹35.87 L | normal |
| Paytm | 935 | 96.79% | 95.58% | ₹8.58 L | normal |
| Navi | 424 | 95.75% | 95.68% | ₹4.61 L | normal |
| SuperMoney | 226 | 96.46% | 95.73% | ₹1.85 L | normal |
| BHIM | 114 | 95.61% | 95.01% | ₹65,476 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,266 | 97.03% | ₹26.05 L |
| Food & Beverage | 1,903 | 96.74% | ₹7.07 L |
| Mobility | 769 | 96.62% | ₹3.47 L |
| Bills | 615 | 95.93% | ₹7.05 L |
| Healthcare | 360 | 95.28% | ₹2.92 L |
| Digital | 205 | 95.61% | ₹1.41 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,314 | 29.3% | 95.68% | ₹31.08 L |
| North | 2,876 | 25.4% | 95.69% | ₹28.53 L |
| West | 2,750 | 24.3% | 96.80% | ₹26.42 L |
| East | 1,307 | 11.6% | 95.64% | ₹12.67 L |
| Central | 1,065 | 9.4% | 95.59% | ₹7.95 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 385 | 96.88% | ₹1.49 L |
| Vasant Wardrobe | Key Account | Retail | 62 | 98.39% | ₹1.07 L |
| Vega Electronics | Large | Retail | 16 | 93.75% | ₹60,974 |
| Hampi Styles | Key Account | Retail | 32 | 96.88% | ₹60,274 |
| Zenith Mart 1521 | Large | Retail | 27 | 100.00% | ₹54,117 |
| Tejas Bites | Key Account | Food & Beverage | 138 | 96.38% | ₹50,325 |
| Girnar Connect | Key Account | Bills | 108 | 99.07% | ₹45,382 |
| Hampi Stores 2298 | Key Account | Retail | 69 | 97.10% | ₹43,173 |

## Failure analysis

Of 448 declined attempts, 376 were business declines (3.324% of attempts — balances, PINs and limits), 43 technical (0.380%), 23 timeouts (0.203%) and 6 risk declines (0.053%).

116 attempts were re-presentations of an earlier failure (1.03% of the day); 64.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 173 | 1.529% | 1.346% |
| ZM | Invalid UPI PIN | business | Customer | 115 | 1.017% | 1.086% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.327% | 0.397% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.256% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.159% | 0.179% |
| UX | Mandate execution outside permitted window | business | PSP | 13 | 0.115% | 0.089% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.115% | 0.124% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 10 | 0.088% | 0.107% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 73 | 76 |
| Auto-reversals | 23 | 24 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹86,854 | ₹1.16 L |

## Customer behaviour

9,562 distinct customers transacted (−5.3% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,970 | 3,342 | 1.13 | 96.32% | ₹989 |
| power | 2,046 | 2,709 | 1.32 | 96.23% | ₹1,302 |
| merchant_heavy | 2,126 | 2,485 | 1.17 | 95.53% | ₹731 |
| small_ticket | 1,412 | 1,726 | 1.22 | 95.65% | ₹416 |
| occasional | 789 | 821 | 1.04 | 95.01% | ₹1,274 |
| new | 184 | 194 | 1.05 | 98.45% | ₹1,119 |
| dormant_returning | 35 | 35 | 1.00 | 88.57% | ₹1,109 |

## Operational events

- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 91% across the trailing window to 251 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 47% across the trailing window to 1,007 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

22 March ran on trend at 95.94% success and ₹1.07 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 91% across the trailing window to 251 today, with success holding, so the growth is healthy and worth funding. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,312, successes=10,853, failed=448, pending=11, settled_value_inr=10,665,326.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=251; window_growth_pct=91; success_rate=96.81
- products: product_name=UPI Lite; attempts=1,007; window_growth_pct=47.5; success_rate=98.91
- geography: region=West; attempts=2,750; success_rate=96.8; own_median=95.66; z=2.22
- banks: payer_bank=Yes Bank; attempts=430; success_rate=98.14; own_median=95.54; z=2.94
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- products: product_name=RuPay Credit on UPI; attempts=118; own_median=221.5; z=-2.45
- products: product_name=Credit on UPI; attempts=81; own_median=148.5; z=-2.22

Refs: enterprise_data/warehouse/transactions, RPT-D76-DAILY, enterprise_data/warehouse/reference/incidents.parquet
