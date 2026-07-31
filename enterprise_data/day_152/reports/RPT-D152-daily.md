---
id: RPT-D152-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 05 Jun 2026)

**Report ID:** RPT-D152-DAILY · **Day 152 of 206** · **Derived from:** 15,909 transaction rows queried live from the warehouse

## Summary

The rail took **15,909 payment attempts** on Friday 05 June 2026 (Working day) and settled **₹2.34 Cr** across 15,385 successful payments. Volume was +8.8% on yesterday and +20.0% on the same weekday last week. Success closed at **96.71%**, above the trailing 28-day median of 96.13%.

Region South ran at 97.17% success on 4,743 attempts (29.8% of the day), 0.99pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,909 | +8.8% | +20.0% | 15,471 |
| Successful payments | 15,385 | +9.1% | +20.8% | 14,937 |
| Success rate | 96.71% | +0.26pp | +0.64pp | 96.54% |
| Settled value | ₹2.34 Cr | +2.0% | +29.5% | ₹2.23 Cr |
| Average ticket | ₹1,522 | −6.5% | +7.2% | ₹1,496 |
| Technical declines | 0.295% | −0.18pp | −0.29pp | 0.347% |
| Business declines | 2.527% | −0.03pp | −0.30pp | 2.626% |
| Risk declines | 0.119% | −0.04pp | +0.01pp | 0.144% |
| Timeout declines | 0.289% | +0.04pp | −0.07pp | 0.249% |
| Retry share | 0.87% | −0.18pp | −0.51pp | 0.94% |
| Latency p95 | 1,251 ms | −6.4% | −1.4% | 1,284 ms |
| Active customers | 12,946 | +7.7% | +17.0% | 12,635 |
| Active merchants | 1,561 | +0.4% | +3.9% | 1,566 |

## What moved

- Region South ran at 97.17% success on 4,743 attempts (29.8% of the day), 0.99pp up its own 28-day median.
- Success rate closed at 96.71%, 0.58pp up the trailing median — a 1.6-sigma move.
- Category Bills carried 1,571 attempts, 72% up its trailing median and 14.4% of the day's volume.
- Product UPI Circle is compounding — attempts up 41% across the trailing window to 706 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 31% across the trailing window to 452 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite ran at 99.30% success on 2,009 attempts (12.6% of the day), 0.33pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,978 | 31.3% | 96.00% | ₹55.83 L | +14.6% |
| UPI Person to Merchant | 3,979 | 25.0% | 96.93% | ₹41.47 L | +2.7% |
| UPI QR Payments | 2,496 | 15.7% | 96.83% | ₹11.49 L | +6.2% |
| UPI Lite | 2,009 | 12.6% | 99.30% | ₹1.79 L | +12.0% |
| UPI Circle | 706 | 4.4% | 97.03% | ₹6.95 L | +15.7% |
| RuPay Credit on UPI | 458 | 2.9% | 95.85% | ₹30.73 L | +23.5% |
| Credit on UPI | 452 | 2.8% | 96.02% | ₹45.92 L | +21.3% |
| UPI AutoPay | 347 | 2.2% | 93.37% | ₹6.32 L | +1.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,947 | 96.60% | 96.05% | ₹65.92 L | normal |
| HDFC Bank | 1,764 | 96.37% | 96.39% | ₹22.64 L | normal |
| Bank of Baroda | 1,210 | 97.19% | 96.26% | ₹17.12 L | normal |
| Union Bank of India | 1,119 | 96.51% | 96.03% | ₹16.70 L | normal |
| Axis Bank | 970 | 96.91% | 96.52% | ₹10.76 L | normal |
| ICICI Bank | 968 | 96.90% | 96.52% | ₹20.18 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,474 | 96.56% | 96.17% | ₹1.09 Cr | normal |
| Google Pay | 5,253 | 96.65% | 96.07% | ₹78.82 L | normal |
| Paytm | 1,306 | 97.09% | 96.14% | ₹22.34 L | normal |
| Navi | 567 | 97.18% | 95.98% | ₹6.96 L | normal |
| SuperMoney | 322 | 96.89% | 96.36% | ₹3.39 L | normal |
| BHIM | 176 | 94.32% | 95.69% | ₹2.84 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,311 | 97.10% | ₹60.04 L |
| Food & Beverage | 2,497 | 97.56% | ₹14.70 L |
| Bills | 1,571 | 97.07% | ₹19.61 L |
| Mobility | 1,242 | 97.34% | ₹7.40 L |
| Healthcare | 526 | 98.10% | ₹6.37 L |
| Digital | 318 | 96.54% | ₹1.64 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,743 | 29.8% | 97.17% | ₹75.12 L |
| North | 3,945 | 24.8% | 96.32% | ₹53.94 L |
| West | 3,924 | 24.7% | 96.69% | ₹63.24 L |
| East | 1,916 | 12.0% | 96.45% | ₹26.19 L |
| Central | 1,381 | 8.7% | 96.60% | ₹15.59 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 40 | 100.00% | ₹3.40 L |
| Vasant Wardrobe | Key Account | Retail | 77 | 98.70% | ₹1.81 L |
| Rapid Bazaar | Key Account | Retail | 387 | 97.93% | ₹1.54 L |
| Ujjwal Water Board | Key Account | Bills | 82 | 95.12% | ₹1.53 L |
| Girnar Connect | Key Account | Bills | 269 | 98.51% | ₹1.27 L |
| Kaveri Trading | Large | Retail | 58 | 96.55% | ₹1.17 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 85 | 98.82% | ₹1.13 L |
| Tejas Restaurant | Large | Food & Beverage | 29 | 100.00% | ₹1.12 L |

