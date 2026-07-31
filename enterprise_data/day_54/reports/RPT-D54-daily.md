---
id: RPT-D54-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 27 Feb 2026)

**Report ID:** RPT-D54-DAILY · **Day 54 of 206** · **Derived from:** 12,636 transaction rows queried live from the warehouse

## Summary

The rail took **12,636 payment attempts** on Friday 27 February 2026 (Working day) and settled **₹1.46 Cr** across 12,075 successful payments. Volume was +26.0% on yesterday and +15.6% on the same weekday last week. Success closed at **95.56%**, in line with the trailing 28-day median of 95.54%.

28 auto-reversals were raised, 3.0 sigma above the trailing median of 17. Attempt volume ran 3.1 standard deviations up its trailing 28-day median at 12,636, 15.6% up on the same weekday last week.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,636 | +26.0% | +15.6% | 10,741 |
| Successful payments | 12,075 | +27.1% | +15.5% | 10,241 |
| Success rate | 95.56% | +0.82pp | −0.06pp | 95.31% |
| Settled value | ₹1.46 Cr | +21.9% | +15.8% | ₹1.22 Cr |
| Average ticket | ₹1,206 | −4.1% | +0.2% | ₹1,188 |
| Technical declines | 0.491% | −0.01pp | +0.04pp | 0.433% |
| Business declines | 3.348% | −0.92pp | −0.07pp | 3.636% |
| Risk declines | 0.111% | +0.09pp | −0.01pp | 0.126% |
| Timeout declines | 0.380% | +0.00pp | +0.04pp | 0.385% |
| Retry share | 1.35% | −0.38pp | +0.01pp | 1.47% |
| Latency p95 | 1,248 ms | −5.8% | −2.3% | 1,282 ms |
| Active customers | 10,452 | +21.0% | +13.0% | 9,085 |
| Active merchants | 1,313 | +4.2% | +2.8% | 1,254 |

## What moved

- Attempt volume ran 3.1 standard deviations up its trailing 28-day median at 12,636, 15.6% up on the same weekday last week.
- Issuer State Bank of India carried 4,115 attempts, 23% up its trailing median and 32.6% of the day's volume.
- Category Bills carried 1,094 attempts, 64% up its trailing median and 14.4% of the day's volume.
- App PhonePe carried 6,008 attempts, 22% up its trailing median and 47.5% of the day's volume.
- Product UPI Person to Person carried 5,033 attempts, 29% up its trailing median and 39.8% of the day's volume.
- App Google Pay carried 4,066 attempts, 18% up its trailing median and 32.2% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,033 | 39.8% | 95.29% | ₹53.76 L | +28.7% |
| UPI Person to Merchant | 3,599 | 28.5% | 96.25% | ₹37.18 L | +15.7% |
| UPI QR Payments | 2,049 | 16.2% | 96.49% | ₹9.44 L | +15.0% |
| UPI Lite | 749 | 5.9% | 99.47% | ₹68,516 | +3.7% |
| UPI AutoPay | 298 | 2.4% | 84.56% | ₹5.08 L | −0.7% |
| RuPay Credit on UPI | 265 | 2.1% | 93.58% | ₹14.82 L | +27.7% |
| Credit on UPI | 162 | 1.3% | 94.44% | ₹10.95 L | +11.0% |
| UPI Circle | 115 | 0.9% | 97.39% | ₹92,796 | +12.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,115 | 95.60% | 95.64% | ₹49.71 L | normal |
| HDFC Bank | 1,341 | 95.82% | 96.15% | ₹15.23 L | normal |
| Bank of Baroda | 960 | 95.42% | 95.45% | ₹11.12 L | normal |
| Union Bank of India | 862 | 95.48% | 95.39% | ₹8.87 L | normal |
| Punjab National Bank | 763 | 95.15% | 94.62% | ₹9.95 L | normal |
| Axis Bank | 736 | 95.65% | 95.47% | ₹9.48 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,008 | 95.79% | 95.54% | ₹72.01 L | normal |
| Google Pay | 4,066 | 95.67% | 95.61% | ₹45.06 L | normal |
| Paytm | 1,079 | 95.46% | 95.54% | ₹10.55 L | normal |
| Navi | 471 | 94.69% | 95.33% | ₹7.41 L | normal |
| SuperMoney | 243 | 93.83% | 96.18% | ₹2.26 L | ⚠ outlier |
| FamApp | 129 | 95.35% | 96.86% | ₹1.38 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,986 | 96.08% | ₹35.43 L |
| Food & Beverage | 1,730 | 97.11% | ₹8.97 L |
| Bills | 1,094 | 96.25% | ₹12.86 L |
| Mobility | 811 | 97.04% | ₹5.17 L |
| Healthcare | 364 | 96.15% | ₹4.27 L |
| Digital | 268 | 90.30% | ₹1.37 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,735 | 29.6% | 95.42% | ₹41.68 L |
| North | 3,178 | 25.2% | 96.07% | ₹35.95 L |
| West | 3,106 | 24.6% | 95.11% | ₹34.38 L |
| East | 1,526 | 12.1% | 95.94% | ₹20.94 L |
| Central | 1,091 | 8.6% | 95.33% | ₹12.68 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 22 | 100.00% | ₹1.77 L |
| Rapid Bazaar | Key Account | Retail | 304 | 97.70% | ₹1.39 L |
| Ujjwal Water Board | Key Account | Bills | 59 | 96.61% | ₹1.15 L |
| Vasant Wardrobe | Key Account | Retail | 50 | 94.00% | ₹1.02 L |
| Girnar Connect | Key Account | Bills | 176 | 96.59% | ₹82,053 |
| Yamuna Restaurant | Key Account | Food & Beverage | 82 | 97.56% | ₹74,354 |
| Urban Boutique | Key Account | Retail | 93 | 95.70% | ₹56,389 |
| Hampi Stores 2298 | Key Account | Retail | 102 | 91.18% | ₹54,497 |

