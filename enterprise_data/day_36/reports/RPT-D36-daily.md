---
id: RPT-D36-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-09T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 09 Feb 2026)

**Report ID:** RPT-D36-DAILY · **Day 36 of 206** · **Derived from:** 10,387 transaction rows queried live from the warehouse

## Summary

The rail took **10,387 payment attempts** on Monday 09 February 2026 (Working day) and settled **₹1.06 Cr** across 9,977 successful payments. Volume was −0.3% on yesterday and −14.2% on the same weekday last week. Success closed at **96.05%**, above the trailing 28-day median of 95.38%.

7 disputes were raised, 2.7 sigma above the trailing median of 3.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,387 | −0.3% | −14.2% | 11,406 |
| Successful payments | 9,977 | +0.4% | −13.9% | 10,921 |
| Success rate | 96.05% | +0.65pp | +0.33pp | 95.74% |
| Settled value | ₹1.06 Cr | +3.9% | −26.3% | ₹1.30 Cr |
| Average ticket | ₹1,062 | +3.6% | −14.4% | ₹1,190 |
| Technical declines | 0.337% | −0.02pp | −0.01pp | 0.385% |
| Business declines | 3.148% | −0.57pp | −0.10pp | 3.354% |
| Risk declines | 0.096% | −0.08pp | −0.14pp | 0.154% |
| Timeout declines | 0.241% | −0.01pp | −0.04pp | 0.256% |
| Retry share | 1.26% | +0.03pp | +0.05pp | 1.20% |
| Latency p95 | 1,280 ms | +7.2% | +2.6% | 1,246 ms |
| Active customers | 8,848 | +0.0% | −12.3% | 9,557 |
| Active merchants | 1,255 | +3.5% | −1.6% | 1,273 |

## What moved

- Product UPI Lite is compounding — attempts up 33% across the trailing window to 1,063 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 32% across the trailing window to 67 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,639 | 35.0% | 95.03% | ₹39.25 L | −8.8% |
| UPI Person to Merchant | 3,026 | 29.1% | 96.13% | ₹25.61 L | −2.1% |
| UPI QR Payments | 1,651 | 15.9% | 96.85% | ₹7.32 L | −8.2% |
| UPI Lite | 1,063 | 10.2% | 98.87% | ₹93,248 | +47.4% |
| UPI AutoPay | 303 | 2.9% | 92.74% | ₹5.43 L | +0.3% |
| RuPay Credit on UPI | 169 | 1.6% | 97.63% | ₹6.26 L | −13.8% |
| Credit on UPI | 145 | 1.4% | 94.48% | ₹8.03 L | +0.0% |
| UPI Circle | 117 | 1.1% | 98.29% | ₹82,053 | +15.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,286 | 96.26% | 95.34% | ₹32.59 L | normal |
| HDFC Bank | 1,160 | 95.60% | 96.02% | ₹12.25 L | normal |
| Bank of Baroda | 796 | 96.23% | 94.72% | ₹8.26 L | normal |
| Union Bank of India | 707 | 95.62% | 94.72% | ₹5.53 L | normal |
| Axis Bank | 658 | 96.50% | 95.13% | ₹6.10 L | normal |
| Punjab National Bank | 631 | 96.35% | 94.71% | ₹6.40 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,893 | 96.34% | 95.22% | ₹47.29 L | normal |
| Google Pay | 3,468 | 95.65% | 95.35% | ₹37.29 L | normal |
| Paytm | 840 | 96.19% | 94.89% | ₹9.30 L | normal |
| Navi | 345 | 95.07% | 95.86% | ₹3.40 L | normal |
| SuperMoney | 200 | 96.50% | 96.18% | ₹1.60 L | normal |
| BHIM | 129 | 96.12% | 94.86% | ₹1.04 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,843 | 96.62% | ₹27.66 L |
| Food & Beverage | 1,687 | 96.80% | ₹7.54 L |
| Mobility | 752 | 97.61% | ₹3.73 L |
| Bills | 665 | 96.54% | ₹5.59 L |
| Healthcare | 349 | 97.42% | ₹2.39 L |
| Digital | 188 | 95.74% | ₹79,817 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,117 | 30.0% | 96.18% | ₹29.75 L |
| North | 2,662 | 25.6% | 96.47% | ₹29.66 L |
| West | 2,494 | 24.0% | 95.95% | ₹25.53 L |
| East | 1,214 | 11.7% | 95.47% | ₹12.42 L |
| Central | 900 | 8.7% | 95.44% | ₹8.59 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 24 | 95.83% | ₹1.79 L |
| Vasant Wardrobe | Key Account | Retail | 60 | 96.67% | ₹1.76 L |
| Rapid Bazaar | Key Account | Retail | 293 | 96.93% | ₹1.64 L |
| Konark Boutique | Large | Retail | 32 | 93.75% | ₹73,555 |
| Ujjwal Water Board | Key Account | Bills | 41 | 100.00% | ₹65,642 |
| Swift Tiffin | Key Account | Food & Beverage | 80 | 96.25% | ₹61,626 |
| Hampi Stores 2298 | Key Account | Retail | 95 | 96.84% | ₹60,227 |
| Girnar Connect | Key Account | Bills | 115 | 97.39% | ₹48,206 |

