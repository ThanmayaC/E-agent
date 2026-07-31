---
id: RPT-D25-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-29T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 29 Jan 2026)

**Report ID:** RPT-D25-DAILY · **Day 25 of 206** · **Derived from:** 8,562 transaction rows queried live from the warehouse

## Summary

The rail took **8,562 payment attempts** on Thursday 29 January 2026 (Working day) and settled **₹95.48 L** across 8,157 successful payments. Volume was −2.8% on yesterday and −22.8% on the same weekday last week. Success closed at **95.27%**, in line with the trailing 28-day median of 95.14%.

10 disputes were raised, 3.8 sigma above the trailing median of 2.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 8,562 | −2.8% | −22.8% | 10,249 |
| Successful payments | 8,157 | −2.0% | −22.9% | 9,750 |
| Success rate | 95.27% | +0.79pp | −0.08pp | 95.11% |
| Settled value | ₹95.48 L | −8.3% | −21.8% | ₹1.15 Cr |
| Average ticket | ₹1,171 | −6.4% | +1.5% | ₹1,181 |
| Technical declines | 0.467% | +0.07pp | −0.05pp | 0.611% |
| Business declines | 3.702% | −0.72pp | +0.22pp | 3.625% |
| Risk declines | 0.105% | −0.03pp | −0.02pp | 0.132% |
| Timeout declines | 0.339% | −0.12pp | −0.06pp | 0.388% |
| Retry share | 1.66% | −0.02pp | +0.26pp | 1.51% |
| Latency p95 | 1,317 ms | +3.0% | +4.3% | 1,247 ms |
| Active customers | 7,412 | −3.1% | −20.4% | 8,687 |
| Active merchants | 1,150 | −2.0% | −4.7% | 1,199 |

## What moved

- Issuer State Bank of India ran at 95.94% success on 2,709 attempts (31.6% of the day), 1.04pp up its own 28-day median.
- Category Food & Beverage carried 1,167 attempts, 21% down its trailing median and 22.4% of the day's volume.
- Region West carried 2,089 attempts, 17% down its trailing median and 24.4% of the day's volume.
- Product UPI Person to Merchant carried 2,308 attempts, 22% down its trailing median and 27.0% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,361 | 39.3% | 94.94% | ₹33.97 L | −16.0% |
| UPI Person to Merchant | 2,308 | 27.0% | 95.58% | ₹19.57 L | −21.8% |
| UPI QR Payments | 1,292 | 15.1% | 95.82% | ₹5.15 L | −22.2% |
| UPI Lite | 573 | 6.7% | 98.78% | ₹48,418 | −12.3% |
| UPI AutoPay | 311 | 3.6% | 87.78% | ₹5.93 L | +2.3% |
| RuPay Credit on UPI | 200 | 2.3% | 94.50% | ₹9.49 L | +6.7% |
| Credit on UPI | 147 | 1.7% | 96.60% | ₹7.27 L | +12.6% |
| UPI International | 81 | 0.9% | 95.06% | ₹8.20 L | +14.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,709 | 95.94% | 94.90% | ₹31.11 L | ⚠ outlier |
| HDFC Bank | 958 | 96.35% | 95.88% | ₹9.40 L | normal |
| Bank of Baroda | 639 | 94.21% | 94.57% | ₹6.24 L | normal |
| Union Bank of India | 595 | 95.29% | 94.67% | ₹7.64 L | normal |
| Punjab National Bank | 534 | 95.51% | 94.71% | ₹5.40 L | normal |
| Axis Bank | 508 | 95.28% | 95.26% | ₹6.47 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 3,997 | 94.97% | 95.09% | ₹42.89 L | normal |
| Google Pay | 2,787 | 96.05% | 95.25% | ₹31.70 L | normal |
| Paytm | 729 | 95.06% | 94.57% | ₹7.01 L | normal |
| Navi | 342 | 96.20% | 95.70% | ₹6.07 L | normal |
| SuperMoney | 167 | 93.41% | 95.62% | ₹1.13 L | normal |
| BHIM | 98 | 93.88% | 95.35% | ₹1.53 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 1,973 | 95.64% | ₹20.44 L |
| Food & Beverage | 1,167 | 96.49% | ₹6.19 L |
| Bills | 775 | 96.00% | ₹7.12 L |
| Mobility | 544 | 95.59% | ₹3.09 L |
| Healthcare | 246 | 97.97% | ₹2.74 L |
| Digital | 205 | 91.71% | ₹80,405 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,552 | 29.8% | 95.14% | ₹25.96 L |
| North | 2,218 | 25.9% | 95.09% | ₹22.36 L |
| West | 2,089 | 24.4% | 94.93% | ₹28.22 L |
| East | 1,022 | 11.9% | 96.28% | ₹12.49 L |
| Central | 681 | 8.0% | 95.89% | ₹6.45 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 56 | 92.86% | ₹1.76 L |
| Vega Electronics | Large | Retail | 21 | 80.95% | ₹1.60 L |
| Rapid Bazaar | Key Account | Retail | 200 | 96.50% | ₹69,558 |
| Ujjwal Water Board | Key Account | Bills | 47 | 97.87% | ₹68,975 |
| Yamuna Restaurant | Key Account | Food & Beverage | 56 | 98.21% | ₹65,953 |
| Girnar Connect | Key Account | Bills | 140 | 96.43% | ₹60,114 |
| Hampi Stores 2298 | Key Account | Retail | 81 | 96.30% | ₹51,696 |
| Swift Mart 1738 | Key Account | Retail | 65 | 95.38% | ₹34,225 |

