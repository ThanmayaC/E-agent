---
id: RPT-D15-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 19 Jan 2026)

**Report ID:** RPT-D15-DAILY · **Day 15 of 206** · **Derived from:** 9,995 transaction rows queried live from the warehouse

## Summary

The rail took **9,995 payment attempts** on Monday 19 January 2026 (Working day) and settled **₹1.11 Cr** across 9,464 successful payments. Volume was +9.0% on yesterday and −4.7% on the same weekday last week. Success closed at **94.69%**, below the trailing 28-day median of 95.44%.

Retries reached 183 attempts (1.83% of the day, 2.6 sigma above normal). 69.4% of re-presented payments recovered, so the retry path was doing its job. App PhonePe ran at 94.37% success on 4,853 attempts (48.6% of the day), 1.13pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,995 | +9.0% | −4.7% | 10,295 |
| Successful payments | 9,464 | +9.7% | −4.1% | 9,796 |
| Success rate | 94.69% | +0.60pp | +0.52pp | 95.13% |
| Settled value | ₹1.11 Cr | +19.2% | −0.8% | ₹1.16 Cr |
| Average ticket | ₹1,174 | +8.6% | +3.5% | ₹1,185 |
| Technical declines | 0.850% | +0.08pp | +0.02pp | 0.643% |
| Business declines | 3.942% | −0.44pp | −0.11pp | 3.557% |
| Risk declines | 0.070% | −0.13pp | −0.07pp | 0.132% |
| Timeout declines | 0.380% | −0.07pp | −0.15pp | 0.400% |
| Retry share | 1.83% | −0.08pp | −0.32pp | 1.48% |
| Latency p95 | 1,255 ms | −3.6% | −0.9% | 1,243 ms |
| Active customers | 8,499 | +8.1% | −3.7% | 8,729 |
| Active merchants | 1,188 | +3.0% | −1.8% | 1,202 |

## What moved

- App PhonePe ran at 94.37% success on 4,853 attempts (48.6% of the day), 1.13pp down its own 28-day median.
- Region South ran at 94.23% success on 2,965 attempts (29.7% of the day), 1.19pp down its own 28-day median.
- Success rate closed at 94.69%, 0.75pp down the trailing median — a 1.6-sigma move.
- Issuer Kotak Mahindra Bank ran at 91.45% success on 339 attempts (3.4% of the day), 3.97pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,702 | 37.0% | 94.38% | ₹36.39 L | −7.9% |
| UPI Person to Merchant | 3,176 | 31.8% | 95.03% | ₹30.61 L | +7.3% |
| UPI QR Payments | 1,497 | 15.0% | 94.86% | ₹5.77 L | −15.1% |
| UPI Lite | 626 | 6.3% | 98.24% | ₹57,039 | −4.3% |
| UPI AutoPay | 306 | 3.1% | 84.97% | ₹5.42 L | +0.7% |
| RuPay Credit on UPI | 206 | 2.1% | 95.15% | ₹8.63 L | +13.5% |
| Credit on UPI | 115 | 1.2% | 95.65% | ₹6.96 L | −20.1% |
| Recurring Payments | 85 | 0.9% | 90.59% | ₹3.87 L | +1.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,182 | 94.19% | 94.92% | ₹36.79 L | normal |
| HDFC Bank | 1,077 | 95.73% | 96.16% | ₹12.91 L | normal |
| Bank of Baroda | 775 | 95.87% | 94.45% | ₹6.86 L | normal |
| Union Bank of India | 697 | 93.54% | 94.90% | ₹6.00 L | normal |
| ICICI Bank | 592 | 94.59% | 96.01% | ₹5.71 L | normal |
| Punjab National Bank | 585 | 94.87% | 95.09% | ₹7.11 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,853 | 94.37% | 95.51% | ₹55.50 L | ⚠ outlier |
| Google Pay | 3,235 | 95.24% | 95.22% | ₹35.52 L | normal |
| Paytm | 797 | 94.23% | 94.68% | ₹8.24 L | normal |
| Navi | 331 | 94.56% | 95.37% | ₹3.41 L | normal |
| SuperMoney | 198 | 94.95% | 95.93% | ₹2.64 L | normal |
| BHIM | 105 | 93.33% | 95.41% | ₹63,585 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,655 | 95.25% | ₹29.12 L |
| Food & Beverage | 1,541 | 95.78% | ₹7.66 L |
| Bills | 657 | 95.89% | ₹8.19 L |
| Mobility | 604 | 95.36% | ₹3.55 L |
| Healthcare | 319 | 94.67% | ₹3.17 L |
| Digital | 199 | 89.45% | ₹80,684 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,965 | 29.7% | 94.23% | ₹33.91 L |
| North | 2,551 | 25.5% | 95.37% | ₹27.73 L |
| West | 2,440 | 24.4% | 94.34% | ₹27.99 L |
| East | 1,208 | 12.1% | 94.29% | ₹13.20 L |
| Central | 831 | 8.3% | 95.79% | ₹8.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 90.62% | ₹1.80 L |
| Vasant Wardrobe | Key Account | Retail | 59 | 96.61% | ₹1.73 L |
| Rapid Bazaar | Key Account | Retail | 270 | 98.52% | ₹1.31 L |
| Ujjwal Water Board | Key Account | Bills | 42 | 95.24% | ₹1.12 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 67 | 98.51% | ₹1.11 L |
| Hampi Stores 2298 | Key Account | Retail | 81 | 95.06% | ₹67,324 |
| Girnar Connect | Key Account | Bills | 106 | 95.28% | ₹44,768 |
| Shakti Stores 1531 | Key Account | Retail | 48 | 95.83% | ₹38,915 |

