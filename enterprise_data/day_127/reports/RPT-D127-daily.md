---
id: RPT-D127-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 11 May 2026)

**Report ID:** RPT-D127-DAILY · **Day 127 of 206** · **Derived from:** 13,671 transaction rows queried live from the warehouse

## Summary

The rail took **13,671 payment attempts** on Monday 11 May 2026 (Working day) and settled **₹1.92 Cr** across 13,169 successful payments. Volume was +0.2% on yesterday and −11.3% on the same weekday last week. Success closed at **96.33%**, above the trailing 28-day median of 95.64%.

Product UPI Circle is compounding — attempts up 66% across the trailing window to 479 today, with success holding, so the growth is healthy and worth funding. Product UPI Person to Person ran at 95.90% success on 4,098 attempts (30.0% of the day), 0.94pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,671 | +0.2% | −11.3% | 15,321 |
| Successful payments | 13,169 | +0.7% | −11.0% | 14,713 |
| Success rate | 96.33% | +0.53pp | +0.26pp | 96.04% |
| Settled value | ₹1.92 Cr | +20.8% | −9.8% | ₹2.02 Cr |
| Average ticket | ₹1,461 | +20.0% | +1.3% | ₹1,367 |
| Technical declines | 0.417% | −0.03pp | −0.13pp | 0.496% |
| Business declines | 2.765% | −0.41pp | −0.16pp | 2.911% |
| Risk declines | 0.110% | −0.00pp | +0.05pp | 0.123% |
| Timeout declines | 0.285% | −0.04pp | +0.03pp | 0.325% |
| Retry share | 1.16% | −0.51pp | +0.03pp | 1.30% |
| Latency p95 | 1,252 ms | +3.3% | +1.6% | 1,242 ms |
| Active customers | 11,339 | +0.5% | −9.7% | 12,396 |
| Active merchants | 1,484 | +3.3% | +0.6% | 1,498 |

## What moved

- Product UPI Circle is compounding — attempts up 66% across the trailing window to 479 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Person ran at 95.90% success on 4,098 attempts (30.0% of the day), 0.94pp up its own 28-day median.
- Product UPI Lite is compounding — attempts up 54% across the trailing window to 1,594 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,098 | 30.0% | 95.90% | ₹43.58 L | −6.5% |
| UPI Person to Merchant | 3,913 | 28.6% | 95.73% | ₹36.38 L | +7.5% |
| UPI QR Payments | 2,094 | 15.3% | 96.94% | ₹8.25 L | −10.7% |
| UPI Lite | 1,594 | 11.7% | 99.06% | ₹1.55 L | +19.8% |
| UPI Circle | 479 | 3.5% | 98.12% | ₹4.26 L | +20.4% |
| Credit on UPI | 373 | 2.7% | 97.59% | ₹30.41 L | +40.2% |
| RuPay Credit on UPI | 373 | 2.7% | 95.98% | ₹27.32 L | +6.6% |
| UPI AutoPay | 321 | 2.3% | 89.72% | ₹5.35 L | −1.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,256 | 96.03% | 95.83% | ₹59.23 L | normal |
| HDFC Bank | 1,503 | 96.41% | 95.96% | ₹27.84 L | normal |
| Bank of Baroda | 1,044 | 96.65% | 95.77% | ₹16.49 L | normal |
| Union Bank of India | 918 | 94.44% | 94.95% | ₹12.64 L | normal |
| Punjab National Bank | 856 | 96.38% | 95.52% | ₹11.99 L | normal |
| ICICI Bank | 847 | 97.76% | 96.39% | ₹9.20 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,480 | 96.36% | 95.76% | ₹87.40 L | normal |
| Google Pay | 4,563 | 96.63% | 95.48% | ₹65.55 L | normal |
| Paytm | 1,056 | 96.40% | 95.66% | ₹14.35 L | normal |
| Navi | 501 | 95.01% | 95.40% | ₹8.09 L | normal |
| SuperMoney | 261 | 96.93% | 95.62% | ₹4.30 L | normal |
| BHIM | 132 | 93.18% | 95.24% | ₹1.55 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,087 | 96.43% | ₹54.88 L |
| Food & Beverage | 2,401 | 97.33% | ₹12.90 L |
| Mobility | 1,075 | 97.77% | ₹5.66 L |
| Bills | 824 | 96.36% | ₹7.96 L |
| Healthcare | 484 | 96.28% | ₹4.54 L |
| Digital | 221 | 93.67% | ₹94,448 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,025 | 29.4% | 95.93% | ₹56.50 L |
| West | 3,427 | 25.1% | 96.32% | ₹46.52 L |
| North | 3,427 | 25.1% | 96.64% | ₹48.60 L |
| East | 1,588 | 11.6% | 96.28% | ₹26.51 L |
| Central | 1,204 | 8.8% | 96.84% | ₹14.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 88 | 97.73% | ₹3.15 L |
| Vega Electronics | Large | Retail | 38 | 100.00% | ₹2.49 L |
| Rapid Bazaar | Key Account | Retail | 405 | 97.53% | ₹1.64 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 98.63% | ₹1.25 L |
| Urban Boutique | Key Account | Retail | 134 | 97.76% | ₹1.14 L |
| Hampi Styles | Key Account | Retail | 35 | 100.00% | ₹90,482 |
| Hampi Stores 2298 | Key Account | Retail | 110 | 96.36% | ₹87,685 |
| Girnar Connect | Key Account | Bills | 151 | 95.36% | ₹69,913 |

