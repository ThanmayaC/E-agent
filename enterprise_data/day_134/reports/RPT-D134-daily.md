---
id: RPT-D134-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 18 May 2026)

**Report ID:** RPT-D134-DAILY · **Day 134 of 206** · **Derived from:** 15,743 transaction rows queried live from the warehouse

## Summary

The rail took **15,743 payment attempts** on Monday 18 May 2026 (Summer Travel Peak) and settled **₹2.20 Cr** across 15,172 successful payments. Volume was +7.7% on yesterday and +15.2% on the same weekday last week. Success closed at **96.37%**, above the trailing 28-day median of 95.84%.

Product UPI Circle is compounding — attempts up 69% across the trailing window to 675 today, with success holding, so the growth is healthy and worth funding. Product UPI Person to Person ran at 96.13% success on 5,174 attempts (32.9% of the day), 1.09pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,743 | +7.7% | +15.2% | 15,095 |
| Successful payments | 15,172 | +8.4% | +15.2% | 14,474 |
| Success rate | 96.37% | +0.67pp | +0.04pp | 95.88% |
| Settled value | ₹2.20 Cr | +40.1% | +14.3% | ₹2.00 Cr |
| Average ticket | ₹1,449 | +29.3% | −0.8% | ₹1,382 |
| Technical declines | 0.432% | −0.03pp | +0.01pp | 0.533% |
| Business declines | 2.636% | −0.74pp | −0.13pp | 2.917% |
| Risk declines | 0.102% | +0.01pp | −0.01pp | 0.125% |
| Timeout declines | 0.349% | +0.07pp | +0.06pp | 0.438% |
| Retry share | 0.92% | −1.00pp | −0.24pp | 1.42% |
| Latency p95 | 1,310 ms | +4.5% | +4.6% | 1,294 ms |
| Active customers | 12,709 | +6.4% | +12.1% | 12,252 |
| Active merchants | 1,560 | +5.0% | +5.1% | 1,508 |

## What moved

- Product UPI Circle is compounding — attempts up 69% across the trailing window to 675 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Person ran at 96.13% success on 5,174 attempts (32.9% of the day), 1.09pp up its own 28-day median.
- Product UPI Lite is compounding — attempts up 55% across the trailing window to 1,795 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,174 | 32.9% | 96.13% | ₹60.33 L | +18.4% |
| UPI Person to Merchant | 3,836 | 24.4% | 95.65% | ₹36.19 L | −1.2% |
| UPI QR Payments | 2,609 | 16.6% | 97.20% | ₹13.44 L | +11.2% |
| UPI Lite | 1,795 | 11.4% | 99.05% | ₹1.74 L | +15.1% |
| UPI Circle | 675 | 4.3% | 97.78% | ₹6.36 L | +40.9% |
| Credit on UPI | 421 | 2.7% | 96.67% | ₹31.67 L | +31.8% |
| RuPay Credit on UPI | 396 | 2.5% | 94.70% | ₹22.47 L | +9.8% |
| UPI AutoPay | 321 | 2.0% | 90.97% | ₹5.55 L | −2.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,003 | 96.04% | 95.95% | ₹68.29 L | normal |
| HDFC Bank | 1,721 | 96.98% | 96.06% | ₹21.16 L | normal |
| Bank of Baroda | 1,165 | 96.82% | 95.79% | ₹17.83 L | normal |
| Union Bank of India | 1,037 | 97.01% | 95.03% | ₹11.60 L | ⚠ outlier |
| Axis Bank | 984 | 96.75% | 96.02% | ₹18.27 L | normal |
| Punjab National Bank | 980 | 97.04% | 95.46% | ₹14.84 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,555 | 96.66% | 95.90% | ₹98.96 L | normal |
| Google Pay | 5,115 | 96.07% | 95.63% | ₹75.80 L | normal |
| Paytm | 1,266 | 95.81% | 96.04% | ₹19.01 L | normal |
| Navi | 562 | 96.26% | 95.51% | ₹6.60 L | normal |
| SuperMoney | 323 | 96.90% | 96.07% | ₹6.21 L | normal |
| BHIM | 150 | 98.67% | 95.64% | ₹1.88 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,484 | 96.63% | ₹54.52 L |
| Food & Beverage | 2,573 | 96.85% | ₹16.23 L |
| Mobility | 1,431 | 98.04% | ₹8.79 L |
| Bills | 833 | 95.92% | ₹7.98 L |
| Healthcare | 482 | 97.72% | ₹5.92 L |
| Travel | 219 | 91.78% | ₹46.47 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,593 | 29.2% | 96.19% | ₹71.29 L |
| North | 3,958 | 25.1% | 96.56% | ₹48.60 L |
| West | 3,844 | 24.4% | 96.57% | ₹54.52 L |
| East | 1,959 | 12.4% | 96.17% | ₹28.33 L |
| Central | 1,389 | 8.8% | 96.18% | ₹17.14 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 494 | 96.15% | ₹2.60 L |
| Vasant Wardrobe | Key Account | Retail | 102 | 94.12% | ₹1.95 L |
| Hampi Stores 2298 | Key Account | Retail | 143 | 97.90% | ₹1.40 L |
| Hampi Styles | Key Account | Retail | 56 | 96.43% | ₹1.39 L |
| Vega Electronics | Large | Retail | 32 | 90.62% | ₹1.38 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 102 | 98.04% | ₹1.08 L |
| Girnar Connect | Key Account | Bills | 144 | 96.53% | ₹75,080 |
| Urban Boutique | Key Account | Retail | 136 | 98.53% | ₹74,587 |

