---
id: RPT-D09-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-13T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 13 Jan 2026)

**Report ID:** RPT-D09-DAILY · **Day 9 of 206** · **Derived from:** 10,621 transaction rows queried live from the warehouse

## Summary

The rail took **10,621 payment attempts** on Tuesday 13 January 2026 (Makar Sankranti / Pongal (build-up)) and settled **₹1.23 Cr** across 10,076 successful payments. Volume was +1.3% on yesterday and +1.1% on the same weekday last week. Success closed at **94.87%**, below the trailing 28-day median of 95.46%.

Retries reached 220 attempts (2.07% of the day, 4.9 sigma above normal). 64.5% of re-presented payments recovered, so the retry path was doing its job. 3 disputes were raised, 4.5 sigma above the trailing median of 0.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,621 | +1.3% | +1.1% | 10,414 |
| Successful payments | 10,076 | +2.1% | +0.5% | 9,916 |
| Success rate | 94.87% | +0.70pp | −0.59pp | 95.21% |
| Settled value | ₹1.23 Cr | +9.4% | +1.7% | ₹1.18 Cr |
| Average ticket | ₹1,216 | +7.2% | +1.2% | ₹1,193 |
| Technical declines | 0.668% | −0.16pp | +0.13pp | 0.607% |
| Business declines | 3.597% | −0.46pp | +0.34pp | 3.477% |
| Risk declines | 0.141% | −0.00pp | −0.05pp | 0.144% |
| Timeout declines | 0.621% | +0.09pp | +0.23pp | 0.416% |
| Retry share | 2.07% | −0.07pp | +0.68pp | 1.45% |
| Latency p95 | 1,236 ms | −2.4% | −1.5% | 1,242 ms |
| Active customers | 8,984 | +1.7% | +0.6% | 8,825 |
| Active merchants | 1,233 | +1.9% | +1.1% | 1,208 |

## What moved

- Success rate closed at 94.87%, 0.59pp down the trailing median — a 1.8-sigma move.
- Issuer State Bank of India ran at 94.09% success on 3,434 attempts (32.3% of the day), 1.14pp down its own 28-day median.
- Category Retail carried 3,117 attempts, 22% up its trailing median and 47.2% of the day's volume.
- Region North carried 2,718 attempts, 3% up its trailing median and 25.6% of the day's volume.
- Region Central ran at 94.17% success on 909 attempts (8.6% of the day), 1.23pp down its own 28-day median.
- Category Mobility carried 619 attempts, 7% down its trailing median and 9.4% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,014 | 37.8% | 93.90% | ₹43.46 L | −0.2% |
| UPI Person to Merchant | 3,086 | 29.1% | 95.53% | ₹28.90 L | +4.9% |
| UPI QR Payments | 1,855 | 17.5% | 95.63% | ₹7.49 L | +5.2% |
| UPI Lite | 617 | 5.8% | 97.57% | ₹54,309 | −12.5% |
| UPI AutoPay | 308 | 2.9% | 89.94% | ₹5.97 L | +2.3% |
| RuPay Credit on UPI | 174 | 1.6% | 92.53% | ₹9.11 L | −10.1% |
| Credit on UPI | 147 | 1.4% | 97.28% | ₹8.59 L | +2.1% |
| Recurring Payments | 97 | 0.9% | 92.78% | ₹5.03 L | +14.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,434 | 94.09% | 95.23% | ₹38.86 L | ⚠ outlier |
| HDFC Bank | 1,131 | 96.29% | 96.04% | ₹16.32 L | normal |
| Bank of Baroda | 809 | 94.07% | 95.23% | ₹9.42 L | normal |
| Union Bank of India | 705 | 94.04% | 95.09% | ₹6.75 L | normal |
| Axis Bank | 689 | 95.36% | 95.57% | ₹7.74 L | normal |
| Punjab National Bank | 639 | 94.37% | 95.51% | ₹6.86 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,109 | 94.99% | 95.51% | ₹58.99 L | normal |
| Google Pay | 3,448 | 94.90% | 95.58% | ₹38.08 L | normal |
| Paytm | 889 | 94.26% | 94.68% | ₹11.45 L | normal |
| Navi | 372 | 94.62% | 95.46% | ₹4.55 L | normal |
| SuperMoney | 205 | 96.10% | 95.95% | ₹2.40 L | normal |
| BHIM | 102 | 95.10% | 95.41% | ₹96,192 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,117 | 95.77% | ₹31.81 L |
| Food & Beverage | 1,465 | 95.36% | ₹7.93 L |
| Mobility | 619 | 95.96% | ₹3.58 L |
| Bills | 597 | 96.82% | ₹7.06 L |
| Healthcare | 296 | 96.96% | ₹4.06 L |
| Digital | 172 | 95.35% | ₹1.04 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,216 | 30.3% | 95.18% | ₹36.28 L |
| North | 2,718 | 25.6% | 94.89% | ₹32.65 L |
| West | 2,527 | 23.8% | 94.90% | ₹30.37 L |
| East | 1,251 | 11.8% | 94.48% | ₹13.03 L |
| Central | 909 | 8.6% | 94.17% | ₹10.16 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 28 | 92.86% | ₹2.85 L |
| Vasant Wardrobe | Key Account | Retail | 79 | 97.47% | ₹1.15 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 81 | 95.06% | ₹1.14 L |
| Rapid Bazaar | Key Account | Retail | 306 | 94.44% | ₹99,356 |
| Urban Boutique | Key Account | Retail | 94 | 96.81% | ₹71,544 |
| Girnar Connect | Key Account | Bills | 113 | 96.46% | ₹66,025 |
| Ujjwal Water Board | Key Account | Bills | 23 | 95.65% | ₹54,693 |
| Hampi Stores 2298 | Key Account | Retail | 98 | 96.94% | ₹50,748 |

