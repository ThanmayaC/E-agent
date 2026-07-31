---
id: RPT-D173-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 26 Jun 2026)

**Report ID:** RPT-D173-DAILY · **Day 173 of 206** · **Derived from:** 13,822 transaction rows queried live from the warehouse

## Summary

The rail took **13,822 payment attempts** on Friday 26 June 2026 (Muharram) and settled **₹1.45 Cr** across 13,246 successful payments. Volume was +5.5% on yesterday and −13.7% on the same weekday last week. Success closed at **95.83%**, below the trailing 28-day median of 96.28%.

Decline code Z9 (Insufficient funds) fired 223 times — 1.613% of attempts against a trailing 1.203%. Owner: Customer. Region South ran at 95.45% success on 4,024 attempts (29.1% of the day), 0.82pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,822 | +5.5% | −13.7% | 14,786 |
| Successful payments | 13,246 | +5.6% | −14.0% | 14,231 |
| Success rate | 95.83% | +0.14pp | −0.40pp | 96.22% |
| Settled value | ₹1.45 Cr | −14.3% | −29.9% | ₹1.92 Cr |
| Average ticket | ₹1,098 | −18.9% | −18.5% | ₹1,350 |
| Technical declines | 0.391% | −0.11pp | −0.15pp | 0.421% |
| Business declines | 3.299% | −0.04pp | +0.58pp | 2.877% |
| Risk declines | 0.174% | +0.04pp | +0.04pp | 0.125% |
| Timeout declines | 0.232% | +0.03pp | −0.04pp | 0.267% |
| Retry share | 1.24% | −0.29pp | +0.11pp | 1.09% |
| Latency p95 | 1,284 ms | −2.9% | −2.3% | 1,278 ms |
| Active customers | 11,550 | +5.0% | −11.8% | 12,163 |
| Active merchants | 1,507 | −0.9% | −2.3% | 1,542 |

## What moved

- Region South ran at 95.45% success on 4,024 attempts (29.1% of the day), 0.82pp down its own 28-day median.
- Success rate closed at 95.83%, 0.45pp down the trailing median — a 1.7-sigma move.
- Category Bills carried 1,312 attempts, 54% up its trailing median and 13.4% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,067 | 29.4% | 94.98% | ₹42.44 L | −2.6% |
| UPI Person to Merchant | 3,110 | 22.5% | 96.05% | ₹31.91 L | −12.6% |
| UPI Lite | 2,335 | 16.9% | 98.42% | ₹2.08 L | +11.8% |
| UPI QR Payments | 2,173 | 15.7% | 96.46% | ₹8.69 L | −7.1% |
| UPI Circle | 815 | 5.9% | 97.06% | ₹7.84 L | +15.0% |
| UPI AutoPay | 354 | 2.6% | 85.59% | ₹5.95 L | −0.1% |
| Credit on UPI | 268 | 1.9% | 95.15% | ₹16.39 L | −40.7% |
| RuPay Credit on UPI | 247 | 1.8% | 96.36% | ₹10.61 L | −34.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,321 | 96.16% | 96.28% | ₹44.24 L | normal |
| HDFC Bank | 1,457 | 95.81% | 96.46% | ₹14.98 L | normal |
| Bank of Baroda | 1,062 | 95.95% | 96.37% | ₹14.48 L | normal |
| Union Bank of India | 991 | 95.16% | 96.24% | ₹10.33 L | normal |
| Punjab National Bank | 887 | 94.81% | 96.27% | ₹9.67 L | ⚠ outlier |
| Axis Bank | 867 | 96.31% | 96.21% | ₹9.22 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,630 | 95.90% | 96.13% | ₹70.11 L | normal |
| Google Pay | 4,484 | 95.83% | 96.36% | ₹43.51 L | normal |
| Paytm | 1,170 | 95.30% | 96.28% | ₹13.32 L | normal |
| Navi | 494 | 95.34% | 96.61% | ₹6.77 L | normal |
| SuperMoney | 247 | 95.55% | 95.97% | ₹1.74 L | normal |
| BHIM | 144 | 95.83% | 95.86% | ₹1.31 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,592 | 96.52% | ₹36.81 L |
| Food & Beverage | 2,385 | 97.23% | ₹9.48 L |
| Bills | 1,312 | 95.35% | ₹12.87 L |
| Mobility | 1,257 | 96.82% | ₹6.08 L |
| Healthcare | 545 | 96.70% | ₹5.55 L |
| Digital | 264 | 90.53% | ₹1.37 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,024 | 29.1% | 95.45% | ₹44.61 L |
| North | 3,616 | 26.2% | 95.66% | ₹38.55 L |
| West | 3,392 | 24.5% | 95.96% | ₹33.24 L |
| East | 1,625 | 11.8% | 96.68% | ₹17.97 L |
| Central | 1,165 | 8.4% | 96.14% | ₹11.07 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 90.32% | ₹3.94 L |
| Rapid Bazaar | Key Account | Retail | 371 | 97.57% | ₹1.75 L |
| Vasant Wardrobe | Key Account | Retail | 49 | 95.92% | ₹1.25 L |
| Girnar Connect | Key Account | Bills | 238 | 95.38% | ₹1.06 L |
| Hampi Stores 2298 | Key Account | Retail | 100 | 96.00% | ₹1.01 L |
| Hampi Styles | Key Account | Retail | 30 | 100.00% | ₹70,414 |
| Ujjwal Water Board | Key Account | Bills | 43 | 95.35% | ₹61,265 |
| Yamuna Restaurant | Key Account | Food & Beverage | 70 | 97.14% | ₹55,847 |

