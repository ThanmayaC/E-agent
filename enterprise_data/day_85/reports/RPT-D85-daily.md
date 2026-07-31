---
id: RPT-D85-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-30T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 30 Mar 2026)

**Report ID:** RPT-D85-DAILY · **Day 85 of 206** · **Derived from:** 13,985 transaction rows queried live from the warehouse

## Summary

The rail took **13,985 payment attempts** on Monday 30 March 2026 (Financial Year End (build-up)) and settled **₹1.83 Cr** across 13,421 successful payments. Volume was +29.3% on yesterday and +28.7% on the same weekday last week. Success closed at **95.97%**, in line with the trailing 28-day median of 95.79%.

Category Bills carried 1,210 attempts, 74% up its trailing median and 13.1% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,985 | +29.3% | +28.7% | 12,436 |
| Successful payments | 13,421 | +30.3% | +29.1% | 11,891 |
| Success rate | 95.97% | +0.76pp | +0.28pp | 95.55% |
| Settled value | ₹1.83 Cr | +53.0% | +42.4% | ₹1.42 Cr |
| Average ticket | ₹1,360 | +17.4% | +10.4% | ₹1,196 |
| Technical declines | 0.408% | −0.02pp | +0.07pp | 0.475% |
| Business declines | 3.060% | −0.79pp | −0.51pp | 3.313% |
| Risk declines | 0.150% | +0.00pp | +0.02pp | 0.123% |
| Timeout declines | 0.315% | +0.11pp | +0.10pp | 0.429% |
| Retry share | 1.08% | −0.18pp | −0.31pp | 1.42% |
| Latency p95 | 1,265 ms | +4.3% | +2.5% | 1,283 ms |
| Active customers | 11,505 | +24.5% | +24.2% | 10,310 |
| Active merchants | 1,416 | +7.8% | +8.7% | 1,323 |

## What moved

- Category Bills carried 1,210 attempts, 74% up its trailing median and 13.1% of the day's volume.
- App Google Pay ran at 96.51% success on 4,697 attempts (33.6% of the day), 0.83pp up its own 28-day median.
- Product Credit on UPI is compounding — attempts up 29% across the trailing window to 258 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,768 | 34.1% | 95.74% | ₹54.99 L | +8.8% |
| UPI Person to Merchant | 4,161 | 29.8% | 95.46% | ₹47.32 L | +20.2% |
| UPI QR Payments | 2,452 | 17.5% | 96.66% | ₹10.96 L | +14.3% |
| UPI Lite | 1,061 | 7.6% | 99.25% | ₹99,663 | +15.2% |
| RuPay Credit on UPI | 365 | 2.6% | 96.44% | ₹16.05 L | +61.9% |
| UPI AutoPay | 300 | 2.1% | 91.67% | ₹5.82 L | −5.2% |
| Credit on UPI | 258 | 1.8% | 94.96% | ₹25.42 L | +65.4% |
| UPI Circle | 229 | 1.6% | 96.94% | ₹1.61 L | +19.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,487 | 95.90% | 95.78% | ₹55.19 L | normal |
| HDFC Bank | 1,556 | 96.21% | 95.59% | ₹22.43 L | normal |
| Bank of Baroda | 1,060 | 96.04% | 95.84% | ₹12.22 L | normal |
| Union Bank of India | 980 | 96.43% | 95.69% | ₹11.01 L | normal |
| ICICI Bank | 866 | 96.54% | 95.76% | ₹10.45 L | normal |
| Axis Bank | 848 | 96.58% | 95.98% | ₹14.64 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,605 | 95.55% | 95.95% | ₹86.18 L | normal |
| Google Pay | 4,697 | 96.51% | 95.68% | ₹65.31 L | ⚠ outlier |
| Paytm | 1,137 | 97.19% | 95.81% | ₹13.48 L | normal |
| Navi | 539 | 95.73% | 95.60% | ₹4.86 L | normal |
| SuperMoney | 256 | 95.31% | 95.09% | ₹2.03 L | normal |
| BHIM | 141 | 95.04% | 95.53% | ₹1.53 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,927 | 95.77% | ₹51.04 L |
| Food & Beverage | 2,140 | 96.82% | ₹11.22 L |
| Bills | 1,210 | 96.03% | ₹14.48 L |
| Mobility | 906 | 97.02% | ₹6.63 L |
| Healthcare | 404 | 97.77% | ₹5.64 L |
| Digital | 227 | 96.48% | ₹1.38 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,177 | 29.9% | 95.98% | ₹56.33 L |
| North | 3,474 | 24.8% | 95.85% | ₹43.97 L |
| West | 3,410 | 24.4% | 95.72% | ₹44.39 L |
| East | 1,723 | 12.3% | 96.40% | ₹19.51 L |
| Central | 1,201 | 8.6% | 96.34% | ₹18.38 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 39 | 89.74% | ₹2.00 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 90.54% | ₹1.94 L |
| Rapid Bazaar | Key Account | Retail | 358 | 97.21% | ₹1.41 L |
| Hampi Stores 2298 | Key Account | Retail | 129 | 96.90% | ₹1.05 L |
| Urban Boutique | Key Account | Retail | 103 | 91.26% | ₹1.03 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 90 | 95.56% | ₹96,460 |
| Ujjwal Water Board | Key Account | Bills | 57 | 89.47% | ₹78,612 |
| Girnar Connect | Key Account | Bills | 206 | 96.60% | ₹78,332 |

