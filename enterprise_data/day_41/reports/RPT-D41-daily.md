---
id: RPT-D41-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 14 Feb 2026)

**Report ID:** RPT-D41-DAILY · **Day 41 of 206** · **Derived from:** 11,752 transaction rows queried live from the warehouse

## Summary

The rail took **11,752 payment attempts** on Saturday 14 February 2026 (Maha Shivaratri (build-up)) and settled **₹1.17 Cr** across 11,262 successful payments. Volume was +15.8% on yesterday and −7.5% on the same weekday last week. Success closed at **95.83%**, above the trailing 28-day median of 95.36%.

10 disputes were raised, 4.0 sigma above the trailing median of 4. Decline code XH (Account does not exist / frozen) fired 44 times — 0.374% of attempts against a trailing 0.233%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,752 | +15.8% | −7.5% | 10,971 |
| Successful payments | 11,262 | +16.3% | −8.0% | 10,463 |
| Success rate | 95.83% | +0.47pp | −0.46pp | 95.31% |
| Settled value | ₹1.17 Cr | +2.9% | −20.8% | ₹1.23 Cr |
| Average ticket | ₹1,042 | −11.5% | −14.0% | ₹1,178 |
| Technical declines | 0.417% | +0.04pp | +0.14pp | 0.438% |
| Business declines | 3.242% | −0.51pp | +0.31pp | 3.540% |
| Risk declines | 0.162% | +0.04pp | +0.00pp | 0.146% |
| Timeout declines | 0.315% | +0.02pp | +0.04pp | 0.448% |
| Retry share | 1.10% | −0.29pp | +0.18pp | 1.52% |
| Latency p95 | 1,221 ms | −2.5% | −3.0% | 1,296 ms |
| Active customers | 9,804 | +13.1% | −6.3% | 9,232 |
| Active merchants | 1,278 | +4.2% | −3.2% | 1,259 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,499 | 38.3% | 95.15% | ₹46.29 L | +15.9% |
| UPI Person to Merchant | 3,458 | 29.4% | 95.86% | ₹30.15 L | +11.6% |
| UPI QR Payments | 2,035 | 17.3% | 96.81% | ₹9.24 L | +22.0% |
| UPI Lite | 856 | 7.3% | 98.60% | ₹73,723 | +18.0% |
| UPI AutoPay | 293 | 2.5% | 94.20% | ₹4.70 L | −3.0% |
| UPI Circle | 149 | 1.3% | 91.95% | ₹96,850 | +45.4% |
| RuPay Credit on UPI | 119 | 1.0% | 95.80% | ₹6.85 L | −40.8% |
| UPI Lite Auto Top-Up | 80 | 0.7% | 98.75% | ₹83,446 | −4.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,691 | 96.02% | 95.39% | ₹38.05 L | normal |
| HDFC Bank | 1,285 | 96.42% | 95.80% | ₹12.46 L | normal |
| Bank of Baroda | 893 | 95.07% | 95.28% | ₹7.88 L | normal |
| Union Bank of India | 824 | 95.39% | 94.81% | ₹7.56 L | normal |
| Axis Bank | 741 | 94.87% | 95.09% | ₹6.75 L | normal |
| ICICI Bank | 709 | 96.05% | 96.29% | ₹6.91 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,527 | 95.82% | 95.22% | ₹58.66 L | normal |
| Google Pay | 3,850 | 96.16% | 95.56% | ₹35.80 L | normal |
| Paytm | 1,000 | 94.20% | 94.89% | ₹8.89 L | normal |
| Navi | 442 | 95.48% | 95.59% | ₹3.05 L | normal |
| SuperMoney | 229 | 96.94% | 95.88% | ₹2.32 L | normal |
| BHIM | 126 | 98.41% | 94.41% | ₹3.30 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,215 | 96.08% | ₹30.82 L |
| Food & Beverage | 1,800 | 96.83% | ₹7.72 L |
| Mobility | 780 | 96.92% | ₹3.60 L |
| Bills | 641 | 95.32% | ₹6.81 L |
| Healthcare | 335 | 97.01% | ₹1.75 L |
| Digital | 189 | 96.83% | ₹97,619 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,556 | 30.3% | 96.01% | ₹32.22 L |
| North | 2,885 | 24.5% | 95.49% | ₹31.97 L |
| West | 2,882 | 24.5% | 95.63% | ₹29.01 L |
| East | 1,378 | 11.7% | 96.95% | ₹14.82 L |
| Central | 1,051 | 8.9% | 95.24% | ₹9.31 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 30 | 96.67% | ₹1.45 L |
| Rapid Bazaar | Key Account | Retail | 337 | 95.55% | ₹1.30 L |
| Vasant Wardrobe | Key Account | Retail | 59 | 94.92% | ₹1.11 L |
| Hampi Stores 2298 | Key Account | Retail | 99 | 96.97% | ₹96,409 |
| Ujjwal Water Board | Key Account | Bills | 30 | 93.33% | ₹83,079 |
| Urban Boutique | Key Account | Retail | 100 | 97.00% | ₹81,948 |
| Kalinga Supermart | Large | Retail | 39 | 100.00% | ₹66,061 |
| Shakti Stores 1531 | Key Account | Retail | 85 | 92.94% | ₹58,149 |

