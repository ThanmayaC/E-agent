---
id: RPT-D153-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-06T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 06 Jun 2026)

**Report ID:** RPT-D153-DAILY · **Day 153 of 206** · **Derived from:** 18,644 transaction rows queried live from the warehouse

## Summary

The rail took **18,644 payment attempts** on Saturday 06 June 2026 (Weekend) and settled **₹2.37 Cr** across 18,037 successful payments. Volume was +17.2% on yesterday and +11.1% on the same weekday last week. Success closed at **96.74%**, above the trailing 28-day median of 96.15%.

App PhonePe carried 8,670 attempts, 26% up its trailing median and 46.5% of the day's volume. Attempt volume ran 3.0 standard deviations up its trailing 28-day median at 18,644, 11.1% up on the same weekday last week.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 18,644 | +17.2% | +11.1% | 16,000 |
| Successful payments | 18,037 | +17.2% | +11.5% | 15,454 |
| Success rate | 96.74% | +0.04pp | +0.32pp | 96.57% |
| Settled value | ₹2.37 Cr | +1.3% | +3.9% | ₹2.26 Cr |
| Average ticket | ₹1,315 | −13.6% | −6.8% | ₹1,466 |
| Technical declines | 0.375% | +0.08pp | −0.01pp | 0.351% |
| Business declines | 2.408% | −0.12pp | −0.32pp | 2.590% |
| Risk declines | 0.134% | +0.01pp | −0.00pp | 0.142% |
| Timeout declines | 0.263% | −0.03pp | +0.03pp | 0.251% |
| Retry share | 0.91% | +0.04pp | −0.02pp | 0.93% |
| Latency p95 | 1,234 ms | −1.4% | −2.2% | 1,276 ms |
| Active customers | 14,704 | +13.6% | +8.6% | 12,980 |
| Active merchants | 1,644 | +5.3% | +3.2% | 1,579 |

## What moved

- App PhonePe carried 8,670 attempts, 26% up its trailing median and 46.5% of the day's volume.
- Attempt volume ran 3.0 standard deviations up its trailing 28-day median at 18,644, 11.1% up on the same weekday last week.
- Region West carried 4,596 attempts, 28% up its trailing median and 24.7% of the day's volume.
- Region South carried 5,600 attempts, 31% up its trailing median and 30.0% of the day's volume.
- Category Bills carried 1,758 attempts, 93% up its trailing median and 13.2% of the day's volume.
- Product UPI QR Payments carried 3,502 attempts, 49% up its trailing median and 18.8% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,347 | 28.7% | 96.11% | ₹59.88 L | +23.1% |
| UPI Person to Merchant | 4,515 | 24.2% | 96.17% | ₹49.93 L | +16.5% |
| UPI QR Payments | 3,502 | 18.8% | 97.37% | ₹14.13 L | +49.0% |
| UPI Lite | 2,694 | 14.4% | 99.55% | ₹2.53 L | +50.3% |
| UPI Circle | 907 | 4.9% | 96.91% | ₹8.29 L | +41.1% |
| RuPay Credit on UPI | 404 | 2.2% | 95.54% | ₹19.89 L | +8.9% |
| Credit on UPI | 388 | 2.1% | 95.62% | ₹35.46 L | +2.9% |
| UPI AutoPay | 364 | 2.0% | 90.93% | ₹6.91 L | +6.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,850 | 96.72% | 96.05% | ₹76.81 L | normal |
| HDFC Bank | 2,077 | 96.53% | 96.37% | ₹25.75 L | normal |
| Bank of Baroda | 1,405 | 97.01% | 96.35% | ₹19.46 L | normal |
| Union Bank of India | 1,283 | 96.65% | 96.27% | ₹12.23 L | normal |
| ICICI Bank | 1,168 | 96.83% | 96.52% | ₹16.93 L | normal |
| Axis Bank | 1,162 | 96.21% | 96.61% | ₹12.83 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,670 | 96.56% | 96.21% | ₹1.15 Cr | normal |
| Google Pay | 6,173 | 96.81% | 96.07% | ₹74.49 L | normal |
| Paytm | 1,606 | 97.14% | 96.14% | ₹20.72 L | normal |
| Navi | 685 | 96.64% | 96.12% | ₹8.88 L | normal |
| SuperMoney | 370 | 96.22% | 96.38% | ₹4.47 L | normal |
| FamApp | 198 | 98.48% | 95.99% | ₹1.27 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,182 | 97.03% | ₹59.37 L |
| Food & Beverage | 3,213 | 97.51% | ₹14.65 L |
| Bills | 1,758 | 96.93% | ₹18.48 L |
| Mobility | 1,627 | 97.73% | ₹9.42 L |
| Healthcare | 626 | 97.12% | ₹7.16 L |
| Digital | 354 | 94.63% | ₹2.29 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,600 | 30.0% | 96.38% | ₹77.44 L |
| West | 4,596 | 24.7% | 96.76% | ₹63.89 L |
| North | 4,594 | 24.6% | 96.82% | ₹53.13 L |
| East | 2,193 | 11.8% | 97.22% | ₹27.12 L |
| Central | 1,661 | 8.9% | 97.11% | ₹15.61 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 83 | 95.18% | ₹2.85 L |
| Rapid Bazaar | Key Account | Retail | 548 | 97.81% | ₹2.17 L |
| Vega Electronics | Large | Retail | 22 | 100.00% | ₹2.11 L |
| Ujjwal Water Board | Key Account | Bills | 73 | 97.26% | ₹1.89 L |
| Urban Boutique | Key Account | Retail | 140 | 97.14% | ₹1.73 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 109 | 94.50% | ₹1.42 L |
| Girnar Connect | Key Account | Bills | 280 | 97.14% | ₹1.20 L |
| Hampi Stores 2298 | Key Account | Retail | 126 | 96.03% | ₹1.06 L |

