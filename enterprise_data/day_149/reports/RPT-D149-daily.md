---
id: RPT-D149-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-02T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 02 Jun 2026)

**Report ID:** RPT-D149-DAILY · **Day 149 of 206** · **Derived from:** 15,620 transaction rows queried live from the warehouse

## Summary

The rail took **15,620 payment attempts** on Tuesday 02 June 2026 (Working day) and settled **₹2.19 Cr** across 15,083 successful payments. Volume was −3.2% on yesterday and +6.6% on the same weekday last week. Success closed at **96.56%**, above the trailing 28-day median of 96.09%.

App PhonePe ran at 96.82% success on 7,388 attempts (47.3% of the day), 0.70pp up its own 28-day median. Category Bills carried 1,652 attempts, 81% up its trailing median and 15.1% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,620 | −3.2% | +6.6% | 15,880 |
| Successful payments | 15,083 | −3.3% | +7.1% | 15,343 |
| Success rate | 96.56% | −0.12pp | +0.48pp | 96.62% |
| Settled value | ₹2.19 Cr | −2.1% | +22.4% | ₹2.21 Cr |
| Average ticket | ₹1,453 | +1.3% | +14.3% | ₹1,444 |
| Technical declines | 0.327% | −0.01pp | −0.16pp | 0.334% |
| Business declines | 2.618% | +0.06pp | −0.25pp | 2.589% |
| Risk declines | 0.141% | +0.01pp | +0.00pp | 0.135% |
| Timeout declines | 0.256% | +0.07pp | −0.02pp | 0.221% |
| Retry share | 1.02% | +0.18pp | −0.16pp | 0.93% |
| Latency p95 | 1,275 ms | +0.9% | +2.5% | 1,270 ms |
| Active customers | 12,684 | −3.5% | +5.8% | 12,911 |
| Active merchants | 1,557 | −3.4% | +2.3% | 1,584 |

## What moved

- App PhonePe ran at 96.82% success on 7,388 attempts (47.3% of the day), 0.70pp up its own 28-day median.
- Category Bills carried 1,652 attempts, 81% up its trailing median and 15.1% of the day's volume.
- Region West ran at 96.91% success on 3,819 attempts (24.4% of the day), 0.87pp up its own 28-day median.
- Product UPI Circle is compounding — attempts up 37% across the trailing window to 726 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,652 | 29.8% | 95.70% | ₹52.74 L | +6.6% |
| UPI Person to Merchant | 4,090 | 26.2% | 95.97% | ₹41.15 L | +4.7% |
| UPI QR Payments | 2,354 | 15.1% | 97.32% | ₹10.19 L | −2.2% |
| UPI Lite | 1,953 | 12.5% | 99.08% | ₹1.82 L | +12.0% |
| UPI Circle | 726 | 4.6% | 98.21% | ₹7.17 L | +20.9% |
| Credit on UPI | 531 | 3.4% | 96.61% | ₹45.10 L | +49.4% |
| RuPay Credit on UPI | 502 | 3.2% | 96.81% | ₹24.37 L | +36.0% |
| UPI AutoPay | 352 | 2.3% | 94.03% | ₹7.28 L | +4.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,010 | 96.43% | 96.04% | ₹75.24 L | normal |
| HDFC Bank | 1,711 | 96.90% | 96.23% | ₹20.40 L | ⚠ outlier |
| Bank of Baroda | 1,213 | 96.78% | 96.14% | ₹16.96 L | normal |
| Union Bank of India | 1,052 | 96.39% | 95.72% | ₹13.44 L | normal |
| Punjab National Bank | 965 | 97.10% | 95.89% | ₹16.26 L | normal |
| Axis Bank | 950 | 97.47% | 96.52% | ₹9.08 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,388 | 96.82% | 96.12% | ₹1.10 Cr | ⚠ outlier |
| Google Pay | 5,148 | 96.33% | 95.98% | ₹71.34 L | normal |
| Paytm | 1,209 | 96.36% | 96.15% | ₹15.56 L | normal |
| Navi | 585 | 96.58% | 95.71% | ₹7.86 L | normal |
| SuperMoney | 312 | 96.47% | 96.24% | ₹4.27 L | normal |
| BHIM | 157 | 95.54% | 95.96% | ₹1.78 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,307 | 97.00% | ₹56.79 L |
| Food & Beverage | 2,485 | 97.55% | ₹14.06 L |
| Bills | 1,652 | 96.31% | ₹19.68 L |
| Mobility | 1,179 | 97.79% | ₹8.14 L |
| Healthcare | 551 | 97.64% | ₹7.82 L |
| Digital | 315 | 94.29% | ₹1.66 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,597 | 29.4% | 96.32% | ₹65.30 L |
| North | 3,937 | 25.2% | 96.47% | ₹52.14 L |
| West | 3,819 | 24.4% | 96.91% | ₹59.42 L |
| East | 1,943 | 12.4% | 96.55% | ₹25.54 L |
| Central | 1,324 | 8.5% | 96.68% | ₹16.76 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 46 | 95.65% | ₹3.23 L |
| Vasant Wardrobe | Key Account | Retail | 83 | 97.59% | ₹2.45 L |
| Rapid Bazaar | Key Account | Retail | 405 | 98.02% | ₹1.94 L |
| Ujjwal Water Board | Key Account | Bills | 91 | 93.41% | ₹1.61 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 83 | 93.98% | ₹1.18 L |
| Kaveri Trading | Large | Retail | 65 | 96.92% | ₹1.05 L |
| Girnar Connect | Key Account | Bills | 265 | 97.36% | ₹1.03 L |
| Swift Grill | Large | Food & Beverage | 42 | 95.24% | ₹81,086 |

