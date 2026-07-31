---
id: RPT-D101-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 15 Apr 2026)

**Report ID:** RPT-D101-DAILY · **Day 101 of 206** · **Derived from:** 10,866 transaction rows queried live from the warehouse

## Summary

The rail took **10,866 payment attempts** on Wednesday 15 April 2026 (Working day) and settled **₹1.48 Cr** across 10,358 successful payments. Volume was −9.2% on yesterday and −19.4% on the same weekday last week. Success closed at **95.32%**, below the trailing 28-day median of 95.94%.

Retries reached 180 attempts (1.66% of the day, 3.1 sigma above normal). 66.1% of re-presented payments recovered, so the retry path was doing its job. Decline code ZM (Invalid UPI PIN) fired 141 times — 1.298% of attempts against a trailing 1.015%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,866 | −9.2% | −19.4% | 12,629 |
| Successful payments | 10,358 | −9.3% | −20.0% | 12,061 |
| Success rate | 95.32% | −0.09pp | −0.65pp | 95.48% |
| Settled value | ₹1.48 Cr | +4.9% | −15.8% | ₹1.63 Cr |
| Average ticket | ₹1,433 | +15.7% | +5.2% | ₹1,346 |
| Technical declines | 0.515% | −0.03pp | −0.04pp | 0.531% |
| Business declines | 3.488% | +0.03pp | +0.61pp | 3.131% |
| Risk declines | 0.175% | +0.03pp | +0.07pp | 0.145% |
| Timeout declines | 0.414% | +0.09pp | +0.04pp | 0.592% |
| Retry share | 1.66% | +0.16pp | +0.43pp | 1.56% |
| Latency p95 | 1,280 ms | +4.6% | +1.9% | 1,323 ms |
| Active customers | 9,263 | −7.2% | −16.8% | 10,493 |
| Active merchants | 1,282 | −5.7% | −7.9% | 1,377 |

## What moved

- Success rate closed at 95.32%, 0.61pp down the trailing median — a 1.7-sigma move.
- Region North ran at 94.93% success on 2,760 attempts (25.4% of the day), 0.90pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 35% across the trailing window to 271 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 227 today, with success holding, so the growth is healthy and worth funding.
- Category Mobility ran at 95.64% success on 734 attempts (10.5% of the day), 1.13pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,877 | 35.7% | 94.82% | ₹41.27 L | −12.9% |
| UPI Person to Merchant | 2,873 | 26.4% | 95.37% | ₹27.15 L | −17.7% |
| UPI QR Payments | 1,679 | 15.5% | 96.31% | ₹6.87 L | −22.7% |
| UPI Lite | 948 | 8.7% | 98.63% | ₹91,492 | −10.9% |
| RuPay Credit on UPI | 323 | 3.0% | 95.98% | ₹16.57 L | +25.7% |
| UPI AutoPay | 299 | 2.8% | 90.30% | ₹5.46 L | −6.7% |
| Credit on UPI | 271 | 2.5% | 94.83% | ₹23.40 L | +52.7% |
| UPI Circle | 227 | 2.1% | 96.04% | ₹2.11 L | −10.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,482 | 95.12% | 95.96% | ₹46.19 L | normal |
| HDFC Bank | 1,222 | 96.32% | 95.92% | ₹15.86 L | normal |
| Bank of Baroda | 879 | 95.34% | 95.83% | ₹9.70 L | normal |
| Union Bank of India | 719 | 93.88% | 95.92% | ₹13.08 L | ⚠ outlier |
| Punjab National Bank | 657 | 96.04% | 95.30% | ₹8.03 L | normal |
| ICICI Bank | 640 | 95.94% | 96.29% | ₹9.48 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,105 | 95.48% | 95.82% | ₹75.46 L | normal |
| Google Pay | 3,622 | 95.42% | 95.76% | ₹45.19 L | normal |
| Paytm | 931 | 94.74% | 95.91% | ₹11.32 L | normal |
| Navi | 403 | 94.79% | 95.88% | ₹4.57 L | normal |
| SuperMoney | 193 | 93.78% | 95.26% | ₹2.17 L | normal |
| BHIM | 114 | 93.86% | 96.28% | ₹1.61 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,908 | 95.94% | ₹32.64 L |
| Food & Beverage | 1,683 | 96.85% | ₹9.03 L |
| Mobility | 734 | 95.64% | ₹3.70 L |
| Bills | 718 | 94.57% | ₹9.74 L |
| Healthcare | 370 | 96.49% | ₹8.86 L |
| Digital | 192 | 93.23% | ₹83,074 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,343 | 30.8% | 95.21% | ₹47.17 L |
| North | 2,760 | 25.4% | 94.93% | ₹35.59 L |
| West | 2,699 | 24.8% | 95.67% | ₹38.95 L |
| East | 1,096 | 10.1% | 94.89% | ₹17.02 L |
| Central | 968 | 8.9% | 96.38% | ₹9.73 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 80 | 98.75% | ₹1.50 L |
| Vega Electronics | Large | Retail | 27 | 96.30% | ₹1.25 L |
| Rapid Bazaar | Key Account | Retail | 319 | 94.36% | ₹1.03 L |
| Ujjwal Water Board | Key Account | Bills | 34 | 97.06% | ₹1.01 L |
| Girnar Connect | Key Account | Bills | 113 | 94.69% | ₹68,367 |
| Yamuna Restaurant | Key Account | Food & Beverage | 57 | 96.49% | ₹55,700 |
| Urban Boutique | Key Account | Retail | 82 | 96.34% | ₹54,816 |
| Hampi Stores 2298 | Key Account | Retail | 77 | 97.40% | ₹42,329 |

