---
id: RPT-D19-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 23 Jan 2026)

**Report ID:** RPT-D19-DAILY · **Day 19 of 206** · **Derived from:** 12,667 transaction rows queried live from the warehouse

## Summary

The rail took **12,667 payment attempts** on Friday 23 January 2026 (Republic Day Sale) and settled **₹1.51 Cr** across 12,093 successful payments. Volume was +14.2% on yesterday and +30.4% on the same weekday last week. Success closed at **95.47%**, in line with the trailing 28-day median of 95.24%.

Category Food & Beverage carried 1,882 attempts, 28% up its trailing median and 24.2% of the day's volume. Region West carried 3,117 attempts, 24% up its trailing median and 24.6% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,667 | +14.2% | +30.4% | 10,397 |
| Successful payments | 12,093 | +14.3% | +31.2% | 9,893 |
| Success rate | 95.47% | +0.12pp | +0.57pp | 95.12% |
| Settled value | ₹1.51 Cr | +24.0% | +29.8% | ₹1.18 Cr |
| Average ticket | ₹1,251 | +8.5% | −1.1% | ₹1,188 |
| Technical declines | 0.758% | +0.24pp | −0.02pp | 0.638% |
| Business declines | 3.166% | −0.31pp | −0.45pp | 3.580% |
| Risk declines | 0.134% | +0.01pp | +0.00pp | 0.131% |
| Timeout declines | 0.347% | −0.05pp | −0.07pp | 0.395% |
| Retry share | 1.29% | −0.11pp | −0.17pp | 1.49% |
| Latency p95 | 1,236 ms | −2.1% | −0.8% | 1,247 ms |
| Active customers | 10,442 | +12.2% | +26.2% | 8,800 |
| Active merchants | 1,294 | +7.2% | +9.3% | 1,205 |

## What moved

- Category Food & Beverage carried 1,882 attempts, 28% up its trailing median and 24.2% of the day's volume.
- Region West carried 3,117 attempts, 24% up its trailing median and 24.6% of the day's volume.
- Category Retail carried 3,530 attempts, 36% up its trailing median and 45.3% of the day's volume.
- Product UPI Person to Merchant carried 3,789 attempts, 28% up its trailing median and 29.9% of the day's volume.
- Attempt volume ran 2.7 standard deviations up its trailing 28-day median at 12,667, 30.4% up on the same weekday last week.
- App PhonePe carried 6,022 attempts, 22% up its trailing median and 47.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,877 | 38.5% | 94.75% | ₹52.95 L | +21.9% |
| UPI Person to Merchant | 3,789 | 29.9% | 95.70% | ₹42.49 L | +28.0% |
| UPI QR Payments | 2,066 | 16.3% | 96.37% | ₹9.17 L | +24.3% |
| UPI Lite | 803 | 6.3% | 99.13% | ₹77,677 | +25.7% |
| UPI AutoPay | 287 | 2.3% | 90.59% | ₹5.63 L | −5.9% |
| RuPay Credit on UPI | 249 | 2.0% | 95.98% | ₹18.24 L | +28.7% |
| Credit on UPI | 160 | 1.3% | 97.50% | ₹9.69 L | +17.2% |
| UPI Circle | 110 | 0.9% | 95.45% | ₹87,042 | +19.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,068 | 95.89% | 94.90% | ₹50.08 L | normal |
| HDFC Bank | 1,329 | 94.81% | 95.90% | ₹13.67 L | normal |
| Bank of Baroda | 934 | 95.93% | 94.70% | ₹9.47 L | normal |
| Union Bank of India | 865 | 95.38% | 94.72% | ₹10.89 L | normal |
| Axis Bank | 800 | 95.75% | 95.37% | ₹9.35 L | normal |
| ICICI Bank | 779 | 96.15% | 95.81% | ₹8.80 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,022 | 95.07% | 95.16% | ₹71.16 L | normal |
| Google Pay | 4,125 | 96.12% | 95.24% | ₹45.00 L | normal |
| Paytm | 1,023 | 94.82% | 94.49% | ₹18.25 L | normal |
| Navi | 449 | 96.21% | 95.37% | ₹4.67 L | normal |
| SuperMoney | 266 | 95.49% | 95.54% | ₹2.88 L | normal |
| BHIM | 131 | 95.42% | 95.41% | ₹1.71 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,530 | 96.26% | ₹46.18 L |
| Food & Beverage | 1,882 | 96.17% | ₹8.49 L |
| Mobility | 752 | 96.01% | ₹4.12 L |
| Bills | 708 | 95.76% | ₹9.46 L |
| Healthcare | 385 | 96.88% | ₹3.31 L |
| Digital | 180 | 94.44% | ₹72,963 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,761 | 29.7% | 95.67% | ₹46.06 L |
| North | 3,245 | 25.6% | 95.04% | ₹36.09 L |
| West | 3,117 | 24.6% | 95.80% | ₹38.14 L |
| East | 1,459 | 11.5% | 95.54% | ₹21.49 L |
| Central | 1,085 | 8.6% | 95.02% | ₹9.54 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 58 | 93.10% | ₹3.58 L |
| Vasant Wardrobe | Key Account | Retail | 125 | 94.40% | ₹2.94 L |
| Rapid Bazaar | Key Account | Retail | 315 | 97.46% | ₹1.48 L |
| Ujjwal Water Board | Key Account | Bills | 31 | 100.00% | ₹85,239 |
| Yamuna Restaurant | Key Account | Food & Beverage | 99 | 98.99% | ₹83,974 |
| Urban Boutique | Key Account | Retail | 125 | 95.20% | ₹82,473 |
| Hampi Stores 2298 | Key Account | Retail | 127 | 95.28% | ₹76,333 |
| Girnar Connect | Key Account | Bills | 119 | 94.12% | ₹58,724 |

