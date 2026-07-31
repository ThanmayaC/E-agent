---
id: RPT-D78-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 23 Mar 2026)

**Report ID:** RPT-D78-DAILY · **Day 78 of 206** · **Derived from:** 10,868 transaction rows queried live from the warehouse

## Summary

The rail took **10,868 payment attempts** on Monday 23 March 2026 (Working day) and settled **₹1.28 Cr** across 10,399 successful payments. Volume was −3.9% on yesterday and −6.9% on the same weekday last week. Success closed at **95.68%**, in line with the trailing 28-day median of 95.79%.

Product UPI Circle is compounding — attempts up 78% across the trailing window to 164 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,868 | −3.9% | −6.9% | 12,737 |
| Successful payments | 10,399 | −4.2% | −7.0% | 12,203 |
| Success rate | 95.68% | −0.26pp | −0.11pp | 95.78% |
| Settled value | ₹1.28 Cr | +20.2% | −4.7% | ₹1.43 Cr |
| Average ticket | ₹1,233 | +25.4% | +2.5% | ₹1,175 |
| Technical declines | 0.340% | −0.04pp | −0.08pp | 0.448% |
| Business declines | 3.570% | +0.25pp | +0.30pp | 3.228% |
| Risk declines | 0.129% | +0.08pp | −0.03pp | 0.121% |
| Timeout declines | 0.212% | +0.01pp | −0.07pp | 0.327% |
| Retry share | 1.39% | +0.36pp | +0.05pp | 1.26% |
| Latency p95 | 1,235 ms | +1.5% | −0.5% | 1,240 ms |
| Active customers | 9,265 | −3.1% | −5.2% | 10,521 |
| Active merchants | 1,303 | +2.4% | −1.3% | 1,324 |

## What moved

- Product UPI Circle is compounding — attempts up 78% across the trailing window to 164 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Lite is compounding — attempts up 42% across the trailing window to 859 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,715 | 34.2% | 94.97% | ₹37.15 L | −16.7% |
| UPI Person to Merchant | 3,219 | 29.6% | 96.30% | ₹30.99 L | −7.8% |
| UPI QR Payments | 1,859 | 17.1% | 96.18% | ₹7.61 L | −14.0% |
| UPI Lite | 859 | 7.9% | 98.72% | ₹80,550 | −6.2% |
| UPI AutoPay | 297 | 2.7% | 91.58% | ₹5.39 L | −5.0% |
| RuPay Credit on UPI | 259 | 2.4% | 91.89% | ₹11.49 L | +16.9% |
| Credit on UPI | 183 | 1.7% | 96.72% | ₹13.70 L | +23.2% |
| UPI Circle | 164 | 1.5% | 92.68% | ₹1.07 L | −9.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,432 | 95.75% | 95.65% | ₹43.00 L | normal |
| HDFC Bank | 1,140 | 95.44% | 95.79% | ₹15.40 L | normal |
| Bank of Baroda | 863 | 94.79% | 95.58% | ₹9.81 L | normal |
| Union Bank of India | 738 | 94.58% | 95.58% | ₹6.26 L | normal |
| Axis Bank | 670 | 94.93% | 95.98% | ₹8.68 L | normal |
| Punjab National Bank | 666 | 96.25% | 95.23% | ₹7.88 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,118 | 96.21% | 95.93% | ₹61.11 L | normal |
| Google Pay | 3,575 | 95.52% | 95.76% | ₹41.46 L | normal |
| Paytm | 865 | 95.14% | 95.65% | ₹11.45 L | normal |
| Navi | 425 | 92.94% | 95.75% | ₹3.69 L | ⚠ outlier |
| SuperMoney | 216 | 93.98% | 95.85% | ₹3.94 L | normal |
| BHIM | 115 | 96.52% | 95.28% | ₹1.16 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,084 | 96.14% | ₹35.37 L |
| Food & Beverage | 1,738 | 96.55% | ₹8.25 L |
| Mobility | 787 | 97.08% | ₹4.11 L |
| Bills | 671 | 94.93% | ₹6.50 L |
| Healthcare | 347 | 96.83% | ₹2.50 L |
| Digital | 173 | 96.53% | ₹73,346 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,189 | 29.3% | 95.14% | ₹40.73 L |
| North | 2,797 | 25.7% | 96.17% | ₹28.57 L |
| West | 2,741 | 25.2% | 95.88% | ₹37.54 L |
| East | 1,216 | 11.2% | 96.22% | ₹13.90 L |
| Central | 925 | 8.5% | 94.81% | ₹7.46 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 100.00% | ₹2.39 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 88.24% | ₹1.35 L |
| Hampi Stores 2298 | Key Account | Retail | 101 | 97.03% | ₹1.15 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 96.77% | ₹96,351 |
| Ujjwal Water Board | Key Account | Bills | 26 | 100.00% | ₹92,832 |
| Rapid Bazaar | Key Account | Retail | 294 | 96.26% | ₹84,755 |
| Hampi Styles | Key Account | Retail | 38 | 97.37% | ₹81,842 |
| Kaveri Trading | Large | Retail | 46 | 97.83% | ₹81,367 |

