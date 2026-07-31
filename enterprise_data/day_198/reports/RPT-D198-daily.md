---
id: RPT-D198-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-21T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 21 Jul 2026)

**Report ID:** RPT-D198-DAILY · **Day 198 of 206** · **Derived from:** 13,507 transaction rows queried live from the warehouse

## Summary

The rail took **13,507 payment attempts** on Tuesday 21 July 2026 (Working day) and settled **₹1.92 Cr** across 12,995 successful payments. Volume was −5.8% on yesterday and −14.4% on the same weekday last week. Success closed at **96.21%**, in line with the trailing 28-day median of 96.19%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,507 | −5.8% | −14.4% | 16,043 |
| Successful payments | 12,995 | −5.9% | −14.4% | 15,421 |
| Success rate | 96.21% | −0.11pp | +0.07pp | 96.15% |
| Settled value | ₹1.92 Cr | −4.0% | −18.7% | ₹2.09 Cr |
| Average ticket | ₹1,481 | +2.0% | −5.1% | ₹1,358 |
| Technical declines | 0.422% | −0.12pp | +0.04pp | 0.453% |
| Business declines | 2.843% | +0.18pp | −0.22pp | 2.816% |
| Risk declines | 0.148% | +0.04pp | +0.07pp | 0.108% |
| Timeout declines | 0.267% | +0.00pp | −0.01pp | 0.381% |
| Retry share | 1.16% | −0.05pp | +0.04pp | 1.31% |
| Latency p95 | 1,317 ms | +0.6% | +1.4% | 1,301 ms |
| Active customers | 11,406 | −4.3% | −12.2% | 13,077 |
| Active merchants | 1,547 | −0.1% | −1.3% | 1,607 |

## What moved

- Issuer Union Bank of India ran at 94.65% success on 954 attempts (7.1% of the day), 1.60pp down its own 28-day median.
- Category Food & Beverage ran at 97.89% success on 2,272 attempts (24.0% of the day), 0.68pp up its own 28-day median.
- Product Credit on UPI is compounding — attempts up 29% across the trailing window to 528 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,054 | 30.0% | 94.99% | ₹41.14 L | −10.5% |
| UPI Person to Merchant | 2,750 | 20.4% | 96.29% | ₹25.43 L | −24.8% |
| UPI QR Payments | 2,210 | 16.4% | 96.92% | ₹10.26 L | −12.8% |
| UPI Lite | 2,003 | 14.8% | 98.45% | ₹1.71 L | −21.6% |
| UPI Circle | 638 | 4.7% | 98.43% | ₹4.77 L | −22.5% |
| Credit on UPI | 528 | 3.9% | 95.45% | ₹44.63 L | +7.1% |
| RuPay Credit on UPI | 403 | 3.0% | 97.52% | ₹26.34 L | +9.2% |
| UPI AutoPay | 382 | 2.8% | 89.79% | ₹6.36 L | +1.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,239 | 96.51% | 96.20% | ₹53.45 L | normal |
| HDFC Bank | 1,445 | 97.02% | 96.41% | ₹22.07 L | normal |
| Bank of Baroda | 1,051 | 95.72% | 96.45% | ₹14.86 L | normal |
| Union Bank of India | 954 | 94.65% | 96.25% | ₹9.64 L | ⚠ outlier |
| Axis Bank | 824 | 97.21% | 96.31% | ₹13.16 L | normal |
| ICICI Bank | 804 | 96.64% | 96.34% | ₹11.49 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,407 | 96.35% | 96.21% | ₹78.71 L | normal |
| Google Pay | 4,480 | 95.80% | 96.14% | ₹62.32 L | normal |
| Paytm | 1,079 | 96.39% | 96.17% | ₹15.88 L | normal |
| Navi | 467 | 96.79% | 96.33% | ₹7.50 L | normal |
| SuperMoney | 266 | 98.12% | 96.34% | ₹8.79 L | normal |
| BHIM | 158 | 94.94% | 95.85% | ₹1.66 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,895 | 96.66% | ₹55.76 L |
| Food & Beverage | 2,272 | 97.89% | ₹12.09 L |
| Mobility | 1,250 | 97.52% | ₹6.90 L |
| Bills | 880 | 95.11% | ₹8.00 L |
| Healthcare | 512 | 97.66% | ₹15.46 L |
| Financial Services | 193 | 86.01% | ₹9.83 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,993 | 29.6% | 96.52% | ₹53.46 L |
| North | 3,436 | 25.4% | 95.84% | ₹52.45 L |
| West | 3,345 | 24.8% | 96.62% | ₹52.69 L |
| East | 1,557 | 11.5% | 95.95% | ₹21.55 L |
| Central | 1,176 | 8.7% | 95.41% | ₹12.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 84.85% | ₹2.70 L |
| Vasant Wardrobe | Key Account | Retail | 75 | 93.33% | ₹2.06 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 58 | 98.28% | ₹1.45 L |
| Rapid Bazaar | Key Account | Retail | 356 | 95.22% | ₹1.40 L |
| Hampi Styles | Key Account | Retail | 42 | 100.00% | ₹1.39 L |
| Girnar Connect | Key Account | Bills | 171 | 98.83% | ₹1.10 L |
| Swift Grill | Large | Food & Beverage | 46 | 97.83% | ₹1.08 L |
| Ujjwal Water Board | Key Account | Bills | 32 | 93.75% | ₹79,658 |

