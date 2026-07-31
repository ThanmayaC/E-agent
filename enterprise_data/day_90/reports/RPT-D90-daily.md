---
id: RPT-D90-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-04T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 04 Apr 2026)

**Report ID:** RPT-D90-DAILY · **Day 90 of 206** · **Derived from:** 14,645 transaction rows queried live from the warehouse

## Summary

The rail took **14,645 payment attempts** on Saturday 04 April 2026 (Weekend) and settled **₹1.93 Cr** across 14,051 successful payments. Volume was +13.7% on yesterday and +15.7% on the same weekday last week. Success closed at **95.94%**, in line with the trailing 28-day median of 95.84%.

Category Bills carried 1,449 attempts, 109% up its trailing median and 15.0% of the day's volume. Region North ran at 96.70% success on 3,695 attempts (25.2% of the day), 0.83pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,645 | +13.7% | +15.7% | 13,172 |
| Successful payments | 14,051 | +13.4% | +15.5% | 12,650 |
| Success rate | 95.94% | −0.24pp | −0.15pp | 96.04% |
| Settled value | ₹1.93 Cr | +5.4% | +37.3% | ₹1.78 Cr |
| Average ticket | ₹1,375 | −7.1% | +18.9% | ₹1,412 |
| Technical declines | 0.430% | +0.07pp | +0.02pp | 0.415% |
| Business declines | 2.943% | +0.15pp | −0.07pp | 2.938% |
| Risk declines | 0.191% | +0.04pp | +0.11pp | 0.150% |
| Timeout declines | 0.355% | −0.00pp | +0.10pp | 0.334% |
| Retry share | 1.12% | +0.10pp | +0.15pp | 1.16% |
| Latency p95 | 1,247 ms | +0.2% | −0.2% | 1,265 ms |
| Active customers | 11,895 | +11.5% | +12.9% | 10,887 |
| Active merchants | 1,440 | +3.1% | +7.1% | 1,395 |

## What moved

- Category Bills carried 1,449 attempts, 109% up its trailing median and 15.0% of the day's volume.
- Region North ran at 96.70% success on 3,695 attempts (25.2% of the day), 0.83pp up its own 28-day median.
- Product UPI QR Payments ran at 95.47% success on 2,606 attempts (17.8% of the day), 1.10pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 165 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Circle is compounding — attempts up 35% across the trailing window to 298 today, with success holding, so the growth is healthy and worth funding.
- Category Food & Beverage carried 2,337 attempts, 29% up its trailing median and 24.2% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,992 | 34.1% | 95.41% | ₹55.78 L | +14.6% |
| UPI Person to Merchant | 3,980 | 27.2% | 96.31% | ₹40.10 L | +16.4% |
| UPI QR Payments | 2,606 | 17.8% | 95.47% | ₹11.46 L | +25.2% |
| UPI Lite | 1,584 | 10.8% | 98.74% | ₹1.43 L | +69.0% |
| UPI AutoPay | 333 | 2.3% | 91.89% | ₹6.01 L | +4.9% |
| UPI Circle | 298 | 2.0% | 96.31% | ₹2.68 L | +35.1% |
| RuPay Credit on UPI | 278 | 1.9% | 96.04% | ₹17.93 L | +11.4% |
| Credit on UPI | 165 | 1.1% | 93.94% | ₹19.19 L | −2.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,561 | 95.61% | 95.82% | ₹56.19 L | normal |
| HDFC Bank | 1,633 | 96.75% | 95.59% | ₹21.55 L | normal |
| Bank of Baroda | 1,102 | 96.19% | 96.02% | ₹14.73 L | normal |
| Union Bank of India | 1,038 | 95.57% | 95.75% | ₹14.66 L | normal |
| ICICI Bank | 907 | 95.26% | 95.86% | ₹15.77 L | normal |
| Axis Bank | 904 | 96.68% | 95.78% | ₹12.81 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,876 | 96.20% | 95.88% | ₹95.96 L | normal |
| Google Pay | 4,849 | 95.44% | 95.78% | ₹60.89 L | normal |
| Paytm | 1,161 | 95.87% | 96.03% | ₹14.74 L | normal |
| Navi | 515 | 97.09% | 95.67% | ₹5.53 L | normal |
| SuperMoney | 346 | 94.80% | 94.84% | ₹6.00 L | normal |
| BHIM | 143 | 97.90% | 95.88% | ₹1.81 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,581 | 95.84% | ₹36.93 L |
| Food & Beverage | 2,337 | 96.53% | ₹10.73 L |
| Bills | 1,449 | 96.62% | ₹16.64 L |
| Mobility | 1,096 | 96.72% | ₹6.23 L |
| Healthcare | 431 | 98.38% | ₹2.89 L |
| Digital | 321 | 96.88% | ₹2.13 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,313 | 29.5% | 95.62% | ₹53.07 L |
| North | 3,695 | 25.2% | 96.70% | ₹43.38 L |
| West | 3,587 | 24.5% | 95.62% | ₹59.05 L |
| East | 1,786 | 12.2% | 96.30% | ₹22.13 L |
| Central | 1,264 | 8.6% | 95.25% | ₹15.59 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 96.88% | ₹1.63 L |
| Ujjwal Water Board | Key Account | Bills | 71 | 97.18% | ₹1.59 L |
| Rapid Bazaar | Key Account | Retail | 382 | 96.07% | ₹1.49 L |
| Vasant Wardrobe | Key Account | Retail | 58 | 93.10% | ₹1.30 L |
| Hampi Styles | Key Account | Retail | 47 | 93.62% | ₹1.05 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 98.39% | ₹95,753 |
| Girnar Connect | Key Account | Bills | 246 | 97.56% | ₹92,773 |
| Hampi Stores 2298 | Key Account | Retail | 96 | 96.88% | ₹83,447 |

