---
id: RPT-D106-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 20 Apr 2026)

**Report ID:** RPT-D106-DAILY · **Day 106 of 206** · **Derived from:** 15,910 transaction rows queried live from the warehouse

## Summary

The rail took **15,910 payment attempts** on Monday 20 April 2026 (Akshaya Tritiya) and settled **₹2.09 Cr** across 15,330 successful payments. Volume was +14.2% on yesterday and +35.9% on the same weekday last week. Success closed at **96.35%**, above the trailing 28-day median of 95.80%.

Category Retail carried 5,566 attempts, 73% up its trailing median and 53.7% of the day's volume. Product UPI Circle is compounding — attempts up 59% across the trailing window to 361 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,910 | +14.2% | +35.9% | 12,973 |
| Successful payments | 15,330 | +15.0% | +37.4% | 12,364 |
| Success rate | 96.35% | +0.72pp | +1.04pp | 95.26% |
| Settled value | ₹2.09 Cr | +35.3% | +22.3% | ₹1.65 Cr |
| Average ticket | ₹1,363 | +17.6% | −11.0% | ₹1,338 |
| Technical declines | 0.440% | +0.02pp | −0.11pp | 0.593% |
| Business declines | 2.671% | −0.72pp | −0.84pp | 3.134% |
| Risk declines | 0.119% | −0.01pp | −0.03pp | 0.144% |
| Timeout declines | 0.321% | +0.02pp | −0.05pp | 0.745% |
| Retry share | 0.97% | −0.21pp | −0.19pp | 1.73% |
| Latency p95 | 1,271 ms | +3.7% | −0.1% | 1,357 ms |
| Active customers | 12,785 | +11.4% | +28.5% | 10,724 |
| Active merchants | 1,480 | +4.5% | +7.9% | 1,389 |

## What moved

- Category Retail carried 5,566 attempts, 73% up its trailing median and 53.7% of the day's volume.
- Product UPI Circle is compounding — attempts up 59% across the trailing window to 361 today, with success holding, so the growth is healthy and worth funding.
- Attempt volume ran 2.5 standard deviations up its trailing 28-day median at 15,910, 35.9% up on the same weekday last week.
- Issuer State Bank of India carried 5,067 attempts, 27% up its trailing median and 31.8% of the day's volume.
- Region North carried 4,089 attempts, 30% up its trailing median and 25.7% of the day's volume.
- App Google Pay carried 5,381 attempts, 31% up its trailing median and 33.8% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,546 | 34.9% | 95.35% | ₹61.37 L | +27.6% |
| UPI Person to Merchant | 4,348 | 27.3% | 96.50% | ₹44.87 L | +27.2% |
| UPI QR Payments | 2,727 | 17.1% | 97.25% | ₹11.92 L | +28.2% |
| UPI Lite | 1,428 | 9.0% | 99.23% | ₹1.41 L | +34.3% |
| RuPay Credit on UPI | 419 | 2.6% | 94.51% | ₹22.81 L | +45.2% |
| UPI Circle | 361 | 2.3% | 98.34% | ₹2.84 L | +35.5% |
| Credit on UPI | 323 | 2.0% | 95.67% | ₹28.56 L | +64.8% |
| UPI AutoPay | 299 | 1.9% | 92.31% | ₹5.73 L | −7.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,067 | 96.61% | 95.83% | ₹74.81 L | normal |
| HDFC Bank | 1,789 | 95.92% | 96.04% | ₹21.65 L | normal |
| Bank of Baroda | 1,197 | 97.08% | 95.83% | ₹13.00 L | normal |
| Union Bank of India | 1,111 | 95.05% | 95.72% | ₹15.92 L | normal |
| Axis Bank | 981 | 95.92% | 95.62% | ₹13.73 L | normal |
| ICICI Bank | 973 | 97.23% | 95.91% | ₹10.25 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,384 | 96.59% | 95.78% | ₹89.49 L | normal |
| Google Pay | 5,381 | 96.30% | 95.59% | ₹70.02 L | normal |
| Paytm | 1,289 | 96.12% | 95.75% | ₹18.14 L | normal |
| Navi | 579 | 96.37% | 95.88% | ₹14.60 L | normal |
| SuperMoney | 300 | 94.33% | 94.46% | ₹2.82 L | normal |
| BHIM | 164 | 98.17% | 96.12% | ₹2.80 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,566 | 96.80% | ₹67.30 L |
| Food & Beverage | 2,020 | 97.92% | ₹10.45 L |
| Mobility | 914 | 97.59% | ₹4.66 L |
| Bills | 809 | 95.92% | ₹8.59 L |
| Healthcare | 433 | 96.77% | ₹4.34 L |
| Digital | 189 | 96.83% | ₹86,770 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,717 | 29.6% | 95.99% | ₹64.47 L |
| North | 4,089 | 25.7% | 96.58% | ₹56.39 L |
| West | 3,916 | 24.6% | 96.37% | ₹42.53 L |
| East | 1,821 | 11.4% | 96.49% | ₹23.07 L |
| Central | 1,367 | 8.6% | 96.71% | ₹22.49 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 52 | 98.08% | ₹3.14 L |
| Vasant Wardrobe | Key Account | Retail | 120 | 93.33% | ₹3.07 L |
| Rapid Bazaar | Key Account | Retail | 483 | 97.72% | ₹2.24 L |
| Hampi Stores 2298 | Key Account | Retail | 192 | 94.79% | ₹1.32 L |
| Urban Boutique | Key Account | Retail | 196 | 97.45% | ₹1.16 L |
| Girnar Connect | Key Account | Bills | 147 | 97.96% | ₹1.05 L |
| Kaveri Trading | Large | Retail | 100 | 97.00% | ₹1.05 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 84 | 98.81% | ₹93,735 |

