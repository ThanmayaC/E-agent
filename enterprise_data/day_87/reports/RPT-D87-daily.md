---
id: RPT-D87-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-01T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 01 Apr 2026)

**Report ID:** RPT-D87-DAILY · **Day 87 of 206** · **Derived from:** 13,214 transaction rows queried live from the warehouse

## Summary

The rail took **13,214 payment attempts** on Wednesday 01 April 2026 (Working day) and settled **₹1.75 Cr** across 12,686 successful payments. Volume was −3.6% on yesterday and +32.6% on the same weekday last week. Success closed at **96.00%**, in line with the trailing 28-day median of 95.83%.

Category Bills carried 1,363 attempts, 96% up its trailing median and 16.1% of the day's volume. Product Credit on UPI is compounding — attempts up 51% across the trailing window to 230 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,214 | −3.6% | +32.6% | 13,214 |
| Successful payments | 12,686 | −3.9% | +33.7% | 12,686 |
| Success rate | 96.00% | −0.32pp | +0.79pp | 96.00% |
| Settled value | ₹1.75 Cr | −15.5% | +47.4% | ₹1.75 Cr |
| Average ticket | ₹1,383 | −12.1% | +10.3% | ₹1,383 |
| Technical declines | 0.431% | −0.03pp | +0.12pp | 0.431% |
| Business declines | 2.967% | +0.30pp | −0.99pp | 2.967% |
| Risk declines | 0.129% | +0.02pp | +0.01pp | 0.129% |
| Timeout declines | 0.356% | +0.02pp | +0.10pp | 0.356% |
| Retry share | 1.35% | +0.08pp | +0.10pp | 1.35% |
| Latency p95 | 1,281 ms | +0.4% | −3.2% | 1,281 ms |
| Active customers | 10,948 | −2.6% | +27.5% | 10,948 |
| Active merchants | 1,394 | −1.1% | +9.4% | 1,394 |

## What moved

- Category Bills carried 1,363 attempts, 96% up its trailing median and 16.1% of the day's volume.
- Product Credit on UPI is compounding — attempts up 51% across the trailing window to 230 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product RuPay Credit on UPI is compounding — attempts up 35% across the trailing window to 310 today, with success holding, so the growth is healthy and worth funding.
- Category Mobility carried 955 attempts, 23% up its trailing median and 11.3% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,751 | 36.0% | 95.33% | ₹54.20 L | +8.4% |
| UPI Person to Merchant | 3,671 | 27.8% | 96.51% | ₹37.01 L | +6.0% |
| UPI QR Payments | 2,144 | 16.2% | 96.46% | ₹9.55 L | +0.8% |
| UPI Lite | 1,147 | 8.7% | 98.61% | ₹1.06 L | +24.1% |
| UPI AutoPay | 312 | 2.4% | 91.35% | ₹5.65 L | −1.7% |
| RuPay Credit on UPI | 310 | 2.3% | 96.77% | ₹20.06 L | +28.9% |
| UPI Circle | 259 | 2.0% | 96.14% | ₹2.79 L | +29.2% |
| Credit on UPI | 230 | 1.7% | 93.91% | ₹15.17 L | +44.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,275 | 96.35% | 95.82% | ₹51.34 L | normal |
| HDFC Bank | 1,455 | 94.91% | 95.59% | ₹20.77 L | normal |
| Bank of Baroda | 990 | 95.15% | 96.02% | ₹13.67 L | normal |
| Union Bank of India | 889 | 96.06% | 95.79% | ₹11.15 L | normal |
| Axis Bank | 817 | 97.43% | 95.98% | ₹11.16 L | normal |
| Punjab National Bank | 791 | 95.20% | 95.41% | ₹11.05 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,228 | 95.70% | 95.93% | ₹77.84 L | normal |
| Google Pay | 4,433 | 96.28% | 95.76% | ₹64.66 L | normal |
| Paytm | 1,049 | 96.28% | 95.81% | ₹15.14 L | normal |
| Navi | 467 | 96.57% | 95.67% | ₹5.74 L | normal |
| SuperMoney | 239 | 96.65% | 95.09% | ₹2.18 L | normal |
| FamApp | 130 | 97.69% | 97.01% | ₹1.89 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,115 | 96.34% | ₹38.47 L |
| Food & Beverage | 1,864 | 97.42% | ₹9.01 L |
| Bills | 1,363 | 96.77% | ₹14.28 L |
| Mobility | 955 | 96.44% | ₹5.69 L |
| Healthcare | 426 | 96.01% | ₹2.77 L |
| Digital | 301 | 98.01% | ₹1.50 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,988 | 30.2% | 96.11% | ₹51.29 L |
| North | 3,318 | 25.1% | 95.90% | ₹45.42 L |
| West | 3,241 | 24.5% | 96.08% | ₹40.77 L |
| East | 1,577 | 11.9% | 95.88% | ₹27.00 L |
| Central | 1,090 | 8.2% | 95.87% | ₹10.98 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 39 | 89.74% | ₹1.92 L |
| Rapid Bazaar | Key Account | Retail | 324 | 97.53% | ₹1.49 L |
| Ujjwal Water Board | Key Account | Bills | 63 | 100.00% | ₹1.36 L |
| Girnar Connect | Key Account | Bills | 238 | 94.96% | ₹1.08 L |
| Vasant Wardrobe | Key Account | Retail | 72 | 93.06% | ₹1.04 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 60 | 98.33% | ₹69,798 |
| Swift Grill | Large | Food & Beverage | 27 | 96.30% | ₹48,860 |
| Urban Boutique | Key Account | Retail | 77 | 93.51% | ₹48,416 |

