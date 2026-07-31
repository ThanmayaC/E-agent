---
id: RPT-D49-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 22 Feb 2026)

**Report ID:** RPT-D49-DAILY · **Day 49 of 206** · **Derived from:** 9,161 transaction rows queried live from the warehouse

## Summary

The rail took **9,161 payment attempts** on Sunday 22 February 2026 (Weekend) and settled **₹93.27 L** across 8,688 successful payments. Volume was −23.0% on yesterday and −13.9% on the same weekday last week. Success closed at **94.84%**, below the trailing 28-day median of 95.52%.

Decline code ZM (Invalid UPI PIN) fired 148 times — 1.616% of attempts against a trailing 1.176%. Owner: Customer. Category Food & Beverage ran at 95.19% success on 1,436 attempts (24.7% of the day), 1.54pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,161 | −23.0% | −13.9% | 10,775 |
| Successful payments | 8,688 | −23.6% | −14.7% | 10,281 |
| Success rate | 94.84% | −0.69pp | −0.83pp | 95.38% |
| Settled value | ₹93.27 L | −29.5% | −25.0% | ₹1.22 Cr |
| Average ticket | ₹1,074 | −7.7% | −12.1% | ₹1,183 |
| Technical declines | 0.327% | −0.03pp | −0.00pp | 0.417% |
| Business declines | 4.377% | +0.87pp | +0.86pp | 3.575% |
| Risk declines | 0.120% | −0.03pp | +0.03pp | 0.135% |
| Timeout declines | 0.218% | −0.13pp | −0.01pp | 0.386% |
| Retry share | 1.38% | +0.07pp | +0.26pp | 1.44% |
| Latency p95 | 1,242 ms | +2.1% | −0.4% | 1,282 ms |
| Active customers | 7,942 | −20.2% | −12.3% | 9,105 |
| Active merchants | 1,194 | −7.6% | −4.8% | 1,254 |

## What moved

- Category Food & Beverage ran at 95.19% success on 1,436 attempts (24.7% of the day), 1.54pp down its own 28-day median.
- Region North ran at 93.74% success on 2,334 attempts (25.5% of the day), 1.67pp down its own 28-day median.
- Success rate closed at 94.84%, 0.68pp down the trailing median — a 1.6-sigma move.
- Product RuPay Credit on UPI is compounding — attempts up 31% across the trailing window to 114 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,352 | 36.6% | 94.15% | ₹31.92 L | −14.3% |
| UPI Person to Merchant | 2,754 | 30.1% | 95.72% | ₹24.05 L | −11.5% |
| UPI QR Payments | 1,517 | 16.6% | 95.45% | ₹5.65 L | −10.6% |
| UPI Lite | 696 | 7.6% | 98.28% | ₹58,492 | −4.3% |
| UPI AutoPay | 304 | 3.3% | 87.50% | ₹4.96 L | +1.8% |
| RuPay Credit on UPI | 114 | 1.2% | 92.11% | ₹5.73 L | −43.1% |
| UPI Circle | 98 | 1.1% | 93.88% | ₹60,780 | −3.4% |
| Recurring Payments | 88 | 1.0% | 87.50% | ₹3.99 L | +4.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,855 | 94.89% | 95.68% | ₹30.00 L | normal |
| HDFC Bank | 998 | 95.69% | 96.15% | ₹9.68 L | normal |
| Bank of Baroda | 712 | 95.37% | 95.45% | ₹6.55 L | normal |
| Union Bank of India | 640 | 94.53% | 95.34% | ₹5.20 L | normal |
| Axis Bank | 588 | 96.60% | 95.20% | ₹7.33 L | normal |
| Punjab National Bank | 581 | 93.12% | 94.23% | ₹5.87 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,354 | 95.18% | 95.54% | ₹48.79 L | normal |
| Google Pay | 2,998 | 94.73% | 95.63% | ₹28.14 L | normal |
| Paytm | 749 | 94.13% | 95.46% | ₹6.75 L | normal |
| Navi | 324 | 92.90% | 95.47% | ₹2.60 L | ⚠ outlier |
| SuperMoney | 181 | 95.03% | 96.32% | ₹2.07 L | normal |
| YONO SBI | 85 | 96.47% | 95.62% | ₹59,519 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,383 | 96.27% | ₹20.12 L |
| Food & Beverage | 1,436 | 95.19% | ₹5.94 L |
| Mobility | 624 | 96.79% | ₹2.56 L |
| Bills | 533 | 94.37% | ₹7.01 L |
| Healthcare | 331 | 95.47% | ₹2.76 L |
| Digital | 204 | 90.69% | ₹1.14 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,756 | 30.1% | 94.88% | ₹29.55 L |
| North | 2,334 | 25.5% | 93.74% | ₹22.68 L |
| West | 2,208 | 24.1% | 95.34% | ₹20.78 L |
| East | 1,075 | 11.7% | 95.26% | ₹9.63 L |
| Central | 788 | 8.6% | 95.94% | ₹10.63 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 273 | 95.24% | ₹1.29 L |
| Ujjwal Water Board | Key Account | Bills | 22 | 90.91% | ₹1.28 L |
| Hampi Stores 2298 | Key Account | Retail | 80 | 96.25% | ₹69,416 |
| Vega Electronics | Large | Retail | 16 | 93.75% | ₹66,220 |
| Vasant Wardrobe | Key Account | Retail | 41 | 95.12% | ₹59,548 |
| Yamuna Restaurant | Key Account | Food & Beverage | 64 | 95.31% | ₹53,890 |
| Urban Boutique | Key Account | Retail | 68 | 97.06% | ₹43,808 |
| Tejas Bites | Key Account | Food & Beverage | 103 | 97.09% | ₹36,730 |