## Failure analysis

Of 522 declined attempts, 409 were business declines (2.618% of attempts — balances, PINs and limits), 51 technical (0.327%), 40 timeouts (0.256%) and 22 risk declines (0.141%).

160 attempts were re-presentations of an earlier failure (1.02% of the day); 69.4% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 170 | 1.088% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 0.864% | 0.970% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.301% | 0.351% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.205% | 0.217% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.147% | 0.148% |
| U30 | Debit failed at remitter bank | technical | Issuer | 17 | 0.109% | 0.202% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.096% | 0.106% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.096% | 0.129% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 101 | 104 |
| Auto-reversals | 21 | 27 |
| Disputes / chargebacks | 11 | 13 |
| Value returned | ₹1.51 L | ₹1.98 L |

## Customer behaviour

12,684 distinct customers transacted (+5.5% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,922 | 4,588 | 1.17 | 96.80% | ₹1,416 |
| power | 2,757 | 3,847 | 1.40 | 95.92% | ₹2,061 |
| merchant_heavy | 2,862 | 3,436 | 1.20 | 96.65% | ₹1,156 |
| small_ticket | 1,911 | 2,441 | 1.28 | 96.60% | ₹595 |
| occasional | 1,009 | 1,064 | 1.05 | 97.27% | ₹1,663 |
| new | 198 | 219 | 1.11 | 97.26% | ₹1,120 |
| dormant_returning | 25 | 25 | 1.00 | 100.00% | ₹2,099 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0087** (Sev-3) — Union Bank of India scheduled CBS maintenance, scoped to Union Bank of India between 01:00 and 05:00. Union Bank of India runs its announced core-banking maintenance slot every 35 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 37% across the trailing window to 726 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 02 June: success came in 0.47pp above baseline at 96.56% on 15,620 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-02` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,620, successes=15,083, failed=522, pending=15, settled_value_inr=21,916,297.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- psps: payer_psp=PhonePe; attempts=7,388; success_rate=96.82; own_median=96.12; z=2.79
- categories: mcc_category=Bills; attempts=1,652; own_median=913; z=4.84
- geography: region=West; attempts=3,819; success_rate=96.91; own_median=96.04; z=2.23
- products: product_name=UPI Circle; attempts=726; window_growth_pct=36.7; success_rate=98.21
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- incidents: event_id=MAINT-0087; kind=maintenance_window; severity=Sev-3; window=2026-01-13 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- banks: payer_bank=HDFC Bank; attempts=1,711; success_rate=96.9; own_median=96.23; z=2.01
- products: product_name=RuPay Credit on UPI; attempts=502; own_median=369; z=3.2
- products: product_name=Credit on UPI; attempts=531; own_median=355.5; z=2.72
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27

Refs: enterprise_data/warehouse/transactions, RPT-D148-DAILY, enterprise_data/warehouse/reference/incidents.parquet
