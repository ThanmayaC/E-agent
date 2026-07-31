---
id: RPT-D59-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-04T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 04 Mar 2026)

**Report ID:** RPT-D59-DAILY · **Day 59 of 206** · **Derived from:** 15,981 transaction rows queried live from the warehouse

## Summary

The rail took **15,981 payment attempts** on Wednesday 04 March 2026 (Holi) and settled **₹1.73 Cr** across 15,366 successful payments. Volume was +8.1% on yesterday and +56.6% on the same weekday last week. Success closed at **96.15%**, above the trailing 28-day median of 95.54%.

Attempt volume ran 7.3 standard deviations up its trailing 28-day median at 15,981, 56.6% up on the same weekday last week. App Google Pay carried 5,317 attempts, 54% up its trailing median and 33.3% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,981 | +8.1% | +56.6% | 15,202 |
| Successful payments | 15,366 | +8.5% | +59.3% | 14,583 |
| Success rate | 96.15% | +0.37pp | +1.64pp | 95.92% |
| Settled value | ₹1.73 Cr | +6.8% | +39.1% | ₹1.65 Cr |
| Average ticket | ₹1,128 | −1.6% | −12.7% | ₹1,133 |
| Technical declines | 0.400% | +0.03pp | −0.27pp | 0.371% |
| Business declines | 2.941% | −0.28pp | −1.29pp | 3.176% |
| Risk declines | 0.131% | −0.02pp | +0.05pp | 0.113% |
| Timeout declines | 0.307% | −0.07pp | −0.11pp | 0.328% |
| Retry share | 1.18% | +0.03pp | −0.82pp | 1.20% |
| Latency p95 | 1,209 ms | −0.9% | −4.9% | 1,211 ms |
| Active customers | 12,747 | +6.7% | +46.6% | 12,197 |
| Active merchants | 1,356 | −1.7% | +9.2% | 1,366 |

## What moved

- Attempt volume ran 7.3 standard deviations up its trailing 28-day median at 15,981, 56.6% up on the same weekday last week.
- App Google Pay carried 5,317 attempts, 54% up its trailing median and 33.3% of the day's volume.
- App PhonePe carried 7,527 attempts, 52% up its trailing median and 47.1% of the day's volume.
- Issuer State Bank of India carried 5,133 attempts, 52% up its trailing median and 32.1% of the day's volume.
- Category Bills carried 1,376 attempts, 107% up its trailing median and 14.2% of the day's volume.
- Product UPI Person to Person carried 6,311 attempts, 61% up its trailing median and 39.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 6,311 | 39.5% | 95.48% | ₹72.41 L | +61.3% |
| UPI Person to Merchant | 4,908 | 30.7% | 96.56% | ₹48.95 L | +56.8% |
| UPI QR Payments | 2,538 | 15.9% | 97.01% | ₹10.94 L | +42.5% |
| UPI Lite | 1,078 | 6.7% | 99.07% | ₹97,083 | +49.1% |
| UPI AutoPay | 330 | 2.1% | 90.91% | ₹6.28 L | +10.0% |
| UPI Circle | 212 | 1.3% | 94.81% | ₹1.90 L | +102.9% |
| RuPay Credit on UPI | 160 | 1.0% | 95.00% | ₹9.50 L | −24.0% |
| Credit on UPI | 114 | 0.7% | 97.37% | ₹6.56 L | −22.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,133 | 95.87% | 95.48% | ₹56.88 L | normal |
| HDFC Bank | 1,712 | 96.67% | 96.22% | ₹18.22 L | normal |
| Bank of Baroda | 1,233 | 96.11% | 95.40% | ₹11.93 L | normal |
| Union Bank of India | 1,133 | 96.20% | 95.26% | ₹12.18 L | normal |
| ICICI Bank | 993 | 96.48% | 95.97% | ₹11.01 L | normal |
| Punjab National Bank | 958 | 97.08% | 94.87% | ₹11.88 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,527 | 96.32% | 95.61% | ₹83.95 L | normal |
| Google Pay | 5,317 | 96.18% | 95.59% | ₹55.67 L | normal |
| Paytm | 1,286 | 95.10% | 95.48% | ₹12.26 L | normal |
| Navi | 581 | 95.52% | 95.15% | ₹5.90 L | normal |
| SuperMoney | 295 | 98.64% | 95.91% | ₹4.06 L | normal |
| BHIM | 170 | 94.12% | 94.88% | ₹1.85 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,069 | 96.93% | ₹40.61 L |
| Food & Beverage | 2,418 | 97.02% | ₹9.46 L |
| Bills | 1,376 | 95.57% | ₹16.34 L |
| Mobility | 760 | 97.37% | ₹4.94 L |
| Healthcare | 392 | 97.19% | ₹2.63 L |
| Digital | 328 | 94.82% | ₹2.07 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,760 | 29.8% | 96.37% | ₹51.50 L |
| North | 4,027 | 25.2% | 95.58% | ₹41.99 L |
| West | 3,839 | 24.0% | 96.30% | ₹45.13 L |
| East | 1,887 | 11.8% | 96.50% | ₹19.19 L |
| Central | 1,468 | 9.2% | 96.19% | ₹15.56 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 108 | 95.37% | ₹2.25 L |
| Ujjwal Water Board | Key Account | Bills | 66 | 95.45% | ₹1.90 L |
| Rapid Bazaar | Key Account | Retail | 416 | 96.39% | ₹1.46 L |
| Urban Boutique | Key Account | Retail | 95 | 96.84% | ₹1.03 L |
| Girnar Connect | Key Account | Bills | 212 | 98.11% | ₹1.01 L |
| Vega Electronics | Large | Retail | 24 | 100.00% | ₹85,415 |
| Swift Mart 1738 | Key Account | Retail | 152 | 98.68% | ₹70,561 |
| Hampi Stores 2298 | Key Account | Retail | 109 | 100.00% | ₹70,249 |