## Failure analysis

Of 486 declined attempts, 381 were business declines (3.242% of attempts — balances, PINs and limits), 49 technical (0.417%), 37 timeouts (0.315%) and 19 risk declines (0.162%).

129 attempts were re-presentations of an earlier failure (1.10% of the day); 63.6% of them succeeded.

- Decline code XH (Account does not exist / frozen) fired 44 times — 0.374% of attempts against a trailing 0.233%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 156 | 1.327% | 1.483% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 1.072% | 1.201% |
| XH | Account does not exist / frozen | business | Issuer | 44 | 0.374% | 0.233% |
| ZA | Transaction declined by customer | business | Customer | 38 | 0.323% | 0.423% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.170% | 0.159% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.170% | 0.222% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.170% | 0.140% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 12 | 0.102% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 69 | 70 |
| Auto-reversals | 16 | 20 |
| Disputes / chargebacks | 10 | 4 |
| Value returned | ₹69,264 | ₹1.16 L |

## Customer behaviour

9,804 distinct customers transacted (+10.7% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,023 | 3,474 | 1.15 | 95.85% | ₹1,006 |
| power | 2,023 | 2,702 | 1.34 | 95.82% | ₹1,433 |
| merchant_heavy | 2,242 | 2,685 | 1.20 | 95.72% | ₹749 |
| small_ticket | 1,465 | 1,794 | 1.22 | 95.71% | ₹506 |
| occasional | 807 | 840 | 1.04 | 96.90% | ₹1,499 |
| new | 207 | 219 | 1.06 | 94.52% | ₹739 |
| dormant_returning | 37 | 38 | 1.03 | 92.11% | ₹686 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 10 disputes were raised, 4.0 sigma above the trailing median of 4.
- Decline code XH (Account does not exist / frozen) fired 44 times — 0.374% of attempts against a trailing 0.233%. Owner: Issuer.
- Product UPI Circle ran at 91.95% success on 149 attempts (1.3% of the day), 5.44pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

14 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.83% success against a 95.36% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,752, successes=11,262, failed=486, pending=4, settled_value_inr=11,732,059.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=10; trailing_median=4; z=4.05
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- failures: failure_code=XH; count=44; rate_pct=0.37; trailing_rate_pct=0.23; owner=Issuer; z=3.1
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=UPI AutoPay; attempts=293; success_rate=94.2; own_median=88.57; z=2.26
- products: product_name=UPI Circle; attempts=149; success_rate=91.95; own_median=97.39; z=-2.54
- categories: mcc_category=Financial Services; attempts=111; success_rate=93.69; own_median=86.22; z=2
- categories: mcc_category=Financial Services; attempts=111; own_median=134; z=-2.59
- products: product_name=UPI Circle; attempts=149; own_median=102.5; z=2.41

Refs: enterprise_data/warehouse/transactions, RPT-D40-DAILY, enterprise_data/warehouse/reference/incidents.parquet
