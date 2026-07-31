---
id: RPT-D167-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 20 Jun 2026)

**Report ID:** RPT-D167-DAILY · **Day 167 of 206** · **Derived from:** 19,314 transaction rows queried live from the warehouse

## Summary

The rail took **19,314 payment attempts** on Saturday 20 June 2026 (Monsoon Sale) and settled **₹2.58 Cr** across 18,658 successful payments. Volume was +20.7% on yesterday and +26.6% on the same weekday last week. Success closed at **96.60%**, above the trailing 28-day median of 96.24%.

22 disputes were raised, 3.0 sigma above the trailing median of 13. Category Retail carried 6,198 attempts, 44% up its trailing median and 44.4% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 19,314 | +20.7% | +26.6% | 15,115 |
| Successful payments | 18,658 | +21.1% | +26.9% | 14,565 |
| Success rate | 96.60% | +0.37pp | +0.21pp | 96.34% |
| Settled value | ₹2.58 Cr | +24.4% | +54.5% | ₹2.01 Cr |
| Average ticket | ₹1,383 | +2.7% | +21.8% | ₹1,380 |
| Technical declines | 0.461% | −0.08pp | +0.05pp | 0.409% |
| Business declines | 2.485% | −0.23pp | −0.29pp | 2.773% |
| Risk declines | 0.109% | −0.03pp | +0.04pp | 0.126% |
| Timeout declines | 0.243% | −0.03pp | −0.01pp | 0.262% |
| Retry share | 0.96% | −0.17pp | −0.06pp | 1.03% |
| Latency p95 | 1,272 ms | −3.2% | +6.0% | 1,277 ms |
| Active customers | 15,208 | +16.1% | +22.8% | 12,385 |
| Active merchants | 1,667 | +8.0% | +7.1% | 1,551 |

## What moved

- Category Retail carried 6,198 attempts, 44% up its trailing median and 44.4% of the day's volume.
- Region North carried 5,046 attempts, 35% up its trailing median and 26.1% of the day's volume.
- Attempt volume ran 3.1 standard deviations up its trailing 28-day median at 19,314, 26.6% up on the same weekday last week.
- App PhonePe ran at 96.65% success on 9,046 attempts (46.8% of the day), 0.52pp up its own 28-day median.
- Category Food & Beverage carried 3,579 attempts, 44% up its trailing median and 25.6% of the day's volume.
- Product UPI QR Payments carried 3,490 attempts, 45% up its trailing median and 18.1% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,359 | 27.7% | 95.54% | ₹58.22 L | +22.9% |
| UPI Person to Merchant | 4,698 | 24.3% | 96.34% | ₹55.53 L | +29.1% |
| UPI QR Payments | 3,490 | 18.1% | 97.02% | ₹16.01 L | +45.1% |
| UPI Lite | 2,787 | 14.4% | 98.92% | ₹2.80 L | +41.6% |
| UPI Circle | 1,295 | 6.7% | 98.22% | ₹11.64 L | +86.3% |
| UPI AutoPay | 385 | 2.0% | 91.69% | ₹7.58 L | +9.5% |
| Credit on UPI | 384 | 2.0% | 96.09% | ₹24.63 L | −10.9% |
| RuPay Credit on UPI | 339 | 1.8% | 94.69% | ₹20.31 L | −6.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 6,131 | 96.28% | 96.18% | ₹78.99 L | normal |
| HDFC Bank | 2,064 | 96.46% | 96.43% | ₹24.99 L | normal |
| Bank of Baroda | 1,513 | 96.70% | 96.46% | ₹20.24 L | normal |
| Union Bank of India | 1,289 | 96.35% | 96.27% | ₹18.33 L | normal |
| ICICI Bank | 1,211 | 97.69% | 96.62% | ₹22.62 L | normal |
| Axis Bank | 1,169 | 96.15% | 96.47% | ₹15.32 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 9,046 | 96.65% | 96.13% | ₹1.23 Cr | ⚠ outlier |
| Google Pay | 6,390 | 96.45% | 96.36% | ₹84.65 L | normal |
| Paytm | 1,655 | 96.98% | 96.12% | ₹21.45 L | normal |
| Navi | 740 | 96.08% | 96.19% | ₹9.01 L | normal |
| SuperMoney | 365 | 97.81% | 96.21% | ₹4.27 L | normal |
| FamApp | 173 | 98.27% | 96.53% | ₹1.50 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 6,198 | 96.87% | ₹80.64 L |
| Food & Beverage | 3,579 | 97.51% | ₹18.18 L |
| Mobility | 1,771 | 97.91% | ₹11.06 L |
| Bills | 996 | 96.49% | ₹11.55 L |
| Healthcare | 670 | 97.76% | ₹5.48 L |
| Digital | 224 | 94.64% | ₹1.30 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,568 | 28.8% | 96.55% | ₹78.44 L |
| North | 5,046 | 26.1% | 96.33% | ₹68.75 L |
| West | 4,780 | 24.7% | 96.69% | ₹64.79 L |
| East | 2,264 | 11.7% | 97.13% | ₹27.09 L |
| Central | 1,656 | 8.6% | 96.62% | ₹18.91 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 66 | 92.42% | ₹6.09 L |
| Vasant Wardrobe | Key Account | Retail | 140 | 92.14% | ₹3.57 L |
| Rapid Bazaar | Key Account | Retail | 595 | 97.82% | ₹2.89 L |
| Hampi Styles | Key Account | Retail | 62 | 96.77% | ₹1.56 L |
| Urban Boutique | Key Account | Retail | 202 | 96.04% | ₹1.54 L |
| Kaveri Trading | Large | Retail | 78 | 97.44% | ₹1.30 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 96 | 95.83% | ₹1.14 L |
| Aravalli Pharmacy | Large | Healthcare | 112 | 96.43% | ₹1.01 L |

