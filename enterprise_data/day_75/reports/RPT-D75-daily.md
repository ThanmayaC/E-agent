---
id: RPT-D75-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 20 Mar 2026)

**Report ID:** RPT-D75-DAILY · **Day 75 of 206** · **Derived from:** 13,361 transaction rows queried live from the warehouse

## Summary

The rail took **13,361 payment attempts** on Friday 20 March 2026 (Eid al-Fitr (build-up)) and settled **₹1.42 Cr** across 12,834 successful payments. Volume was −2.0% on yesterday and +12.2% on the same weekday last week. Success closed at **96.06%**, above the trailing 28-day median of 95.72%.

Product UPI Circle is compounding — attempts up 96% across the trailing window to 192 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,361 | −2.0% | +12.2% | 12,764 |
| Successful payments | 12,834 | −2.1% | +12.6% | 12,228 |
| Success rate | 96.06% | −0.16pp | +0.38pp | 95.77% |
| Settled value | ₹1.42 Cr | −5.9% | +0.9% | ₹1.45 Cr |
| Average ticket | ₹1,110 | −3.9% | −10.4% | ₹1,187 |
| Technical declines | 0.412% | +0.02pp | −0.08pp | 0.454% |
| Business declines | 2.882% | −0.00pp | −0.40pp | 3.213% |
| Risk declines | 0.187% | +0.05pp | +0.04pp | 0.123% |
| Timeout declines | 0.367% | +0.08pp | −0.00pp | 0.340% |
| Retry share | 1.03% | −0.13pp | −0.02pp | 1.28% |
| Latency p95 | 1,227 ms | −0.5% | −0.5% | 1,244 ms |
| Active customers | 11,074 | +0.0% | +11.2% | 10,535 |
| Active merchants | 1,337 | −0.7% | +0.6% | 1,325 |

## What moved

- Product UPI Circle is compounding — attempts up 96% across the trailing window to 192 today, with success holding, so the growth is healthy and worth funding.
- Region North ran at 96.83% success on 3,349 attempts (25.1% of the day), 1.00pp up its own 28-day median.
- Product UPI 123Pay is compounding — attempts up 35% across the trailing window to 86 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,870 | 36.4% | 94.89% | ₹54.28 L | +11.4% |
| UPI Person to Merchant | 3,776 | 28.3% | 96.58% | ₹36.68 L | +8.7% |
| UPI QR Payments | 2,310 | 17.3% | 96.97% | ₹9.99 L | +10.7% |
| UPI Lite | 1,161 | 8.7% | 98.88% | ₹1.07 L | +36.8% |
| UPI AutoPay | 307 | 2.3% | 90.88% | ₹5.35 L | −1.3% |
| RuPay Credit on UPI | 222 | 1.7% | 94.59% | ₹8.43 L | +0.0% |
| UPI Circle | 192 | 1.4% | 99.48% | ₹1.74 L | +12.9% |
| Credit on UPI | 148 | 1.1% | 94.59% | ₹9.24 L | +0.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,156 | 95.57% | 95.65% | ₹44.51 L | normal |
| HDFC Bank | 1,522 | 95.86% | 95.79% | ₹14.34 L | normal |
| Bank of Baroda | 1,074 | 95.81% | 95.58% | ₹11.99 L | normal |
| Union Bank of India | 960 | 96.56% | 95.30% | ₹10.10 L | normal |
| Axis Bank | 830 | 97.47% | 95.84% | ₹9.31 L | ⚠ outlier |
| Punjab National Bank | 817 | 95.59% | 95.15% | ₹8.21 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,183 | 96.23% | 95.78% | ₹63.83 L | normal |
| Google Pay | 4,481 | 95.80% | 95.64% | ₹49.10 L | normal |
| Paytm | 1,120 | 96.07% | 95.50% | ₹13.05 L | normal |
| Navi | 499 | 95.39% | 95.68% | ₹5.56 L | normal |
| SuperMoney | 275 | 98.55% | 95.73% | ₹3.72 L | normal |
| BHIM | 153 | 93.46% | 95.28% | ₹1.20 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,859 | 96.71% | ₹38.11 L |
| Food & Beverage | 2,299 | 96.87% | ₹10.99 L |
| Mobility | 773 | 98.19% | ₹4.78 L |
| Bills | 680 | 96.91% | ₹9.44 L |
| Healthcare | 386 | 97.93% | ₹3.78 L |
| Digital | 179 | 94.97% | ₹84,444 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,988 | 29.8% | 96.39% | ₹45.49 L |
| North | 3,349 | 25.1% | 96.83% | ₹32.57 L |
| West | 3,282 | 24.6% | 95.52% | ₹34.47 L |
| East | 1,586 | 11.9% | 95.46% | ₹18.00 L |
| Central | 1,156 | 8.7% | 94.98% | ₹11.91 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 34 | 100.00% | ₹1.48 L |
| Vega Electronics | Large | Retail | 38 | 94.74% | ₹1.43 L |
| Vasant Wardrobe | Key Account | Retail | 97 | 98.97% | ₹1.35 L |
| Rapid Bazaar | Key Account | Retail | 400 | 97.50% | ₹1.19 L |
| Hampi Styles | Key Account | Retail | 52 | 94.23% | ₹1.03 L |
| Swift Mart 1738 | Key Account | Retail | 132 | 94.70% | ₹90,851 |
| Hampi Stores 2298 | Key Account | Retail | 110 | 96.36% | ₹81,544 |
| Trinetra Restaurant | Large | Food & Beverage | 35 | 97.14% | ₹66,817 |

