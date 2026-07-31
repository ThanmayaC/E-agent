---
id: RPT-D103-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 17 Apr 2026)

**Report ID:** RPT-D103-DAILY · **Day 103 of 206** · **Derived from:** 12,333 transaction rows queried live from the warehouse

## Summary

The rail took **12,333 payment attempts** on Friday 17 April 2026 (Working day) and settled **₹1.47 Cr** across 11,042 successful payments. Volume was +5.9% on yesterday and −4.7% on the same weekday last week. Success closed at **89.53%**, below the trailing 28-day median of 95.92%.

Decline code BT (Acquirer / NPCI switch timeout) fired 212 times — 1.719% of attempts against a trailing 0.102%. Owner: NPCI. Decline code U54 (Transaction timed out at beneficiary) fired 291 times — 2.360% of attempts against a trailing 0.182%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,333 | +5.9% | −4.7% | 12,554 |
| Successful payments | 11,042 | −0.6% | −11.3% | 11,945 |
| Success rate | 89.53% | −5.86pp | −6.70pp | 95.13% |
| Settled value | ₹1.47 Cr | −10.8% | −18.3% | ₹1.62 Cr |
| Average ticket | ₹1,329 | −10.2% | −7.9% | ₹1,353 |
| Technical declines | 2.051% | +1.38pp | +1.72pp | 0.628% |
| Business declines | 3.422% | +0.15pp | +0.42pp | 3.156% |
| Risk declines | 0.186% | −0.00pp | +0.10pp | 0.150% |
| Timeout declines | 4.565% | +4.18pp | +4.31pp | 0.813% |
| Retry share | 4.99% | +3.70pp | +3.91pp | 1.75% |
| Latency p95 | 2,288 ms | +81.7% | +76.5% | 1,376 ms |
| Active customers | 10,007 | +1.6% | −6.7% | 10,426 |
| Active merchants | 1,373 | −0.5% | −0.3% | 1,377 |

## What moved

- Success rate closed at 89.53%, 6.39pp down the trailing median — a 17.1-sigma move.
- App PhonePe ran at 89.05% success on 5,806 attempts (47.1% of the day), 6.76pp down its own 28-day median.
- Category Retail ran at 89.25% success on 3,301 attempts (40.2% of the day), 6.93pp down its own 28-day median.
- App Google Pay ran at 89.51% success on 4,100 attempts (33.2% of the day), 6.17pp down its own 28-day median.
- Product UPI Person to Person ran at 89.25% success on 4,130 attempts (33.5% of the day), 6.02pp down its own 28-day median.
- Region North ran at 89.32% success on 3,110 attempts (25.2% of the day), 6.44pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,130 | 33.5% | 89.25% | ₹41.82 L | −5.0% |
| UPI Person to Merchant | 3,271 | 26.5% | 88.66% | ₹33.37 L | −4.3% |
| UPI QR Payments | 2,111 | 17.1% | 90.90% | ₹8.11 L | −1.9% |
| UPI Lite | 1,148 | 9.3% | 91.11% | ₹96,864 | +9.2% |
| RuPay Credit on UPI | 336 | 2.7% | 89.29% | ₹16.17 L | +21.5% |
| UPI Circle | 329 | 2.7% | 89.67% | ₹2.62 L | +27.8% |
| UPI AutoPay | 323 | 2.6% | 87.62% | ₹5.68 L | +0.9% |
| Credit on UPI | 265 | 2.1% | 85.66% | ₹15.54 L | +41.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,827 | 89.16% | 95.92% | ₹42.97 L | ⚠ outlier |
| HDFC Bank | 1,350 | 89.93% | 95.92% | ₹16.07 L | ⚠ outlier |
| Bank of Baroda | 961 | 90.63% | 95.81% | ₹11.15 L | ⚠ outlier |
| Union Bank of India | 845 | 89.70% | 95.89% | ₹8.78 L | ⚠ outlier |
| ICICI Bank | 766 | 89.56% | 96.29% | ₹9.12 L | ⚠ outlier |
| Punjab National Bank | 765 | 89.28% | 95.60% | ₹8.61 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,806 | 89.05% | 95.80% | ₹68.99 L | ⚠ outlier |
| Google Pay | 4,100 | 89.51% | 95.69% | ₹47.50 L | ⚠ outlier |
| Paytm | 1,008 | 89.78% | 95.85% | ₹12.31 L | ⚠ outlier |
| Navi | 435 | 94.25% | 95.77% | ₹5.81 L | normal |
| SuperMoney | 207 | 90.82% | 94.87% | ₹3.82 L | ⚠ outlier |
| BHIM | 120 | 85.83% | 96.12% | ₹1.31 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,301 | 89.25% | ₹39.54 L |
| Food & Beverage | 2,018 | 91.03% | ₹9.57 L |
| Mobility | 951 | 90.01% | ₹4.96 L |
| Bills | 896 | 88.62% | ₹9.34 L |
| Healthcare | 411 | 90.51% | ₹4.07 L |
| Digital | 195 | 93.85% | ₹69,984 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,658 | 29.7% | 89.42% | ₹41.33 L |
| North | 3,110 | 25.2% | 89.32% | ₹35.53 L |
| West | 3,039 | 24.6% | 88.98% | ₹43.88 L |
| East | 1,484 | 12.0% | 90.84% | ₹16.81 L |
| Central | 1,042 | 8.4% | 90.31% | ₹9.25 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 64 | 90.62% | ₹2.32 L |
| Hampi Stores 2298 | Key Account | Retail | 119 | 84.03% | ₹1.54 L |
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹1.46 L |
| Rapid Bazaar | Key Account | Retail | 316 | 91.46% | ₹1.19 L |
| Ujjwal Water Board | Key Account | Bills | 49 | 91.84% | ₹90,837 |
| Girnar Connect | Key Account | Bills | 150 | 92.67% | ₹87,030 |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 95.16% | ₹72,468 |
| Aravalli Pharmacy | Large | Healthcare | 81 | 88.89% | ₹66,497 |