## Failure analysis

Of 554 declined attempts, 415 were business declines (2.636% of attempts — balances, PINs and limits), 68 technical (0.432%), 55 timeouts (0.349%) and 16 risk declines (0.102%).

145 attempts were re-presentations of an earlier failure (0.92% of the day); 70.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.112% | 1.210% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 0.800% | 1.040% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.337% | 0.343% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.222% | 0.218% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 35 | 0.222% | 0.165% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.140% | 0.212% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.133% | 0.139% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.095% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 104 | 92 |
| Auto-reversals | 25 | 28 |
| Disputes / chargebacks | 13 | 14 |
| Value returned | ₹2.40 L | ₹1.74 L |

## Customer behaviour

12,709 distinct customers transacted (+10.7% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,998 | 4,666 | 1.17 | 96.46% | ₹1,390 |
| power | 2,721 | 3,791 | 1.39 | 95.57% | ₹1,995 |
| merchant_heavy | 2,898 | 3,594 | 1.24 | 97.02% | ₹1,066 |
| small_ticket | 1,859 | 2,381 | 1.28 | 96.60% | ₹650 |
| occasional | 989 | 1,048 | 1.06 | 96.28% | ₹2,163 |
| new | 216 | 235 | 1.09 | 95.32% | ₹1,167 |
| dormant_returning | 28 | 28 | 1.00 | 100.00% | ₹746 |

## Operational events

- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0063** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0066** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI 123Pay ran at 90.20% success on 102 attempts (0.6% of the day), 4.54pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 69% across the trailing window to 675 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 55% across the trailing window to 1,795 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 18 May: success came in 0.54pp above baseline at 96.37% on 15,743 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,743, successes=15,172, failed=554, pending=17, settled_value_inr=21,989,416.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=675; window_growth_pct=68.8; success_rate=97.78
- products: product_name=UPI Person to Person; attempts=5,174; success_rate=96.13; own_median=95.05; z=2.84
- products: product_name=UPI Lite; attempts=1,795; window_growth_pct=55; success_rate=99.05
- banks: payer_bank=Union Bank of India; attempts=1,037; success_rate=97.01; own_median=95.03; z=2.3
- banks: payer_bank=Yes Bank; attempts=599; success_rate=98; own_median=95.64; z=2.48
- incidents: event_id=CMP-0067; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-19; success_impact_pp=-0.12; volume_impact_pct=49.99
- incidents: event_id=CMP-0063; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-22; success_impact_pp=-0.19; volume_impact_pct=75.81
- incidents: event_id=CMP-0066; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-21; success_impact_pp=-0.17; volume_impact_pct=66.69
- categories: mcc_category=Travel; attempts=219; own_median=144; z=2.53
- products: product_name=UPI International; attempts=218; own_median=142; z=2.7

Refs: enterprise_data/warehouse/transactions, RPT-D133-DAILY, enterprise_data/warehouse/reference/incidents.parquet