## Failure analysis

Of 547 declined attempts, 423 were business declines (3.348% of attempts — balances, PINs and limits), 62 technical (0.491%), 48 timeouts (0.380%) and 14 risk declines (0.111%).

171 attempts were re-presentations of an earlier failure (1.35% of the day); 73.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.488% | 1.466% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 1.076% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.356% | 0.431% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 27 | 0.214% | 0.147% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.214% | 0.240% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.206% | 0.168% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.142% | 0.114% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.119% | 0.105% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 69 | 70 |
| Auto-reversals | 28 | 17 |
| Disputes / chargebacks | 7 | 6 |
| Value returned | ₹89,175 | ₹96,246 |

## Customer behaviour

10,452 distinct customers transacted (+18.0% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,234 | 3,727 | 1.15 | 95.49% | ₹1,350 |
| power | 2,184 | 2,978 | 1.36 | 95.03% | ₹1,597 |
| merchant_heavy | 2,407 | 2,864 | 1.19 | 95.64% | ₹864 |
| small_ticket | 1,541 | 1,906 | 1.24 | 95.91% | ₹437 |
| occasional | 860 | 915 | 1.06 | 96.61% | ₹1,460 |
| new | 197 | 215 | 1.09 | 95.81% | ₹496 |
| dormant_returning | 29 | 31 | 1.07 | 93.55% | ₹778 |

## Operational events

- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- 28 auto-reversals were raised, 3.0 sigma above the trailing median of 17.
- Category Financial Services ran at 79.38% success on 160 attempts (2.1% of the day), 7.06pp down its own 28-day median.
- Product UPI Lite Auto Top-Up ran at 93.33% success on 90 attempts (0.7% of the day), 4.25pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

27 February ran on trend at 95.56% success and ₹1.46 Cr settled. The movement worth carrying forward is in money moving back: 28 auto-reversals were raised, 3.0 sigma above the trailing median of 17. 8 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,636, successes=12,075, failed=547, pending=14, settled_value_inr=14,561,699.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: reversals=28; trailing_median=17; z=2.97
- headline: attempts=12,636; trailing_median=10,436; z=3.07
- banks: payer_bank=State Bank of India; attempts=4,115; own_median=3,332; z=3.43
- categories: mcc_category=Bills; attempts=1,094; own_median=665.5; z=5.12
- psps: payer_psp=PhonePe; attempts=6,008; own_median=4,923.5; z=2.66
- products: product_name=UPI Person to Person; attempts=5,033; own_median=3,912; z=2.77
- psps: payer_psp=Google Pay; attempts=4,066; own_median=3,437.5; z=3
- geography: region=West; attempts=3,106; own_median=2,567; z=2.91
- geography: region=South; attempts=3,735; own_median=3,086; z=2.53
- geography: region=North; attempts=3,178; own_median=2,664; z=2.22

Refs: enterprise_data/warehouse/transactions, RPT-D53-DAILY, enterprise_data/warehouse/reference/incidents.parquet
