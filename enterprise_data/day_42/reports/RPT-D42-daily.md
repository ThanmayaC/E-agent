---
id: RPT-D42-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 15 Feb 2026)

**Report ID:** RPT-D42-DAILY · **Day 42 of 206** · **Derived from:** 10,643 transaction rows queried live from the warehouse

## Summary

The rail took **10,643 payment attempts** on Sunday 15 February 2026 (Maha Shivaratri) and settled **₹1.24 Cr** across 10,182 successful payments. Volume was −9.4% on yesterday and +2.1% on the same weekday last week. Success closed at **95.67%**, above the trailing 28-day median of 95.38%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,643 | −9.4% | +2.1% | 10,949 |
| Successful payments | 10,182 | −9.6% | +2.4% | 10,444 |
| Success rate | 95.67% | −0.16pp | +0.27pp | 95.34% |
| Settled value | ₹1.24 Cr | +6.0% | +22.0% | ₹1.23 Cr |
| Average ticket | ₹1,221 | +17.2% | +19.1% | ₹1,181 |
| Technical declines | 0.329% | −0.09pp | −0.03pp | 0.430% |
| Business declines | 3.514% | +0.27pp | −0.20pp | 3.538% |
| Risk declines | 0.094% | −0.07pp | −0.08pp | 0.142% |
| Timeout declines | 0.226% | −0.09pp | −0.02pp | 0.433% |
| Retry share | 1.12% | +0.02pp | −0.11pp | 1.50% |
| Latency p95 | 1,247 ms | +2.1% | +4.4% | 1,292 ms |
| Active customers | 9,054 | −7.6% | +2.3% | 9,220 |
| Active merchants | 1,254 | −1.9% | +3.5% | 1,259 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,921 | 36.8% | 95.08% | ₹43.30 L | +1.0% |
| UPI Person to Merchant | 3,301 | 31.0% | 95.79% | ₹35.07 L | +6.5% |
| UPI QR Payments | 1,733 | 16.3% | 96.83% | ₹7.09 L | +3.9% |
| UPI Lite | 809 | 7.6% | 99.13% | ₹65,256 | +11.5% |
| UPI AutoPay | 290 | 2.7% | 89.31% | ₹4.81 L | −3.5% |
| UPI Circle | 128 | 1.2% | 96.09% | ₹1.03 L | +24.9% |
| RuPay Credit on UPI | 123 | 1.2% | 94.31% | ₹13.03 L | −38.8% |
| Recurring Payments | 91 | 0.9% | 83.52% | ₹4.15 L | +10.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,431 | 95.48% | 95.46% | ₹41.82 L | normal |
| HDFC Bank | 1,161 | 95.00% | 95.88% | ₹10.85 L | normal |
| Bank of Baroda | 791 | 95.07% | 95.28% | ₹13.83 L | normal |
| Union Bank of India | 764 | 95.81% | 95.00% | ₹11.89 L | normal |
| Axis Bank | 649 | 96.15% | 95.05% | ₹6.43 L | normal |
| ICICI Bank | 648 | 96.76% | 96.29% | ₹6.34 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,951 | 96.16% | 95.22% | ₹58.59 L | normal |
| Google Pay | 3,676 | 95.67% | 95.59% | ₹44.57 L | normal |
| Paytm | 831 | 93.74% | 94.87% | ₹8.94 L | normal |
| Navi | 372 | 94.62% | 95.58% | ₹4.03 L | normal |
| SuperMoney | 190 | 95.79% | 96.27% | ₹1.50 L | normal |
| BHIM | 98 | 98.98% | 94.41% | ₹1.02 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,106 | 96.14% | ₹32.38 L |
| Food & Beverage | 1,606 | 96.39% | ₹6.96 L |
| Mobility | 652 | 96.93% | ₹3.06 L |
| Bills | 589 | 96.10% | ₹6.58 L |
| Healthcare | 294 | 97.96% | ₹1.72 L |
| Digital | 178 | 92.70% | ₹78,885 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,172 | 29.8% | 95.55% | ₹37.45 L |
| North | 2,686 | 25.2% | 95.12% | ₹35.03 L |
| West | 2,594 | 24.4% | 96.26% | ₹31.92 L |
| East | 1,226 | 11.5% | 96.66% | ₹12.79 L |
| Central | 965 | 9.1% | 94.72% | ₹7.16 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 75 | 93.33% | ₹1.39 L |
| Rapid Bazaar | Key Account | Retail | 319 | 96.55% | ₹1.21 L |
| Vega Electronics | Large | Retail | 23 | 91.30% | ₹1.19 L |
| Hampi Stores 2298 | Key Account | Retail | 93 | 97.85% | ₹68,568 |
| Urban Boutique | Key Account | Retail | 89 | 95.51% | ₹63,555 |
| Ujjwal Water Board | Key Account | Bills | 25 | 88.00% | ₹63,439 |
| Girnar Connect | Key Account | Bills | 108 | 97.22% | ₹57,269 |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 92.65% | ₹50,601 |

## Failure analysis

Of 443 declined attempts, 374 were business declines (3.514% of attempts — balances, PINs and limits), 35 technical (0.329%), 24 timeouts (0.226%) and 10 risk declines (0.094%).

119 attempts were re-presentations of an earlier failure (1.12% of the day); 63.0% of them succeeded.

- Decline code ZX (Mandate not found or revoked) fired 18 times — 0.169% of attempts against a trailing 0.089%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 147 | 1.381% | 1.483% |
| ZM | Invalid UPI PIN | business | Customer | 127 | 1.193% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.432% | 0.423% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.207% | 0.233% |
| ZX | Mandate not found or revoked | business | PSP | 18 | 0.169% | 0.089% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 13 | 0.122% | 0.159% |
| UX | Mandate execution outside permitted window | business | PSP | 11 | 0.103% | 0.105% |
| U30 | Debit failed at remitter bank | technical | Issuer | 11 | 0.103% | 0.219% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 57 | 70 |
| Auto-reversals | 13 | 20 |
| Disputes / chargebacks | 6 | 4 |
| Value returned | ₹66,467 | ₹1.16 L |

## Customer behaviour

9,054 distinct customers transacted (+2.2% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,745 | 3,121 | 1.14 | 95.83% | ₹1,280 |
| power | 1,938 | 2,472 | 1.28 | 95.06% | ₹1,488 |
| merchant_heavy | 2,065 | 2,444 | 1.18 | 96.03% | ₹1,164 |
| small_ticket | 1,380 | 1,631 | 1.18 | 96.20% | ₹459 |
| occasional | 721 | 753 | 1.04 | 94.82% | ₹1,284 |
| new | 179 | 196 | 1.09 | 94.90% | ₹925 |
| dormant_returning | 26 | 26 | 1.00 | 96.15% | ₹740 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code ZX (Mandate not found or revoked) fired 18 times — 0.169% of attempts against a trailing 0.089%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

15 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.67% success against a 95.38% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,643, successes=10,182, failed=443, pending=18, settled_value_inr=12,435,179.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- failures: failure_code=ZX; count=18; rate_pct=0.17; trailing_rate_pct=0.09; owner=PSP; z=3.46
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- banks: payer_bank=Federal Bank; attempts=256; success_rate=97.66; own_median=95.1; z=2.03
- products: product_name=Credit on UPI; attempts=56; own_median=145; z=-3.87

Refs: enterprise_data/warehouse/transactions, RPT-D41-DAILY, enterprise_data/warehouse/reference/incidents.parquet
