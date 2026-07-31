---
id: RPT-D22-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 26 Jan 2026)

**Report ID:** RPT-D22-DAILY · **Day 22 of 206** · **Derived from:** 9,695 transaction rows queried live from the warehouse

## Summary

The rail took **9,695 payment attempts** on Monday 26 January 2026 (Republic Day) and settled **₹97.62 L** across 9,225 successful payments. Volume was −7.7% on yesterday and −3.0% on the same weekday last week. Success closed at **95.15%**, in line with the trailing 28-day median of 95.35%.

5 disputes were raised, 2.7 sigma above the trailing median of 1. Category Bills carried 904 attempts, 46% up its trailing median and 15.4% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,695 | −7.7% | −3.0% | 10,447 |
| Successful payments | 9,225 | −7.5% | −2.5% | 9,942 |
| Success rate | 95.15% | +0.20pp | +0.46pp | 95.14% |
| Settled value | ₹97.62 L | −8.3% | −12.1% | ₹1.17 Cr |
| Average ticket | ₹1,058 | −0.9% | −9.9% | ₹1,177 |
| Technical declines | 0.640% | −0.02pp | −0.21pp | 0.635% |
| Business declines | 3.404% | −0.41pp | −0.54pp | 3.565% |
| Risk declines | 0.217% | +0.10pp | +0.15pp | 0.134% |
| Timeout declines | 0.392% | +0.05pp | +0.01pp | 0.390% |
| Retry share | 1.68% | +0.27pp | −0.15pp | 1.49% |
| Latency p95 | 1,244 ms | +1.8% | −0.9% | 1,242 ms |
| Active customers | 8,339 | −6.1% | −1.9% | 8,835 |
| Active merchants | 1,173 | −1.4% | −1.3% | 1,204 |

## What moved

- Category Bills carried 904 attempts, 46% up its trailing median and 15.4% of the day's volume.
- Category Bills ran at 94.58% success on 904 attempts (15.4% of the day), 1.24pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,824 | 39.4% | 94.74% | ₹40.09 L | −4.9% |
| UPI Person to Merchant | 2,734 | 28.2% | 96.05% | ₹27.05 L | −8.7% |
| UPI QR Payments | 1,567 | 16.2% | 96.55% | ₹6.83 L | −10.1% |
| UPI Lite | 724 | 7.5% | 99.03% | ₹68,353 | +9.5% |
| UPI AutoPay | 300 | 3.1% | 82.33% | ₹4.69 L | −1.3% |
| Recurring Payments | 103 | 1.1% | 84.47% | ₹4.94 L | +22.6% |
| UPI Circle | 94 | 1.0% | 95.74% | ₹75,354 | +1.1% |
| RuPay Credit on UPI | 86 | 0.9% | 94.19% | ₹3.82 L | −55.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,094 | 94.80% | 94.91% | ₹29.27 L | normal |
| HDFC Bank | 1,040 | 95.87% | 95.89% | ₹10.72 L | normal |
| Bank of Baroda | 749 | 94.26% | 94.67% | ₹7.77 L | normal |
| Union Bank of India | 672 | 94.20% | 94.72% | ₹5.79 L | normal |
| ICICI Bank | 601 | 96.67% | 95.92% | ₹8.23 L | normal |
| Axis Bank | 586 | 94.37% | 95.36% | ₹5.66 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,502 | 94.65% | 95.19% | ₹46.97 L | normal |
| Google Pay | 3,270 | 95.26% | 95.24% | ₹32.32 L | normal |
| Paytm | 745 | 95.97% | 94.59% | ₹6.66 L | normal |
| Navi | 364 | 96.98% | 95.56% | ₹3.67 L | normal |
| SuperMoney | 204 | 96.57% | 95.32% | ₹2.58 L | normal |
| BHIM | 101 | 93.07% | 95.42% | ₹82,507 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,110 | 95.92% | ₹19.76 L |
| Food & Beverage | 1,441 | 96.53% | ₹6.41 L |
| Bills | 904 | 94.58% | ₹10.87 L |
| Mobility | 605 | 96.86% | ₹3.19 L |
| Healthcare | 285 | 95.79% | ₹1.52 L |
| Digital | 237 | 92.41% | ₹1.05 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,829 | 29.2% | 95.02% | ₹27.61 L |
| North | 2,484 | 25.6% | 95.29% | ₹24.72 L |
| West | 2,378 | 24.5% | 94.74% | ₹22.89 L |
| East | 1,183 | 12.2% | 95.35% | ₹13.71 L |
| Central | 821 | 8.5% | 96.10% | ₹8.69 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 53 | 92.45% | ₹2.46 L |
| Vega Electronics | Large | Retail | 23 | 100.00% | ₹2.00 L |
| Vasant Wardrobe | Key Account | Retail | 44 | 90.91% | ₹87,866 |
| Rapid Bazaar | Key Account | Retail | 230 | 95.65% | ₹80,736 |
| Girnar Connect | Key Account | Bills | 156 | 94.87% | ₹60,307 |
| Yamuna Restaurant | Key Account | Food & Beverage | 60 | 100.00% | ₹54,807 |
| Swift Mart 1738 | Key Account | Retail | 77 | 97.40% | ₹42,822 |
| Tejas Bites | Key Account | Food & Beverage | 119 | 98.32% | ₹40,279 |

