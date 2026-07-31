---
id: RPT-D37-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 10 Feb 2026)

**Report ID:** RPT-D37-DAILY · **Day 37 of 206** · **Derived from:** 9,866 transaction rows queried live from the warehouse

## Summary

The rail took **9,866 payment attempts** on Tuesday 10 February 2026 (Working day) and settled **₹1.07 Cr** across 9,048 successful payments. Volume was −5.0% on yesterday and −13.4% on the same weekday last week. Success closed at **91.71%**, below the trailing 28-day median of 95.41%.

Decline code BT (Acquirer / NPCI switch timeout) fired 109 times — 1.105% of attempts against a trailing 0.114%. Owner: NPCI. Decline code U54 (Transaction timed out at beneficiary) fired 122 times — 1.237% of attempts against a trailing 0.163%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,866 | −5.0% | −13.4% | 11,252 |
| Successful payments | 9,048 | −9.3% | −16.9% | 10,734 |
| Success rate | 91.71% | −4.34pp | −3.85pp | 95.34% |
| Settled value | ₹1.07 Cr | +0.5% | −20.8% | ₹1.28 Cr |
| Average ticket | ₹1,177 | +10.9% | −4.8% | ₹1,189 |
| Technical declines | 1.003% | +0.67pp | +0.61pp | 0.447% |
| Business declines | 4.267% | +1.12pp | +0.68pp | 3.445% |
| Risk declines | 0.132% | +0.04pp | +0.03pp | 0.152% |
| Timeout declines | 2.645% | +2.40pp | +2.37pp | 0.495% |
| Retry share | 3.46% | +2.20pp | +2.20pp | 1.43% |
| Latency p95 | 1,948 ms | +52.2% | +56.8% | 1,317 ms |
| Active customers | 8,307 | −6.1% | −12.6% | 9,432 |
| Active merchants | 1,234 | −1.7% | −3.3% | 1,269 |

## What moved

- Product UPI Person to Merchant ran at 91.23% success on 3,101 attempts (31.4% of the day), 4.64pp down its own 28-day median.
- Category Retail ran at 92.11% success on 2,688 attempts (41.8% of the day), 3.98pp down its own 28-day median.
- Success rate closed at 91.71%, 3.70pp down the trailing median — a 5.9-sigma move.
- App PhonePe ran at 91.73% success on 4,680 attempts (47.4% of the day), 3.62pp down its own 28-day median.
- Product UPI Person to Person ran at 91.40% success on 3,441 attempts (34.9% of the day), 3.31pp down its own 28-day median.
- Region South ran at 91.25% success on 2,914 attempts (29.5% of the day), 3.93pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,441 | 34.9% | 91.40% | ₹37.32 L | −12.6% |
| UPI Person to Merchant | 3,101 | 31.4% | 91.23% | ₹29.53 L | +0.3% |
| UPI QR Payments | 1,520 | 15.4% | 92.30% | ₹6.81 L | −15.2% |
| UPI Lite | 717 | 7.3% | 96.09% | ₹61,837 | −1.2% |
| UPI AutoPay | 328 | 3.3% | 88.11% | ₹5.25 L | +8.6% |
| RuPay Credit on UPI | 189 | 1.9% | 92.06% | ₹6.37 L | −3.6% |
| Credit on UPI | 156 | 1.6% | 88.46% | ₹9.48 L | +7.6% |
| Recurring Payments | 94 | 1.0% | 85.11% | ₹4.04 L | +13.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,043 | 91.62% | 95.40% | ₹30.92 L | ⚠ outlier |
| HDFC Bank | 1,107 | 92.50% | 96.02% | ₹12.18 L | ⚠ outlier |
| Bank of Baroda | 750 | 93.60% | 94.99% | ₹8.60 L | normal |
| Union Bank of India | 707 | 90.66% | 94.81% | ₹9.42 L | ⚠ outlier |
| Punjab National Bank | 617 | 89.47% | 94.76% | ₹6.71 L | ⚠ outlier |
| Axis Bank | 592 | 91.89% | 95.13% | ₹5.35 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,680 | 91.73% | 95.35% | ₹50.52 L | ⚠ outlier |
| Google Pay | 3,281 | 92.41% | 95.45% | ₹34.13 L | ⚠ outlier |
| Paytm | 773 | 91.72% | 94.98% | ₹10.53 L | ⚠ outlier |
| Navi | 363 | 90.08% | 95.86% | ₹4.31 L | ⚠ outlier |
| SuperMoney | 198 | 91.41% | 96.27% | ₹2.14 L | ⚠ outlier |
| BHIM | 113 | 92.92% | 94.86% | ₹89,408 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,688 | 92.11% | ₹28.71 L |
| Food & Beverage | 1,529 | 93.59% | ₹7.47 L |
| Bills | 684 | 92.84% | ₹9.76 L |
| Mobility | 680 | 91.03% | ₹3.33 L |
| Healthcare | 332 | 90.36% | ₹2.54 L |
| Digital | 196 | 88.78% | ₹81,566 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,914 | 29.5% | 91.25% | ₹32.12 L |
| North | 2,506 | 25.4% | 91.94% | ₹27.50 L |
| West | 2,434 | 24.7% | 91.95% | ₹27.13 L |
| East | 1,146 | 11.6% | 91.45% | ₹11.46 L |
| Central | 866 | 8.8% | 92.26% | ₹8.31 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 90.32% | ₹1.77 L |
| Rapid Bazaar | Key Account | Retail | 245 | 93.47% | ₹1.45 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 95.95% | ₹1.45 L |
| Ujjwal Water Board | Key Account | Bills | 46 | 95.65% | ₹94,825 |
| Hampi Stores 2298 | Key Account | Retail | 92 | 94.57% | ₹93,803 |
| Yamuna Restaurant | Key Account | Food & Beverage | 71 | 91.55% | ₹83,169 |
| Urban Boutique | Key Account | Retail | 87 | 90.80% | ₹70,421 |
| Girnar Connect | Key Account | Bills | 105 | 93.33% | ₹53,058 |

