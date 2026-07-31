---
id: RPT-D73-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 18 Mar 2026)

**Report ID:** RPT-D73-DAILY · **Day 73 of 206** · **Derived from:** 12,959 transaction rows queried live from the warehouse

## Summary

The rail took **12,959 payment attempts** on Wednesday 18 March 2026 (Ugadi / Gudi Padwa (build-up)) and settled **₹1.50 Cr** across 12,414 successful payments. Volume was +9.8% on yesterday and +16.3% on the same weekday last week. Success closed at **95.79%**, in line with the trailing 28-day median of 95.65%.

Product UPI Circle is compounding — attempts up 86% across the trailing window to 209 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,959 | +9.8% | +16.3% | 12,683 |
| Successful payments | 12,414 | +9.6% | +17.9% | 12,145 |
| Success rate | 95.79% | −0.17pp | +1.24pp | 95.73% |
| Settled value | ₹1.50 Cr | +7.2% | +17.6% | ₹1.45 Cr |
| Average ticket | ₹1,205 | −2.2% | −0.2% | ₹1,193 |
| Technical declines | 0.486% | +0.00pp | −0.26pp | 0.460% |
| Business declines | 3.172% | +0.05pp | −0.42pp | 3.250% |
| Risk declines | 0.131% | +0.04pp | +0.01pp | 0.119% |
| Timeout declines | 0.301% | +0.06pp | −0.59pp | 0.341% |
| Retry share | 1.19% | +0.14pp | −0.89pp | 1.30% |
| Latency p95 | 1,247 ms | +1.7% | −13.3% | 1,246 ms |
| Active customers | 10,693 | +8.1% | +14.3% | 10,475 |
| Active merchants | 1,316 | +2.5% | +0.8% | 1,324 |

## What moved

- Product UPI Circle is compounding — attempts up 86% across the trailing window to 209 today, with success holding, so the growth is healthy and worth funding.
- Product UPI 123Pay is compounding — attempts up 31% across the trailing window to 80 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,768 | 36.8% | 95.41% | ₹55.54 L | +12.3% |
| UPI Person to Merchant | 3,786 | 29.2% | 96.09% | ₹41.06 L | +14.5% |
| UPI QR Payments | 2,180 | 16.8% | 96.38% | ₹9.96 L | +10.5% |
| UPI Lite | 978 | 7.5% | 98.98% | ₹93,138 | +24.1% |
| UPI AutoPay | 335 | 2.6% | 90.75% | ₹5.96 L | +8.2% |
| RuPay Credit on UPI | 210 | 1.6% | 94.29% | ₹9.34 L | −6.9% |
| UPI Circle | 209 | 1.6% | 96.65% | ₹1.73 L | +29.4% |
| Credit on UPI | 138 | 1.1% | 94.93% | ₹10.63 L | −11.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,055 | 95.98% | 95.59% | ₹44.48 L | normal |
| HDFC Bank | 1,343 | 94.79% | 95.84% | ₹16.77 L | normal |
| Bank of Baroda | 981 | 94.80% | 95.64% | ₹10.15 L | normal |
| Union Bank of India | 909 | 97.03% | 95.13% | ₹12.11 L | ⚠ outlier |
| Axis Bank | 809 | 96.79% | 95.84% | ₹7.85 L | normal |
| Punjab National Bank | 796 | 95.23% | 95.11% | ₹9.09 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,110 | 95.78% | 95.66% | ₹68.31 L | normal |
| Google Pay | 4,330 | 95.75% | 95.57% | ₹54.66 L | normal |
| Paytm | 1,044 | 94.73% | 95.50% | ₹12.20 L | normal |
| Navi | 462 | 97.40% | 95.52% | ₹4.72 L | normal |
| SuperMoney | 218 | 95.41% | 95.85% | ₹2.07 L | normal |
| BHIM | 120 | 97.50% | 94.88% | ₹1.17 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,002 | 96.08% | ₹40.21 L |
| Food & Beverage | 1,856 | 97.25% | ₹11.56 L |
| Mobility | 736 | 96.33% | ₹5.22 L |
| Bills | 683 | 94.73% | ₹7.96 L |
| Healthcare | 366 | 96.72% | ₹2.99 L |
| Digital | 181 | 95.58% | ₹98,607 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,780 | 29.2% | 95.37% | ₹44.56 L |
| North | 3,299 | 25.5% | 95.94% | ₹35.09 L |
| West | 3,208 | 24.8% | 96.26% | ₹39.20 L |
| East | 1,452 | 11.2% | 95.80% | ₹20.65 L |
| Central | 1,220 | 9.4% | 95.49% | ₹10.09 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 95 | 91.58% | ₹2.62 L |
| Rapid Bazaar | Key Account | Retail | 485 | 95.46% | ₹2.08 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 67 | 95.52% | ₹1.13 L |
| Vega Electronics | Large | Retail | 24 | 95.83% | ₹1.09 L |
| Ujjwal Water Board | Key Account | Bills | 24 | 100.00% | ₹82,285 |
| Hampi Styles | Key Account | Retail | 39 | 94.87% | ₹81,882 |
| Urban Boutique | Key Account | Retail | 98 | 95.92% | ₹72,594 |
| Girnar Connect | Key Account | Bills | 114 | 95.61% | ₹64,396 |