## Failure analysis

Of 534 declined attempts, 382 were business declines (3.597% of attempts — balances, PINs and limits), 71 technical (0.668%), 66 timeouts (0.621%) and 15 risk declines (0.141%).

220 attempts were re-presentations of an earlier failure (2.07% of the day); 64.5% of them succeeded.

- Retries reached 220 attempts (2.07% of the day, 4.9 sigma above normal). 64.5% of re-presented payments recovered, so the retry path was doing its job.
- Decline code ZA (Transaction declined by customer) fired 48 times — 0.452% of attempts against a trailing 0.366%. Owner: Customer.
- Decline code UX (Mandate execution outside permitted window) fired 14 times — 0.132% of attempts against a trailing 0.078%. Owner: PSP.
- Decline code ZX (Mandate not found or revoked) fired 15 times — 0.141% of attempts against a trailing 0.072%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 154 | 1.450% | 1.460% |
| ZM | Invalid UPI PIN | business | Customer | 120 | 1.130% | 1.091% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.452% | 0.366% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 34 | 0.320% | 0.182% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.273% | 0.261% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.264% | 0.261% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.198% | 0.163% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 20 | 0.188% | 0.137% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 40 | 18 |
| Auto-reversals | 24 | 22 |
| Disputes / chargebacks | 3 | 0 |
| Value returned | ₹1.01 L | ₹33,529 |

## Customer behaviour

8,984 distinct customers transacted (+1.5% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,696 | 3,063 | 1.14 | 94.61% | ₹1,323 |
| power | 1,890 | 2,442 | 1.29 | 94.92% | ₹1,648 |
| merchant_heavy | 2,044 | 2,437 | 1.19 | 94.58% | ₹837 |
| small_ticket | 1,364 | 1,645 | 1.21 | 95.14% | ₹537 |
| occasional | 768 | 803 | 1.05 | 95.02% | ₹1,321 |
| new | 199 | 208 | 1.05 | 98.08% | ₹838 |
| dormant_returning | 23 | 23 | 1.00 | 100.00% | ₹719 |

## Operational events

- **INC-BANK-0017** (Sev-2) — State Bank of India issuer decline spike, scoped to State Bank of India between 19:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-PSP-0034** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **MAINT-0087** (Sev-3) — Union Bank of India scheduled CBS maintenance, scoped to Union Bank of India between 01:00 and 05:00. Union Bank of India runs its announced core-banking maintenance slot every 35 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.

## Risks and opportunities

### Risks

- 3 disputes were raised, 4.5 sigma above the trailing median of 0.
- Decline code ZA (Transaction declined by customer) fired 48 times — 0.452% of attempts against a trailing 0.366%. Owner: Customer.
- Success rate closed at 94.87%, 0.59pp down the trailing median — a 1.8-sigma move.
- Issuer State Bank of India ran at 94.09% success on 3,434 attempts (32.3% of the day), 1.14pp down its own 28-day median.
- Decline code UX (Mandate execution outside permitted window) fired 14 times — 0.132% of attempts against a trailing 0.078%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

13 January was an incident day: INC-BANK-0017, INC-PSP-0034 were live and the rail closed at 94.87% success against a 95.46% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-13` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,621, successes=10,076, failed=534, pending=11, settled_value_inr=12,250,209.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=220; retry_share_pct=2.07; recovery_pct=64.55; z=4.86
- adjustments: chargebacks=3; trailing_median=0; z=4.54
- failures: failure_code=ZA; count=48; rate_pct=0.45; trailing_rate_pct=0.37; owner=Customer; z=3.08
- incidents: event_id=INC-BANK-0017; kind=bank_outage; severity=Sev-2; window=2026-01-12 to 2026-01-14; success_impact_pp=-16.02; volume_impact_pct=-14.21
- incidents: event_id=INC-PSP-0034; kind=psp_degradation; severity=Sev-2; window=2026-01-12 to 2026-01-15; success_impact_pp=-6.55; volume_impact_pct=-10.26
- headline: success_rate=94.87; trailing_median=95.46; z=-1.85
- banks: payer_bank=State Bank of India; attempts=3,434; success_rate=94.09; own_median=95.23; z=-2.42
- failures: failure_code=UX; count=14; rate_pct=0.13; trailing_rate_pct=0.08; owner=PSP; z=4.02
- categories: mcc_category=Retail; attempts=3,117; own_median=2,550.5; z=2.48
- geography: region=North; attempts=2,718; own_median=2,636; z=2.99

Refs: enterprise_data/warehouse/transactions, RPT-D08-DAILY, enterprise_data/warehouse/reference/incidents.parquet