## Failure analysis

Of 462 declined attempts, 401 were business declines (4.377% of attempts — balances, PINs and limits), 30 technical (0.327%), 20 timeouts (0.218%) and 11 risk declines (0.120%).

126 attempts were re-presentations of an earlier failure (1.38% of the day); 59.5% of them succeeded.

- Decline code ZM (Invalid UPI PIN) fired 148 times — 1.616% of attempts against a trailing 1.176%. Owner: Customer.
- Decline code ZX (Mandate not found or revoked) fired 15 times — 0.164% of attempts against a trailing 0.087%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 152 | 1.659% | 1.452% |
| ZM | Invalid UPI PIN | business | Customer | 148 | 1.616% | 1.176% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.546% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.262% | 0.235% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.186% | 0.119% |
| ZX | Mandate not found or revoked | business | PSP | 15 | 0.164% | 0.087% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 11 | 0.120% | 0.147% |
| UX | Mandate execution outside permitted window | business | PSP | 11 | 0.120% | 0.105% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 88 | 68 |
| Auto-reversals | 21 | 17 |
| Disputes / chargebacks | 7 | 6 |
| Value returned | ₹1.64 L | ₹97,625 |

## Customer behaviour

7,942 distinct customers transacted (−10.5% on the 28-day median) at 1.15 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,447 | 2,670 | 1.09 | 95.24% | ₹1,046 |
| merchant_heavy | 1,816 | 2,133 | 1.17 | 95.64% | ₹746 |
| power | 1,675 | 2,105 | 1.26 | 93.87% | ₹1,529 |
| small_ticket | 1,190 | 1,404 | 1.18 | 94.30% | ₹419 |
| occasional | 633 | 660 | 1.04 | 95.76% | ₹1,528 |
| new | 168 | 176 | 1.05 | 90.91% | ₹686 |
| dormant_returning | 13 | 13 | 1.00 | 100.00% | ₹562 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 148 times — 1.616% of attempts against a trailing 1.176%. Owner: Customer.
- Category Food & Beverage ran at 95.19% success on 1,436 attempts (24.7% of the day), 1.54pp down its own 28-day median.
- Region North ran at 93.74% success on 2,334 attempts (25.5% of the day), 1.67pp down its own 28-day median.
- Decline code ZX (Mandate not found or revoked) fired 15 times — 0.164% of attempts against a trailing 0.087%. Owner: PSP.
- Success rate closed at 94.84%, 0.68pp down the trailing median — a 1.6-sigma move.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

22 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 94.84% success against a 95.52% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,161, successes=8,688, failed=462, pending=11, settled_value_inr=9,327,280.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZM; count=148; rate_pct=1.62; trailing_rate_pct=1.18; owner=Customer; z=2.79
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- categories: mcc_category=Food & Beverage; attempts=1,436; success_rate=95.19; own_median=96.74; z=-4.93
- geography: region=North; attempts=2,334; success_rate=93.74; own_median=95.42; z=-3.18
- failures: failure_code=ZX; count=15; rate_pct=0.16; trailing_rate_pct=0.09; owner=PSP; z=3.68
- headline: success_rate=94.84; trailing_median=95.52; z=-1.56
- products: product_name=RuPay Credit on UPI; attempts=114; window_growth_pct=31; success_rate=92.11
- banks: payer_bank=Canara Bank; attempts=570; success_rate=92.11; own_median=95.62; z=-2.88
- categories: mcc_category=Bills; attempts=533; success_rate=94.37; own_median=95.98; z=-2.2
- psps: payer_psp=Navi; attempts=324; success_rate=92.9; own_median=95.47; z=-2.41

Refs: enterprise_data/warehouse/transactions, RPT-D48-DAILY, enterprise_data/warehouse/reference/incidents.parquet
