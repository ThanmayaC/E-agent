---
id: RPT-D131-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 15 May 2026)

**Report ID:** RPT-D131-DAILY · **Day 131 of 206** · **Derived from:** 14,232 transaction rows queried live from the warehouse

## Summary

The rail took **14,232 payment attempts** on Friday 15 May 2026 (Summer Travel Peak (build-up)) and settled **₹1.97 Cr** across 13,234 successful payments. Volume was +4.1% on yesterday and −14.5% on the same weekday last week. Success closed at **92.99%**, below the trailing 28-day median of 95.92%.

Decline code U54 (Transaction timed out at beneficiary) fired 160 times — 1.124% of attempts against a trailing 0.165%. Owner: Issuer. Decline code BT (Acquirer / NPCI switch timeout) fired 125 times — 0.878% of attempts against a trailing 0.116%. Owner: NPCI.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,232 | +4.1% | −14.5% | 14,942 |
| Successful payments | 13,234 | +0.6% | −17.3% | 14,327 |
| Success rate | 92.99% | −3.24pp | −3.14pp | 95.88% |
| Settled value | ₹1.97 Cr | −5.4% | −13.9% | ₹2.00 Cr |
| Average ticket | ₹1,486 | −6.0% | +4.1% | ₹1,394 |
| Technical declines | 1.349% | +0.87pp | +0.74pp | 0.538% |
| Business declines | 3.064% | +0.28pp | +0.30pp | 2.893% |
| Risk declines | 0.155% | +0.03pp | +0.02pp | 0.128% |
| Timeout declines | 2.333% | +2.05pp | +2.04pp | 0.456% |
| Retry share | 3.19% | +2.17pp | +2.12pp | 1.37% |
| Latency p95 | 1,978 ms | +57.8% | +59.0% | 1,296 ms |
| Active customers | 11,557 | +1.7% | −12.5% | 12,147 |
| Active merchants | 1,507 | +1.1% | −2.3% | 1,500 |

## What moved

- Product UPI Person to Person ran at 91.22% success on 3,862 attempts (27.1% of the day), 3.83pp down its own 28-day median.
- Success rate closed at 92.99%, 2.93pp down the trailing median — a 6.6-sigma move.
- Product UPI Person to Merchant ran at 93.29% success on 3,920 attempts (27.5% of the day), 2.69pp down its own 28-day median.
- Category Food & Beverage ran at 94.33% success on 2,593 attempts (25.0% of the day), 2.69pp down its own 28-day median.
- App PhonePe ran at 93.34% success on 6,695 attempts (47.0% of the day), 2.59pp down its own 28-day median.
- Product UPI Lite ran at 95.94% success on 1,947 attempts (13.7% of the day), 2.85pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 3,920 | 27.5% | 93.29% | ₹40.12 L | +1.6% |
| UPI Person to Person | 3,862 | 27.1% | 91.22% | ₹39.11 L | −11.9% |
| UPI QR Payments | 2,325 | 16.3% | 92.65% | ₹11.02 L | −0.9% |
| UPI Lite | 1,947 | 13.7% | 95.94% | ₹1.75 L | +27.6% |
| UPI Circle | 561 | 3.9% | 95.54% | ₹4.91 L | +18.7% |
| Credit on UPI | 404 | 2.8% | 93.56% | ₹31.53 L | +26.8% |
| RuPay Credit on UPI | 398 | 2.8% | 92.71% | ₹23.09 L | +11.8% |
| UPI AutoPay | 309 | 2.2% | 88.03% | ₹5.24 L | −5.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,427 | 93.29% | 95.96% | ₹54.67 L | ⚠ outlier |
| HDFC Bank | 1,591 | 93.09% | 96.01% | ₹22.15 L | ⚠ outlier |
| Bank of Baroda | 1,071 | 91.22% | 95.88% | ₹15.94 L | ⚠ outlier |
| Union Bank of India | 1,011 | 93.47% | 94.99% | ₹17.04 L | normal |
| Punjab National Bank | 919 | 92.06% | 95.52% | ₹10.42 L | ⚠ outlier |
| Axis Bank | 898 | 92.65% | 96.27% | ₹15.29 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,695 | 93.34% | 95.93% | ₹98.47 L | ⚠ outlier |
| Google Pay | 4,723 | 92.91% | 95.71% | ₹59.33 L | ⚠ outlier |
| Paytm | 1,176 | 91.84% | 95.95% | ₹14.72 L | ⚠ outlier |
| Navi | 552 | 92.57% | 95.54% | ₹5.60 L | ⚠ outlier |
| SuperMoney | 254 | 94.88% | 96.07% | ₹2.09 L | normal |
| BHIM | 136 | 93.38% | 95.46% | ₹3.05 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,374 | 93.67% | ₹51.03 L |
| Food & Beverage | 2,593 | 94.33% | ₹14.76 L |
| Mobility | 1,307 | 92.65% | ₹7.39 L |
| Bills | 864 | 94.79% | ₹10.21 L |
| Healthcare | 523 | 94.46% | ₹10.38 L |
| Digital | 217 | 94.01% | ₹1.01 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,084 | 28.7% | 93.51% | ₹64.22 L |
| North | 3,601 | 25.3% | 93.17% | ₹39.52 L |
| West | 3,563 | 25.0% | 92.39% | ₹54.15 L |
| East | 1,699 | 11.9% | 92.58% | ₹23.04 L |
| Central | 1,285 | 9.0% | 93.00% | ₹15.72 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 47 | 95.74% | ₹3.22 L |
| Vasant Wardrobe | Key Account | Retail | 90 | 88.89% | ₹3.16 L |
| Swift Grill | Large | Food & Beverage | 40 | 92.50% | ₹2.70 L |
| Ujjwal Water Board | Key Account | Bills | 46 | 97.83% | ₹2.18 L |
| Rapid Bazaar | Key Account | Retail | 390 | 93.59% | ₹1.75 L |
| Hampi Stores 2298 | Key Account | Retail | 139 | 96.40% | ₹1.29 L |
| Hampi Styles | Key Account | Retail | 51 | 86.27% | ₹1.13 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 81 | 95.06% | ₹89,365 |

