---
id: RPT-D46-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 19 Feb 2026)

**Report ID:** RPT-D46-DAILY · **Day 46 of 206** · **Derived from:** 9,964 transaction rows queried live from the warehouse

## Summary

The rail took **9,964 payment attempts** on Thursday 19 February 2026 (Working day) and settled **₹1.12 Cr** across 9,484 successful payments. Volume was +2.5% on yesterday and +0.5% on the same weekday last week. Success closed at **95.18%**, below the trailing 28-day median of 95.49%.

13 disputes were raised, 5.4 sigma above the trailing median of 5. Retries reached 165 attempts (1.66% of the day, 2.3 sigma above normal). 59.4% of re-presented payments recovered, so the retry path was doing its job.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,964 | +2.5% | +0.5% | 10,792 |
| Successful payments | 9,484 | +1.8% | +0.3% | 10,298 |
| Success rate | 95.18% | −0.60pp | −0.17pp | 95.38% |
| Settled value | ₹1.12 Cr | +0.5% | +4.9% | ₹1.22 Cr |
| Average ticket | ₹1,179 | −1.3% | +4.6% | ₹1,188 |
| Technical declines | 0.422% | +0.10pp | +0.03pp | 0.423% |
| Business declines | 3.904% | +0.53pp | +0.12pp | 3.545% |
| Risk declines | 0.100% | +0.02pp | −0.03pp | 0.136% |
| Timeout declines | 0.311% | +0.00pp | +0.07pp | 0.399% |
| Retry share | 1.66% | +0.40pp | +0.35pp | 1.45% |
| Latency p95 | 1,296 ms | +3.2% | +6.8% | 1,287 ms |
| Active customers | 8,553 | +2.7% | +0.6% | 9,114 |
| Active merchants | 1,235 | −0.3% | +0.2% | 1,254 |

## What moved

- Issuer ICICI Bank ran at 94.28% success on 559 attempts (5.6% of the day), 2.11pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,920 | 39.3% | 94.44% | ₹42.17 L | +0.2% |
| UPI Person to Merchant | 2,898 | 29.1% | 95.86% | ₹25.54 L | −6.8% |
| UPI QR Payments | 1,359 | 13.6% | 96.10% | ₹5.34 L | −22.8% |
| UPI Lite | 678 | 6.8% | 98.38% | ₹55,967 | −6.8% |
| UPI AutoPay | 300 | 3.0% | 88.00% | ₹5.09 L | +1.0% |
| RuPay Credit on UPI | 258 | 2.6% | 95.74% | ₹11.71 L | +28.7% |
| Credit on UPI | 158 | 1.6% | 95.57% | ₹9.06 L | +8.6% |
| UPI Circle | 94 | 0.9% | 91.49% | ₹83,680 | −12.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,196 | 95.12% | 95.68% | ₹35.53 L | normal |
| HDFC Bank | 1,091 | 96.33% | 96.07% | ₹13.28 L | normal |
| Bank of Baroda | 752 | 96.28% | 95.30% | ₹8.04 L | normal |
| Union Bank of India | 718 | 95.13% | 95.33% | ₹7.68 L | normal |
| Axis Bank | 636 | 95.75% | 95.10% | ₹6.98 L | normal |
| Punjab National Bank | 592 | 93.58% | 94.76% | ₹8.15 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,635 | 95.32% | 95.49% | ₹52.91 L | normal |
| Google Pay | 3,415 | 95.46% | 95.65% | ₹38.95 L | normal |
| Paytm | 806 | 94.17% | 95.68% | ₹8.29 L | normal |
| Navi | 361 | 95.01% | 95.69% | ₹3.03 L | normal |
| SuperMoney | 177 | 97.18% | 96.06% | ₹3.06 L | normal |
| BHIM | 101 | 94.06% | 94.76% | ₹1.33 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,501 | 96.40% | ₹27.93 L |
| Food & Beverage | 1,482 | 96.29% | ₹6.56 L |
| Bills | 630 | 95.56% | ₹6.03 L |
| Mobility | 587 | 96.76% | ₹3.83 L |
| Healthcare | 319 | 94.98% | ₹2.08 L |
| Digital | 185 | 91.35% | ₹77,122 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,863 | 28.7% | 95.49% | ₹33.20 L |
| North | 2,546 | 25.6% | 94.82% | ₹28.98 L |
| West | 2,458 | 24.7% | 95.52% | ₹28.07 L |
| East | 1,220 | 12.2% | 94.84% | ₹13.07 L |
| Central | 877 | 8.8% | 94.75% | ₹8.51 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 30 | 93.33% | ₹2.19 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 95.31% | ₹1.32 L |
| Hampi Styles | Key Account | Retail | 28 | 100.00% | ₹88,039 |
| Rapid Bazaar | Key Account | Retail | 230 | 97.39% | ₹74,075 |
| Yamuna Restaurant | Key Account | Food & Beverage | 72 | 94.44% | ₹61,699 |
| Urban Boutique | Key Account | Retail | 84 | 94.05% | ₹58,538 |
| Girnar Connect | Key Account | Bills | 96 | 94.79% | ₹49,937 |
| Kaveri Trading | Large | Retail | 53 | 86.79% | ₹44,645 |

