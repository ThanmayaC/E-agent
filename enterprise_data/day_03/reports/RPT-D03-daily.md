---
id: RPT-D03-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 07 Jan 2026)

**Report ID:** RPT-D03-DAILY · **Day 3 of 206** · **Derived from:** 10,469 transaction rows queried live from the warehouse

## Summary

The rail took **10,469 payment attempts** on Wednesday 07 January 2026 (Working day) and settled **₹1.25 Cr** across 10,018 successful payments. Volume was −0.3% on yesterday and — on the same weekday last week. Success closed at **95.69%**, in line with the trailing 28-day median of 95.62%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,469 | −0.3% | — | 10,527 |
| Successful payments | 10,018 | −0.1% | — | 10,068 |
| Success rate | 95.69% | +0.23pp | — | 95.64% |
| Settled value | ₹1.25 Cr | +4.0% | — | ₹1.28 Cr |
| Average ticket | ₹1,250 | +4.0% | — | ₹1,275 |
| Technical declines | 0.525% | −0.02pp | — | 0.513% |
| Business declines | 3.229% | −0.03pp | — | 3.186% |
| Risk declines | 0.086% | −0.10pp | — | 0.152% |
| Timeout declines | 0.373% | −0.02pp | — | 0.349% |
| Retry share | 1.19% | −0.20pp | — | 1.07% |
| Latency p95 | 1,268 ms | +1.1% | — | 1,265 ms |
| Active customers | 8,876 | −0.6% | — | 8,934 |
| Active merchants | 1,213 | −0.5% | — | 1,220 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,839 | 36.7% | 94.69% | ₹40.46 L | −4.1% |
| UPI Person to Merchant | 3,086 | 29.5% | 96.60% | ₹33.18 L | +3.0% |
| UPI QR Payments | 1,820 | 17.4% | 96.48% | ₹7.32 L | +3.3% |
| UPI Lite | 637 | 6.1% | 98.90% | ₹57,665 | −10.3% |
| UPI AutoPay | 306 | 2.9% | 87.91% | ₹5.58 L | −0.5% |
| RuPay Credit on UPI | 213 | 2.0% | 95.31% | ₹7.77 L | +12.7% |
| Credit on UPI | 180 | 1.7% | 95.00% | ₹12.80 L | +11.1% |
| UPI Circle | 88 | 0.8% | 96.59% | ₹1.21 L | −20.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,337 | 95.50% | 95.39% | ₹41.89 L | normal |
| HDFC Bank | 1,148 | 96.17% | 95.62% | ₹13.70 L | normal |
| Bank of Baroda | 810 | 97.16% | 95.10% | ₹9.28 L | normal |
| Union Bank of India | 767 | 94.78% | 95.83% | ₹9.80 L | normal |
| ICICI Bank | 642 | 95.17% | 95.59% | ₹6.25 L | normal |
| Punjab National Bank | 608 | 96.88% | 95.26% | ₹7.78 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,006 | 95.55% | 95.54% | ₹55.01 L | normal |
| Google Pay | 3,447 | 95.56% | 95.68% | ₹47.03 L | normal |
| Paytm | 790 | 96.71% | 95.23% | ₹8.55 L | normal |
| Navi | 375 | 96.00% | 96.09% | ₹5.27 L | normal |
| SuperMoney | 212 | 95.28% | 96.12% | ₹2.29 L | normal |
| BHIM | 97 | 97.94% | 96.07% | ₹96,710 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,473 | 96.20% | ₹28.07 L |
| Food & Beverage | 1,433 | 96.65% | ₹6.70 L |
| Bills | 1,148 | 97.56% | ₹17.00 L |
| Mobility | 674 | 97.18% | ₹3.53 L |
| Healthcare | 337 | 96.14% | ₹2.68 L |
| Digital | 262 | 93.51% | ₹1.10 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,122 | 29.8% | 96.57% | ₹35.48 L |
| North | 2,641 | 25.2% | 95.15% | ₹31.36 L |
| West | 2,546 | 24.3% | 94.82% | ₹28.95 L |
| East | 1,273 | 12.2% | 96.62% | ₹15.47 L |
| Central | 887 | 8.5% | 95.38% | ₹13.97 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 62 | 98.39% | ₹2.97 L |
| Vasant Wardrobe | Key Account | Retail | 70 | 97.14% | ₹1.61 L |
| Vega Electronics | Large | Retail | 27 | 96.30% | ₹1.35 L |
| Rapid Bazaar | Key Account | Retail | 253 | 95.26% | ₹1.33 L |
| Girnar Connect | Key Account | Bills | 196 | 97.96% | ₹99,559 |
| Hampi Stores 2298 | Key Account | Retail | 89 | 92.13% | ₹66,070 |
| Yamuna Restaurant | Key Account | Food & Beverage | 72 | 97.22% | ₹57,436 |
| Aravalli Pharmacy | Large | Healthcare | 69 | 95.65% | ₹48,221 |

## Failure analysis

Of 441 declined attempts, 338 were business declines (3.229% of attempts — balances, PINs and limits), 55 technical (0.525%), 39 timeouts (0.373%) and 9 risk declines (0.086%).

125 attempts were re-presentations of an earlier failure (1.19% of the day); 69.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 153 | 1.461% | 1.506% |
| ZM | Invalid UPI PIN | business | Customer | 100 | 0.955% | 0.962% |
| ZA | Transaction declined by customer | business | Customer | 33 | 0.315% | 0.360% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.315% | 0.204% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.229% | 0.251% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.181% | 0.209% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.143% | 0.104% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.134% | 0.128% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 7 | 1 |
| Auto-reversals | 21 | 8 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹26,925 | ₹4,734 |

## Customer behaviour

8,876 distinct customers transacted (−1.0% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,637 | 2,988 | 1.13 | 95.62% | ₹1,287 |
| power | 1,887 | 2,434 | 1.29 | 96.14% | ₹1,733 |
| merchant_heavy | 1,989 | 2,369 | 1.19 | 95.57% | ₹1,019 |
| small_ticket | 1,396 | 1,649 | 1.18 | 95.94% | ₹566 |
| occasional | 753 | 796 | 1.06 | 95.23% | ₹1,209 |
| new | 190 | 208 | 1.09 | 94.23% | ₹598 |
| dormant_returning | 24 | 25 | 1.04 | 84.00% | ₹991 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

07 January was an unremarkable day, and that is the finding: 10,469 attempts, 95.69% success, ₹1.25 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,469, successes=10,018, failed=441, pending=10, settled_value_inr=12,523,426.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.

Refs: enterprise_data/warehouse/transactions, RPT-D02-DAILY, enterprise_data/warehouse/reference/incidents.parquet
