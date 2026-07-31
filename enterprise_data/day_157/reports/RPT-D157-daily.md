---
id: RPT-D157-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 10 Jun 2026)

**Report ID:** RPT-D157-DAILY · **Day 157 of 206** · **Derived from:** 13,837 transaction rows queried live from the warehouse

## Summary

The rail took **13,837 payment attempts** on Wednesday 10 June 2026 (Working day) and settled **₹1.97 Cr** across 13,334 successful payments. Volume was −2.6% on yesterday and −8.2% on the same weekday last week. Success closed at **96.36%**, in line with the trailing 28-day median of 96.21%.

Region South ran at 96.84% success on 4,017 attempts (29.0% of the day), 0.57pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,837 | −2.6% | −8.2% | 15,558 |
| Successful payments | 13,334 | −2.4% | −8.1% | 15,012 |
| Success rate | 96.36% | +0.17pp | +0.06pp | 96.48% |
| Settled value | ₹1.97 Cr | +4.9% | −5.8% | ₹2.15 Cr |
| Average ticket | ₹1,481 | +7.4% | +2.5% | ₹1,437 |
| Technical declines | 0.289% | −0.16pp | −0.01pp | 0.379% |
| Business declines | 2.884% | +0.03pp | +0.02pp | 2.655% |
| Risk declines | 0.173% | +0.07pp | +0.01pp | 0.132% |
| Timeout declines | 0.202% | −0.11pp | −0.06pp | 0.264% |
| Retry share | 1.13% | −0.04pp | +0.25pp | 0.98% |
| Latency p95 | 1,267 ms | −2.0% | −2.0% | 1,273 ms |
| Active customers | 11,558 | −1.4% | −6.7% | 12,683 |
| Active merchants | 1,525 | +1.0% | −1.4% | 1,564 |

## What moved

- Region South ran at 96.84% success on 4,017 attempts (29.0% of the day), 0.57pp up its own 28-day median.
- Product Credit on UPI is compounding — attempts up 28% across the trailing window to 518 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,884 | 28.1% | 95.52% | ₹40.96 L | −11.8% |
| UPI Person to Merchant | 3,416 | 24.7% | 96.49% | ₹35.58 L | −11.8% |
| UPI QR Payments | 2,121 | 15.3% | 96.23% | ₹9.47 L | −11.9% |
| UPI Lite | 2,048 | 14.8% | 98.83% | ₹1.88 L | +7.3% |
| UPI Circle | 643 | 4.6% | 98.13% | ₹5.66 L | −5.8% |
| Credit on UPI | 518 | 3.7% | 96.53% | ₹50.06 L | +33.7% |
| RuPay Credit on UPI | 404 | 2.9% | 96.53% | ₹18.02 L | +7.9% |
| UPI AutoPay | 351 | 2.5% | 89.46% | ₹5.69 L | +2.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,282 | 96.68% | 96.13% | ₹62.21 L | normal |
| HDFC Bank | 1,488 | 96.24% | 96.42% | ₹23.29 L | normal |
| Bank of Baroda | 1,108 | 96.21% | 96.51% | ₹12.47 L | normal |
| Union Bank of India | 984 | 96.44% | 96.38% | ₹10.91 L | normal |
| ICICI Bank | 872 | 95.76% | 96.68% | ₹10.42 L | normal |
| Axis Bank | 855 | 96.14% | 96.52% | ₹9.64 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,445 | 96.06% | 96.21% | ₹89.51 L | normal |
| Google Pay | 4,634 | 96.40% | 96.18% | ₹71.45 L | normal |
| Paytm | 1,176 | 96.85% | 96.12% | ₹13.29 L | normal |
| Navi | 501 | 97.80% | 96.19% | ₹8.79 L | normal |
| SuperMoney | 218 | 96.33% | 96.26% | ₹2.93 L | normal |
| BHIM | 123 | 95.93% | 95.96% | ₹1.13 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,232 | 97.02% | ₹56.93 L |
| Food & Beverage | 2,431 | 97.70% | ₹12.81 L |
| Mobility | 1,167 | 97.34% | ₹6.32 L |
| Bills | 882 | 95.92% | ₹9.01 L |
| Healthcare | 562 | 96.62% | ₹11.89 L |
| Digital | 221 | 90.95% | ₹84,052 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,017 | 29.0% | 96.84% | ₹55.46 L |
| North | 3,504 | 25.3% | 96.60% | ₹49.48 L |
| West | 3,458 | 25.0% | 95.78% | ₹58.16 L |
| East | 1,599 | 11.6% | 96.56% | ₹19.31 L |
| Central | 1,259 | 9.1% | 95.55% | ₹15.05 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 96.77% | ₹2.93 L |
| Rapid Bazaar | Key Account | Retail | 393 | 97.20% | ₹1.62 L |
| Hampi Styles | Key Account | Retail | 46 | 95.65% | ₹1.48 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 97.06% | ₹1.39 L |
| Ujjwal Water Board | Key Account | Bills | 42 | 100.00% | ₹96,098 |
| Hampi Stores 2298 | Key Account | Retail | 113 | 97.35% | ₹81,394 |
| Urban Boutique | Key Account | Retail | 98 | 100.00% | ₹69,340 |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 94.52% | ₹61,447 |