## Failure analysis

Of 524 declined attempts, 394 were business declines (3.942% of attempts — balances, PINs and limits), 85 technical (0.850%), 38 timeouts (0.380%) and 7 risk declines (0.070%).

183 attempts were re-presentations of an earlier failure (1.83% of the day); 69.4% of them succeeded.

- Retries reached 183 attempts (1.83% of the day, 2.6 sigma above normal). 69.4% of re-presented payments recovered, so the retry path was doing its job.
- Decline code ZX (Mandate not found or revoked) fired 16 times — 0.160% of attempts against a trailing 0.090%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 160 | 1.601% | 1.460% |
| ZM | Invalid UPI PIN | business | Customer | 134 | 1.341% | 1.099% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.440% | 0.376% |
| U30 | Debit failed at remitter bank | technical | Issuer | 33 | 0.330% | 0.268% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.260% | 0.263% |
| U28 | Remitter bank unavailable | technical | Issuer | 22 | 0.220% | 0.178% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.170% | 0.185% |
| U69 | Beneficiary bank offline | technical | Issuer | 16 | 0.160% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 68 | 29 |
| Auto-reversals | 18 | 22 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹1.64 L | ₹57,544 |

## Customer behaviour

8,499 distinct customers transacted (−4.0% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,605 | 2,940 | 1.13 | 94.59% | ₹1,161 |
| power | 1,771 | 2,315 | 1.31 | 94.43% | ₹1,535 |
| merchant_heavy | 1,942 | 2,282 | 1.18 | 94.57% | ₹947 |
| small_ticket | 1,300 | 1,538 | 1.18 | 95.58% | ₹589 |
| occasional | 674 | 702 | 1.04 | 94.30% | ₹1,306 |
| new | 181 | 191 | 1.06 | 94.76% | ₹775 |
| dormant_returning | 26 | 27 | 1.04 | 96.30% | ₹426 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- App PhonePe ran at 94.37% success on 4,853 attempts (48.6% of the day), 1.13pp down its own 28-day median.
- Region South ran at 94.23% success on 2,965 attempts (29.7% of the day), 1.19pp down its own 28-day median.
- Success rate closed at 94.69%, 0.75pp down the trailing median — a 1.6-sigma move.
- Issuer Kotak Mahindra Bank ran at 91.45% success on 339 attempts (3.4% of the day), 3.97pp down its own 28-day median.
- Decline code ZX (Mandate not found or revoked) fired 16 times — 0.160% of attempts against a trailing 0.090%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 19 January: success came in 0.75pp below baseline at 94.69% on 9,995 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,995, successes=9,464, failed=524, pending=7, settled_value_inr=11,111,079.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=183; retry_share_pct=1.83; recovery_pct=69.4; z=2.56
- psps: payer_psp=PhonePe; attempts=4,853; success_rate=94.37; own_median=95.51; z=-3.21
- geography: region=South; attempts=2,965; success_rate=94.23; own_median=95.42; z=-2.38
- headline: success_rate=94.69; trailing_median=95.44; z=-1.57
- banks: payer_bank=Kotak Mahindra Bank; attempts=339; success_rate=91.45; own_median=95.42; z=-4.35
- failures: failure_code=ZX; count=16; rate_pct=0.16; trailing_rate_pct=0.09; owner=PSP; z=2.25
- categories: mcc_category=Digital; attempts=199; success_rate=89.45; own_median=93.44; z=-2.34
- banks: payer_bank=IndusInd Bank; attempts=214; success_rate=92.99; own_median=95.73; z=-2.58
- categories: mcc_category=Services; attempts=89; success_rate=89.89; own_median=94.31; z=-2.25
- banks: payer_bank=IndusInd Bank; attempts=214; own_median=241; z=-2.43

Refs: enterprise_data/warehouse/transactions, RPT-D14-DAILY, enterprise_data/warehouse/reference/incidents.parquet
