---
id: RPT-D20-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 24 Jan 2026)

**Report ID:** RPT-D20-DAILY · **Day 20 of 206** · **Derived from:** 12,084 transaction rows queried live from the warehouse

## Summary

The rail took **12,084 payment attempts** on Saturday 24 January 2026 (Weekend) and settled **₹1.37 Cr** across 11,555 successful payments. Volume was −4.6% on yesterday and +5.6% on the same weekday last week. Success closed at **95.62%**, above the trailing 28-day median of 95.35%.

5 disputes were raised, 4.1 sigma above the trailing median of 0. Category Food & Beverage carried 1,926 attempts, 30% up its trailing median and 25.4% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,084 | −4.6% | +5.6% | 10,481 |
| Successful payments | 11,555 | −4.4% | +6.2% | 9,976 |
| Success rate | 95.62% | +0.15pp | +0.49pp | 95.15% |
| Settled value | ₹1.37 Cr | −9.3% | +12.8% | ₹1.19 Cr |
| Average ticket | ₹1,188 | −5.0% | +6.2% | ₹1,188 |
| Technical declines | 0.546% | −0.21pp | −0.26pp | 0.633% |
| Business declines | 3.203% | +0.04pp | −0.24pp | 3.561% |
| Risk declines | 0.141% | +0.01pp | +0.03pp | 0.131% |
| Timeout declines | 0.356% | +0.01pp | −0.05pp | 0.393% |
| Retry share | 1.29% | +0.00pp | −0.09pp | 1.48% |
| Latency p95 | 1,165 ms | −5.7% | −2.9% | 1,243 ms |
| Active customers | 9,942 | −4.8% | +3.6% | 8,857 |
| Active merchants | 1,242 | −4.0% | −0.8% | 1,206 |

## What moved

- Category Food & Beverage carried 1,926 attempts, 30% up its trailing median and 25.4% of the day's volume.
- Product UPI Person to Merchant carried 3,770 attempts, 26% up its trailing median and 31.2% of the day's volume.
- Region West carried 2,935 attempts, 17% up its trailing median and 24.3% of the day's volume.
- Region West ran at 95.74% success on 2,935 attempts (24.3% of the day), 0.69pp up its own 28-day median.
- Category Bills ran at 94.06% success on 724 attempts (9.5% of the day), 1.77pp down its own 28-day median.
- Category Mobility carried 815 attempts, 25% up its trailing median and 10.7% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,488 | 37.1% | 95.41% | ₹44.54 L | +11.8% |
| UPI Person to Merchant | 3,770 | 31.2% | 96.13% | ₹44.31 L | +25.8% |
| UPI QR Payments | 2,050 | 17.0% | 96.34% | ₹9.32 L | +22.5% |
| UPI Lite | 918 | 7.6% | 98.37% | ₹87,175 | +43.2% |
| UPI AutoPay | 317 | 2.6% | 84.23% | ₹4.83 L | +4.3% |
| UPI Circle | 119 | 1.0% | 97.48% | ₹1.24 L | +29.3% |
| RuPay Credit on UPI | 100 | 0.8% | 100.00% | ₹8.04 L | −48.7% |
| UPI Lite Auto Top-Up | 80 | 0.7% | 92.50% | ₹76,837 | −4.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,838 | 95.83% | 94.91% | ₹47.77 L | normal |
| HDFC Bank | 1,337 | 96.34% | 95.89% | ₹16.32 L | normal |
| Bank of Baroda | 931 | 94.20% | 94.72% | ₹10.29 L | normal |
| Union Bank of India | 853 | 94.02% | 94.72% | ₹7.44 L | normal |
| ICICI Bank | 767 | 96.09% | 95.92% | ₹9.27 L | normal |
| Axis Bank | 762 | 95.28% | 95.39% | ₹7.90 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,688 | 95.62% | 95.09% | ₹61.42 L | normal |
| Google Pay | 4,005 | 95.66% | 95.24% | ₹50.01 L | normal |
| Paytm | 952 | 96.11% | 94.54% | ₹9.74 L | ⚠ outlier |
| Navi | 450 | 95.56% | 95.56% | ₹3.67 L | normal |
| SuperMoney | 238 | 94.96% | 95.49% | ₹2.20 L | normal |
| FamApp | 116 | 96.55% | 95.70% | ₹77,652 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,199 | 96.06% | ₹36.89 L |
| Food & Beverage | 1,926 | 96.68% | ₹9.36 L |
| Mobility | 815 | 97.18% | ₹4.10 L |
| Bills | 724 | 94.06% | ₹8.03 L |
| Healthcare | 403 | 98.76% | ₹7.38 L |
| Digital | 222 | 90.09% | ₹1.38 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,522 | 29.1% | 95.32% | ₹39.49 L |
| North | 3,061 | 25.3% | 95.88% | ₹32.21 L |
| West | 2,935 | 24.3% | 95.74% | ₹33.80 L |
| East | 1,496 | 12.4% | 95.92% | ₹19.32 L |
| Central | 1,070 | 8.9% | 95.14% | ₹12.47 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 46 | 89.13% | ₹2.37 L |
| Vasant Wardrobe | Key Account | Retail | 82 | 93.90% | ₹1.62 L |
| Rapid Bazaar | Key Account | Retail | 342 | 97.95% | ₹1.55 L |
| Ujjwal Water Board | Key Account | Bills | 45 | 97.78% | ₹72,062 |
| Girnar Connect | Key Account | Bills | 125 | 96.80% | ₹64,929 |
| Yamuna Restaurant | Key Account | Food & Beverage | 80 | 98.75% | ₹58,820 |
| Aravalli Pharmacy | Large | Healthcare | 72 | 100.00% | ₹56,604 |
| Hampi Stores 2298 | Key Account | Retail | 96 | 96.88% | ₹51,554 |