## Failure analysis

Of 491 declined attempts, 399 were business declines (2.884% of attempts — balances, PINs and limits), 40 technical (0.289%), 28 timeouts (0.202%) and 24 risk declines (0.173%).

157 attempts were re-presentations of an earlier failure (1.13% of the day); 65.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 168 | 1.214% | 1.158% |
| ZM | Invalid UPI PIN | business | Customer | 133 | 0.961% | 0.904% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.376% | 0.346% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.210% | 0.205% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.145% | 0.111% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.116% | 0.115% |
| U30 | Debit failed at remitter bank | technical | Issuer | 14 | 0.101% | 0.194% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 12 | 0.087% | 0.146% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 116 | 106 |
| Auto-reversals | 20 | 26 |
| Disputes / chargebacks | 11 | 13 |
| Value returned | ₹1.64 L | ₹1.88 L |

## Customer behaviour

11,558 distinct customers transacted (−4.1% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,585 | 4,091 | 1.14 | 95.62% | ₹1,555 |
| power | 2,446 | 3,291 | 1.35 | 96.90% | ₹1,984 |
| merchant_heavy | 2,655 | 3,177 | 1.20 | 96.51% | ₹1,135 |
| small_ticket | 1,735 | 2,093 | 1.21 | 96.70% | ₹697 |
| occasional | 889 | 916 | 1.03 | 95.96% | ₹1,660 |
| new | 226 | 247 | 1.09 | 97.98% | ₹972 |
| dormant_returning | 22 | 22 | 1.00 | 100.00% | ₹1,432 |

## Operational events

- **INC-BANK-0002** (Sev-2) — Yes Bank issuer decline spike, scoped to Yes Bank between 01:00 and 08:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **REG-0071** (Sev-2) — MDR reinstated on RuPay Credit above ₹2,000, scoped to RUPAY_CREDIT. Merchant discount rate reinstated on higher-value RuPay Credit transactions. Large-ticket volume moved back to debit-funded rails; the product's average ticket falls.
- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Category Digital ran at 90.95% success on 221 attempts (2.2% of the day), 3.61pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 28% across the trailing window to 518 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

10 June was an incident day: INC-BANK-0002 was live and the rail closed at 96.36% success against a 96.21% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,837, successes=13,334, failed=491, pending=12, settled_value_inr=19,746,495.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0002; kind=bank_outage; severity=Sev-2; window=2026-06-08 to 2026-06-10; success_impact_pp=-19.67; volume_impact_pct=-17.45
- geography: region=South; attempts=4,017; success_rate=96.84; own_median=96.27; z=2.58
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- incidents: event_id=REG-0071; kind=pricing_change; severity=Sev-2; window=2026-06-08 to 2026-07-29; success_impact_pp=0.1; volume_impact_pct=-17
- products: product_name=Credit on UPI; attempts=518; window_growth_pct=28.2; success_rate=96.53
- incidents: event_id=MAINT-0086; kind=maintenance_window; severity=Sev-3; window=2026-01-11 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- banks: payer_bank=Kotak Mahindra Bank; attempts=459; own_median=532; z=-2.98
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- categories: mcc_category=Digital; attempts=221; success_rate=90.95; own_median=94.56; z=-2.15

Refs: enterprise_data/warehouse/transactions, RPT-D156-DAILY, enterprise_data/warehouse/reference/incidents.parquet
