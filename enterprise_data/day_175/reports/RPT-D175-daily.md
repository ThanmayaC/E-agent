---
id: RPT-D175-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 28 Jun 2026)

**Report ID:** RPT-D175-DAILY · **Day 175 of 206** · **Derived from:** 14,050 transaction rows queried live from the warehouse

## Summary

The rail took **14,050 payment attempts** on Sunday 28 June 2026 (Quarter Close Q1FY27 (build-up)) and settled **₹1.58 Cr** across 13,501 successful payments. Volume was −12.9% on yesterday and −0.1% on the same weekday last week. Success closed at **96.09%**, in line with the trailing 28-day median of 96.25%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,050 | −12.9% | −0.1% | 14,808 |
| Successful payments | 13,501 | −13.1% | +0.2% | 14,251 |
| Success rate | 96.09% | −0.16pp | +0.33pp | 96.22% |
| Settled value | ₹1.58 Cr | −20.0% | +9.6% | ₹1.91 Cr |
| Average ticket | ₹1,167 | −7.9% | +9.4% | ₹1,340 |
| Technical declines | 0.391% | −0.07pp | −0.06pp | 0.421% |
| Business declines | 3.060% | +0.23pp | −0.17pp | 2.882% |
| Risk declines | 0.135% | +0.02pp | +0.00pp | 0.125% |
| Timeout declines | 0.228% | −0.01pp | −0.11pp | 0.265% |
| Retry share | 1.18% | +0.07pp | −0.11pp | 1.10% |
| Latency p95 | 1,235 ms | −3.3% | +1.7% | 1,277 ms |
| Active customers | 11,658 | −11.2% | −0.5% | 12,180 |
| Active merchants | 1,529 | −4.3% | +1.7% | 1,543 |

## What moved

- Category Bills carried 1,181 attempts, 39% up its trailing median and 11.9% of the day's volume.
- Product UPI Lite carried 2,607 attempts, 23% up its trailing median and 18.6% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,105 | 29.2% | 95.08% | ₹40.88 L | −1.7% |
| UPI Person to Merchant | 2,958 | 21.1% | 96.38% | ₹28.44 L | −16.8% |
| UPI Lite | 2,607 | 18.6% | 98.58% | ₹2.29 L | +23.5% |
| UPI QR Payments | 2,247 | 16.0% | 96.80% | ₹8.87 L | −3.9% |
| UPI Circle | 796 | 5.7% | 97.24% | ₹6.31 L | +10.9% |
| UPI AutoPay | 387 | 2.8% | 87.34% | ₹6.93 L | +7.8% |
| Credit on UPI | 308 | 2.2% | 93.83% | ₹23.31 L | −31.9% |
| RuPay Credit on UPI | 212 | 1.5% | 95.28% | ₹7.98 L | −42.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,307 | 96.40% | 96.28% | ₹52.70 L | normal |
| HDFC Bank | 1,532 | 95.76% | 96.46% | ₹16.50 L | normal |
| Bank of Baroda | 1,088 | 96.42% | 96.22% | ₹9.95 L | normal |
| Union Bank of India | 965 | 94.72% | 96.21% | ₹11.01 L | ⚠ outlier |
| Axis Bank | 897 | 95.54% | 96.23% | ₹9.31 L | normal |
| Punjab National Bank | 887 | 95.49% | 96.23% | ₹8.63 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,611 | 96.23% | 96.11% | ₹76.42 L | normal |
| Google Pay | 4,740 | 95.70% | 96.36% | ₹56.24 L | normal |
| Paytm | 1,127 | 96.27% | 96.12% | ₹10.83 L | normal |
| Navi | 498 | 95.98% | 96.61% | ₹3.99 L | normal |
| SuperMoney | 267 | 97.38% | 95.97% | ₹3.28 L | normal |
| BHIM | 136 | 99.26% | 95.85% | ₹86,936 | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,859 | 97.10% | ₹40.49 L |
| Food & Beverage | 2,501 | 97.12% | ₹9.20 L |
| Mobility | 1,258 | 97.54% | ₹4.79 L |
| Bills | 1,181 | 95.43% | ₹11.54 L |
| Healthcare | 473 | 97.04% | ₹6.88 L |
| Digital | 241 | 92.95% | ₹96,752 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,086 | 29.1% | 95.86% | ₹49.08 L |
| North | 3,594 | 25.6% | 96.10% | ₹32.98 L |
| West | 3,485 | 24.8% | 96.10% | ₹44.48 L |
| East | 1,688 | 12.0% | 96.03% | ₹17.32 L |
| Central | 1,197 | 8.5% | 96.91% | ₹13.72 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Hampi Styles | Key Account | Retail | 24 | 100.00% | ₹1.67 L |
| Rapid Bazaar | Key Account | Retail | 356 | 98.88% | ₹1.62 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 97.30% | ₹1.40 L |
| Urban Boutique | Key Account | Retail | 139 | 97.84% | ₹1.10 L |
| Vega Electronics | Large | Retail | 17 | 94.12% | ₹1.03 L |
| Girnar Connect | Key Account | Bills | 213 | 96.24% | ₹97,781 |
| Ujjwal Water Board | Key Account | Bills | 40 | 97.50% | ₹67,345 |
| Hampi Stores 2298 | Key Account | Retail | 93 | 93.55% | ₹66,624 |

