---
id: RPT-D56-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-01T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 01 Mar 2026)

**Report ID:** RPT-D56-DAILY · **Day 56 of 206** · **Derived from:** 15,034 transaction rows queried live from the warehouse

## Summary

The rail took **15,034 payment attempts** on Sunday 01 March 2026 (Weekend) and settled **₹1.55 Cr** across 14,414 successful payments. Volume was +10.3% on yesterday and +64.1% on the same weekday last week. Success closed at **95.88%**, above the trailing 28-day median of 95.52%.

Attempt volume ran 6.0 standard deviations up its trailing 28-day median at 15,034, 64.1% up on the same weekday last week. App Google Pay carried 5,066 attempts, 47% up its trailing median and 33.7% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,034 | +10.3% | +64.1% | 15,034 |
| Successful payments | 14,414 | +10.7% | +65.9% | 14,414 |
| Success rate | 95.88% | +0.37pp | +1.04pp | 95.88% |
| Settled value | ₹1.55 Cr | +0.5% | +66.2% | ₹1.55 Cr |
| Average ticket | ₹1,076 | −9.2% | +0.2% | ₹1,076 |
| Technical declines | 0.333% | −0.14pp | +0.01pp | 0.333% |
| Business declines | 3.379% | −0.13pp | −1.00pp | 3.379% |
| Risk declines | 0.093% | +0.01pp | −0.03pp | 0.093% |
| Timeout declines | 0.239% | −0.07pp | +0.02pp | 0.239% |
| Retry share | 1.26% | −0.10pp | −0.12pp | 1.26% |
| Latency p95 | 1,213 ms | +0.7% | −2.3% | 1,213 ms |
| Active customers | 12,045 | +8.3% | +51.7% | 12,045 |
| Active merchants | 1,359 | −0.7% | +13.8% | 1,359 |

## What moved

- Attempt volume ran 6.0 standard deviations up its trailing 28-day median at 15,034, 64.1% up on the same weekday last week.
- App Google Pay carried 5,066 attempts, 47% up its trailing median and 33.7% of the day's volume.
- Category Bills carried 1,381 attempts, 108% up its trailing median and 15.1% of the day's volume.
- App PhonePe carried 7,033 attempts, 42% up its trailing median and 46.8% of the day's volume.
- Product UPI Person to Person carried 5,896 attempts, 51% up its trailing median and 39.2% of the day's volume.
- Issuer State Bank of India carried 4,816 attempts, 42% up its trailing median and 32.0% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,896 | 39.2% | 95.59% | ₹64.66 L | +50.7% |
| UPI Person to Merchant | 4,503 | 30.0% | 95.98% | ₹40.29 L | +43.9% |
| UPI QR Payments | 2,537 | 16.9% | 96.26% | ₹10.65 L | +42.4% |
| UPI Lite | 1,079 | 7.2% | 98.89% | ₹98,725 | +49.2% |
| UPI AutoPay | 318 | 2.1% | 89.62% | ₹5.21 L | +6.4% |
| UPI Circle | 197 | 1.3% | 96.45% | ₹1.92 L | +88.5% |
| RuPay Credit on UPI | 141 | 0.9% | 97.87% | ₹12.31 L | −33.0% |
| Credit on UPI | 94 | 0.6% | 92.55% | ₹5.71 L | −35.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,816 | 95.47% | 95.62% | ₹49.18 L | normal |
| HDFC Bank | 1,589 | 97.23% | 96.15% | ₹14.94 L | normal |
| Bank of Baroda | 1,150 | 95.65% | 95.38% | ₹9.28 L | normal |
| Union Bank of India | 1,022 | 94.81% | 95.39% | ₹7.34 L | normal |
| Punjab National Bank | 932 | 96.57% | 94.62% | ₹16.44 L | normal |
| Axis Bank | 897 | 95.54% | 95.61% | ₹8.75 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,033 | 95.78% | 95.54% | ₹69.26 L | normal |
| Google Pay | 5,066 | 95.82% | 95.59% | ₹52.98 L | normal |
| Paytm | 1,250 | 95.60% | 95.41% | ₹12.46 L | normal |
| Navi | 555 | 97.30% | 95.15% | ₹5.10 L | ⚠ outlier |
| SuperMoney | 274 | 97.08% | 96.18% | ₹6.67 L | normal |
| BHIM | 144 | 97.92% | 94.88% | ₹1.09 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,643 | 96.43% | ₹31.03 L |
| Food & Beverage | 2,177 | 96.51% | ₹8.12 L |
| Bills | 1,381 | 95.29% | ₹14.34 L |
| Mobility | 914 | 96.72% | ₹4.76 L |
| Healthcare | 399 | 96.24% | ₹2.90 L |
| Digital | 311 | 95.50% | ₹1.52 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,478 | 29.8% | 95.91% | ₹41.38 L |
| North | 3,776 | 25.1% | 96.11% | ₹36.74 L |
| West | 3,665 | 24.4% | 95.83% | ₹41.82 L |
| East | 1,802 | 12.0% | 95.12% | ₹22.07 L |
| Central | 1,313 | 8.7% | 96.27% | ₹13.03 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 407 | 96.81% | ₹1.65 L |
| Ujjwal Water Board | Key Account | Bills | 90 | 93.33% | ₹1.35 L |
| Vega Electronics | Large | Retail | 22 | 90.91% | ₹1.34 L |
| Swift Mart 1738 | Key Account | Retail | 126 | 99.21% | ₹88,492 |
| Hampi Stores 2298 | Key Account | Retail | 102 | 95.10% | ₹84,943 |
| Girnar Connect | Key Account | Bills | 208 | 95.19% | ₹80,519 |
| Vasant Wardrobe | Key Account | Retail | 70 | 92.86% | ₹78,063 |
| Aravalli Pharmacy | Large | Healthcare | 80 | 95.00% | ₹56,821 |

