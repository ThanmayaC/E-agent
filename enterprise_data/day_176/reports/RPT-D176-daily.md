---
id: RPT-D176-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-29T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 29 Jun 2026)

**Report ID:** RPT-D176-DAILY · **Day 176 of 206** · **Derived from:** 17,193 transaction rows queried live from the warehouse

## Summary

The rail took **17,193 payment attempts** on Monday 29 June 2026 (Quarter Close Q1FY27 (build-up)) and settled **₹2.36 Cr** across 16,600 successful payments. Volume was +22.4% on yesterday and +20.5% on the same weekday last week. Success closed at **96.55%**, above the trailing 28-day median of 96.24%.

App PhonePe ran at 96.77% success on 8,090 attempts (47.1% of the day), 0.67pp up its own 28-day median. Category Bills carried 1,457 attempts, 71% up its trailing median and 12.0% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 17,193 | +22.4% | +20.5% | 14,890 |
| Successful payments | 16,600 | +23.0% | +21.0% | 14,332 |
| Success rate | 96.55% | +0.46pp | +0.42pp | 96.23% |
| Settled value | ₹2.36 Cr | +49.8% | +25.5% | ₹1.93 Cr |
| Average ticket | ₹1,422 | +21.8% | +3.7% | ₹1,343 |
| Technical declines | 0.396% | +0.00pp | −0.04pp | 0.421% |
| Business declines | 2.664% | −0.40pp | −0.24pp | 2.875% |
| Risk declines | 0.081% | −0.05pp | −0.04pp | 0.124% |
| Timeout declines | 0.256% | +0.03pp | −0.07pp | 0.264% |
| Retry share | 1.02% | −0.16pp | −0.25pp | 1.09% |
| Latency p95 | 1,273 ms | +3.1% | −0.8% | 1,276 ms |
| Active customers | 13,881 | +19.1% | +17.1% | 12,238 |
| Active merchants | 1,627 | +6.4% | +7.4% | 1,546 |

## What moved

- App PhonePe ran at 96.77% success on 8,090 attempts (47.1% of the day), 0.67pp up its own 28-day median.
- Category Bills carried 1,457 attempts, 71% up its trailing median and 12.0% of the day's volume.
- Region North carried 4,527 attempts, 25% up its trailing median and 26.3% of the day's volume.
- Attempt volume ran 2.3 standard deviations up its trailing 28-day median at 17,193, 20.5% up on the same weekday last week.
- Product UPI Lite carried 2,862 attempts, 36% up its trailing median and 16.6% of the day's volume.
- Category Food & Beverage carried 2,982 attempts, 19% up its trailing median and 24.7% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,101 | 29.7% | 95.90% | ₹55.47 L | +22.1% |
| UPI Person to Merchant | 3,713 | 21.6% | 96.07% | ₹38.22 L | +7.1% |
| UPI Lite | 2,862 | 16.6% | 98.78% | ₹2.71 L | +35.5% |
| UPI QR Payments | 2,675 | 15.6% | 97.23% | ₹12.83 L | +15.7% |
| UPI Circle | 831 | 4.8% | 96.87% | ₹7.06 L | +15.7% |
| Credit on UPI | 614 | 3.6% | 95.77% | ₹49.66 L | +35.8% |
| RuPay Credit on UPI | 440 | 2.6% | 95.68% | ₹19.80 L | +19.6% |
| UPI AutoPay | 378 | 2.2% | 91.80% | ₹6.58 L | +4.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,443 | 96.64% | 96.30% | ₹76.31 L | normal |
| HDFC Bank | 1,875 | 97.01% | 96.43% | ₹24.48 L | normal |
| Bank of Baroda | 1,248 | 96.15% | 96.22% | ₹15.84 L | normal |
| Union Bank of India | 1,179 | 97.20% | 96.11% | ₹19.31 L | normal |
| Axis Bank | 1,109 | 95.49% | 96.21% | ₹15.50 L | normal |
| ICICI Bank | 1,059 | 95.75% | 96.54% | ₹11.15 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,090 | 96.77% | 96.11% | ₹1.10 Cr | ⚠ outlier |
| Google Pay | 5,719 | 96.17% | 96.36% | ₹73.80 L | normal |
| Paytm | 1,414 | 96.75% | 96.12% | ₹22.40 L | normal |
| Navi | 652 | 97.09% | 96.44% | ₹8.28 L | normal |
| SuperMoney | 309 | 95.47% | 95.97% | ₹4.94 L | normal |
| BHIM | 173 | 94.80% | 95.85% | ₹5.59 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,740 | 96.90% | ₹60.25 L |
| Food & Beverage | 2,982 | 97.52% | ₹15.68 L |
| Mobility | 1,510 | 97.75% | ₹9.27 L |
| Bills | 1,457 | 96.36% | ₹14.90 L |
| Healthcare | 602 | 97.18% | ₹14.30 L |
| Digital | 292 | 95.55% | ₹1.45 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,997 | 29.1% | 96.76% | ₹70.42 L |
| North | 4,527 | 26.3% | 96.38% | ₹57.80 L |
| West | 4,198 | 24.4% | 95.97% | ₹56.58 L |
| East | 2,038 | 11.9% | 97.06% | ₹33.19 L |
| Central | 1,433 | 8.3% | 97.35% | ₹18.04 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 48 | 95.83% | ₹3.83 L |
| Vasant Wardrobe | Key Account | Retail | 88 | 97.73% | ₹3.09 L |
| Hampi Styles | Key Account | Retail | 39 | 94.87% | ₹2.28 L |
| Rapid Bazaar | Key Account | Retail | 420 | 97.38% | ₹1.75 L |
| Hampi Stores 2298 | Key Account | Retail | 147 | 96.60% | ₹1.16 L |
| Swift Grill | Large | Food & Beverage | 71 | 98.59% | ₹1.14 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 83 | 95.18% | ₹1.14 L |
| Ujjwal Water Board | Key Account | Bills | 56 | 94.64% | ₹1.05 L |

