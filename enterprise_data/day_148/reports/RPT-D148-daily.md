---
id: RPT-D148-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-01T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 01 Jun 2026)

**Report ID:** RPT-D148-DAILY · **Day 148 of 206** · **Derived from:** 16,139 transaction rows queried live from the warehouse

## Summary

The rail took **16,139 payment attempts** on Monday 01 June 2026 (Working day) and settled **₹2.24 Cr** across 15,603 successful payments. Volume was +7.5% on yesterday and +8.4% on the same weekday last week. Success closed at **96.68%**, above the trailing 28-day median of 96.08%.

Success rate closed at 96.68%, 0.60pp up the trailing median — a 1.9-sigma move. Category Bills carried 1,723 attempts, 89% up its trailing median and 14.5% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,139 | +7.5% | +8.4% | 16,139 |
| Successful payments | 15,603 | +7.8% | +9.0% | 15,603 |
| Success rate | 96.68% | +0.29pp | +0.54pp | 96.68% |
| Settled value | ₹2.24 Cr | +18.6% | +15.6% | ₹2.24 Cr |
| Average ticket | ₹1,435 | +10.0% | +6.1% | ₹1,435 |
| Technical declines | 0.341% | +0.01pp | −0.11pp | 0.341% |
| Business declines | 2.559% | −0.26pp | −0.36pp | 2.559% |
| Risk declines | 0.130% | −0.02pp | +0.01pp | 0.130% |
| Timeout declines | 0.186% | −0.03pp | −0.09pp | 0.186% |
| Retry share | 0.84% | −0.06pp | −0.38pp | 0.84% |
| Latency p95 | 1,264 ms | +4.0% | −0.5% | 1,264 ms |
| Active customers | 13,138 | +6.9% | +7.3% | 13,138 |
| Active merchants | 1,611 | +5.8% | +6.3% | 1,611 |

## What moved

- Success rate closed at 96.68%, 0.60pp up the trailing median — a 1.9-sigma move.
- Category Bills carried 1,723 attempts, 89% up its trailing median and 14.5% of the day's volume.
- App PhonePe ran at 96.62% success on 7,634 attempts (47.3% of the day), 0.50pp up its own 28-day median.
- Region South ran at 96.75% success on 4,794 attempts (29.7% of the day), 0.64pp up its own 28-day median.
- App Google Pay ran at 96.86% success on 5,281 attempts (32.7% of the day), 0.88pp up its own 28-day median.
- Product UPI Circle is compounding — attempts up 32% across the trailing window to 777 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 4,524 | 28.0% | 96.64% | ₹51.34 L | +15.8% |
| UPI Person to Person | 4,245 | 26.3% | 95.71% | ₹47.70 L | −3.8% |
| UPI QR Payments | 2,773 | 17.2% | 96.93% | ₹11.27 L | +15.2% |
| UPI Lite | 2,058 | 12.8% | 99.08% | ₹2.01 L | +18.6% |
| UPI Circle | 777 | 4.8% | 97.94% | ₹7.86 L | +30.9% |
| Credit on UPI | 465 | 2.9% | 96.34% | ₹42.16 L | +30.8% |
| RuPay Credit on UPI | 454 | 2.8% | 95.59% | ₹17.53 L | +23.0% |
| UPI AutoPay | 334 | 2.1% | 92.22% | ₹6.21 L | −0.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,141 | 96.56% | 96.04% | ₹66.73 L | normal |
| HDFC Bank | 1,702 | 96.53% | 96.21% | ₹22.12 L | normal |
| Bank of Baroda | 1,184 | 96.79% | 96.01% | ₹17.37 L | normal |
| Union Bank of India | 1,101 | 97.64% | 95.72% | ₹17.48 L | normal |
| Punjab National Bank | 1,043 | 97.12% | 95.73% | ₹15.82 L | normal |
| ICICI Bank | 1,002 | 97.31% | 96.46% | ₹19.11 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,634 | 96.62% | 96.12% | ₹1.03 Cr | ⚠ outlier |
| Google Pay | 5,281 | 96.86% | 95.98% | ₹78.11 L | ⚠ outlier |
| Paytm | 1,339 | 97.24% | 96.14% | ₹19.15 L | normal |
| Navi | 577 | 96.71% | 95.45% | ₹6.66 L | normal |
| SuperMoney | 313 | 94.25% | 96.33% | ₹4.16 L | normal |
| BHIM | 174 | 94.83% | 95.96% | ₹2.85 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,547 | 97.10% | ₹60.40 L |
| Food & Beverage | 2,746 | 97.78% | ₹14.08 L |
| Bills | 1,723 | 96.52% | ₹19.40 L |
| Mobility | 1,428 | 96.64% | ₹7.75 L |
| Healthcare | 608 | 98.36% | ₹8.82 L |
| Digital | 383 | 95.56% | ₹2.58 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,794 | 29.7% | 96.75% | ₹63.14 L |
| West | 4,019 | 24.9% | 96.44% | ₹60.04 L |
| North | 3,978 | 24.6% | 96.78% | ₹49.22 L |
| East | 1,992 | 12.3% | 96.44% | ₹31.83 L |
| Central | 1,356 | 8.4% | 97.20% | ₹19.60 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 95 | 95.79% | ₹2.22 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 96.72% | ₹2.01 L |
| Vega Electronics | Large | Retail | 31 | 90.32% | ₹1.93 L |
| Rapid Bazaar | Key Account | Retail | 419 | 97.85% | ₹1.78 L |
| Hampi Styles | Key Account | Retail | 42 | 97.62% | ₹1.42 L |
| Girnar Connect | Key Account | Bills | 275 | 96.73% | ₹1.33 L |
| Hampi Stores 2298 | Key Account | Retail | 119 | 96.64% | ₹1.21 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 98.63% | ₹1.01 L |

