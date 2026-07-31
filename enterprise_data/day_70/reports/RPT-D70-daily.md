---
id: RPT-D70-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 15 Mar 2026)

**Report ID:** RPT-D70-DAILY · **Day 70 of 206** · **Derived from:** 10,365 transaction rows queried live from the warehouse

## Summary

The rail took **10,365 payment attempts** on Sunday 15 March 2026 (Weekend) and settled **₹1.05 Cr** across 9,842 successful payments. Volume was −15.8% on yesterday and −11.6% on the same weekday last week. Success closed at **94.95%**, below the trailing 28-day median of 95.64%.

Decline code ZM (Invalid UPI PIN) fired 152 times — 1.466% of attempts against a trailing 1.109%. Owner: Customer. Product UPI Circle is compounding — attempts up 81% across the trailing window to 171 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,365 | −15.8% | −11.6% | 12,791 |
| Successful payments | 9,842 | −16.5% | −12.3% | 12,246 |
| Success rate | 94.95% | −0.81pp | −0.66pp | 95.71% |
| Settled value | ₹1.05 Cr | −20.7% | −15.2% | ₹1.45 Cr |
| Average ticket | ₹1,069 | −5.0% | −3.3% | ₹1,189 |
| Technical declines | 0.482% | +0.03pp | −0.07pp | 0.459% |
| Business declines | 3.965% | +0.72pp | +0.73pp | 3.263% |
| Risk declines | 0.087% | −0.00pp | +0.01pp | 0.117% |
| Timeout declines | 0.386% | +0.07pp | −0.01pp | 0.354% |
| Retry share | 1.56% | +0.30pp | +0.04pp | 1.32% |
| Latency p95 | 1,226 ms | +3.2% | +1.7% | 1,247 ms |
| Active customers | 8,782 | −14.2% | −10.7% | 10,546 |
| Active merchants | 1,254 | −5.2% | −2.6% | 1,327 |

## What moved

- Product UPI Circle is compounding — attempts up 81% across the trailing window to 171 today, with success holding, so the growth is healthy and worth funding.
- Success rate closed at 94.95%, 0.69pp down the trailing median — a 1.9-sigma move.
- Product UPI Person to Person ran at 93.80% success on 3,663 attempts (35.3% of the day), 1.22pp down its own 28-day median.
- Region West ran at 94.21% success on 2,470 attempts (23.8% of the day), 1.37pp down its own 28-day median.
- Product UPI 123Pay is compounding — attempts up 39% across the trailing window to 48 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Merchant ran at 95.28% success on 2,969 attempts (28.6% of the day), 0.64pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,663 | 35.3% | 93.80% | ₹37.52 L | −11.4% |
| UPI Person to Merchant | 2,969 | 28.6% | 95.28% | ₹24.14 L | −7.9% |
| UPI QR Payments | 1,933 | 18.6% | 96.74% | ₹7.62 L | −4.8% |
| UPI Lite | 749 | 7.2% | 98.13% | ₹69,244 | −3.6% |
| UPI AutoPay | 311 | 3.0% | 86.50% | ₹5.16 L | +0.5% |
| UPI Circle | 171 | 1.6% | 97.08% | ₹1.19 L | +17.9% |
| RuPay Credit on UPI | 161 | 1.6% | 95.03% | ₹10.82 L | −26.5% |
| Credit on UPI | 126 | 1.2% | 95.24% | ₹7.01 L | −17.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,277 | 95.03% | 95.59% | ₹33.90 L | normal |
| HDFC Bank | 1,100 | 94.91% | 96.03% | ₹10.79 L | normal |
| Bank of Baroda | 788 | 94.92% | 95.64% | ₹6.98 L | normal |
| Union Bank of India | 733 | 94.54% | 95.30% | ₹8.26 L | normal |
| ICICI Bank | 645 | 95.66% | 95.85% | ₹5.47 L | normal |
| Axis Bank | 627 | 95.37% | 95.88% | ₹6.81 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,846 | 95.11% | 95.66% | ₹47.32 L | normal |
| Google Pay | 3,501 | 94.86% | 95.67% | ₹36.10 L | normal |
| Paytm | 837 | 95.70% | 95.48% | ₹8.86 L | normal |
| Navi | 396 | 96.72% | 95.49% | ₹5.28 L | normal |
| SuperMoney | 202 | 94.55% | 95.88% | ₹2.75 L | normal |
| BHIM | 88 | 95.45% | 94.88% | ₹70,088 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,903 | 95.87% | ₹26.04 L |
| Food & Beverage | 1,640 | 95.91% | ₹6.90 L |
| Mobility | 739 | 97.83% | ₹3.57 L |
| Bills | 619 | 95.15% | ₹6.06 L |
| Healthcare | 287 | 96.17% | ₹1.65 L |
| Digital | 184 | 92.39% | ₹97,063 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,097 | 29.9% | 95.09% | ₹32.41 L |
| North | 2,727 | 26.3% | 95.31% | ₹27.14 L |
| West | 2,470 | 23.8% | 94.21% | ₹25.00 L |
| East | 1,201 | 11.6% | 94.75% | ₹12.09 L |
| Central | 870 | 8.4% | 95.75% | ₹8.55 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 19 | 94.74% | ₹1.40 L |
| Rapid Bazaar | Key Account | Retail | 299 | 97.32% | ₹1.22 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 66 | 95.45% | ₹56,685 |
| Girnar Connect | Key Account | Bills | 115 | 95.65% | ₹56,144 |
| Hampi Stores 2298 | Key Account | Retail | 91 | 95.60% | ₹53,595 |
| Vasant Wardrobe | Key Account | Retail | 42 | 92.86% | ₹53,285 |
| Urban Boutique | Key Account | Retail | 87 | 94.25% | ₹51,558 |
| Kaveri Trading | Large | Retail | 43 | 95.35% | ₹49,457 |

