---
id: RPT-D118-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-02T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 02 May 2026)

**Report ID:** RPT-D118-DAILY · **Day 118 of 206** · **Derived from:** 17,447 transaction rows queried live from the warehouse

## Summary

The rail took **17,447 payment attempts** on Saturday 02 May 2026 (Weekend) and settled **₹2.49 Cr** across 16,797 successful payments. Volume was +18.2% on yesterday and +33.4% on the same weekday last week. Success closed at **96.27%**, above the trailing 28-day median of 95.42%.

Category Food & Beverage carried 2,846 attempts, 41% up its trailing median and 23.4% of the day's volume. Category Bills carried 1,758 attempts, 120% up its trailing median and 14.5% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 17,447 | +18.2% | +33.4% | 16,106 |
| Successful payments | 16,797 | +18.5% | +34.6% | 15,488 |
| Success rate | 96.27% | +0.24pp | +0.84pp | 96.15% |
| Settled value | ₹2.49 Cr | +47.8% | +57.4% | ₹2.09 Cr |
| Average ticket | ₹1,481 | +24.7% | +16.9% | ₹1,335 |
| Technical declines | 0.418% | +0.07pp | −0.06pp | 0.385% |
| Business declines | 2.711% | −0.36pp | −0.73pp | 2.890% |
| Risk declines | 0.160% | +0.03pp | +0.02pp | 0.148% |
| Timeout declines | 0.373% | +0.12pp | −0.05pp | 0.312% |
| Retry share | 1.15% | −0.46pp | −0.27pp | 1.38% |
| Latency p95 | 1,238 ms | +1.7% | +1.1% | 1,228 ms |
| Active customers | 13,773 | +14.8% | +26.0% | 12,885 |
| Active merchants | 1,588 | +8.2% | +13.8% | 1,528 |

## What moved

- Category Food & Beverage carried 2,846 attempts, 41% up its trailing median and 23.4% of the day's volume.
- Category Bills carried 1,758 attempts, 120% up its trailing median and 14.5% of the day's volume.
- Category Retail carried 4,491 attempts, 37% up its trailing median and 37.0% of the day's volume.
- Attempt volume ran 3.2 standard deviations up its trailing 28-day median at 17,447, 33.4% up on the same weekday last week.
- Product UPI Circle is compounding — attempts up 58% across the trailing window to 707 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Merchant carried 4,732 attempts, 43% up its trailing median and 27.1% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,303 | 30.4% | 95.53% | ₹59.06 L | +21.0% |
| UPI Person to Merchant | 4,732 | 27.1% | 96.13% | ₹51.24 L | +43.0% |
| UPI QR Payments | 3,278 | 18.8% | 96.55% | ₹14.89 L | +43.1% |
| UPI Lite | 2,018 | 11.6% | 99.06% | ₹1.97 L | +74.1% |
| UPI Circle | 707 | 4.1% | 96.75% | ₹6.47 L | +120.9% |
| RuPay Credit on UPI | 367 | 2.1% | 96.19% | ₹23.06 L | +11.9% |
| UPI AutoPay | 325 | 1.9% | 92.31% | ₹6.14 L | −0.5% |
| Credit on UPI | 272 | 1.6% | 95.59% | ₹29.56 L | +14.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,510 | 96.24% | 95.52% | ₹76.28 L | normal |
| HDFC Bank | 1,917 | 96.30% | 95.87% | ₹25.70 L | normal |
| Bank of Baroda | 1,359 | 95.88% | 95.62% | ₹20.45 L | normal |
| Union Bank of India | 1,207 | 96.35% | 94.95% | ₹19.18 L | normal |
| ICICI Bank | 1,096 | 96.53% | 96.26% | ₹18.04 L | normal |
| Axis Bank | 1,041 | 97.02% | 95.93% | ₹15.71 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,202 | 95.90% | 95.73% | ₹1.06 Cr | normal |
| Google Pay | 5,822 | 96.70% | 95.43% | ₹90.83 L | ⚠ outlier |
| Paytm | 1,398 | 96.49% | 95.27% | ₹18.28 L | normal |
| Navi | 642 | 97.04% | 96.03% | ₹11.70 L | normal |
| SuperMoney | 332 | 95.18% | 95.51% | ₹7.18 L | normal |
| BHIM | 172 | 96.51% | 95.70% | ₹3.25 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,491 | 96.59% | ₹46.70 L |
| Food & Beverage | 2,846 | 97.01% | ₹12.97 L |
| Bills | 1,758 | 96.47% | ₹20.14 L |
| Mobility | 1,455 | 97.32% | ₹8.91 L |
| Healthcare | 696 | 97.27% | ₹5.82 L |
| Digital | 361 | 94.74% | ₹2.49 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,192 | 29.8% | 96.21% | ₹71.45 L |
| North | 4,382 | 25.1% | 96.05% | ₹64.18 L |
| West | 4,254 | 24.4% | 96.66% | ₹69.48 L |
| East | 2,093 | 12.0% | 96.03% | ₹28.04 L |
| Central | 1,526 | 8.7% | 96.40% | ₹15.69 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 26 | 92.31% | ₹3.25 L |
| Rapid Bazaar | Key Account | Retail | 474 | 97.26% | ₹2.08 L |
| Ujjwal Water Board | Key Account | Bills | 96 | 98.96% | ₹1.84 L |
| Vasant Wardrobe | Key Account | Retail | 79 | 97.47% | ₹1.54 L |
| Hampi Stores 2298 | Key Account | Retail | 122 | 98.36% | ₹1.30 L |
| Girnar Connect | Key Account | Bills | 291 | 95.53% | ₹1.13 L |
| Urban Boutique | Key Account | Retail | 127 | 95.28% | ₹1.01 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 72 | 97.22% | ₹95,519 |

