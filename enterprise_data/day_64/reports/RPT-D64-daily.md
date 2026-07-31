---
id: RPT-D64-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-09T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 09 Mar 2026)

**Report ID:** RPT-D64-DAILY · **Day 64 of 206** · **Derived from:** 11,817 transaction rows queried live from the warehouse

## Summary

The rail took **11,817 payment attempts** on Monday 09 March 2026 (Working day) and settled **₹1.41 Cr** across 11,333 successful payments. Volume was +0.7% on yesterday and −21.3% on the same weekday last week. Success closed at **95.90%**, above the trailing 28-day median of 95.59%.

Product UPI Circle is compounding — attempts up 77% across the trailing window to 174 today, with success holding, so the growth is healthy and worth funding. Product UPI QR Payments is compounding — attempts up 50% across the trailing window to 2,232 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,817 | +0.7% | −21.3% | 13,865 |
| Successful payments | 11,333 | +1.0% | −21.2% | 13,298 |
| Success rate | 95.90% | +0.29pp | +0.02pp | 95.91% |
| Settled value | ₹1.41 Cr | +13.7% | −17.2% | ₹1.58 Cr |
| Average ticket | ₹1,243 | +12.5% | +5.1% | ₹1,193 |
| Technical declines | 0.516% | −0.04pp | +0.14pp | 0.412% |
| Business declines | 3.021% | −0.22pp | −0.14pp | 3.156% |
| Risk declines | 0.152% | +0.08pp | +0.08pp | 0.115% |
| Timeout declines | 0.305% | −0.10pp | −0.09pp | 0.312% |
| Retry share | 1.07% | −0.45pp | −0.12pp | 1.18% |
| Latency p95 | 1,305 ms | +8.3% | +8.6% | 1,228 ms |
| Active customers | 9,921 | +0.9% | −17.7% | 11,299 |
| Active merchants | 1,273 | −1.2% | −7.0% | 1,344 |

## What moved

- Product UPI Circle is compounding — attempts up 77% across the trailing window to 174 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments is compounding — attempts up 50% across the trailing window to 2,232 today, with success holding, so the growth is healthy and worth funding.
- Category Food & Beverage ran at 97.47% success on 1,740 attempts (23.9% of the day), 0.91pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,535 | 38.4% | 95.28% | ₹50.35 L | +14.2% |
| UPI Person to Merchant | 3,066 | 25.9% | 95.53% | ₹28.56 L | −3.3% |
| UPI QR Payments | 2,232 | 18.9% | 96.77% | ₹10.20 L | +22.9% |
| UPI Lite | 748 | 6.3% | 98.93% | ₹68,459 | −1.5% |
| UPI AutoPay | 271 | 2.3% | 92.62% | ₹5.42 L | −10.4% |
| RuPay Credit on UPI | 261 | 2.2% | 97.70% | ₹14.12 L | +23.7% |
| UPI Circle | 174 | 1.5% | 95.98% | ₹1.65 L | +52.6% |
| Credit on UPI | 157 | 1.3% | 94.90% | ₹12.06 L | +7.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,689 | 95.55% | 95.48% | ₹42.78 L | normal |
| HDFC Bank | 1,269 | 96.38% | 95.98% | ₹16.88 L | normal |
| Bank of Baroda | 915 | 96.17% | 95.41% | ₹9.63 L | normal |
| Union Bank of India | 816 | 95.71% | 95.26% | ₹9.22 L | normal |
| Punjab National Bank | 749 | 95.86% | 94.96% | ₹10.41 L | normal |
| Axis Bank | 732 | 97.13% | 95.79% | ₹9.41 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,524 | 95.94% | 95.61% | ₹64.67 L | normal |
| Google Pay | 3,970 | 95.92% | 95.61% | ₹46.20 L | normal |
| Paytm | 932 | 95.49% | 95.36% | ₹13.98 L | normal |
| Navi | 398 | 96.48% | 95.45% | ₹4.38 L | normal |
| SuperMoney | 247 | 94.74% | 95.91% | ₹2.60 L | normal |
| BHIM | 136 | 97.06% | 94.88% | ₹1.41 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,263 | 95.95% | ₹32.10 L |
| Food & Beverage | 1,740 | 97.47% | ₹8.15 L |
| Mobility | 814 | 97.05% | ₹5.86 L |
| Bills | 606 | 93.89% | ₹8.93 L |
| Healthcare | 381 | 97.90% | ₹3.92 L |
| Digital | 151 | 95.36% | ₹75,688 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,482 | 29.5% | 95.86% | ₹39.44 L |
| North | 2,992 | 25.3% | 95.99% | ₹37.25 L |
| West | 2,905 | 24.6% | 95.59% | ₹40.07 L |
| East | 1,429 | 12.1% | 96.43% | ₹15.32 L |
| Central | 1,009 | 8.5% | 95.94% | ₹8.84 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 24 | 100.00% | ₹1.55 L |
| Rapid Bazaar | Key Account | Retail | 358 | 98.32% | ₹1.37 L |
| Vasant Wardrobe | Key Account | Retail | 62 | 98.39% | ₹1.06 L |
| Ujjwal Water Board | Key Account | Bills | 22 | 90.91% | ₹92,610 |
| Yamuna Restaurant | Key Account | Food & Beverage | 70 | 97.14% | ₹82,856 |
| Hampi Styles | Key Account | Retail | 35 | 97.14% | ₹69,655 |
| Hampi Stores 2298 | Key Account | Retail | 83 | 100.00% | ₹67,925 |
| Kaveri Trading | Large | Retail | 50 | 92.00% | ₹66,190 |

