---
id: RPT-D151-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-04T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 04 Jun 2026)

**Report ID:** RPT-D151-DAILY · **Day 151 of 206** · **Derived from:** 14,624 transaction rows queried live from the warehouse

## Summary

The rail took **14,624 payment attempts** on Thursday 04 June 2026 (Working day) and settled **₹2.30 Cr** across 14,104 successful payments. Volume was −2.9% on yesterday and +10.1% on the same weekday last week. Success closed at **96.44%**, above the trailing 28-day median of 96.11%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,624 | −2.9% | +10.1% | 15,362 |
| Successful payments | 14,104 | −2.8% | +11.1% | 14,825 |
| Success rate | 96.44% | +0.13pp | +0.85pp | 96.50% |
| Settled value | ₹2.30 Cr | +9.5% | +26.0% | ₹2.21 Cr |
| Average ticket | ₹1,627 | +12.6% | +13.3% | ₹1,490 |
| Technical declines | 0.472% | +0.17pp | −0.08pp | 0.359% |
| Business declines | 2.557% | −0.31pp | −0.78pp | 2.651% |
| Risk declines | 0.164% | −0.00pp | +0.04pp | 0.150% |
| Timeout declines | 0.253% | −0.01pp | −0.05pp | 0.238% |
| Retry share | 1.05% | +0.17pp | −0.27pp | 0.95% |
| Latency p95 | 1,337 ms | +3.4% | +2.6% | 1,292 ms |
| Active customers | 12,015 | −3.1% | +7.8% | 12,558 |
| Active merchants | 1,555 | +0.6% | +3.5% | 1,567 |

## What moved

- Category Bills carried 1,480 attempts, 62% up its trailing median and 14.4% of the day's volume.
- Product UPI Circle is compounding — attempts up 37% across the trailing window to 688 today, with success holding, so the growth is healthy and worth funding.
- Settled value moved up while volume moved down — average ticket at ₹1,627 against a trailing ₹1,421, so the day's shape is a mix shift rather than a demand shift.
- Product Credit on UPI is compounding — attempts up 27% across the trailing window to 459 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,338 | 29.7% | 95.71% | ₹48.03 L | −0.6% |
| UPI Person to Merchant | 3,635 | 24.9% | 96.40% | ₹35.85 L | −7.0% |
| UPI QR Payments | 2,300 | 15.7% | 96.70% | ₹11.20 L | −3.0% |
| UPI Lite | 1,933 | 13.2% | 98.97% | ₹1.82 L | +8.3% |
| UPI Circle | 688 | 4.7% | 97.53% | ₹6.25 L | +13.5% |
| Credit on UPI | 459 | 3.1% | 96.95% | ₹57.51 L | +26.8% |
| RuPay Credit on UPI | 419 | 2.9% | 96.90% | ₹19.31 L | +12.9% |
| UPI AutoPay | 352 | 2.4% | 89.49% | ₹6.83 L | +3.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,626 | 96.39% | 96.05% | ₹75.08 L | normal |
| HDFC Bank | 1,587 | 96.79% | 96.32% | ₹24.84 L | normal |
| Bank of Baroda | 1,108 | 96.30% | 96.22% | ₹15.87 L | normal |
| Union Bank of India | 1,048 | 96.37% | 95.84% | ₹13.15 L | normal |
| Axis Bank | 911 | 96.38% | 96.52% | ₹10.38 L | normal |
| Punjab National Bank | 887 | 96.28% | 95.89% | ₹13.00 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,851 | 96.39% | 96.13% | ₹1.04 Cr | normal |
| Google Pay | 4,823 | 96.39% | 96.02% | ₹81.60 L | normal |
| Paytm | 1,193 | 96.56% | 96.14% | ₹18.64 L | normal |
| Navi | 533 | 97.56% | 95.98% | ₹11.23 L | normal |
| SuperMoney | 310 | 97.42% | 96.24% | ₹3.41 L | normal |
| BHIM | 156 | 94.87% | 95.96% | ₹1.61 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,020 | 96.92% | ₹51.39 L |
| Food & Beverage | 2,308 | 97.27% | ₹12.10 L |
| Bills | 1,480 | 95.81% | ₹14.08 L |
| Mobility | 1,175 | 97.79% | ₹6.79 L |
| Healthcare | 501 | 98.40% | ₹11.70 L |
| Digital | 324 | 97.53% | ₹2.19 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,323 | 29.6% | 96.72% | ₹77.99 L |
| West | 3,592 | 24.6% | 96.13% | ₹57.79 L |
| North | 3,588 | 24.5% | 96.88% | ₹55.81 L |
| East | 1,793 | 12.3% | 95.54% | ₹24.41 L |
| Central | 1,328 | 9.1% | 96.46% | ₹13.54 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 29 | 100.00% | ₹2.40 L |
| Rapid Bazaar | Key Account | Retail | 430 | 96.05% | ₹1.79 L |
| Vasant Wardrobe | Key Account | Retail | 79 | 94.94% | ₹1.44 L |
| Hampi Styles | Key Account | Retail | 36 | 97.22% | ₹1.41 L |
| Ujjwal Water Board | Key Account | Bills | 72 | 93.06% | ₹1.40 L |
| Hampi Stores 2298 | Key Account | Retail | 115 | 98.26% | ₹1.00 L |
| Girnar Connect | Key Account | Bills | 254 | 94.09% | ₹92,400 |
| Yamuna Restaurant | Key Account | Food & Beverage | 46 | 97.83% | ₹87,583 |

