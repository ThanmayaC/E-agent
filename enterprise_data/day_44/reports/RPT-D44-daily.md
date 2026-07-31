---
id: RPT-D44-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 17 Feb 2026)

**Report ID:** RPT-D44-DAILY · **Day 44 of 206** · **Derived from:** 10,229 transaction rows queried live from the warehouse

## Summary

The rail took **10,229 payment attempts** on Tuesday 17 February 2026 (Working day) and settled **₹1.18 Cr** across 9,757 successful payments. Volume was −6.1% on yesterday and +3.7% on the same weekday last week. Success closed at **95.39%**, in line with the trailing 28-day median of 95.44%.

8 disputes were raised, 2.7 sigma above the trailing median of 4.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,229 | −6.1% | +3.7% | 10,904 |
| Successful payments | 9,757 | −6.6% | +7.8% | 10,404 |
| Success rate | 95.39% | −0.47pp | +3.68pp | 95.37% |
| Settled value | ₹1.18 Cr | −11.4% | +10.9% | ₹1.24 Cr |
| Average ticket | ₹1,210 | −5.1% | +2.8% | ₹1,189 |
| Technical declines | 0.411% | −0.02pp | −0.59pp | 0.429% |
| Business declines | 3.705% | +0.41pp | −0.56pp | 3.534% |
| Risk declines | 0.127% | −0.01pp | −0.00pp | 0.141% |
| Timeout declines | 0.264% | +0.06pp | −2.38pp | 0.410% |
| Retry share | 1.11% | −0.04pp | −2.34pp | 1.45% |
| Latency p95 | 1,257 ms | −0.5% | −35.5% | 1,289 ms |
| Active customers | 8,769 | −4.8% | +5.6% | 9,193 |
| Active merchants | 1,223 | −2.5% | −0.9% | 1,257 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,840 | 37.5% | 94.71% | ₹40.29 L | −1.9% |
| UPI Person to Merchant | 3,064 | 30.0% | 96.02% | ₹25.50 L | −1.5% |
| UPI QR Payments | 1,547 | 15.1% | 96.06% | ₹7.99 L | −12.2% |
| UPI Lite | 683 | 6.7% | 98.54% | ₹58,448 | −6.1% |
| UPI AutoPay | 319 | 3.1% | 89.97% | ₹5.70 L | +7.4% |
| RuPay Credit on UPI | 199 | 1.9% | 94.47% | ₹9.10 L | −1.0% |
| Credit on UPI | 168 | 1.6% | 93.45% | ₹10.84 L | +15.9% |
| UPI Circle | 113 | 1.1% | 99.12% | ₹1.06 L | +8.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,214 | 95.64% | 95.57% | ₹38.53 L | normal |
| HDFC Bank | 1,137 | 96.31% | 95.94% | ₹14.27 L | normal |
| Bank of Baroda | 788 | 95.05% | 95.28% | ₹7.98 L | normal |
| Union Bank of India | 727 | 94.91% | 95.20% | ₹7.51 L | normal |
| Punjab National Bank | 668 | 94.16% | 94.76% | ₹10.00 L | normal |
| ICICI Bank | 640 | 94.53% | 96.31% | ₹7.21 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,810 | 95.20% | 95.38% | ₹54.48 L | normal |
| Google Pay | 3,406 | 95.27% | 95.63% | ₹41.43 L | normal |
| Paytm | 836 | 96.17% | 94.98% | ₹9.04 L | normal |
| Navi | 385 | 95.84% | 95.69% | ₹4.11 L | normal |
| SuperMoney | 197 | 94.92% | 96.27% | ₹1.51 L | normal |
| BHIM | 115 | 97.39% | 94.95% | ₹1.81 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,732 | 95.72% | ₹26.53 L |
| Food & Beverage | 1,497 | 96.79% | ₹8.38 L |
| Mobility | 662 | 96.53% | ₹4.34 L |
| Bills | 658 | 96.35% | ₹8.20 L |
| Healthcare | 324 | 95.68% | ₹3.14 L |
| Digital | 202 | 93.56% | ₹95,420 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,008 | 29.4% | 95.11% | ₹32.62 L |
| North | 2,653 | 25.9% | 95.78% | ₹29.50 L |
| West | 2,441 | 23.9% | 95.00% | ₹32.65 L |
| East | 1,221 | 11.9% | 96.07% | ₹14.79 L |
| Central | 906 | 8.9% | 95.25% | ₹8.51 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 29 | 96.55% | ₹1.94 L |
| Ujjwal Water Board | Key Account | Bills | 32 | 96.88% | ₹1.81 L |
| Rapid Bazaar | Key Account | Retail | 318 | 94.65% | ₹1.28 L |
| Girnar Connect | Key Account | Bills | 115 | 98.26% | ₹74,322 |
| Vasant Wardrobe | Key Account | Retail | 48 | 91.67% | ₹67,593 |
| Konark Boutique | Large | Retail | 18 | 88.89% | ₹52,359 |
| Urban Boutique | Key Account | Retail | 67 | 91.04% | ₹49,671 |
| Yamuna Restaurant | Key Account | Food & Beverage | 52 | 98.08% | ₹47,006 |

## Failure analysis

Of 461 declined attempts, 379 were business declines (3.705% of attempts — balances, PINs and limits), 42 technical (0.411%), 27 timeouts (0.264%) and 13 risk declines (0.127%).

114 attempts were re-presentations of an earlier failure (1.11% of the day); 57.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 161 | 1.574% | 1.447% |
| ZM | Invalid UPI PIN | business | Customer | 114 | 1.114% | 1.168% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.489% | 0.423% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.274% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 17 | 0.166% | 0.207% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.137% | 0.128% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 13 | 0.127% | 0.154% |
| UX | Mandate execution outside permitted window | business | PSP | 11 | 0.108% | 0.105% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 68 | 70 |
| Auto-reversals | 15 | 20 |
| Disputes / chargebacks | 8 | 4 |
| Value returned | ₹76,050 | ₹1.13 L |

## Customer behaviour

8,769 distinct customers transacted (−1.3% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,750 | 3,070 | 1.12 | 94.95% | ₹1,208 |
| power | 1,835 | 2,349 | 1.28 | 95.02% | ₹1,673 |
| merchant_heavy | 1,963 | 2,267 | 1.15 | 96.07% | ₹1,042 |
| small_ticket | 1,309 | 1,581 | 1.21 | 96.14% | ₹470 |
| occasional | 701 | 739 | 1.05 | 94.32% | ₹1,188 |
| new | 192 | 204 | 1.06 | 96.08% | ₹846 |
| dormant_returning | 19 | 19 | 1.00 | 100.00% | ₹658 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **MAINT-0087** (Sev-3) — Union Bank of India scheduled CBS maintenance, scoped to Union Bank of India between 01:00 and 05:00. Union Bank of India runs its announced core-banking maintenance slot every 35 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 8 disputes were raised, 2.7 sigma above the trailing median of 4.
- Issuer ICICI Bank ran at 94.53% success on 640 attempts (6.3% of the day), 1.78pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

17 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.39% success against a 95.44% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,229, successes=9,757, failed=461, pending=11, settled_value_inr=11,807,916.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- adjustments: chargebacks=8; trailing_median=4; z=2.7
- incidents: event_id=MAINT-0087; kind=maintenance_window; severity=Sev-3; window=2026-01-13 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- banks: payer_bank=ICICI Bank; attempts=640; success_rate=94.53; own_median=96.31; z=-2.29
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24

Refs: enterprise_data/warehouse/transactions, RPT-D43-DAILY, enterprise_data/warehouse/reference/incidents.parquet
