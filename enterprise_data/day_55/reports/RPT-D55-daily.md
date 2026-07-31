---
id: RPT-D55-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 28 Feb 2026)

**Report ID:** RPT-D55-DAILY · **Day 55 of 206** · **Derived from:** 13,627 transaction rows queried live from the warehouse

## Summary

The rail took **13,627 payment attempts** on Saturday 28 February 2026 (Weekend) and settled **₹1.54 Cr** across 13,015 successful payments. Volume was +7.8% on yesterday and +14.5% on the same weekday last week. Success closed at **95.51%**, in line with the trailing 28-day median of 95.54%.

Attempt volume ran 4.2 standard deviations up its trailing 28-day median at 13,627, 14.5% up on the same weekday last week. Category Bills carried 1,249 attempts, 88% up its trailing median and 14.4% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,627 | +7.8% | +14.5% | 10,844 |
| Successful payments | 13,015 | +7.8% | +14.4% | 10,340 |
| Success rate | 95.51% | −0.05pp | −0.02pp | 95.31% |
| Settled value | ₹1.54 Cr | +5.9% | +16.6% | ₹1.23 Cr |
| Average ticket | ₹1,185 | −1.7% | +1.9% | ₹1,187 |
| Technical declines | 0.477% | −0.01pp | +0.12pp | 0.435% |
| Business declines | 3.508% | +0.16pp | −0.00pp | 3.631% |
| Risk declines | 0.088% | −0.02pp | −0.06pp | 0.125% |
| Timeout declines | 0.308% | −0.07pp | −0.04pp | 0.383% |
| Retry share | 1.36% | +0.00pp | +0.06pp | 1.47% |
| Latency p95 | 1,204 ms | −3.6% | −1.1% | 1,280 ms |
| Active customers | 11,123 | +6.4% | +11.8% | 9,158 |
| Active merchants | 1,369 | +4.3% | +6.0% | 1,258 |

## What moved

- Attempt volume ran 4.2 standard deviations up its trailing 28-day median at 13,627, 14.5% up on the same weekday last week.
- Category Bills carried 1,249 attempts, 88% up its trailing median and 14.4% of the day's volume.
- App Google Pay carried 4,448 attempts, 29% up its trailing median and 32.6% of the day's volume.
- App PhonePe carried 6,450 attempts, 30% up its trailing median and 47.3% of the day's volume.
- Product UPI Person to Merchant carried 4,389 attempts, 40% up its trailing median and 32.2% of the day's volume.
- Category Retail carried 3,453 attempts, 27% up its trailing median and 39.7% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,932 | 36.2% | 95.03% | ₹54.40 L | +26.1% |
| UPI Person to Merchant | 4,389 | 32.2% | 95.97% | ₹44.34 L | +40.3% |
| UPI QR Payments | 2,295 | 16.8% | 96.30% | ₹9.25 L | +28.8% |
| UPI Lite | 907 | 6.7% | 98.02% | ₹84,105 | +25.4% |
| UPI AutoPay | 335 | 2.5% | 87.76% | ₹5.34 L | +12.0% |
| RuPay Credit on UPI | 178 | 1.3% | 96.07% | ₹11.78 L | −15.4% |
| UPI Circle | 147 | 1.1% | 97.96% | ₹1.41 L | +40.7% |
| Credit on UPI | 125 | 0.9% | 95.20% | ₹10.25 L | −14.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,430 | 95.26% | 95.64% | ₹54.54 L | normal |
| HDFC Bank | 1,456 | 96.63% | 96.07% | ₹15.20 L | normal |
| Bank of Baroda | 1,111 | 94.96% | 95.40% | ₹14.03 L | normal |
| Union Bank of India | 910 | 94.40% | 95.44% | ₹8.80 L | normal |
| Axis Bank | 817 | 96.33% | 95.47% | ₹9.43 L | normal |
| Punjab National Bank | 815 | 94.85% | 94.62% | ₹7.89 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,450 | 95.66% | 95.54% | ₹76.55 L | normal |
| Google Pay | 4,448 | 95.10% | 95.61% | ₹49.83 L | normal |
| Paytm | 1,120 | 95.36% | 95.48% | ₹9.72 L | normal |
| Navi | 520 | 96.15% | 95.15% | ₹6.56 L | normal |
| SuperMoney | 263 | 96.96% | 96.18% | ₹2.20 L | normal |
| FamApp | 136 | 96.32% | 96.86% | ₹1.48 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,453 | 95.66% | ₹36.27 L |
| Food & Beverage | 2,058 | 97.04% | ₹9.00 L |
| Bills | 1,249 | 95.44% | ₹16.76 L |
| Mobility | 844 | 96.21% | ₹4.62 L |
| Healthcare | 428 | 98.13% | ₹4.84 L |
| Digital | 317 | 93.06% | ₹1.77 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,027 | 29.6% | 95.90% | ₹49.17 L |
| North | 3,487 | 25.6% | 95.38% | ₹36.24 L |
| West | 3,236 | 23.7% | 95.40% | ₹34.45 L |
| East | 1,637 | 12.0% | 95.60% | ₹21.51 L |
| Central | 1,240 | 9.1% | 94.76% | ₹12.85 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 85 | 96.47% | ₹2.14 L |
| Vasant Wardrobe | Key Account | Retail | 66 | 95.45% | ₹2.02 L |
| Rapid Bazaar | Key Account | Retail | 375 | 96.00% | ₹1.42 L |
| Vega Electronics | Large | Retail | 25 | 92.00% | ₹1.16 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 86 | 94.19% | ₹93,402 |
| Urban Boutique | Key Account | Retail | 98 | 97.96% | ₹88,515 |
| Girnar Connect | Key Account | Bills | 209 | 95.69% | ₹78,106 |
| Hampi Stores 2298 | Key Account | Retail | 108 | 94.44% | ₹76,195 |

