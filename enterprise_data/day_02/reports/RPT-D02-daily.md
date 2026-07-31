---
id: RPT-D02-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-06T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 06 Jan 2026)

**Report ID:** RPT-D02-DAILY · **Day 2 of 206** · **Derived from:** 10,501 transaction rows queried live from the warehouse

## Summary

The rail took **10,501 payment attempts** on Tuesday 06 January 2026 (Working day) and settled **₹1.20 Cr** across 10,024 successful payments. Volume was −1.0% on yesterday and — on the same weekday last week. Success closed at **95.46%**, below the trailing 28-day median of 95.78%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,501 | −1.0% | — | 10,556 |
| Successful payments | 10,024 | −1.4% | — | 10,094 |
| Success rate | 95.46% | −0.32pp | — | 95.62% |
| Settled value | ₹1.20 Cr | −13.8% | — | ₹1.30 Cr |
| Average ticket | ₹1,202 | −12.6% | — | ₹1,288 |
| Technical declines | 0.543% | +0.07pp | — | 0.507% |
| Business declines | 3.257% | +0.18pp | — | 3.165% |
| Risk declines | 0.190% | +0.01pp | — | 0.185% |
| Timeout declines | 0.390% | +0.11pp | — | 0.337% |
| Retry share | 1.39% | +0.76pp | — | 1.01% |
| Latency p95 | 1,255 ms | −1.3% | — | 1,263 ms |
| Active customers | 8,927 | −0.8% | — | 8,964 |
| Active merchants | 1,219 | −0.7% | — | 1,223 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,021 | 38.3% | 94.90% | ₹41.54 L | +0.9% |
| UPI Person to Merchant | 2,864 | 27.3% | 95.74% | ₹27.26 L | −8.5% |
| UPI QR Payments | 1,781 | 17.0% | 96.24% | ₹7.69 L | +2.1% |
| UPI Lite | 724 | 6.9% | 98.48% | ₹65,133 | +4.0% |
| UPI AutoPay | 321 | 3.1% | 92.21% | ₹5.20 L | +9.2% |
| RuPay Credit on UPI | 195 | 1.9% | 92.31% | ₹12.14 L | +6.6% |
| Credit on UPI | 156 | 1.5% | 98.08% | ₹10.43 L | −7.1% |
| UPI Circle | 122 | 1.2% | 94.26% | ₹1.09 L | +22.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,400 | 95.12% | 95.67% | ₹39.18 L | normal |
| HDFC Bank | 1,153 | 95.06% | 96.18% | ₹13.69 L | normal |
| Bank of Baroda | 752 | 95.74% | 94.46% | ₹9.06 L | normal |
| Union Bank of India | 742 | 96.50% | 95.16% | ₹10.49 L | normal |
| ICICI Bank | 642 | 96.11% | 95.07% | ₹7.41 L | normal |
| Punjab National Bank | 629 | 96.18% | 94.33% | ₹8.24 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,964 | 95.47% | 95.62% | ₹60.41 L | normal |
| Google Pay | 3,474 | 95.60% | 95.77% | ₹39.27 L | normal |
| Paytm | 843 | 94.54% | 95.92% | ₹8.04 L | normal |
| Navi | 365 | 95.89% | 96.29% | ₹3.62 L | normal |
| SuperMoney | 212 | 95.75% | 96.49% | ₹2.58 L | normal |
| BHIM | 119 | 96.64% | 95.50% | ₹93,455 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,347 | 95.82% | ₹28.33 L |
| Food & Beverage | 1,398 | 95.57% | ₹6.56 L |
| Bills | 1,169 | 96.24% | ₹12.43 L |
| Mobility | 679 | 97.35% | ₹4.13 L |
| Healthcare | 302 | 96.36% | ₹1.98 L |
| Digital | 291 | 96.91% | ₹1.33 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,141 | 29.9% | 95.29% | ₹36.75 L |
| North | 2,639 | 25.1% | 95.04% | ₹28.37 L |
| West | 2,506 | 23.9% | 95.77% | ₹30.63 L |
| East | 1,296 | 12.3% | 95.60% | ₹15.08 L |
| Central | 919 | 8.8% | 96.19% | ₹9.62 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 69 | 91.30% | ₹1.53 L |
| Vega Electronics | Large | Retail | 24 | 91.67% | ₹1.23 L |
| Girnar Connect | Key Account | Bills | 219 | 98.17% | ₹95,691 |
| Rapid Bazaar | Key Account | Retail | 249 | 95.18% | ₹90,038 |
| Vasant Wardrobe | Key Account | Retail | 54 | 96.30% | ₹88,437 |
| Yamuna Restaurant | Key Account | Food & Beverage | 53 | 100.00% | ₹58,496 |
| Hampi Stores 2298 | Key Account | Retail | 71 | 98.59% | ₹51,433 |
| Aravalli Pharmacy | Large | Healthcare | 51 | 98.04% | ₹40,581 |

## Failure analysis

Of 460 declined attempts, 342 were business declines (3.257% of attempts — balances, PINs and limits), 57 technical (0.543%), 41 timeouts (0.390%) and 20 risk declines (0.190%).

146 attempts were re-presentations of an earlier failure (1.39% of the day); 73.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 148 | 1.409% | 1.602% |
| ZM | Invalid UPI PIN | business | Customer | 115 | 1.095% | 0.829% |
| ZA | Transaction declined by customer | business | Customer | 39 | 0.371% | 0.349% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.248% | 0.170% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.229% | 0.273% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.210% | 0.198% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.190% | 0.170% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.152% | 0.104% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 2 | 0 |
| Auto-reversals | 9 | 7 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹5,345 | ₹4,124 |

## Customer behaviour

8,927 distinct customers transacted (−0.8% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,731 | 3,064 | 1.12 | 95.10% | ₹1,261 |
| power | 1,861 | 2,455 | 1.32 | 94.62% | ₹1,490 |
| merchant_heavy | 2,063 | 2,413 | 1.17 | 96.10% | ₹1,053 |
| small_ticket | 1,345 | 1,603 | 1.19 | 96.51% | ₹516 |
| occasional | 734 | 767 | 1.04 | 94.92% | ₹1,270 |
| new | 167 | 173 | 1.04 | 97.11% | ₹906 |
| dormant_returning | 26 | 26 | 1.00 | 96.15% | ₹1,056 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

06 January was an unremarkable day, and that is the finding: 10,501 attempts, 95.46% success, ₹1.20 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-06` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,501, successes=10,024, failed=460, pending=17, settled_value_inr=12,045,229.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.

Refs: enterprise_data/warehouse/transactions, RPT-D01-DAILY, enterprise_data/warehouse/reference/incidents.parquet
