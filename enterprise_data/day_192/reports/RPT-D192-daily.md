---
id: RPT-D192-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 15 Jul 2026)

**Report ID:** RPT-D192-DAILY · **Day 192 of 206** · **Derived from:** 14,885 transaction rows queried live from the warehouse

## Summary

The rail took **14,885 payment attempts** on Wednesday 15 July 2026 (Working day) and settled **₹2.17 Cr** across 14,368 successful payments. Volume was −5.7% on yesterday and −10.5% on the same weekday last week. Success closed at **96.53%**, above the trailing 28-day median of 96.13%.

Product UPI Person to Person ran at 95.98% success on 4,649 attempts (31.2% of the day), 0.84pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,885 | −5.7% | −10.5% | 16,564 |
| Successful payments | 14,368 | −5.3% | −10.7% | 15,916 |
| Success rate | 96.53% | +0.39pp | −0.27pp | 96.13% |
| Settled value | ₹2.17 Cr | −8.2% | +0.9% | ₹2.14 Cr |
| Average ticket | ₹1,512 | −3.1% | +13.0% | ₹1,345 |
| Technical declines | 0.329% | −0.06pp | −0.08pp | 0.473% |
| Business declines | 2.808% | −0.25pp | +0.35pp | 2.774% |
| Risk declines | 0.074% | −0.01pp | −0.03pp | 0.105% |
| Timeout declines | 0.141% | −0.13pp | −0.05pp | 0.437% |
| Retry share | 0.99% | −0.13pp | +0.09pp | 1.39% |
| Latency p95 | 1,301 ms | +0.2% | +4.0% | 1,304 ms |
| Active customers | 12,350 | −4.9% | −8.1% | 13,414 |
| Active merchants | 1,570 | +0.2% | −3.7% | 1,619 |

## What moved

- Product UPI Person to Person ran at 95.98% success on 4,649 attempts (31.2% of the day), 0.84pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,649 | 31.2% | 95.98% | ₹49.11 L | +3.2% |
| UPI Person to Merchant | 3,549 | 23.8% | 96.20% | ₹36.65 L | −2.0% |
| UPI QR Payments | 2,167 | 14.6% | 96.54% | ₹9.80 L | −16.0% |
| UPI Lite | 2,027 | 13.6% | 99.26% | ₹1.80 L | −21.0% |
| UPI Circle | 696 | 4.7% | 98.13% | ₹5.34 L | −13.8% |
| Credit on UPI | 594 | 4.0% | 96.30% | ₹54.14 L | +24.5% |
| UPI AutoPay | 369 | 2.5% | 92.14% | ₹8.20 L | −2.4% |
| RuPay Credit on UPI | 355 | 2.4% | 94.65% | ₹16.20 L | −7.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,697 | 96.64% | 96.18% | ₹65.87 L | normal |
| HDFC Bank | 1,633 | 96.75% | 96.39% | ₹22.82 L | normal |
| Bank of Baroda | 1,163 | 96.47% | 96.22% | ₹13.40 L | normal |
| Union Bank of India | 1,044 | 97.03% | 96.13% | ₹19.61 L | normal |
| ICICI Bank | 918 | 96.19% | 96.37% | ₹11.99 L | normal |
| Axis Bank | 909 | 96.04% | 96.17% | ₹14.61 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,010 | 96.69% | 96.15% | ₹99.98 L | normal |
| Google Pay | 4,843 | 96.04% | 96.13% | ₹65.50 L | normal |
| Paytm | 1,214 | 96.71% | 96.24% | ₹20.28 L | normal |
| Navi | 592 | 97.97% | 96.37% | ₹7.03 L | normal |
| SuperMoney | 301 | 96.01% | 96.19% | ₹7.22 L | normal |
| BHIM | 133 | 96.24% | 95.87% | ₹4.49 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,222 | 96.87% | ₹62.81 L |
| Food & Beverage | 2,574 | 97.24% | ₹12.80 L |
| Mobility | 1,245 | 97.83% | ₹7.38 L |
| Bills | 953 | 96.96% | ₹10.83 L |
| Healthcare | 580 | 95.34% | ₹8.98 L |
| Digital | 185 | 92.97% | ₹80,508 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,510 | 30.3% | 96.70% | ₹65.00 L |
| North | 3,725 | 25.0% | 96.78% | ₹51.92 L |
| West | 3,679 | 24.7% | 96.17% | ₹61.01 L |
| East | 1,694 | 11.4% | 96.87% | ₹24.10 L |
| Central | 1,277 | 8.6% | 95.77% | ₹15.21 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 43 | 90.70% | ₹2.42 L |
| Vasant Wardrobe | Key Account | Retail | 82 | 93.90% | ₹2.39 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 84 | 97.62% | ₹1.99 L |
| Rapid Bazaar | Key Account | Retail | 429 | 96.74% | ₹1.95 L |
| Hampi Styles | Key Account | Retail | 54 | 96.30% | ₹1.19 L |
| Hampi Stores 2298 | Key Account | Retail | 99 | 97.98% | ₹92,994 |
| Urban Boutique | Key Account | Retail | 119 | 96.64% | ₹88,666 |
| Girnar Connect | Key Account | Bills | 155 | 96.13% | ₹88,199 |

## Failure analysis

Of 499 declined attempts, 418 were business declines (2.808% of attempts — balances, PINs and limits), 49 technical (0.329%), 21 timeouts (0.141%) and 11 risk declines (0.074%).

148 attempts were re-presentations of an earlier failure (0.99% of the day); 66.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 169 | 1.135% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 133 | 0.894% | 0.956% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.336% | 0.323% |
| XH | Account does not exist / frozen | business | Issuer | 36 | 0.242% | 0.187% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.141% | 0.176% |
| ZX | Mandate not found or revoked | business | PSP | 18 | 0.121% | 0.080% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.114% | 0.131% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.107% | 0.121% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 95 | 112 |
| Auto-reversals | 16 | 24 |
| Disputes / chargebacks | 17 | 14 |
| Value returned | ₹1.72 L | ₹1.80 L |

## Customer behaviour

12,350 distinct customers transacted (−5.8% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,910 | 4,489 | 1.15 | 96.48% | ₹1,533 |
| power | 2,679 | 3,590 | 1.34 | 95.99% | ₹2,109 |
| merchant_heavy | 2,774 | 3,336 | 1.20 | 96.73% | ₹1,092 |
| small_ticket | 1,779 | 2,175 | 1.22 | 96.78% | ₹708 |
| occasional | 965 | 1,024 | 1.06 | 97.17% | ₹1,780 |
| new | 218 | 243 | 1.11 | 97.53% | ₹761 |
| dormant_returning | 25 | 28 | 1.12 | 96.43% | ₹2,777 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Category Healthcare ran at 95.34% success on 580 attempts (5.7% of the day), 1.81pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

15 July ran on trend at 96.53% success and ₹2.17 Cr settled. The movement worth carrying forward is in the product mix: product UPI Person to Person ran at 95.98% success on 4,649 attempts (31.2% of the day), 0.84pp up its own 28-day median. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,885, successes=14,368, failed=499, pending=18, settled_value_inr=21,724,115.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Person to Person; attempts=4,649; success_rate=95.98; own_median=95.14; z=2.41
- categories: mcc_category=Healthcare; attempts=580; success_rate=95.34; own_median=97.15; z=-2.67

Refs: enterprise_data/warehouse/transactions, RPT-D191-DAILY, enterprise_data/warehouse/reference/incidents.parquet
