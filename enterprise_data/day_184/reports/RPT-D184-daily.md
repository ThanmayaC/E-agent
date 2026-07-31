---
id: RPT-D184-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 07 Jul 2026)

**Report ID:** RPT-D184-DAILY · **Day 184 of 206** · **Derived from:** 16,497 transaction rows queried live from the warehouse

## Summary

The rail took **16,497 payment attempts** on Tuesday 07 July 2026 (Working day) and settled **₹2.32 Cr** across 15,946 successful payments. Volume was −1.5% on yesterday and −5.0% on the same weekday last week. Success closed at **96.66%**, above the trailing 28-day median of 96.16%.

Category Bills carried 1,829 attempts, 115% up its trailing median and 15.5% of the day's volume. Product UPI Lite is compounding — attempts up 48% across the trailing window to 2,584 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,497 | −1.5% | −5.0% | 17,616 |
| Successful payments | 15,946 | −1.6% | −4.3% | 16,897 |
| Success rate | 96.66% | −0.12pp | +0.72pp | 95.98% |
| Settled value | ₹2.32 Cr | −0.9% | −10.1% | ₹2.26 Cr |
| Average ticket | ₹1,455 | +0.8% | −6.1% | ₹1,338 |
| Technical declines | 0.394% | −0.06pp | −0.06pp | 0.524% |
| Business declines | 2.503% | +0.19pp | −0.54pp | 2.636% |
| Risk declines | 0.073% | −0.08pp | −0.03pp | 0.112% |
| Timeout declines | 0.273% | +0.03pp | −0.10pp | 0.666% |
| Retry share | 0.89% | −0.03pp | −0.53pp | 1.62% |
| Latency p95 | 1,311 ms | +3.0% | −4.1% | 1,338 ms |
| Active customers | 13,384 | −1.3% | −4.1% | 14,092 |
| Active merchants | 1,659 | +1.5% | +0.9% | 1,655 |

## What moved

- Category Bills carried 1,829 attempts, 115% up its trailing median and 15.5% of the day's volume.
- Product UPI Lite is compounding — attempts up 48% across the trailing window to 2,584 today, with success holding, so the growth is healthy and worth funding.
- App Google Pay ran at 97.01% success on 5,443 attempts (33.0% of the day), 0.79pp up its own 28-day median.
- Region South ran at 96.98% success on 4,908 attempts (29.8% of the day), 0.81pp up its own 28-day median.
- Product UPI 123Pay is compounding — attempts up 41% across the trailing window to 115 today, with success holding, so the growth is healthy and worth funding.
- Region West ran at 96.86% success on 4,018 attempts (24.4% of the day), 0.90pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,706 | 28.5% | 95.37% | ₹51.95 L | +12.7% |
| UPI Person to Merchant | 3,831 | 23.2% | 96.37% | ₹38.60 L | +11.4% |
| UPI QR Payments | 2,662 | 16.1% | 97.26% | ₹13.18 L | +8.2% |
| UPI Lite | 2,584 | 15.7% | 99.19% | ₹2.49 L | +13.4% |
| UPI Circle | 865 | 5.2% | 97.11% | ₹7.93 L | +8.9% |
| Credit on UPI | 487 | 3.0% | 95.48% | ₹48.75 L | +3.5% |
| RuPay Credit on UPI | 406 | 2.5% | 98.28% | ₹23.61 L | +10.3% |
| UPI AutoPay | 377 | 2.3% | 92.57% | ₹7.21 L | +0.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,182 | 96.26% | 96.16% | ₹72.35 L | normal |
| HDFC Bank | 1,753 | 97.26% | 96.37% | ₹30.15 L | normal |
| Bank of Baroda | 1,304 | 97.16% | 96.21% | ₹18.97 L | normal |
| Union Bank of India | 1,118 | 96.42% | 96.00% | ₹13.09 L | normal |
| Axis Bank | 1,060 | 97.08% | 96.10% | ₹17.83 L | normal |
| Punjab National Bank | 1,017 | 96.17% | 95.91% | ₹12.69 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,823 | 96.25% | 96.13% | ₹1.12 Cr | normal |
| Google Pay | 5,443 | 97.01% | 96.21% | ₹78.11 L | ⚠ outlier |
| Paytm | 1,349 | 97.33% | 95.98% | ₹16.33 L | normal |
| Navi | 582 | 97.59% | 96.34% | ₹7.59 L | normal |
| SuperMoney | 339 | 96.17% | 95.51% | ₹3.64 L | normal |
| BHIM | 161 | 95.03% | 95.87% | ₹2.83 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,458 | 96.86% | ₹56.38 L |
| Food & Beverage | 2,662 | 97.60% | ₹12.81 L |
| Bills | 1,829 | 97.10% | ₹18.95 L |
| Mobility | 1,392 | 98.35% | ₹7.64 L |
| Healthcare | 575 | 97.22% | ₹8.08 L |
| Digital | 313 | 95.85% | ₹1.68 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,908 | 29.8% | 96.98% | ₹74.26 L |
| North | 4,230 | 25.6% | 96.38% | ₹60.89 L |
| West | 4,018 | 24.4% | 96.86% | ₹58.46 L |
| East | 2,001 | 12.1% | 96.40% | ₹23.29 L |
| Central | 1,340 | 8.1% | 96.12% | ₹15.09 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 35 | 88.57% | ₹2.91 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 98.65% | ₹2.11 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 74 | 98.65% | ₹1.86 L |
| Rapid Bazaar | Key Account | Retail | 418 | 97.85% | ₹1.44 L |
| Girnar Connect | Key Account | Bills | 317 | 98.42% | ₹1.25 L |
| Ujjwal Water Board | Key Account | Bills | 57 | 96.49% | ₹1.18 L |
| Hampi Styles | Key Account | Retail | 44 | 93.18% | ₹1.17 L |
| Urban Boutique | Key Account | Retail | 130 | 98.46% | ₹1.10 L |

