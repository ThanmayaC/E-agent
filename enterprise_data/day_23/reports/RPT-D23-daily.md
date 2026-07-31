---
id: RPT-D23-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 27 Jan 2026)

**Report ID:** RPT-D23-DAILY · **Day 23 of 206** · **Derived from:** 9,020 transaction rows queried live from the warehouse

## Summary

The rail took **9,020 payment attempts** on Tuesday 27 January 2026 (Working day) and settled **₹1.04 Cr** across 8,561 successful payments. Volume was −7.0% on yesterday and −3.5% on the same weekday last week. Success closed at **94.91%**, below the trailing 28-day median of 95.25%.

Retries reached 166 attempts (1.84% of the day, 2.3 sigma above normal). 68.1% of re-presented payments recovered, so the retry path was doing its job.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,020 | −7.0% | −3.5% | 10,385 |
| Successful payments | 8,561 | −7.2% | −3.2% | 9,881 |
| Success rate | 94.91% | −0.24pp | +0.31pp | 95.13% |
| Settled value | ₹1.04 Cr | +7.0% | −4.4% | ₹1.17 Cr |
| Average ticket | ₹1,220 | +15.3% | −1.2% | ₹1,179 |
| Technical declines | 0.455% | −0.18pp | −0.16pp | 0.627% |
| Business declines | 4.058% | +0.65pp | −0.20pp | 3.586% |
| Risk declines | 0.111% | −0.11pp | +0.01pp | 0.133% |
| Timeout declines | 0.322% | −0.07pp | +0.00pp | 0.387% |
| Retry share | 1.84% | +0.16pp | +0.00pp | 1.50% |
| Latency p95 | 1,261 ms | +1.4% | −2.9% | 1,243 ms |
| Active customers | 7,753 | −7.0% | −3.4% | 8,788 |
| Active merchants | 1,155 | −1.5% | −1.5% | 1,202 |

## What moved

- Category Bills carried 872 attempts, 40% up its trailing median and 15.9% of the day's volume.
- Category Food & Beverage carried 1,220 attempts, 18% down its trailing median and 22.2% of the day's volume.
- Product UPI Person to Merchant carried 2,398 attempts, 20% down its trailing median and 26.6% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,523 | 39.1% | 94.29% | ₹35.80 L | −12.3% |
| UPI Person to Merchant | 2,398 | 26.6% | 95.70% | ₹19.60 L | −19.7% |
| UPI QR Payments | 1,395 | 15.5% | 96.49% | ₹5.71 L | −18.4% |
| UPI Lite | 645 | 7.2% | 98.76% | ₹52,391 | −3.2% |
| UPI AutoPay | 319 | 3.5% | 86.52% | ₹5.08 L | +4.9% |
| RuPay Credit on UPI | 215 | 2.4% | 92.09% | ₹9.40 L | +14.7% |
| Credit on UPI | 132 | 1.5% | 92.42% | ₹10.37 L | +2.3% |
| UPI Lite Auto Top-Up | 91 | 1.0% | 92.31% | ₹92,006 | +9.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,838 | 94.82% | 94.90% | ₹31.26 L | normal |
| HDFC Bank | 1,045 | 95.98% | 95.88% | ₹14.26 L | normal |
| Bank of Baroda | 707 | 94.77% | 94.57% | ₹8.69 L | normal |
| Union Bank of India | 613 | 94.62% | 94.66% | ₹7.04 L | normal |
| Punjab National Bank | 551 | 93.83% | 94.76% | ₹4.81 L | normal |
| Axis Bank | 550 | 94.00% | 95.32% | ₹5.26 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,242 | 94.39% | 95.14% | ₹49.32 L | normal |
| Google Pay | 2,989 | 95.78% | 95.25% | ₹34.81 L | normal |
| Paytm | 735 | 94.42% | 94.68% | ₹6.98 L | normal |
| Navi | 356 | 95.79% | 95.73% | ₹3.19 L | normal |
| SuperMoney | 167 | 96.41% | 95.40% | ₹1.24 L | normal |
| BHIM | 87 | 94.25% | 95.37% | ₹74,236 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,070 | 95.07% | ₹20.30 L |
| Food & Beverage | 1,220 | 96.64% | ₹5.40 L |
| Bills | 872 | 94.50% | ₹8.63 L |
| Mobility | 583 | 96.91% | ₹2.74 L |
| Healthcare | 286 | 97.20% | ₹2.62 L |
| Digital | 200 | 95.00% | ₹1.12 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,666 | 29.6% | 94.19% | ₹24.80 L |
| West | 2,268 | 25.1% | 95.19% | ₹28.36 L |
| North | 2,252 | 25.0% | 95.16% | ₹30.49 L |
| East | 1,076 | 11.9% | 96.28% | ₹13.78 L |
| Central | 758 | 8.4% | 93.93% | ₹7.00 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 55 | 96.36% | ₹1.39 L |
| Vasant Wardrobe | Key Account | Retail | 55 | 89.09% | ₹1.14 L |
| Rapid Bazaar | Key Account | Retail | 223 | 93.27% | ₹93,458 |
| Vega Electronics | Large | Retail | 21 | 95.24% | ₹71,919 |
| Girnar Connect | Key Account | Bills | 133 | 94.74% | ₹53,709 |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 94.12% | ₹50,203 |
| Urban Boutique | Key Account | Retail | 68 | 94.12% | ₹44,672 |
| Tejas Supermart | Large | Retail | 23 | 100.00% | ₹31,682 |

