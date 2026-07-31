---
id: RPT-D205-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 28 Jul 2026)

**Report ID:** RPT-D205-DAILY · **Day 205 of 206** · **Derived from:** 14,982 transaction rows queried live from the warehouse

## Summary

The rail took **14,982 payment attempts** on Tuesday 28 July 2026 (Working day) and settled **₹2.09 Cr** across 14,396 successful payments. Volume was +1.3% on yesterday and +10.9% on the same weekday last week. Success closed at **96.09%**, in line with the trailing 28-day median of 96.17%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,982 | +1.3% | +10.9% | 15,704 |
| Successful payments | 14,396 | +1.2% | +10.8% | 15,092 |
| Success rate | 96.09% | −0.13pp | −0.12pp | 96.13% |
| Settled value | ₹2.09 Cr | +7.2% | +8.5% | ₹2.05 Cr |
| Average ticket | ₹1,450 | +5.9% | −2.1% | ₹1,362 |
| Technical declines | 0.327% | −0.06pp | −0.09pp | 0.441% |
| Business declines | 3.137% | +0.22pp | +0.29pp | 2.864% |
| Risk declines | 0.107% | −0.03pp | −0.04pp | 0.110% |
| Timeout declines | 0.220% | −0.04pp | −0.05pp | 0.364% |
| Retry share | 1.17% | −0.18pp | +0.01pp | 1.28% |
| Latency p95 | 1,257 ms | −2.1% | −4.5% | 1,292 ms |
| Active customers | 12,398 | +1.0% | +8.7% | 12,868 |
| Active merchants | 1,635 | +0.6% | +5.7% | 1,604 |

## What moved

- Category Bills carried 1,516 attempts, 55% up its trailing median and 14.2% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,309 | 28.8% | 95.36% | ₹45.08 L | −4.2% |
| UPI Person to Merchant | 3,826 | 25.5% | 95.97% | ₹35.13 L | +0.6% |
| UPI QR Payments | 2,205 | 14.7% | 96.69% | ₹10.21 L | −12.5% |
| UPI Lite | 2,141 | 14.3% | 99.21% | ₹1.89 L | −4.1% |
| UPI Circle | 722 | 4.8% | 97.09% | ₹7.15 L | −9.8% |
| Credit on UPI | 516 | 3.4% | 95.16% | ₹43.41 L | −1.0% |
| UPI AutoPay | 391 | 2.6% | 87.98% | ₹7.18 L | +3.2% |
| RuPay Credit on UPI | 373 | 2.5% | 97.59% | ₹23.63 L | −0.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,796 | 96.39% | 96.28% | ₹69.90 L | normal |
| HDFC Bank | 1,599 | 97.00% | 96.40% | ₹24.78 L | normal |
| Bank of Baroda | 1,158 | 94.91% | 96.38% | ₹12.65 L | normal |
| Union Bank of India | 1,045 | 96.27% | 96.16% | ₹15.24 L | normal |
| Punjab National Bank | 937 | 96.37% | 95.90% | ₹11.31 L | normal |
| Axis Bank | 905 | 94.70% | 96.34% | ₹15.65 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,086 | 95.99% | 96.19% | ₹98.33 L | normal |
| Google Pay | 4,958 | 96.15% | 96.33% | ₹69.74 L | normal |
| Paytm | 1,197 | 96.07% | 96.19% | ₹15.33 L | normal |
| Navi | 575 | 96.35% | 96.51% | ₹7.53 L | normal |
| SuperMoney | 287 | 95.12% | 96.48% | ₹3.99 L | normal |
| BHIM | 155 | 94.19% | 95.76% | ₹3.46 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,084 | 96.43% | ₹51.13 L |
| Food & Beverage | 2,480 | 96.94% | ₹10.31 L |
| Bills | 1,516 | 96.17% | ₹14.34 L |
| Mobility | 1,259 | 98.17% | ₹7.45 L |
| Healthcare | 523 | 97.13% | ₹10.31 L |
| Digital | 278 | 92.81% | ₹1.91 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,498 | 30.0% | 96.02% | ₹56.74 L |
| North | 3,789 | 25.3% | 96.01% | ₹52.61 L |
| West | 3,686 | 24.6% | 96.31% | ₹59.34 L |
| East | 1,704 | 11.4% | 95.77% | ₹21.43 L |
| Central | 1,305 | 8.7% | 96.32% | ₹18.69 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 36 | 88.89% | ₹5.32 L |
| Vasant Wardrobe | Key Account | Retail | 80 | 96.25% | ₹2.41 L |
| Ujjwal Water Board | Key Account | Bills | 48 | 97.92% | ₹2.18 L |
| Hampi Stores 2298 | Key Account | Retail | 89 | 97.75% | ₹1.32 L |
| Girnar Connect | Key Account | Bills | 287 | 95.82% | ₹1.20 L |
| Rapid Bazaar | Key Account | Retail | 364 | 98.08% | ₹1.16 L |
| Hampi Styles | Key Account | Retail | 48 | 93.75% | ₹1.01 L |
| Swift Mart 1738 | Key Account | Retail | 132 | 97.73% | ₹86,145 |

