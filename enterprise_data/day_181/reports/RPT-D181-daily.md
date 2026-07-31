---
id: RPT-D181-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-04T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 04 Jul 2026)

**Report ID:** RPT-D181-DAILY · **Day 181 of 206** · **Derived from:** 19,832 transaction rows queried live from the warehouse

## Summary

The rail took **19,832 payment attempts** on Saturday 04 July 2026 (Weekend) and settled **₹2.35 Cr** across 18,413 successful payments. Volume was +14.2% on yesterday and +22.9% on the same weekday last week. Success closed at **92.84%**, below the trailing 28-day median of 96.21%.

Decline code U54 (Transaction timed out at beneficiary) fired 260 times — 1.311% of attempts against a trailing 0.133%. Owner: Issuer. Decline code BT (Acquirer / NPCI switch timeout) fired 202 times — 1.019% of attempts against a trailing 0.092%. Owner: NPCI.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 19,832 | +14.2% | +22.9% | 18,481 |
| Successful payments | 18,413 | +9.7% | +18.5% | 17,666 |
| Success rate | 92.84% | −3.83pp | −3.41pp | 95.66% |
| Settled value | ₹2.35 Cr | +4.2% | +19.3% | ₹2.38 Cr |
| Average ticket | ₹1,276 | −5.0% | +0.6% | ₹1,349 |
| Technical declines | 1.361% | +1.02pp | +0.90pp | 0.599% |
| Business declines | 2.698% | +0.15pp | −0.13pp | 2.645% |
| Risk declines | 0.141% | +0.01pp | +0.02pp | 0.111% |
| Timeout declines | 2.849% | +2.61pp | +2.61pp | 0.901% |
| Retry share | 3.37% | +2.41pp | +2.26pp | 1.65% |
| Latency p95 | 1,844 ms | +46.7% | +44.4% | 1,389 ms |
| Active customers | 15,281 | +8.8% | +16.5% | 14,639 |
| Active merchants | 1,689 | +2.0% | +5.8% | 1,670 |

## What moved

- Success rate closed at 92.84%, 3.37pp down the trailing median — a 12.0-sigma move.
- App PhonePe ran at 93.07% success on 9,254 attempts (46.7% of the day), 3.03pp down its own 28-day median.
- Region South ran at 92.60% success on 5,853 attempts (29.5% of the day), 3.64pp down its own 28-day median.
- App Google Pay ran at 92.52% success on 6,667 attempts (33.6% of the day), 3.82pp down its own 28-day median.
- Issuer State Bank of India ran at 92.37% success on 6,223 attempts (31.4% of the day), 3.81pp down its own 28-day median.
- Category Retail ran at 93.29% success on 5,306 attempts (36.6% of the day), 3.58pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,333 | 26.9% | 91.79% | ₹53.88 L | +27.7% |
| UPI Person to Merchant | 4,476 | 22.6% | 92.72% | ₹46.80 L | +29.1% |
| UPI Lite | 3,836 | 19.3% | 95.18% | ₹3.34 L | +72.3% |
| UPI QR Payments | 3,249 | 16.4% | 93.29% | ₹12.67 L | +32.1% |
| UPI Circle | 1,219 | 6.1% | 92.04% | ₹11.43 L | +60.1% |
| RuPay Credit on UPI | 415 | 2.1% | 93.25% | ₹24.92 L | +12.8% |
| UPI AutoPay | 404 | 2.0% | 88.37% | ₹7.27 L | +8.7% |
| Credit on UPI | 384 | 1.9% | 92.97% | ₹33.65 L | −19.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 6,223 | 92.37% | 96.18% | ₹78.23 L | ⚠ outlier |
| HDFC Bank | 2,197 | 92.49% | 96.43% | ₹25.64 L | ⚠ outlier |
| Bank of Baroda | 1,503 | 93.81% | 96.22% | ₹15.14 L | ⚠ outlier |
| Union Bank of India | 1,382 | 92.69% | 96.00% | ₹15.04 L | ⚠ outlier |
| Punjab National Bank | 1,221 | 92.96% | 95.93% | ₹13.54 L | ⚠ outlier |
| Axis Bank | 1,219 | 93.68% | 96.15% | ₹14.11 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 9,254 | 93.07% | 96.11% | ₹1.09 Cr | ⚠ outlier |
| Google Pay | 6,667 | 92.52% | 96.33% | ₹78.98 L | ⚠ outlier |
| Paytm | 1,592 | 93.09% | 96.12% | ₹18.50 L | ⚠ outlier |
| Navi | 766 | 91.64% | 96.47% | ₹10.24 L | ⚠ outlier |
| SuperMoney | 389 | 93.83% | 95.97% | ₹5.23 L | ⚠ outlier |
| YONO SBI | 187 | 92.51% | 96.22% | ₹1.26 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,306 | 93.29% | ₹57.62 L |
| Food & Beverage | 3,573 | 93.95% | ₹15.10 L |
| Bills | 2,089 | 93.44% | ₹19.19 L |
| Mobility | 1,870 | 93.64% | ₹8.36 L |
| Healthcare | 731 | 92.61% | ₹11.27 L |
| Digital | 358 | 93.02% | ₹1.82 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,853 | 29.5% | 92.60% | ₹69.26 L |
| North | 5,111 | 25.8% | 92.62% | ₹58.85 L |
| West | 4,859 | 24.5% | 93.21% | ₹61.55 L |
| East | 2,287 | 11.5% | 92.65% | ₹29.34 L |
| Central | 1,722 | 8.7% | 93.55% | ₹15.86 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 555 | 94.41% | ₹2.37 L |
| Vasant Wardrobe | Key Account | Retail | 67 | 83.58% | ₹2.36 L |
| Ujjwal Water Board | Key Account | Bills | 92 | 96.74% | ₹2.27 L |
| Vega Electronics | Large | Retail | 33 | 90.91% | ₹2.22 L |
| Hampi Stores 2298 | Key Account | Retail | 140 | 93.57% | ₹1.40 L |
| Girnar Connect | Key Account | Bills | 321 | 93.46% | ₹1.23 L |
| Aravalli Pharmacy | Large | Healthcare | 120 | 96.67% | ₹1.12 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 88 | 96.59% | ₹90,641 |