## Failure analysis

Of 566 declined attempts, 456 were business declines (3.299% of attempts — balances, PINs and limits), 54 technical (0.391%), 32 timeouts (0.232%) and 24 risk declines (0.174%).

172 attempts were re-presentations of an earlier failure (1.24% of the day); 66.3% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 223 times — 1.613% of attempts against a trailing 1.203%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 223 | 1.613% | 1.203% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 0.998% | 0.943% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.355% | 0.337% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.188% | 0.173% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.166% | 0.200% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 22 | 0.159% | 0.109% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.130% | 0.086% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 13 | 0.094% | 0.141% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 104 | 106 |
| Auto-reversals | 22 | 24 |
| Disputes / chargebacks | 15 | 13 |
| Value returned | ₹2.48 L | ₹1.70 L |

## Customer behaviour

11,550 distinct customers transacted (−4.5% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,519 | 3,971 | 1.13 | 95.57% | ₹1,146 |
| power | 2,636 | 3,543 | 1.34 | 95.60% | ₹1,384 |
| merchant_heavy | 2,667 | 3,161 | 1.19 | 95.95% | ₹805 |
| small_ticket | 1,674 | 2,037 | 1.22 | 96.66% | ₹524 |
| occasional | 816 | 855 | 1.05 | 95.32% | ₹1,331 |
| new | 211 | 228 | 1.08 | 97.37% | ₹1,269 |
| dormant_returning | 27 | 27 | 1.00 | 92.59% | ₹1,797 |

## Operational events

- **INC-BANK-0010** (Sev-2) — Kotak Mahindra Bank issuer decline spike, scoped to Kotak Mahindra Bank between 10:00 and 15:00. Kotak Mahindra Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 223 times — 1.613% of attempts against a trailing 1.203%. Owner: Customer.
- Region South ran at 95.45% success on 4,024 attempts (29.1% of the day), 0.82pp down its own 28-day median.
- Success rate closed at 95.83%, 0.45pp down the trailing median — a 1.7-sigma move.
- Issuer Punjab National Bank ran at 94.81% success on 887 attempts (6.4% of the day), 1.46pp down its own 28-day median.
- Product UPI Lite Auto Top-Up ran at 89.17% success on 120 attempts (0.9% of the day), 8.47pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

26 June was an incident day: INC-BANK-0010 was live and the rail closed at 95.83% success against a 96.28% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,822, successes=13,246, failed=566, pending=10, settled_value_inr=14,543,684.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=223; rate_pct=1.61; trailing_rate_pct=1.2; owner=Customer; z=4.59
- geography: region=South; attempts=4,024; success_rate=95.45; own_median=96.27; z=-3.85
- incidents: event_id=INC-BANK-0010; kind=bank_outage; severity=Sev-2; window=2026-06-25 to 2026-06-27; success_impact_pp=-19.68; volume_impact_pct=-17.46
- headline: success_rate=95.83; trailing_median=96.28; z=-1.68
- categories: mcc_category=Bills; attempts=1,312; own_median=852; z=4.37
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- banks: payer_bank=Punjab National Bank; attempts=887; success_rate=94.81; own_median=96.27; z=-2.39
- products: product_name=UPI Lite Auto Top-Up; attempts=120; success_rate=89.17; own_median=97.63; z=-6.39
- categories: mcc_category=Digital; attempts=264; success_rate=90.53; own_median=94.64; z=-3.49
- products: product_name=UPI AutoPay; attempts=354; success_rate=85.59; own_median=91.03; z=-2.86

Refs: enterprise_data/warehouse/transactions, RPT-D172-DAILY, enterprise_data/warehouse/reference/incidents.parquet
