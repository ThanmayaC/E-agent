---
id: RPT-D124-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 08 May 2026)

**Report ID:** RPT-D124-DAILY · **Day 124 of 206** · **Derived from:** 16,638 transaction rows queried live from the warehouse

## Summary

The rail took **16,638 payment attempts** on Friday 08 May 2026 (Working day) and settled **₹2.28 Cr** across 15,993 successful payments. Volume was +7.5% on yesterday and +12.7% on the same weekday last week. Success closed at **96.12%**, above the trailing 28-day median of 95.53%.

Product UPI Circle is compounding — attempts up 84% across the trailing window to 473 today, with success holding, so the growth is healthy and worth funding. Product UPI Lite is compounding — attempts up 60% across the trailing window to 1,967 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,638 | +7.5% | +12.7% | 15,594 |
| Successful payments | 15,993 | +7.6% | +12.8% | 14,983 |
| Success rate | 96.12% | +0.10pp | +0.09pp | 96.08% |
| Settled value | ₹2.28 Cr | −2.1% | +35.5% | ₹2.10 Cr |
| Average ticket | ₹1,427 | −9.0% | +20.2% | ₹1,397 |
| Technical declines | 0.613% | +0.05pp | +0.26pp | 0.505% |
| Business declines | 2.759% | −0.01pp | −0.31pp | 2.861% |
| Risk declines | 0.138% | −0.02pp | +0.00pp | 0.127% |
| Timeout declines | 0.288% | −0.05pp | +0.04pp | 0.320% |
| Retry share | 1.07% | −0.11pp | −0.54pp | 1.23% |
| Latency p95 | 1,244 ms | −1.7% | +2.2% | 1,245 ms |
| Active customers | 13,213 | +5.9% | +10.1% | 12,584 |
| Active merchants | 1,542 | +2.6% | +5.1% | 1,503 |

## What moved

- Product UPI Circle is compounding — attempts up 84% across the trailing window to 473 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 60% across the trailing window to 1,967 today, with success holding, so the growth is healthy and worth funding.
- Category Retail carried 4,794 attempts, 39% up its trailing median and 42.5% of the day's volume.
- Product UPI Person to Person ran at 95.83% success on 5,370 attempts (32.3% of the day), 0.88pp up its own 28-day median.
- Category Food & Beverage carried 2,832 attempts, 37% up its trailing median and 25.1% of the day's volume.
- Region West carried 4,244 attempts, 35% up its trailing median and 25.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,370 | 32.3% | 95.83% | ₹60.85 L | +22.5% |
| UPI Person to Merchant | 4,485 | 27.0% | 96.05% | ₹52.99 L | +34.9% |
| UPI QR Payments | 2,795 | 16.8% | 96.49% | ₹13.02 L | +20.5% |
| UPI Lite | 1,967 | 11.8% | 98.88% | ₹1.85 L | +51.3% |
| UPI Circle | 473 | 2.8% | 98.31% | ₹4.42 L | +33.2% |
| RuPay Credit on UPI | 421 | 2.5% | 95.25% | ₹21.25 L | +20.6% |
| Credit on UPI | 347 | 2.1% | 95.39% | ₹34.94 L | +31.7% |
| UPI AutoPay | 295 | 1.8% | 86.10% | ₹4.89 L | −9.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,310 | 96.31% | 95.67% | ₹69.45 L | normal |
| HDFC Bank | 1,853 | 96.76% | 95.96% | ₹25.68 L | normal |
| Bank of Baroda | 1,289 | 96.20% | 95.66% | ₹19.92 L | normal |
| Union Bank of India | 1,174 | 95.23% | 94.95% | ₹14.72 L | normal |
| ICICI Bank | 1,018 | 97.45% | 96.41% | ₹10.88 L | normal |
| Axis Bank | 1,016 | 95.57% | 95.87% | ₹17.18 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,897 | 95.95% | 95.76% | ₹1.04 Cr | normal |
| Google Pay | 5,553 | 96.45% | 95.56% | ₹73.76 L | normal |
| Paytm | 1,331 | 96.77% | 95.42% | ₹22.54 L | normal |
| Navi | 601 | 94.51% | 95.83% | ₹9.38 L | normal |
| SuperMoney | 278 | 96.40% | 95.39% | ₹3.34 L | normal |
| FamApp | 161 | 94.41% | 95.77% | ₹2.13 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,794 | 96.54% | ₹59.64 L |
| Food & Beverage | 2,832 | 96.86% | ₹15.63 L |
| Mobility | 1,350 | 97.33% | ₹6.70 L |
| Bills | 946 | 95.03% | ₹12.87 L |
| Healthcare | 613 | 95.92% | ₹10.08 L |
| Digital | 217 | 92.17% | ₹1.19 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,831 | 29.0% | 95.92% | ₹66.75 L |
| West | 4,244 | 25.5% | 96.37% | ₹54.96 L |
| North | 4,207 | 25.3% | 95.91% | ₹63.85 L |
| East | 1,945 | 11.7% | 96.61% | ₹28.86 L |
| Central | 1,411 | 8.5% | 96.03% | ₹13.85 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 40 | 87.50% | ₹3.31 L |
| Vasant Wardrobe | Key Account | Retail | 84 | 94.05% | ₹2.82 L |
| Rapid Bazaar | Key Account | Retail | 479 | 98.75% | ₹1.98 L |
| Trinetra Restaurant | Large | Food & Beverage | 42 | 95.24% | ₹1.57 L |
| Hampi Stores 2298 | Key Account | Retail | 141 | 97.16% | ₹1.56 L |
| Urban Boutique | Key Account | Retail | 141 | 93.62% | ₹1.02 L |
| Hampi Styles | Key Account | Retail | 44 | 95.45% | ₹89,728 |
| Sarita Kitchen | Key Account | Food & Beverage | 163 | 96.93% | ₹89,533 |

