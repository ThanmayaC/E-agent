---
id: RPT-D104-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 18 Apr 2026)

**Report ID:** RPT-D104-DAILY · **Day 104 of 206** · **Derived from:** 16,188 transaction rows queried live from the warehouse

## Summary

The rail took **16,188 payment attempts** on Saturday 18 April 2026 (Weekend) and settled **₹1.92 Cr** across 15,558 successful payments. Volume was +31.3% on yesterday and +24.3% on the same weekday last week. Success closed at **96.11%**, in line with the trailing 28-day median of 95.90%.

Retries reached 435 attempts (2.69% of the day, 6.4 sigma above normal). 75.6% of re-presented payments recovered, so the retry path was doing its job. 101 auto-reversals were raised, 7.1 sigma above the trailing median of 22.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,188 | +31.3% | +24.3% | 12,756 |
| Successful payments | 15,558 | +40.9% | +24.6% | 12,146 |
| Success rate | 96.11% | +6.58pp | +0.20pp | 95.18% |
| Settled value | ₹1.92 Cr | +30.9% | +23.9% | ₹1.63 Cr |
| Average ticket | ₹1,235 | −7.1% | −0.5% | ₹1,346 |
| Technical declines | 0.315% | −1.74pp | −0.03pp | 0.611% |
| Business declines | 2.953% | −0.47pp | −0.16pp | 3.145% |
| Risk declines | 0.086% | −0.10pp | −0.08pp | 0.147% |
| Timeout declines | 0.451% | −4.11pp | +0.11pp | 0.793% |
| Retry share | 2.69% | −2.31pp | +1.55pp | 1.80% |
| Latency p95 | 1,248 ms | −45.5% | +3.0% | 1,369 ms |
| Active customers | 12,985 | +29.8% | +19.7% | 10,568 |
| Active merchants | 1,469 | +7.0% | +7.0% | 1,382 |

## What moved

- Category Retail carried 4,936 attempts, 53% up its trailing median and 45.9% of the day's volume.
- Attempt volume ran 2.8 standard deviations up its trailing 28-day median at 16,188, 24.3% up on the same weekday last week.
- App PhonePe carried 7,656 attempts, 31% up its trailing median and 47.3% of the day's volume.
- App Google Pay carried 5,411 attempts, 33% up its trailing median and 33.4% of the day's volume.
- Product UPI Circle is compounding — attempts up 45% across the trailing window to 483 today, with success holding, so the growth is healthy and worth funding.
- Issuer State Bank of India carried 5,177 attempts, 31% up its trailing median and 32.0% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,433 | 33.6% | 95.27% | ₹58.79 L | +28.8% |
| UPI Person to Merchant | 4,248 | 26.2% | 96.63% | ₹43.77 L | +27.0% |
| UPI QR Payments | 2,930 | 18.1% | 96.62% | ₹13.19 L | +37.7% |
| UPI Lite | 1,768 | 10.9% | 98.47% | ₹1.67 L | +68.2% |
| UPI Circle | 483 | 3.0% | 96.48% | ₹4.32 L | +84.0% |
| RuPay Credit on UPI | 351 | 2.2% | 95.16% | ₹24.26 L | +24.0% |
| UPI AutoPay | 335 | 2.1% | 89.25% | ₹5.00 L | +4.5% |
| Credit on UPI | 226 | 1.4% | 95.13% | ₹11.98 L | +16.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,177 | 95.96% | 95.92% | ₹62.03 L | normal |
| HDFC Bank | 1,801 | 96.61% | 95.87% | ₹19.59 L | normal |
| Bank of Baroda | 1,212 | 96.04% | 95.67% | ₹13.46 L | normal |
| ICICI Bank | 1,061 | 95.66% | 96.08% | ₹11.40 L | normal |
| Union Bank of India | 1,060 | 95.94% | 95.72% | ₹17.88 L | normal |
| Axis Bank | 1,033 | 96.52% | 95.62% | ₹10.88 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,656 | 95.95% | 95.78% | ₹86.69 L | normal |
| Google Pay | 5,411 | 96.41% | 95.63% | ₹63.28 L | normal |
| Paytm | 1,280 | 95.86% | 95.75% | ₹17.31 L | normal |
| Navi | 590 | 96.10% | 95.77% | ₹6.55 L | normal |
| SuperMoney | 299 | 97.66% | 94.55% | ₹5.40 L | normal |
| BHIM | 170 | 91.76% | 96.12% | ₹2.70 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,936 | 96.88% | ₹49.19 L |
| Food & Beverage | 2,494 | 97.23% | ₹11.05 L |
| Mobility | 1,210 | 96.45% | ₹6.44 L |
| Bills | 989 | 94.54% | ₹10.42 L |
| Healthcare | 494 | 97.98% | ₹3.54 L |
| Digital | 195 | 94.87% | ₹1.61 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,747 | 29.3% | 96.12% | ₹63.66 L |
| North | 4,081 | 25.2% | 95.91% | ₹45.00 L |
| West | 4,012 | 24.8% | 96.39% | ₹50.39 L |
| East | 1,857 | 11.5% | 95.32% | ₹19.79 L |
| Central | 1,491 | 9.2% | 96.85% | ₹13.29 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 90 | 95.56% | ₹3.04 L |
| Rapid Bazaar | Key Account | Retail | 539 | 98.52% | ₹2.55 L |
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹1.39 L |
| Urban Boutique | Key Account | Retail | 144 | 96.53% | ₹1.01 L |
| Ujjwal Water Board | Key Account | Bills | 42 | 100.00% | ₹1.01 L |
| Hampi Stores 2298 | Key Account | Retail | 164 | 96.95% | ₹91,651 |
| Girnar Connect | Key Account | Bills | 164 | 95.73% | ₹70,012 |
| Hampi Styles | Key Account | Retail | 36 | 94.44% | ₹61,476 |