## Failure analysis

Of 510 declined attempts, 411 were business declines (3.965% of attempts — balances, PINs and limits), 50 technical (0.482%), 40 timeouts (0.386%) and 9 risk declines (0.087%).

162 attempts were re-presentations of an earlier failure (1.56% of the day); 65.4% of them succeeded.

- Decline code ZM (Invalid UPI PIN) fired 152 times — 1.466% of attempts against a trailing 1.109%. Owner: Customer.
- Decline code UX (Mandate execution outside permitted window) fired 18 times — 0.174% of attempts against a trailing 0.103%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 157 | 1.515% | 1.404% |
| ZM | Invalid UPI PIN | business | Customer | 152 | 1.466% | 1.109% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.444% | 0.406% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.251% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.203% | 0.166% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.193% | 0.171% |
| UX | Mandate execution outside permitted window | business | PSP | 18 | 0.174% | 0.103% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.125% | 0.122% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 85 | 68 |
| Auto-reversals | 36 | 21 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹1.12 L | ₹91,753 |

## Customer behaviour

8,782 distinct customers transacted (−8.5% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,676 | 3,022 | 1.13 | 95.20% | ₹1,037 |
| power | 1,934 | 2,530 | 1.31 | 95.14% | ₹1,524 |
| merchant_heavy | 1,960 | 2,299 | 1.17 | 94.26% | ₹798 |
| small_ticket | 1,279 | 1,533 | 1.20 | 94.65% | ₹478 |
| occasional | 729 | 764 | 1.05 | 95.68% | ₹1,104 |
| new | 185 | 198 | 1.07 | 96.46% | ₹527 |
| dormant_returning | 19 | 19 | 1.00 | 94.74% | ₹749 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0065** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 152 times — 1.466% of attempts against a trailing 1.109%. Owner: Customer.
- Success rate closed at 94.95%, 0.69pp down the trailing median — a 1.9-sigma move.
- Product UPI Person to Person ran at 93.80% success on 3,663 attempts (35.3% of the day), 1.22pp down its own 28-day median.
- Region West ran at 94.21% success on 2,470 attempts (23.8% of the day), 1.37pp down its own 28-day median.
- Product UPI Person to Merchant ran at 95.28% success on 2,969 attempts (28.6% of the day), 0.64pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 81% across the trailing window to 171 today, with success holding, so the growth is healthy and worth funding.
- Product UPI 123Pay is compounding — attempts up 39% across the trailing window to 48 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

15 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 94.95% success against a 95.64% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,365, successes=9,842, failed=510, pending=13, settled_value_inr=10,517,513.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZM; count=152; rate_pct=1.47; trailing_rate_pct=1.11; owner=Customer; z=2.55
- products: product_name=UPI Circle; attempts=171; window_growth_pct=80.5; success_rate=97.08
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- headline: success_rate=94.95; trailing_median=95.64; z=-1.95
- products: product_name=UPI Person to Person; attempts=3,663; success_rate=93.8; own_median=95.02; z=-2.48
- geography: region=West; attempts=2,470; success_rate=94.21; own_median=95.58; z=-2.64
- products: product_name=UPI 123Pay; attempts=48; window_growth_pct=39.1; success_rate=97.92
- products: product_name=UPI Person to Merchant; attempts=2,969; success_rate=95.28; own_median=95.92; z=-2
- failures: failure_code=UX; count=18; rate_pct=0.17; trailing_rate_pct=0.1; owner=PSP; z=2.86
- categories: mcc_category=Mobility; attempts=739; success_rate=97.83; own_median=96.81; z=2.4

Refs: enterprise_data/warehouse/transactions, RPT-D69-DAILY, enterprise_data/warehouse/reference/incidents.parquet