## Failure analysis

Of 489 declined attempts, 378 were business declines (2.765% of attempts — balances, PINs and limits), 57 technical (0.417%), 39 timeouts (0.285%) and 15 risk declines (0.110%).

159 attempts were re-presentations of an earlier failure (1.16% of the day); 66.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 164 | 1.200% | 1.267% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 1.009% | 1.054% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.315% | 0.378% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.197% | 0.220% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.132% | 0.176% |
| XH | Account does not exist / frozen | business | Issuer | 18 | 0.132% | 0.220% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.117% | 0.137% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.102% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 108 | 89 |
| Auto-reversals | 17 | 28 |
| Disputes / chargebacks | 14 | 11 |
| Value returned | ₹2.10 L | ₹1.43 L |

## Customer behaviour

11,339 distinct customers transacted (+0.6% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,496 | 3,996 | 1.14 | 96.95% | ₹1,548 |
| power | 2,436 | 3,244 | 1.33 | 95.93% | ₹1,845 |
| merchant_heavy | 2,644 | 3,213 | 1.22 | 96.05% | ₹1,151 |
| small_ticket | 1,662 | 2,054 | 1.24 | 95.86% | ₹773 |
| occasional | 893 | 941 | 1.05 | 96.60% | ₹1,601 |
| new | 187 | 202 | 1.08 | 98.02% | ₹1,247 |
| dormant_returning | 21 | 21 | 1.00 | 100.00% | ₹1,260 |

## Operational events

- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **INC-BANK-0001** (Sev-3) — Yes Bank issuer decline spike, scoped to Yes Bank between 23:00 and 05:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 66% across the trailing window to 479 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 54% across the trailing window to 1,594 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 11 May: success came in 0.69pp above baseline at 96.33% on 13,671 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,671, successes=13,169, failed=489, pending=13, settled_value_inr=19,240,878.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=479; window_growth_pct=66.2; success_rate=98.12
- products: product_name=UPI Person to Person; attempts=4,098; success_rate=95.9; own_median=94.96; z=2.99
- products: product_name=UPI Lite; attempts=1,594; window_growth_pct=53.7; success_rate=99.06
- incidents: event_id=MAINT-0086; kind=maintenance_window; severity=Sev-3; window=2026-01-11 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- incidents: event_id=INC-BANK-0001; kind=bank_outage; severity=Sev-3; window=2026-05-08 to 2026-05-12; success_impact_pp=-6.2; volume_impact_pct=-5.5
- banks: payer_bank=Axis Bank; attempts=838; success_rate=98.09; own_median=95.92; z=2.65
- banks: payer_bank=Indian Bank; attempts=464; success_rate=98.28; own_median=95.11; z=3.5
- banks: payer_bank=IndusInd Bank; attempts=290; success_rate=98.62; own_median=95.68; z=2.31
- categories: mcc_category=Services; attempts=132; own_median=103.5; z=2.56

Refs: enterprise_data/warehouse/transactions, RPT-D126-DAILY, enterprise_data/warehouse/reference/incidents.parquet
