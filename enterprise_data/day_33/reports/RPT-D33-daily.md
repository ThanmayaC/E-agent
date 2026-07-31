---
id: RPT-D33-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-06T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 06 Feb 2026)

**Report ID:** RPT-D33-DAILY · **Day 33 of 206** · **Derived from:** 12,193 transaction rows queried live from the warehouse

## Summary

The rail took **12,193 payment attempts** on Friday 06 February 2026 (Working day) and settled **₹1.41 Cr** across 11,697 successful payments. Volume was +16.3% on yesterday and +16.7% on the same weekday last week. Success closed at **95.93%**, above the trailing 28-day median of 95.31%.

Category Bills carried 1,387 attempts, 103% up its trailing median and 17.7% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,193 | +16.3% | +16.7% | 11,523 |
| Successful payments | 11,697 | +16.8% | +16.6% | 11,023 |
| Success rate | 95.93% | +0.42pp | −0.02pp | 95.66% |
| Settled value | ₹1.41 Cr | +5.8% | +10.0% | ₹1.36 Cr |
| Average ticket | ₹1,208 | −9.4% | −5.7% | ₹1,236 |
| Technical declines | 0.336% | −0.11pp | −0.09pp | 0.416% |
| Business declines | 3.223% | −0.35pp | +0.08pp | 3.399% |
| Risk declines | 0.164% | +0.04pp | +0.06pp | 0.160% |
| Timeout declines | 0.262% | +0.01pp | +0.00pp | 0.256% |
| Retry share | 1.19% | −0.02pp | −0.03pp | 1.24% |
| Latency p95 | 1,260 ms | −2.2% | +4.7% | 1,247 ms |
| Active customers | 10,147 | +14.1% | +14.4% | 9,642 |
| Active merchants | 1,314 | +4.9% | +8.6% | 1,279 |

## What moved

- Category Bills carried 1,387 attempts, 103% up its trailing median and 17.7% of the day's volume.
- Product UPI Person to Merchant carried 3,938 attempts, 29% up its trailing median and 32.3% of the day's volume.
- Region West ran at 96.37% success on 3,030 attempts (24.9% of the day), 1.18pp up its own 28-day median.
- Region North ran at 96.33% success on 3,051 attempts (25.0% of the day), 1.14pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,365 | 35.8% | 95.01% | ₹43.83 L | +9.4% |
| UPI Person to Merchant | 3,938 | 32.3% | 96.19% | ₹41.11 L | +29.5% |
| UPI QR Payments | 1,829 | 15.0% | 96.94% | ₹7.58 L | +5.6% |
| UPI Lite | 918 | 7.5% | 98.91% | ₹88,199 | +32.2% |
| UPI AutoPay | 288 | 2.4% | 89.24% | ₹4.61 L | −5.1% |
| RuPay Credit on UPI | 236 | 1.9% | 97.46% | ₹14.96 L | +22.9% |
| Credit on UPI | 163 | 1.3% | 97.55% | ₹12.33 L | +24.0% |
| UPI Circle | 116 | 1.0% | 97.41% | ₹1.09 L | +24.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,897 | 95.71% | 95.06% | ₹47.18 L | normal |
| HDFC Bank | 1,310 | 96.41% | 95.90% | ₹15.99 L | normal |
| Bank of Baroda | 915 | 95.63% | 94.70% | ₹13.50 L | normal |
| Union Bank of India | 869 | 95.40% | 94.72% | ₹8.51 L | normal |
| Axis Bank | 752 | 95.74% | 95.19% | ₹9.37 L | normal |
| Punjab National Bank | 750 | 96.00% | 94.71% | ₹9.37 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,797 | 95.96% | 95.14% | ₹71.48 L | normal |
| Google Pay | 3,906 | 95.60% | 95.35% | ₹44.18 L | normal |
| Paytm | 1,027 | 96.30% | 94.80% | ₹9.96 L | normal |
| Navi | 471 | 97.66% | 95.70% | ₹5.28 L | normal |
| SuperMoney | 247 | 96.36% | 96.12% | ₹2.48 L | normal |
| BHIM | 131 | 93.89% | 94.53% | ₹1.15 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,982 | 96.85% | ₹31.41 L |
| Food & Beverage | 1,716 | 97.26% | ₹9.23 L |
| Bills | 1,387 | 95.96% | ₹16.02 L |
| Mobility | 743 | 96.77% | ₹4.65 L |
| Healthcare | 388 | 97.16% | ₹3.95 L |
| Digital | 294 | 92.52% | ₹1.59 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,610 | 29.6% | 95.18% | ₹43.95 L |
| North | 3,051 | 25.0% | 96.33% | ₹29.99 L |
| West | 3,030 | 24.9% | 96.37% | ₹37.06 L |
| East | 1,446 | 11.9% | 95.64% | ₹19.10 L |
| Central | 1,056 | 8.7% | 96.50% | ₹11.20 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 92 | 95.65% | ₹2.10 L |
| Rapid Bazaar | Key Account | Retail | 305 | 97.38% | ₹1.98 L |
| Girnar Connect | Key Account | Bills | 227 | 95.59% | ₹1.20 L |
| Vega Electronics | Large | Retail | 27 | 100.00% | ₹1.15 L |
| Vasant Wardrobe | Key Account | Retail | 76 | 98.68% | ₹1.05 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 83 | 95.18% | ₹96,390 |
| Urban Boutique | Key Account | Retail | 106 | 98.11% | ₹78,325 |
| Aravalli Pharmacy | Large | Healthcare | 78 | 100.00% | ₹69,545 |

