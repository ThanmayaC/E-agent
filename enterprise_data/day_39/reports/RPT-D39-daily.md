---
id: RPT-D39-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 12 Feb 2026)

**Report ID:** RPT-D39-DAILY · **Day 39 of 206** · **Derived from:** 9,919 transaction rows queried live from the warehouse

## Summary

The rail took **9,919 payment attempts** on Thursday 12 February 2026 (Working day) and settled **₹1.07 Cr** across 9,458 successful payments. Volume was +7.2% on yesterday and −5.4% on the same weekday last week. Success closed at **95.35%**, in line with the trailing 28-day median of 95.38%.

44 auto-reversals were raised, 3.4 sigma above the trailing median of 21.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,919 | +7.2% | −5.4% | 10,974 |
| Successful payments | 9,458 | +8.2% | −5.6% | 10,462 |
| Success rate | 95.35% | +0.88pp | −0.16pp | 95.27% |
| Settled value | ₹1.07 Cr | −3.3% | −20.2% | ₹1.25 Cr |
| Average ticket | ₹1,127 | −10.6% | −15.5% | ₹1,190 |
| Technical declines | 0.393% | −0.08pp | −0.05pp | 0.445% |
| Business declines | 3.781% | −0.55pp | +0.21pp | 3.547% |
| Risk declines | 0.131% | +0.02pp | +0.01pp | 0.147% |
| Timeout declines | 0.242% | −0.23pp | −0.02pp | 0.472% |
| Retry share | 1.31% | −1.94pp | +0.10pp | 1.57% |
| Latency p95 | 1,214 ms | −5.6% | −5.8% | 1,306 ms |
| Active customers | 8,505 | +6.9% | −4.4% | 9,232 |
| Active merchants | 1,232 | +2.8% | −1.7% | 1,260 |

## What moved

- Product UPI Lite is compounding — attempts up 34% across the trailing window to 676 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,538 | 35.7% | 94.66% | ₹36.27 L | −8.9% |
| UPI Person to Merchant | 3,121 | 31.5% | 96.09% | ₹27.38 L | +1.0% |
| UPI QR Payments | 1,565 | 15.8% | 96.23% | ₹6.76 L | −5.9% |
| UPI Lite | 676 | 6.8% | 98.22% | ₹59,552 | −6.8% |
| UPI AutoPay | 289 | 2.9% | 88.93% | ₹5.94 L | −4.3% |
| RuPay Credit on UPI | 213 | 2.1% | 92.96% | ₹7.52 L | +6.2% |
| Credit on UPI | 146 | 1.5% | 92.47% | ₹7.87 L | +5.4% |
| UPI Circle | 97 | 1.0% | 94.85% | ₹67,950 | −5.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,176 | 95.37% | 95.35% | ₹38.17 L | normal |
| HDFC Bank | 1,075 | 95.53% | 95.88% | ₹12.49 L | normal |
| Bank of Baroda | 732 | 94.67% | 94.99% | ₹6.45 L | normal |
| Union Bank of India | 669 | 94.47% | 94.81% | ₹6.10 L | normal |
| Axis Bank | 605 | 96.36% | 95.09% | ₹6.39 L | normal |
| Punjab National Bank | 588 | 95.24% | 94.71% | ₹5.92 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,632 | 95.32% | 95.22% | ₹48.28 L | normal |
| Google Pay | 3,363 | 95.15% | 95.45% | ₹36.54 L | normal |
| Paytm | 798 | 95.86% | 94.89% | ₹8.97 L | normal |
| Navi | 351 | 95.44% | 95.70% | ₹3.80 L | normal |
| SuperMoney | 185 | 94.59% | 96.27% | ₹2.20 L | normal |
| BHIM | 97 | 92.78% | 94.41% | ₹1.07 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,737 | 95.98% | ₹27.24 L |
| Food & Beverage | 1,547 | 96.25% | ₹6.88 L |
| Mobility | 636 | 97.48% | ₹4.23 L |
| Bills | 614 | 96.09% | ₹6.97 L |
| Healthcare | 343 | 96.79% | ₹2.67 L |
| Digital | 183 | 91.26% | ₹77,123 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,905 | 29.3% | 95.46% | ₹31.73 L |
| North | 2,491 | 25.1% | 95.46% | ₹29.78 L |
| West | 2,469 | 24.9% | 95.02% | ₹25.01 L |
| East | 1,169 | 11.8% | 95.21% | ₹12.42 L |
| Central | 885 | 8.9% | 95.82% | ₹7.68 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 83 | 95.18% | ₹1.96 L |
| Vega Electronics | Large | Retail | 33 | 93.94% | ₹1.22 L |
| Hampi Stores 2298 | Key Account | Retail | 98 | 97.96% | ₹95,530 |
| Ujjwal Water Board | Key Account | Bills | 28 | 96.43% | ₹84,178 |
| Rapid Bazaar | Key Account | Retail | 265 | 96.60% | ₹83,500 |
| Nova Chemists | Large | Healthcare | 30 | 93.33% | ₹65,451 |
| Yamuna Restaurant | Key Account | Food & Beverage | 54 | 96.30% | ₹49,136 |
| Urban Boutique | Key Account | Retail | 70 | 95.71% | ₹47,219 |

