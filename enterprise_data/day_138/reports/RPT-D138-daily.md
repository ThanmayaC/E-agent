---
id: RPT-D138-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 22 May 2026)

**Report ID:** RPT-D138-DAILY · **Day 138 of 206** · **Derived from:** 13,859 transaction rows queried live from the warehouse

## Summary

The rail took **13,859 payment attempts** on Friday 22 May 2026 (Working day) and settled **₹2.23 Cr** across 13,290 successful payments. Volume was +5.3% on yesterday and −2.6% on the same weekday last week. Success closed at **95.89%**, in line with the trailing 28-day median of 96.03%.

Decline code Z9 (Insufficient funds) fired 197 times — 1.421% of attempts against a trailing 1.181%. Owner: Customer. Product UPI International is compounding — attempts up 72% across the trailing window to 176 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,859 | +5.3% | −2.6% | 14,883 |
| Successful payments | 13,290 | +4.8% | +0.4% | 14,277 |
| Success rate | 95.89% | −0.48pp | +2.91pp | 95.93% |
| Settled value | ₹2.23 Cr | +22.4% | +13.4% | ₹2.00 Cr |
| Average ticket | ₹1,678 | +16.8% | +12.9% | ₹1,400 |
| Technical declines | 0.440% | +0.11pp | −0.91pp | 0.509% |
| Business declines | 3.153% | +0.32pp | +0.09pp | 2.920% |
| Risk declines | 0.115% | +0.00pp | −0.04pp | 0.125% |
| Timeout declines | 0.281% | +0.00pp | −2.05pp | 0.410% |
| Retry share | 1.10% | −0.17pp | −2.09pp | 1.38% |
| Latency p95 | 1,303 ms | +3.7% | −34.1% | 1,291 ms |
| Active customers | 11,477 | +4.3% | −0.7% | 12,122 |
| Active merchants | 1,467 | +0.5% | −2.7% | 1,500 |

## What moved

- Product UPI International is compounding — attempts up 72% across the trailing window to 176 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 59% across the trailing window to 604 today, with success holding, so the growth is healthy and worth funding.
- Region West ran at 94.95% success on 3,425 attempts (24.7% of the day), 0.94pp down its own 28-day median.
- Issuer HDFC Bank ran at 95.17% success on 1,532 attempts (11.1% of the day), 1.01pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,530 | 32.7% | 95.23% | ₹47.54 L | +3.6% |
| UPI Person to Merchant | 3,400 | 24.5% | 95.85% | ₹37.14 L | −12.5% |
| UPI QR Payments | 2,237 | 16.1% | 95.75% | ₹10.32 L | −4.8% |
| UPI Lite | 1,480 | 10.7% | 99.26% | ₹1.45 L | −11.5% |
| UPI Circle | 604 | 4.4% | 97.35% | ₹4.51 L | +18.0% |
| Credit on UPI | 459 | 3.3% | 96.08% | ₹48.71 L | +31.3% |
| RuPay Credit on UPI | 373 | 2.7% | 96.25% | ₹27.36 L | +2.8% |
| UPI AutoPay | 317 | 2.3% | 91.17% | ₹5.84 L | −3.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,379 | 96.07% | 96.04% | ₹62.58 L | normal |
| HDFC Bank | 1,532 | 95.17% | 96.18% | ₹23.74 L | ⚠ outlier |
| Bank of Baroda | 997 | 95.49% | 95.81% | ₹14.91 L | normal |
| Union Bank of India | 967 | 96.69% | 95.26% | ₹10.64 L | normal |
| ICICI Bank | 871 | 95.98% | 96.43% | ₹14.35 L | normal |
| Punjab National Bank | 852 | 94.48% | 95.61% | ₹17.45 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,530 | 95.79% | 95.95% | ₹1.02 Cr | normal |
| Google Pay | 4,586 | 95.84% | 95.85% | ₹84.59 L | normal |
| Paytm | 1,121 | 95.36% | 96.05% | ₹14.82 L | normal |
| Navi | 530 | 96.42% | 95.51% | ₹5.60 L | normal |
| SuperMoney | 266 | 98.12% | 96.11% | ₹2.98 L | normal |
| BHIM | 130 | 94.62% | 96.15% | ₹1.14 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,894 | 96.35% | ₹56.64 L |
| Food & Beverage | 2,177 | 96.51% | ₹10.77 L |
| Mobility | 1,175 | 97.02% | ₹6.69 L |
| Bills | 846 | 95.63% | ₹8.54 L |
| Healthcare | 501 | 97.01% | ₹8.40 L |
| Digital | 213 | 96.71% | ₹94,717 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,063 | 29.3% | 96.38% | ₹71.96 L |
| North | 3,551 | 25.6% | 96.09% | ₹45.47 L |
| West | 3,425 | 24.7% | 94.95% | ₹61.82 L |
| East | 1,650 | 11.9% | 96.30% | ₹27.43 L |
| Central | 1,170 | 8.4% | 95.81% | ₹16.35 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 39 | 94.87% | ₹3.57 L |
| Rapid Bazaar | Key Account | Retail | 384 | 95.83% | ₹1.96 L |
| Vasant Wardrobe | Key Account | Retail | 72 | 95.83% | ₹1.44 L |
| Hampi Styles | Key Account | Retail | 39 | 94.87% | ₹1.34 L |
| Hampi Stores 2298 | Key Account | Retail | 141 | 94.33% | ₹1.31 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 95.59% | ₹85,349 |
| Girnar Connect | Key Account | Bills | 159 | 96.23% | ₹77,100 |
| Urban Boutique | Key Account | Retail | 104 | 97.12% | ₹73,554 |