## Failure analysis

Of 397 declined attempts, 327 were business declines (3.148% of attempts — balances, PINs and limits), 35 technical (0.337%), 25 timeouts (0.241%) and 10 risk declines (0.096%).

131 attempts were re-presentations of an earlier failure (1.26% of the day); 67.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 136 | 1.309% | 1.491% |
| ZM | Invalid UPI PIN | business | Customer | 117 | 1.126% | 1.139% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.347% | 0.423% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.202% | 0.237% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 14 | 0.135% | 0.166% |
| U30 | Debit failed at remitter bank | technical | Issuer | 12 | 0.116% | 0.234% |
| U69 | Beneficiary bank offline | technical | Issuer | 11 | 0.106% | 0.100% |
| UX | Mandate execution outside permitted window | business | PSP | 9 | 0.087% | 0.107% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 59 | 66 |
| Auto-reversals | 13 | 21 |
| Disputes / chargebacks | 7 | 3 |
| Value returned | ₹47,693 | ₹1.15 L |

## Customer behaviour

8,848 distinct customers transacted (−0.5% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,652 | 2,971 | 1.12 | 96.36% | ₹1,089 |
| power | 1,903 | 2,435 | 1.28 | 95.89% | ₹1,438 |
| merchant_heavy | 2,011 | 2,367 | 1.18 | 96.03% | ₹892 |
| small_ticket | 1,349 | 1,624 | 1.20 | 96.49% | ₹437 |
| occasional | 714 | 749 | 1.05 | 94.79% | ₹1,132 |
| new | 189 | 211 | 1.12 | 95.73% | ₹762 |
| dormant_returning | 30 | 30 | 1.00 | 90.00% | ₹940 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0021** (Sev-2) — Bank of Baroda issuer decline spike, scoped to Bank of Baroda between 10:00 and 16:00. Bank of Baroda core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 7 disputes were raised, 2.7 sigma above the trailing median of 3.

### Opportunities

- Product UPI Lite is compounding — attempts up 33% across the trailing window to 1,063 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 32% across the trailing window to 67 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

09 February was an incident day: INC-FRAUD-0049, INC-BANK-0021 were live and the rail closed at 96.05% success against a 95.38% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-09` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,387, successes=9,977, failed=397, pending=13, settled_value_inr=10,593,788.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=7; trailing_median=3; z=2.7
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- incidents: event_id=INC-BANK-0021; kind=bank_outage; severity=Sev-2; window=2026-02-09 to 2026-02-11; success_impact_pp=-9.27; volume_impact_pct=-8.22
- products: product_name=UPI Lite; attempts=1,063; window_growth_pct=32.7; success_rate=98.87
- products: product_name=UPI International; attempts=67; window_growth_pct=31.5; success_rate=100
- products: product_name=UPI Lite; attempts=1,063; own_median=721; z=2.43
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24

Refs: enterprise_data/warehouse/transactions, RPT-D35-DAILY, enterprise_data/warehouse/reference/incidents.parquet
