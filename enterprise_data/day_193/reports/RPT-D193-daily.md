---
id: RPT-D193-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 16 Jul 2026)

**Report ID:** RPT-D193-DAILY · **Day 193 of 206** · **Derived from:** 14,591 transaction rows queried live from the warehouse

## Summary

The rail took **14,591 payment attempts** on Thursday 16 July 2026 (Working day) and settled **₹2.00 Cr** across 14,014 successful payments. Volume was −2.0% on yesterday and −4.1% on the same weekday last week. Success closed at **96.05%**, in line with the trailing 28-day median of 96.18%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,591 | −2.0% | −4.1% | 16,441 |
| Successful payments | 14,014 | −2.5% | −4.5% | 15,797 |
| Success rate | 96.05% | −0.48pp | −0.43pp | 96.12% |
| Settled value | ₹2.00 Cr | −8.0% | +6.1% | ₹2.13 Cr |
| Average ticket | ₹1,426 | −5.7% | +11.1% | ₹1,350 |
| Technical declines | 0.322% | −0.01pp | −0.07pp | 0.463% |
| Business declines | 3.180% | +0.37pp | +0.50pp | 2.799% |
| Risk declines | 0.117% | +0.04pp | +0.02pp | 0.106% |
| Timeout declines | 0.240% | +0.10pp | −0.03pp | 0.425% |
| Retry share | 1.01% | +0.01pp | +0.02pp | 1.36% |
| Latency p95 | 1,314 ms | +1.0% | +3.4% | 1,305 ms |
| Active customers | 12,215 | −1.1% | −2.7% | 13,339 |
| Active merchants | 1,584 | +0.9% | +0.3% | 1,617 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,508 | 30.9% | 95.01% | ₹46.04 L | −2.0% |
| UPI Person to Merchant | 3,318 | 22.7% | 96.26% | ₹28.05 L | −8.3% |
| UPI Lite | 2,144 | 14.7% | 99.49% | ₹1.99 L | −16.4% |
| UPI QR Payments | 2,089 | 14.3% | 96.46% | ₹9.44 L | −19.1% |
| UPI Circle | 712 | 4.9% | 97.33% | ₹5.98 L | −11.8% |
| Credit on UPI | 578 | 4.0% | 95.16% | ₹55.80 L | +20.7% |
| UPI AutoPay | 397 | 2.7% | 88.92% | ₹7.36 L | +5.2% |
| RuPay Credit on UPI | 344 | 2.4% | 93.60% | ₹16.71 L | −10.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,569 | 95.67% | 96.19% | ₹58.77 L | normal |
| HDFC Bank | 1,604 | 95.82% | 96.44% | ₹24.47 L | normal |
| Bank of Baroda | 1,136 | 96.92% | 96.25% | ₹16.30 L | normal |
| Union Bank of India | 1,010 | 96.14% | 96.18% | ₹11.74 L | normal |
| Axis Bank | 965 | 97.20% | 96.17% | ₹16.66 L | normal |
| ICICI Bank | 880 | 97.16% | 96.34% | ₹13.68 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,831 | 96.21% | 96.20% | ₹97.93 L | normal |
| Google Pay | 4,848 | 95.90% | 96.13% | ₹61.89 L | normal |
| Paytm | 1,239 | 96.05% | 96.29% | ₹18.79 L | normal |
| Navi | 524 | 95.99% | 96.52% | ₹4.48 L | normal |
| SuperMoney | 305 | 96.72% | 96.19% | ₹2.73 L | normal |
| BHIM | 138 | 94.93% | 95.93% | ₹81,872 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,195 | 96.52% | ₹52.48 L |
| Food & Beverage | 2,515 | 97.50% | ₹12.70 L |
| Mobility | 1,170 | 98.38% | ₹7.06 L |
| Bills | 925 | 94.92% | ₹9.02 L |
| Healthcare | 579 | 98.10% | ₹14.78 L |
| Digital | 203 | 93.60% | ₹1.02 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,365 | 29.9% | 96.15% | ₹68.25 L |
| North | 3,721 | 25.5% | 96.29% | ₹43.92 L |
| West | 3,565 | 24.4% | 95.90% | ₹54.40 L |
| East | 1,682 | 11.5% | 95.48% | ₹21.98 L |
| Central | 1,258 | 8.6% | 96.10% | ₹11.34 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 87.88% | ₹2.54 L |
| Vasant Wardrobe | Key Account | Retail | 86 | 96.51% | ₹2.43 L |
| Hampi Styles | Key Account | Retail | 35 | 100.00% | ₹1.42 L |
| Rapid Bazaar | Key Account | Retail | 416 | 97.12% | ₹1.35 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 95.16% | ₹94,534 |
| Hampi Stores 2298 | Key Account | Retail | 119 | 94.96% | ₹88,567 |
| Girnar Connect | Key Account | Bills | 149 | 97.32% | ₹65,526 |
| Urban Boutique | Key Account | Retail | 96 | 98.96% | ₹64,763 |

## Failure analysis

Of 563 declined attempts, 464 were business declines (3.180% of attempts — balances, PINs and limits), 47 technical (0.322%), 35 timeouts (0.240%) and 17 risk declines (0.117%).

147 attempts were re-presentations of an earlier failure (1.01% of the day); 61.9% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 63 times — 0.432% of attempts against a trailing 0.323%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 183 | 1.254% | 1.209% |
| ZM | Invalid UPI PIN | business | Customer | 161 | 1.103% | 0.951% |
| ZA | Transaction declined by customer | business | Customer | 63 | 0.432% | 0.323% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.164% | 0.187% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.137% | 0.131% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.123% | 0.175% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.117% | 0.121% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.110% | 0.083% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 138 | 112 |
| Auto-reversals | 15 | 24 |
| Disputes / chargebacks | 17 | 15 |
| Value returned | ₹2.13 L | ₹1.72 L |

## Customer behaviour

12,215 distinct customers transacted (−6.8% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,754 | 4,284 | 1.14 | 95.99% | ₹1,514 |
| power | 2,680 | 3,556 | 1.33 | 95.64% | ₹1,794 |
| merchant_heavy | 2,797 | 3,302 | 1.18 | 96.09% | ₹1,211 |
| small_ticket | 1,810 | 2,207 | 1.22 | 96.87% | ₹624 |
| occasional | 946 | 994 | 1.05 | 95.37% | ₹1,566 |
| new | 202 | 220 | 1.09 | 97.73% | ₹768 |
| dormant_returning | 26 | 28 | 1.08 | 96.43% | ₹792 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 63 times — 0.432% of attempts against a trailing 0.323%. Owner: Customer.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

16 July ran on trend at 96.05% success and ₹2.00 Cr settled. The movement worth carrying forward is in the decline profile: decline code ZA (Transaction declined by customer) fired 63 times — 0.432% of attempts against a trailing 0.323%. Owner: Customer. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,591, successes=14,014, failed=563, pending=14, settled_value_inr=19,988,541.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZA; count=63; rate_pct=0.43; trailing_rate_pct=0.32; owner=Customer; z=2.18

Refs: enterprise_data/warehouse/transactions, RPT-D192-DAILY, enterprise_data/warehouse/reference/incidents.parquet