## Failure analysis

Of 574 declined attempts, 431 were business declines (2.943% of attempts — balances, PINs and limits), 63 technical (0.430%), 52 timeouts (0.355%) and 28 risk declines (0.191%).

164 attempts were re-presentations of an earlier failure (1.12% of the day); 68.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 183 | 1.250% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 139 | 0.949% | 1.072% |
| ZA | Transaction declined by customer | business | Customer | 60 | 0.410% | 0.364% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.219% | 0.190% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.205% | 0.224% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 30 | 0.205% | 0.155% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 26 | 0.178% | 0.115% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.102% | 0.104% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 73 | 76 |
| Auto-reversals | 23 | 24 |
| Disputes / chargebacks | 5 | 11 |
| Value returned | ₹99,372 | ₹1.33 L |

## Customer behaviour

11,895 distinct customers transacted (+19.6% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,629 | 4,211 | 1.16 | 95.75% | ₹1,548 |
| power | 2,458 | 3,422 | 1.39 | 96.05% | ₹1,797 |
| merchant_heavy | 2,764 | 3,411 | 1.23 | 96.75% | ₹1,035 |
| small_ticket | 1,769 | 2,224 | 1.26 | 95.50% | ₹570 |
| occasional | 977 | 1,045 | 1.07 | 94.83% | ₹1,506 |
| new | 261 | 295 | 1.13 | 95.25% | ₹883 |
| dormant_returning | 37 | 37 | 1.00 | 97.30% | ₹562 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-PSP-0028** (Sev-3) — Axis Mobile app release regression, scoped to Axis Mobile between 19:00 and 23:00. A Axis Mobile client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **REG-0068** (Sev-3) — UPI Lite per-transaction cap raised to ₹1,000, scoped to UPI_LITE. The Lite per-transaction cap was raised, moving a band of small-ticket payments off the full UPI rail onto Lite. Lite volume steps up permanently and average ticket rises.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI QR Payments ran at 95.47% success on 2,606 attempts (17.8% of the day), 1.10pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 165 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Circle is compounding — attempts up 35% across the trailing window to 298 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

04 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 95.94% success against a 95.84% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-04` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,645, successes=14,051, failed=574, pending=20, settled_value_inr=19,321,866.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- categories: mcc_category=Bills; attempts=1,449; own_median=694.5; z=8.48
- geography: region=North; attempts=3,695; success_rate=96.7; own_median=95.87; z=2.81
- products: product_name=UPI QR Payments; attempts=2,606; success_rate=95.47; own_median=96.58; z=-3.26
- products: product_name=Credit on UPI; attempts=165; window_growth_pct=35.7; success_rate=93.94
- products: product_name=UPI Circle; attempts=298; window_growth_pct=35.2; success_rate=96.31
- categories: mcc_category=Food & Beverage; attempts=2,337; own_median=1,809.5; z=2.34
- categories: mcc_category=Mobility; attempts=1,096; own_median=777.5; z=3.14
- products: product_name=UPI QR Payments; attempts=2,606; own_median=2,081.5; z=2.37
- incidents: event_id=INC-PSP-0028; kind=psp_degradation; severity=Sev-3; window=2026-04-02 to 2026-04-05; success_impact_pp=-3.75; volume_impact_pct=-5.87

Refs: enterprise_data/warehouse/transactions, RPT-D89-DAILY, enterprise_data/warehouse/reference/incidents.parquet
