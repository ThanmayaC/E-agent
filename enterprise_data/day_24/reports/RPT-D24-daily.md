---
id: RPT-D24-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 28 Jan 2026)

**Report ID:** RPT-D24-DAILY · **Day 24 of 206** · **Derived from:** 8,810 transaction rows queried live from the warehouse

## Summary

The rail took **8,810 payment attempts** on Wednesday 28 January 2026 (Working day) and settled **₹1.04 Cr** across 8,324 successful payments. Volume was −2.3% on yesterday and −11.9% on the same weekday last week. Success closed at **94.48%**, below the trailing 28-day median of 95.15%.

Decline code Z9 (Insufficient funds) fired 184 times — 2.089% of attempts against a trailing 1.503%. Owner: Customer. Decline code ZM (Invalid UPI PIN) fired 125 times — 1.419% of attempts against a trailing 1.103%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 8,810 | −2.3% | −11.9% | 10,319 |
| Successful payments | 8,324 | −2.8% | −12.4% | 9,817 |
| Success rate | 94.48% | −0.43pp | −0.52pp | 95.10% |
| Settled value | ₹1.04 Cr | −0.3% | −5.7% | ₹1.16 Cr |
| Average ticket | ₹1,251 | +2.5% | +7.7% | ₹1,182 |
| Technical declines | 0.397% | −0.06pp | −0.20pp | 0.617% |
| Business declines | 4.427% | +0.37pp | +0.67pp | 3.621% |
| Risk declines | 0.136% | +0.03pp | −0.00pp | 0.133% |
| Timeout declines | 0.454% | +0.13pp | +0.02pp | 0.390% |
| Retry share | 1.68% | −0.16pp | +0.13pp | 1.51% |
| Latency p95 | 1,279 ms | +1.4% | +2.2% | 1,245 ms |
| Active customers | 7,648 | −1.4% | −10.0% | 8,740 |
| Active merchants | 1,174 | +1.6% | −1.1% | 1,201 |

## What moved

- Category Bills carried 831 attempts, 34% up its trailing median and 15.4% of the day's volume.
- Category Food & Beverage carried 1,213 attempts, 18% down its trailing median and 22.4% of the day's volume.
- App Google Pay carried 2,849 attempts, 17% down its trailing median and 32.3% of the day's volume.
- Product UPI Person to Merchant carried 2,430 attempts, 18% down its trailing median and 27.6% of the day's volume.
- Region West carried 2,122 attempts, 16% down its trailing median and 24.1% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,397 | 38.6% | 93.41% | ₹34.70 L | −15.4% |
| UPI Person to Merchant | 2,430 | 27.6% | 95.51% | ₹26.12 L | −18.4% |
| UPI QR Payments | 1,376 | 15.6% | 96.15% | ₹5.17 L | −17.8% |
| UPI Lite | 627 | 7.1% | 98.56% | ₹51,019 | −5.1% |
| UPI AutoPay | 293 | 3.3% | 83.28% | ₹5.39 L | −3.6% |
| RuPay Credit on UPI | 172 | 2.0% | 97.09% | ₹10.51 L | −10.4% |
| Credit on UPI | 131 | 1.5% | 91.60% | ₹6.61 L | +0.8% |
| UPI Circle | 89 | 1.0% | 95.51% | ₹59,087 | −4.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,808 | 95.19% | 94.89% | ₹33.99 L | normal |
| HDFC Bank | 961 | 95.01% | 95.89% | ₹11.25 L | normal |
| Bank of Baroda | 682 | 92.96% | 94.67% | ₹8.33 L | normal |
| Union Bank of India | 627 | 94.90% | 94.62% | ₹5.52 L | normal |
| ICICI Bank | 535 | 94.39% | 96.09% | ₹8.25 L | ⚠ outlier |
| Axis Bank | 535 | 93.83% | 95.28% | ₹5.96 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,208 | 94.30% | 95.09% | ₹49.47 L | normal |
| Google Pay | 2,849 | 94.81% | 95.26% | ₹33.33 L | normal |
| Paytm | 736 | 94.29% | 94.59% | ₹8.44 L | normal |
| Navi | 319 | 95.61% | 95.79% | ₹4.36 L | normal |
| SuperMoney | 143 | 96.50% | 95.49% | ₹2.43 L | normal |
| BHIM | 108 | 95.37% | 95.33% | ₹1.14 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,071 | 95.70% | ₹23.45 L |
| Food & Beverage | 1,213 | 95.88% | ₹6.31 L |
| Bills | 831 | 94.58% | ₹10.99 L |
| Mobility | 559 | 97.50% | ₹2.51 L |
| Healthcare | 242 | 95.87% | ₹2.02 L |
| Digital | 202 | 91.09% | ₹95,093 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,711 | 30.8% | 94.76% | ₹31.03 L |
| North | 2,258 | 25.6% | 94.38% | ₹27.93 L |
| West | 2,122 | 24.1% | 94.44% | ₹26.98 L |
| East | 992 | 11.3% | 93.95% | ₹12.30 L |
| Central | 727 | 8.3% | 94.64% | ₹5.86 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 51 | 96.08% | ₹1.28 L |
| Vega Electronics | Large | Retail | 17 | 94.12% | ₹1.24 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 61 | 96.72% | ₹75,761 |
| Vasant Wardrobe | Key Account | Retail | 46 | 97.83% | ₹73,960 |
| Rapid Bazaar | Key Account | Retail | 212 | 97.64% | ₹73,132 |
| Girnar Connect | Key Account | Bills | 145 | 95.86% | ₹71,356 |
| Trinetra Restaurant | Large | Food & Beverage | 19 | 94.74% | ₹65,051 |
| Shakti Stores 1531 | Key Account | Retail | 49 | 97.96% | ₹54,594 |