## Failure analysis

Of 558 declined attempts, 401 were business declines (3.166% of attempts — balances, PINs and limits), 96 technical (0.758%), 44 timeouts (0.347%) and 17 risk declines (0.134%).

163 attempts were re-presentations of an earlier failure (1.29% of the day); 71.8% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.382% | 1.522% |
| ZM | Invalid UPI PIN | business | Customer | 129 | 1.018% | 1.117% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.371% | 0.383% |
| U30 | Debit failed at remitter bank | technical | Issuer | 43 | 0.339% | 0.265% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.197% | 0.185% |
| U28 | Remitter bank unavailable | technical | Issuer | 23 | 0.182% | 0.178% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.166% | 0.261% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.134% | 0.094% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 60 | 40 |
| Auto-reversals | 21 | 24 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹80,844 | ₹92,515 |

## Customer behaviour

10,442 distinct customers transacted (+18.6% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,193 | 3,693 | 1.16 | 94.96% | ₹1,349 |
| power | 2,155 | 2,916 | 1.35 | 95.47% | ₹1,669 |
| merchant_heavy | 2,388 | 2,911 | 1.22 | 95.67% | ₹956 |
| small_ticket | 1,625 | 2,007 | 1.24 | 95.71% | ₹530 |
| occasional | 836 | 877 | 1.05 | 96.81% | ₹1,250 |
| new | 209 | 227 | 1.09 | 92.95% | ₹1,371 |
| dormant_returning | 36 | 36 | 1.00 | 100.00% | ₹850 |

## Operational events

- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

23 January ran on trend at 95.47% success and ₹1.51 Cr settled. The movement worth carrying forward is in merchant categories: category Food & Beverage carried 1,882 attempts, 28% up its trailing median and 24.2% of the day's volume. 10 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,667, successes=12,093, failed=558, pending=16, settled_value_inr=15,131,629.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Food & Beverage; attempts=1,882; own_median=1,474; z=7.75
- geography: region=West; attempts=3,117; own_median=2,510.5; z=5.72
- categories: mcc_category=Retail; attempts=3,530; own_median=2,601; z=3.82
- products: product_name=UPI Person to Merchant; attempts=3,789; own_median=2,960; z=4.05
- headline: attempts=12,667; trailing_median=10,429.5; z=2.74
- psps: payer_psp=PhonePe; attempts=6,022; own_median=4,916; z=2.84
- banks: payer_bank=State Bank of India; attempts=4,068; own_median=3,317.5; z=3.19
- geography: region=North; attempts=3,245; own_median=2,627.5; z=3.43
- geography: region=South; attempts=3,761; own_median=3,103.5; z=3.02
- psps: payer_psp=Google Pay; attempts=4,125; own_median=3,447.5; z=2.57

Refs: enterprise_data/warehouse/transactions, RPT-D18-DAILY, enterprise_data/warehouse/reference/incidents.parquet