## Failure analysis

Of 794 declined attempts, 421 were business declines (4.267% of attempts — balances, PINs and limits), 99 technical (1.003%), 261 timeouts (2.645%) and 13 risk declines (0.132%).

341 attempts were re-presentations of an earlier failure (3.46% of the day); 29.0% of them succeeded.

- Decline code BT (Acquirer / NPCI switch timeout) fired 109 times — 1.105% of attempts against a trailing 0.114%. Owner: NPCI.
- Decline code U54 (Transaction timed out at beneficiary) fired 122 times — 1.237% of attempts against a trailing 0.163%. Owner: Issuer.
- Retries reached 341 attempts (3.46% of the day, 13.4 sigma above normal). Only 29.0% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 30 times — 0.304% of attempts against a trailing 0.044%. Owner: NPCI.
- Decline code ZM (Invalid UPI PIN) fired 189 times — 1.916% of attempts against a trailing 1.132%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 189 | 1.916% | 1.132% |
| Z9 | Insufficient funds | business | Customer | 143 | 1.449% | 1.464% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 122 | 1.237% | 0.163% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 109 | 1.105% | 0.114% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.436% | 0.423% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.385% | 0.227% |
| U28 | Remitter bank unavailable | technical | Issuer | 32 | 0.324% | 0.140% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 30 | 0.304% | 0.044% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 81 | 66 |
| Auto-reversals | 42 | 21 |
| Disputes / chargebacks | 6 | 3 |
| Value returned | ₹1.20 L | ₹1.15 L |

## Customer behaviour

8,307 distinct customers transacted (−6.5% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,538 | 2,884 | 1.14 | 91.71% | ₹1,084 |
| power | 1,761 | 2,278 | 1.29 | 91.22% | ₹1,460 |
| merchant_heavy | 1,898 | 2,239 | 1.18 | 92.72% | ₹927 |
| small_ticket | 1,266 | 1,552 | 1.23 | 91.37% | ₹519 |
| occasional | 627 | 675 | 1.08 | 91.70% | ₹1,552 |
| new | 182 | 202 | 1.11 | 88.61% | ₹1,226 |
| dormant_returning | 35 | 36 | 1.03 | 91.67% | ₹660 |

## Operational events

- **INC-NET-0038** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 19:00 and 22:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0021** (Sev-2) — Bank of Baroda issuer decline spike, scoped to Bank of Baroda between 10:00 and 16:00. Bank of Baroda core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code BT (Acquirer / NPCI switch timeout) fired 109 times — 1.105% of attempts against a trailing 0.114%. Owner: NPCI.
- Decline code U54 (Transaction timed out at beneficiary) fired 122 times — 1.237% of attempts against a trailing 0.163%. Owner: Issuer.
- Retries reached 341 attempts (3.46% of the day, 13.4 sigma above normal). Only 29.0% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 30 times — 0.304% of attempts against a trailing 0.044%. Owner: NPCI.
- Product UPI Person to Merchant ran at 91.23% success on 3,101 attempts (31.4% of the day), 4.64pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

10 February was an incident day: INC-NET-0038, INC-FRAUD-0049 were live and the rail closed at 91.71% success against a 95.41% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,866, successes=9,048, failed=794, pending=24, settled_value_inr=10,651,178.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=BT; count=109; rate_pct=1.1; trailing_rate_pct=0.11; owner=NPCI; z=33.76
- failures: failure_code=U54; count=122; rate_pct=1.24; trailing_rate_pct=0.16; owner=Issuer; z=23.14
- failures: retries=341; retry_share_pct=3.46; recovery_pct=29.03; z=13.39
- failures: failure_code=U67; count=30; rate_pct=0.3; trailing_rate_pct=0.04; owner=NPCI; z=15.69
- products: product_name=UPI Person to Merchant; attempts=3,101; success_rate=91.23; own_median=95.86; z=-11.77
- failures: failure_code=ZM; count=189; rate_pct=1.92; trailing_rate_pct=1.13; owner=Customer; z=4.58
- categories: mcc_category=Retail; attempts=2,688; success_rate=92.11; own_median=96.09; z=-8.23
- headline: success_rate=91.71; trailing_median=95.41; z=-5.95
- psps: payer_psp=PhonePe; attempts=4,680; success_rate=91.73; own_median=95.35; z=-6.36
- products: product_name=UPI Person to Person; attempts=3,441; success_rate=91.4; own_median=94.71; z=-6.93

Refs: enterprise_data/warehouse/transactions, RPT-D36-DAILY, enterprise_data/warehouse/reference/incidents.parquet
