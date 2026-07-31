---
id: RPT-D66-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 11 Mar 2026)

**Report ID:** RPT-D66-DAILY · **Day 66 of 206** · **Derived from:** 11,139 transaction rows queried live from the warehouse

## Summary

The rail took **11,139 payment attempts** on Wednesday 11 March 2026 (Working day) and settled **₹1.27 Cr** across 10,532 successful payments. Volume was +5.5% on yesterday and −30.3% on the same weekday last week. Success closed at **94.55%**, below the trailing 28-day median of 95.62%.

Retries reached 232 attempts (2.08% of the day, 4.9 sigma above normal). Only 49.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them. Decline code U54 (Transaction timed out at beneficiary) fired 47 times — 0.422% of attempts against a trailing 0.164%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,139 | +5.5% | −30.3% | 13,317 |
| Successful payments | 10,532 | +3.6% | −31.5% | 12,762 |
| Success rate | 94.55% | −1.72pp | −1.60pp | 95.82% |
| Settled value | ₹1.27 Cr | +2.4% | −26.6% | ₹1.52 Cr |
| Average ticket | ₹1,208 | −1.1% | +7.1% | ₹1,197 |
| Technical declines | 0.745% | +0.24pp | +0.34pp | 0.450% |
| Business declines | 3.591% | +0.74pp | +0.65pp | 3.167% |
| Risk declines | 0.117% | +0.01pp | −0.01pp | 0.114% |
| Timeout declines | 0.889% | +0.70pp | +0.58pp | 0.354% |
| Retry share | 2.08% | +0.94pp | +0.90pp | 1.26% |
| Latency p95 | 1,439 ms | +13.6% | +19.0% | 1,250 ms |
| Active customers | 9,355 | +4.0% | −26.6% | 10,913 |
| Active merchants | 1,306 | −0.2% | −3.7% | 1,337 |

## What moved

- Product UPI Person to Merchant ran at 94.58% success on 3,156 attempts (28.3% of the day), 1.39pp down its own 28-day median.
- Success rate closed at 94.55%, 1.07pp down the trailing median — a 2.8-sigma move.
- Category Retail ran at 94.82% success on 3,029 attempts (42.5% of the day), 1.32pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 75% across the trailing window to 160 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer State Bank of India ran at 93.86% success on 3,567 attempts (32.0% of the day), 1.66pp down its own 28-day median.
- Region West ran at 93.28% success on 2,812 attempts (25.2% of the day), 2.30pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,014 | 36.0% | 94.00% | ₹41.72 L | −0.6% |
| UPI Person to Merchant | 3,156 | 28.3% | 94.58% | ₹30.83 L | −1.4% |
| UPI QR Payments | 1,926 | 17.3% | 94.96% | ₹8.04 L | −1.6% |
| UPI Lite | 750 | 6.7% | 96.67% | ₹65,828 | −1.3% |
| UPI AutoPay | 340 | 3.1% | 91.18% | ₹5.81 L | +13.0% |
| RuPay Credit on UPI | 288 | 2.6% | 96.53% | ₹15.22 L | +35.5% |
| Credit on UPI | 170 | 1.5% | 95.88% | ₹8.63 L | +15.6% |
| UPI Circle | 160 | 1.4% | 95.62% | ₹1.18 L | +31.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,567 | 93.86% | 95.52% | ₹39.53 L | ⚠ outlier |
| HDFC Bank | 1,236 | 95.95% | 96.23% | ₹13.24 L | normal |
| Bank of Baroda | 806 | 95.53% | 95.47% | ₹10.17 L | normal |
| Union Bank of India | 790 | 94.18% | 95.43% | ₹9.35 L | normal |
| Axis Bank | 710 | 95.07% | 95.88% | ₹7.93 L | normal |
| Punjab National Bank | 693 | 95.96% | 95.03% | ₹8.49 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,320 | 94.44% | 95.66% | ₹58.77 L | ⚠ outlier |
| Google Pay | 3,663 | 94.95% | 95.67% | ₹43.45 L | normal |
| Paytm | 934 | 94.86% | 95.41% | ₹11.26 L | normal |
| Navi | 360 | 93.89% | 95.49% | ₹4.71 L | normal |
| SuperMoney | 201 | 94.03% | 95.88% | ₹1.84 L | normal |
| BHIM | 126 | 89.68% | 95.18% | ₹1.29 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,029 | 94.82% | ₹34.75 L |
| Food & Beverage | 1,733 | 95.33% | ₹9.11 L |
| Mobility | 784 | 96.30% | ₹4.94 L |
| Bills | 643 | 95.18% | ₹5.89 L |
| Healthcare | 380 | 93.68% | ₹3.95 L |
| Digital | 218 | 95.41% | ₹1.39 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,240 | 29.1% | 94.66% | ₹37.83 L |
| West | 2,812 | 25.2% | 93.28% | ₹33.31 L |
| North | 2,797 | 25.1% | 95.24% | ₹31.56 L |
| East | 1,273 | 11.4% | 96.47% | ₹14.25 L |
| Central | 1,017 | 9.1% | 93.41% | ₹10.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 67 | 94.03% | ₹2.05 L |
| Vega Electronics | Large | Retail | 25 | 96.00% | ₹1.91 L |
| Rapid Bazaar | Key Account | Retail | 297 | 94.61% | ₹1.46 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 81 | 95.06% | ₹96,823 |
| Girnar Connect | Key Account | Bills | 114 | 93.86% | ₹73,705 |
| Hampi Stores 2298 | Key Account | Retail | 86 | 95.35% | ₹70,988 |
| Aravalli Pharmacy | Large | Healthcare | 63 | 95.24% | ₹63,336 |
| Urban Boutique | Key Account | Retail | 86 | 87.21% | ₹52,258 |

