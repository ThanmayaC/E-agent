---
id: RPT-D156-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-09T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 09 Jun 2026)

**Report ID:** RPT-D156-DAILY · **Day 156 of 206** · **Derived from:** 14,201 transaction rows queried live from the warehouse

## Summary

The rail took **14,201 payment attempts** on Tuesday 09 June 2026 (Working day) and settled **₹1.88 Cr** across 13,660 successful payments. Volume was −13.0% on yesterday and −9.1% on the same weekday last week. Success closed at **96.19%**, in line with the trailing 28-day median of 96.21%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,201 | −13.0% | −9.1% | 15,749 |
| Successful payments | 13,660 | −13.2% | −9.4% | 15,198 |
| Success rate | 96.19% | −0.26pp | −0.37pp | 96.49% |
| Settled value | ₹1.88 Cr | −18.9% | −14.1% | ₹2.17 Cr |
| Average ticket | ₹1,378 | −6.6% | −5.1% | ₹1,432 |
| Technical declines | 0.451% | −0.07pp | +0.12pp | 0.389% |
| Business declines | 2.852% | +0.33pp | +0.23pp | 2.630% |
| Risk declines | 0.099% | −0.01pp | −0.04pp | 0.128% |
| Timeout declines | 0.310% | −0.04pp | +0.05pp | 0.270% |
| Retry share | 1.18% | +0.17pp | +0.15pp | 0.97% |
| Latency p95 | 1,293 ms | −1.4% | +1.4% | 1,274 ms |
| Active customers | 11,721 | −11.0% | −7.6% | 12,808 |
| Active merchants | 1,510 | −4.9% | −3.0% | 1,569 |

## What moved

- Issuer Axis Bank ran at 93.95% success on 827 attempts (5.8% of the day), 2.66pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 29% across the trailing window to 521 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,136 | 29.1% | 95.14% | ₹45.35 L | −6.1% |
| UPI Person to Merchant | 3,520 | 24.8% | 96.28% | ₹35.01 L | −10.0% |
| UPI QR Payments | 2,259 | 15.9% | 97.03% | ₹10.00 L | −6.2% |
| UPI Lite | 1,933 | 13.6% | 98.91% | ₹1.81 L | +2.8% |
| UPI Circle | 632 | 4.5% | 96.20% | ₹5.62 L | −7.4% |
| Credit on UPI | 521 | 3.7% | 95.97% | ₹34.78 L | +35.5% |
| UPI AutoPay | 396 | 2.8% | 89.65% | ₹7.31 L | +15.3% |
| RuPay Credit on UPI | 347 | 2.4% | 96.83% | ₹16.11 L | −7.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,449 | 96.31% | 96.11% | ₹61.47 L | normal |
| HDFC Bank | 1,593 | 96.74% | 96.41% | ₹19.62 L | normal |
| Bank of Baroda | 1,140 | 96.58% | 96.45% | ₹13.62 L | normal |
| Union Bank of India | 1,028 | 94.84% | 96.38% | ₹9.30 L | ⚠ outlier |
| Punjab National Bank | 909 | 95.38% | 96.26% | ₹13.67 L | normal |
| Axis Bank | 827 | 93.95% | 96.61% | ₹11.01 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,819 | 96.14% | 96.21% | ₹89.55 L | normal |
| Google Pay | 4,546 | 96.44% | 96.09% | ₹62.80 L | normal |
| Paytm | 1,177 | 95.75% | 96.19% | ₹14.59 L | normal |
| Navi | 526 | 95.44% | 96.23% | ₹5.57 L | normal |
| SuperMoney | 264 | 96.21% | 96.38% | ₹3.70 L | normal |
| BHIM | 158 | 96.20% | 95.69% | ₹2.08 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,454 | 96.88% | ₹60.94 L |
| Food & Beverage | 2,401 | 97.17% | ₹12.00 L |
| Mobility | 1,146 | 97.82% | ₹6.24 L |
| Bills | 827 | 95.41% | ₹8.15 L |
| Healthcare | 530 | 96.42% | ₹6.25 L |
| Digital | 222 | 94.14% | ₹1.22 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,249 | 29.9% | 96.19% | ₹62.12 L |
| North | 3,516 | 24.8% | 96.02% | ₹41.90 L |
| West | 3,460 | 24.4% | 96.24% | ₹45.66 L |
| East | 1,639 | 11.5% | 96.89% | ₹21.82 L |
| Central | 1,337 | 9.4% | 95.66% | ₹16.76 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 475 | 98.74% | ₹2.25 L |
| Vega Electronics | Large | Retail | 36 | 88.89% | ₹1.97 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 100.00% | ₹1.85 L |
| Hampi Stores 2298 | Key Account | Retail | 118 | 94.92% | ₹1.31 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 85 | 97.65% | ₹1.13 L |
| Girnar Connect | Key Account | Bills | 159 | 94.34% | ₹87,474 |
| Ujjwal Water Board | Key Account | Bills | 39 | 84.62% | ₹58,156 |
| Tejas Bites | Key Account | Food & Beverage | 189 | 96.30% | ₹57,134 |

