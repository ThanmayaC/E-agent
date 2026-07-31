---
id: RPT-D16-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 20 Jan 2026)

**Report ID:** RPT-D16-DAILY · **Day 16 of 206** · **Derived from:** 9,351 transaction rows queried live from the warehouse

## Summary

The rail took **9,351 payment attempts** on Tuesday 20 January 2026 (Working day) and settled **₹1.09 Cr** across 8,846 successful payments. Volume was −6.4% on yesterday and −12.0% on the same weekday last week. Success closed at **94.60%**, below the trailing 28-day median of 95.43%.

Decline code ZM (Invalid UPI PIN) fired 151 times — 1.615% of attempts against a trailing 1.103%. Owner: Customer. 3 disputes were raised, 2.5 sigma above the trailing median of 0.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,351 | −6.4% | −12.0% | 10,236 |
| Successful payments | 8,846 | −6.5% | −12.2% | 9,737 |
| Success rate | 94.60% | −0.09pp | −0.27pp | 95.10% |
| Settled value | ₹1.09 Cr | −1.7% | −10.8% | ₹1.16 Cr |
| Average ticket | ₹1,235 | +5.2% | +1.6% | ₹1,188 |
| Technical declines | 0.610% | −0.24pp | −0.06pp | 0.641% |
| Business declines | 4.256% | +0.31pp | +0.66pp | 3.601% |
| Risk declines | 0.096% | +0.03pp | −0.04pp | 0.130% |
| Timeout declines | 0.321% | −0.06pp | −0.30pp | 0.395% |
| Retry share | 1.84% | +0.01pp | −0.23pp | 1.50% |
| Latency p95 | 1,299 ms | +3.5% | +5.1% | 1,247 ms |
| Active customers | 8,022 | −5.6% | −10.7% | 8,685 |
| Active merchants | 1,173 | −1.3% | −4.9% | 1,200 |

## What moved

- Success rate closed at 94.60%, 0.83pp down the trailing median — a 1.6-sigma move.
- Region West carried 2,313 attempts, 8% down its trailing median and 24.7% of the day's volume.
- Category Bills ran at 94.19% success on 620 attempts (10.7% of the day), 1.70pp down its own 28-day median.
- Category Food & Beverage carried 1,340 attempts, 9% down its trailing median and 23.1% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,553 | 38.0% | 93.64% | ₹35.84 L | −11.5% |
| UPI Person to Merchant | 2,845 | 30.4% | 95.89% | ₹27.37 L | −5.0% |
| UPI QR Payments | 1,260 | 13.5% | 94.76% | ₹4.32 L | −27.8% |
| UPI Lite | 589 | 6.3% | 98.98% | ₹52,426 | −7.5% |
| UPI AutoPay | 310 | 3.3% | 89.03% | ₹5.18 L | +2.0% |
| RuPay Credit on UPI | 225 | 2.4% | 94.22% | ₹10.13 L | +23.0% |
| Credit on UPI | 159 | 1.7% | 91.82% | ₹10.70 L | +11.2% |
| UPI Circle | 93 | 1.0% | 97.85% | ₹88,364 | +1.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,983 | 94.87% | 94.91% | ₹33.07 L | normal |
| HDFC Bank | 965 | 95.34% | 96.14% | ₹10.80 L | normal |
| Bank of Baroda | 751 | 94.67% | 94.46% | ₹8.29 L | normal |
| Union Bank of India | 641 | 93.60% | 94.78% | ₹9.20 L | normal |
| Punjab National Bank | 608 | 94.57% | 94.87% | ₹7.25 L | normal |
| Axis Bank | 574 | 93.03% | 95.39% | ₹7.32 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,444 | 94.76% | 95.47% | ₹50.12 L | normal |
| Google Pay | 3,068 | 94.43% | 95.24% | ₹36.72 L | normal |
| Paytm | 750 | 94.00% | 94.59% | ₹10.18 L | normal |
| Navi | 339 | 93.51% | 95.18% | ₹3.68 L | normal |
| SuperMoney | 201 | 97.51% | 95.75% | ₹1.88 L | normal |
| BHIM | 97 | 95.88% | 95.33% | ₹67,893 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,428 | 95.26% | ₹28.52 L |
| Food & Beverage | 1,340 | 95.90% | ₹6.78 L |
| Bills | 620 | 94.19% | ₹6.77 L |
| Mobility | 591 | 96.62% | ₹3.09 L |
| Healthcare | 317 | 96.21% | ₹2.97 L |
| Digital | 177 | 93.79% | ₹89,711 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,791 | 29.8% | 94.12% | ₹30.23 L |
| North | 2,333 | 24.9% | 94.60% | ₹27.01 L |
| West | 2,313 | 24.7% | 94.90% | ₹29.05 L |
| East | 1,132 | 12.1% | 95.05% | ₹15.82 L |
| Central | 782 | 8.4% | 94.76% | ₹7.12 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 38 | 92.11% | ₹2.58 L |
| Vasant Wardrobe | Key Account | Retail | 70 | 95.71% | ₹1.60 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 94.52% | ₹97,041 |
| Rapid Bazaar | Key Account | Retail | 243 | 97.94% | ₹95,972 |
| Ujjwal Water Board | Key Account | Bills | 33 | 96.97% | ₹74,766 |
| Girnar Connect | Key Account | Bills | 123 | 92.68% | ₹70,005 |
| Hampi Stores 2298 | Key Account | Retail | 89 | 92.13% | ₹49,340 |
| Kaveri Emporium | Large | Retail | 30 | 100.00% | ₹35,743 |

