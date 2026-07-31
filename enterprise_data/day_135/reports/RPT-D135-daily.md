---
id: RPT-D135-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 19 May 2026)

**Report ID:** RPT-D135-DAILY · **Day 135 of 206** · **Derived from:** 14,608 transaction rows queried live from the warehouse

## Summary

The rail took **14,608 payment attempts** on Tuesday 19 May 2026 (Summer Travel Peak (build-up)) and settled **₹2.00 Cr** across 14,048 successful payments. Volume was −7.2% on yesterday and +6.0% on the same weekday last week. Success closed at **96.17%**, above the trailing 28-day median of 95.84%.

Product UPI Circle is compounding — attempts up 79% across the trailing window to 520 today, with success holding, so the growth is healthy and worth funding. Product UPI International is compounding — attempts up 67% across the trailing window to 204 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,608 | −7.2% | +6.0% | 15,070 |
| Successful payments | 14,048 | −7.4% | +6.1% | 14,452 |
| Success rate | 96.17% | −0.21pp | +0.07pp | 95.90% |
| Settled value | ₹2.00 Cr | −9.1% | +5.6% | ₹2.00 Cr |
| Average ticket | ₹1,423 | −1.8% | −0.4% | ₹1,384 |
| Technical declines | 0.459% | +0.03pp | +0.08pp | 0.529% |
| Business declines | 2.807% | +0.17pp | −0.15pp | 2.911% |
| Risk declines | 0.130% | +0.03pp | +0.01pp | 0.125% |
| Timeout declines | 0.322% | −0.03pp | −0.06pp | 0.432% |
| Retry share | 1.18% | +0.26pp | +0.13pp | 1.41% |
| Latency p95 | 1,273 ms | −2.8% | +1.7% | 1,293 ms |
| Active customers | 12,049 | −5.2% | +5.7% | 12,241 |
| Active merchants | 1,482 | −5.0% | −3.7% | 1,506 |

## What moved

- Product UPI Circle is compounding — attempts up 79% across the trailing window to 520 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 67% across the trailing window to 204 today, with success holding, so the growth is healthy and worth funding.
- Region Central ran at 97.53% success on 1,294 attempts (8.9% of the day), 1.55pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,443 | 30.4% | 95.32% | ₹45.99 L | +1.7% |
| UPI Person to Merchant | 3,987 | 27.3% | 96.39% | ₹39.61 L | +3.4% |
| UPI QR Payments | 2,430 | 16.6% | 96.79% | ₹10.78 L | +3.6% |
| UPI Lite | 1,684 | 11.5% | 98.40% | ₹1.44 L | +6.7% |
| UPI Circle | 520 | 3.6% | 96.73% | ₹4.34 L | +8.4% |
| Credit on UPI | 381 | 2.6% | 95.80% | ₹32.53 L | +19.2% |
| UPI AutoPay | 354 | 2.4% | 89.55% | ₹6.53 L | +7.9% |
| RuPay Credit on UPI | 324 | 2.2% | 95.37% | ₹17.30 L | −10.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,703 | 95.96% | 95.95% | ₹57.60 L | normal |
| HDFC Bank | 1,499 | 96.20% | 96.12% | ₹27.14 L | normal |
| Bank of Baroda | 1,106 | 95.93% | 95.79% | ₹13.10 L | normal |
| Union Bank of India | 1,046 | 96.85% | 95.06% | ₹14.62 L | normal |
| Axis Bank | 923 | 97.18% | 96.27% | ₹12.49 L | normal |
| Punjab National Bank | 849 | 96.35% | 95.46% | ₹11.80 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,825 | 96.25% | 95.90% | ₹96.30 L | normal |
| Google Pay | 4,868 | 96.08% | 95.63% | ₹67.70 L | normal |
| Paytm | 1,241 | 95.41% | 95.95% | ₹14.68 L | normal |
| Navi | 546 | 96.70% | 95.51% | ₹6.02 L | normal |
| SuperMoney | 277 | 95.67% | 96.38% | ₹4.81 L | normal |
| FamApp | 138 | 97.10% | 95.12% | ₹1.47 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,417 | 96.69% | ₹54.41 L |
| Food & Beverage | 2,590 | 96.83% | ₹15.52 L |
| Mobility | 1,161 | 97.50% | ₹6.60 L |
| Bills | 838 | 97.02% | ₹10.07 L |
| Healthcare | 468 | 95.73% | ₹6.39 L |
| Digital | 197 | 94.92% | ₹1.21 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,224 | 28.9% | 96.40% | ₹55.48 L |
| North | 3,692 | 25.3% | 95.72% | ₹52.41 L |
| West | 3,634 | 24.9% | 95.90% | ₹47.62 L |
| East | 1,764 | 12.1% | 96.09% | ₹27.17 L |
| Central | 1,294 | 8.9% | 97.53% | ₹17.17 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 36 | 91.67% | ₹3.61 L |
| Rapid Bazaar | Key Account | Retail | 461 | 96.75% | ₹2.22 L |
| Vasant Wardrobe | Key Account | Retail | 93 | 93.55% | ₹1.73 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 95 | 94.74% | ₹96,196 |
| Urban Boutique | Key Account | Retail | 121 | 95.87% | ₹95,882 |
| Hampi Stores 2298 | Key Account | Retail | 130 | 97.69% | ₹87,396 |
| Ujjwal Water Board | Key Account | Bills | 48 | 95.83% | ₹87,047 |
| Girnar Connect | Key Account | Bills | 145 | 97.93% | ₹68,526 |