## Failure analysis

Of 1,398 declined attempts, 535 were business declines (2.698% of attempts — balances, PINs and limits), 270 technical (1.361%), 565 timeouts (2.849%) and 28 risk declines (0.141%).

668 attempts were re-presentations of an earlier failure (3.37% of the day); 38.5% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 260 times — 1.311% of attempts against a trailing 0.133%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 202 times — 1.019% of attempts against a trailing 0.092%. Owner: NPCI.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 103 times — 0.519% of attempts against a trailing 0.037%. Owner: NPCI.
- Retries reached 668 attempts (3.37% of the day, 13.2 sigma above normal). Only 38.5% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U30 (Debit failed at remitter bank) fired 135 times — 0.681% of attempts against a trailing 0.176%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 260 | 1.311% | 0.133% |
| ZM | Invalid UPI PIN | business | Customer | 219 | 1.104% | 0.954% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 202 | 1.019% | 0.092% |
| Z9 | Insufficient funds | business | Customer | 194 | 0.978% | 1.220% |
| U30 | Debit failed at remitter bank | technical | Issuer | 135 | 0.681% | 0.176% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 103 | 0.519% | 0.037% |
| ZA | Transaction declined by customer | business | Customer | 58 | 0.292% | 0.325% |
| U28 | Remitter bank unavailable | technical | Issuer | 56 | 0.282% | 0.118% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 123 | 110 |
| Auto-reversals | 79 | 24 |
| Disputes / chargebacks | 13 | 14 |
| Value returned | ₹2.06 L | ₹1.70 L |

## Customer behaviour

15,281 distinct customers transacted (+27.2% on the 28-day median) at 1.30 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,882 | 5,971 | 1.22 | 92.92% | ₹1,416 |
| power | 3,190 | 4,790 | 1.50 | 92.57% | ₹1,651 |
| merchant_heavy | 3,416 | 4,411 | 1.29 | 92.95% | ₹813 |
| small_ticket | 2,289 | 3,046 | 1.33 | 92.71% | ₹553 |
| occasional | 1,198 | 1,276 | 1.07 | 93.18% | ₹1,271 |
| new | 257 | 287 | 1.12 | 93.38% | ₹657 |
| dormant_returning | 49 | 51 | 1.04 | 98.04% | ₹879 |

## Operational events

- **INC-NET-0040** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 20:00 and 24:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **CMP-0052** (Sev-3) — Hospitals cashback campaign, scoped to 8062. A cashback campaign across Hospitals merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U54 (Transaction timed out at beneficiary) fired 260 times — 1.311% of attempts against a trailing 0.133%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 202 times — 1.019% of attempts against a trailing 0.092%. Owner: NPCI.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 103 times — 0.519% of attempts against a trailing 0.037%. Owner: NPCI.
- Retries reached 668 attempts (3.37% of the day, 13.2 sigma above normal). Only 38.5% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U30 (Debit failed at remitter bank) fired 135 times — 0.681% of attempts against a trailing 0.176%. Owner: Issuer.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

04 July was an incident day: INC-NET-0040 was live and the rail closed at 92.84% success against a 96.21% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-04` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=19,832, successes=18,413, failed=1,398, pending=21, settled_value_inr=23,486,114.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U54; count=260; rate_pct=1.31; trailing_rate_pct=0.13; owner=Issuer; z=33.94
- failures: failure_code=BT; count=202; rate_pct=1.02; trailing_rate_pct=0.09; owner=NPCI; z=27.38
- failures: failure_code=U67; count=103; rate_pct=0.52; trailing_rate_pct=0.04; owner=NPCI; z=28.48
- failures: retries=668; retry_share_pct=3.37; recovery_pct=38.47; z=13.24
- failures: failure_code=U30; count=135; rate_pct=0.68; trailing_rate_pct=0.18; owner=Issuer; z=13.89
- headline: success_rate=92.84; trailing_median=96.21; z=-12.01
- psps: payer_psp=PhonePe; attempts=9,254; success_rate=93.07; own_median=96.11; z=-11.66
- adjustments: reversals=79; trailing_median=24; z=12.37
- geography: region=South; attempts=5,853; success_rate=92.6; own_median=96.24; z=-11.94
- psps: payer_psp=Google Pay; attempts=6,667; success_rate=92.52; own_median=96.33; z=-10.3

Refs: enterprise_data/warehouse/transactions, RPT-D180-DAILY, enterprise_data/warehouse/reference/incidents.parquet