## Failure analysis

Of 637 declined attempts, 480 were business declines (2.485% of attempts — balances, PINs and limits), 89 technical (0.461%), 47 timeouts (0.243%) and 21 risk declines (0.109%).

186 attempts were re-presentations of an earlier failure (0.96% of the day); 67.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 194 | 1.004% | 1.203% |
| ZM | Invalid UPI PIN | business | Customer | 176 | 0.911% | 0.932% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.259% | 0.354% |
| XH | Account does not exist / frozen | business | Issuer | 38 | 0.197% | 0.206% |
| U30 | Debit failed at remitter bank | technical | Issuer | 34 | 0.176% | 0.186% |
| U28 | Remitter bank unavailable | technical | Issuer | 29 | 0.150% | 0.113% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.109% | 0.141% |
| U69 | Beneficiary bank offline | technical | Issuer | 16 | 0.083% | 0.078% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 116 | 106 |
| Auto-reversals | 19 | 24 |
| Disputes / chargebacks | 22 | 13 |
| Value returned | ₹1.51 L | ₹1.71 L |

## Customer behaviour

15,208 distinct customers transacted (+24.6% on the 28-day median) at 1.27 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,822 | 5,731 | 1.19 | 96.37% | ₹1,451 |
| power | 3,124 | 4,549 | 1.46 | 96.68% | ₹1,881 |
| merchant_heavy | 3,470 | 4,431 | 1.28 | 96.91% | ₹1,073 |
| small_ticket | 2,217 | 2,912 | 1.31 | 96.74% | ₹616 |
| occasional | 1,243 | 1,326 | 1.07 | 96.23% | ₹1,471 |
| new | 288 | 319 | 1.11 | 96.55% | ₹1,272 |
| dormant_returning | 44 | 46 | 1.05 | 91.30% | ₹525 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.

## Risks and opportunities

### Risks

- 22 disputes were raised, 3.0 sigma above the trailing median of 13.

### Opportunities

- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 384 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

20 June ran on trend at 96.60% success and ₹2.58 Cr settled. The movement worth carrying forward is in money moving back: 22 disputes were raised, 3.0 sigma above the trailing median of 13. 14 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=19,314, successes=18,658, failed=637, pending=19, settled_value_inr=25,797,910.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=22; trailing_median=13; z=3.04
- categories: mcc_category=Retail; attempts=6,198; own_median=4,309; z=4.7
- geography: region=North; attempts=5,046; own_median=3,750; z=4.55
- headline: attempts=19,314; trailing_median=14,771; z=3.13
- psps: payer_psp=PhonePe; attempts=9,046; success_rate=96.65; own_median=96.13; z=2.38
- categories: mcc_category=Food & Beverage; attempts=3,579; own_median=2,480; z=4.31
- products: product_name=UPI QR Payments; attempts=3,490; own_median=2,405.5; z=5.1
- psps: payer_psp=PhonePe; attempts=9,046; own_median=7,000.5; z=2.99
- psps: payer_psp=Google Pay; attempts=6,390; own_median=4,891; z=3.36
- categories: mcc_category=Mobility; attempts=1,771; own_median=1,196.5; z=5.27

Refs: enterprise_data/warehouse/transactions, RPT-D166-DAILY, enterprise_data/warehouse/reference/incidents.parquet