## Failure analysis

Of 616 declined attempts, 478 were business declines (2.953% of attempts — balances, PINs and limits), 51 technical (0.315%), 73 timeouts (0.451%) and 14 risk declines (0.086%).

435 attempts were re-presentations of an earlier failure (2.69% of the day); 75.6% of them succeeded.

- Retries reached 435 attempts (2.69% of the day, 6.4 sigma above normal). 75.6% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.161% | 1.322% |
| ZM | Invalid UPI PIN | business | Customer | 167 | 1.032% | 1.015% |
| ZA | Transaction declined by customer | business | Customer | 62 | 0.383% | 0.369% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 41 | 0.253% | 0.182% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.167% | 0.221% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 22 | 0.136% | 0.103% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.136% | 0.193% |
| ZX | Mandate not found or revoked | business | PSP | 18 | 0.111% | 0.072% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 74 | 78 |
| Auto-reversals | 101 | 22 |
| Disputes / chargebacks | 11 | 11 |
| Value returned | ₹4.87 L | ₹1.55 L |

## Customer behaviour

12,985 distinct customers transacted (+27.2% on the 28-day median) at 1.25 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,052 | 4,784 | 1.18 | 96.24% | ₹1,399 |
| power | 2,630 | 3,759 | 1.43 | 95.85% | ₹1,781 |
| merchant_heavy | 2,956 | 3,671 | 1.24 | 96.24% | ₹857 |
| small_ticket | 1,973 | 2,518 | 1.28 | 96.07% | ₹501 |
| occasional | 1,077 | 1,137 | 1.06 | 95.95% | ₹1,029 |
| new | 259 | 278 | 1.07 | 97.84% | ₹814 |
| dormant_returning | 38 | 41 | 1.08 | 87.80% | ₹549 |

## Operational events

- **INC-PSP-0033** (Sev-1) — SuperMoney app release regression, scoped to SuperMoney between 18:00 and 23:00. A SuperMoney client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-NET-0042** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 11:00 and 16:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 101 auto-reversals were raised, 7.1 sigma above the trailing median of 22.

### Opportunities

- Product UPI Circle is compounding — attempts up 45% across the trailing window to 483 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

18 April was an incident day: INC-PSP-0033, INC-NET-0042 were live and the rail closed at 96.11% success against a 95.90% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,188, successes=15,558, failed=616, pending=14, settled_value_inr=19,213,171.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=435; retry_share_pct=2.69; recovery_pct=75.63; z=6.36
- adjustments: reversals=101; trailing_median=22.5; z=7.06
- categories: mcc_category=Retail; attempts=4,936; own_median=3,224.5; z=7.06
- incidents: event_id=INC-PSP-0033; kind=psp_degradation; severity=Sev-1; window=2026-04-15 to 2026-04-18; success_impact_pp=-23.53; volume_impact_pct=-36.83
- incidents: event_id=INC-NET-0042; kind=network_latency; severity=Sev-1; window=2026-04-17 to 2026-04-18; success_impact_pp=-13.62; volume_impact_pct=-12.58
- headline: attempts=16,188; trailing_median=12,295; z=2.8
- psps: payer_psp=PhonePe; attempts=7,656; own_median=5,830.5; z=2.69
- psps: payer_psp=Google Pay; attempts=5,411; own_median=4,079; z=3.01
- products: product_name=UPI Circle; attempts=483; window_growth_pct=45.2; success_rate=96.48
- banks: payer_bank=State Bank of India; attempts=5,177; own_median=3,951; z=2.81

Refs: enterprise_data/warehouse/transactions, RPT-D103-DAILY, enterprise_data/warehouse/reference/incidents.parquet
