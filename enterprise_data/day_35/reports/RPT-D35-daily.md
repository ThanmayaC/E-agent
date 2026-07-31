---
id: RPT-D35-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 08 Feb 2026)

**Report ID:** RPT-D35-DAILY · **Day 35 of 206** · **Derived from:** 10,420 transaction rows queried live from the warehouse

## Summary

The rail took **10,420 payment attempts** on Sunday 08 February 2026 (Weekend) and settled **₹1.02 Cr** across 9,941 successful payments. Volume was −18.0% on yesterday and −13.6% on the same weekday last week. Success closed at **95.40%**, in line with the trailing 28-day median of 95.31%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,420 | −18.0% | −13.6% | 11,533 |
| Successful payments | 9,941 | −18.7% | −13.6% | 11,039 |
| Success rate | 95.40% | −0.89pp | −0.01pp | 95.70% |
| Settled value | ₹1.02 Cr | −31.2% | −17.7% | ₹1.33 Cr |
| Average ticket | ₹1,025 | −15.3% | −4.7% | ₹1,206 |
| Technical declines | 0.355% | +0.08pp | −0.26pp | 0.391% |
| Business declines | 3.714% | +0.79pp | +0.31pp | 3.379% |
| Risk declines | 0.173% | +0.02pp | −0.01pp | 0.162% |
| Timeout declines | 0.250% | −0.03pp | +0.02pp | 0.257% |
| Retry share | 1.23% | +0.32pp | −0.07pp | 1.20% |
| Latency p95 | 1,194 ms | −5.1% | −1.3% | 1,242 ms |
| Active customers | 8,848 | −15.5% | −12.0% | 9,646 |
| Active merchants | 1,212 | −8.2% | −5.8% | 1,276 |

## What moved

- Product UPI Lite is compounding — attempts up 34% across the trailing window to 831 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 30% across the trailing window to 49 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,745 | 35.9% | 94.55% | ₹38.70 L | −6.2% |
| UPI Person to Merchant | 3,080 | 29.6% | 95.65% | ₹28.10 L | −0.4% |
| UPI QR Payments | 1,924 | 18.5% | 96.36% | ₹8.00 L | +7.4% |
| UPI Lite | 831 | 8.0% | 99.16% | ₹76,585 | +19.7% |
| UPI AutoPay | 297 | 2.9% | 86.87% | ₹4.75 L | −1.7% |
| RuPay Credit on UPI | 107 | 1.0% | 93.46% | ₹6.24 L | −45.4% |
| UPI Circle | 101 | 1.0% | 98.02% | ₹90,767 | +3.1% |
| UPI Lite Auto Top-Up | 80 | 0.8% | 96.25% | ₹86,083 | −4.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,378 | 95.41% | 95.24% | ₹32.67 L | normal |
| HDFC Bank | 1,135 | 96.21% | 95.94% | ₹11.12 L | normal |
| Bank of Baroda | 781 | 95.39% | 94.70% | ₹7.23 L | normal |
| Union Bank of India | 724 | 93.78% | 94.72% | ₹7.76 L | normal |
| Axis Bank | 647 | 94.59% | 95.19% | ₹5.68 L | normal |
| Punjab National Bank | 619 | 95.96% | 94.71% | ₹7.06 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,951 | 95.98% | 95.14% | ₹48.15 L | normal |
| Google Pay | 3,428 | 94.84% | 95.35% | ₹32.58 L | normal |
| Paytm | 876 | 94.52% | 94.89% | ₹9.53 L | normal |
| Navi | 375 | 94.13% | 95.86% | ₹5.52 L | normal |
| SuperMoney | 190 | 96.32% | 96.18% | ₹1.36 L | normal |
| BHIM | 106 | 95.28% | 94.59% | ₹73,659 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,738 | 96.06% | ₹25.67 L |
| Food & Beverage | 1,725 | 96.75% | ₹7.80 L |
| Mobility | 760 | 96.97% | ₹4.20 L |
| Bills | 624 | 94.23% | ₹5.53 L |
| Healthcare | 354 | 96.05% | ₹2.48 L |
| Digital | 179 | 93.30% | ₹96,175 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,036 | 29.1% | 95.59% | ₹27.37 L |
| North | 2,666 | 25.6% | 94.86% | ₹25.33 L |
| West | 2,568 | 24.6% | 96.03% | ₹24.98 L |
| East | 1,214 | 11.7% | 94.81% | ₹15.89 L |
| Central | 936 | 9.0% | 95.41% | ₹8.36 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 100.00% | ₹1.71 L |
| Rapid Bazaar | Key Account | Retail | 328 | 97.87% | ₹1.70 L |
| Vasant Wardrobe | Key Account | Retail | 53 | 88.68% | ₹1.14 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 82 | 93.90% | ₹94,727 |
| Girnar Connect | Key Account | Bills | 113 | 97.35% | ₹52,360 |
| Urban Boutique | Key Account | Retail | 82 | 96.34% | ₹51,342 |
| Hampi Stores 2298 | Key Account | Retail | 105 | 91.43% | ₹50,326 |
| Ujjwal Water Board | Key Account | Bills | 27 | 96.30% | ₹44,950 |

## Failure analysis

Of 468 declined attempts, 387 were business declines (3.714% of attempts — balances, PINs and limits), 37 technical (0.355%), 26 timeouts (0.250%) and 18 risk declines (0.173%).

128 attempts were re-presentations of an earlier failure (1.23% of the day); 60.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 161 | 1.545% | 1.491% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 1.296% | 1.139% |
| ZA | Transaction declined by customer | business | Customer | 39 | 0.374% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.269% | 0.237% |
| U30 | Debit failed at remitter bank | technical | Issuer | 16 | 0.154% | 0.237% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 14 | 0.134% | 0.113% |
| UX | Mandate execution outside permitted window | business | PSP | 11 | 0.106% | 0.113% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 11 | 0.106% | 0.122% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 79 | 65 |
| Auto-reversals | 17 | 21 |
| Disputes / chargebacks | 4 | 3 |
| Value returned | ₹1.81 L | ₹1.13 L |

## Customer behaviour

8,848 distinct customers transacted (−0.5% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,715 | 3,084 | 1.14 | 95.33% | ₹962 |
| power | 1,848 | 2,405 | 1.30 | 94.93% | ₹1,317 |
| merchant_heavy | 2,060 | 2,402 | 1.17 | 96.25% | ₹965 |
| small_ticket | 1,307 | 1,569 | 1.20 | 94.96% | ₹474 |
| occasional | 716 | 742 | 1.04 | 95.55% | ₹1,113 |
| new | 174 | 189 | 1.09 | 94.71% | ₹745 |
| dormant_returning | 28 | 29 | 1.04 | 96.55% | ₹1,042 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Category Bills ran at 94.23% success on 624 attempts (9.3% of the day), 1.59pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 34% across the trailing window to 831 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 30% across the trailing window to 49 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

08 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 95.40% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,420, successes=9,941, failed=468, pending=11, settled_value_inr=10,193,301.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- products: product_name=UPI Lite; attempts=831; window_growth_pct=33.7; success_rate=99.16
- products: product_name=UPI International; attempts=49; window_growth_pct=30.3; success_rate=100
- categories: mcc_category=Bills; attempts=624; success_rate=94.23; own_median=95.82; z=-2.11
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=Credit on UPI; attempts=75; own_median=145; z=-2.86

Refs: enterprise_data/warehouse/transactions, RPT-D34-DAILY, enterprise_data/warehouse/reference/incidents.parquet