## Failure analysis

Of 451 declined attempts, 330 were business declines (3.404% of attempts — balances, PINs and limits), 62 technical (0.640%), 38 timeouts (0.392%) and 21 risk declines (0.217%).

163 attempts were re-presentations of an earlier failure (1.68% of the day); 79.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 140 | 1.444% | 1.503% |
| ZM | Invalid UPI PIN | business | Customer | 105 | 1.083% | 1.103% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.454% | 0.385% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.278% | 0.267% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.237% | 0.260% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.227% | 0.184% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.165% | 0.113% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.155% | 0.173% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 61 | 49 |
| Auto-reversals | 22 | 24 |
| Disputes / chargebacks | 5 | 1 |
| Value returned | ₹96,474 | ₹99,753 |

## Customer behaviour

8,339 distinct customers transacted (−6.1% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,560 | 2,882 | 1.13 | 94.93% | ₹1,076 |
| power | 1,775 | 2,259 | 1.27 | 95.13% | ₹1,404 |
| merchant_heavy | 1,885 | 2,170 | 1.15 | 94.84% | ₹893 |
| small_ticket | 1,283 | 1,512 | 1.18 | 95.83% | ₹464 |
| occasional | 661 | 689 | 1.04 | 95.50% | ₹973 |
| new | 150 | 157 | 1.05 | 96.82% | ₹1,023 |
| dormant_returning | 25 | 26 | 1.04 | 88.46% | ₹732 |

## Operational events

- **INC-FRAUD-0047** (Sev-1) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 5 disputes were raised, 2.7 sigma above the trailing median of 1.
- Category Bills ran at 94.58% success on 904 attempts (15.4% of the day), 1.24pp down its own 28-day median.
- Product UPI AutoPay ran at 82.33% success on 300 attempts (3.1% of the day), 6.70pp down its own 28-day median.
- Product Credit on UPI ran at 88.14% success on 59 attempts (0.6% of the day), 6.46pp down its own 28-day median.
- Product UPI Lite Auto Top-Up ran at 90.12% success on 81 attempts (0.8% of the day), 6.31pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

26 January was an incident day: INC-FRAUD-0047 was live and the rail closed at 95.15% success against a 95.35% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,695, successes=9,225, failed=451, pending=19, settled_value_inr=9,762,107.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0047; kind=fraud_spike; severity=Sev-1; window=2026-01-25 to 2026-01-29; success_impact_pp=-2.24; volume_impact_pct=10.81
- adjustments: chargebacks=5; trailing_median=1; z=2.7
- categories: mcc_category=Bills; attempts=904; own_median=620; z=5.04
- categories: mcc_category=Bills; attempts=904; success_rate=94.58; own_median=95.82; z=-2.01
- categories: mcc_category=Digital; attempts=237; own_median=188; z=3.31
- products: product_name=UPI AutoPay; attempts=300; success_rate=82.33; own_median=89.03; z=-2.43
- banks: payer_bank=Kotak Mahindra Bank; attempts=374; success_rate=96.79; own_median=95.25; z=2.04
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=Credit on UPI; attempts=59; success_rate=88.14; own_median=94.59; z=-4.12
- products: product_name=UPI Lite Auto Top-Up; attempts=81; success_rate=90.12; own_median=96.43; z=-3.49

Refs: enterprise_data/warehouse/transactions, RPT-D21-DAILY, enterprise_data/warehouse/reference/incidents.parquet