## Failure analysis

Of 1,261 declined attempts, 422 were business declines (3.422% of attempts — balances, PINs and limits), 253 technical (2.051%), 563 timeouts (4.565%) and 23 risk declines (0.186%).

616 attempts were re-presentations of an earlier failure (4.99% of the day); 37.0% of them succeeded.

- Decline code BT (Acquirer / NPCI switch timeout) fired 212 times — 1.719% of attempts against a trailing 0.102%. Owner: NPCI.
- Decline code U54 (Transaction timed out at beneficiary) fired 291 times — 2.360% of attempts against a trailing 0.182%. Owner: Issuer.
- Decline code U28 (Remitter bank unavailable) fired 93 times — 0.754% of attempts against a trailing 0.103%. Owner: Issuer.
- Retries reached 616 attempts (4.99% of the day, 17.5 sigma above normal). Only 37.0% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U30 (Debit failed at remitter bank) fired 98 times — 0.795% of attempts against a trailing 0.191%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 291 | 2.360% | 0.182% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 212 | 1.719% | 0.102% |
| ZM | Invalid UPI PIN | business | Customer | 166 | 1.346% | 1.013% |
| Z9 | Insufficient funds | business | Customer | 157 | 1.273% | 1.322% |
| U30 | Debit failed at remitter bank | technical | Issuer | 98 | 0.795% | 0.191% |
| U28 | Remitter bank unavailable | technical | Issuer | 93 | 0.754% | 0.103% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 60 | 0.486% | 0.047% |
| U69 | Beneficiary bank offline | technical | Issuer | 49 | 0.397% | 0.063% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 78 | 78 |
| Auto-reversals | 84 | 22 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹2.49 L | ₹1.44 L |

## Customer behaviour

10,007 distinct customers transacted (−2.3% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,093 | 3,626 | 1.17 | 89.71% | ₹1,311 |
| power | 2,141 | 2,897 | 1.35 | 89.47% | ₹1,654 |
| merchant_heavy | 2,312 | 2,852 | 1.23 | 89.69% | ₹889 |
| small_ticket | 1,482 | 1,886 | 1.27 | 89.13% | ₹620 |
| occasional | 772 | 844 | 1.09 | 89.57% | ₹1,390 |
| new | 180 | 198 | 1.10 | 88.89% | ₹1,150 |
| dormant_returning | 27 | 30 | 1.11 | 86.67% | ₹891 |

## Operational events

- **INC-PSP-0033** (Sev-1) — SuperMoney app release regression, scoped to SuperMoney between 18:00 and 23:00. A SuperMoney client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-NET-0042** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 11:00 and 16:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code BT (Acquirer / NPCI switch timeout) fired 212 times — 1.719% of attempts against a trailing 0.102%. Owner: NPCI.
- Decline code U54 (Transaction timed out at beneficiary) fired 291 times — 2.360% of attempts against a trailing 0.182%. Owner: Issuer.
- Decline code U28 (Remitter bank unavailable) fired 93 times — 0.754% of attempts against a trailing 0.103%. Owner: Issuer.
- Retries reached 616 attempts (4.99% of the day, 17.5 sigma above normal). Only 37.0% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Success rate closed at 89.53%, 6.39pp down the trailing median — a 17.1-sigma move.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

17 April was an incident day: INC-PSP-0033, INC-NET-0042 were live and the rail closed at 89.53% success against a 95.92% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,333, successes=11,042, failed=1,261, pending=30, settled_value_inr=14,679,433.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=BT; count=212; rate_pct=1.72; trailing_rate_pct=0.1; owner=NPCI; z=90.43
- failures: failure_code=U54; count=291; rate_pct=2.36; trailing_rate_pct=0.18; owner=Issuer; z=34.95
- failures: failure_code=U28; count=93; rate_pct=0.75; trailing_rate_pct=0.1; owner=Issuer; z=24.42
- failures: retries=616; retry_share_pct=4.99; recovery_pct=37.01; z=17.51
- headline: success_rate=89.53; trailing_median=95.92; z=-17.08
- psps: payer_psp=PhonePe; attempts=5,806; success_rate=89.05; own_median=95.8; z=-16.26
- categories: mcc_category=Retail; attempts=3,301; success_rate=89.25; own_median=96.18; z=-17.58
- failures: failure_code=U30; count=98; rate_pct=0.79; trailing_rate_pct=0.19; owner=Issuer; z=12.25
- psps: payer_psp=Google Pay; attempts=4,100; success_rate=89.51; own_median=95.69; z=-16.19
- products: product_name=UPI Person to Person; attempts=4,130; success_rate=89.25; own_median=95.27; z=-12.59

Refs: enterprise_data/warehouse/transactions, RPT-D102-DAILY, enterprise_data/warehouse/reference/incidents.parquet
