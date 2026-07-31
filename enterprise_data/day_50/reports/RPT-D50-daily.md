---
id: RPT-D50-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 23 Feb 2026)

**Report ID:** RPT-D50-DAILY · **Day 50 of 206** · **Derived from:** 10,128 transaction rows queried live from the warehouse

## Summary

The rail took **10,128 payment attempts** on Monday 23 February 2026 (Working day) and settled **₹1.10 Cr** across 9,678 successful payments. Volume was +10.6% on yesterday and −7.1% on the same weekday last week. Success closed at **95.56%**, in line with the trailing 28-day median of 95.52%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,128 | +10.6% | −7.1% | 10,747 |
| Successful payments | 9,678 | +11.4% | −7.3% | 10,255 |
| Success rate | 95.56% | +0.72pp | −0.30pp | 95.38% |
| Settled value | ₹1.10 Cr | +18.0% | −17.4% | ₹1.21 Cr |
| Average ticket | ₹1,137 | +5.9% | −10.9% | ₹1,181 |
| Technical declines | 0.247% | −0.08pp | −0.18pp | 0.410% |
| Business declines | 3.693% | −0.68pp | +0.40pp | 3.580% |
| Risk declines | 0.138% | +0.02pp | +0.00pp | 0.135% |
| Timeout declines | 0.217% | −0.00pp | +0.02pp | 0.379% |
| Retry share | 1.22% | −0.15pp | +0.07pp | 1.43% |
| Latency p95 | 1,247 ms | +0.4% | −1.3% | 1,280 ms |
| Active customers | 8,682 | +9.3% | −5.7% | 9,087 |
| Active merchants | 1,240 | +3.9% | −1.2% | 1,254 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,544 | 35.0% | 94.44% | ₹35.66 L | −8.8% |
| UPI Person to Merchant | 2,965 | 29.3% | 96.09% | ₹28.05 L | −4.7% |
| UPI QR Payments | 1,820 | 18.0% | 96.54% | ₹7.31 L | +9.8% |
| UPI Lite | 692 | 6.8% | 98.84% | ₹61,315 | −4.6% |
| UPI AutoPay | 290 | 2.9% | 91.38% | ₹4.67 L | −3.3% |
| RuPay Credit on UPI | 242 | 2.4% | 96.69% | ₹12.44 L | +20.7% |
| Credit on UPI | 158 | 1.6% | 93.67% | ₹8.37 L | +8.2% |
| UPI Circle | 113 | 1.1% | 95.58% | ₹88,799 | +12.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,226 | 95.47% | 95.68% | ₹35.73 L | normal |
| HDFC Bank | 1,090 | 96.79% | 96.15% | ₹13.49 L | normal |
| Bank of Baroda | 771 | 95.33% | 95.45% | ₹8.67 L | normal |
| Union Bank of India | 663 | 95.93% | 95.34% | ₹6.54 L | normal |
| Axis Bank | 623 | 95.83% | 95.33% | ₹7.41 L | normal |
| Punjab National Bank | 612 | 95.92% | 94.23% | ₹7.27 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,805 | 95.30% | 95.54% | ₹51.96 L | normal |
| Google Pay | 3,374 | 95.91% | 95.63% | ₹37.71 L | normal |
| Paytm | 801 | 95.51% | 95.46% | ₹8.45 L | normal |
| Navi | 363 | 96.42% | 95.45% | ₹3.83 L | normal |
| SuperMoney | 205 | 96.10% | 96.32% | ₹1.88 L | normal |
| BHIM | 101 | 92.08% | 94.41% | ₹1.35 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,739 | 96.46% | ₹32.39 L |
| Food & Beverage | 1,622 | 96.36% | ₹7.90 L |
| Mobility | 715 | 96.78% | ₹3.59 L |
| Bills | 670 | 95.67% | ₹7.28 L |
| Healthcare | 329 | 98.18% | ₹2.54 L |
| Digital | 187 | 93.05% | ₹88,046 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,915 | 28.8% | 95.51% | ₹29.58 L |
| West | 2,576 | 25.4% | 95.73% | ₹29.32 L |
| North | 2,560 | 25.3% | 95.47% | ₹30.10 L |
| East | 1,206 | 11.9% | 95.19% | ₹12.71 L |
| Central | 871 | 8.6% | 95.98% | ₹8.36 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 30 | 86.67% | ₹3.09 L |
| Rapid Bazaar | Key Account | Retail | 262 | 96.56% | ₹1.29 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 98.53% | ₹1.22 L |
| Hampi Stores 2298 | Key Account | Retail | 73 | 95.89% | ₹96,785 |
| Hampi Styles | Key Account | Retail | 29 | 93.10% | ₹92,184 |
| Girnar Connect | Key Account | Bills | 131 | 94.66% | ₹55,712 |
| Urban Boutique | Key Account | Retail | 91 | 92.31% | ₹55,607 |
| Aravalli Pharmacy | Large | Healthcare | 53 | 98.11% | ₹52,116 |

## Failure analysis

Of 435 declined attempts, 374 were business declines (3.693% of attempts — balances, PINs and limits), 25 technical (0.247%), 22 timeouts (0.217%) and 14 risk declines (0.138%).

124 attempts were re-presentations of an earlier failure (1.22% of the day); 63.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 150 | 1.481% | 1.452% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 1.343% | 1.196% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.454% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.247% | 0.235% |
| U30 | Debit failed at remitter bank | technical | Issuer | 13 | 0.128% | 0.168% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 12 | 0.118% | 0.147% |
| ZX | Mandate not found or revoked | business | PSP | 10 | 0.099% | 0.091% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 9 | 0.089% | 0.106% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 56 | 70 |
| Auto-reversals | 16 | 17 |
| Disputes / chargebacks | 9 | 6 |
| Value returned | ₹63,322 | ₹97,625 |

## Customer behaviour

8,682 distinct customers transacted (−2.0% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,663 | 2,976 | 1.12 | 95.87% | ₹1,116 |
| power | 1,869 | 2,401 | 1.28 | 95.21% | ₹1,473 |
| merchant_heavy | 1,983 | 2,320 | 1.17 | 95.34% | ₹964 |
| small_ticket | 1,290 | 1,509 | 1.17 | 95.63% | ₹483 |
| occasional | 689 | 712 | 1.03 | 95.65% | ₹1,429 |
| new | 163 | 185 | 1.13 | 96.76% | ₹794 |
| dormant_returning | 25 | 25 | 1.00 | 96.00% | ₹804 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.

## Risks and opportunities

### Risks

- Product UPI Lite Auto Top-Up ran at 93.42% success on 76 attempts (0.8% of the day), 4.16pp down its own 28-day median.

### Opportunities

- Product RuPay Credit on UPI is compounding — attempts up 26% across the trailing window to 242 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

23 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.56% success against a 95.52% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,128, successes=9,678, failed=435, pending=15, settled_value_inr=11,007,420.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- products: product_name=RuPay Credit on UPI; attempts=242; window_growth_pct=26; success_rate=96.69
- incidents: event_id=MAINT-0084; kind=maintenance_window; severity=Sev-3; window=2026-01-24 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- products: product_name=UPI Lite Auto Top-Up; attempts=76; success_rate=93.42; own_median=97.58; z=-2.27

Refs: enterprise_data/warehouse/transactions, RPT-D49-DAILY, enterprise_data/warehouse/reference/incidents.parquet
