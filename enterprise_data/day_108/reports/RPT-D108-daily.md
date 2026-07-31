---
id: RPT-D108-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 22 Apr 2026)

**Report ID:** RPT-D108-DAILY · **Day 108 of 206** · **Derived from:** 10,926 transaction rows queried live from the warehouse

## Summary

The rail took **10,926 payment attempts** on Wednesday 22 April 2026 (Working day) and settled **₹1.60 Cr** across 10,406 successful payments. Volume was −15.4% on yesterday and +0.6% on the same weekday last week. Success closed at **95.24%**, below the trailing 28-day median of 95.92%.

Decline code BT (Acquirer / NPCI switch timeout) fired 24 times — 0.220% of attempts against a trailing 0.107%. Owner: NPCI.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,926 | −15.4% | +0.6% | 12,877 |
| Successful payments | 10,406 | −16.0% | +0.5% | 12,276 |
| Success rate | 95.24% | −0.60pp | −0.08pp | 95.29% |
| Settled value | ₹1.60 Cr | −11.6% | +7.7% | ₹1.66 Cr |
| Average ticket | ₹1,537 | +5.2% | +7.2% | ₹1,352 |
| Technical declines | 0.522% | +0.00pp | +0.01pp | 0.586% |
| Business declines | 3.515% | +0.45pp | +0.03pp | 3.148% |
| Risk declines | 0.128% | +0.04pp | −0.05pp | 0.141% |
| Timeout declines | 0.476% | +0.10pp | +0.06pp | 0.716% |
| Retry share | 1.49% | +0.40pp | −0.16pp | 1.69% |
| Latency p95 | 1,250 ms | −2.1% | −2.3% | 1,348 ms |
| Active customers | 9,319 | −13.6% | +0.6% | 10,664 |
| Active merchants | 1,362 | −2.9% | +6.2% | 1,388 |

## What moved

- Success rate closed at 95.24%, 0.68pp down the trailing median — a 1.6-sigma move.
- Product UPI Circle is compounding — attempts up 47% across the trailing window to 300 today, with success holding, so the growth is healthy and worth funding.
- Region South ran at 94.23% success on 3,226 attempts (29.5% of the day), 1.62pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 39% across the trailing window to 957 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,641 | 33.3% | 94.29% | ₹37.90 L | −17.6% |
| UPI Person to Merchant | 2,839 | 26.0% | 95.88% | ₹28.12 L | −18.1% |
| UPI QR Payments | 1,902 | 17.4% | 95.90% | ₹7.42 L | −12.4% |
| UPI Lite | 957 | 8.8% | 98.12% | ₹82,735 | −13.0% |
| UPI AutoPay | 319 | 2.9% | 90.60% | ₹6.86 L | −1.2% |
| RuPay Credit on UPI | 315 | 2.9% | 95.87% | ₹21.80 L | +5.2% |
| UPI Circle | 300 | 2.7% | 96.33% | ₹2.35 L | +9.3% |
| Credit on UPI | 256 | 2.3% | 92.19% | ₹17.39 L | +24.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,384 | 94.77% | 95.92% | ₹51.27 L | normal |
| HDFC Bank | 1,192 | 95.39% | 95.95% | ₹18.51 L | normal |
| Bank of Baroda | 822 | 95.99% | 95.88% | ₹12.52 L | normal |
| Union Bank of India | 766 | 94.78% | 95.72% | ₹8.42 L | normal |
| Axis Bank | 674 | 97.03% | 95.74% | ₹11.52 L | normal |
| Punjab National Bank | 662 | 94.86% | 95.60% | ₹11.99 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,311 | 95.71% | 95.80% | ₹77.03 L | normal |
| Google Pay | 3,471 | 94.73% | 95.63% | ₹48.97 L | normal |
| Paytm | 903 | 94.57% | 95.85% | ₹12.97 L | normal |
| Navi | 390 | 94.87% | 96.24% | ₹6.09 L | normal |
| SuperMoney | 209 | 97.13% | 94.71% | ₹4.80 L | normal |
| BHIM | 117 | 95.73% | 96.12% | ₹1.66 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,076 | 96.29% | ₹35.09 L |
| Food & Beverage | 1,772 | 96.39% | ₹7.54 L |
| Mobility | 815 | 96.20% | ₹4.87 L |
| Bills | 653 | 94.64% | ₹9.08 L |
| Healthcare | 363 | 96.14% | ₹5.03 L |
| Financial Services | 172 | 86.05% | ₹9.49 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,226 | 29.5% | 94.23% | ₹41.54 L |
| North | 2,798 | 25.6% | 95.85% | ₹41.42 L |
| West | 2,617 | 24.0% | 95.57% | ₹38.86 L |
| East | 1,330 | 12.2% | 95.71% | ₹26.28 L |
| Central | 955 | 8.7% | 95.29% | ₹11.80 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 96.88% | ₹1.27 L |
| Vasant Wardrobe | Key Account | Retail | 52 | 94.23% | ₹1.17 L |
| Rapid Bazaar | Key Account | Retail | 287 | 95.47% | ₹88,171 |
| Ujjwal Water Board | Key Account | Bills | 25 | 100.00% | ₹70,639 |
| Hampi Stores 2298 | Key Account | Retail | 112 | 93.75% | ₹65,584 |
| Urban Boutique | Key Account | Retail | 90 | 95.56% | ₹64,587 |
| Trinetra Restaurant | Large | Food & Beverage | 32 | 96.88% | ₹58,441 |
| Swift Mart 1738 | Key Account | Retail | 102 | 95.10% | ₹54,628 |