## Failure analysis

Of 608 declined attempts, 508 were business declines (3.379% of attempts — balances, PINs and limits), 50 technical (0.333%), 36 timeouts (0.239%) and 14 risk declines (0.093%).

189 attempts were re-presentations of an earlier failure (1.26% of the day); 66.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 214 | 1.423% | 1.484% |
| ZM | Invalid UPI PIN | business | Customer | 166 | 1.104% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 59 | 0.392% | 0.431% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.233% | 0.244% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.153% | 0.168% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.133% | 0.154% |
| ZX | Mandate not found or revoked | business | PSP | 17 | 0.113% | 0.091% |
| UX | Mandate execution outside permitted window | business | PSP | 14 | 0.093% | 0.109% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 64 | 69 |
| Auto-reversals | 21 | 17 |
| Disputes / chargebacks | 10 | 6 |
| Value returned | ₹88,737 | ₹97,739 |

## Customer behaviour

12,045 distinct customers transacted (+35.8% on the 28-day median) at 1.25 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,693 | 4,309 | 1.17 | 95.85% | ₹1,109 |
| power | 2,476 | 3,520 | 1.42 | 95.88% | ₹1,380 |
| merchant_heavy | 2,793 | 3,491 | 1.25 | 96.25% | ₹905 |
| small_ticket | 1,797 | 2,330 | 1.30 | 95.84% | ₹438 |
| occasional | 999 | 1,065 | 1.07 | 94.46% | ₹1,346 |
| new | 248 | 278 | 1.12 | 97.48% | ₹729 |
| dormant_returning | 39 | 41 | 1.05 | 95.12% | ₹1,270 |

## Operational events

- **INC-PSP-0031** (Sev-3) — HDFC MobileBanking app release regression, scoped to HDFC MobileBanking between 19:00 and 23:00. A HDFC MobileBanking client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

01 March ran on trend at 95.88% success and ₹1.55 Cr settled. The movement worth carrying forward is in the headline numbers: attempt volume ran 6.0 standard deviations up its trailing 28-day median at 15,034, 64.1% up on the same weekday last week. 13 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-01` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,034, successes=14,414, failed=608, pending=12, settled_value_inr=15,503,329.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: attempts=15,034; trailing_median=10,454; z=6.03
- psps: payer_psp=Google Pay; attempts=5,066; own_median=3,457.5; z=6.68
- categories: mcc_category=Bills; attempts=1,381; own_median=665.5; z=8.54
- psps: payer_psp=PhonePe; attempts=7,033; own_median=4,951; z=4.73
- products: product_name=UPI Person to Person; attempts=5,896; own_median=3,912; z=4.55
- banks: payer_bank=State Bank of India; attempts=4,816; own_median=3,383; z=4.98
- headline: value_inr=15,503,329; avg_ticket=1,075.57; trailing_avg_ticket=1,199.12
- geography: region=West; attempts=3,665; own_median=2,572; z=5.48
- geography: region=South; attempts=4,478; own_median=3,120; z=4.35
- geography: region=North; attempts=3,776; own_median=2,664; z=4.53

Refs: enterprise_data/warehouse/transactions, RPT-D55-DAILY, enterprise_data/warehouse/reference/incidents.parquet
