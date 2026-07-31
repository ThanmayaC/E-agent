---
id: RPT-D126-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 10 May 2026)

**Report ID:** RPT-D126-DAILY · **Day 126 of 206** · **Derived from:** 13,649 transaction rows queried live from the warehouse

## Summary

The rail took **13,649 payment attempts** on Sunday 10 May 2026 (Weekend) and settled **₹1.59 Cr** across 13,076 successful payments. Volume was −17.1% on yesterday and −6.0% on the same weekday last week. Success closed at **95.80%**, above the trailing 28-day median of 95.53%.

Product UPI Circle is compounding — attempts up 66% across the trailing window to 589 today, but success is slipping as it scales, so the growth is outrunning its reliability. Product UPI Lite is compounding — attempts up 58% across the trailing window to 1,723 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,649 | −17.1% | −6.0% | 15,486 |
| Successful payments | 13,076 | −16.9% | −6.3% | 14,868 |
| Success rate | 95.80% | +0.16pp | −0.32pp | 96.01% |
| Settled value | ₹1.59 Cr | −14.4% | −3.2% | ₹2.02 Cr |
| Average ticket | ₹1,218 | +3.1% | +3.3% | ₹1,357 |
| Technical declines | 0.447% | −0.11pp | −0.02pp | 0.504% |
| Business declines | 3.180% | −0.01pp | +0.38pp | 2.926% |
| Risk declines | 0.110% | +0.00pp | +0.01pp | 0.124% |
| Timeout declines | 0.322% | −0.08pp | −0.07pp | 0.329% |
| Retry share | 1.67% | +0.05pp | +0.26pp | 1.31% |
| Latency p95 | 1,212 ms | −2.4% | +0.2% | 1,241 ms |
| Active customers | 11,283 | −13.7% | −5.1% | 12,502 |
| Active merchants | 1,437 | −6.1% | −1.8% | 1,499 |

## What moved

- Product UPI Circle is compounding — attempts up 66% across the trailing window to 589 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Lite is compounding — attempts up 58% across the trailing window to 1,723 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,255 | 31.2% | 94.95% | ₹44.30 L | −2.9% |
| UPI Person to Merchant | 3,847 | 28.2% | 95.94% | ₹36.75 L | +10.4% |
| UPI QR Payments | 2,165 | 15.9% | 96.63% | ₹8.60 L | −7.7% |
| UPI Lite | 1,723 | 12.6% | 98.96% | ₹1.52 L | +30.0% |
| UPI Circle | 589 | 4.3% | 95.42% | ₹5.30 L | +59.6% |
| UPI AutoPay | 370 | 2.7% | 88.65% | ₹6.50 L | +13.7% |
| RuPay Credit on UPI | 195 | 1.4% | 93.85% | ₹8.67 L | −44.3% |
| Credit on UPI | 145 | 1.1% | 95.86% | ₹17.50 L | −45.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,305 | 96.05% | 95.67% | ₹45.96 L | normal |
| HDFC Bank | 1,418 | 96.26% | 95.96% | ₹15.65 L | normal |
| Bank of Baroda | 1,019 | 95.19% | 95.77% | ₹13.47 L | normal |
| Union Bank of India | 965 | 95.85% | 94.95% | ₹12.97 L | normal |
| Axis Bank | 867 | 96.66% | 95.87% | ₹10.96 L | normal |
| Punjab National Bank | 848 | 94.58% | 95.52% | ₹13.67 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,560 | 96.01% | 95.73% | ₹82.35 L | normal |
| Google Pay | 4,460 | 95.18% | 95.56% | ₹40.95 L | normal |
| Paytm | 1,089 | 96.14% | 95.42% | ₹16.81 L | normal |
| Navi | 508 | 96.06% | 95.40% | ₹6.44 L | normal |
| SuperMoney | 248 | 96.77% | 95.51% | ₹3.97 L | normal |
| BHIM | 151 | 96.69% | 95.24% | ₹2.40 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,854 | 96.26% | ₹35.68 L |
| Food & Beverage | 2,483 | 97.02% | ₹11.24 L |
| Mobility | 1,054 | 97.63% | ₹5.00 L |
| Bills | 805 | 95.40% | ₹8.14 L |
| Healthcare | 524 | 95.61% | ₹3.46 L |
| Digital | 245 | 93.06% | ₹1.22 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,018 | 29.4% | 95.67% | ₹53.86 L |
| North | 3,425 | 25.1% | 95.07% | ₹41.58 L |
| West | 3,369 | 24.7% | 96.17% | ₹37.24 L |
| East | 1,625 | 11.9% | 96.25% | ₹16.60 L |
| Central | 1,212 | 8.9% | 96.70% | ₹9.94 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 54 | 96.30% | ₹2.80 L |
| Rapid Bazaar | Key Account | Retail | 426 | 95.54% | ₹1.67 L |
| Vega Electronics | Large | Retail | 24 | 87.50% | ₹1.18 L |
| Hampi Styles | Key Account | Retail | 19 | 100.00% | ₹1.15 L |
| Girnar Connect | Key Account | Bills | 149 | 97.32% | ₹76,863 |
| Ujjwal Water Board | Key Account | Bills | 44 | 84.09% | ₹71,356 |
| Urban Boutique | Key Account | Retail | 95 | 95.79% | ₹66,943 |
| Hampi Stores 2298 | Key Account | Retail | 100 | 94.00% | ₹63,854 |

