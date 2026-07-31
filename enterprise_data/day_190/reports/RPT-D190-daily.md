---
id: RPT-D190-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-13T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 13 Jul 2026)

**Report ID:** RPT-D190-DAILY · **Day 190 of 206** · **Derived from:** 14,549 transaction rows queried live from the warehouse

## Summary

The rail took **14,549 payment attempts** on Monday 13 July 2026 (Working day) and settled **₹2.06 Cr** across 14,006 successful payments. Volume was +1.9% on yesterday and −13.1% on the same weekday last week. Success closed at **96.27%**, in line with the trailing 28-day median of 96.11%.

Decline code XH (Account does not exist / frozen) fired 42 times — 0.289% of attempts against a trailing 0.187%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,549 | +1.9% | −13.1% | 16,754 |
| Successful payments | 14,006 | +2.2% | −13.6% | 16,093 |
| Success rate | 96.27% | +0.34pp | −0.51pp | 96.09% |
| Settled value | ₹2.06 Cr | +28.2% | −12.1% | ₹2.12 Cr |
| Average ticket | ₹1,469 | +25.4% | +1.7% | ₹1,315 |
| Technical declines | 0.488% | +0.07pp | +0.03pp | 0.491% |
| Business declines | 2.797% | −0.44pp | +0.48pp | 2.749% |
| Risk declines | 0.103% | +0.01pp | −0.05pp | 0.109% |
| Timeout declines | 0.268% | +0.07pp | +0.02pp | 0.472% |
| Retry share | 1.14% | −0.27pp | +0.22pp | 1.44% |
| Latency p95 | 1,298 ms | +4.3% | +1.9% | 1,305 ms |
| Active customers | 12,065 | +1.5% | −11.0% | 13,529 |
| Active merchants | 1,585 | +3.7% | −3.0% | 1,626 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,457 | 30.6% | 95.06% | ₹48.76 L | +0.1% |
| UPI Person to Merchant | 3,253 | 22.4% | 96.31% | ₹28.57 L | −10.1% |
| UPI Lite | 2,199 | 15.1% | 98.45% | ₹1.97 L | −14.3% |
| UPI QR Payments | 2,041 | 14.0% | 96.77% | ₹9.16 L | −20.9% |
| UPI Circle | 741 | 5.1% | 96.76% | ₹6.34 L | −8.2% |
| Credit on UPI | 589 | 4.0% | 97.11% | ₹49.70 L | +24.1% |
| UPI AutoPay | 388 | 2.7% | 92.78% | ₹7.42 L | +2.8% |
| RuPay Credit on UPI | 378 | 2.6% | 97.62% | ₹18.67 L | +1.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,562 | 96.43% | 96.16% | ₹63.06 L | normal |
| HDFC Bank | 1,552 | 96.71% | 96.37% | ₹23.15 L | normal |
| Bank of Baroda | 1,106 | 96.56% | 96.22% | ₹15.22 L | normal |
| Union Bank of India | 1,008 | 96.53% | 96.12% | ₹17.81 L | normal |
| Axis Bank | 864 | 96.76% | 96.17% | ₹12.51 L | normal |
| ICICI Bank | 861 | 96.40% | 96.34% | ₹8.78 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,730 | 96.24% | 96.15% | ₹96.38 L | normal |
| Google Pay | 4,841 | 96.49% | 96.13% | ₹63.76 L | normal |
| Paytm | 1,287 | 95.49% | 96.24% | ₹18.03 L | normal |
| Navi | 525 | 96.19% | 96.37% | ₹11.01 L | normal |
| SuperMoney | 287 | 97.21% | 96.12% | ₹2.77 L | normal |
| BHIM | 150 | 96.67% | 95.85% | ₹1.67 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,161 | 96.88% | ₹61.33 L |
| Food & Beverage | 2,510 | 96.97% | ₹12.31 L |
| Mobility | 1,241 | 97.82% | ₹6.30 L |
| Bills | 921 | 96.85% | ₹7.98 L |
| Healthcare | 547 | 97.26% | ₹7.24 L |
| Digital | 215 | 94.42% | ₹1.00 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,344 | 29.9% | 96.41% | ₹57.24 L |
| North | 3,756 | 25.8% | 95.71% | ₹52.09 L |
| West | 3,607 | 24.8% | 96.17% | ₹56.07 L |
| East | 1,618 | 11.1% | 97.03% | ₹26.28 L |
| Central | 1,224 | 8.4% | 96.73% | ₹14.08 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 80 | 93.75% | ₹3.84 L |
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹2.56 L |
| Rapid Bazaar | Key Account | Retail | 406 | 97.78% | ₹1.85 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 95.89% | ₹96,901 |
| Hampi Styles | Key Account | Retail | 43 | 95.35% | ₹84,040 |
| Hampi Stores 2298 | Key Account | Retail | 104 | 98.08% | ₹81,179 |
| Girnar Connect | Key Account | Bills | 163 | 97.55% | ₹74,157 |
| Aravalli Pharmacy | Large | Healthcare | 88 | 100.00% | ₹63,502 |