## Failure analysis

Of 472 declined attempts, 389 were business declines (3.904% of attempts — balances, PINs and limits), 42 technical (0.422%), 31 timeouts (0.311%) and 10 risk declines (0.100%).

165 attempts were re-presentations of an earlier failure (1.66% of the day); 59.4% of them succeeded.

- Retries reached 165 attempts (1.66% of the day, 2.3 sigma above normal). 59.4% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 152 | 1.525% | 1.440% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 1.385% | 1.135% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.442% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.281% | 0.227% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.181% | 0.147% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.151% | 0.124% |
| UX | Mandate execution outside permitted window | business | PSP | 15 | 0.151% | 0.105% |
| U69 | Beneficiary bank offline | technical | Issuer | 11 | 0.110% | 0.062% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 51 | 68 |
| Auto-reversals | 15 | 18 |
| Disputes / chargebacks | 13 | 5 |
| Value returned | ₹90,304 | ₹1.01 L |

## Customer behaviour

8,553 distinct customers transacted (−3.8% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,555 | 2,849 | 1.12 | 94.42% | ₹1,187 |
| power | 1,849 | 2,350 | 1.27 | 94.94% | ₹1,662 |
| merchant_heavy | 1,941 | 2,254 | 1.16 | 96.01% | ₹873 |
| small_ticket | 1,334 | 1,588 | 1.19 | 95.65% | ₹481 |
| occasional | 682 | 714 | 1.05 | 95.24% | ₹1,276 |
| new | 167 | 184 | 1.10 | 96.20% | ₹1,321 |
| dormant_returning | 25 | 25 | 1.00 | 92.00% | ₹472 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0006** (Sev-1) — Punjab National Bank issuer decline spike, scoped to Punjab National Bank between 19:00 and 24:00. Punjab National Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-BANK-0011** (Sev-2) — State Bank of India issuer decline spike, scoped to State Bank of India between 17:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 13 disputes were raised, 5.4 sigma above the trailing median of 5.
- Issuer ICICI Bank ran at 94.28% success on 559 attempts (5.6% of the day), 2.11pp down its own 28-day median.
- Issuer Federal Bank ran at 91.94% success on 248 attempts (2.5% of the day), 3.38pp down its own 28-day median.
- Product UPI Circle ran at 91.49% success on 94 attempts (0.9% of the day), 5.22pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

19 February was an incident day: INC-FRAUD-0048, INC-BANK-0006 were live and the rail closed at 95.18% success against a 95.49% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,964, successes=9,484, failed=472, pending=8, settled_value_inr=11,184,103.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=13; trailing_median=5; z=5.4
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- incidents: event_id=INC-BANK-0006; kind=bank_outage; severity=Sev-1; window=2026-02-19 to 2026-02-20; success_impact_pp=-25.39; volume_impact_pct=-22.52
- failures: retries=165; retry_share_pct=1.66; recovery_pct=59.39; z=2.31
- incidents: event_id=INC-BANK-0011; kind=bank_outage; severity=Sev-2; window=2026-02-19 to 2026-02-19; success_impact_pp=-11.8; volume_impact_pct=-10.46
- banks: payer_bank=ICICI Bank; attempts=559; success_rate=94.28; own_median=96.39; z=-3.44
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- banks: payer_bank=Federal Bank; attempts=248; success_rate=91.94; own_median=95.32; z=-2.05
- products: product_name=UPI Circle; attempts=94; success_rate=91.49; own_median=96.71; z=-2.87

Refs: enterprise_data/warehouse/transactions, RPT-D45-DAILY, enterprise_data/warehouse/reference/incidents.parquet