## Failure analysis

Of 527 declined attempts, 405 were business declines (2.852% of attempts — balances, PINs and limits), 64 technical (0.451%), 44 timeouts (0.310%) and 14 risk declines (0.099%).

167 attempts were re-presentations of an earlier failure (1.18% of the day); 61.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 163 | 1.148% | 1.171% |
| ZM | Invalid UPI PIN | business | Customer | 131 | 0.922% | 0.904% |
| ZA | Transaction declined by customer | business | Customer | 59 | 0.415% | 0.343% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.183% | 0.207% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.183% | 0.194% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.176% | 0.146% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.106% | 0.115% |
| UX | Mandate execution outside permitted window | business | PSP | 15 | 0.106% | 0.069% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 118 | 106 |
| Auto-reversals | 32 | 25 |
| Disputes / chargebacks | 13 | 13 |
| Value returned | ₹2.49 L | ₹1.80 L |

## Customer behaviour

11,721 distinct customers transacted (−2.8% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,562 | 4,087 | 1.15 | 95.79% | ₹1,402 |
| power | 2,604 | 3,508 | 1.35 | 96.04% | ₹1,856 |
| merchant_heavy | 2,610 | 3,160 | 1.21 | 96.74% | ₹1,058 |
| small_ticket | 1,746 | 2,184 | 1.25 | 96.02% | ₹621 |
| occasional | 937 | 979 | 1.04 | 96.63% | ₹1,718 |
| new | 231 | 250 | 1.08 | 97.60% | ₹702 |
| dormant_returning | 31 | 33 | 1.06 | 96.97% | ₹894 |

## Operational events

- **INC-BANK-0002** (Sev-2) — Yes Bank issuer decline spike, scoped to Yes Bank between 01:00 and 08:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-BANK-0007** (Sev-2) — Punjab National Bank issuer decline spike, scoped to Punjab National Bank between 19:00 and 22:00. Punjab National Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **REG-0071** (Sev-2) — MDR reinstated on RuPay Credit above ₹2,000, scoped to RUPAY_CREDIT. Merchant discount rate reinstated on higher-value RuPay Credit transactions. Large-ticket volume moved back to debit-funded rails; the product's average ticket falls.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Issuer Axis Bank ran at 93.95% success on 827 attempts (5.8% of the day), 2.66pp down its own 28-day median.
- Issuer Union Bank of India ran at 94.84% success on 1,028 attempts (7.2% of the day), 1.54pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 29% across the trailing window to 521 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

09 June was an incident day: INC-BANK-0002, INC-BANK-0007 were live and the rail closed at 96.19% success against a 96.21% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-09` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,201, successes=13,660, failed=527, pending=14, settled_value_inr=18,826,806.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0002; kind=bank_outage; severity=Sev-2; window=2026-06-08 to 2026-06-10; success_impact_pp=-19.67; volume_impact_pct=-17.45
- incidents: event_id=INC-BANK-0007; kind=bank_outage; severity=Sev-2; window=2026-06-08 to 2026-06-09; success_impact_pp=-15.67; volume_impact_pct=-13.9
- banks: payer_bank=Axis Bank; attempts=827; success_rate=93.95; own_median=96.61; z=-5.08
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- incidents: event_id=REG-0071; kind=pricing_change; severity=Sev-2; window=2026-06-08 to 2026-07-29; success_impact_pp=0.1; volume_impact_pct=-17
- products: product_name=Credit on UPI; attempts=521; window_growth_pct=29.1; success_rate=95.97
- banks: payer_bank=Union Bank of India; attempts=1,028; success_rate=94.84; own_median=96.38; z=-2.15
- banks: payer_bank=IndusInd Bank; attempts=287; success_rate=99.3; own_median=96.44; z=3.05
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5

Refs: enterprise_data/warehouse/transactions, RPT-D155-DAILY, enterprise_data/warehouse/reference/incidents.parquet
