---
id: RPT-D185-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 08 Jul 2026)

**Report ID:** RPT-D185-DAILY · **Day 185 of 206** · **Derived from:** 16,626 transaction rows queried live from the warehouse

## Summary

The rail took **16,626 payment attempts** on Wednesday 08 July 2026 (Working day) and settled **₹2.15 Cr** across 16,094 successful payments. Volume was +0.8% on yesterday and −10.5% on the same weekday last week. Success closed at **96.80%**, above the trailing 28-day median of 96.16%.

22 disputes were raised, 2.7 sigma above the trailing median of 14. Success rate closed at 96.80%, 0.64pp up the trailing median — a 1.8-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,626 | +0.8% | −10.5% | 17,492 |
| Successful payments | 16,094 | +0.9% | −10.1% | 16,797 |
| Success rate | 96.80% | +0.14pp | +0.45pp | 96.08% |
| Settled value | ₹2.15 Cr | −7.2% | −14.6% | ₹2.25 Cr |
| Average ticket | ₹1,338 | −8.1% | −5.0% | ₹1,338 |
| Technical declines | 0.409% | +0.01pp | +0.03pp | 0.509% |
| Business declines | 2.454% | −0.05pp | −0.43pp | 2.613% |
| Risk declines | 0.108% | +0.04pp | +0.04pp | 0.111% |
| Timeout declines | 0.186% | −0.09pp | −0.06pp | 0.606% |
| Retry share | 0.91% | +0.02pp | −0.41pp | 1.53% |
| Latency p95 | 1,250 ms | −4.6% | +0.4% | 1,327 ms |
| Active customers | 13,436 | +0.4% | −8.7% | 14,010 |
| Active merchants | 1,631 | −1.7% | −1.6% | 1,652 |

## What moved

- Success rate closed at 96.80%, 0.64pp up the trailing median — a 1.8-sigma move.
- Product UPI Lite is compounding — attempts up 47% across the trailing window to 2,547 today, with success holding, so the growth is healthy and worth funding.
- Region South ran at 97.18% success on 4,865 attempts (29.3% of the day), 0.99pp up its own 28-day median.
- Product UPI Person to Person ran at 96.08% success on 4,820 attempts (29.0% of the day), 0.92pp up its own 28-day median.
- Product UPI Circle is compounding — attempts up 36% across the trailing window to 768 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments ran at 97.33% success on 2,733 attempts (16.4% of the day), 0.77pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,820 | 29.0% | 96.08% | ₹52.03 L | +13.1% |
| UPI Person to Merchant | 3,971 | 23.9% | 96.32% | ₹38.92 L | +15.5% |
| UPI QR Payments | 2,733 | 16.4% | 97.33% | ₹12.14 L | +10.1% |
| UPI Lite | 2,547 | 15.3% | 99.14% | ₹2.50 L | +7.7% |
| UPI Circle | 768 | 4.6% | 97.92% | ₹5.74 L | −3.8% |
| Credit on UPI | 500 | 3.0% | 95.00% | ₹37.89 L | +6.3% |
| RuPay Credit on UPI | 416 | 2.5% | 97.12% | ₹18.88 L | +10.9% |
| UPI AutoPay | 378 | 2.3% | 92.06% | ₹7.56 L | +0.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,246 | 96.34% | 96.16% | ₹71.45 L | normal |
| HDFC Bank | 1,807 | 97.68% | 96.37% | ₹22.14 L | normal |
| Bank of Baroda | 1,294 | 97.37% | 96.21% | ₹15.56 L | normal |
| Union Bank of India | 1,142 | 96.41% | 96.10% | ₹14.43 L | normal |
| Punjab National Bank | 1,000 | 96.70% | 95.93% | ₹14.16 L | normal |
| Axis Bank | 983 | 97.05% | 96.12% | ₹17.24 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,699 | 96.60% | 96.15% | ₹1.04 Cr | normal |
| Google Pay | 5,627 | 96.89% | 96.21% | ₹67.25 L | normal |
| Paytm | 1,344 | 96.88% | 96.03% | ₹23.19 L | normal |
| Navi | 652 | 97.09% | 96.55% | ₹5.96 L | normal |
| SuperMoney | 314 | 98.73% | 95.51% | ₹3.55 L | ⚠ outlier |
| BHIM | 162 | 97.53% | 95.85% | ₹1.86 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,927 | 96.91% | ₹58.39 L |
| Food & Beverage | 3,000 | 97.73% | ₹14.62 L |
| Mobility | 1,502 | 98.40% | ₹8.15 L |
| Bills | 956 | 96.44% | ₹10.33 L |
| Healthcare | 697 | 97.13% | ₹10.13 L |
| Digital | 225 | 95.11% | ₹98,043 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,865 | 29.3% | 97.18% | ₹62.21 L |
| North | 4,413 | 26.5% | 96.56% | ₹54.59 L |
| West | 4,085 | 24.6% | 96.45% | ₹56.70 L |
| East | 1,915 | 11.5% | 96.71% | ₹25.91 L |
| Central | 1,348 | 8.1% | 97.40% | ₹15.86 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 43 | 100.00% | ₹2.75 L |
| Rapid Bazaar | Key Account | Retail | 465 | 98.06% | ₹2.31 L |
| Vasant Wardrobe | Key Account | Retail | 90 | 94.44% | ₹2.12 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 88 | 97.73% | ₹1.69 L |
| Hampi Styles | Key Account | Retail | 55 | 100.00% | ₹1.59 L |
| Hampi Stores 2298 | Key Account | Retail | 129 | 99.22% | ₹1.19 L |
| Urban Boutique | Key Account | Retail | 125 | 95.20% | ₹82,733 |
| Aravalli Pharmacy | Large | Healthcare | 113 | 99.12% | ₹73,135 |