## Failure analysis

Of 497 declined attempts, 384 were business declines (2.843% of attempts — balances, PINs and limits), 57 technical (0.422%), 36 timeouts (0.267%) and 20 risk declines (0.148%).

157 attempts were re-presentations of an earlier failure (1.16% of the day); 72.6% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 56 times — 0.415% of attempts against a trailing 0.324%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 160 | 1.185% | 1.209% |
| ZM | Invalid UPI PIN | business | Customer | 117 | 0.866% | 0.978% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.415% | 0.324% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.192% | 0.184% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.155% | 0.111% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.148% | 0.128% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.141% | 0.172% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.118% | 0.092% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 102 | 112 |
| Auto-reversals | 23 | 23 |
| Disputes / chargebacks | 10 | 15 |
| Value returned | ₹1.31 L | ₹1.97 L |

## Customer behaviour

11,406 distinct customers transacted (−12.6% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,539 | 3,989 | 1.13 | 96.44% | ₹1,512 |
| power | 2,467 | 3,244 | 1.31 | 95.84% | ₹1,952 |
| merchant_heavy | 2,662 | 3,142 | 1.18 | 95.86% | ₹1,143 |
| small_ticket | 1,692 | 2,036 | 1.20 | 96.46% | ₹664 |
| occasional | 835 | 873 | 1.05 | 97.02% | ₹2,041 |
| new | 184 | 196 | 1.07 | 96.94% | ₹681 |
| dormant_returning | 27 | 27 | 1.00 | 96.30% | ₹718 |

## Operational events

- **INC-BANK-0012** (Sev-3) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 23:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 56 times — 0.415% of attempts against a trailing 0.324%. Owner: Customer.
- Issuer Union Bank of India ran at 94.65% success on 954 attempts (7.1% of the day), 1.60pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 29% across the trailing window to 528 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

21 July ran on trend at 96.21% success and ₹1.92 Cr settled. The movement worth carrying forward is in the decline profile: decline code ZA (Transaction declined by customer) fired 56 times — 0.415% of attempts against a trailing 0.324%. Owner: Customer. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-21` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,507, successes=12,995, failed=497, pending=15, settled_value_inr=19,243,173.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZA; count=56; rate_pct=0.41; trailing_rate_pct=0.32; owner=Customer; z=2.24
- banks: payer_bank=Union Bank of India; attempts=954; success_rate=94.65; own_median=96.25; z=-4.12
- categories: mcc_category=Food & Beverage; attempts=2,272; success_rate=97.89; own_median=97.21; z=2.04
- products: product_name=Credit on UPI; attempts=528; window_growth_pct=29.5; success_rate=95.45
- incidents: event_id=INC-BANK-0012; kind=bank_outage; severity=Sev-3; window=2026-07-20 to 2026-07-23; success_impact_pp=-4.37; volume_impact_pct=-3.88

Refs: enterprise_data/warehouse/transactions, RPT-D197-DAILY, enterprise_data/warehouse/reference/incidents.parquet
