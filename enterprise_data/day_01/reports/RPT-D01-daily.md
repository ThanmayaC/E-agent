---
id: RPT-D01-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 05 Jan 2026)

**Report ID:** RPT-D01-DAILY · **Day 1 of 206** · **Derived from:** 10,611 transaction rows queried live from the warehouse

## Summary

The rail took **10,611 payment attempts** on Monday 05 January 2026 (Working day) and settled **₹1.40 Cr** across 10,163 successful payments. Volume was — on yesterday and — on the same weekday last week. Success closed at **95.78%**, in line with the trailing 28-day median of 95.78%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,611 | — | — | 10,611 |
| Successful payments | 10,163 | — | — | 10,163 |
| Success rate | 95.78% | — | — | 95.78% |
| Settled value | ₹1.40 Cr | — | — | ₹1.40 Cr |
| Average ticket | ₹1,374 | — | — | ₹1,374 |
| Technical declines | 0.471% | — | — | 0.471% |
| Business declines | 3.072% | — | — | 3.072% |
| Risk declines | 0.179% | — | — | 0.179% |
| Timeout declines | 0.283% | — | — | 0.283% |
| Retry share | 0.63% | — | — | 0.63% |
| Latency p95 | 1,272 ms | — | — | 1,272 ms |
| Active customers | 9,000 | — | — | 9,000 |
| Active merchants | 1,227 | — | — | 1,227 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,987 | 37.6% | 95.21% | ₹43.82 L | — |
| UPI Person to Merchant | 3,130 | 29.5% | 96.26% | ₹33.93 L | — |
| UPI QR Payments | 1,744 | 16.4% | 96.62% | ₹7.70 L | — |
| UPI Lite | 696 | 6.6% | 99.28% | ₹66,511 | — |
| UPI AutoPay | 294 | 2.8% | 91.16% | ₹5.09 L | — |
| RuPay Credit on UPI | 183 | 1.7% | 96.17% | ₹11.18 L | — |
| Credit on UPI | 168 | 1.6% | 94.64% | ₹17.21 L | — |
| UPI Circle | 100 | 0.9% | 96.00% | ₹56,401 | — |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,395 | 95.67% | — | ₹45.77 L | normal |
| HDFC Bank | 1,177 | 96.18% | — | ₹13.40 L | normal |
| Bank of Baroda | 831 | 94.46% | — | ₹10.86 L | normal |
| Union Bank of India | 744 | 95.16% | — | ₹10.40 L | normal |
| Axis Bank | 674 | 96.44% | — | ₹11.92 L | normal |
| ICICI Bank | 629 | 95.07% | — | ₹9.08 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,003 | 95.62% | — | ₹63.38 L | normal |
| Google Pay | 3,545 | 95.77% | — | ₹50.83 L | normal |
| Paytm | 833 | 95.92% | — | ₹10.43 L | normal |
| Navi | 350 | 96.29% | — | ₹4.32 L | normal |
| SuperMoney | 228 | 96.49% | — | ₹4.83 L | normal |
| BHIM | 111 | 95.50% | — | ₹1.06 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,446 | 96.52% | ₹29.43 L |
| Food & Beverage | 1,493 | 96.92% | ₹6.57 L |
| Bills | 1,141 | 96.06% | ₹14.55 L |
| Mobility | 669 | 96.41% | ₹4.07 L |
| Healthcare | 319 | 97.81% | ₹5.40 L |
| Digital | 255 | 93.73% | ₹1.37 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,219 | 30.3% | 95.71% | ₹43.36 L |
| North | 2,622 | 24.7% | 96.07% | ₹39.22 L |
| West | 2,515 | 23.7% | 96.06% | ₹31.13 L |
| East | 1,304 | 12.3% | 95.32% | ₹16.64 L |
| Central | 951 | 9.0% | 95.06% | ₹9.34 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 66 | 95.45% | ₹1.79 L |
| Vasant Wardrobe | Key Account | Retail | 62 | 96.77% | ₹1.32 L |
| Rapid Bazaar | Key Account | Retail | 255 | 96.86% | ₹1.01 L |
| Vega Electronics | Large | Retail | 26 | 100.00% | ₹95,051 |
| Hampi Stores 2298 | Key Account | Retail | 82 | 97.56% | ₹90,047 |
| Girnar Connect | Key Account | Bills | 195 | 96.41% | ₹77,752 |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 100.00% | ₹71,128 |
| Urban Boutique | Key Account | Retail | 75 | 93.33% | ₹35,324 |

## Failure analysis

Of 425 declined attempts, 326 were business declines (3.072% of attempts — balances, PINs and limits), 50 technical (0.471%), 30 timeouts (0.283%) and 19 risk declines (0.179%).

67 attempts were re-presentations of an earlier failure (0.63% of the day); 70.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 170 | 1.602% | — |
| ZM | Invalid UPI PIN | business | Customer | 88 | 0.829% | — |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.349% | — |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.273% | — |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.198% | — |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.170% | — |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.170% | — |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 11 | 0.104% | — |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 0 | — |
| Auto-reversals | 7 | — |
| Disputes / chargebacks | 0 | — |
| Value returned | ₹4,124 | — |

## Customer behaviour

9,000 distinct customers transacted (— on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,724 | 3,074 | 1.13 | 95.84% | ₹1,505 |
| power | 1,904 | 2,511 | 1.32 | 96.26% | ₹1,710 |
| merchant_heavy | 1,998 | 2,342 | 1.17 | 95.22% | ₹971 |
| small_ticket | 1,375 | 1,645 | 1.20 | 95.93% | ₹567 |
| occasional | 769 | 797 | 1.04 | 95.23% | ₹2,041 |
| new | 198 | 210 | 1.06 | 96.19% | ₹917 |
| dormant_returning | 32 | 32 | 1.00 | 96.88% | ₹662 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

05 January was an unremarkable day, and that is the finding: 10,611 attempts, 95.78% success, ₹1.40 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,611, successes=10,163, failed=425, pending=23, settled_value_inr=13,967,987.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.

Refs: enterprise_data/warehouse/transactions, RPT-D01-DAILY, enterprise_data/warehouse/reference/incidents.parquet