## Failure analysis

Of 553 declined attempts, 437 were business declines (3.153% of attempts — balances, PINs and limits), 61 technical (0.440%), 39 timeouts (0.281%) and 16 risk declines (0.115%).

153 attempts were re-presentations of an earlier failure (1.10% of the day); 64.1% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 197 times — 1.421% of attempts against a trailing 1.181%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 197 | 1.421% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 133 | 0.960% | 1.027% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.404% | 0.339% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.245% | 0.218% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.209% | 0.206% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.130% | 0.158% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.123% | 0.136% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.108% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 103 | 94 |
| Auto-reversals | 28 | 28 |
| Disputes / chargebacks | 13 | 14 |
| Value returned | ₹2.28 L | ₹1.88 L |

## Customer behaviour

11,477 distinct customers transacted (−1.0% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,589 | 4,092 | 1.14 | 95.82% | ₹1,712 |
| merchant_heavy | 2,685 | 3,252 | 1.21 | 96.16% | ₹1,149 |
| power | 2,406 | 3,250 | 1.35 | 95.69% | ₹2,496 |
| small_ticket | 1,697 | 2,091 | 1.23 | 95.60% | ₹761 |
| occasional | 867 | 922 | 1.06 | 96.53% | ₹1,456 |
| new | 211 | 230 | 1.09 | 96.52% | ₹1,806 |
| dormant_returning | 22 | 22 | 1.00 | 95.45% | ₹4,619 |

## Operational events

- **INC-PSP-0024** (Sev-3) — PhonePe app release regression, scoped to PhonePe between 19:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CMP-0063** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 197 times — 1.421% of attempts against a trailing 1.181%. Owner: Customer.
- Region West ran at 94.95% success on 3,425 attempts (24.7% of the day), 0.94pp down its own 28-day median.
- Issuer HDFC Bank ran at 95.17% success on 1,532 attempts (11.1% of the day), 1.01pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 72% across the trailing window to 176 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 59% across the trailing window to 604 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

22 May ran on trend at 95.89% success and ₹2.23 Cr settled. The movement worth carrying forward is in the decline profile: decline code Z9 (Insufficient funds) fired 197 times — 1.421% of attempts against a trailing 1.181%. Owner: Customer. 3 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,859, successes=13,290, failed=553, pending=16, settled_value_inr=22,303,207.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=197; rate_pct=1.42; trailing_rate_pct=1.18; owner=Customer; z=2.62
- products: product_name=UPI International; attempts=176; window_growth_pct=71.8; success_rate=94.32
- products: product_name=UPI Circle; attempts=604; window_growth_pct=59; success_rate=97.35
- geography: region=West; attempts=3,425; success_rate=94.95; own_median=95.89; z=-2.28
- banks: payer_bank=HDFC Bank; attempts=1,532; success_rate=95.17; own_median=96.18; z=-2.56
- incidents: event_id=INC-PSP-0024; kind=psp_degradation; severity=Sev-3; window=2026-05-21 to 2026-05-24; success_impact_pp=-4.06; volume_impact_pct=-6.35
- incidents: event_id=CMP-0063; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-22; success_impact_pp=-0.19; volume_impact_pct=75.81

Refs: enterprise_data/warehouse/transactions, RPT-D137-DAILY, enterprise_data/warehouse/reference/incidents.parquet