## Failure analysis

Of 565 declined attempts, 425 were business declines (2.671% of attempts — balances, PINs and limits), 70 technical (0.440%), 51 timeouts (0.321%) and 19 risk declines (0.119%).

154 attempts were re-presentations of an earlier failure (0.97% of the day); 64.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 192 | 1.207% | 1.322% |
| ZM | Invalid UPI PIN | business | Customer | 131 | 0.823% | 1.030% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.308% | 0.378% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.195% | 0.193% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 28 | 0.176% | 0.183% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.163% | 0.220% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.119% | 0.103% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.101% | 0.117% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 80 | 78 |
| Auto-reversals | 26 | 22 |
| Disputes / chargebacks | 18 | 11 |
| Value returned | ₹1.04 L | ₹1.55 L |

## Customer behaviour

12,785 distinct customers transacted (+24.8% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,853 | 4,530 | 1.18 | 96.75% | ₹1,685 |
| power | 2,681 | 3,817 | 1.42 | 96.02% | ₹1,579 |
| merchant_heavy | 2,904 | 3,602 | 1.24 | 96.09% | ₹1,098 |
| small_ticket | 1,991 | 2,522 | 1.27 | 96.59% | ₹564 |
| occasional | 1,049 | 1,108 | 1.06 | 95.94% | ₹1,413 |
| new | 272 | 295 | 1.08 | 97.29% | ₹908 |
| dormant_returning | 35 | 36 | 1.03 | 97.22% | ₹571 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0062** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 59% across the trailing window to 361 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 39% across the trailing window to 1,428 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 20 April: success came in 0.56pp above baseline at 96.35% on 15,910 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,910, successes=15,330, failed=565, pending=15, settled_value_inr=20,894,916.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Retail; attempts=5,566; own_median=3,224.5; z=8.12
- products: product_name=UPI Circle; attempts=361; window_growth_pct=59.3; success_rate=98.34
- headline: attempts=15,910; trailing_median=12,448; z=2.55
- banks: payer_bank=State Bank of India; attempts=5,067; own_median=4,004; z=2.72
- geography: region=North; attempts=4,089; own_median=3,150; z=3.02
- psps: payer_psp=Google Pay; attempts=5,381; own_median=4,102; z=2.61
- products: product_name=UPI Lite; attempts=1,428; window_growth_pct=39.1; success_rate=99.23
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- geography: region=South; attempts=4,717; own_median=3,695.5; z=2.24
- products: product_name=UPI Person to Merchant; attempts=4,348; own_median=3,417.5; z=2.25

Refs: enterprise_data/warehouse/transactions, RPT-D105-DAILY, enterprise_data/warehouse/reference/incidents.parquet
