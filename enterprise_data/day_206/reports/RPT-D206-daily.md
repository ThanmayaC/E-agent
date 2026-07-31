---
id: RPT-D206-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-29T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 29 Jul 2026)

**Report ID:** RPT-D206-DAILY · **Day 206 of 206** · **Derived from:** 15,589 transaction rows queried live from the warehouse

## Summary

The rail took **15,589 payment attempts** on Wednesday 29 July 2026 (Guru Purnima) and settled **₹1.92 Cr** across 15,013 successful payments. Volume was +4.1% on yesterday and +15.4% on the same weekday last week. Success closed at **96.31%**, in line with the trailing 28-day median of 96.17%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,589 | +4.1% | +15.4% | 15,700 |
| Successful payments | 15,013 | +4.3% | +15.6% | 15,090 |
| Success rate | 96.31% | +0.22pp | +0.23pp | 96.13% |
| Settled value | ₹1.92 Cr | −8.1% | −0.9% | ₹2.05 Cr |
| Average ticket | ₹1,279 | −11.8% | −14.3% | ₹1,359 |
| Technical declines | 0.289% | −0.04pp | −0.10pp | 0.436% |
| Business declines | 3.015% | −0.12pp | +0.06pp | 2.869% |
| Risk declines | 0.115% | +0.01pp | −0.02pp | 0.111% |
| Timeout declines | 0.173% | −0.05pp | −0.17pp | 0.358% |
| Retry share | 1.12% | −0.06pp | −0.02pp | 1.28% |
| Latency p95 | 1,245 ms | −1.0% | −3.1% | 1,290 ms |
| Active customers | 12,951 | +4.5% | +13.5% | 12,870 |
| Active merchants | 1,606 | −1.8% | +2.2% | 1,604 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,736 | 30.4% | 95.29% | ₹47.06 L | +5.8% |
| UPI Person to Merchant | 3,658 | 23.5% | 96.01% | ₹34.21 L | −4.2% |
| UPI QR Payments | 2,673 | 17.1% | 97.23% | ₹11.55 L | +8.4% |
| UPI Lite | 2,149 | 13.8% | 98.70% | ₹1.98 L | −2.8% |
| UPI Circle | 770 | 4.9% | 97.92% | ₹7.37 L | −3.1% |
| Credit on UPI | 471 | 3.0% | 97.03% | ₹45.03 L | −8.5% |
| UPI AutoPay | 374 | 2.4% | 91.18% | ₹6.87 L | −1.3% |
| RuPay Credit on UPI | 304 | 2.0% | 96.05% | ₹12.46 L | −18.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,916 | 96.32% | 96.31% | ₹59.53 L | normal |
| HDFC Bank | 1,656 | 96.92% | 96.41% | ₹19.70 L | normal |
| Bank of Baroda | 1,197 | 96.32% | 96.08% | ₹13.02 L | normal |
| Union Bank of India | 1,086 | 96.50% | 96.20% | ₹10.35 L | normal |
| Axis Bank | 1,008 | 95.54% | 96.34% | ₹10.21 L | normal |
| ICICI Bank | 931 | 96.89% | 96.62% | ₹17.81 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,377 | 96.54% | 96.18% | ₹85.39 L | normal |
| Google Pay | 5,063 | 95.93% | 96.33% | ₹65.57 L | normal |
| Paytm | 1,306 | 96.48% | 96.19% | ₹15.47 L | normal |
| Navi | 581 | 96.56% | 96.37% | ₹9.17 L | normal |
| SuperMoney | 328 | 95.73% | 96.48% | ₹2.75 L | normal |
| BHIM | 173 | 95.95% | 95.29% | ₹1.99 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,296 | 96.81% | ₹52.20 L |
| Food & Beverage | 2,647 | 97.09% | ₹12.96 L |
| Bills | 1,323 | 96.98% | ₹11.95 L |
| Mobility | 1,299 | 97.84% | ₹6.65 L |
| Healthcare | 550 | 97.82% | ₹6.99 L |
| Digital | 272 | 93.01% | ₹1.45 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,695 | 30.1% | 95.83% | ₹62.55 L |
| North | 3,979 | 25.5% | 96.46% | ₹46.96 L |
| West | 3,837 | 24.6% | 96.19% | ₹45.80 L |
| East | 1,702 | 10.9% | 96.65% | ₹24.29 L |
| Central | 1,376 | 8.8% | 97.38% | ₹12.41 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 37 | 91.89% | ₹3.04 L |
| Vasant Wardrobe | Key Account | Retail | 86 | 91.86% | ₹2.29 L |
| Rapid Bazaar | Key Account | Retail | 386 | 97.15% | ₹1.47 L |
| Urban Boutique | Key Account | Retail | 127 | 98.43% | ₹1.28 L |
| Ujjwal Water Board | Key Account | Bills | 53 | 98.11% | ₹1.13 L |
| Swift Grill | Large | Food & Beverage | 57 | 96.49% | ₹94,205 |
| Hampi Styles | Key Account | Retail | 40 | 97.50% | ₹92,652 |
| Hampi Stores 2298 | Key Account | Retail | 119 | 99.16% | ₹84,501 |

## Failure analysis

Of 560 declined attempts, 470 were business declines (3.015% of attempts — balances, PINs and limits), 45 technical (0.289%), 27 timeouts (0.173%) and 18 risk declines (0.115%).

174 attempts were re-presentations of an earlier failure (1.12% of the day); 65.5% of them succeeded.

- Decline code UX (Mandate execution outside permitted window) fired 26 times — 0.167% of attempts against a trailing 0.083%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 185 | 1.187% | 1.199% |
| ZM | Invalid UPI PIN | business | Customer | 162 | 1.039% | 0.959% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.340% | 0.326% |
| XH | Account does not exist / frozen | business | Issuer | 37 | 0.237% | 0.197% |
| UX | Mandate execution outside permitted window | business | PSP | 26 | 0.167% | 0.083% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.135% | 0.168% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.103% | 0.094% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.090% | 0.115% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 109 | 114 |
| Auto-reversals | 21 | 23 |
| Disputes / chargebacks | 17 | 15 |
| Value returned | ₹1.76 L | ₹1.85 L |

## Customer behaviour

12,951 distinct customers transacted (+1.1% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,082 | 4,622 | 1.13 | 96.37% | ₹1,351 |
| power | 2,806 | 3,797 | 1.35 | 96.23% | ₹1,745 |
| merchant_heavy | 2,978 | 3,592 | 1.21 | 96.21% | ₹839 |
| small_ticket | 1,932 | 2,375 | 1.23 | 96.42% | ₹590 |
| occasional | 939 | 976 | 1.04 | 96.11% | ₹1,705 |
| new | 190 | 203 | 1.07 | 97.04% | ₹851 |
| dormant_returning | 24 | 24 | 1.00 | 100.00% | ₹3,250 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Decline code UX (Mandate execution outside permitted window) fired 26 times — 0.167% of attempts against a trailing 0.083%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

29 July was an unremarkable day, and that is the finding: 15,589 attempts, 96.31% success, ₹1.92 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-29` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,589, successes=15,013, failed=560, pending=16, settled_value_inr=19,199,707.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=UX; count=26; rate_pct=0.17; trailing_rate_pct=0.08; owner=PSP; z=2.78

Refs: enterprise_data/warehouse/transactions, RPT-D205-DAILY, enterprise_data/warehouse/reference/incidents.parquet