## Failure analysis

Of 507 declined attempts, 384 were business declines (3.515% of attempts — balances, PINs and limits), 57 technical (0.522%), 52 timeouts (0.476%) and 14 risk declines (0.128%).

163 attempts were re-presentations of an earlier failure (1.49% of the day); 69.9% of them succeeded.

- Decline code BT (Acquirer / NPCI switch timeout) fired 24 times — 0.220% of attempts against a trailing 0.107%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 158 | 1.446% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 128 | 1.172% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.394% | 0.378% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.229% | 0.188% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.220% | 0.220% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 24 | 0.220% | 0.107% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.220% | 0.192% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.146% | 0.083% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 81 | 80 |
| Auto-reversals | 29 | 28 |
| Disputes / chargebacks | 13 | 11 |
| Value returned | ₹2.89 L | ₹1.55 L |

## Customer behaviour

9,319 distinct customers transacted (−12.1% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,828 | 3,179 | 1.12 | 95.38% | ₹1,613 |
| power | 1,997 | 2,583 | 1.29 | 95.55% | ₹2,036 |
| merchant_heavy | 2,174 | 2,531 | 1.16 | 94.90% | ₹1,216 |
| small_ticket | 1,423 | 1,690 | 1.19 | 95.38% | ₹537 |
| occasional | 711 | 750 | 1.05 | 94.27% | ₹1,854 |
| new | 163 | 170 | 1.04 | 95.29% | ₹1,208 |
| dormant_returning | 23 | 23 | 1.00 | 100.00% | ₹980 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0062** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code BT (Acquirer / NPCI switch timeout) fired 24 times — 0.220% of attempts against a trailing 0.107%. Owner: NPCI.
- Success rate closed at 95.24%, 0.68pp down the trailing median — a 1.6-sigma move.
- Region South ran at 94.23% success on 3,226 attempts (29.5% of the day), 1.62pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 39% across the trailing window to 957 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer ICICI Bank ran at 94.25% success on 661 attempts (6.0% of the day), 2.11pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 47% across the trailing window to 300 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 22 April: success came in 0.68pp below baseline at 95.24% on 10,926 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,926, successes=10,406, failed=507, pending=13, settled_value_inr=15,989,986.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=BT; count=24; rate_pct=0.22; trailing_rate_pct=0.11; owner=NPCI; z=3.46
- headline: success_rate=95.24; trailing_median=95.92; z=-1.65
- products: product_name=UPI Circle; attempts=300; window_growth_pct=47.1; success_rate=96.33
- geography: region=South; attempts=3,226; success_rate=94.23; own_median=95.86; z=-2.29
- products: product_name=UPI Lite; attempts=957; window_growth_pct=39.4; success_rate=98.12
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- banks: payer_bank=ICICI Bank; attempts=661; success_rate=94.25; own_median=96.36; z=-2.2
- incidents: event_id=CMP-0054; kind=merchant_campaign; severity=Sev-3; window=2026-04-15 to 2026-04-22; success_impact_pp=-0.17; volume_impact_pct=66.38
- incidents: event_id=CMP-0062; kind=merchant_campaign; severity=Sev-3; window=2026-04-20 to 2026-04-22; success_impact_pp=-0.09; volume_impact_pct=36.4
- categories: mcc_category=Services; attempts=99; success_rate=91.92; own_median=96.13; z=-2.38

Refs: enterprise_data/warehouse/transactions, RPT-D107-DAILY, enterprise_data/warehouse/reference/incidents.parquet