## Failure analysis

Of 446 declined attempts, 366 were business declines (4.058% of attempts — balances, PINs and limits), 41 technical (0.455%), 29 timeouts (0.322%) and 10 risk declines (0.111%).

166 attempts were re-presentations of an earlier failure (1.84% of the day); 68.1% of them succeeded.

- Retries reached 166 attempts (1.84% of the day, 2.3 sigma above normal). 68.1% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 161 | 1.785% | 1.482% |
| ZM | Invalid UPI PIN | business | Customer | 117 | 1.297% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 42 | 0.466% | 0.392% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.222% | 0.270% |
| XH | Account does not exist / frozen | business | Issuer | 20 | 0.222% | 0.249% |
| UX | Mandate execution outside permitted window | business | PSP | 12 | 0.133% | 0.092% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 12 | 0.133% | 0.132% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 11 | 0.122% | 0.185% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 55 | 54 |
| Auto-reversals | 21 | 24 |
| Disputes / chargebacks | 3 | 1 |
| Value returned | ₹82,822 | ₹98,113 |

## Customer behaviour

7,753 distinct customers transacted (−12.4% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,390 | 2,654 | 1.11 | 93.90% | ₹1,130 |
| power | 1,657 | 2,117 | 1.28 | 95.32% | ₹1,786 |
| merchant_heavy | 1,722 | 1,974 | 1.15 | 95.04% | ₹775 |
| small_ticket | 1,176 | 1,428 | 1.21 | 95.45% | ₹558 |
| occasional | 622 | 645 | 1.04 | 95.66% | ₹1,809 |
| new | 161 | 176 | 1.09 | 96.02% | ₹858 |
| dormant_returning | 25 | 26 | 1.04 | 100.00% | ₹687 |

## Operational events

- **INC-FRAUD-0047** (Sev-1) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Region Central ran at 93.93% success on 758 attempts (8.4% of the day), 1.42pp down its own 28-day median.
- Product RuPay Credit on UPI ran at 92.09% success on 215 attempts (2.4% of the day), 3.13pp down its own 28-day median.
- Product UPI Lite Auto Top-Up ran at 92.31% success on 91 attempts (1.0% of the day), 4.03pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

27 January was an incident day: INC-FRAUD-0047 was live and the rail closed at 94.91% success against a 95.25% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,020, successes=8,561, failed=446, pending=13, settled_value_inr=10,442,727.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0047; kind=fraud_spike; severity=Sev-1; window=2026-01-25 to 2026-01-29; success_impact_pp=-2.24; volume_impact_pct=10.81
- failures: retries=166; retry_share_pct=1.84; recovery_pct=68.07; z=2.29
- categories: mcc_category=Bills; attempts=872; own_median=621; z=4.29
- categories: mcc_category=Food & Beverage; attempts=1,220; own_median=1,479.5; z=-3.24
- products: product_name=UPI Person to Merchant; attempts=2,398; own_median=2,987; z=-2.53
- geography: region=Central; attempts=758; success_rate=93.93; own_median=95.35; z=-2.43
- banks: payer_bank=ICICI Bank; attempts=491; own_median=622; z=-2.76
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=RuPay Credit on UPI; attempts=215; success_rate=92.09; own_median=95.22; z=-2.3
- banks: payer_bank=Yes Bank; attempts=344; own_median=388.5; z=-2.4

Refs: enterprise_data/warehouse/transactions, RPT-D22-DAILY, enterprise_data/warehouse/reference/incidents.parquet
