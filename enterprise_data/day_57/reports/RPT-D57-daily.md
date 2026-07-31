---
id: RPT-D57-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-02T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 02 Mar 2026)

**Report ID:** RPT-D57-DAILY · **Day 57 of 206** · **Derived from:** 15,008 transaction rows queried live from the warehouse

## Summary

The rail took **15,008 payment attempts** on Monday 02 March 2026 (Holi (build-up)) and settled **₹1.70 Cr** across 14,391 successful payments. Volume was −0.2% on yesterday and +48.2% on the same weekday last week. Success closed at **95.89%**, above the trailing 28-day median of 95.54%.

Attempt volume ran 6.0 standard deviations up its trailing 28-day median at 15,008, 48.2% up on the same weekday last week. App Google Pay carried 4,942 attempts, 43% up its trailing median and 32.9% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,008 | −0.2% | +48.2% | 15,021 |
| Successful payments | 14,391 | −0.2% | +48.7% | 14,402 |
| Success rate | 95.89% | +0.01pp | +0.33pp | 95.88% |
| Settled value | ₹1.70 Cr | +9.8% | +54.7% | ₹1.63 Cr |
| Average ticket | ₹1,183 | +10.0% | +4.0% | ₹1,129 |
| Technical declines | 0.380% | +0.05pp | +0.13pp | 0.356% |
| Business declines | 3.165% | −0.21pp | −0.53pp | 3.272% |
| Risk declines | 0.073% | −0.02pp | −0.06pp | 0.083% |
| Timeout declines | 0.393% | +0.15pp | +0.18pp | 0.316% |
| Retry share | 1.19% | −0.06pp | −0.03pp | 1.22% |
| Latency p95 | 1,202 ms | −0.9% | −3.6% | 1,207 ms |
| Active customers | 12,050 | +0.0% | +38.8% | 12,048 |
| Active merchants | 1,369 | +0.7% | +10.4% | 1,364 |

## What moved

- Attempt volume ran 6.0 standard deviations up its trailing 28-day median at 15,008, 48.2% up on the same weekday last week.
- App Google Pay carried 4,942 attempts, 43% up its trailing median and 32.9% of the day's volume.
- App PhonePe carried 7,015 attempts, 42% up its trailing median and 46.7% of the day's volume.
- Region West carried 3,702 attempts, 44% up its trailing median and 24.7% of the day's volume.
- Issuer State Bank of India carried 4,767 attempts, 41% up its trailing median and 31.8% of the day's volume.
- Category Bills carried 1,275 attempts, 92% up its trailing median and 13.8% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,802 | 38.7% | 95.59% | ₹66.74 L | +48.3% |
| UPI Person to Merchant | 4,564 | 30.4% | 95.64% | ₹48.63 L | +45.8% |
| UPI QR Payments | 2,646 | 17.6% | 96.49% | ₹12.02 L | +48.5% |
| UPI Lite | 855 | 5.7% | 99.77% | ₹77,299 | +18.3% |
| UPI AutoPay | 280 | 1.9% | 90.00% | ₹5.09 L | −6.4% |
| RuPay Credit on UPI | 223 | 1.5% | 95.07% | ₹10.67 L | +5.9% |
| Credit on UPI | 158 | 1.1% | 96.84% | ₹12.26 L | +8.2% |
| UPI Circle | 143 | 1.0% | 95.10% | ₹1.23 L | +36.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,767 | 95.80% | 95.54% | ₹53.88 L | normal |
| HDFC Bank | 1,609 | 96.40% | 96.15% | ₹19.74 L | normal |
| Bank of Baroda | 1,143 | 94.93% | 95.40% | ₹11.01 L | normal |
| Union Bank of India | 1,064 | 95.68% | 95.39% | ₹15.27 L | normal |
| ICICI Bank | 980 | 94.80% | 96.03% | ₹9.88 L | normal |
| Axis Bank | 906 | 96.69% | 95.61% | ₹11.32 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,015 | 96.02% | 95.55% | ₹84.56 L | normal |
| Google Pay | 4,942 | 95.93% | 95.61% | ₹52.35 L | normal |
| Paytm | 1,216 | 96.79% | 95.41% | ₹13.96 L | normal |
| Navi | 570 | 95.09% | 95.15% | ₹6.51 L | normal |
| SuperMoney | 319 | 95.92% | 96.18% | ₹3.18 L | normal |
| BHIM | 159 | 94.34% | 95.09% | ₹2.10 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,880 | 96.16% | ₹42.46 L |
| Food & Beverage | 2,212 | 96.02% | ₹10.53 L |
| Bills | 1,275 | 95.69% | ₹17.53 L |
| Mobility | 810 | 98.02% | ₹5.87 L |
| Healthcare | 405 | 96.54% | ₹3.88 L |
| Digital | 293 | 95.56% | ₹1.62 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,406 | 29.4% | 95.60% | ₹47.37 L |
| North | 3,835 | 25.6% | 95.91% | ₹42.48 L |
| West | 3,702 | 24.7% | 96.46% | ₹44.67 L |
| East | 1,753 | 11.7% | 95.04% | ₹21.38 L |
| Central | 1,312 | 8.7% | 96.34% | ₹14.38 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 419 | 97.61% | ₹2.57 L |
| Vasant Wardrobe | Key Account | Retail | 92 | 95.65% | ₹2.48 L |
| Vega Electronics | Large | Retail | 35 | 94.29% | ₹1.99 L |
| Ujjwal Water Board | Key Account | Bills | 90 | 94.44% | ₹1.98 L |
| Tejas Restaurant | Large | Food & Beverage | 41 | 97.56% | ₹90,781 |
| Hampi Styles | Key Account | Retail | 61 | 96.72% | ₹86,444 |
| Girnar Connect | Key Account | Bills | 196 | 96.43% | ₹78,899 |
| Hampi Stores 2298 | Key Account | Retail | 123 | 95.12% | ₹68,952 |

