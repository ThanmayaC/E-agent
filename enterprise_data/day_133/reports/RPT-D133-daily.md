---
id: RPT-D133-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 17 May 2026)

**Report ID:** RPT-D133-DAILY · **Day 133 of 206** · **Derived from:** 14,624 transaction rows queried live from the warehouse

## Summary

The rail took **14,624 payment attempts** on Sunday 17 May 2026 (Summer Travel Peak (build-up)) and settled **₹1.57 Cr** across 13,996 successful payments. Volume was −15.1% on yesterday and +7.1% on the same weekday last week. Success closed at **95.71%**, in line with the trailing 28-day median of 95.84%.

Product UPI Circle is compounding — attempts up 63% across the trailing window to 705 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,624 | −15.1% | +7.1% | 15,057 |
| Successful payments | 13,996 | −15.0% | +7.0% | 14,433 |
| Success rate | 95.71% | +0.11pp | −0.10pp | 95.85% |
| Settled value | ₹1.57 Cr | −31.4% | −1.4% | ₹1.99 Cr |
| Average ticket | ₹1,121 | −19.4% | −7.9% | ₹1,378 |
| Technical declines | 0.465% | −0.17pp | +0.02pp | 0.539% |
| Business declines | 3.378% | +0.28pp | +0.20pp | 2.933% |
| Risk declines | 0.089% | −0.05pp | −0.02pp | 0.126% |
| Timeout declines | 0.280% | −0.14pp | −0.04pp | 0.443% |
| Retry share | 1.92% | −0.34pp | +0.25pp | 1.45% |
| Latency p95 | 1,254 ms | −3.0% | +3.5% | 1,293 ms |
| Active customers | 11,943 | −12.7% | +5.8% | 12,225 |
| Active merchants | 1,486 | −7.1% | +3.4% | 1,505 |

## What moved

- Product UPI Circle is compounding — attempts up 63% across the trailing window to 705 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Lite is compounding — attempts up 48% across the trailing window to 2,060 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Category Food & Beverage ran at 96.22% success on 2,671 attempts (25.8% of the day), 0.80pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,262 | 29.1% | 95.33% | ₹43.62 L | −2.7% |
| UPI Person to Merchant | 3,772 | 25.8% | 95.57% | ₹34.81 L | −2.9% |
| UPI QR Payments | 2,668 | 18.2% | 95.95% | ₹12.18 L | +13.7% |
| UPI Lite | 2,060 | 14.1% | 98.25% | ₹1.77 L | +33.4% |
| UPI Circle | 705 | 4.8% | 94.89% | ₹5.45 L | +48.1% |
| UPI AutoPay | 368 | 2.5% | 91.03% | ₹6.60 L | +12.2% |
| RuPay Credit on UPI | 195 | 1.3% | 95.38% | ₹12.15 L | −45.9% |
| Credit on UPI | 188 | 1.3% | 97.34% | ₹14.40 L | −41.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,695 | 95.76% | 95.95% | ₹54.81 L | normal |
| HDFC Bank | 1,604 | 96.20% | 96.01% | ₹14.06 L | normal |
| Bank of Baroda | 1,104 | 95.02% | 95.88% | ₹13.02 L | normal |
| Union Bank of India | 976 | 95.29% | 94.99% | ₹9.54 L | normal |
| Axis Bank | 928 | 96.98% | 96.02% | ₹10.61 L | normal |
| ICICI Bank | 876 | 96.00% | 96.43% | ₹10.79 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,890 | 95.78% | 95.93% | ₹73.50 L | normal |
| Google Pay | 4,879 | 95.47% | 95.63% | ₹52.30 L | normal |
| Paytm | 1,150 | 95.48% | 96.04% | ₹12.73 L | normal |
| Navi | 536 | 95.90% | 95.35% | ₹5.70 L | normal |
| SuperMoney | 269 | 97.77% | 95.74% | ₹3.34 L | normal |
| BHIM | 145 | 97.24% | 95.46% | ₹1.61 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,132 | 95.98% | ₹37.94 L |
| Food & Beverage | 2,671 | 96.22% | ₹10.88 L |
| Mobility | 1,517 | 95.98% | ₹7.48 L |
| Bills | 840 | 96.90% | ₹9.72 L |
| Healthcare | 534 | 98.13% | ₹3.62 L |
| Digital | 199 | 91.46% | ₹96,876 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,238 | 29.0% | 96.04% | ₹44.77 L |
| North | 3,702 | 25.3% | 95.65% | ₹36.83 L |
| West | 3,695 | 25.3% | 95.78% | ₹42.14 L |
| East | 1,721 | 11.8% | 94.94% | ₹22.19 L |
| Central | 1,268 | 8.7% | 95.58% | ₹11.00 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 90 | 95.56% | ₹2.02 L |
| Rapid Bazaar | Key Account | Retail | 411 | 94.89% | ₹1.49 L |
| Vega Electronics | Large | Retail | 23 | 91.30% | ₹1.18 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 70 | 98.57% | ₹94,417 |
| Urban Boutique | Key Account | Retail | 129 | 97.67% | ₹87,824 |
| Hampi Styles | Key Account | Retail | 39 | 92.31% | ₹83,875 |
| Girnar Connect | Key Account | Bills | 161 | 97.52% | ₹80,280 |
| Hampi Stores 2298 | Key Account | Retail | 113 | 95.58% | ₹73,179 |