## Failure analysis

Of 513 declined attempts, 387 were business declines (3.203% of attempts — balances, PINs and limits), 66 technical (0.546%), 43 timeouts (0.356%) and 17 risk declines (0.141%).

156 attempts were re-presentations of an earlier failure (1.29% of the day); 70.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 168 | 1.390% | 1.503% |
| ZM | Invalid UPI PIN | business | Customer | 112 | 0.927% | 1.103% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.455% | 0.382% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.232% | 0.267% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.199% | 0.260% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.166% | 0.185% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.141% | 0.182% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.132% | 0.140% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 60 | 41 |
| Auto-reversals | 26 | 23 |
| Disputes / chargebacks | 5 | 0 |
| Value returned | ₹1.12 L | ₹85,277 |

## Customer behaviour

9,942 distinct customers transacted (+12.6% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,078 | 3,525 | 1.15 | 95.94% | ₹1,089 |
| power | 2,069 | 2,832 | 1.37 | 95.87% | ₹1,880 |
| merchant_heavy | 2,251 | 2,736 | 1.22 | 95.32% | ₹898 |
| small_ticket | 1,487 | 1,860 | 1.25 | 95.54% | ₹459 |
| occasional | 834 | 884 | 1.06 | 95.25% | ₹1,219 |
| new | 195 | 218 | 1.12 | 92.66% | ₹716 |
| dormant_returning | 28 | 29 | 1.04 | 100.00% | ₹717 |

## Operational events

- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.

## Risks and opportunities

### Risks

- 5 disputes were raised, 4.1 sigma above the trailing median of 0.
- Category Bills ran at 94.06% success on 724 attempts (9.5% of the day), 1.77pp down its own 28-day median.
- Product UPI AutoPay ran at 84.23% success on 317 attempts (2.6% of the day), 5.09pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

24 January ran on trend at 95.62% success and ₹1.37 Cr settled. The movement worth carrying forward is in money moving back: 5 disputes were raised, 4.1 sigma above the trailing median of 0. 3 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,084, successes=11,555, failed=513, pending=16, settled_value_inr=13,729,200.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=5; trailing_median=0; z=4.05
- categories: mcc_category=Food & Beverage; attempts=1,926; own_median=1,478; z=6.71
- products: product_name=UPI Person to Merchant; attempts=3,770; own_median=2,996; z=3.3
- geography: region=West; attempts=2,935; own_median=2,515; z=3.68
- geography: region=West; attempts=2,935; success_rate=95.74; own_median=95.05; z=2.01
- categories: mcc_category=Bills; attempts=724; success_rate=94.06; own_median=95.83; z=-2.97
- categories: mcc_category=Mobility; attempts=815; own_median=652; z=3.55
- products: product_name=UPI Lite; attempts=918; own_median=641; z=3.59
- incidents: event_id=MAINT-0084; kind=maintenance_window; severity=Sev-3; window=2026-01-24 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- geography: region=East; attempts=1,496; own_median=1,237; z=2.33

Refs: enterprise_data/warehouse/transactions, RPT-D19-DAILY, enterprise_data/warehouse/reference/incidents.parquet