## Failure analysis

Of 514 declined attempts, 402 were business declines (2.527% of attempts — balances, PINs and limits), 47 technical (0.295%), 46 timeouts (0.289%) and 19 risk declines (0.119%).

139 attempts were re-presentations of an earlier failure (0.87% of the day); 64.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 181 | 1.138% | 1.179% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 0.855% | 0.949% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.277% | 0.348% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 28 | 0.176% | 0.146% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.113% | 0.108% |
| U30 | Debit failed at remitter bank | technical | Issuer | 17 | 0.107% | 0.198% |
| XH | Account does not exist / frozen | business | Issuer | 16 | 0.101% | 0.211% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.088% | 0.120% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 116 | 104 |
| Auto-reversals | 20 | 26 |
| Disputes / chargebacks | 9 | 13 |
| Value returned | ₹1.39 L | ₹1.88 L |

## Customer behaviour

12,946 distinct customers transacted (+7.8% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,056 | 4,687 | 1.16 | 96.69% | ₹1,542 |
| power | 2,705 | 3,765 | 1.39 | 96.84% | ₹2,260 |
| merchant_heavy | 2,880 | 3,550 | 1.23 | 96.93% | ₹1,137 |
| small_ticket | 1,996 | 2,518 | 1.26 | 96.27% | ₹633 |
| occasional | 1,036 | 1,098 | 1.06 | 96.72% | ₹1,497 |
| new | 235 | 252 | 1.07 | 95.63% | ₹1,480 |
| dormant_returning | 38 | 39 | 1.03 | 100.00% | ₹748 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **INC-BANK-0014** (Sev-3) — Punjab National Bank issuer decline spike, scoped to Punjab National Bank between 19:00 and 23:00. Punjab National Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 41% across the trailing window to 706 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 31% across the trailing window to 452 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 05 June: success came in 0.58pp above baseline at 96.71% on 15,909 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,909, successes=15,385, failed=514, pending=10, settled_value_inr=23,408,457.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- geography: region=South; attempts=4,743; success_rate=97.17; own_median=96.19; z=3.03
- headline: success_rate=96.71; trailing_median=96.13; z=1.6
- categories: mcc_category=Bills; attempts=1,571; own_median=913; z=4.31
- products: product_name=UPI Circle; attempts=706; window_growth_pct=40.9; success_rate=97.03
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=Credit on UPI; attempts=452; window_growth_pct=30.8; success_rate=96.02
- products: product_name=UPI Lite; attempts=2,009; success_rate=99.3; own_median=98.97; z=2.08
- incidents: event_id=INC-BANK-0014; kind=bank_outage; severity=Sev-3; window=2026-06-04 to 2026-06-05; success_impact_pp=-6.03; volume_impact_pct=-5.34
- banks: payer_bank=Kotak Mahindra Bank; attempts=545; success_rate=98.17; own_median=95.95; z=2.2
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27

Refs: enterprise_data/warehouse/transactions, RPT-D151-DAILY, enterprise_data/warehouse/reference/incidents.parquet