## Failure analysis

Of 543 declined attempts, 410 were business declines (2.807% of attempts — balances, PINs and limits), 67 technical (0.459%), 47 timeouts (0.322%) and 19 risk declines (0.130%).

172 attempts were re-presentations of an earlier failure (1.18% of the day); 75.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 195 | 1.335% | 1.207% |
| ZM | Invalid UPI PIN | business | Customer | 124 | 0.849% | 1.040% |
| ZA | Transaction declined by customer | business | Customer | 41 | 0.281% | 0.343% |
| XH | Account does not exist / frozen | business | Issuer | 37 | 0.253% | 0.219% |
| U30 | Debit failed at remitter bank | technical | Issuer | 30 | 0.205% | 0.212% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.178% | 0.165% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.116% | 0.104% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.110% | 0.139% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 105 | 92 |
| Auto-reversals | 29 | 28 |
| Disputes / chargebacks | 11 | 13 |
| Value returned | ₹1.88 L | ₹1.98 L |

## Customer behaviour

12,049 distinct customers transacted (+4.9% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,747 | 4,280 | 1.14 | 95.86% | ₹1,488 |
| power | 2,548 | 3,482 | 1.37 | 96.35% | ₹1,749 |
| merchant_heavy | 2,760 | 3,352 | 1.21 | 96.03% | ₹1,221 |
| small_ticket | 1,817 | 2,258 | 1.24 | 96.68% | ₹681 |
| occasional | 923 | 964 | 1.04 | 96.06% | ₹1,686 |
| new | 224 | 241 | 1.08 | 96.68% | ₹971 |
| dormant_returning | 30 | 31 | 1.03 | 93.55% | ₹1,109 |

## Operational events

- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0063** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0066** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 79% across the trailing window to 520 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 67% across the trailing window to 204 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

19 May ran on trend at 96.17% success and ₹2.00 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 79% across the trailing window to 520 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,608, successes=14,048, failed=543, pending=17, settled_value_inr=19,983,858.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=520; window_growth_pct=78.7; success_rate=96.73
- products: product_name=UPI International; attempts=204; window_growth_pct=66.7; success_rate=98.04
- geography: region=Central; attempts=1,294; success_rate=97.53; own_median=95.98; z=3.21
- banks: payer_bank=IDFC First Bank; attempts=401; success_rate=97.76; own_median=95.77; z=2.44
- incidents: event_id=CMP-0067; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-19; success_impact_pp=-0.12; volume_impact_pct=49.99
- incidents: event_id=CMP-0063; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-22; success_impact_pp=-0.19; volume_impact_pct=75.81
- incidents: event_id=CMP-0066; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-21; success_impact_pp=-0.17; volume_impact_pct=66.69

Refs: enterprise_data/warehouse/transactions, RPT-D134-DAILY, enterprise_data/warehouse/reference/incidents.parquet
