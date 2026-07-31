---
id: RPT-D179-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-02T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 02 Jul 2026)

**Report ID:** RPT-D179-DAILY · **Day 179 of 206** · **Derived from:** 18,152 transaction rows queried live from the warehouse

## Summary

The rail took **18,152 payment attempts** on Thursday 02 July 2026 (Working day) and settled **₹2.41 Cr** across 17,567 successful payments. Volume was −2.3% on yesterday and +38.5% on the same weekday last week. Success closed at **96.78%**, above the trailing 28-day median of 96.21%.

Category Bills carried 2,042 attempts, 140% up its trailing median and 15.4% of the day's volume. Success rate closed at 96.78%, 0.57pp up the trailing median — a 2.0-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 18,152 | −2.3% | +38.5% | 18,362 |
| Successful payments | 17,567 | −1.8% | +40.1% | 17,730 |
| Success rate | 96.78% | +0.43pp | +1.08pp | 96.56% |
| Settled value | ₹2.41 Cr | −4.5% | +41.9% | ₹2.46 Cr |
| Average ticket | ₹1,371 | −2.7% | +1.3% | ₹1,390 |
| Technical declines | 0.314% | −0.06pp | −0.19pp | 0.345% |
| Business declines | 2.446% | −0.44pp | −0.89pp | 2.666% |
| Risk declines | 0.105% | +0.03pp | −0.03pp | 0.087% |
| Timeout declines | 0.275% | +0.03pp | +0.07pp | 0.259% |
| Retry share | 0.96% | −0.36pp | −0.57pp | 1.14% |
| Latency p95 | 1,210 ms | −2.9% | −8.4% | 1,228 ms |
| Active customers | 14,502 | −1.5% | +31.9% | 14,612 |
| Active merchants | 1,678 | +1.2% | +10.4% | 1,668 |

## What moved

- Category Bills carried 2,042 attempts, 140% up its trailing median and 15.4% of the day's volume.
- Success rate closed at 96.78%, 0.57pp up the trailing median — a 2.0-sigma move.
- Region South ran at 97.06% success on 5,374 attempts (29.6% of the day), 0.82pp up its own 28-day median.
- Attempt volume ran 2.7 standard deviations up its trailing 28-day median at 18,152, 38.5% up on the same weekday last week.
- App PhonePe carried 8,506 attempts, 24% up its trailing median and 46.9% of the day's volume.
- App Google Pay ran at 96.96% success on 6,077 attempts (33.5% of the day), 0.62pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,870 | 26.8% | 95.44% | ₹53.15 L | +16.6% |
| UPI Person to Merchant | 4,369 | 24.1% | 96.54% | ₹45.18 L | +26.0% |
| UPI Lite | 3,303 | 18.2% | 99.18% | ₹3.18 L | +50.8% |
| UPI QR Payments | 2,976 | 16.4% | 97.08% | ₹13.18 L | +24.5% |
| UPI Circle | 800 | 4.4% | 98.38% | ₹8.03 L | +11.4% |
| Credit on UPI | 514 | 2.8% | 97.28% | ₹48.20 L | +12.8% |
| RuPay Credit on UPI | 402 | 2.2% | 97.01% | ₹26.45 L | +9.2% |
| UPI AutoPay | 371 | 2.0% | 90.84% | ₹7.29 L | −0.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,724 | 96.89% | 96.18% | ₹64.48 L | ⚠ outlier |
| HDFC Bank | 1,995 | 97.04% | 96.39% | ₹23.06 L | normal |
| Bank of Baroda | 1,355 | 96.90% | 96.22% | ₹19.04 L | normal |
| Union Bank of India | 1,281 | 96.33% | 96.00% | ₹20.08 L | normal |
| Axis Bank | 1,123 | 97.60% | 96.15% | ₹19.74 L | normal |
| Punjab National Bank | 1,065 | 95.21% | 96.05% | ₹17.31 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,506 | 96.60% | 96.11% | ₹1.11 Cr | normal |
| Google Pay | 6,077 | 96.96% | 96.33% | ₹79.53 L | ⚠ outlier |
| Paytm | 1,517 | 97.30% | 96.12% | ₹22.99 L | normal |
| Navi | 632 | 96.99% | 96.47% | ₹9.30 L | normal |
| SuperMoney | 365 | 96.99% | 95.97% | ₹5.80 L | normal |
| BHIM | 187 | 94.65% | 95.91% | ₹1.66 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,993 | 97.36% | ₹53.32 L |
| Food & Beverage | 3,105 | 97.52% | ₹14.52 L |
| Bills | 2,042 | 97.26% | ₹20.96 L |
| Mobility | 1,637 | 97.98% | ₹8.85 L |
| Healthcare | 663 | 98.49% | ₹8.04 L |
| Digital | 332 | 93.98% | ₹1.91 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,374 | 29.6% | 97.06% | ₹71.34 L |
| North | 4,577 | 25.2% | 96.66% | ₹62.04 L |
| West | 4,468 | 24.6% | 96.33% | ₹61.01 L |
| East | 2,158 | 11.9% | 96.99% | ₹29.78 L |
| Central | 1,575 | 8.7% | 97.14% | ₹16.59 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 505 | 97.62% | ₹2.73 L |
| Vasant Wardrobe | Key Account | Retail | 97 | 96.91% | ₹2.72 L |
| Vega Electronics | Large | Retail | 41 | 97.56% | ₹2.47 L |
| Girnar Connect | Key Account | Bills | 338 | 97.34% | ₹1.42 L |
| Ujjwal Water Board | Key Account | Bills | 70 | 94.29% | ₹1.31 L |
| Hampi Stores 2298 | Key Account | Retail | 119 | 97.48% | ₹1.14 L |
| Hampi Styles | Key Account | Retail | 42 | 95.24% | ₹1.13 L |
| Urban Boutique | Key Account | Retail | 141 | 97.16% | ₹1.12 L |