## Failure analysis

Of 639 declined attempts, 473 were business declines (2.711% of attempts — balances, PINs and limits), 73 technical (0.418%), 65 timeouts (0.373%) and 28 risk declines (0.160%).

200 attempts were re-presentations of an earlier failure (1.15% of the day); 47.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 180 | 1.032% | 1.313% |
| ZM | Invalid UPI PIN | business | Customer | 178 | 1.020% | 1.054% |
| XH | Account does not exist / frozen | business | Issuer | 42 | 0.241% | 0.211% |
| ZA | Transaction declined by customer | business | Customer | 42 | 0.241% | 0.384% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 35 | 0.201% | 0.203% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.166% | 0.212% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 24 | 0.138% | 0.112% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 20 | 0.115% | 0.108% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 99 | 84 |
| Auto-reversals | 57 | 29 |
| Disputes / chargebacks | 14 | 11 |
| Value returned | ₹3.98 L | ₹1.43 L |

## Customer behaviour

13,773 distinct customers transacted (+30.7% on the 28-day median) at 1.27 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,283 | 5,129 | 1.20 | 95.93% | ₹1,431 |
| power | 2,857 | 4,163 | 1.46 | 96.52% | ₹2,035 |
| merchant_heavy | 3,118 | 3,947 | 1.27 | 96.50% | ₹1,264 |
| small_ticket | 2,071 | 2,664 | 1.29 | 96.40% | ₹670 |
| occasional | 1,132 | 1,209 | 1.07 | 95.86% | ₹1,430 |
| new | 284 | 307 | 1.08 | 96.09% | ₹1,743 |
| dormant_returning | 28 | 28 | 1.00 | 100.00% | ₹1,195 |

## Operational events

- **INC-PSP-0029** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 57 auto-reversals were raised, 2.4 sigma above the trailing median of 29.

### Opportunities

- Product UPI Circle is compounding — attempts up 58% across the trailing window to 707 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 45% across the trailing window to 272 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

02 May was an incident day: INC-PSP-0029 was live and the rail closed at 96.27% success against a 95.42% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-02` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=17,447, successes=16,797, failed=639, pending=11, settled_value_inr=24,884,609.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Food & Beverage; attempts=2,846; own_median=2,021.5; z=5.59
- categories: mcc_category=Bills; attempts=1,758; own_median=798.5; z=6.41
- categories: mcc_category=Retail; attempts=4,491; own_median=3,287; z=3.98
- headline: attempts=17,447; trailing_median=12,742; z=3.22
- incidents: event_id=INC-PSP-0029; kind=psp_degradation; severity=Sev-2; window=2026-05-02 to 2026-05-04; success_impact_pp=-10.68; volume_impact_pct=-16.71
- products: product_name=UPI Circle; attempts=707; window_growth_pct=58.4; success_rate=96.75
- products: product_name=UPI Person to Merchant; attempts=4,732; own_median=3,310; z=4.18
- psps: payer_psp=PhonePe; attempts=8,202; own_median=6,048; z=2.85
- banks: payer_bank=State Bank of India; attempts=5,510; own_median=4,035.5; z=3.42
- adjustments: reversals=57; trailing_median=29; z=2.36

Refs: enterprise_data/warehouse/transactions, RPT-D117-DAILY, enterprise_data/warehouse/reference/incidents.parquet
