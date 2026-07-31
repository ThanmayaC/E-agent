---
id: RPT-D47-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 20 Feb 2026)

**Report ID:** RPT-D47-DAILY · **Day 47 of 206** · **Derived from:** 10,930 transaction rows queried live from the warehouse

## Summary

The rail took **10,930 payment attempts** on Friday 20 February 2026 (Working day) and settled **₹1.26 Cr** across 10,451 successful payments. Volume was +9.7% on yesterday and +7.7% on the same weekday last week. Success closed at **95.62%**, in line with the trailing 28-day median of 95.49%.

9 disputes were raised, 2.7 sigma above the trailing median of 5.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,930 | +9.7% | +7.7% | 10,799 |
| Successful payments | 10,451 | +10.2% | +8.0% | 10,306 |
| Success rate | 95.62% | +0.43pp | +0.26pp | 95.39% |
| Settled value | ₹1.26 Cr | +12.5% | +10.4% | ₹1.23 Cr |
| Average ticket | ₹1,203 | +2.0% | +2.2% | ₹1,189 |
| Technical declines | 0.448% | +0.03pp | +0.07pp | 0.424% |
| Business declines | 3.413% | −0.49pp | −0.34pp | 3.538% |
| Risk declines | 0.119% | +0.02pp | +0.00pp | 0.135% |
| Timeout declines | 0.339% | +0.03pp | +0.04pp | 0.396% |
| Retry share | 1.34% | −0.31pp | −0.04pp | 1.45% |
| Latency p95 | 1,278 ms | −1.4% | +2.0% | 1,287 ms |
| Active customers | 9,252 | +8.2% | +6.7% | 9,121 |
| Active merchants | 1,277 | +3.4% | +4.1% | 1,256 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,144 | 37.9% | 94.91% | ₹44.03 L | +5.9% |
| UPI Person to Merchant | 3,230 | 29.6% | 95.88% | ₹32.06 L | +3.8% |
| UPI QR Payments | 1,652 | 15.1% | 96.49% | ₹7.20 L | −6.2% |
| UPI Lite | 770 | 7.0% | 98.05% | ₹71,496 | +5.8% |
| UPI AutoPay | 302 | 2.8% | 91.72% | ₹5.38 L | +1.2% |
| RuPay Credit on UPI | 286 | 2.6% | 95.45% | ₹12.47 L | +42.6% |
| Credit on UPI | 146 | 1.3% | 95.21% | ₹9.66 L | +0.0% |
| UPI Circle | 94 | 0.9% | 97.87% | ₹99,567 | −10.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,529 | 96.06% | 95.68% | ₹41.53 L | normal |
| HDFC Bank | 1,205 | 96.27% | 96.15% | ₹12.86 L | normal |
| Bank of Baroda | 817 | 96.45% | 95.30% | ₹10.02 L | normal |
| Union Bank of India | 731 | 94.53% | 95.33% | ₹9.40 L | normal |
| ICICI Bank | 663 | 95.02% | 96.31% | ₹6.28 L | normal |
| Canara Bank | 642 | 95.64% | 95.13% | ₹6.62 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,227 | 95.54% | 95.49% | ₹56.98 L | normal |
| Google Pay | 3,536 | 96.01% | 95.65% | ₹41.71 L | normal |
| Paytm | 947 | 95.35% | 95.68% | ₹12.52 L | normal |
| Navi | 403 | 93.30% | 95.58% | ₹4.97 L | ⚠ outlier |
| SuperMoney | 197 | 96.95% | 96.27% | ₹1.72 L | normal |
| BHIM | 129 | 93.02% | 94.74% | ₹2.21 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,926 | 95.93% | ₹33.61 L |
| Food & Beverage | 1,599 | 96.62% | ₹7.69 L |
| Mobility | 701 | 96.29% | ₹4.55 L |
| Bills | 666 | 96.85% | ₹7.64 L |
| Healthcare | 359 | 95.82% | ₹2.56 L |
| Digital | 204 | 95.59% | ₹1.08 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,182 | 29.1% | 95.22% | ₹35.48 L |
| North | 2,784 | 25.5% | 95.51% | ₹31.94 L |
| West | 2,671 | 24.4% | 95.92% | ₹34.10 L |
| East | 1,311 | 12.0% | 95.42% | ₹14.99 L |
| Central | 982 | 9.0% | 96.64% | ₹9.25 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 70 | 98.57% | ₹2.30 L |
| Vega Electronics | Large | Retail | 33 | 87.88% | ₹1.23 L |
| Rapid Bazaar | Key Account | Retail | 288 | 97.92% | ₹1.20 L |
| Hampi Styles | Key Account | Retail | 42 | 92.86% | ₹1.03 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 78 | 96.15% | ₹83,069 |
| Urban Boutique | Key Account | Retail | 92 | 100.00% | ₹68,960 |
| Girnar Connect | Key Account | Bills | 111 | 92.79% | ₹47,903 |
| Hampi Stores 2298 | Key Account | Retail | 91 | 96.70% | ₹43,420 |