## Failure analysis

Of 536 declined attempts, 430 were business declines (3.060% of attempts — balances, PINs and limits), 55 technical (0.391%), 32 timeouts (0.228%) and 19 risk declines (0.135%).

166 attempts were re-presentations of an earlier failure (1.18% of the day); 65.7% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 64 times — 0.456% of attempts against a trailing 0.334%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 196 | 1.395% | 1.217% |
| ZM | Invalid UPI PIN | business | Customer | 125 | 0.890% | 0.943% |
| ZA | Transaction declined by customer | business | Customer | 64 | 0.456% | 0.334% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.185% | 0.204% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.171% | 0.176% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.121% | 0.112% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 16 | 0.114% | 0.139% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.107% | 0.112% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 113 | 107 |
| Auto-reversals | 26 | 22 |
| Disputes / chargebacks | 16 | 14 |
| Value returned | ₹2.94 L | ₹1.70 L |

## Customer behaviour

11,658 distinct customers transacted (−3.6% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,550 | 4,064 | 1.14 | 95.84% | ₹1,243 |
| power | 2,571 | 3,453 | 1.34 | 96.38% | ₹1,473 |
| merchant_heavy | 2,691 | 3,250 | 1.21 | 96.37% | ₹983 |
| small_ticket | 1,744 | 2,125 | 1.22 | 95.95% | ₹539 |
| occasional | 859 | 897 | 1.04 | 95.65% | ₹1,244 |
| new | 219 | 237 | 1.08 | 94.94% | ₹640 |
| dormant_returning | 24 | 24 | 1.00 | 100.00% | ₹442 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 64 times — 0.456% of attempts against a trailing 0.334%. Owner: Customer.
- Issuer Union Bank of India ran at 94.72% success on 965 attempts (6.9% of the day), 1.49pp down its own 28-day median.
- Issuer Indian Bank ran at 94.00% success on 450 attempts (3.2% of the day), 2.21pp down its own 28-day median.
- Product Credit on UPI ran at 93.83% success on 308 attempts (2.2% of the day), 2.11pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

28 June ran on trend at 96.09% success and ₹1.58 Cr settled. The movement worth carrying forward is in the decline profile: decline code ZA (Transaction declined by customer) fired 64 times — 0.456% of attempts against a trailing 0.334%. Owner: Customer. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,050, successes=13,501, failed=536, pending=13, settled_value_inr=15,758,055.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZA; count=64; rate_pct=0.46; trailing_rate_pct=0.33; owner=Customer; z=2.18
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- categories: mcc_category=Bills; attempts=1,181; own_median=852; z=3.13
- products: product_name=UPI Lite; attempts=2,607; own_median=2,111.5; z=2.33
- banks: payer_bank=Union Bank of India; attempts=965; success_rate=94.72; own_median=96.21; z=-2.05
- banks: payer_bank=Indian Bank; attempts=450; success_rate=94; own_median=96.21; z=-2.64
- incidents: event_id=ADOPT-0074; kind=adoption_surge; severity=Sev-3; window=2026-06-22 to 2026-07-05; success_impact_pp=-0.45; volume_impact_pct=40.31
- products: product_name=Credit on UPI; attempts=308; success_rate=93.83; own_median=95.94; z=-2.22
- products: product_name=UPI International; attempts=171; success_rate=98.25; own_median=95.51; z=2.8

Refs: enterprise_data/warehouse/transactions, RPT-D174-DAILY, enterprise_data/warehouse/reference/incidents.parquet