## Failure analysis

Of 597 declined attempts, 478 were business declines (3.508% of attempts — balances, PINs and limits), 65 technical (0.477%), 42 timeouts (0.308%) and 12 risk declines (0.088%).

185 attempts were re-presentations of an earlier failure (1.36% of the day); 70.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 216 | 1.585% | 1.479% |
| ZM | Invalid UPI PIN | business | Customer | 148 | 1.086% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.389% | 0.431% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.250% | 0.239% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.213% | 0.168% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.161% | 0.150% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.125% | 0.114% |
| UX | Mandate execution outside permitted window | business | PSP | 15 | 0.110% | 0.109% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 78 | 69 |
| Auto-reversals | 29 | 17 |
| Disputes / chargebacks | 6 | 6 |
| Value returned | ₹1.21 L | ₹96,246 |

## Customer behaviour

11,123 distinct customers transacted (+25.4% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,432 | 3,966 | 1.16 | 95.97% | ₹1,313 |
| power | 2,306 | 3,200 | 1.39 | 95.50% | ₹1,487 |
| merchant_heavy | 2,469 | 3,058 | 1.24 | 95.13% | ₹875 |
| small_ticket | 1,704 | 2,125 | 1.25 | 95.11% | ₹480 |
| occasional | 929 | 973 | 1.05 | 96.40% | ₹1,587 |
| new | 249 | 271 | 1.09 | 94.46% | ₹739 |
| dormant_returning | 34 | 34 | 1.00 | 85.29% | ₹588 |

## Operational events

- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- 29 auto-reversals were raised, 3.2 sigma above the trailing median of 17.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

28 February ran on trend at 95.51% success and ₹1.54 Cr settled. The movement worth carrying forward is in the headline numbers: attempt volume ran 4.2 standard deviations up its trailing 28-day median at 13,627, 14.5% up on the same weekday last week. 14 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,627, successes=13,015, failed=597, pending=15, settled_value_inr=15,421,813.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: attempts=13,627; trailing_median=10,454; z=4.18
- categories: mcc_category=Bills; attempts=1,249; own_median=665.5; z=6.97
- adjustments: reversals=29; trailing_median=17; z=3.24
- psps: payer_psp=Google Pay; attempts=4,448; own_median=3,457.5; z=4.11
- psps: payer_psp=PhonePe; attempts=6,450; own_median=4,951; z=3.4
- products: product_name=UPI Person to Merchant; attempts=4,389; own_median=3,129; z=3.99
- categories: mcc_category=Retail; attempts=3,453; own_median=2,714; z=3.5
- banks: payer_bank=State Bank of India; attempts=4,430; own_median=3,383; z=3.64
- geography: region=North; attempts=3,487; own_median=2,664; z=3.35
- geography: region=West; attempts=3,236; own_median=2,572; z=3.33

Refs: enterprise_data/warehouse/transactions, RPT-D54-DAILY, enterprise_data/warehouse/reference/incidents.parquet