## Failure analysis

Of 472 declined attempts, 357 were business declines (3.021% of attempts — balances, PINs and limits), 61 technical (0.516%), 36 timeouts (0.305%) and 18 risk declines (0.152%).

127 attempts were re-presentations of an earlier failure (1.07% of the day); 66.9% of them succeeded.

- Decline code U16 (Risk threshold exceeded at remitter) fired 17 times — 0.144% of attempts against a trailing 0.091%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 160 | 1.354% | 1.452% |
| ZM | Invalid UPI PIN | business | Customer | 101 | 0.855% | 1.120% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.364% | 0.410% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.254% | 0.240% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.228% | 0.161% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.144% | 0.115% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.144% | 0.167% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.144% | 0.091% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 95 | 68 |
| Auto-reversals | 29 | 20 |
| Disputes / chargebacks | 10 | 9 |
| Value returned | ₹1.22 L | ₹88,956 |

## Customer behaviour

9,921 distinct customers transacted (+8.6% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,142 | 3,602 | 1.15 | 96.03% | ₹1,211 |
| power | 2,058 | 2,713 | 1.32 | 95.25% | ₹1,654 |
| merchant_heavy | 2,199 | 2,618 | 1.19 | 95.42% | ₹970 |
| small_ticket | 1,477 | 1,794 | 1.21 | 96.82% | ₹574 |
| occasional | 823 | 854 | 1.04 | 96.49% | ₹1,635 |
| new | 195 | 208 | 1.07 | 98.56% | ₹1,240 |
| dormant_returning | 27 | 28 | 1.04 | 92.86% | ₹748 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CMP-0058** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code U16 (Risk threshold exceeded at remitter) fired 17 times — 0.144% of attempts against a trailing 0.091%. Owner: Issuer.

### Opportunities

- Product UPI Circle is compounding — attempts up 77% across the trailing window to 174 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments is compounding — attempts up 50% across the trailing window to 2,232 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

09 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.90% success against a 95.59% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-09` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,817, successes=11,333, failed=472, pending=12, settled_value_inr=14,092,076.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=174; window_growth_pct=77.2; success_rate=95.98
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI QR Payments; attempts=2,232; window_growth_pct=50; success_rate=96.77
- categories: mcc_category=Food & Beverage; attempts=1,740; success_rate=97.47; own_median=96.57; z=2.29
- failures: failure_code=U16; count=17; rate_pct=0.14; trailing_rate_pct=0.09; owner=Issuer; z=2.27
- incidents: event_id=CMP-0058; kind=merchant_campaign; severity=Sev-3; window=2026-03-07 to 2026-03-10; success_impact_pp=-0.16; volume_impact_pct=63.89
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- products: product_name=UPI International; attempts=117; own_median=75; z=4.36
- products: product_name=RuPay Credit on UPI; attempts=261; success_rate=97.7; own_median=95.26; z=2.06
- categories: mcc_category=Financial Services; attempts=132; success_rate=94.7; own_median=85.72; z=2.01

Refs: enterprise_data/warehouse/transactions, RPT-D63-DAILY, enterprise_data/warehouse/reference/incidents.parquet