## Failure analysis

Of 477 declined attempts, 390 were business declines (4.427% of attempts — balances, PINs and limits), 35 technical (0.397%), 40 timeouts (0.454%) and 12 risk declines (0.136%).

148 attempts were re-presentations of an earlier failure (1.68% of the day); 65.5% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 184 times — 2.089% of attempts against a trailing 1.503%. Owner: Customer.
- Decline code ZM (Invalid UPI PIN) fired 125 times — 1.419% of attempts against a trailing 1.103%. Owner: Customer.
- Decline code ZA (Transaction declined by customer) fired 49 times — 0.556% of attempts against a trailing 0.400%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 24 times — 0.272% of attempts against a trailing 0.184%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 184 | 2.089% | 1.503% |
| ZM | Invalid UPI PIN | business | Customer | 125 | 1.419% | 1.103% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.556% | 0.400% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.272% | 0.184% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.238% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 14 | 0.159% | 0.267% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.148% | 0.162% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 10 | 0.114% | 0.113% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 66 | 55 |
| Auto-reversals | 19 | 23 |
| Disputes / chargebacks | 4 | 1 |
| Value returned | ₹63,233 | ₹96,474 |

## Customer behaviour

7,648 distinct customers transacted (−13.4% on the 28-day median) at 1.15 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,326 | 2,583 | 1.11 | 94.85% | ₹1,254 |
| power | 1,613 | 2,040 | 1.26 | 94.46% | ₹1,735 |
| merchant_heavy | 1,685 | 1,948 | 1.16 | 93.99% | ₹969 |
| small_ticket | 1,184 | 1,352 | 1.14 | 94.97% | ₹496 |
| occasional | 656 | 687 | 1.05 | 93.45% | ₹1,342 |
| new | 161 | 177 | 1.10 | 94.35% | ₹734 |
| dormant_returning | 23 | 23 | 1.00 | 100.00% | ₹821 |

## Operational events

- **INC-FRAUD-0047** (Sev-1) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-PSP-0025** (Sev-2) — Navi app release regression, scoped to Navi between 18:00 and 23:00. A Navi client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 184 times — 2.089% of attempts against a trailing 1.503%. Owner: Customer.
- Decline code ZM (Invalid UPI PIN) fired 125 times — 1.419% of attempts against a trailing 1.103%. Owner: Customer.
- Decline code ZA (Transaction declined by customer) fired 49 times — 0.556% of attempts against a trailing 0.400%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 24 times — 0.272% of attempts against a trailing 0.184%. Owner: Issuer.
- Issuer ICICI Bank ran at 94.39% success on 535 attempts (6.1% of the day), 1.70pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

28 January was an incident day: INC-FRAUD-0047, INC-PSP-0025 were live and the rail closed at 94.48% success against a 95.15% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=8,810, successes=8,324, failed=477, pending=9, settled_value_inr=10,409,561.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=184; rate_pct=2.09; trailing_rate_pct=1.5; owner=Customer; z=3.24
- incidents: event_id=INC-FRAUD-0047; kind=fraud_spike; severity=Sev-1; window=2026-01-25 to 2026-01-29; success_impact_pp=-2.24; volume_impact_pct=10.81
- failures: failure_code=ZM; count=125; rate_pct=1.42; trailing_rate_pct=1.1; owner=Customer; z=2.41
- incidents: event_id=INC-PSP-0025; kind=psp_degradation; severity=Sev-2; window=2026-01-28 to 2026-01-30; success_impact_pp=-7.08; volume_impact_pct=-11.08
- failures: failure_code=ZA; count=49; rate_pct=0.56; trailing_rate_pct=0.4; owner=Customer; z=2.03
- failures: failure_code=U54; count=24; rate_pct=0.27; trailing_rate_pct=0.18; owner=Issuer; z=2.54
- categories: mcc_category=Bills; attempts=831; own_median=622; z=3.44
- categories: mcc_category=Food & Beverage; attempts=1,213; own_median=1,478; z=-2.84
- psps: payer_psp=Google Pay; attempts=2,849; own_median=3,447; z=-2.22
- products: product_name=UPI Person to Merchant; attempts=2,430; own_median=2,978; z=-2.37

Refs: enterprise_data/warehouse/transactions, RPT-D23-DAILY, enterprise_data/warehouse/reference/incidents.parquet
