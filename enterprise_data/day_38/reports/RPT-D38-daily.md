---
id: RPT-D38-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 11 Feb 2026)

**Report ID:** RPT-D38-DAILY · **Day 38 of 206** · **Derived from:** 9,255 transaction rows queried live from the warehouse

## Summary

The rail took **9,255 payment attempts** on Wednesday 11 February 2026 (Working day) and settled **₹1.10 Cr** across 8,743 successful payments. Volume was −6.2% on yesterday and −15.1% on the same weekday last week. Success closed at **94.47%**, below the trailing 28-day median of 95.41%.

Retries reached 301 attempts (3.25% of the day, 12.1 sigma above normal). 64.5% of re-presented payments recovered, so the retry path was doing its job. Decline code ZM (Invalid UPI PIN) fired 160 times — 1.729% of attempts against a trailing 1.139%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,255 | −6.2% | −15.1% | 11,070 |
| Successful payments | 8,743 | −3.4% | −16.3% | 10,553 |
| Success rate | 94.47% | +2.76pp | −1.33pp | 95.26% |
| Settled value | ₹1.10 Cr | +3.5% | −20.1% | ₹1.26 Cr |
| Average ticket | ₹1,261 | +7.2% | −4.5% | ₹1,196 |
| Technical declines | 0.475% | −0.53pp | +0.12pp | 0.449% |
| Business declines | 4.333% | +0.07pp | +0.98pp | 3.526% |
| Risk declines | 0.108% | −0.02pp | −0.05pp | 0.148% |
| Timeout declines | 0.475% | −2.17pp | +0.25pp | 0.493% |
| Retry share | 3.25% | −0.20pp | +2.01pp | 1.59% |
| Latency p95 | 1,286 ms | −34.0% | +4.0% | 1,314 ms |
| Active customers | 7,955 | −4.2% | −13.2% | 9,298 |
| Active merchants | 1,199 | −2.8% | −5.4% | 1,263 |

## What moved

- Category Retail ran at 94.79% success on 2,417 attempts (41.0% of the day), 1.31pp down its own 28-day median.
- Product UPI Person to Merchant ran at 94.74% success on 2,736 attempts (29.6% of the day), 1.13pp down its own 28-day median.
- Region North ran at 93.72% success on 2,389 attempts (25.8% of the day), 1.60pp down its own 28-day median.
- Success rate closed at 94.47%, 0.94pp down the trailing median — a 1.5-sigma move.
- Product UPI Lite is compounding — attempts up 35% across the trailing window to 683 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- App Navi ran at 91.91% success on 371 attempts (4.0% of the day), 3.95pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,356 | 36.3% | 93.80% | ₹34.59 L | −13.9% |
| UPI Person to Merchant | 2,736 | 29.6% | 94.74% | ₹26.76 L | −11.7% |
| UPI QR Payments | 1,476 | 15.9% | 95.60% | ₹5.87 L | −14.8% |
| UPI Lite | 683 | 7.4% | 98.24% | ₹57,620 | −5.9% |
| UPI AutoPay | 304 | 3.3% | 87.50% | ₹4.88 L | +0.7% |
| RuPay Credit on UPI | 201 | 2.2% | 95.52% | ₹9.67 L | +2.6% |
| Credit on UPI | 127 | 1.4% | 92.91% | ₹13.34 L | −12.4% |
| UPI Lite Auto Top-Up | 87 | 0.9% | 95.40% | ₹87,961 | +4.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,879 | 94.27% | 95.40% | ₹36.77 L | normal |
| HDFC Bank | 946 | 94.93% | 95.94% | ₹9.66 L | normal |
| Bank of Baroda | 738 | 95.66% | 94.99% | ₹9.22 L | normal |
| Union Bank of India | 656 | 95.58% | 94.81% | ₹6.99 L | normal |
| ICICI Bank | 570 | 95.26% | 96.29% | ₹10.03 L | normal |
| Punjab National Bank | 569 | 93.67% | 94.76% | ₹6.44 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,375 | 94.95% | 95.35% | ₹51.29 L | normal |
| Google Pay | 3,027 | 94.12% | 95.45% | ₹36.35 L | normal |
| Paytm | 736 | 94.84% | 94.98% | ₹7.49 L | normal |
| Navi | 371 | 91.91% | 95.86% | ₹6.07 L | ⚠ outlier |
| SuperMoney | 181 | 95.03% | 96.27% | ₹2.27 L | normal |
| BHIM | 112 | 90.18% | 94.59% | ₹80,970 | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,417 | 94.79% | ₹29.38 L |
| Food & Beverage | 1,400 | 96.29% | ₹5.89 L |
| Mobility | 639 | 96.56% | ₹3.16 L |
| Bills | 634 | 94.32% | ₹6.88 L |
| Healthcare | 322 | 95.03% | ₹2.80 L |
| Digital | 190 | 91.05% | ₹1.02 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,695 | 29.1% | 94.36% | ₹33.54 L |
| North | 2,389 | 25.8% | 93.72% | ₹27.11 L |
| West | 2,232 | 24.1% | 95.03% | ₹29.80 L |
| East | 1,114 | 12.0% | 95.42% | ₹12.57 L |
| Central | 825 | 8.9% | 94.18% | ₹7.27 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 21 | 95.24% | ₹1.06 L |
| Rapid Bazaar | Key Account | Retail | 236 | 95.76% | ₹96,064 |
| Aravalli Pharmacy | Large | Healthcare | 69 | 95.65% | ₹92,280 |
| Vasant Wardrobe | Key Account | Retail | 63 | 90.48% | ₹75,483 |
| Hampi Stores 2298 | Key Account | Retail | 82 | 89.02% | ₹54,205 |
| Urban Boutique | Key Account | Retail | 69 | 97.10% | ₹51,105 |
| Yamuna Restaurant | Key Account | Food & Beverage | 65 | 92.31% | ₹43,461 |
| Girnar Connect | Key Account | Bills | 99 | 96.97% | ₹42,213 |