## Failure analysis

Of 519 declined attempts, 413 were business declines (2.559% of attempts — balances, PINs and limits), 55 technical (0.341%), 30 timeouts (0.186%) and 21 risk declines (0.130%).

136 attempts were re-presentations of an earlier failure (0.84% of the day); 66.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 160 | 0.991% | 1.207% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 0.843% | 0.980% |
| ZA | Transaction declined by customer | business | Customer | 63 | 0.390% | 0.346% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.186% | 0.217% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.143% | 0.207% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.118% | 0.148% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.105% | 0.106% |
| U69 | Beneficiary bank offline | technical | Issuer | 16 | 0.099% | 0.079% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 94 | 104 |
| Auto-reversals | 16 | 27 |
| Disputes / chargebacks | 14 | 13 |
| Value returned | ₹1.71 L | ₹2.09 L |

## Customer behaviour

13,138 distinct customers transacted (+9.3% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,094 | 4,721 | 1.15 | 96.67% | ₹1,553 |
| power | 2,761 | 3,841 | 1.39 | 96.51% | ₹2,056 |
| merchant_heavy | 2,994 | 3,690 | 1.23 | 96.88% | ₹1,040 |
| small_ticket | 1,960 | 2,471 | 1.26 | 96.28% | ₹625 |
| occasional | 1,066 | 1,134 | 1.06 | 97.00% | ₹1,402 |
| new | 222 | 240 | 1.08 | 98.33% | ₹614 |
| dormant_returning | 41 | 42 | 1.02 | 100.00% | ₹774 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 32% across the trailing window to 777 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 01 June: success came in 0.60pp above baseline at 96.68% on 16,139 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-01` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,139, successes=15,603, failed=519, pending=17, settled_value_inr=22,383,158.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: success_rate=96.68; trailing_median=96.08; z=1.85
- categories: mcc_category=Bills; attempts=1,723; own_median=913; z=5.3
- psps: payer_psp=PhonePe; attempts=7,634; success_rate=96.62; own_median=96.12; z=2.01
- geography: region=South; attempts=4,794; success_rate=96.75; own_median=96.11; z=2.36
- psps: payer_psp=Google Pay; attempts=5,281; success_rate=96.86; own_median=95.98; z=2.03
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Circle; attempts=777; window_growth_pct=32.4; success_rate=97.94
- categories: mcc_category=Mobility; attempts=1,428; own_median=1,185; z=2.21
- banks: payer_bank=Canara Bank; attempts=919; success_rate=97.06; own_median=95.72; z=2.27
- categories: mcc_category=Digital; attempts=383; own_median=222; z=4.1

Refs: enterprise_data/warehouse/transactions, RPT-D147-DAILY, enterprise_data/warehouse/reference/incidents.parquet
