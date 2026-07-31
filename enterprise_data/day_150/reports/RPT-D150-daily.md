---
id: RPT-D150-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-03T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 03 Jun 2026)

**Report ID:** RPT-D150-DAILY · **Day 150 of 206** · **Derived from:** 15,065 transaction rows queried live from the warehouse

## Summary

The rail took **15,065 payment attempts** on Wednesday 03 June 2026 (Working day) and settled **₹2.10 Cr** across 14,509 successful payments. Volume was −3.6% on yesterday and −2.0% on the same weekday last week. Success closed at **96.31%**, in line with the trailing 28-day median of 96.11%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,065 | −3.6% | −2.0% | 15,608 |
| Successful payments | 14,509 | −3.8% | −1.8% | 15,065 |
| Success rate | 96.31% | −0.25pp | +0.23pp | 96.52% |
| Settled value | ₹2.10 Cr | −4.3% | +7.0% | ₹2.18 Cr |
| Average ticket | ₹1,445 | −0.6% | +8.9% | ₹1,444 |
| Technical declines | 0.299% | −0.03pp | −0.22pp | 0.322% |
| Business declines | 2.868% | +0.25pp | −0.05pp | 2.682% |
| Risk declines | 0.166% | +0.03pp | +0.06pp | 0.146% |
| Timeout declines | 0.259% | +0.00pp | −0.07pp | 0.234% |
| Retry share | 0.88% | −0.14pp | −0.42pp | 0.92% |
| Latency p95 | 1,293 ms | +1.4% | +2.4% | 1,277 ms |
| Active customers | 12,394 | −2.3% | −1.1% | 12,739 |
| Active merchants | 1,546 | −0.7% | +0.4% | 1,571 |

## What moved

- Category Bills carried 1,553 attempts, 70% up its trailing median and 14.8% of the day's volume.
- Product UPI Circle is compounding — attempts up 36% across the trailing window to 757 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,560 | 30.3% | 95.46% | ₹47.70 L | +4.5% |
| UPI Person to Merchant | 3,842 | 25.5% | 96.38% | ₹43.75 L | −1.9% |
| UPI QR Payments | 2,285 | 15.2% | 97.07% | ₹9.44 L | −5.0% |
| UPI Lite | 1,959 | 13.0% | 99.03% | ₹1.80 L | +11.0% |
| UPI Circle | 757 | 5.0% | 97.36% | ₹7.95 L | +25.4% |
| RuPay Credit on UPI | 465 | 3.1% | 94.19% | ₹24.78 L | +26.0% |
| Credit on UPI | 422 | 2.8% | 94.79% | ₹44.73 L | +17.9% |
| UPI AutoPay | 318 | 2.1% | 91.19% | ₹6.13 L | −6.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,767 | 96.52% | 96.05% | ₹69.41 L | normal |
| HDFC Bank | 1,613 | 96.47% | 96.25% | ₹19.15 L | normal |
| Bank of Baroda | 1,130 | 96.90% | 96.21% | ₹12.34 L | normal |
| Union Bank of India | 1,053 | 96.49% | 95.79% | ₹16.83 L | normal |
| Axis Bank | 986 | 96.25% | 96.52% | ₹13.58 L | normal |
| Punjab National Bank | 910 | 96.48% | 95.89% | ₹15.11 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,142 | 96.42% | 96.13% | ₹98.97 L | normal |
| Google Pay | 4,945 | 96.68% | 95.99% | ₹67.15 L | normal |
| Paytm | 1,258 | 94.91% | 96.15% | ₹16.79 L | normal |
| Navi | 524 | 96.18% | 95.71% | ₹7.40 L | normal |
| SuperMoney | 316 | 94.94% | 96.33% | ₹3.08 L | normal |
| BHIM | 140 | 93.57% | 95.96% | ₹1.79 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,130 | 96.54% | ₹57.44 L |
| Food & Beverage | 2,364 | 97.38% | ₹10.42 L |
| Bills | 1,553 | 96.20% | ₹19.81 L |
| Mobility | 1,174 | 98.21% | ₹6.67 L |
| Healthcare | 507 | 98.03% | ₹9.57 L |
| Digital | 310 | 94.52% | ₹2.01 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,471 | 29.7% | 96.11% | ₹62.79 L |
| North | 3,786 | 25.1% | 96.86% | ₹52.03 L |
| West | 3,755 | 24.9% | 95.95% | ₹53.82 L |
| East | 1,763 | 11.7% | 95.92% | ₹26.62 L |
| Central | 1,290 | 8.6% | 96.98% | ₹14.40 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 27 | 85.19% | ₹2.05 L |
| Hampi Styles | Key Account | Retail | 39 | 97.44% | ₹1.89 L |
| Ujjwal Water Board | Key Account | Bills | 82 | 97.56% | ₹1.75 L |
| Rapid Bazaar | Key Account | Retail | 405 | 95.80% | ₹1.64 L |
| Vasant Wardrobe | Key Account | Retail | 58 | 93.10% | ₹1.51 L |
| Hampi Stores 2298 | Key Account | Retail | 138 | 96.38% | ₹99,125 |
| Girnar Connect | Key Account | Bills | 250 | 97.20% | ₹97,324 |
| Aravalli Pharmacy | Large | Healthcare | 87 | 97.70% | ₹66,309 |

