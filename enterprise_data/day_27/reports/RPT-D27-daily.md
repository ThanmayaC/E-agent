---
id: RPT-D27-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-31T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 31 Jan 2026)

**Report ID:** RPT-D27-DAILY · **Day 27 of 206** · **Derived from:** 11,765 transaction rows queried live from the warehouse

## Summary

The rail took **11,765 payment attempts** on Saturday 31 January 2026 (Weekend) and settled **₹1.26 Cr** across 11,284 successful payments. Volume was +12.6% on yesterday and −2.6% on the same weekday last week. Success closed at **95.91%**, above the trailing 28-day median of 95.21%.

Issuer State Bank of India ran at 96.34% success on 3,794 attempts (32.2% of the day), 1.42pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,765 | +12.6% | −2.6% | 10,312 |
| Successful payments | 11,284 | +12.5% | −2.3% | 9,817 |
| Success rate | 95.91% | −0.04pp | +0.29pp | 95.17% |
| Settled value | ₹1.26 Cr | −2.0% | −8.3% | ₹1.16 Cr |
| Average ticket | ₹1,116 | −12.9% | −6.1% | ₹1,183 |
| Technical declines | 0.416% | −0.01pp | −0.13pp | 0.597% |
| Business declines | 3.026% | −0.12pp | −0.18pp | 3.585% |
| Risk declines | 0.204% | +0.10pp | +0.06pp | 0.134% |
| Timeout declines | 0.280% | +0.02pp | −0.08pp | 0.379% |
| Retry share | 1.01% | −0.20pp | −0.28pp | 1.48% |
| Latency p95 | 1,215 ms | +1.0% | +4.3% | 1,245 ms |
| Active customers | 9,827 | +10.8% | −1.2% | 8,736 |
| Active merchants | 1,295 | +7.0% | +4.3% | 1,203 |

## What moved

- Issuer State Bank of India ran at 96.34% success on 3,794 attempts (32.2% of the day), 1.42pp up its own 28-day median.
- Region North ran at 96.50% success on 2,941 attempts (25.0% of the day), 1.34pp up its own 28-day median.
- Category Food & Beverage carried 1,789 attempts, 21% up its trailing median and 24.4% of the day's volume.
- Product UPI Person to Merchant ran at 96.59% success on 3,137 attempts (26.7% of the day), 0.84pp up its own 28-day median.
- Category Mobility carried 868 attempts, 35% up its trailing median and 11.8% of the day's volume.
- Category Bills carried 972 attempts, 51% up its trailing median and 13.2% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,420 | 37.6% | 95.54% | ₹48.85 L | +11.1% |
| UPI Person to Merchant | 3,137 | 26.7% | 96.59% | ₹28.80 L | +7.4% |
| UPI QR Payments | 2,105 | 17.9% | 95.72% | ₹8.51 L | +26.7% |
| UPI Lite | 1,018 | 8.7% | 99.02% | ₹96,317 | +55.9% |
| UPI AutoPay | 303 | 2.6% | 89.11% | ₹4.99 L | −0.3% |
| RuPay Credit on UPI | 205 | 1.7% | 96.59% | ₹8.18 L | +7.3% |
| Credit on UPI | 145 | 1.2% | 93.10% | ₹9.46 L | +10.3% |
| UPI Circle | 125 | 1.1% | 97.60% | ₹1.09 L | +35.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,794 | 96.34% | 94.92% | ₹40.01 L | ⚠ outlier |
| HDFC Bank | 1,292 | 96.05% | 95.90% | ₹12.83 L | normal |
| Bank of Baroda | 845 | 95.50% | 94.57% | ₹8.13 L | normal |
| Union Bank of India | 789 | 95.56% | 94.72% | ₹8.06 L | normal |
| Punjab National Bank | 695 | 95.68% | 94.76% | ₹6.77 L | normal |
| ICICI Bank | 693 | 96.54% | 96.00% | ₹7.79 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,470 | 95.63% | 95.09% | ₹57.45 L | normal |
| Google Pay | 3,868 | 96.15% | 95.30% | ₹41.53 L | normal |
| Paytm | 1,001 | 95.90% | 94.68% | ₹11.37 L | normal |
| Navi | 469 | 97.23% | 95.84% | ₹4.78 L | normal |
| SuperMoney | 239 | 96.65% | 95.40% | ₹4.07 L | normal |
| BHIM | 136 | 94.12% | 95.21% | ₹1.28 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,782 | 96.26% | ₹24.37 L |
| Food & Beverage | 1,789 | 96.93% | ₹8.23 L |
| Bills | 972 | 96.40% | ₹9.80 L |
| Mobility | 868 | 96.54% | ₹4.57 L |
| Healthcare | 329 | 97.87% | ₹2.91 L |
| Digital | 284 | 92.96% | ₹1.28 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,494 | 29.7% | 95.85% | ₹36.98 L |
| North | 2,941 | 25.0% | 96.50% | ₹30.82 L |
| West | 2,886 | 24.5% | 95.46% | ₹33.98 L |
| East | 1,424 | 12.1% | 96.07% | ₹15.88 L |
| Central | 1,020 | 8.7% | 95.49% | ₹8.27 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 58 | 96.55% | ₹1.90 L |
| Ujjwal Water Board | Key Account | Bills | 56 | 98.21% | ₹1.11 L |
| Rapid Bazaar | Key Account | Retail | 311 | 96.14% | ₹1.10 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 83 | 96.39% | ₹1.09 L |
| Hampi Stores 2298 | Key Account | Retail | 83 | 96.39% | ₹82,519 |
| Girnar Connect | Key Account | Bills | 167 | 96.41% | ₹59,775 |
| Vega Electronics | Large | Retail | 24 | 87.50% | ₹52,421 |
| Aravalli Pharmacy | Large | Healthcare | 68 | 94.12% | ₹47,099 |

