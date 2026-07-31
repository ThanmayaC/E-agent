---
id: RPT-D83-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 28 Mar 2026)

**Report ID:** RPT-D83-DAILY · **Day 83 of 206** · **Derived from:** 12,661 transaction rows queried live from the warehouse

## Summary

The rail took **12,661 payment attempts** on Saturday 28 March 2026 (Weekend) and settled **₹1.41 Cr** across 12,167 successful payments. Volume was +3.3% on yesterday and −18.3% on the same weekday last week. Success closed at **96.10%**, above the trailing 28-day median of 95.79%.

64 auto-reversals were raised, 6.0 sigma above the trailing median of 24.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,661 | +3.3% | −18.3% | 12,438 |
| Successful payments | 12,167 | +3.8% | −18.1% | 11,893 |
| Success rate | 96.10% | +0.42pp | +0.21pp | 95.55% |
| Settled value | ₹1.41 Cr | −5.7% | −11.7% | ₹1.41 Cr |
| Average ticket | ₹1,157 | −9.1% | +7.9% | ₹1,191 |
| Technical declines | 0.411% | +0.11pp | −0.10pp | 0.479% |
| Business declines | 3.009% | −0.52pp | −0.08pp | 3.303% |
| Risk declines | 0.079% | +0.01pp | −0.06pp | 0.122% |
| Timeout declines | 0.253% | −0.07pp | −0.05pp | 0.442% |
| Retry share | 0.97% | −1.93pp | −0.05pp | 1.43% |
| Latency p95 | 1,250 ms | −5.9% | +4.8% | 1,286 ms |
| Active customers | 10,535 | +2.8% | −15.5% | 10,306 |
| Active merchants | 1,344 | +0.6% | −2.3% | 1,320 |

## What moved

- Category Bills carried 1,089 attempts, 57% up its trailing median and 13.3% of the day's volume.
- App Google Pay ran at 96.42% success on 4,105 attempts (32.4% of the day), 0.74pp up its own 28-day median.
- Category Food & Beverage ran at 97.58% success on 1,944 attempts (23.7% of the day), 0.91pp up its own 28-day median.
- Product UPI International is compounding — attempts up 29% across the trailing window to 103 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,453 | 35.2% | 95.53% | ₹47.59 L | −0.2% |
| UPI Person to Merchant | 3,665 | 28.9% | 96.73% | ₹31.84 L | +5.5% |
| UPI QR Payments | 2,222 | 17.5% | 96.67% | ₹9.24 L | +2.8% |
| UPI Lite | 1,041 | 8.2% | 98.37% | ₹91,022 | +13.7% |
| UPI AutoPay | 320 | 2.5% | 89.38% | ₹5.27 L | +1.1% |
| UPI Circle | 295 | 2.3% | 97.97% | ₹2.78 L | +56.1% |
| RuPay Credit on UPI | 196 | 1.5% | 96.43% | ₹10.09 L | −13.1% |
| Credit on UPI | 136 | 1.1% | 94.12% | ₹14.72 L | −12.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,997 | 96.00% | 95.74% | ₹39.25 L | normal |
| HDFC Bank | 1,439 | 96.11% | 95.59% | ₹16.42 L | normal |
| Bank of Baroda | 945 | 95.87% | 95.64% | ₹11.08 L | normal |
| Union Bank of India | 877 | 97.04% | 95.53% | ₹12.01 L | normal |
| ICICI Bank | 790 | 96.71% | 95.86% | ₹8.03 L | normal |
| Punjab National Bank | 776 | 96.01% | 95.62% | ₹8.70 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,958 | 95.69% | 95.95% | ₹66.53 L | normal |
| Google Pay | 4,105 | 96.42% | 95.68% | ₹46.68 L | ⚠ outlier |
| Paytm | 1,048 | 96.66% | 95.68% | ₹12.01 L | normal |
| Navi | 500 | 96.80% | 95.68% | ₹4.66 L | normal |
| SuperMoney | 251 | 94.02% | 95.43% | ₹2.31 L | normal |
| BHIM | 141 | 97.87% | 95.53% | ₹1.29 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,320 | 96.30% | ₹29.53 L |
| Food & Beverage | 1,944 | 97.58% | ₹8.74 L |
| Bills | 1,089 | 95.68% | ₹11.65 L |
| Mobility | 861 | 97.79% | ₹5.05 L |
| Healthcare | 357 | 98.32% | ₹3.44 L |
| Digital | 284 | 95.07% | ₹1.50 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,733 | 29.5% | 96.33% | ₹44.37 L |
| North | 3,228 | 25.5% | 96.28% | ₹35.28 L |
| West | 3,090 | 24.4% | 96.21% | ₹32.56 L |
| East | 1,476 | 11.7% | 95.26% | ₹15.68 L |
| Central | 1,134 | 9.0% | 95.59% | ₹12.83 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 35 | 88.57% | ₹3.09 L |
| Rapid Bazaar | Key Account | Retail | 408 | 97.06% | ₹2.00 L |
| Vasant Wardrobe | Key Account | Retail | 60 | 95.00% | ₹1.49 L |
| Ujjwal Water Board | Key Account | Bills | 64 | 100.00% | ₹1.48 L |
| Girnar Connect | Key Account | Bills | 197 | 93.40% | ₹73,932 |
| Hampi Styles | Key Account | Retail | 27 | 92.59% | ₹69,268 |
| Aravalli Pharmacy | Large | Healthcare | 68 | 95.59% | ₹64,092 |
| Tejas Bites | Key Account | Food & Beverage | 142 | 98.59% | ₹62,342 |