## Failure analysis

Of 494 declined attempts, 398 were business declines (4.256% of attempts — balances, PINs and limits), 57 technical (0.610%), 30 timeouts (0.321%) and 9 risk declines (0.096%).

172 attempts were re-presentations of an earlier failure (1.84% of the day); 66.3% of them succeeded.

- Decline code ZM (Invalid UPI PIN) fired 151 times — 1.615% of attempts against a trailing 1.103%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 156 | 1.668% | 1.461% |
| ZM | Invalid UPI PIN | business | Customer | 151 | 1.615% | 1.103% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.385% | 0.382% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.289% | 0.262% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.267% | 0.273% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 15 | 0.160% | 0.184% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.150% | 0.183% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 12 | 0.128% | 0.143% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 72 | 32 |
| Auto-reversals | 29 | 22 |
| Disputes / chargebacks | 3 | 0 |
| Value returned | ₹1.14 L | ₹64,902 |

## Customer behaviour

8,022 distinct customers transacted (−9.2% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,399 | 2,687 | 1.12 | 94.38% | ₹1,284 |
| power | 1,706 | 2,188 | 1.28 | 94.79% | ₹1,555 |
| merchant_heavy | 1,838 | 2,141 | 1.16 | 95.05% | ₹1,021 |
| small_ticket | 1,255 | 1,475 | 1.18 | 94.51% | ₹652 |
| occasional | 635 | 664 | 1.05 | 93.83% | ₹1,221 |
| new | 174 | 181 | 1.04 | 93.92% | ₹585 |
| dormant_returning | 15 | 15 | 1.00 | 93.33% | ₹481 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 151 times — 1.615% of attempts against a trailing 1.103%. Owner: Customer.
- 3 disputes were raised, 2.5 sigma above the trailing median of 0.
- Success rate closed at 94.60%, 0.83pp down the trailing median — a 1.6-sigma move.
- Category Bills ran at 94.19% success on 620 attempts (10.7% of the day), 1.70pp down its own 28-day median.
- Issuer Axis Bank ran at 93.03% success on 574 attempts (6.1% of the day), 2.36pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 20 January: success came in 0.83pp below baseline at 94.60% on 9,351 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,351, successes=8,846, failed=494, pending=11, settled_value_inr=10,923,875.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZM; count=151; rate_pct=1.61; trailing_rate_pct=1.1; owner=Customer; z=3.91
- adjustments: chargebacks=3; trailing_median=0; z=2.49
- headline: success_rate=94.6; trailing_median=95.43; z=-1.62
- geography: region=West; attempts=2,313; own_median=2,515; z=-3.24
- categories: mcc_category=Bills; attempts=620; success_rate=94.19; own_median=95.89; z=-3.31
- categories: mcc_category=Food & Beverage; attempts=1,340; own_median=1,470; z=-2.37
- banks: payer_bank=Axis Bank; attempts=574; success_rate=93.03; own_median=95.39; z=-2.95
- products: product_name=UPI QR Payments; attempts=1,260; own_median=1,744; z=-2.53
- banks: payer_bank=HDFC Bank; attempts=965; own_median=1,135; z=-2.49
- banks: payer_bank=IndusInd Bank; attempts=194; own_median=240; z=-3.88

Refs: enterprise_data/warehouse/transactions, RPT-D15-DAILY, enterprise_data/warehouse/reference/incidents.parquet
