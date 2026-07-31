---
id: RPT-D99-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-13T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 13 Apr 2026)

**Report ID:** RPT-D99-DAILY · **Day 99 of 206** · **Derived from:** 11,706 transaction rows queried live from the warehouse

## Summary

The rail took **11,706 payment attempts** on Monday 13 April 2026 (Working day) and settled **₹1.71 Cr** across 11,157 successful payments. Volume was +3.2% on yesterday and −14.3% on the same weekday last week. Success closed at **95.31%**, below the trailing 28-day median of 95.94%.

Decline code ZA (Transaction declined by customer) fired 68 times — 0.581% of attempts against a trailing 0.358%. Owner: Customer. Success rate closed at 95.31%, 0.63pp down the trailing median — a 2.8-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,706 | +3.2% | −14.3% | 12,815 |
| Successful payments | 11,157 | +3.2% | −15.1% | 12,241 |
| Success rate | 95.31% | −0.05pp | −0.88pp | 95.50% |
| Settled value | ₹1.71 Cr | +39.2% | −1.6% | ₹1.65 Cr |
| Average ticket | ₹1,531 | +34.9% | +16.0% | ₹1,348 |
| Technical declines | 0.547% | +0.11pp | +0.10pp | 0.531% |
| Business declines | 3.511% | −0.07pp | +0.73pp | 3.078% |
| Risk declines | 0.154% | +0.03pp | +0.01pp | 0.143% |
| Timeout declines | 0.367% | −0.03pp | −0.01pp | 0.626% |
| Retry share | 1.15% | −0.25pp | −1.63pp | 1.56% |
| Latency p95 | 1,272 ms | +1.8% | +0.2% | 1,334 ms |
| Active customers | 9,952 | +3.9% | −11.4% | 10,627 |
| Active merchants | 1,372 | +1.8% | −3.8% | 1,386 |

## What moved

- Success rate closed at 95.31%, 0.63pp down the trailing median — a 2.8-sigma move.
- Issuer State Bank of India ran at 94.81% success on 3,798 attempts (32.4% of the day), 1.18pp down its own 28-day median.
- App Google Pay ran at 94.91% success on 3,815 attempts (32.6% of the day), 0.84pp down its own 28-day median.
- Region North ran at 95.07% success on 2,963 attempts (25.3% of the day), 0.77pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 35% across the trailing window to 254 today, with success holding, so the growth is healthy and worth funding.
- Product RuPay Credit on UPI is compounding — attempts up 32% across the trailing window to 369 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,135 | 35.3% | 94.68% | ₹42.13 L | −7.1% |
| UPI Person to Merchant | 3,120 | 26.7% | 96.06% | ₹28.44 L | −10.3% |
| UPI QR Payments | 1,844 | 15.8% | 96.10% | ₹7.47 L | −15.1% |
| UPI Lite | 1,006 | 8.6% | 97.91% | ₹89,286 | −5.4% |
| RuPay Credit on UPI | 369 | 3.2% | 94.85% | ₹25.03 L | +43.6% |
| UPI AutoPay | 304 | 2.6% | 89.80% | ₹5.97 L | −5.0% |
| UPI Circle | 295 | 2.5% | 93.22% | ₹2.63 L | +21.4% |
| Credit on UPI | 254 | 2.2% | 96.06% | ₹35.27 L | +43.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,798 | 94.81% | 95.99% | ₹50.84 L | ⚠ outlier |
| HDFC Bank | 1,323 | 96.30% | 95.76% | ₹19.31 L | normal |
| Bank of Baroda | 856 | 96.38% | 95.81% | ₹8.09 L | normal |
| Union Bank of India | 787 | 96.19% | 95.89% | ₹10.62 L | normal |
| ICICI Bank | 715 | 95.38% | 96.30% | ₹12.54 L | normal |
| Axis Bank | 697 | 93.40% | 95.83% | ₹8.88 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,546 | 95.55% | 95.93% | ₹80.68 L | normal |
| Google Pay | 3,815 | 94.91% | 95.76% | ₹57.86 L | ⚠ outlier |
| Paytm | 945 | 94.81% | 96.01% | ₹8.06 L | normal |
| Navi | 481 | 95.43% | 96.03% | ₹5.13 L | normal |
| SuperMoney | 222 | 94.14% | 95.09% | ₹3.19 L | normal |
| FamApp | 121 | 93.39% | 97.11% | ₹1.77 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,231 | 96.19% | ₹41.01 L |
| Food & Beverage | 1,807 | 96.02% | ₹8.09 L |
| Mobility | 791 | 95.95% | ₹4.68 L |
| Bills | 703 | 94.88% | ₹8.39 L |
| Healthcare | 410 | 97.07% | ₹11.86 L |
| Digital | 182 | 93.96% | ₹94,730 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,464 | 29.6% | 95.32% | ₹54.59 L |
| North | 2,963 | 25.3% | 95.07% | ₹38.67 L |
| West | 2,868 | 24.5% | 95.64% | ₹46.86 L |
| East | 1,414 | 12.1% | 95.05% | ₹20.29 L |
| Central | 997 | 8.5% | 95.39% | ₹10.40 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 25 | 96.00% | ₹3.27 L |
| Vasant Wardrobe | Key Account | Retail | 72 | 94.44% | ₹1.69 L |
| Rapid Bazaar | Key Account | Retail | 301 | 98.01% | ₹1.34 L |
| Ujjwal Water Board | Key Account | Bills | 47 | 93.62% | ₹98,925 |
| Hampi Styles | Key Account | Retail | 38 | 97.37% | ₹79,087 |
| Yamuna Restaurant | Key Account | Food & Beverage | 66 | 90.91% | ₹78,606 |
| Urban Boutique | Key Account | Retail | 88 | 94.32% | ₹59,690 |
| Kaveri Emporium | Large | Retail | 29 | 96.55% | ₹54,846 |