## Failure analysis

Of 451 declined attempts, 375 were business declines (3.781% of attempts — balances, PINs and limits), 39 technical (0.393%), 24 timeouts (0.242%) and 13 risk declines (0.131%).

130 attempts were re-presentations of an earlier failure (1.31% of the day); 60.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 156 | 1.573% | 1.491% |
| ZM | Invalid UPI PIN | business | Customer | 119 | 1.200% | 1.166% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.534% | 0.423% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.232% | 0.235% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.202% | 0.229% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 15 | 0.151% | 0.163% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 13 | 0.131% | 0.110% |
| UX | Mandate execution outside permitted window | business | PSP | 13 | 0.131% | 0.113% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 80 | 69 |
| Auto-reversals | 44 | 21 |
| Disputes / chargebacks | 6 | 4 |
| Value returned | ₹1.19 L | ₹1.16 L |

## Customer behaviour

8,505 distinct customers transacted (−4.0% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,643 | 2,955 | 1.12 | 94.72% | ₹1,071 |
| power | 1,782 | 2,286 | 1.28 | 94.93% | ₹1,596 |
| merchant_heavy | 1,927 | 2,244 | 1.16 | 96.08% | ₹812 |
| small_ticket | 1,255 | 1,493 | 1.19 | 95.45% | ₹485 |
| occasional | 713 | 743 | 1.04 | 96.37% | ₹1,558 |
| new | 161 | 174 | 1.08 | 96.55% | ₹621 |
| dormant_returning | 24 | 24 | 1.00 | 100.00% | ₹1,492 |

## Operational events

- **INC-NET-0038** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 19:00 and 22:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 44 auto-reversals were raised, 3.4 sigma above the trailing median of 21.
- Product UPI Lite is compounding — attempts up 34% across the trailing window to 676 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

12 February was an incident day: INC-NET-0038, INC-FRAUD-0049 were live and the rail closed at 95.35% success against a 95.38% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,919, successes=9,458, failed=451, pending=10, settled_value_inr=10,661,977.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-NET-0038; kind=network_latency; severity=Sev-1; window=2026-02-10 to 2026-02-12; success_impact_pp=-12.04; volume_impact_pct=-11.11
- adjustments: reversals=44; trailing_median=21; z=3.45
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- products: product_name=UPI Lite; attempts=676; window_growth_pct=34.1; success_rate=98.22
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- banks: payer_bank=Federal Bank; attempts=255; success_rate=96.86; own_median=95.13; z=2.03
- categories: mcc_category=Financial Services; attempts=150; own_median=131.5; z=2.27

Refs: enterprise_data/warehouse/transactions, RPT-D38-DAILY, enterprise_data/warehouse/reference/incidents.parquet