## Failure analysis

Of 982 declined attempts, 436 were business declines (3.064% of attempts — balances, PINs and limits), 192 technical (1.349%), 332 timeouts (2.333%) and 22 risk declines (0.155%).

454 attempts were re-presentations of an earlier failure (3.19% of the day); 41.6% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 160 times — 1.124% of attempts against a trailing 0.165%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 125 times — 0.878% of attempts against a trailing 0.116%. Owner: NPCI.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 47 times — 0.330% of attempts against a trailing 0.052%. Owner: NPCI.
- Retries reached 454 attempts (3.19% of the day, 6.0 sigma above normal). Only 41.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U69 (Beneficiary bank offline) fired 53 times — 0.372% of attempts against a trailing 0.081%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 168 | 1.180% | 1.032% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 160 | 1.124% | 0.165% |
| Z9 | Insufficient funds | business | Customer | 158 | 1.110% | 1.214% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 125 | 0.878% | 0.116% |
| U30 | Debit failed at remitter bank | technical | Issuer | 69 | 0.485% | 0.209% |
| U28 | Remitter bank unavailable | technical | Issuer | 54 | 0.379% | 0.137% |
| U69 | Beneficiary bank offline | technical | Issuer | 53 | 0.372% | 0.081% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.344% | 0.355% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 91 | 90 |
| Auto-reversals | 62 | 28 |
| Disputes / chargebacks | 18 | 13 |
| Value returned | ₹1.88 L | ₹1.51 L |

## Customer behaviour

11,557 distinct customers transacted (+1.2% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,553 | 4,169 | 1.17 | 92.30% | ₹1,589 |
| power | 2,468 | 3,382 | 1.37 | 93.23% | ₹1,839 |
| merchant_heavy | 2,706 | 3,324 | 1.23 | 93.02% | ₹1,096 |
| small_ticket | 1,723 | 2,160 | 1.25 | 94.12% | ₹567 |
| occasional | 883 | 952 | 1.08 | 92.44% | ₹1,864 |
| new | 195 | 216 | 1.11 | 92.59% | ₹792 |
| dormant_returning | 29 | 29 | 1.00 | 96.55% | ₹294 |

## Operational events

- **INC-NET-0036** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 11:00 and 14:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **CMP-0061** (Sev-3) — Wealth & SIP cashback campaign, scoped to 6211. A cashback campaign across Wealth & SIP merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **REG-0069** (Sev-3) — UPI International — two new acceptance corridors live, scoped to UPI_INTL. Two new cross-border acceptance corridors went live. Volume steps up; early-corridor settlement immaturity temporarily depresses the success rate.

## Risks and opportunities

### Risks

- Decline code U54 (Transaction timed out at beneficiary) fired 160 times — 1.124% of attempts against a trailing 0.165%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 125 times — 0.878% of attempts against a trailing 0.116%. Owner: NPCI.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 47 times — 0.330% of attempts against a trailing 0.052%. Owner: NPCI.
- Product UPI Person to Person ran at 91.22% success on 3,862 attempts (27.1% of the day), 3.83pp down its own 28-day median.
- Retries reached 454 attempts (3.19% of the day, 6.0 sigma above normal). Only 41.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

15 May was an incident day: INC-NET-0036 was live and the rail closed at 92.99% success against a 95.92% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,232, successes=13,234, failed=982, pending=16, settled_value_inr=19,665,326.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U54; count=160; rate_pct=1.12; trailing_rate_pct=0.16; owner=Issuer; z=25.11
- failures: failure_code=BT; count=125; rate_pct=0.88; trailing_rate_pct=0.12; owner=NPCI; z=23.27
- failures: failure_code=U67; count=47; rate_pct=0.33; trailing_rate_pct=0.05; owner=NPCI; z=16.08
- products: product_name=UPI Person to Person; attempts=3,862; success_rate=91.22; own_median=95.05; z=-11.33
- failures: retries=454; retry_share_pct=3.19; recovery_pct=41.63; z=5.96
- headline: success_rate=92.99; trailing_median=95.92; z=-6.57
- failures: failure_code=U69; count=53; rate_pct=0.37; trailing_rate_pct=0.08; owner=Issuer; z=8.8
- products: product_name=UPI Person to Merchant; attempts=3,920; success_rate=93.29; own_median=95.98; z=-8.51
- categories: mcc_category=Food & Beverage; attempts=2,593; success_rate=94.33; own_median=97.02; z=-8.76
- psps: payer_psp=PhonePe; attempts=6,695; success_rate=93.34; own_median=95.93; z=-5.74

Refs: enterprise_data/warehouse/transactions, RPT-D130-DAILY, enterprise_data/warehouse/reference/incidents.parquet