## Failure analysis

Of 475 declined attempts, 381 were business declines (3.009% of attempts — balances, PINs and limits), 52 technical (0.411%), 32 timeouts (0.253%) and 10 risk declines (0.079%).

123 attempts were re-presentations of an earlier failure (0.97% of the day); 79.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 198 | 1.564% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 99 | 0.782% | 1.084% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.284% | 0.391% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.221% | 0.224% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.190% | 0.172% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 14 | 0.111% | 0.155% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.103% | 0.101% |
| U28 | Remitter bank unavailable | technical | Issuer | 12 | 0.095% | 0.118% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 67 | 78 |
| Auto-reversals | 64 | 24 |
| Disputes / chargebacks | 12 | 10 |
| Value returned | ₹1.62 L | ₹1.29 L |

## Customer behaviour

10,535 distinct customers transacted (+4.3% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,221 | 3,663 | 1.14 | 96.21% | ₹1,205 |
| power | 2,202 | 2,971 | 1.35 | 95.79% | ₹1,632 |
| merchant_heavy | 2,449 | 2,952 | 1.21 | 96.34% | ₹869 |
| small_ticket | 1,582 | 1,942 | 1.23 | 95.88% | ₹578 |
| occasional | 847 | 883 | 1.04 | 96.49% | ₹1,068 |
| new | 204 | 220 | 1.08 | 95.91% | ₹612 |
| dormant_returning | 30 | 30 | 1.00 | 93.33% | ₹1,559 |

## Operational events

- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 64 auto-reversals were raised, 6.0 sigma above the trailing median of 24.
- Product Recurring Payments ran at 80.65% success on 93 attempts (0.7% of the day), 7.84pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 29% across the trailing window to 103 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

28 March ran on trend at 96.10% success and ₹1.41 Cr settled. The movement worth carrying forward is in money moving back: 64 auto-reversals were raised, 6.0 sigma above the trailing median of 24. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,661, successes=12,167, failed=475, pending=19, settled_value_inr=14,071,559.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: reversals=64; trailing_median=24; z=6
- categories: mcc_category=Bills; attempts=1,089; own_median=694.5; z=4.43
- psps: payer_psp=Google Pay; attempts=4,105; success_rate=96.42; own_median=95.68; z=2.04
- categories: mcc_category=Food & Beverage; attempts=1,944; success_rate=97.58; own_median=96.67; z=2.02
- products: product_name=UPI International; attempts=103; window_growth_pct=29.3; success_rate=98.06
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- incidents: event_id=CMP-0057; kind=merchant_campaign; severity=Sev-3; window=2026-03-25 to 2026-04-01; success_impact_pp=-0.07; volume_impact_pct=28.96
- categories: mcc_category=Digital; attempts=284; own_median=203.5; z=2.31
- products: product_name=UPI Circle; attempts=295; own_median=189; z=2.8
- products: product_name=Recurring Payments; attempts=93; success_rate=80.65; own_median=88.48; z=-2.21

Refs: enterprise_data/warehouse/transactions, RPT-D82-DAILY, enterprise_data/warehouse/reference/incidents.parquet