## Failure analysis

Of 632 declined attempts, 459 were business declines (2.759% of attempts — balances, PINs and limits), 102 technical (0.613%), 48 timeouts (0.288%) and 23 risk declines (0.138%).

178 attempts were re-presentations of an earlier failure (1.07% of the day); 66.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 186 | 1.118% | 1.292% |
| ZM | Invalid UPI PIN | business | Customer | 140 | 0.841% | 1.050% |
| ZA | Transaction declined by customer | business | Customer | 59 | 0.355% | 0.384% |
| U30 | Debit failed at remitter bank | technical | Issuer | 45 | 0.270% | 0.216% |
| XH | Account does not exist / frozen | business | Issuer | 42 | 0.252% | 0.224% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.150% | 0.188% |
| U69 | Beneficiary bank offline | technical | Issuer | 23 | 0.138% | 0.082% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.126% | 0.136% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 90 | 88 |
| Auto-reversals | 29 | 26 |
| Disputes / chargebacks | 17 | 11 |
| Value returned | ₹4.64 L | ₹1.43 L |

## Customer behaviour

13,213 distinct customers transacted (+22.2% on the 28-day median) at 1.26 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,130 | 4,915 | 1.19 | 95.95% | ₹1,548 |
| power | 2,751 | 3,922 | 1.43 | 95.92% | ₹1,845 |
| merchant_heavy | 2,965 | 3,753 | 1.27 | 96.30% | ₹1,140 |
| small_ticket | 2,008 | 2,587 | 1.29 | 96.29% | ₹711 |
| occasional | 1,077 | 1,148 | 1.07 | 96.25% | ₹1,377 |
| new | 251 | 281 | 1.12 | 97.51% | ₹881 |
| dormant_returning | 31 | 32 | 1.03 | 96.88% | ₹1,096 |

## Operational events

- **INC-BANK-0001** (Sev-3) — Yes Bank issuer decline spike, scoped to Yes Bank between 23:00 and 05:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 84% across the trailing window to 473 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 60% across the trailing window to 1,967 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 08 May: success came in 0.59pp above baseline at 96.12% on 16,638 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,638, successes=15,993, failed=632, pending=13, settled_value_inr=22,827,153.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=473; window_growth_pct=84.1; success_rate=98.31
- products: product_name=UPI Lite; attempts=1,967; window_growth_pct=60.2; success_rate=98.88
- categories: mcc_category=Retail; attempts=4,794; own_median=3,454; z=2.99
- products: product_name=UPI Person to Person; attempts=5,370; success_rate=95.83; own_median=94.95; z=2.37
- categories: mcc_category=Food & Beverage; attempts=2,832; own_median=2,064.5; z=3.08
- geography: region=West; attempts=4,244; own_median=3,147.5; z=2.39
- incidents: event_id=INC-BANK-0001; kind=bank_outage; severity=Sev-3; window=2026-05-08 to 2026-05-12; success_impact_pp=-6.2; volume_impact_pct=-5.5
- categories: mcc_category=Mobility; attempts=1,350; own_median=938; z=2.46
- products: product_name=UPI Circle; attempts=473; success_rate=98.31; own_median=96.42; z=2.27
- incidents: event_id=CMP-0055; kind=merchant_campaign; severity=Sev-3; window=2026-04-30 to 2026-05-08; success_impact_pp=-0.17; volume_impact_pct=67.55

Refs: enterprise_data/warehouse/transactions, RPT-D123-DAILY, enterprise_data/warehouse/reference/incidents.parquet