## Failure analysis

Of 550 declined attempts, 428 were business declines (3.060% of attempts — balances, PINs and limits), 57 technical (0.408%), 44 timeouts (0.315%) and 21 risk declines (0.150%).

151 attempts were re-presentations of an earlier failure (1.08% of the day); 69.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.344% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 131 | 0.937% | 1.082% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.358% | 0.384% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.250% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.186% | 0.179% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.179% | 0.154% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.150% | 0.107% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.100% | 0.114% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 94 | 78 |
| Auto-reversals | 22 | 24 |
| Disputes / chargebacks | 13 | 10 |
| Value returned | ₹1.30 L | ₹1.31 L |

## Customer behaviour

11,505 distinct customers transacted (+15.7% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,611 | 4,133 | 1.14 | 95.86% | ₹1,359 |
| power | 2,437 | 3,327 | 1.37 | 95.88% | ₹1,897 |
| merchant_heavy | 2,588 | 3,158 | 1.22 | 96.11% | ₹1,136 |
| small_ticket | 1,705 | 2,122 | 1.24 | 95.99% | ₹582 |
| occasional | 932 | 992 | 1.06 | 96.47% | ₹1,348 |
| new | 202 | 222 | 1.10 | 94.59% | ₹646 |
| dormant_returning | 30 | 31 | 1.03 | 96.77% | ₹838 |

## Operational events

- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product Credit on UPI is compounding — attempts up 29% across the trailing window to 258 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

30 March ran on trend at 95.97% success and ₹1.83 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 1,210 attempts, 74% up its trailing median and 13.1% of the day's volume. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-30` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,985, successes=13,421, failed=550, pending=14, settled_value_inr=18,257,875.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,210; own_median=694.5; z=5.79
- psps: payer_psp=Google Pay; attempts=4,697; success_rate=96.51; own_median=95.68; z=2.29
- products: product_name=Credit on UPI; attempts=258; window_growth_pct=28.8; success_rate=94.96
- categories: mcc_category=Mobility; attempts=906; own_median=773; z=2.53
- products: product_name=RuPay Credit on UPI; attempts=365; own_median=225.5; z=3.19
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- incidents: event_id=CMP-0057; kind=merchant_campaign; severity=Sev-3; window=2026-03-25 to 2026-04-01; success_impact_pp=-0.07; volume_impact_pct=28.96
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- products: product_name=Credit on UPI; attempts=258; own_median=156; z=2.81
- categories: mcc_category=Services; attempts=120; own_median=98; z=2.28

Refs: enterprise_data/warehouse/transactions, RPT-D84-DAILY, enterprise_data/warehouse/reference/incidents.parquet