## Failure analysis

Of 568 declined attempts, 470 were business declines (3.137% of attempts — balances, PINs and limits), 49 technical (0.327%), 33 timeouts (0.220%) and 16 risk declines (0.107%).

176 attempts were re-presentations of an earlier failure (1.17% of the day); 62.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 192 | 1.282% | 1.199% |
| ZM | Invalid UPI PIN | business | Customer | 165 | 1.101% | 0.959% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.354% | 0.325% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.227% | 0.192% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.127% | 0.171% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.113% | 0.117% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 15 | 0.100% | 0.135% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.093% | 0.088% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 116 | 114 |
| Auto-reversals | 14 | 23 |
| Disputes / chargebacks | 15 | 15 |
| Value returned | ₹2.38 L | ₹1.68 L |

## Customer behaviour

12,398 distinct customers transacted (−3.9% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,788 | 4,328 | 1.14 | 96.05% | ₹1,499 |
| power | 2,661 | 3,641 | 1.37 | 95.94% | ₹2,131 |
| merchant_heavy | 2,965 | 3,553 | 1.20 | 96.23% | ₹978 |
| small_ticket | 1,859 | 2,270 | 1.22 | 96.21% | ₹580 |
| occasional | 918 | 966 | 1.05 | 95.55% | ₹1,640 |
| new | 191 | 208 | 1.09 | 98.08% | ₹779 |
| dormant_returning | 16 | 16 | 1.00 | 100.00% | ₹5,847 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Issuer Axis Bank ran at 94.70% success on 905 attempts (6.0% of the day), 1.64pp down its own 28-day median.
- Issuer IDFC First Bank ran at 94.03% success on 352 attempts (2.3% of the day), 2.54pp down its own 28-day median.
- Product UPI Lite Auto Top-Up ran at 91.13% success on 124 attempts (0.8% of the day), 5.61pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

28 July was an unremarkable day, and that is the finding: 14,982 attempts, 96.09% success, ₹2.09 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,982, successes=14,396, failed=568, pending=18, settled_value_inr=20,880,709.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,516; own_median=976; z=3.34
- banks: payer_bank=Axis Bank; attempts=905; success_rate=94.7; own_median=96.34; z=-2.17
- banks: payer_bank=IDFC First Bank; attempts=352; success_rate=94.03; own_median=96.57; z=-2.77
- products: product_name=UPI Lite Auto Top-Up; attempts=124; success_rate=91.13; own_median=96.74; z=-2.53
- products: product_name=UPI Lite Auto Top-Up; attempts=124; own_median=102.5; z=2.23

Refs: enterprise_data/warehouse/transactions, RPT-D204-DAILY, enterprise_data/warehouse/reference/incidents.parquet