## Failure analysis

Of 595 declined attempts, 400 were business declines (3.591% of attempts — balances, PINs and limits), 83 technical (0.745%), 99 timeouts (0.889%) and 13 risk declines (0.117%).

232 attempts were re-presentations of an earlier failure (2.08% of the day); 49.6% of them succeeded.

- Retries reached 232 attempts (2.08% of the day, 4.9 sigma above normal). Only 49.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U54 (Transaction timed out at beneficiary) fired 47 times — 0.422% of attempts against a trailing 0.164%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 35 times — 0.314% of attempts against a trailing 0.105%. Owner: NPCI.
- Decline code ZM (Invalid UPI PIN) fired 157 times — 1.409% of attempts against a trailing 1.101%. Owner: Customer.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 17 times — 0.153% of attempts against a trailing 0.045%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 157 | 1.409% | 1.101% |
| Z9 | Insufficient funds | business | Customer | 157 | 1.409% | 1.439% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.440% | 0.406% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 47 | 0.422% | 0.164% |
| U30 | Debit failed at remitter bank | technical | Issuer | 36 | 0.323% | 0.165% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 35 | 0.314% | 0.105% |
| U28 | Remitter bank unavailable | technical | Issuer | 22 | 0.198% | 0.119% |
| XH | Account does not exist / frozen | business | Issuer | 19 | 0.171% | 0.248% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 78 | 68 |
| Auto-reversals | 25 | 20 |
| Disputes / chargebacks | 8 | 9 |
| Value returned | ₹1.67 L | ₹89,740 |

## Customer behaviour

9,355 distinct customers transacted (+1.3% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,886 | 3,273 | 1.13 | 94.13% | ₹1,327 |
| power | 2,056 | 2,674 | 1.30 | 94.84% | ₹1,408 |
| merchant_heavy | 2,088 | 2,533 | 1.21 | 94.43% | ₹993 |
| small_ticket | 1,358 | 1,644 | 1.21 | 94.83% | ₹522 |
| occasional | 760 | 794 | 1.04 | 94.96% | ₹1,311 |
| new | 185 | 197 | 1.06 | 95.94% | ₹840 |
| dormant_returning | 22 | 24 | 1.09 | 87.50% | ₹1,413 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-NET-0037** (Sev-2) — NPCI switch latency degradation, scoped to ecosystem-wide between 19:00 and 21:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0065** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Retries reached 232 attempts (2.08% of the day, 4.9 sigma above normal). Only 49.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U54 (Transaction timed out at beneficiary) fired 47 times — 0.422% of attempts against a trailing 0.164%. Owner: Issuer.
- Product UPI Person to Merchant ran at 94.58% success on 3,156 attempts (28.3% of the day), 1.39pp down its own 28-day median.
- Decline code BT (Acquirer / NPCI switch timeout) fired 35 times — 0.314% of attempts against a trailing 0.105%. Owner: NPCI.
- Decline code ZM (Invalid UPI PIN) fired 157 times — 1.409% of attempts against a trailing 1.101%. Owner: Customer.

### Opportunities

- Product UPI 123Pay is compounding — attempts up 45% across the trailing window to 72 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

11 March was an incident day: INC-FRAUD-0046, INC-NET-0037 were live and the rail closed at 94.55% success against a 95.62% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,139, successes=10,532, failed=595, pending=12, settled_value_inr=12,722,794.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=232; retry_share_pct=2.08; recovery_pct=49.57; z=4.85
- failures: failure_code=U54; count=47; rate_pct=0.42; trailing_rate_pct=0.16; owner=Issuer; z=4.69
- products: product_name=UPI Person to Merchant; attempts=3,156; success_rate=94.58; own_median=95.97; z=-4.94
- failures: failure_code=BT; count=35; rate_pct=0.31; trailing_rate_pct=0.11; owner=NPCI; z=4.94
- failures: failure_code=ZM; count=157; rate_pct=1.41; trailing_rate_pct=1.1; owner=Customer; z=2.26
- headline: success_rate=94.55; trailing_median=95.62; z=-2.79
- categories: mcc_category=Retail; attempts=3,029; success_rate=94.82; own_median=96.14; z=-3.22
- products: product_name=UPI Circle; attempts=160; window_growth_pct=75.1; success_rate=95.62
- banks: payer_bank=State Bank of India; attempts=3,567; success_rate=93.86; own_median=95.52; z=-3.4
- geography: region=West; attempts=2,812; success_rate=93.28; own_median=95.58; z=-3.77

Refs: enterprise_data/warehouse/transactions, RPT-D65-DAILY, enterprise_data/warehouse/reference/incidents.parquet