## Failure analysis

Of 602 declined attempts, 475 were business declines (3.165% of attempts — balances, PINs and limits), 57 technical (0.380%), 59 timeouts (0.393%) and 11 risk declines (0.073%).

179 attempts were re-presentations of an earlier failure (1.19% of the day); 58.7% of them succeeded.

- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 12 times — 0.080% of attempts against a trailing 0.045%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 192 | 1.279% | 1.484% |
| ZM | Invalid UPI PIN | business | Customer | 161 | 1.073% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 64 | 0.426% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.193% | 0.243% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.167% | 0.154% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 22 | 0.147% | 0.103% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.140% | 0.166% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.113% | 0.108% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 84 | 68 |
| Auto-reversals | 24 | 17 |
| Disputes / chargebacks | 10 | 6 |
| Value returned | ₹79,738 | ₹96,246 |

## Customer behaviour

12,050 distinct customers transacted (+35.8% on the 28-day median) at 1.25 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,769 | 4,393 | 1.17 | 95.72% | ₹1,253 |
| power | 2,463 | 3,496 | 1.42 | 95.48% | ₹1,487 |
| merchant_heavy | 2,720 | 3,396 | 1.25 | 96.29% | ₹956 |
| small_ticket | 1,801 | 2,336 | 1.30 | 96.02% | ₹505 |
| occasional | 1,006 | 1,070 | 1.06 | 96.07% | ₹1,417 |
| new | 251 | 275 | 1.10 | 96.73% | ₹1,162 |
| dormant_returning | 40 | 42 | 1.05 | 97.62% | ₹1,436 |

## Operational events

- **INC-PSP-0026** (Sev-2) — YONO SBI app release regression, scoped to YONO SBI between 18:00 and 23:00. A YONO SBI client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-PSP-0031** (Sev-3) — HDFC MobileBanking app release regression, scoped to HDFC MobileBanking between 19:00 and 23:00. A HDFC MobileBanking client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-BANK-0009** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 17:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 12 times — 0.080% of attempts against a trailing 0.045%. Owner: NPCI.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

02 March was an incident day: INC-PSP-0026 was live and the rail closed at 95.89% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-02` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,008, successes=14,391, failed=602, pending=15, settled_value_inr=17,027,947.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: attempts=15,008; trailing_median=10,454; z=5.99
- psps: payer_psp=Google Pay; attempts=4,942; own_median=3,457.5; z=6.16
- psps: payer_psp=PhonePe; attempts=7,015; own_median=4,951; z=4.69
- geography: region=West; attempts=3,702; own_median=2,572; z=5.67
- banks: payer_bank=State Bank of India; attempts=4,767; own_median=3,383; z=4.81
- categories: mcc_category=Bills; attempts=1,275; own_median=665.5; z=7.28
- products: product_name=UPI Person to Person; attempts=5,802; own_median=3,912; z=4.34
- categories: mcc_category=Retail; attempts=3,880; own_median=2,734.5; z=4.02
- geography: region=North; attempts=3,835; own_median=2,664; z=4.77
- incidents: event_id=INC-PSP-0026; kind=psp_degradation; severity=Sev-2; window=2026-03-02 to 2026-03-05; success_impact_pp=-9.44; volume_impact_pct=-14.77

Refs: enterprise_data/warehouse/transactions, RPT-D56-DAILY, enterprise_data/warehouse/reference/incidents.parquet