## Failure analysis

Of 499 declined attempts, 401 were business declines (4.333% of attempts — balances, PINs and limits), 44 technical (0.475%), 44 timeouts (0.475%) and 10 risk declines (0.108%).

301 attempts were re-presentations of an earlier failure (3.25% of the day); 64.5% of them succeeded.

- Retries reached 301 attempts (3.25% of the day, 12.1 sigma above normal). 64.5% of re-presented payments recovered, so the retry path was doing its job.
- Decline code ZM (Invalid UPI PIN) fired 160 times — 1.729% of attempts against a trailing 1.139%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 27 times — 0.292% of attempts against a trailing 0.163%. Owner: Issuer.
- Decline code UX (Mandate execution outside permitted window) fired 17 times — 0.184% of attempts against a trailing 0.107%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 160 | 1.729% | 1.139% |
| Z9 | Insufficient funds | business | Customer | 153 | 1.653% | 1.464% |
| ZA | Transaction declined by customer | business | Customer | 34 | 0.367% | 0.423% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 27 | 0.292% | 0.163% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.292% | 0.232% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.227% | 0.227% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.184% | 0.107% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.151% | 0.140% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 82 | 67 |
| Auto-reversals | 36 | 21 |
| Disputes / chargebacks | 4 | 4 |
| Value returned | ₹1.14 L | ₹1.17 L |

## Customer behaviour

7,955 distinct customers transacted (−10.4% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,422 | 2,686 | 1.11 | 94.68% | ₹1,271 |
| merchant_heavy | 1,840 | 2,171 | 1.18 | 94.24% | ₹1,016 |
| power | 1,673 | 2,121 | 1.27 | 94.34% | ₹1,757 |
| small_ticket | 1,213 | 1,432 | 1.18 | 94.83% | ₹521 |
| occasional | 637 | 657 | 1.03 | 95.13% | ₹1,206 |
| new | 147 | 165 | 1.12 | 90.30% | ₹806 |
| dormant_returning | 23 | 23 | 1.00 | 91.30% | ₹581 |

## Operational events

- **INC-NET-0038** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 19:00 and 22:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0021** (Sev-2) — Bank of Baroda issuer decline spike, scoped to Bank of Baroda between 10:00 and 16:00. Bank of Baroda core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 160 times — 1.729% of attempts against a trailing 1.139%. Owner: Customer.
- Category Retail ran at 94.79% success on 2,417 attempts (41.0% of the day), 1.31pp down its own 28-day median.
- Product UPI Person to Merchant ran at 94.74% success on 2,736 attempts (29.6% of the day), 1.13pp down its own 28-day median.
- Decline code U54 (Transaction timed out at beneficiary) fired 27 times — 0.292% of attempts against a trailing 0.163%. Owner: Issuer.
- Region North ran at 93.72% success on 2,389 attempts (25.8% of the day), 1.60pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

11 February was an incident day: INC-NET-0038, INC-FRAUD-0049 were live and the rail closed at 94.47% success against a 95.41% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,255, successes=8,743, failed=499, pending=13, settled_value_inr=11,029,197.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=301; retry_share_pct=3.25; recovery_pct=64.45; z=12.11
- failures: failure_code=ZM; count=160; rate_pct=1.73; trailing_rate_pct=1.14; owner=Customer; z=3.27
- incidents: event_id=INC-NET-0038; kind=network_latency; severity=Sev-1; window=2026-02-10 to 2026-02-12; success_impact_pp=-12.04; volume_impact_pct=-11.11
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- incidents: event_id=INC-BANK-0021; kind=bank_outage; severity=Sev-2; window=2026-02-09 to 2026-02-11; success_impact_pp=-9.27; volume_impact_pct=-8.22
- categories: mcc_category=Retail; attempts=2,417; success_rate=94.79; own_median=96.09; z=-2.46
- products: product_name=UPI Person to Merchant; attempts=2,736; success_rate=94.74; own_median=95.86; z=-2.86
- failures: failure_code=U54; count=27; rate_pct=0.29; trailing_rate_pct=0.16; owner=Issuer; z=2.78
- geography: region=North; attempts=2,389; success_rate=93.72; own_median=95.32; z=-2.54
- adjustments: reversals=36; trailing_median=21; z=2.25

Refs: enterprise_data/warehouse/transactions, RPT-D37-DAILY, enterprise_data/warehouse/reference/incidents.parquet
