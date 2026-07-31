---
id: RPT-D155-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 08 Jun 2026)

**Report ID:** RPT-D155-DAILY · **Day 155 of 206** · **Derived from:** 16,320 transaction rows queried live from the warehouse

## Summary

The rail took **16,320 payment attempts** on Monday 08 June 2026 (Working day) and settled **₹2.32 Cr** across 15,741 successful payments. Volume was +7.2% on yesterday and +1.1% on the same weekday last week. Success closed at **96.45%**, in line with the trailing 28-day median of 96.21%.

Category Retail carried 5,137 attempts, 24% up its trailing median and 43.9% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,320 | +7.2% | +1.1% | 15,943 |
| Successful payments | 15,741 | +7.4% | +0.9% | 15,391 |
| Success rate | 96.45% | +0.12pp | −0.23pp | 96.53% |
| Settled value | ₹2.32 Cr | +27.7% | +3.8% | ₹2.21 Cr |
| Average ticket | ₹1,476 | +18.9% | +2.9% | ₹1,439 |
| Technical declines | 0.521% | +0.10pp | +0.18pp | 0.381% |
| Business declines | 2.525% | −0.23pp | −0.03pp | 2.602% |
| Risk declines | 0.104% | +0.01pp | −0.03pp | 0.131% |
| Timeout declines | 0.349% | +0.08pp | +0.16pp | 0.266% |
| Retry share | 1.00% | +0.07pp | +0.16pp | 0.94% |
| Latency p95 | 1,311 ms | +8.6% | +3.7% | 1,271 ms |
| Active customers | 13,169 | +5.3% | +0.2% | 12,944 |
| Active merchants | 1,587 | +2.5% | −1.5% | 1,576 |

## What moved

- Category Retail carried 5,137 attempts, 24% up its trailing median and 43.9% of the day's volume.
- Region East ran at 97.22% success on 1,907 attempts (11.7% of the day), 1.06pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,614 | 28.3% | 95.67% | ₹50.79 L | +5.7% |
| UPI Person to Merchant | 4,224 | 25.9% | 96.35% | ₹43.38 L | +8.1% |
| UPI QR Payments | 2,589 | 15.9% | 96.45% | ₹12.59 L | +9.2% |
| UPI Lite | 2,272 | 13.9% | 99.12% | ₹2.12 L | +23.7% |
| UPI Circle | 702 | 4.3% | 96.58% | ₹6.34 L | +3.8% |
| Credit on UPI | 598 | 3.7% | 96.49% | ₹56.39 L | +56.7% |
| RuPay Credit on UPI | 446 | 2.7% | 97.31% | ₹22.73 L | +19.6% |
| UPI AutoPay | 361 | 2.2% | 90.86% | ₹6.84 L | +5.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,205 | 96.41% | 96.06% | ₹73.56 L | normal |
| HDFC Bank | 1,783 | 96.24% | 96.42% | ₹21.88 L | normal |
| Bank of Baroda | 1,305 | 96.48% | 96.49% | ₹21.02 L | normal |
| Union Bank of India | 1,082 | 96.49% | 96.36% | ₹14.62 L | normal |
| Punjab National Bank | 1,005 | 95.32% | 96.31% | ₹10.08 L | normal |
| Axis Bank | 983 | 96.85% | 96.61% | ₹17.60 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,690 | 96.03% | 96.23% | ₹1.09 Cr | normal |
| Google Pay | 5,420 | 96.51% | 96.09% | ₹74.02 L | normal |
| Paytm | 1,344 | 97.47% | 96.19% | ₹22.84 L | normal |
| Navi | 593 | 97.30% | 96.19% | ₹7.90 L | normal |
| SuperMoney | 291 | 96.91% | 96.38% | ₹3.48 L | normal |
| BHIM | 144 | 96.53% | 95.55% | ₹1.88 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,137 | 97.26% | ₹69.73 L |
| Food & Beverage | 2,902 | 96.69% | ₹14.51 L |
| Mobility | 1,390 | 97.19% | ₹7.68 L |
| Bills | 915 | 95.96% | ₹9.89 L |
| Healthcare | 612 | 97.55% | ₹15.06 L |
| Digital | 225 | 94.67% | ₹1.09 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,759 | 29.2% | 96.41% | ₹68.11 L |
| North | 4,205 | 25.8% | 96.39% | ₹63.79 L |
| West | 3,993 | 24.5% | 96.12% | ₹55.90 L |
| East | 1,907 | 11.7% | 97.22% | ₹25.08 L |
| Central | 1,456 | 8.9% | 96.70% | ₹19.39 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 39 | 97.44% | ₹5.86 L |
| Vasant Wardrobe | Key Account | Retail | 70 | 92.86% | ₹2.55 L |
| Rapid Bazaar | Key Account | Retail | 499 | 97.80% | ₹2.10 L |
| Hampi Stores 2298 | Key Account | Retail | 147 | 96.60% | ₹1.18 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 69 | 95.65% | ₹85,990 |
| Hampi Styles | Key Account | Retail | 44 | 93.18% | ₹82,427 |
| Kaveri Trading | Large | Retail | 67 | 100.00% | ₹81,278 |
| Zenith Diner | Large | Food & Beverage | 42 | 95.24% | ₹81,251 |

