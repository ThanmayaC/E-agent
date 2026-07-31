---
id: RPT-D72-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 17 Mar 2026)

**Report ID:** RPT-D72-DAILY · **Day 72 of 206** · **Derived from:** 11,803 transaction rows queried live from the warehouse

## Summary

The rail took **11,803 payment attempts** on Tuesday 17 March 2026 (Working day) and settled **₹1.40 Cr** across 11,327 successful payments. Volume was +1.2% on yesterday and +11.7% on the same weekday last week. Success closed at **95.97%**, above the trailing 28-day median of 95.62%.

Product UPI Circle is compounding — attempts up 79% across the trailing window to 188 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,803 | +1.2% | +11.7% | 12,667 |
| Successful payments | 11,327 | +1.3% | +11.4% | 12,129 |
| Success rate | 95.97% | +0.18pp | −0.30pp | 95.73% |
| Settled value | ₹1.40 Cr | +3.8% | +12.3% | ₹1.44 Cr |
| Average ticket | ₹1,232 | +2.4% | +0.8% | ₹1,192 |
| Technical declines | 0.483% | +0.06pp | −0.02pp | 0.458% |
| Business declines | 3.118% | −0.15pp | +0.27pp | 3.255% |
| Risk declines | 0.093% | −0.07pp | −0.01pp | 0.118% |
| Timeout declines | 0.246% | −0.04pp | +0.06pp | 0.344% |
| Retry share | 1.05% | −0.29pp | −0.10pp | 1.30% |
| Latency p95 | 1,226 ms | −1.2% | −3.3% | 1,246 ms |
| Active customers | 9,892 | +1.2% | +10.0% | 10,462 |
| Active merchants | 1,284 | −2.7% | −1.9% | 1,324 |

## What moved

- Product UPI Circle is compounding — attempts up 79% across the trailing window to 188 today, with success holding, so the growth is healthy and worth funding.
- Product UPI 123Pay is compounding — attempts up 38% across the trailing window to 76 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,362 | 37.0% | 95.58% | ₹47.15 L | +5.5% |
| UPI Person to Merchant | 3,478 | 29.5% | 95.66% | ₹31.09 L | +7.9% |
| UPI QR Payments | 1,789 | 15.2% | 96.76% | ₹8.49 L | −9.3% |
| UPI Lite | 924 | 7.8% | 99.03% | ₹86,763 | +18.9% |
| UPI AutoPay | 305 | 2.6% | 92.13% | ₹5.39 L | −1.9% |
| RuPay Credit on UPI | 249 | 2.1% | 94.38% | ₹11.02 L | +12.2% |
| UPI Circle | 188 | 1.6% | 97.34% | ₹1.48 L | +19.0% |
| Credit on UPI | 161 | 1.4% | 97.52% | ₹15.76 L | +3.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,761 | 96.33% | 95.59% | ₹48.88 L | normal |
| HDFC Bank | 1,258 | 94.75% | 95.90% | ₹13.55 L | normal |
| Bank of Baroda | 899 | 96.44% | 95.58% | ₹9.52 L | normal |
| Union Bank of India | 822 | 95.13% | 95.09% | ₹9.32 L | normal |
| Punjab National Bank | 731 | 95.08% | 95.09% | ₹8.00 L | normal |
| ICICI Bank | 715 | 97.20% | 95.70% | ₹10.07 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,559 | 96.19% | 95.64% | ₹66.86 L | normal |
| Google Pay | 3,922 | 95.61% | 95.52% | ₹47.21 L | normal |
| Paytm | 985 | 96.35% | 95.50% | ₹10.80 L | normal |
| Navi | 410 | 95.61% | 95.52% | ₹4.03 L | normal |
| SuperMoney | 238 | 94.96% | 95.85% | ₹2.82 L | normal |
| BHIM | 116 | 100.00% | 94.88% | ₹1.26 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,445 | 96.66% | ₹38.06 L |
| Food & Beverage | 1,655 | 96.56% | ₹8.37 L |
| Mobility | 748 | 97.46% | ₹4.85 L |
| Bills | 706 | 94.62% | ₹8.17 L |
| Healthcare | 377 | 94.16% | ₹3.32 L |
| Digital | 185 | 93.51% | ₹83,776 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,505 | 29.7% | 95.72% | ₹44.53 L |
| North | 2,958 | 25.1% | 95.54% | ₹33.67 L |
| West | 2,919 | 24.7% | 96.37% | ₹34.73 L |
| East | 1,375 | 11.6% | 96.36% | ₹16.40 L |
| Central | 1,046 | 8.9% | 96.37% | ₹10.20 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 385 | 95.32% | ₹1.31 L |
| Vasant Wardrobe | Key Account | Retail | 70 | 92.86% | ₹1.28 L |
| Hampi Styles | Key Account | Retail | 36 | 97.22% | ₹89,457 |
| Vega Electronics | Large | Retail | 25 | 88.00% | ₹88,079 |
| Yamuna Restaurant | Key Account | Food & Beverage | 55 | 92.73% | ₹79,575 |
| Hampi Stores 2298 | Key Account | Retail | 106 | 96.23% | ₹77,466 |
| Urban Boutique | Key Account | Retail | 88 | 97.73% | ₹70,561 |
| Girnar Connect | Key Account | Bills | 134 | 95.52% | ₹52,126 |

## Failure analysis

Of 465 declined attempts, 368 were business declines (3.118% of attempts — balances, PINs and limits), 57 technical (0.483%), 29 timeouts (0.246%) and 11 risk declines (0.093%).

124 attempts were re-presentations of an earlier failure (1.05% of the day); 67.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 158 | 1.339% | 1.420% |
| ZM | Invalid UPI PIN | business | Customer | 115 | 0.974% | 1.123% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.441% | 0.403% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.195% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.195% | 0.169% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.144% | 0.178% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.110% | 0.124% |
| ZX | Mandate not found or revoked | business | PSP | 11 | 0.093% | 0.095% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 70 | 75 |
| Auto-reversals | 20 | 24 |
| Disputes / chargebacks | 8 | 10 |
| Value returned | ₹1.29 L | ₹96,246 |

## Customer behaviour

9,892 distinct customers transacted (+0.9% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,987 | 3,375 | 1.13 | 95.73% | ₹1,102 |
| power | 2,111 | 2,799 | 1.33 | 96.03% | ₹1,752 |
| merchant_heavy | 2,287 | 2,749 | 1.20 | 96.03% | ₹975 |
| small_ticket | 1,494 | 1,827 | 1.22 | 96.00% | ₹562 |
| occasional | 793 | 820 | 1.03 | 96.46% | ₹1,755 |
| new | 196 | 209 | 1.07 | 96.17% | ₹805 |
| dormant_returning | 24 | 24 | 1.00 | 91.67% | ₹584 |

## Operational events

- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 79% across the trailing window to 188 today, with success holding, so the growth is healthy and worth funding.
- Product UPI 123Pay is compounding — attempts up 38% across the trailing window to 76 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

17 March ran on trend at 95.97% success and ₹1.40 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 79% across the trailing window to 188 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,803, successes=11,327, failed=465, pending=11, settled_value_inr=13,953,727.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=188; window_growth_pct=79.1; success_rate=97.34
- products: product_name=UPI 123Pay; attempts=76; window_growth_pct=38; success_rate=96.05
- banks: payer_bank=Yes Bank; attempts=435; success_rate=97.7; own_median=95.44; z=2.08
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31

Refs: enterprise_data/warehouse/transactions, RPT-D71-DAILY, enterprise_data/warehouse/reference/incidents.parquet
