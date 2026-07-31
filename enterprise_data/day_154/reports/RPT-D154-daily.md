---
id: RPT-D154-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 07 Jun 2026)

**Report ID:** RPT-D154-DAILY · **Day 154 of 206** · **Derived from:** 15,221 transaction rows queried live from the warehouse

## Summary

The rail took **15,221 payment attempts** on Sunday 07 June 2026 (Weekend) and settled **₹1.82 Cr** across 14,663 successful payments. Volume was −18.4% on yesterday and +1.4% on the same weekday last week. Success closed at **96.33%**, in line with the trailing 28-day median of 96.17%.

123 refunds were raised, 2.7 sigma above the trailing median of 105.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,221 | −18.4% | +1.4% | 15,889 |
| Successful payments | 14,663 | −18.7% | +1.3% | 15,341 |
| Success rate | 96.33% | −0.41pp | −0.06pp | 96.54% |
| Settled value | ₹1.82 Cr | −23.3% | −3.6% | ₹2.19 Cr |
| Average ticket | ₹1,241 | −5.6% | −4.8% | ₹1,434 |
| Technical declines | 0.420% | +0.05pp | +0.09pp | 0.361% |
| Business declines | 2.753% | +0.34pp | −0.06pp | 2.613% |
| Risk declines | 0.092% | −0.04pp | −0.06pp | 0.135% |
| Timeout declines | 0.269% | +0.01pp | +0.05pp | 0.254% |
| Retry share | 0.94% | +0.03pp | +0.03pp | 0.93% |
| Latency p95 | 1,207 ms | −2.2% | −0.7% | 1,266 ms |
| Active customers | 12,504 | −15.0% | +1.7% | 12,912 |
| Active merchants | 1,549 | −5.8% | +1.7% | 1,575 |

## What moved

- Category Bills carried 1,557 attempts, 71% up its trailing median and 14.4% of the day's volume.
- Product UPI Circle is compounding — attempts up 33% across the trailing window to 724 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product Credit on UPI is compounding — attempts up 27% across the trailing window to 271 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,423 | 29.1% | 95.23% | ₹47.18 L | +1.8% |
| UPI Person to Merchant | 4,124 | 27.1% | 96.22% | ₹42.86 L | +6.5% |
| UPI QR Payments | 2,485 | 16.3% | 96.86% | ₹11.21 L | +5.7% |
| UPI Lite | 2,232 | 14.7% | 99.15% | ₹1.96 L | +24.5% |
| UPI Circle | 724 | 4.8% | 96.69% | ₹7.04 L | +12.5% |
| UPI AutoPay | 349 | 2.3% | 91.98% | ₹6.84 L | +2.2% |
| Credit on UPI | 271 | 1.8% | 94.10% | ₹21.65 L | −29.0% |
| RuPay Credit on UPI | 203 | 1.3% | 97.04% | ₹9.26 L | −45.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,840 | 95.93% | 96.06% | ₹58.19 L | normal |
| HDFC Bank | 1,648 | 96.60% | 96.39% | ₹19.26 L | normal |
| Bank of Baroda | 1,161 | 96.55% | 96.41% | ₹15.13 L | normal |
| Union Bank of India | 1,044 | 95.88% | 96.36% | ₹8.92 L | normal |
| Axis Bank | 975 | 97.13% | 96.61% | ₹17.00 L | normal |
| Punjab National Bank | 934 | 96.47% | 96.26% | ₹8.85 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,135 | 95.96% | 96.23% | ₹83.29 L | normal |
| Google Pay | 5,115 | 96.89% | 96.07% | ₹63.54 L | normal |
| Paytm | 1,241 | 96.54% | 96.14% | ₹14.27 L | normal |
| Navi | 548 | 95.80% | 96.19% | ₹6.74 L | normal |
| SuperMoney | 311 | 97.43% | 96.38% | ₹4.78 L | normal |
| BHIM | 137 | 91.24% | 95.69% | ₹1.08 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,175 | 97.17% | ₹41.34 L |
| Food & Beverage | 2,608 | 96.78% | ₹12.57 L |
| Bills | 1,557 | 96.79% | ₹17.83 L |
| Mobility | 1,211 | 97.19% | ₹6.15 L |
| Healthcare | 484 | 97.73% | ₹4.24 L |
| Digital | 327 | 95.11% | ₹1.59 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,436 | 29.1% | 96.28% | ₹50.11 L |
| North | 3,876 | 25.5% | 96.36% | ₹46.69 L |
| West | 3,811 | 25.0% | 96.38% | ₹47.94 L |
| East | 1,762 | 11.6% | 96.14% | ₹22.32 L |
| Central | 1,336 | 8.8% | 96.56% | ₹14.88 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 90.32% | ₹3.57 L |
| Hampi Stores 2298 | Key Account | Retail | 125 | 98.40% | ₹2.67 L |
| Rapid Bazaar | Key Account | Retail | 475 | 97.68% | ₹1.92 L |
| Ujjwal Water Board | Key Account | Bills | 68 | 98.53% | ₹1.87 L |
| Vasant Wardrobe | Key Account | Retail | 63 | 100.00% | ₹1.64 L |
| Girnar Connect | Key Account | Bills | 255 | 98.04% | ₹1.04 L |
| Urban Boutique | Key Account | Retail | 111 | 97.30% | ₹80,251 |
| Tejas Supermart | Large | Retail | 37 | 89.19% | ₹66,576 |