## Failure analysis

Of 462 declined attempts, 356 were business declines (3.026% of attempts — balances, PINs and limits), 49 technical (0.416%), 33 timeouts (0.280%) and 24 risk declines (0.204%).

119 attempts were re-presentations of an earlier failure (1.01% of the day); 59.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 138 | 1.173% | 1.522% |
| ZM | Invalid UPI PIN | business | Customer | 121 | 1.028% | 1.117% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.365% | 0.405% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.221% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.204% | 0.261% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.178% | 0.111% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.144% | 0.185% |
| UX | Mandate execution outside permitted window | business | PSP | 14 | 0.119% | 0.093% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 71 | 60 |
| Auto-reversals | 16 | 22 |
| Disputes / chargebacks | 3 | 2 |
| Value returned | ₹63,040 | ₹93,909 |

## Customer behaviour

9,827 distinct customers transacted (+11.6% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,092 | 3,521 | 1.14 | 96.93% | ₹1,128 |
| power | 2,058 | 2,734 | 1.33 | 95.50% | ₹1,393 |
| merchant_heavy | 2,228 | 2,703 | 1.21 | 95.30% | ₹953 |
| small_ticket | 1,452 | 1,757 | 1.21 | 96.07% | ₹540 |
| occasional | 775 | 815 | 1.05 | 94.60% | ₹1,317 |
| new | 193 | 205 | 1.06 | 95.61% | ₹778 |
| dormant_returning | 29 | 30 | 1.03 | 96.67% | ₹1,803 |

## Operational events

- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 31 January: success came in 0.70pp above baseline at 95.91% on 11,765 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-31` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,765, successes=11,284, failed=462, pending=19, settled_value_inr=12,593,088.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- banks: payer_bank=State Bank of India; attempts=3,794; success_rate=96.34; own_median=94.92; z=2.38
- geography: region=North; attempts=2,941; success_rate=96.5; own_median=95.16; z=2.57
- categories: mcc_category=Food & Beverage; attempts=1,789; own_median=1,474; z=3.12
- products: product_name=UPI Person to Merchant; attempts=3,137; success_rate=96.59; own_median=95.75; z=2.15
- categories: mcc_category=Mobility; attempts=868; own_median=643.5; z=3.83
- categories: mcc_category=Bills; attempts=972; own_median=644.5; z=3.51
- products: product_name=UPI Lite; attempts=1,018; own_median=653; z=3.91
- geography: region=West; attempts=2,886; own_median=2,510.5; z=2.3
- psps: payer_psp=Navi; attempts=469; own_median=367; z=4.17
- banks: payer_bank=Kotak Mahindra Bank; attempts=471; own_median=363; z=2.97

Refs: enterprise_data/warehouse/transactions, RPT-D26-DAILY, enterprise_data/warehouse/reference/incidents.parquet
