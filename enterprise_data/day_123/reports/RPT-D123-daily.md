---
id: RPT-D123-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 07 May 2026)

**Report ID:** RPT-D123-DAILY · **Day 123 of 206** · **Derived from:** 15,479 transaction rows queried live from the warehouse

## Summary

The rail took **15,479 payment attempts** on Thursday 07 May 2026 (Working day) and settled **₹2.33 Cr** across 14,864 successful payments. Volume was +0.4% on yesterday and +10.8% on the same weekday last week. Success closed at **96.03%**, above the trailing 28-day median of 95.53%.

Product UPI Circle is compounding — attempts up 80% across the trailing window to 549 today, with success holding, so the growth is healthy and worth funding. Product Credit on UPI is compounding — attempts up 56% across the trailing window to 330 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,479 | +0.4% | +10.8% | 15,445 |
| Successful payments | 14,864 | +0.3% | +12.6% | 14,839 |
| Success rate | 96.03% | −0.11pp | +1.52pp | 96.07% |
| Settled value | ₹2.33 Cr | +12.7% | +16.8% | ₹2.07 Cr |
| Average ticket | ₹1,568 | +12.3% | +3.8% | ₹1,392 |
| Technical declines | 0.562% | +0.08pp | −0.37pp | 0.490% |
| Business declines | 2.765% | −0.06pp | −0.13pp | 2.875% |
| Risk declines | 0.162% | +0.02pp | +0.05pp | 0.126% |
| Timeout declines | 0.342% | +0.04pp | −1.13pp | 0.324% |
| Retry share | 1.18% | +0.05pp | −1.21pp | 1.25% |
| Latency p95 | 1,266 ms | −1.1% | −18.2% | 1,245 ms |
| Active customers | 12,481 | −0.2% | +9.1% | 12,494 |
| Active merchants | 1,503 | +0.2% | +2.7% | 1,497 |

## What moved

- Product UPI Circle is compounding — attempts up 80% across the trailing window to 549 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 56% across the trailing window to 330 today, with success holding, so the growth is healthy and worth funding.
- Category Bills carried 1,671 attempts, 96% up its trailing median and 15.9% of the day's volume.
- Settled value moved up while volume moved up — average ticket at ₹1,568 against a trailing ₹1,380, so the day's shape is a mix shift rather than a demand shift.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,985 | 32.2% | 95.05% | ₹54.82 L | +13.7% |
| UPI Person to Merchant | 4,149 | 26.8% | 96.29% | ₹50.01 L | +25.3% |
| UPI QR Payments | 2,536 | 16.4% | 97.00% | ₹11.02 L | +11.8% |
| UPI Lite | 1,778 | 11.5% | 98.65% | ₹1.75 L | +44.1% |
| UPI Circle | 549 | 3.5% | 96.36% | ₹4.72 L | +57.3% |
| RuPay Credit on UPI | 381 | 2.5% | 93.70% | ₹26.13 L | +10.3% |
| Credit on UPI | 330 | 2.1% | 96.36% | ₹41.55 L | +27.2% |
| UPI AutoPay | 329 | 2.1% | 92.40% | ₹6.95 L | +1.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,823 | 96.08% | 95.67% | ₹75.45 L | normal |
| HDFC Bank | 1,661 | 96.03% | 95.93% | ₹30.20 L | normal |
| Bank of Baroda | 1,175 | 96.09% | 95.57% | ₹18.64 L | normal |
| Union Bank of India | 1,111 | 94.87% | 94.99% | ₹15.79 L | normal |
| ICICI Bank | 1,003 | 96.91% | 96.41% | ₹15.64 L | normal |
| Axis Bank | 984 | 95.73% | 95.93% | ₹12.97 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,285 | 96.12% | 95.76% | ₹1.15 Cr | normal |
| Google Pay | 5,103 | 95.87% | 95.56% | ₹76.14 L | normal |
| Paytm | 1,275 | 96.16% | 95.42% | ₹19.31 L | normal |
| Navi | 543 | 96.32% | 95.83% | ₹4.84 L | normal |
| SuperMoney | 306 | 94.44% | 95.51% | ₹2.86 L | normal |
| BHIM | 157 | 96.18% | 95.11% | ₹2.42 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,894 | 96.58% | ₹56.78 L |
| Food & Beverage | 2,405 | 97.05% | ₹12.70 L |
| Bills | 1,671 | 97.19% | ₹19.27 L |
| Mobility | 1,143 | 96.94% | ₹5.96 L |
| Healthcare | 580 | 96.03% | ₹5.07 L |
| Digital | 325 | 94.15% | ₹1.82 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,756 | 30.7% | 95.90% | ₹62.66 L |
| North | 3,818 | 24.7% | 96.20% | ₹63.79 L |
| West | 3,712 | 24.0% | 95.72% | ₹64.79 L |
| East | 1,935 | 12.5% | 96.43% | ₹29.80 L |
| Central | 1,258 | 8.1% | 96.26% | ₹12.11 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 84.85% | ₹3.55 L |
| Vasant Wardrobe | Key Account | Retail | 69 | 89.86% | ₹2.22 L |
| Ujjwal Water Board | Key Account | Bills | 82 | 93.90% | ₹1.40 L |
| Rapid Bazaar | Key Account | Retail | 372 | 97.04% | ₹1.28 L |
| Girnar Connect | Key Account | Bills | 293 | 98.98% | ₹1.10 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 66 | 95.45% | ₹1.07 L |
| Hampi Stores 2298 | Key Account | Retail | 101 | 97.03% | ₹94,317 |
| Hampi Styles | Key Account | Retail | 34 | 97.06% | ₹84,436 |