## Failure analysis

Of 593 declined attempts, 449 were business declines (2.408% of attempts — balances, PINs and limits), 70 technical (0.375%), 49 timeouts (0.263%) and 25 risk declines (0.134%).

170 attempts were re-presentations of an earlier failure (0.91% of the day); 70.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 195 | 1.046% | 1.179% |
| ZM | Invalid UPI PIN | business | Customer | 148 | 0.794% | 0.949% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.279% | 0.346% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 29 | 0.156% | 0.146% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.139% | 0.194% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.139% | 0.208% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 23 | 0.123% | 0.108% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.097% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 104 | 105 |
| Auto-reversals | 25 | 26 |
| Disputes / chargebacks | 16 | 13 |
| Value returned | ₹1.70 L | ₹1.80 L |

## Customer behaviour

14,704 distinct customers transacted (+22.5% on the 28-day median) at 1.27 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,553 | 5,425 | 1.19 | 96.72% | ₹1,382 |
| power | 3,114 | 4,544 | 1.46 | 96.79% | ₹1,808 |
| merchant_heavy | 3,292 | 4,157 | 1.26 | 97.02% | ₹1,037 |
| small_ticket | 2,165 | 2,831 | 1.31 | 96.54% | ₹469 |
| occasional | 1,273 | 1,353 | 1.06 | 96.23% | ₹1,584 |
| new | 268 | 294 | 1.10 | 97.28% | ₹620 |
| dormant_returning | 39 | 40 | 1.03 | 95.00% | ₹1,084 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Product Credit on UPI is compounding — attempts up 31% across the trailing window to 388 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Circle is compounding — attempts up 38% across the trailing window to 907 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 06 June: success came in 0.59pp above baseline at 96.74% on 18,644 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-06` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=18,644, successes=18,037, failed=593, pending=14, settled_value_inr=23,718,847.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- psps: payer_psp=PhonePe; attempts=8,670; own_median=6,870.5; z=3.46
- headline: attempts=18,644; trailing_median=14,624; z=3.01
- geography: region=West; attempts=4,596; own_median=3,589; z=4.09
- geography: region=South; attempts=5,600; own_median=4,278.5; z=3.47
- categories: mcc_category=Bills; attempts=1,758; own_median=913; z=5.18
- products: product_name=UPI QR Payments; attempts=3,502; own_median=2,350.5; z=4.16
- psps: payer_psp=Google Pay; attempts=6,173; own_median=4,851; z=3.05
- headline: success_rate=96.74; trailing_median=96.15; z=1.61
- categories: mcc_category=Retail; attempts=5,182; own_median=4,136.5; z=2.7
- banks: payer_bank=State Bank of India; attempts=5,850; own_median=4,640.5; z=3

Refs: enterprise_data/warehouse/transactions, RPT-D152-DAILY, enterprise_data/warehouse/reference/incidents.parquet