## Failure analysis

Of 616 declined attempts, 494 were business declines (3.378% of attempts — balances, PINs and limits), 68 technical (0.465%), 41 timeouts (0.280%) and 13 risk declines (0.089%).

281 attempts were re-presentations of an earlier failure (1.92% of the day); 64.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 201 | 1.374% | 1.210% |
| ZM | Invalid UPI PIN | business | Customer | 181 | 1.238% | 1.040% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.335% | 0.348% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.198% | 0.212% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.185% | 0.219% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.137% | 0.165% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.137% | 0.139% |
| ZX | Mandate not found or revoked | business | PSP | 17 | 0.116% | 0.081% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 115 | 92 |
| Auto-reversals | 47 | 28 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹3.06 L | ₹1.51 L |

## Customer behaviour

11,943 distinct customers transacted (+4.2% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,669 | 4,238 | 1.16 | 95.35% | ₹1,181 |
| power | 2,541 | 3,496 | 1.38 | 95.97% | ₹1,350 |
| merchant_heavy | 2,777 | 3,414 | 1.23 | 95.55% | ₹919 |
| small_ticket | 1,767 | 2,219 | 1.26 | 96.62% | ₹594 |
| occasional | 943 | 997 | 1.06 | 94.88% | ₹1,319 |
| new | 217 | 231 | 1.06 | 94.81% | ₹775 |
| dormant_returning | 29 | 29 | 1.00 | 100.00% | ₹613 |

## Operational events

- **CMP-0061** (Sev-3) — Wealth & SIP cashback campaign, scoped to 6211. A cashback campaign across Wealth & SIP merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **REG-0069** (Sev-3) — UPI International — two new acceptance corridors live, scoped to UPI_INTL. Two new cross-border acceptance corridors went live. Volume steps up; early-corridor settlement immaturity temporarily depresses the success rate.
- **CMP-0063** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0066** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 63% across the trailing window to 705 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Lite is compounding — attempts up 48% across the trailing window to 2,060 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- 47 auto-reversals were raised, 2.3 sigma above the trailing median of 28.
- Category Food & Beverage ran at 96.22% success on 2,671 attempts (25.8% of the day), 0.80pp down its own 28-day median.
- Product UPI Circle ran at 94.89% success on 705 attempts (4.8% of the day), 1.78pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

17 May ran on trend at 95.71% success and ₹1.57 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 63% across the trailing window to 705 today, but success is slipping as it scales, so the growth is outrunning its reliability. 3 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,624, successes=13,996, failed=616, pending=12, settled_value_inr=15,693,423.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=705; window_growth_pct=62.8; success_rate=94.89
- products: product_name=UPI Lite; attempts=2,060; window_growth_pct=48; success_rate=98.25
- adjustments: reversals=47; trailing_median=28.5; z=2.27
- categories: mcc_category=Food & Beverage; attempts=2,671; success_rate=96.22; own_median=97.02; z=-2.09
- products: product_name=UPI Circle; attempts=705; success_rate=94.89; own_median=96.68; z=-2.01
- incidents: event_id=CMP-0061; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-17; success_impact_pp=-0.14; volume_impact_pct=57.92
- incidents: event_id=CMP-0067; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-19; success_impact_pp=-0.12; volume_impact_pct=49.99
- incidents: event_id=REG-0069; kind=corridor_launch; severity=Sev-3; window=2026-05-14 to 2026-07-29; success_impact_pp=-0.55; volume_impact_pct=54
- incidents: event_id=CMP-0063; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-22; success_impact_pp=-0.19; volume_impact_pct=75.81
- incidents: event_id=CMP-0066; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-21; success_impact_pp=-0.17; volume_impact_pct=66.69

Refs: enterprise_data/warehouse/transactions, RPT-D132-DAILY, enterprise_data/warehouse/reference/incidents.parquet