## Failure analysis

Of 554 declined attempts, 434 were business declines (3.180% of attempts — balances, PINs and limits), 61 technical (0.447%), 44 timeouts (0.322%) and 15 risk declines (0.110%).

228 attempts were re-presentations of an earlier failure (1.67% of the day); 62.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 166 | 1.216% | 1.054% |
| Z9 | Insufficient funds | business | Customer | 157 | 1.150% | 1.279% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.410% | 0.378% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.227% | 0.220% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.190% | 0.220% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.154% | 0.180% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.139% | 0.137% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.117% | 0.115% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 92 | 89 |
| Auto-reversals | 23 | 28 |
| Disputes / chargebacks | 11 | 11 |
| Value returned | ₹1.30 L | ₹1.43 L |

## Customer behaviour

11,283 distinct customers transacted (+1.7% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,459 | 3,964 | 1.15 | 95.96% | ₹1,339 |
| power | 2,402 | 3,289 | 1.37 | 95.68% | ₹1,725 |
| merchant_heavy | 2,599 | 3,118 | 1.20 | 96.09% | ₹895 |
| small_ticket | 1,701 | 2,094 | 1.23 | 95.27% | ₹445 |
| occasional | 912 | 961 | 1.05 | 95.84% | ₹1,081 |
| new | 186 | 198 | 1.06 | 95.45% | ₹737 |
| dormant_returning | 24 | 25 | 1.04 | 96.00% | ₹1,456 |

## Operational events

- **INC-SETL-0080** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **INC-BANK-0001** (Sev-3) — Yes Bank issuer decline spike, scoped to Yes Bank between 23:00 and 05:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 66% across the trailing window to 589 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Lite is compounding — attempts up 58% across the trailing window to 1,723 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

10 May was an incident day: INC-SETL-0080 was live and the rail closed at 95.80% success against a 95.53% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,649, successes=13,076, failed=554, pending=19, settled_value_inr=15,923,102.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=589; window_growth_pct=66.2; success_rate=95.42
- incidents: event_id=INC-SETL-0080; kind=settlement_delay; severity=Sev-2; window=2026-05-09 to 2026-05-10; success_impact_pp=-4.79; volume_impact_pct=-24.04
- products: product_name=UPI Lite; attempts=1,723; window_growth_pct=57.8; success_rate=98.96
- incidents: event_id=INC-BANK-0001; kind=bank_outage; severity=Sev-3; window=2026-05-08 to 2026-05-12; success_impact_pp=-6.2; volume_impact_pct=-5.5
- products: product_name=RuPay Credit on UPI; attempts=195; own_median=350; z=-3.17

Refs: enterprise_data/warehouse/transactions, RPT-D125-DAILY, enterprise_data/warehouse/reference/incidents.parquet