## Failure analysis

Of 530 declined attempts, 411 were business declines (3.172% of attempts — balances, PINs and limits), 63 technical (0.486%), 39 timeouts (0.301%) and 17 risk declines (0.131%).

154 attempts were re-presentations of an earlier failure (1.19% of the day); 68.8% of them succeeded.

- Decline code U28 (Remitter bank unavailable) fired 26 times — 0.201% of attempts against a trailing 0.122%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 163 | 1.258% | 1.413% |
| ZM | Invalid UPI PIN | business | Customer | 140 | 1.080% | 1.118% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.394% | 0.403% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.255% | 0.228% |
| U28 | Remitter bank unavailable | technical | Issuer | 26 | 0.201% | 0.122% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.162% | 0.178% |
| U30 | Debit failed at remitter bank | technical | Issuer | 17 | 0.131% | 0.178% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.116% | 0.091% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 72 | 75 |
| Auto-reversals | 16 | 24 |
| Disputes / chargebacks | 12 | 10 |
| Value returned | ₹1.84 L | ₹99,240 |

## Customer behaviour

10,693 distinct customers transacted (+8.4% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,260 | 3,728 | 1.14 | 95.98% | ₹1,186 |
| power | 2,299 | 3,105 | 1.35 | 95.97% | ₹1,707 |
| merchant_heavy | 2,472 | 3,028 | 1.22 | 95.08% | ₹866 |
| small_ticket | 1,574 | 1,948 | 1.24 | 95.89% | ₹549 |
| occasional | 853 | 897 | 1.05 | 96.88% | ₹1,469 |
| new | 203 | 221 | 1.09 | 95.02% | ₹868 |
| dormant_returning | 32 | 32 | 1.00 | 93.75% | ₹1,144 |

## Operational events

- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Decline code U28 (Remitter bank unavailable) fired 26 times — 0.201% of attempts against a trailing 0.122%. Owner: Issuer.
- Product UPI 123Pay is compounding — attempts up 31% across the trailing window to 80 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Circle is compounding — attempts up 86% across the trailing window to 209 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

18 March ran on trend at 95.79% success and ₹1.50 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 86% across the trailing window to 209 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,959, successes=12,414, failed=530, pending=15, settled_value_inr=14,958,954.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=209; window_growth_pct=86.3; success_rate=96.65
- failures: failure_code=U28; count=26; rate_pct=0.2; trailing_rate_pct=0.12; owner=Issuer; z=2.86
- products: product_name=UPI 123Pay; attempts=80; window_growth_pct=30.6; success_rate=92.5
- banks: payer_bank=Union Bank of India; attempts=909; success_rate=97.03; own_median=95.13; z=2.14
- categories: mcc_category=Services; attempts=141; own_median=99; z=5.67
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- banks: payer_bank=IDFC First Bank; attempts=348; success_rate=97.7; own_median=95.7; z=2.2

Refs: enterprise_data/warehouse/transactions, RPT-D72-DAILY, enterprise_data/warehouse/reference/incidents.parquet