## Failure analysis

Of 538 declined attempts, 419 were business declines (2.753% of attempts — balances, PINs and limits), 64 technical (0.420%), 41 timeouts (0.269%) and 14 risk declines (0.092%).

143 attempts were re-presentations of an earlier failure (0.94% of the day); 67.8% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.235% | 1.158% |
| ZM | Invalid UPI PIN | business | Customer | 120 | 0.788% | 0.933% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.315% | 0.346% |
| XH | Account does not exist / frozen | business | Issuer | 39 | 0.256% | 0.207% |
| U28 | Remitter bank unavailable | technical | Issuer | 23 | 0.151% | 0.115% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.151% | 0.194% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.138% | 0.146% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.099% | 0.099% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 123 | 105 |
| Auto-reversals | 20 | 25 |
| Disputes / chargebacks | 8 | 13 |
| Value returned | ₹2.75 L | ₹1.80 L |

## Customer behaviour

12,504 distinct customers transacted (+4.2% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,847 | 4,452 | 1.16 | 96.00% | ₹1,123 |
| power | 2,718 | 3,666 | 1.35 | 96.59% | ₹1,795 |
| merchant_heavy | 2,825 | 3,460 | 1.22 | 96.04% | ₹965 |
| small_ticket | 1,864 | 2,327 | 1.25 | 96.73% | ₹551 |
| occasional | 976 | 1,020 | 1.05 | 96.76% | ₹1,595 |
| new | 238 | 260 | 1.09 | 96.54% | ₹1,032 |
| dormant_returning | 36 | 36 | 1.00 | 100.00% | ₹2,692 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 123 refunds were raised, 2.7 sigma above the trailing median of 105.
- Product UPI Circle is compounding — attempts up 33% across the trailing window to 724 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product Credit on UPI is compounding — attempts up 27% across the trailing window to 271 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

07 June ran on trend at 96.33% success and ₹1.82 Cr settled. The movement worth carrying forward is in money moving back: 123 refunds were raised, 2.7 sigma above the trailing median of 105. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,221, successes=14,663, failed=538, pending=20, settled_value_inr=18,194,753.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: refunds=123; trailing_median=105; z=2.7
- categories: mcc_category=Bills; attempts=1,557; own_median=913; z=3.78
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Circle; attempts=724; window_growth_pct=32.5; success_rate=96.69
- products: product_name=Credit on UPI; attempts=271; window_growth_pct=27.4; success_rate=94.1
- banks: payer_bank=Kotak Mahindra Bank; attempts=541; success_rate=98.52; own_median=96.01; z=2.34
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- products: product_name=RuPay Credit on UPI; attempts=203; own_median=373; z=-3.32

Refs: enterprise_data/warehouse/transactions, RPT-D153-DAILY, enterprise_data/warehouse/reference/incidents.parquet