## Failure analysis

Of 532 declined attempts, 407 were business declines (2.797% of attempts — balances, PINs and limits), 71 technical (0.488%), 39 timeouts (0.268%) and 15 risk declines (0.103%).

166 attempts were re-presentations of an earlier failure (1.14% of the day); 68.7% of them succeeded.

- Decline code XH (Account does not exist / frozen) fired 42 times — 0.289% of attempts against a trailing 0.187%. Owner: Issuer.
- Decline code UX (Mandate execution outside permitted window) fired 25 times — 0.172% of attempts against a trailing 0.079%. Owner: PSP.
- Decline code U30 (Debit failed at remitter bank) fired 38 times — 0.261% of attempts against a trailing 0.175%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 177 | 1.217% | 1.223% |
| ZM | Invalid UPI PIN | business | Customer | 115 | 0.790% | 0.970% |
| XH | Account does not exist / frozen | business | Issuer | 42 | 0.289% | 0.187% |
| ZA | Transaction declined by customer | business | Customer | 40 | 0.275% | 0.325% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.261% | 0.175% |
| UX | Mandate execution outside permitted window | business | PSP | 25 | 0.172% | 0.079% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.117% | 0.096% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.117% | 0.130% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 130 | 110 |
| Auto-reversals | 17 | 24 |
| Disputes / chargebacks | 15 | 14 |
| Value returned | ₹1.13 L | ₹1.71 L |

## Customer behaviour

12,065 distinct customers transacted (−8.0% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,672 | 4,189 | 1.14 | 96.20% | ₹1,723 |
| power | 2,687 | 3,628 | 1.35 | 96.36% | ₹1,793 |
| merchant_heavy | 2,771 | 3,324 | 1.20 | 96.51% | ₹1,146 |
| small_ticket | 1,854 | 2,254 | 1.22 | 95.79% | ₹638 |
| occasional | 873 | 924 | 1.06 | 96.32% | ₹1,457 |
| new | 185 | 206 | 1.11 | 97.57% | ₹748 |
| dormant_returning | 23 | 24 | 1.04 | 91.67% | ₹4,503 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Decline code XH (Account does not exist / frozen) fired 42 times — 0.289% of attempts against a trailing 0.187%. Owner: Issuer.
- Decline code UX (Mandate execution outside permitted window) fired 25 times — 0.172% of attempts against a trailing 0.079%. Owner: PSP.
- Decline code U30 (Debit failed at remitter bank) fired 38 times — 0.261% of attempts against a trailing 0.175%. Owner: Issuer.
- Issuer Punjab National Bank ran at 94.27% success on 838 attempts (5.8% of the day), 1.64pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

13 July ran on trend at 96.27% success and ₹2.06 Cr settled. The movement worth carrying forward is in the decline profile: decline code XH (Account does not exist / frozen) fired 42 times — 0.289% of attempts against a trailing 0.187%. Owner: Issuer. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-13` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,549, successes=14,006, failed=532, pending=11, settled_value_inr=20,576,662.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=XH; count=42; rate_pct=0.29; trailing_rate_pct=0.19; owner=Issuer; z=3.35
- failures: failure_code=UX; count=25; rate_pct=0.17; trailing_rate_pct=0.08; owner=PSP; z=3.21
- failures: failure_code=U30; count=38; rate_pct=0.26; trailing_rate_pct=0.17; owner=Issuer; z=2.19
- banks: payer_bank=Punjab National Bank; attempts=838; success_rate=94.27; own_median=95.92; z=-2.36

Refs: enterprise_data/warehouse/transactions, RPT-D189-DAILY, enterprise_data/warehouse/reference/incidents.parquet
