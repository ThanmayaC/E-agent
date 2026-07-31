---
id: RPT-D191-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 14 Jul 2026)

**Report ID:** RPT-D191-DAILY · **Day 191 of 206** · **Derived from:** 15,783 transaction rows queried live from the warehouse

## Summary

The rail took **15,783 payment attempts** on Tuesday 14 July 2026 (Working day) and settled **₹2.37 Cr** across 15,173 successful payments. Volume was +8.5% on yesterday and −4.3% on the same weekday last week. Success closed at **96.14%**, in line with the trailing 28-day median of 96.11%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,783 | +8.5% | −4.3% | 16,684 |
| Successful payments | 15,173 | +8.3% | −4.8% | 16,027 |
| Success rate | 96.14% | −0.13pp | −0.52pp | 96.10% |
| Settled value | ₹2.37 Cr | +15.0% | +2.0% | ₹2.14 Cr |
| Average ticket | ₹1,560 | +6.2% | +7.2% | ₹1,333 |
| Technical declines | 0.386% | −0.10pp | −0.01pp | 0.483% |
| Business declines | 3.060% | +0.26pp | +0.56pp | 2.771% |
| Risk declines | 0.082% | −0.02pp | +0.01pp | 0.107% |
| Timeout declines | 0.272% | +0.00pp | −0.00pp | 0.458% |
| Retry share | 1.12% | −0.02pp | +0.23pp | 1.42% |
| Latency p95 | 1,299 ms | +0.1% | −0.9% | 1,304 ms |
| Active customers | 12,985 | +7.6% | −3.0% | 13,490 |
| Active merchants | 1,567 | −1.1% | −5.5% | 1,622 |

## What moved

- Product UPI Person to Person ran at 95.82% success on 5,843 attempts (37.0% of the day), 0.68pp up its own 28-day median.
- Product UPI Person to Person carried 5,843 attempts, 31% up its trailing median and 37.0% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,843 | 37.0% | 95.82% | ₹62.63 L | +31.1% |
| UPI Person to Merchant | 3,492 | 22.1% | 96.36% | ₹33.56 L | −3.5% |
| UPI Lite | 1,916 | 12.1% | 98.90% | ₹1.70 L | −25.3% |
| UPI QR Payments | 1,884 | 11.9% | 96.50% | ₹8.08 L | −27.0% |
| UPI Circle | 686 | 4.3% | 97.08% | ₹5.29 L | −15.0% |
| Credit on UPI | 658 | 4.2% | 94.38% | ₹60.38 L | +38.7% |
| RuPay Credit on UPI | 400 | 2.5% | 94.25% | ₹21.18 L | +7.8% |
| UPI AutoPay | 371 | 2.4% | 87.87% | ₹6.20 L | −1.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,115 | 96.48% | 96.18% | ₹75.03 L | normal |
| HDFC Bank | 1,730 | 96.71% | 96.37% | ₹27.78 L | normal |
| Bank of Baroda | 1,245 | 95.42% | 96.22% | ₹20.56 L | normal |
| Union Bank of India | 1,034 | 96.13% | 96.13% | ₹11.96 L | normal |
| Axis Bank | 970 | 95.57% | 96.17% | ₹15.51 L | normal |
| Punjab National Bank | 893 | 95.07% | 95.88% | ₹11.25 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,469 | 96.00% | 96.15% | ₹1.17 Cr | normal |
| Google Pay | 5,124 | 96.25% | 96.13% | ₹75.71 L | normal |
| Paytm | 1,344 | 95.83% | 96.24% | ₹19.13 L | normal |
| Navi | 568 | 96.65% | 96.33% | ₹9.02 L | normal |
| SuperMoney | 287 | 96.86% | 96.12% | ₹2.76 L | normal |
| BHIM | 149 | 95.97% | 95.87% | ₹1.32 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,315 | 96.52% | ₹65.79 L |
| Food & Beverage | 2,428 | 97.08% | ₹10.58 L |
| Mobility | 1,082 | 97.41% | ₹6.07 L |
| Bills | 906 | 95.03% | ₹9.39 L |
| Healthcare | 508 | 97.64% | ₹12.98 L |
| Digital | 227 | 96.92% | ₹1.29 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,626 | 29.3% | 96.43% | ₹79.68 L |
| North | 4,034 | 25.6% | 96.26% | ₹51.58 L |
| West | 3,954 | 25.1% | 95.42% | ₹58.05 L |
| East | 1,814 | 11.5% | 96.31% | ₹28.08 L |
| Central | 1,355 | 8.6% | 96.61% | ₹19.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 83 | 96.39% | ₹2.66 L |
| Vega Electronics | Large | Retail | 34 | 97.06% | ₹1.90 L |
| Rapid Bazaar | Key Account | Retail | 384 | 95.57% | ₹1.44 L |
| Hampi Styles | Key Account | Retail | 58 | 98.28% | ₹1.39 L |
| Hampi Stores 2298 | Key Account | Retail | 115 | 93.04% | ₹94,566 |
| Girnar Connect | Key Account | Bills | 162 | 96.91% | ₹82,607 |
| Ujjwal Water Board | Key Account | Bills | 35 | 94.29% | ₹72,836 |
| Urban Boutique | Key Account | Retail | 116 | 95.69% | ₹72,472 |

## Failure analysis

Of 600 declined attempts, 483 were business declines (3.060% of attempts — balances, PINs and limits), 61 technical (0.386%), 43 timeouts (0.272%) and 13 risk declines (0.082%).

177 attempts were re-presentations of an earlier failure (1.12% of the day); 65.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 199 | 1.261% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 175 | 1.109% | 0.956% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.323% | 0.323% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.184% | 0.190% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.158% | 0.130% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.152% | 0.176% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.114% | 0.121% |
| ZX | Mandate not found or revoked | business | PSP | 16 | 0.101% | 0.080% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 132 | 110 |
| Auto-reversals | 18 | 24 |
| Disputes / chargebacks | 13 | 14 |
| Value returned | ₹2.40 L | ₹1.71 L |

## Customer behaviour

12,985 distinct customers transacted (−0.9% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,081 | 4,723 | 1.16 | 96.23% | ₹1,601 |
| power | 2,796 | 3,807 | 1.36 | 96.01% | ₹2,092 |
| merchant_heavy | 2,971 | 3,598 | 1.21 | 96.00% | ₹1,131 |
| small_ticket | 1,917 | 2,379 | 1.24 | 96.26% | ₹814 |
| occasional | 1,006 | 1,047 | 1.04 | 96.28% | ₹1,809 |
| new | 187 | 201 | 1.07 | 96.52% | ₹848 |
| dormant_returning | 27 | 28 | 1.04 | 96.43% | ₹2,464 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Issuer Indian Bank ran at 94.63% success on 503 attempts (3.2% of the day), 1.51pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

14 July ran on trend at 96.14% success and ₹2.37 Cr settled. The movement worth carrying forward is in the product mix: product UPI Person to Person ran at 95.82% success on 5,843 attempts (37.0% of the day), 0.68pp up its own 28-day median. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,783, successes=15,173, failed=600, pending=10, settled_value_inr=23,667,237.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Person to Person; attempts=5,843; success_rate=95.82; own_median=95.14; z=2.15
- products: product_name=UPI Person to Person; attempts=5,843; own_median=4,458.5; z=2.48
- banks: payer_bank=Indian Bank; attempts=503; success_rate=94.63; own_median=96.15; z=-2.04

Refs: enterprise_data/warehouse/transactions, RPT-D190-DAILY, enterprise_data/warehouse/reference/incidents.parquet