## Failure analysis

Of 499 declined attempts, 379 were business declines (3.488% of attempts — balances, PINs and limits), 56 technical (0.515%), 45 timeouts (0.414%) and 19 risk declines (0.175%).

180 attempts were re-presentations of an earlier failure (1.66% of the day); 66.1% of them succeeded.

- Retries reached 180 attempts (1.66% of the day, 3.1 sigma above normal). 66.1% of re-presented payments recovered, so the retry path was doing its job.
- Decline code ZM (Invalid UPI PIN) fired 141 times — 1.298% of attempts against a trailing 1.015%. Owner: Customer.
- Decline code U69 (Beneficiary bank offline) fired 15 times — 0.138% of attempts against a trailing 0.063%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 15 times — 0.138% of attempts against a trailing 0.102%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 142 | 1.307% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 141 | 1.298% | 1.015% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.460% | 0.359% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.193% | 0.224% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.193% | 0.188% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.184% | 0.175% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.147% | 0.116% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.138% | 0.102% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 92 | 76 |
| Auto-reversals | 18 | 22 |
| Disputes / chargebacks | 5 | 11 |
| Value returned | ₹1.21 L | ₹1.61 L |

## Customer behaviour

9,263 distinct customers transacted (−12.6% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,883 | 3,253 | 1.13 | 95.20% | ₹1,449 |
| power | 1,971 | 2,529 | 1.28 | 95.57% | ₹1,993 |
| merchant_heavy | 2,092 | 2,431 | 1.16 | 95.02% | ₹1,068 |
| small_ticket | 1,375 | 1,664 | 1.21 | 95.19% | ₹670 |
| occasional | 734 | 770 | 1.05 | 95.84% | ₹1,471 |
| new | 172 | 183 | 1.06 | 96.17% | ₹975 |
| dormant_returning | 36 | 36 | 1.00 | 100.00% | ₹2,018 |

## Operational events

- **INC-PSP-0033** (Sev-1) — SuperMoney app release regression, scoped to SuperMoney between 18:00 and 23:00. A SuperMoney client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-PSP-0030** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 16:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 141 times — 1.298% of attempts against a trailing 1.015%. Owner: Customer.
- Success rate closed at 95.32%, 0.61pp down the trailing median — a 1.7-sigma move.
- Region North ran at 94.93% success on 2,760 attempts (25.4% of the day), 0.90pp down its own 28-day median.
- Decline code U69 (Beneficiary bank offline) fired 15 times — 0.138% of attempts against a trailing 0.063%. Owner: Issuer.
- Category Mobility ran at 95.64% success on 734 attempts (10.5% of the day), 1.13pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 35% across the trailing window to 271 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 227 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

15 April was an incident day: INC-PSP-0033, INC-PSP-0030 were live and the rail closed at 95.32% success against a 95.94% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,866, successes=10,358, failed=499, pending=9, settled_value_inr=14,846,336.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-PSP-0033; kind=psp_degradation; severity=Sev-1; window=2026-04-15 to 2026-04-18; success_impact_pp=-23.53; volume_impact_pct=-36.83
- failures: retries=180; retry_share_pct=1.66; recovery_pct=66.11; z=3.06
- failures: failure_code=ZM; count=141; rate_pct=1.3; trailing_rate_pct=1.02; owner=Customer; z=2.8
- incidents: event_id=INC-PSP-0030; kind=psp_degradation; severity=Sev-2; window=2026-04-14 to 2026-04-16; success_impact_pp=-7.77; volume_impact_pct=-12.17
- headline: success_rate=95.32; trailing_median=95.94; z=-1.69
- geography: region=North; attempts=2,760; success_rate=94.93; own_median=95.83; z=-2.64
- failures: failure_code=U69; count=15; rate_pct=0.14; trailing_rate_pct=0.06; owner=Issuer; z=3.45
- products: product_name=Credit on UPI; attempts=271; window_growth_pct=35.3; success_rate=94.83
- products: product_name=UPI Circle; attempts=227; window_growth_pct=34.1; success_rate=96.04
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83

Refs: enterprise_data/warehouse/transactions, RPT-D100-DAILY, enterprise_data/warehouse/reference/incidents.parquet