## Failure analysis

Of 486 declined attempts, 393 were business declines (3.223% of attempts — balances, PINs and limits), 41 technical (0.336%), 32 timeouts (0.262%) and 20 risk declines (0.164%).

145 attempts were re-presentations of an earlier failure (1.19% of the day); 66.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.435% | 1.491% |
| ZM | Invalid UPI PIN | business | Customer | 130 | 1.066% | 1.139% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.426% | 0.425% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.164% | 0.111% |
| XH | Account does not exist / frozen | business | Issuer | 19 | 0.156% | 0.238% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.131% | 0.158% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.131% | 0.126% |
| U30 | Debit failed at remitter bank | technical | Issuer | 14 | 0.115% | 0.255% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 64 | 64 |
| Auto-reversals | 18 | 22 |
| Disputes / chargebacks | 4 | 3 |
| Value returned | ₹1.33 L | ₹1.00 L |

## Customer behaviour

10,147 distinct customers transacted (+14.3% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,032 | 3,462 | 1.14 | 95.84% | ₹1,187 |
| power | 2,177 | 2,968 | 1.36 | 95.62% | ₹1,548 |
| merchant_heavy | 2,329 | 2,760 | 1.19 | 96.49% | ₹861 |
| small_ticket | 1,543 | 1,880 | 1.22 | 95.27% | ₹492 |
| occasional | 801 | 841 | 1.05 | 96.79% | ₹2,153 |
| new | 223 | 240 | 1.08 | 97.92% | ₹1,117 |
| dormant_returning | 42 | 42 | 1.00 | 90.48% | ₹1,050 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

06 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 95.93% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-06` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,193, successes=11,697, failed=486, pending=10, settled_value_inr=14,129,077.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- categories: mcc_category=Bills; attempts=1,387; own_median=683.5; z=4.67
- products: product_name=UPI Person to Merchant; attempts=3,938; own_median=3,041; z=2.87
- geography: region=West; attempts=3,030; success_rate=96.37; own_median=95.19; z=2.17
- geography: region=North; attempts=3,051; success_rate=96.33; own_median=95.19; z=2.09
- categories: mcc_category=Digital; attempts=294; own_median=198.5; z=3.48
- banks: payer_bank=Indian Bank; attempts=373; success_rate=97.59; own_median=94.84; z=2.48
- psps: payer_psp=Navi; attempts=471; own_median=373.5; z=2.58
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- banks: payer_bank=IndusInd Bank; attempts=268; success_rate=98.88; own_median=95.8; z=2.2

Refs: enterprise_data/warehouse/transactions, RPT-D32-DAILY, enterprise_data/warehouse/reference/incidents.parquet
