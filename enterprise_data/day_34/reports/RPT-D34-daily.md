---
id: RPT-D34-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 07 Feb 2026)

**Report ID:** RPT-D34-DAILY · **Day 34 of 206** · **Derived from:** 12,706 transaction rows queried live from the warehouse

## Summary

The rail took **12,706 payment attempts** on Saturday 07 February 2026 (Weekend) and settled **₹1.48 Cr** across 12,235 successful payments. Volume was +4.2% on yesterday and +8.0% on the same weekday last week. Success closed at **96.29%**, above the trailing 28-day median of 95.31%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,706 | +4.2% | +8.0% | 11,692 |
| Successful payments | 12,235 | +4.6% | +8.4% | 11,196 |
| Success rate | 96.29% | +0.36pp | +0.38pp | 95.75% |
| Settled value | ₹1.48 Cr | +4.8% | +17.6% | ₹1.38 Cr |
| Average ticket | ₹1,211 | +0.2% | +8.5% | ₹1,232 |
| Technical declines | 0.275% | −0.06pp | −0.14pp | 0.396% |
| Business declines | 2.928% | −0.30pp | −0.10pp | 3.331% |
| Risk declines | 0.157% | −0.01pp | −0.05pp | 0.160% |
| Timeout declines | 0.275% | +0.01pp | −0.01pp | 0.259% |
| Retry share | 0.91% | −0.28pp | −0.10pp | 1.19% |
| Latency p95 | 1,259 ms | −0.1% | +3.6% | 1,249 ms |
| Active customers | 10,465 | +3.1% | +6.5% | 9,760 |
| Active merchants | 1,320 | +0.5% | +1.9% | 1,285 |

## What moved

- Success rate closed at 96.29%, 0.98pp up the trailing median — a 1.6-sigma move.
- Category Bills carried 1,415 attempts, 101% up its trailing median and 16.7% of the day's volume.
- Product UPI Person to Person ran at 95.72% success on 4,233 attempts (33.3% of the day), 1.08pp up its own 28-day median.
- Product UPI Person to Merchant carried 4,145 attempts, 34% up its trailing median and 32.6% of the day's volume.
- Product UPI International is compounding — attempts up 32% across the trailing window to 115 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 31% across the trailing window to 981 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,233 | 33.3% | 95.72% | ₹43.79 L | +6.1% |
| UPI Person to Merchant | 4,145 | 32.6% | 96.33% | ₹43.90 L | +34.1% |
| UPI QR Payments | 2,240 | 17.6% | 97.28% | ₹10.09 L | +25.0% |
| UPI Lite | 981 | 7.7% | 98.98% | ₹93,089 | +41.3% |
| UPI AutoPay | 290 | 2.3% | 90.69% | ₹4.59 L | −4.4% |
| RuPay Credit on UPI | 201 | 1.6% | 93.03% | ₹11.66 L | +4.7% |
| Credit on UPI | 146 | 1.1% | 96.58% | ₹12.62 L | +5.4% |
| UPI Circle | 131 | 1.0% | 96.95% | ₹1.07 L | +33.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,057 | 95.96% | 95.06% | ₹49.70 L | normal |
| HDFC Bank | 1,405 | 96.09% | 95.94% | ₹13.13 L | normal |
| Bank of Baroda | 902 | 96.23% | 94.70% | ₹10.06 L | normal |
| Union Bank of India | 865 | 97.57% | 94.72% | ₹9.51 L | ⚠ outlier |
| Punjab National Bank | 811 | 95.56% | 94.71% | ₹10.24 L | normal |
| Axis Bank | 768 | 96.48% | 95.19% | ₹9.02 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,947 | 96.35% | 95.14% | ₹70.47 L | normal |
| Google Pay | 4,171 | 96.09% | 95.35% | ₹47.34 L | normal |
| Paytm | 1,069 | 95.79% | 94.85% | ₹14.00 L | normal |
| Navi | 486 | 96.71% | 95.86% | ₹5.62 L | normal |
| SuperMoney | 246 | 97.15% | 96.18% | ₹3.08 L | normal |
| FamApp | 133 | 98.50% | 95.62% | ₹1.12 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,192 | 96.71% | ₹37.61 L |
| Food & Beverage | 1,922 | 97.29% | ₹8.05 L |
| Bills | 1,415 | 96.18% | ₹18.41 L |
| Mobility | 935 | 97.54% | ₹5.66 L |
| Healthcare | 395 | 97.22% | ₹3.29 L |
| Digital | 306 | 94.44% | ₹1.69 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,790 | 29.8% | 96.20% | ₹42.98 L |
| North | 3,192 | 25.1% | 96.18% | ₹39.73 L |
| West | 3,009 | 23.7% | 96.14% | ₹36.10 L |
| East | 1,625 | 12.8% | 96.68% | ₹19.45 L |
| Central | 1,090 | 8.6% | 96.79% | ₹9.87 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 23 | 100.00% | ₹3.99 L |
| Ujjwal Water Board | Key Account | Bills | 77 | 96.10% | ₹2.75 L |
| Vasant Wardrobe | Key Account | Retail | 69 | 95.65% | ₹1.96 L |
| Rapid Bazaar | Key Account | Retail | 356 | 96.91% | ₹1.33 L |
| Girnar Connect | Key Account | Bills | 248 | 97.58% | ₹1.19 L |
| Konark Boutique | Large | Retail | 26 | 92.31% | ₹81,656 |
| Hampi Stores 2298 | Key Account | Retail | 89 | 98.88% | ₹79,234 |
| Urban Boutique | Key Account | Retail | 99 | 98.99% | ₹70,794 |