## Failure analysis

Of 504 declined attempts, 374 were business declines (2.557% of attempts — balances, PINs and limits), 69 technical (0.472%), 37 timeouts (0.253%) and 24 risk declines (0.164%).

154 attempts were re-presentations of an earlier failure (1.05% of the day); 67.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 149 | 1.019% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 120 | 0.821% | 0.949% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.349% | 0.346% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.212% | 0.198% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.191% | 0.211% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.144% | 0.108% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.144% | 0.147% |
| UX | Mandate execution outside permitted window | business | PSP | 20 | 0.137% | 0.073% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 105 | 104 |
| Auto-reversals | 22 | 26 |
| Disputes / chargebacks | 14 | 13 |
| Value returned | ₹2.14 L | ₹1.88 L |

## Customer behaviour

12,015 distinct customers transacted (−0.1% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,655 | 4,181 | 1.14 | 95.81% | ₹1,850 |
| power | 2,608 | 3,585 | 1.37 | 97.07% | ₹2,132 |
| merchant_heavy | 2,822 | 3,443 | 1.22 | 96.46% | ₹1,306 |
| small_ticket | 1,771 | 2,191 | 1.24 | 96.62% | ₹546 |
| occasional | 926 | 978 | 1.06 | 95.91% | ₹1,757 |
| new | 206 | 218 | 1.06 | 98.17% | ₹695 |
| dormant_returning | 27 | 28 | 1.04 | 100.00% | ₹454 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **INC-BANK-0014** (Sev-3) — Punjab National Bank issuer decline spike, scoped to Punjab National Bank between 19:00 and 23:00. Punjab National Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 37% across the trailing window to 688 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 27% across the trailing window to 459 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

04 June ran on trend at 96.44% success and ₹2.30 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 1,480 attempts, 62% up its trailing median and 14.4% of the day's volume. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-04` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,624, successes=14,104, failed=504, pending=16, settled_value_inr=22,953,038.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,480; own_median=913; z=3.71
- products: product_name=UPI Circle; attempts=688; window_growth_pct=37.1; success_rate=97.53
- headline: value_inr=22,953,038; avg_ticket=1,627.41; trailing_avg_ticket=1,421.03
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=Credit on UPI; attempts=459; window_growth_pct=26.9; success_rate=96.95
- banks: payer_bank=Kotak Mahindra Bank; attempts=521; success_rate=98.85; own_median=95.95; z=3.86
- incidents: event_id=INC-BANK-0014; kind=bank_outage; severity=Sev-3; window=2026-06-04 to 2026-06-05; success_impact_pp=-6.03; volume_impact_pct=-5.34
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- categories: mcc_category=Digital; attempts=324; own_median=222; z=2.6

Refs: enterprise_data/warehouse/transactions, RPT-D150-DAILY, enterprise_data/warehouse/reference/incidents.parquet