## Failure analysis

Of 462 declined attempts, 388 were business declines (3.570% of attempts — balances, PINs and limits), 37 technical (0.340%), 23 timeouts (0.212%) and 14 risk declines (0.129%).

151 attempts were re-presentations of an earlier failure (1.39% of the day); 62.3% of them succeeded.

- Decline code UX (Mandate execution outside permitted window) fired 19 times — 0.175% of attempts against a trailing 0.089%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 149 | 1.371% | 1.084% |
| Z9 | Insufficient funds | business | Customer | 144 | 1.325% | 1.346% |
| ZA | Transaction declined by customer | business | Customer | 39 | 0.359% | 0.394% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.202% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.193% | 0.179% |
| UX | Mandate execution outside permitted window | business | PSP | 19 | 0.175% | 0.089% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 11 | 0.101% | 0.097% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 11 | 0.101% | 0.164% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 73 | 74 |
| Auto-reversals | 18 | 24 |
| Disputes / chargebacks | 7 | 10 |
| Value returned | ₹1.33 L | ₹1.04 L |

## Customer behaviour

9,265 distinct customers transacted (−8.2% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,768 | 3,095 | 1.12 | 95.90% | ₹1,238 |
| power | 1,991 | 2,580 | 1.30 | 95.85% | ₹1,731 |
| merchant_heavy | 2,145 | 2,519 | 1.17 | 95.24% | ₹873 |
| small_ticket | 1,394 | 1,662 | 1.19 | 95.85% | ₹601 |
| occasional | 779 | 815 | 1.05 | 95.34% | ₹1,454 |
| new | 162 | 171 | 1.06 | 96.49% | ₹749 |
| dormant_returning | 26 | 26 | 1.00 | 92.31% | ₹472 |

## Operational events

- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 78% across the trailing window to 164 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code UX (Mandate execution outside permitted window) fired 19 times — 0.175% of attempts against a trailing 0.089%. Owner: PSP.
- App Navi ran at 92.94% success on 425 attempts (3.9% of the day), 2.81pp down its own 28-day median.
- Product RuPay Credit on UPI ran at 91.89% success on 259 attempts (2.4% of the day), 4.17pp down its own 28-day median.
- Product UPI Circle ran at 92.68% success on 164 attempts (1.5% of the day), 3.74pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 42% across the trailing window to 859 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

23 March ran on trend at 95.68% success and ₹1.28 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 78% across the trailing window to 164 today, but success is slipping as it scales, so the growth is outrunning its reliability. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,868, successes=10,399, failed=462, pending=7, settled_value_inr=12,819,667.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=164; window_growth_pct=78.4; success_rate=92.68
- products: product_name=UPI Lite; attempts=859; window_growth_pct=41.6; success_rate=98.72
- failures: failure_code=UX; count=19; rate_pct=0.17; trailing_rate_pct=0.09; owner=PSP; z=2.59
- psps: payer_psp=Navi; attempts=425; success_rate=92.94; own_median=95.75; z=-3.14
- products: product_name=RuPay Credit on UPI; attempts=259; success_rate=91.89; own_median=96.06; z=-2.78
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- products: product_name=UPI Circle; attempts=164; success_rate=92.68; own_median=96.42; z=-2.67

Refs: enterprise_data/warehouse/transactions, RPT-D77-DAILY, enterprise_data/warehouse/reference/incidents.parquet