## Failure analysis

Of 570 declined attempts, 444 were business declines (2.446% of attempts — balances, PINs and limits), 57 technical (0.314%), 50 timeouts (0.275%) and 19 risk declines (0.105%).

175 attempts were re-presentations of an earlier failure (0.96% of the day); 68.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 177 | 0.975% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 157 | 0.865% | 0.954% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.281% | 0.328% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.165% | 0.194% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.132% | 0.135% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 23 | 0.127% | 0.092% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.105% | 0.177% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.094% | 0.102% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 95 | 110 |
| Auto-reversals | 28 | 24 |
| Disputes / chargebacks | 16 | 14 |
| Value returned | ₹3.68 L | ₹1.70 L |

## Customer behaviour

14,502 distinct customers transacted (+21.5% on the 28-day median) at 1.25 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,540 | 5,378 | 1.18 | 96.86% | ₹1,389 |
| power | 3,032 | 4,330 | 1.43 | 97.02% | ₹1,953 |
| merchant_heavy | 3,376 | 4,209 | 1.25 | 96.44% | ₹1,033 |
| small_ticket | 2,145 | 2,735 | 1.28 | 96.67% | ₹681 |
| occasional | 1,150 | 1,216 | 1.06 | 96.79% | ₹1,228 |
| new | 227 | 252 | 1.11 | 97.62% | ₹1,642 |
| dormant_returning | 32 | 32 | 1.00 | 96.88% | ₹1,002 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Lite is compounding — attempts up 26% across the trailing window to 3,303 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 02 July: success came in 0.57pp above baseline at 96.78% on 18,152 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-02` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=18,152, successes=17,567, failed=570, pending=15, settled_value_inr=24,076,042.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=2,042; own_median=852; z=11.3
- headline: success_rate=96.78; trailing_median=96.21; z=2.02
- geography: region=South; attempts=5,374; success_rate=97.06; own_median=96.24; z=2.7
- headline: attempts=18,152; trailing_median=14,446; z=2.71
- psps: payer_psp=PhonePe; attempts=8,506; own_median=6,835; z=2.43
- psps: payer_psp=Google Pay; attempts=6,077; success_rate=96.96; own_median=96.33; z=2.06
- banks: payer_bank=State Bank of India; attempts=5,724; success_rate=96.89; own_median=96.17; z=2.01
- products: product_name=UPI Lite; attempts=3,303; own_median=2,191; z=3.54
- psps: payer_psp=Google Pay; attempts=6,077; own_median=4,781.5; z=2.56
- geography: region=North; attempts=4,577; own_median=3,624; z=2.84

Refs: enterprise_data/warehouse/transactions, RPT-D178-DAILY, enterprise_data/warehouse/reference/incidents.parquet