## Failure analysis

Of 584 declined attempts, 458 were business declines (2.664% of attempts — balances, PINs and limits), 68 technical (0.396%), 44 timeouts (0.256%) and 14 risk declines (0.081%).

175 attempts were re-presentations of an earlier failure (1.02% of the day); 68.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 201 | 1.169% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 150 | 0.872% | 0.942% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.320% | 0.334% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.151% | 0.200% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.151% | 0.176% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.134% | 0.137% |
| ZX | Mandate not found or revoked | business | PSP | 17 | 0.099% | 0.078% |
| U69 | Beneficiary bank offline | technical | Issuer | 17 | 0.099% | 0.082% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 108 | 108 |
| Auto-reversals | 22 | 22 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹93,764 | ₹1.70 L |

## Customer behaviour

13,881 distinct customers transacted (+16.3% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,377 | 5,099 | 1.16 | 96.86% | ₹1,543 |
| power | 2,937 | 4,114 | 1.40 | 96.52% | ₹1,918 |
| merchant_heavy | 3,227 | 3,999 | 1.24 | 96.60% | ₹1,019 |
| small_ticket | 2,020 | 2,575 | 1.27 | 96.54% | ₹621 |
| occasional | 1,063 | 1,122 | 1.06 | 95.54% | ₹1,713 |
| new | 232 | 258 | 1.11 | 94.96% | ₹852 |
| dormant_returning | 25 | 26 | 1.04 | 92.31% | ₹1,037 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

29 June ran on trend at 96.55% success and ₹2.36 Cr settled. The movement worth carrying forward is in app performance: app PhonePe ran at 96.77% success on 8,090 attempts (47.1% of the day), 0.67pp up its own 28-day median. 3 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-29` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=17,193, successes=16,600, failed=584, pending=9, settled_value_inr=23,602,353.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- psps: payer_psp=PhonePe; attempts=8,090; success_rate=96.77; own_median=96.11; z=2.26
- categories: mcc_category=Bills; attempts=1,457; own_median=852; z=5.75
- geography: region=North; attempts=4,527; own_median=3,624; z=3.37
- headline: attempts=17,193; trailing_median=14,446; z=2.35
- products: product_name=UPI Lite; attempts=2,862; own_median=2,111.5; z=3.26
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- categories: mcc_category=Food & Beverage; attempts=2,982; own_median=2,507.5; z=2.46
- banks: payer_bank=Kotak Mahindra Bank; attempts=663; own_median=518; z=4.35
- categories: mcc_category=Mobility; attempts=1,510; own_median=1,254.5; z=2.38
- geography: region=East; attempts=2,038; own_median=1,692.5; z=2.4

Refs: enterprise_data/warehouse/transactions, RPT-D175-DAILY, enterprise_data/warehouse/reference/incidents.parquet