## Failure analysis

Of 535 declined attempts, 413 were business declines (2.503% of attempts — balances, PINs and limits), 65 technical (0.394%), 45 timeouts (0.273%) and 12 risk declines (0.073%).

147 attempts were re-presentations of an earlier failure (0.89% of the day); 74.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 172 | 1.043% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 123 | 0.746% | 0.970% |
| ZA | Transaction declined by customer | business | Customer | 61 | 0.370% | 0.328% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.158% | 0.199% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.152% | 0.177% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.152% | 0.132% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.145% | 0.118% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.097% | 0.073% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 126 | 108 |
| Auto-reversals | 24 | 24 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹2.07 L | ₹1.71 L |

## Customer behaviour

13,384 distinct customers transacted (+11.4% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,131 | 4,770 | 1.15 | 96.83% | ₹1,447 |
| power | 2,867 | 4,041 | 1.41 | 96.81% | ₹1,846 |
| merchant_heavy | 3,091 | 3,798 | 1.23 | 96.52% | ₹1,327 |
| small_ticket | 1,991 | 2,508 | 1.26 | 96.37% | ₹814 |
| occasional | 1,056 | 1,110 | 1.05 | 96.67% | ₹1,416 |
| new | 218 | 240 | 1.10 | 95.42% | ₹677 |
| dormant_returning | 30 | 30 | 1.00 | 100.00% | ₹855 |

## Operational events

- **MAINT-0087** (Sev-3) — Union Bank of India scheduled CBS maintenance, scoped to Union Bank of India between 01:00 and 05:00. Union Bank of India runs its announced core-banking maintenance slot every 35 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **CMP-0052** (Sev-3) — Hospitals cashback campaign, scoped to 8062. A cashback campaign across Hospitals merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Lite is compounding — attempts up 48% across the trailing window to 2,584 today, with success holding, so the growth is healthy and worth funding.
- Product UPI 123Pay is compounding — attempts up 41% across the trailing window to 115 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 07 July: success came in 0.50pp above baseline at 96.66% on 16,497 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,497, successes=15,946, failed=535, pending=16, settled_value_inr=23,198,849.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,829; own_median=852; z=7.62
- products: product_name=UPI Lite; attempts=2,584; window_growth_pct=48.1; success_rate=99.19
- psps: payer_psp=Google Pay; attempts=5,443; success_rate=97.01; own_median=96.21; z=2.17
- geography: region=South; attempts=4,908; success_rate=96.98; own_median=96.18; z=2.09
- products: product_name=UPI 123Pay; attempts=115; window_growth_pct=40.6; success_rate=98.26
- geography: region=West; attempts=4,018; success_rate=96.86; own_median=95.96; z=2.17
- incidents: event_id=MAINT-0087; kind=maintenance_window; severity=Sev-3; window=2026-01-13 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- incidents: event_id=CMP-0052; kind=merchant_campaign; severity=Sev-3; window=2026-07-04 to 2026-07-07; success_impact_pp=-0.15; volume_impact_pct=61.4
- categories: mcc_category=Digital; attempts=313; own_median=223; z=2.29
- categories: mcc_category=Travel; attempts=146; success_rate=98.63; own_median=94.8; z=2.37

Refs: enterprise_data/warehouse/transactions, RPT-D183-DAILY, enterprise_data/warehouse/reference/incidents.parquet