## Failure analysis

Of 536 declined attempts, 411 were business declines (3.511% of attempts — balances, PINs and limits), 64 technical (0.547%), 43 timeouts (0.367%) and 18 risk declines (0.154%).

135 attempts were re-presentations of an earlier failure (1.15% of the day); 61.5% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 68 times — 0.581% of attempts against a trailing 0.358%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 173 | 1.478% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 127 | 1.085% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 68 | 0.581% | 0.358% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 30 | 0.256% | 0.159% |
| U30 | Debit failed at remitter bank | technical | Issuer | 30 | 0.256% | 0.186% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.231% | 0.221% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.137% | 0.103% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.137% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 78 | 74 |
| Auto-reversals | 34 | 22 |
| Disputes / chargebacks | 13 | 11 |
| Value returned | ₹1.39 L | ₹1.55 L |

## Customer behaviour

9,952 distinct customers transacted (−6.1% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,996 | 3,405 | 1.14 | 95.12% | ₹1,494 |
| power | 2,093 | 2,695 | 1.29 | 95.03% | ₹1,947 |
| merchant_heavy | 2,281 | 2,671 | 1.17 | 95.28% | ₹1,394 |
| small_ticket | 1,530 | 1,835 | 1.20 | 95.86% | ₹663 |
| occasional | 820 | 849 | 1.04 | 96.00% | ₹1,835 |
| new | 201 | 219 | 1.09 | 94.52% | ₹817 |
| dormant_returning | 31 | 32 | 1.03 | 96.88% | ₹2,191 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 68 times — 0.581% of attempts against a trailing 0.358%. Owner: Customer.
- Success rate closed at 95.31%, 0.63pp down the trailing median — a 2.8-sigma move.
- Issuer State Bank of India ran at 94.81% success on 3,798 attempts (32.4% of the day), 1.18pp down its own 28-day median.
- App Google Pay ran at 94.91% success on 3,815 attempts (32.6% of the day), 0.84pp down its own 28-day median.
- Region North ran at 95.07% success on 2,963 attempts (25.3% of the day), 0.77pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 35% across the trailing window to 254 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 13 April: success came in 0.63pp below baseline at 95.31% on 11,706 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-13` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,706, successes=11,157, failed=536, pending=13, settled_value_inr=17,080,955.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZA; count=68; rate_pct=0.58; trailing_rate_pct=0.36; owner=Customer; z=3.79
- headline: success_rate=95.31; trailing_median=95.94; z=-2.79
- banks: payer_bank=State Bank of India; attempts=3,798; success_rate=94.81; own_median=95.99; z=-2.36
- psps: payer_psp=Google Pay; attempts=3,815; success_rate=94.91; own_median=95.76; z=-2.11
- geography: region=North; attempts=2,963; success_rate=95.07; own_median=95.84; z=-2.27
- products: product_name=Credit on UPI; attempts=254; window_growth_pct=35.2; success_rate=96.06
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- products: product_name=RuPay Credit on UPI; attempts=369; window_growth_pct=31.7; success_rate=94.85
- products: product_name=UPI Lite; attempts=1,006; success_rate=97.91; own_median=98.94; z=-2.51
- banks: payer_bank=Axis Bank; attempts=697; success_rate=93.4; own_median=95.83; z=-2.43

Refs: enterprise_data/warehouse/transactions, RPT-D98-DAILY, enterprise_data/warehouse/reference/incidents.parquet