## Failure analysis

Of 525 declined attempts, 408 were business declines (2.454% of attempts — balances, PINs and limits), 68 technical (0.409%), 31 timeouts (0.186%) and 18 risk declines (0.108%).

151 attempts were re-presentations of an earlier failure (0.91% of the day); 64.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 0.932% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 141 | 0.848% | 0.970% |
| ZA | Transaction declined by customer | business | Customer | 59 | 0.355% | 0.328% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.174% | 0.176% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.132% | 0.199% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.120% | 0.122% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.102% | 0.102% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 15 | 0.090% | 0.132% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 124 | 108 |
| Auto-reversals | 19 | 24 |
| Disputes / chargebacks | 22 | 14 |
| Value returned | ₹1.31 L | ₹1.71 L |

## Customer behaviour

13,436 distinct customers transacted (+10.1% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,224 | 4,957 | 1.17 | 96.71% | ₹1,301 |
| power | 2,896 | 4,018 | 1.39 | 96.47% | ₹1,908 |
| merchant_heavy | 3,064 | 3,837 | 1.25 | 97.16% | ₹1,020 |
| small_ticket | 2,009 | 2,497 | 1.24 | 96.68% | ₹505 |
| occasional | 994 | 1,041 | 1.05 | 97.21% | ₹1,858 |
| new | 213 | 238 | 1.12 | 97.48% | ₹1,104 |
| dormant_returning | 36 | 38 | 1.06 | 100.00% | ₹1,028 |

## Operational events

- **INC-BANK-0022** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 11:00 and 14:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- 22 disputes were raised, 2.7 sigma above the trailing median of 14.

### Opportunities

- Product UPI Lite is compounding — attempts up 47% across the trailing window to 2,547 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 36% across the trailing window to 768 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 08 July: success came in 0.64pp above baseline at 96.80% on 16,626 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,626, successes=16,094, failed=525, pending=7, settled_value_inr=21,527,718.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=22; trailing_median=14; z=2.7
- headline: success_rate=96.8; trailing_median=96.16; z=1.79
- products: product_name=UPI Lite; attempts=2,547; window_growth_pct=47.2; success_rate=99.14
- geography: region=South; attempts=4,865; success_rate=97.18; own_median=96.19; z=2.42
- products: product_name=UPI Person to Person; attempts=4,820; success_rate=96.08; own_median=95.16; z=2.05
- products: product_name=UPI Circle; attempts=768; window_growth_pct=35.8; success_rate=97.92
- products: product_name=UPI QR Payments; attempts=2,733; success_rate=97.33; own_median=96.56; z=2
- incidents: event_id=INC-BANK-0022; kind=bank_outage; severity=Sev-3; window=2026-07-08 to 2026-07-09; success_impact_pp=-5.53; volume_impact_pct=-4.91
- banks: payer_bank=Yes Bank; attempts=569; success_rate=97.89; own_median=96.1; z=2.26
- categories: mcc_category=Services; attempts=154; own_median=107; z=2.26

Refs: enterprise_data/warehouse/transactions, RPT-D184-DAILY, enterprise_data/warehouse/reference/incidents.parquet