## Failure analysis

Of 462 declined attempts, 372 were business declines (2.928% of attempts — balances, PINs and limits), 35 technical (0.275%), 35 timeouts (0.275%) and 20 risk declines (0.157%).

116 attempts were re-presentations of an earlier failure (0.91% of the day); 62.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 168 | 1.322% | 1.491% |
| ZM | Invalid UPI PIN | business | Customer | 114 | 0.897% | 1.139% |
| ZA | Transaction declined by customer | business | Customer | 57 | 0.449% | 0.428% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.157% | 0.166% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.134% | 0.111% |
| XH | Account does not exist / frozen | business | Issuer | 16 | 0.126% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 15 | 0.118% | 0.244% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.102% | 0.126% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 56 | 65 |
| Auto-reversals | 9 | 22 |
| Disputes / chargebacks | 6 | 3 |
| Value returned | ₹1.52 L | ₹1.06 L |

## Customer behaviour

10,465 distinct customers transacted (+17.7% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,248 | 3,706 | 1.14 | 96.52% | ₹1,260 |
| power | 2,179 | 2,949 | 1.35 | 96.37% | ₹1,658 |
| merchant_heavy | 2,396 | 2,900 | 1.21 | 96.52% | ₹959 |
| small_ticket | 1,586 | 2,013 | 1.27 | 95.98% | ₹600 |
| occasional | 838 | 899 | 1.07 | 95.11% | ₹1,233 |
| new | 191 | 211 | 1.10 | 97.16% | ₹651 |
| dormant_returning | 27 | 28 | 1.04 | 89.29% | ₹573 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI International is compounding — attempts up 32% across the trailing window to 115 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 31% across the trailing window to 981 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

07 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 96.29% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,706, successes=12,235, failed=462, pending=9, settled_value_inr=14,812,143.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- headline: success_rate=96.29; trailing_median=95.31; z=1.65
- categories: mcc_category=Bills; attempts=1,415; own_median=702.5; z=3.97
- products: product_name=UPI Person to Person; attempts=4,233; success_rate=95.72; own_median=94.65; z=2.04
- products: product_name=UPI Person to Merchant; attempts=4,145; own_median=3,092; z=2.75
- products: product_name=UPI International; attempts=115; window_growth_pct=31.8; success_rate=96.52
- products: product_name=UPI Lite; attempts=981; window_growth_pct=30.8; success_rate=98.98
- categories: mcc_category=Mobility; attempts=935; own_median=649.5; z=2.94
- banks: payer_bank=Union Bank of India; attempts=865; success_rate=97.57; own_median=94.72; z=2.23
- products: product_name=UPI Lite; attempts=981; own_median=694.5; z=2.42

Refs: enterprise_data/warehouse/transactions, RPT-D33-DAILY, enterprise_data/warehouse/reference/incidents.parquet