## Failure analysis

Of 541 declined attempts, 432 were business declines (2.868% of attempts — balances, PINs and limits), 45 technical (0.299%), 39 timeouts (0.259%) and 25 risk declines (0.166%).

133 attempts were re-presentations of an earlier failure (0.88% of the day); 63.9% of them succeeded.

- Decline code U16 (Risk threshold exceeded at remitter) fired 24 times — 0.159% of attempts against a trailing 0.106%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 187 | 1.241% | 1.161% |
| ZM | Invalid UPI PIN | business | Customer | 152 | 1.009% | 0.949% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.305% | 0.346% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 24 | 0.159% | 0.106% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.153% | 0.214% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.146% | 0.148% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.119% | 0.199% |
| ZX | Mandate not found or revoked | business | PSP | 17 | 0.113% | 0.074% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 104 | 104 |
| Auto-reversals | 16 | 26 |
| Disputes / chargebacks | 12 | 13 |
| Value returned | ₹1.36 L | ₹1.98 L |

## Customer behaviour

12,394 distinct customers transacted (+3.1% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,862 | 4,460 | 1.15 | 95.99% | ₹1,521 |
| power | 2,590 | 3,545 | 1.37 | 96.61% | ₹1,918 |
| merchant_heavy | 2,900 | 3,475 | 1.20 | 96.12% | ₹994 |
| small_ticket | 1,846 | 2,324 | 1.26 | 96.73% | ₹776 |
| occasional | 945 | 996 | 1.05 | 96.39% | ₹1,842 |
| new | 214 | 228 | 1.07 | 96.93% | ₹1,071 |
| dormant_returning | 37 | 37 | 1.00 | 91.89% | ₹1,254 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code U16 (Risk threshold exceeded at remitter) fired 24 times — 0.159% of attempts against a trailing 0.106%. Owner: Issuer.

### Opportunities

- Product UPI Circle is compounding — attempts up 36% across the trailing window to 757 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

03 June ran on trend at 96.31% success and ₹2.10 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 1,553 attempts, 70% up its trailing median and 14.8% of the day's volume. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-03` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,065, successes=14,509, failed=541, pending=15, settled_value_inr=20,965,391.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,553; own_median=913; z=4.19
- products: product_name=UPI Circle; attempts=757; window_growth_pct=35.5; success_rate=97.36
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- failures: failure_code=U16; count=24; rate_pct=0.16; trailing_rate_pct=0.11; owner=Issuer; z=2.46
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- categories: mcc_category=Digital; attempts=310; own_median=222; z=2.24

Refs: enterprise_data/warehouse/transactions, RPT-D149-DAILY, enterprise_data/warehouse/reference/incidents.parquet