## Failure analysis

Of 604 declined attempts, 470 were business declines (2.941% of attempts — balances, PINs and limits), 64 technical (0.400%), 49 timeouts (0.307%) and 21 risk declines (0.131%).

189 attempts were re-presentations of an earlier failure (1.18% of the day); 64.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.176% | 1.479% |
| ZM | Invalid UPI PIN | business | Customer | 157 | 0.982% | 1.196% |
| ZA | Transaction declined by customer | business | Customer | 58 | 0.363% | 0.426% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.194% | 0.248% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.150% | 0.159% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.125% | 0.159% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.113% | 0.104% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.113% | 0.119% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 68 | 68 |
| Auto-reversals | 27 | 18 |
| Disputes / chargebacks | 9 | 7 |
| Value returned | ₹65,722 | ₹96,246 |

## Customer behaviour

12,747 distinct customers transacted (+43.7% on the 28-day median) at 1.25 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,017 | 4,731 | 1.18 | 96.36% | ₹1,134 |
| power | 2,616 | 3,743 | 1.43 | 95.91% | ₹1,624 |
| merchant_heavy | 2,920 | 3,690 | 1.26 | 96.12% | ₹859 |
| small_ticket | 1,855 | 2,382 | 1.28 | 96.35% | ₹434 |
| occasional | 1,042 | 1,117 | 1.07 | 95.79% | ₹1,293 |
| new | 262 | 281 | 1.07 | 95.37% | ₹768 |
| dormant_returning | 35 | 37 | 1.06 | 100.00% | ₹792 |

## Operational events

- **INC-PSP-0026** (Sev-2) — YONO SBI app release regression, scoped to YONO SBI between 18:00 and 23:00. A YONO SBI client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-BANK-0009** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 17:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **REG-0070** (Sev-3) — UPI Circle full-delegation rollout to all PSPs, scoped to UPI_CIRCLE. Full-delegation Circle became available across every major PSP, converting the pilot cohort into mainstream volume.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 30% across the trailing window to 212 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Person to Person is compounding — attempts up 29% across the trailing window to 6,311 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

04 March was an incident day: INC-PSP-0026 was live and the rail closed at 96.15% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-04` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,981, successes=15,366, failed=604, pending=11, settled_value_inr=17,337,380.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: attempts=15,981; trailing_median=10,454; z=7.27
- psps: payer_psp=Google Pay; attempts=5,317; own_median=3,457.5; z=7.72
- psps: payer_psp=PhonePe; attempts=7,527; own_median=4,951; z=5.85
- banks: payer_bank=State Bank of India; attempts=5,133; own_median=3,383; z=5.99
- categories: mcc_category=Bills; attempts=1,376; own_median=665.5; z=8.48
- products: product_name=UPI Person to Person; attempts=6,311; own_median=3,912; z=5.09
- geography: region=West; attempts=3,839; own_median=2,572; z=6.35
- headline: value_inr=17,337,380; avg_ticket=1,128.29; trailing_avg_ticket=1,184.08
- geography: region=South; attempts=4,760; own_median=3,120; z=5.25
- geography: region=North; attempts=4,027; own_median=2,664; z=5.3

Refs: enterprise_data/warehouse/transactions, RPT-D58-DAILY, enterprise_data/warehouse/reference/incidents.parquet