## Failure analysis

Of 514 declined attempts, 385 were business declines (2.882% of attempts — balances, PINs and limits), 55 technical (0.412%), 49 timeouts (0.367%) and 25 risk declines (0.187%).

138 attempts were re-presentations of an earlier failure (1.03% of the day); 64.5% of them succeeded.

- Decline code U16 (Risk threshold exceeded at remitter) fired 25 times — 0.187% of attempts against a trailing 0.097%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.310% | 1.386% |
| ZM | Invalid UPI PIN | business | Customer | 119 | 0.891% | 1.098% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.277% | 0.397% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.240% | 0.228% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.195% | 0.171% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 25 | 0.187% | 0.097% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.172% | 0.178% |
| UX | Mandate execution outside permitted window | business | PSP | 15 | 0.112% | 0.090% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 62 | 76 |
| Auto-reversals | 17 | 24 |
| Disputes / chargebacks | 8 | 10 |
| Value returned | ₹61,313 | ₹1.07 L |

## Customer behaviour

11,074 distinct customers transacted (+11.4% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,380 | 3,904 | 1.16 | 95.82% | ₹1,168 |
| power | 2,334 | 3,137 | 1.34 | 96.11% | ₹1,485 |
| merchant_heavy | 2,511 | 3,007 | 1.20 | 96.11% | ₹814 |
| small_ticket | 1,706 | 2,114 | 1.24 | 96.55% | ₹510 |
| occasional | 883 | 924 | 1.05 | 96.00% | ₹1,375 |
| new | 235 | 250 | 1.06 | 95.20% | ₹781 |
| dormant_returning | 25 | 25 | 1.00 | 88.00% | ₹1,531 |

## Operational events

- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Decline code U16 (Risk threshold exceeded at remitter) fired 25 times — 0.187% of attempts against a trailing 0.097%. Owner: Issuer.

### Opportunities

- Product UPI Circle is compounding — attempts up 96% across the trailing window to 192 today, with success holding, so the growth is healthy and worth funding.
- Product UPI 123Pay is compounding — attempts up 35% across the trailing window to 86 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

20 March ran on trend at 96.06% success and ₹1.42 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 96% across the trailing window to 192 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,361, successes=12,834, failed=514, pending=13, settled_value_inr=14,243,620.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=192; window_growth_pct=96.5; success_rate=99.48
- geography: region=North; attempts=3,349; success_rate=96.83; own_median=95.84; z=2.55
- failures: failure_code=U16; count=25; rate_pct=0.19; trailing_rate_pct=0.1; owner=Issuer; z=2.61
- products: product_name=UPI 123Pay; attempts=86; window_growth_pct=34.8; success_rate=96.51
- incidents: event_id=MAINT-0085; kind=maintenance_window; severity=Sev-3; window=2026-01-23 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- categories: mcc_category=Mobility; attempts=773; success_rate=98.19; own_median=96.89; z=2.15
- banks: payer_bank=Axis Bank; attempts=830; success_rate=97.47; own_median=95.84; z=2.31
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- products: product_name=UPI Circle; attempts=192; success_rate=99.48; own_median=96.31; z=2.06

Refs: enterprise_data/warehouse/transactions, RPT-D74-DAILY, enterprise_data/warehouse/reference/incidents.parquet
