---
id: RPT-D05-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-09T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 09 Jan 2026)

**Report ID:** RPT-D05-DAILY · **Day 5 of 206** · **Derived from:** 10,390 transaction rows queried live from the warehouse

## Summary

The rail took **10,390 payment attempts** on Friday 09 January 2026 (Working day) and settled **₹1.12 Cr** across 9,940 successful payments. Volume was +1.5% on yesterday and — on the same weekday last week. Success closed at **95.67%**, in line with the trailing 28-day median of 95.58%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,390 | +1.5% | — | 10,442 |
| Successful payments | 9,940 | +1.7% | — | 9,984 |
| Success rate | 95.67% | +0.20pp | — | 95.61% |
| Settled value | ₹1.12 Cr | −6.7% | — | ₹1.24 Cr |
| Average ticket | ₹1,131 | −8.2% | — | ₹1,238 |
| Technical declines | 0.577% | +0.07pp | — | 0.525% |
| Business declines | 3.070% | −0.17pp | — | 3.174% |
| Risk declines | 0.164% | −0.01pp | — | 0.159% |
| Timeout declines | 0.423% | −0.01pp | — | 0.380% |
| Retry share | 1.20% | −0.11pp | — | 1.15% |
| Latency p95 | 1,242 ms | −0.0% | — | 1,256 ms |
| Active customers | 8,775 | +0.5% | — | 8,862 |
| Active merchants | 1,175 | −2.9% | — | 1,209 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,141 | 39.9% | 95.27% | ₹43.22 L | +3.4% |
| UPI Person to Merchant | 2,838 | 27.3% | 96.02% | ₹25.03 L | −5.0% |
| UPI QR Payments | 1,600 | 15.4% | 96.44% | ₹5.96 L | −9.2% |
| UPI Lite | 786 | 7.6% | 98.22% | ₹71,205 | +11.4% |
| UPI AutoPay | 289 | 2.8% | 92.04% | ₹5.56 L | −3.7% |
| RuPay Credit on UPI | 208 | 2.0% | 94.71% | ₹7.37 L | +2.0% |
| Credit on UPI | 128 | 1.2% | 96.09% | ₹9.70 L | −21.0% |
| UPI Circle | 91 | 0.9% | 98.90% | ₹1.07 L | −7.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,332 | 95.35% | 95.44% | ₹35.87 L | normal |
| HDFC Bank | 1,152 | 95.92% | 96.17% | ₹13.48 L | normal |
| Bank of Baroda | 774 | 95.99% | 95.10% | ₹9.06 L | normal |
| Union Bank of India | 676 | 96.15% | 95.09% | ₹6.73 L | normal |
| Punjab National Bank | 666 | 95.65% | 95.50% | ₹6.64 L | normal |
| ICICI Bank | 645 | 96.43% | 95.64% | ₹7.66 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,803 | 95.71% | 95.58% | ₹48.91 L | normal |
| Google Pay | 3,461 | 96.13% | 95.58% | ₹39.77 L | normal |
| Paytm | 887 | 94.59% | 96.31% | ₹8.75 L | normal |
| Navi | 374 | 93.05% | 95.95% | ₹4.51 L | normal |
| SuperMoney | 233 | 96.14% | 95.52% | ₹3.76 L | normal |
| BHIM | 109 | 94.50% | 96.07% | ₹1.50 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,631 | 96.09% | ₹26.69 L |
| Food & Beverage | 1,504 | 97.34% | ₹8.52 L |
| Mobility | 662 | 97.43% | ₹3.40 L |
| Bills | 632 | 94.46% | ₹6.77 L |
| Healthcare | 341 | 93.55% | ₹2.65 L |
| Digital | 196 | 93.37% | ₹1.28 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,123 | 30.1% | 95.55% | ₹33.58 L |
| North | 2,659 | 25.6% | 95.60% | ₹29.03 L |
| West | 2,473 | 23.8% | 95.55% | ₹26.99 L |
| East | 1,190 | 11.5% | 96.13% | ₹13.08 L |
| Central | 945 | 9.1% | 95.98% | ₹9.75 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 29 | 96.55% | ₹1.70 L |
| Vasant Wardrobe | Key Account | Retail | 69 | 95.65% | ₹1.65 L |
| Tejas Restaurant | Large | Food & Beverage | 28 | 96.43% | ₹1.10 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 96.77% | ₹84,316 |
| Rapid Bazaar | Key Account | Retail | 251 | 96.81% | ₹70,906 |
| Hampi Stores 2298 | Key Account | Retail | 102 | 96.08% | ₹69,752 |
| Urban Boutique | Key Account | Retail | 85 | 97.65% | ₹65,762 |
| Ujjwal Water Board | Key Account | Bills | 37 | 89.19% | ₹55,830 |

## Failure analysis

Of 440 declined attempts, 319 were business declines (3.070% of attempts — balances, PINs and limits), 60 technical (0.577%), 44 timeouts (0.423%) and 17 risk declines (0.164%).

125 attempts were re-presentations of an earlier failure (1.20% of the day); 65.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 134 | 1.290% | 1.435% |
| ZM | Invalid UPI PIN | business | Customer | 113 | 1.088% | 1.025% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.346% | 0.355% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.260% | 0.242% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.202% | 0.222% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.183% | 0.215% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.173% | 0.125% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.164% | 0.111% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 19 | 4 |
| Auto-reversals | 19 | 15 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹26,765 | ₹16,135 |

## Customer behaviour

8,775 distinct customers transacted (−1.4% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,664 | 3,019 | 1.13 | 95.96% | ₹1,218 |
| power | 1,881 | 2,437 | 1.30 | 95.08% | ₹1,419 |
| merchant_heavy | 1,995 | 2,353 | 1.18 | 96.26% | ₹893 |
| small_ticket | 1,313 | 1,606 | 1.22 | 95.58% | ₹543 |
| occasional | 716 | 755 | 1.05 | 94.97% | ₹1,199 |
| new | 179 | 193 | 1.08 | 94.30% | ₹1,118 |
| dormant_returning | 27 | 27 | 1.00 | 100.00% | ₹489 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

09 January was an unremarkable day, and that is the finding: 10,390 attempts, 95.67% success, ₹1.12 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-09` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,390, successes=9,940, failed=440, pending=10, settled_value_inr=11,242,896.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.

Refs: enterprise_data/warehouse/transactions, RPT-D04-DAILY, enterprise_data/warehouse/reference/incidents.parquet