## Failure analysis

Of 395 declined attempts, 317 were business declines (3.702% of attempts — balances, PINs and limits), 40 technical (0.467%), 29 timeouts (0.339%) and 9 risk declines (0.105%).

142 attempts were re-presentations of an earlier failure (1.66% of the day); 69.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 132 | 1.542% | 1.522% |
| ZM | Invalid UPI PIN | business | Customer | 110 | 1.285% | 1.117% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.420% | 0.405% |
| XH | Account does not exist / frozen | business | Issuer | 20 | 0.234% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.222% | 0.265% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.210% | 0.185% |
| U28 | Remitter bank unavailable | technical | Issuer | 12 | 0.140% | 0.158% |
| ZX | Mandate not found or revoked | business | PSP | 11 | 0.128% | 0.090% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 74 | 57 |
| Auto-reversals | 16 | 22 |
| Disputes / chargebacks | 10 | 2 |
| Value returned | ₹1.23 L | ₹90,875 |

## Customer behaviour

7,412 distinct customers transacted (−15.8% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,287 | 2,524 | 1.10 | 95.25% | ₹1,140 |
| power | 1,657 | 2,077 | 1.25 | 95.38% | ₹1,447 |
| merchant_heavy | 1,617 | 1,895 | 1.17 | 95.88% | ₹960 |
| small_ticket | 1,079 | 1,267 | 1.17 | 94.71% | ₹622 |
| occasional | 589 | 612 | 1.04 | 95.10% | ₹1,519 |
| new | 154 | 158 | 1.03 | 91.14% | ₹663 |
| dormant_returning | 29 | 29 | 1.00 | 100.00% | ₹824 |

## Operational events

- **INC-FRAUD-0047** (Sev-1) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-PSP-0025** (Sev-2) — Navi app release regression, scoped to Navi between 18:00 and 23:00. A Navi client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-BANK-0015** (Sev-3) — Union Bank of India issuer decline spike, scoped to Union Bank of India between 10:00 and 14:00. Union Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 10 disputes were raised, 3.8 sigma above the trailing median of 2.
- Issuer Indian Bank ran at 90.14% success on 284 attempts (3.3% of the day), 4.70pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

29 January was an incident day: INC-FRAUD-0047, INC-PSP-0025 were live and the rail closed at 95.27% success against a 95.14% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-29` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=8,562, successes=8,157, failed=395, pending=10, settled_value_inr=9,547,999.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=10; trailing_median=1.5; z=3.82
- incidents: event_id=INC-FRAUD-0047; kind=fraud_spike; severity=Sev-1; window=2026-01-25 to 2026-01-29; success_impact_pp=-2.24; volume_impact_pct=10.81
- incidents: event_id=INC-PSP-0025; kind=psp_degradation; severity=Sev-2; window=2026-01-28 to 2026-01-30; success_impact_pp=-7.08; volume_impact_pct=-11.08
- banks: payer_bank=State Bank of India; attempts=2,709; success_rate=95.94; own_median=94.9; z=2.03
- categories: mcc_category=Food & Beverage; attempts=1,167; own_median=1,474; z=-3.05
- geography: region=West; attempts=2,089; own_median=2,510.5; z=-2.58
- products: product_name=UPI Person to Merchant; attempts=2,308; own_median=2,951; z=-2.4
- incidents: event_id=INC-BANK-0015; kind=bank_outage; severity=Sev-3; window=2026-01-29 to 2026-01-30; success_impact_pp=-4.58; volume_impact_pct=-4.06
- banks: payer_bank=Indian Bank; attempts=284; success_rate=90.14; own_median=94.84; z=-3.61
- categories: mcc_category=Healthcare; attempts=246; own_median=318; z=-2.43

Refs: enterprise_data/warehouse/transactions, RPT-D24-DAILY, enterprise_data/warehouse/reference/incidents.parquet