## Failure analysis

Of 593 declined attempts, 428 were business declines (2.765% of attempts — balances, PINs and limits), 87 technical (0.562%), 53 timeouts (0.342%) and 25 risk declines (0.162%).

183 attempts were re-presentations of an earlier failure (1.18% of the day); 70.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 180 | 1.163% | 1.292% |
| ZM | Invalid UPI PIN | business | Customer | 142 | 0.917% | 1.050% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.317% | 0.384% |
| U30 | Debit failed at remitter bank | technical | Issuer | 35 | 0.226% | 0.212% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.187% | 0.224% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.162% | 0.196% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.155% | 0.128% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.136% | 0.108% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 82 | 89 |
| Auto-reversals | 30 | 26 |
| Disputes / chargebacks | 11 | 12 |
| Value returned | ₹2.08 L | ₹1.43 L |

## Customer behaviour

12,481 distinct customers transacted (+16.0% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,975 | 4,646 | 1.17 | 96.00% | ₹1,559 |
| power | 2,571 | 3,618 | 1.41 | 95.38% | ₹2,442 |
| merchant_heavy | 2,855 | 3,577 | 1.25 | 96.34% | ₹1,038 |
| small_ticket | 1,793 | 2,261 | 1.26 | 96.42% | ₹592 |
| occasional | 1,022 | 1,089 | 1.07 | 95.87% | ₹1,721 |
| new | 230 | 251 | 1.09 | 98.80% | ₹927 |
| dormant_returning | 35 | 37 | 1.06 | 94.59% | ₹2,121 |

## Operational events

- **INC-BANK-0008** (Sev-3) — Canara Bank issuer decline spike, scoped to Canara Bank between 20:00 and 24:00. Canara Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 80% across the trailing window to 549 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 56% across the trailing window to 330 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 07 May: success came in 0.49pp above baseline at 96.03% on 15,479 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,479, successes=14,864, failed=593, pending=22, settled_value_inr=23,314,043.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=549; window_growth_pct=79.5; success_rate=96.36
- products: product_name=Credit on UPI; attempts=330; window_growth_pct=55.9; success_rate=96.36
- categories: mcc_category=Bills; attempts=1,671; own_median=852.5; z=3.97
- headline: value_inr=23,314,043; avg_ticket=1,568.49; trailing_avg_ticket=1,379.63
- incidents: event_id=INC-BANK-0008; kind=bank_outage; severity=Sev-3; window=2026-05-05 to 2026-05-07; success_impact_pp=-5.9; volume_impact_pct=-5.23
- categories: mcc_category=Healthcare; attempts=580; own_median=427.5; z=2.45
- categories: mcc_category=Digital; attempts=325; own_median=209.5; z=3.25
- incidents: event_id=CMP-0055; kind=merchant_campaign; severity=Sev-3; window=2026-04-30 to 2026-05-08; success_impact_pp=-0.17; volume_impact_pct=67.55

Refs: enterprise_data/warehouse/transactions, RPT-D122-DAILY, enterprise_data/warehouse/reference/incidents.parquet