## Failure analysis

Of 513 declined attempts, 392 were business declines (2.967% of attempts — balances, PINs and limits), 57 technical (0.431%), 47 timeouts (0.356%) and 17 risk declines (0.129%).

178 attempts were re-presentations of an earlier failure (1.35% of the day); 66.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.173% | 1.341% |
| ZM | Invalid UPI PIN | business | Customer | 134 | 1.014% | 1.081% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.348% | 0.364% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.227% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.212% | 0.188% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.182% | 0.154% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 20 | 0.151% | 0.101% |
| ZX | Mandate not found or revoked | business | PSP | 13 | 0.098% | 0.083% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 97 | 78 |
| Auto-reversals | 29 | 24 |
| Disputes / chargebacks | 8 | 10 |
| Value returned | ₹1.98 L | ₹1.31 L |

## Customer behaviour

10,948 distinct customers transacted (+10.1% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,411 | 3,864 | 1.13 | 96.17% | ₹1,315 |
| power | 2,307 | 3,136 | 1.36 | 95.63% | ₹1,891 |
| merchant_heavy | 2,474 | 2,981 | 1.20 | 96.18% | ₹1,116 |
| small_ticket | 1,673 | 2,083 | 1.25 | 95.92% | ₹489 |
| occasional | 852 | 896 | 1.05 | 96.32% | ₹2,203 |
| new | 206 | 229 | 1.11 | 95.20% | ₹856 |
| dormant_returning | 25 | 25 | 1.00 | 100.00% | ₹719 |

## Operational events

- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **REG-0068** (Sev-3) — UPI Lite per-transaction cap raised to ₹1,000, scoped to UPI_LITE. The Lite per-transaction cap was raised, moving a band of small-ticket payments off the full UPI rail onto Lite. Lite volume steps up permanently and average ticket rises.

## Risks and opportunities

### Risks

- Product Credit on UPI is compounding — attempts up 51% across the trailing window to 230 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product RuPay Credit on UPI is compounding — attempts up 35% across the trailing window to 310 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

01 April ran on trend at 96.00% success and ₹1.75 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 1,363 attempts, 96% up its trailing median and 16.1% of the day's volume. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-01` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,214, successes=12,686, failed=513, pending=15, settled_value_inr=17,545,411.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,363; own_median=694.5; z=7.51
- products: product_name=Credit on UPI; attempts=230; window_growth_pct=50.9; success_rate=93.91
- products: product_name=RuPay Credit on UPI; attempts=310; window_growth_pct=34.9; success_rate=96.77
- categories: mcc_category=Mobility; attempts=955; own_median=773.5; z=3.14
- categories: mcc_category=Travel; attempts=136; own_median=65; z=5.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- incidents: event_id=CMP-0057; kind=merchant_campaign; severity=Sev-3; window=2026-03-25 to 2026-04-01; success_impact_pp=-0.07; volume_impact_pct=28.96
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41
- incidents: event_id=REG-0068; kind=regulatory_change; severity=Sev-3; window=2026-04-01 to 2026-07-29; success_impact_pp=0.18; volume_impact_pct=26

Refs: enterprise_data/warehouse/transactions, RPT-D86-DAILY, enterprise_data/warehouse/reference/incidents.parquet