## Failure analysis

Of 571 declined attempts, 412 were business declines (2.525% of attempts — balances, PINs and limits), 85 technical (0.521%), 57 timeouts (0.349%) and 17 risk declines (0.104%).

164 attempts were re-presentations of an earlier failure (1.00% of the day); 68.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 193 | 1.183% | 1.179% |
| ZM | Invalid UPI PIN | business | Customer | 117 | 0.717% | 0.924% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.319% | 0.343% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.196% | 0.194% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.190% | 0.207% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.159% | 0.145% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.147% | 0.115% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.110% | 0.097% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 120 | 106 |
| Auto-reversals | 24 | 25 |
| Disputes / chargebacks | 18 | 13 |
| Value returned | ₹1.45 L | ₹1.88 L |

## Customer behaviour

13,169 distinct customers transacted (+9.4% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,053 | 4,718 | 1.16 | 96.80% | ₹1,365 |
| power | 2,831 | 4,005 | 1.41 | 95.96% | ₹1,969 |
| merchant_heavy | 3,021 | 3,713 | 1.23 | 96.71% | ₹1,277 |
| small_ticket | 1,957 | 2,476 | 1.27 | 96.45% | ₹577 |
| occasional | 1,026 | 1,102 | 1.07 | 96.28% | ₹2,255 |
| new | 257 | 280 | 1.09 | 95.00% | ₹781 |
| dormant_returning | 24 | 26 | 1.08 | 96.15% | ₹1,193 |

## Operational events

- **INC-BANK-0002** (Sev-2) — Yes Bank issuer decline spike, scoped to Yes Bank between 01:00 and 08:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-BANK-0007** (Sev-2) — Punjab National Bank issuer decline spike, scoped to Punjab National Bank between 19:00 and 22:00. Punjab National Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **REG-0071** (Sev-2) — MDR reinstated on RuPay Credit above ₹2,000, scoped to RUPAY_CREDIT. Merchant discount rate reinstated on higher-value RuPay Credit transactions. Large-ticket volume moved back to debit-funded rails; the product's average ticket falls.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 26% across the trailing window to 702 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product Credit on UPI is compounding — attempts up 26% across the trailing window to 598 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

08 June was an incident day: INC-BANK-0002, INC-BANK-0007 were live and the rail closed at 96.45% success against a 96.21% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,320, successes=15,741, failed=571, pending=8, settled_value_inr=23,227,197.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0002; kind=bank_outage; severity=Sev-2; window=2026-06-08 to 2026-06-10; success_impact_pp=-19.67; volume_impact_pct=-17.45
- incidents: event_id=INC-BANK-0007; kind=bank_outage; severity=Sev-2; window=2026-06-08 to 2026-06-09; success_impact_pp=-15.67; volume_impact_pct=-13.9
- categories: mcc_category=Retail; attempts=5,137; own_median=4,157; z=2.77
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- incidents: event_id=REG-0071; kind=pricing_change; severity=Sev-2; window=2026-06-08 to 2026-07-29; success_impact_pp=0.1; volume_impact_pct=-17
- geography: region=East; attempts=1,907; success_rate=97.22; own_median=96.16; z=2.2
- products: product_name=Credit on UPI; attempts=598; window_growth_pct=26.1; success_rate=96.49
- products: product_name=UPI Circle; attempts=702; window_growth_pct=25.8; success_rate=96.58
- products: product_name=Credit on UPI; attempts=598; own_median=381.5; z=3.65
- categories: mcc_category=Healthcare; attempts=612; own_median=509; z=2.78

Refs: enterprise_data/warehouse/transactions, RPT-D154-DAILY, enterprise_data/warehouse/reference/incidents.parquet