## Failure analysis

Of 472 declined attempts, 373 were business declines (3.413% of attempts — balances, PINs and limits), 49 technical (0.448%), 37 timeouts (0.339%) and 13 risk declines (0.119%).

147 attempts were re-presentations of an earlier failure (1.34% of the day); 61.9% of them succeeded.

- Decline code YA (PSP not available) fired 15 times — 0.137% of attempts against a trailing 0.051%. Owner: PSP.
- Decline code UX (Mandate execution outside permitted window) fired 20 times — 0.183% of attempts against a trailing 0.105%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 159 | 1.455% | 1.440% |
| ZM | Invalid UPI PIN | business | Customer | 120 | 1.098% | 1.168% |
| ZA | Transaction declined by customer | business | Customer | 42 | 0.384% | 0.431% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.201% | 0.147% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.192% | 0.233% |
| UX | Mandate execution outside permitted window | business | PSP | 20 | 0.183% | 0.105% |
| YA | PSP not available | technical | PSP | 15 | 0.137% | 0.051% |
| U30 | Debit failed at remitter bank | technical | Issuer | 13 | 0.119% | 0.193% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 61 | 68 |
| Auto-reversals | 18 | 17 |
| Disputes / chargebacks | 9 | 5 |
| Value returned | ₹95,789 | ₹97,625 |

## Customer behaviour

9,252 distinct customers transacted (+4.2% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,859 | 3,239 | 1.13 | 95.00% | ₹1,333 |
| power | 1,940 | 2,530 | 1.30 | 96.01% | ₹1,522 |
| merchant_heavy | 2,085 | 2,469 | 1.18 | 96.19% | ₹883 |
| small_ticket | 1,412 | 1,689 | 1.20 | 95.56% | ₹696 |
| occasional | 733 | 767 | 1.05 | 94.78% | ₹1,143 |
| new | 194 | 206 | 1.06 | 97.09% | ₹635 |
| dormant_returning | 29 | 30 | 1.03 | 96.67% | ₹1,541 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0006** (Sev-1) — Punjab National Bank issuer decline spike, scoped to Punjab National Bank between 19:00 and 24:00. Punjab National Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 9 disputes were raised, 2.7 sigma above the trailing median of 5.
- Decline code YA (PSP not available) fired 15 times — 0.137% of attempts against a trailing 0.051%. Owner: PSP.
- Decline code UX (Mandate execution outside permitted window) fired 20 times — 0.183% of attempts against a trailing 0.105%. Owner: PSP.
- App Navi ran at 93.30% success on 403 attempts (3.7% of the day), 2.28pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

20 February was an incident day: INC-FRAUD-0048, INC-BANK-0006 were live and the rail closed at 95.62% success against a 95.49% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,930, successes=10,451, failed=472, pending=7, settled_value_inr=12,576,713.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- incidents: event_id=INC-BANK-0006; kind=bank_outage; severity=Sev-1; window=2026-02-19 to 2026-02-20; success_impact_pp=-25.39; volume_impact_pct=-22.52
- adjustments: chargebacks=9; trailing_median=5; z=2.7
- failures: failure_code=YA; count=15; rate_pct=0.14; trailing_rate_pct=0.05; owner=PSP; z=3.41
- failures: failure_code=UX; count=20; rate_pct=0.18; trailing_rate_pct=0.11; owner=PSP; z=2.03
- incidents: event_id=MAINT-0085; kind=maintenance_window; severity=Sev-3; window=2026-01-23 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- psps: payer_psp=Navi; attempts=403; success_rate=93.3; own_median=95.58; z=-2.54
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=RuPay Credit on UPI; attempts=286; own_median=200.5; z=2.26

Refs: enterprise_data/warehouse/transactions, RPT-D46-DAILY, enterprise_data/warehouse/reference/incidents.parquet
