---
id: RPT-D178-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-01T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 01 Jul 2026)

**Report ID:** RPT-D178-DAILY · **Day 178 of 206** · **Derived from:** 18,572 transaction rows queried live from the warehouse

## Summary

The rail took **18,572 payment attempts** on Wednesday 01 July 2026 (Working day) and settled **₹2.52 Cr** across 17,894 successful payments. Volume was +7.0% on yesterday and +44.2% on the same weekday last week. Success closed at **96.35%**, in line with the trailing 28-day median of 96.21%.

Category Bills carried 2,041 attempts, 140% up its trailing median and 15.3% of the day's volume. Attempt volume ran 3.5 standard deviations up its trailing 28-day median at 18,572, 44.2% up on the same weekday last week.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 18,572 | +7.0% | +44.2% | 18,572 |
| Successful payments | 17,894 | +7.4% | +45.7% | 17,894 |
| Success rate | 96.35% | +0.41pp | +0.93pp | 96.35% |
| Settled value | ₹2.52 Cr | −2.3% | +55.4% | ₹2.52 Cr |
| Average ticket | ₹1,409 | −9.1% | +6.7% | ₹1,409 |
| Technical declines | 0.377% | −0.07pp | −0.07pp | 0.377% |
| Business declines | 2.886% | −0.16pp | −0.73pp | 2.886% |
| Risk declines | 0.070% | −0.03pp | −0.01pp | 0.070% |
| Timeout declines | 0.242% | −0.13pp | −0.09pp | 0.242% |
| Retry share | 1.32% | −0.10pp | +0.05pp | 1.32% |
| Latency p95 | 1,246 ms | −8.9% | −6.8% | 1,246 ms |
| Active customers | 14,722 | +5.5% | +36.2% | 14,722 |
| Active merchants | 1,658 | +0.8% | +10.2% | 1,658 |

## What moved

- Category Bills carried 2,041 attempts, 140% up its trailing median and 15.3% of the day's volume.
- Attempt volume ran 3.5 standard deviations up its trailing 28-day median at 18,572, 44.2% up on the same weekday last week.
- Region North carried 4,825 attempts, 33% up its trailing median and 26.0% of the day's volume.
- App PhonePe carried 8,688 attempts, 27% up its trailing median and 46.8% of the day's volume.
- Issuer State Bank of India carried 5,895 attempts, 30% up its trailing median and 31.7% of the day's volume.
- App Google Pay carried 6,219 attempts, 30% up its trailing median and 33.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,198 | 28.0% | 95.21% | ₹58.58 L | +24.4% |
| UPI Person to Merchant | 4,435 | 23.9% | 96.08% | ₹46.31 L | +27.9% |
| UPI Lite | 3,266 | 17.6% | 98.96% | ₹3.18 L | +50.5% |
| UPI QR Payments | 2,911 | 15.7% | 96.67% | ₹12.04 L | +25.9% |
| UPI Circle | 856 | 4.6% | 98.13% | ₹8.47 L | +19.2% |
| Credit on UPI | 557 | 3.0% | 95.69% | ₹50.05 L | +23.2% |
| RuPay Credit on UPI | 416 | 2.2% | 94.71% | ₹17.18 L | +13.0% |
| UPI AutoPay | 398 | 2.1% | 90.70% | ₹7.60 L | +8.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,895 | 96.00% | 96.23% | ₹82.99 L | normal |
| HDFC Bank | 2,030 | 96.80% | 96.39% | ₹29.71 L | normal |
| Bank of Baroda | 1,429 | 97.34% | 96.22% | ₹17.91 L | ⚠ outlier |
| Union Bank of India | 1,263 | 96.12% | 96.00% | ₹16.60 L | normal |
| Punjab National Bank | 1,164 | 96.74% | 96.05% | ₹15.03 L | normal |
| ICICI Bank | 1,117 | 96.33% | 96.39% | ₹15.67 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,688 | 96.28% | 96.11% | ₹1.13 Cr | normal |
| Google Pay | 6,219 | 96.61% | 96.33% | ₹80.90 L | normal |
| Paytm | 1,486 | 96.77% | 96.03% | ₹20.65 L | normal |
| Navi | 683 | 95.17% | 96.47% | ₹13.65 L | normal |
| SuperMoney | 398 | 95.48% | 95.97% | ₹8.03 L | normal |
| BHIM | 184 | 96.74% | 95.87% | ₹2.40 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,913 | 97.17% | ₹62.86 L |
| Food & Beverage | 3,166 | 97.13% | ₹15.25 L |
| Bills | 2,041 | 95.98% | ₹20.15 L |
| Mobility | 1,656 | 97.34% | ₹6.97 L |
| Healthcare | 686 | 97.08% | ₹7.43 L |
| Digital | 358 | 96.65% | ₹1.80 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,428 | 29.2% | 96.46% | ₹68.24 L |
| North | 4,825 | 26.0% | 96.27% | ₹65.99 L |
| West | 4,574 | 24.6% | 96.15% | ₹71.08 L |
| East | 2,231 | 12.0% | 96.15% | ₹30.31 L |
| Central | 1,514 | 8.2% | 97.09% | ₹16.43 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 76 | 98.68% | ₹3.32 L |
| Vega Electronics | Large | Retail | 34 | 100.00% | ₹2.40 L |
| Rapid Bazaar | Key Account | Retail | 454 | 98.24% | ₹2.33 L |
| Vasant Wardrobe | Key Account | Retail | 79 | 93.67% | ₹2.31 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 90 | 94.44% | ₹1.69 L |
| Girnar Connect | Key Account | Bills | 345 | 96.81% | ₹1.27 L |
| Hampi Stores 2298 | Key Account | Retail | 115 | 98.26% | ₹84,024 |
| Hampi Styles | Key Account | Retail | 42 | 97.62% | ₹78,265 |

## Failure analysis

Of 664 declined attempts, 536 were business declines (2.886% of attempts — balances, PINs and limits), 70 technical (0.377%), 45 timeouts (0.242%) and 13 risk declines (0.070%).

245 attempts were re-presentations of an earlier failure (1.32% of the day); 63.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 223 | 1.201% | 1.224% |
| ZM | Invalid UPI PIN | business | Customer | 184 | 0.991% | 0.954% |
| ZA | Transaction declined by customer | business | Customer | 60 | 0.323% | 0.328% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.178% | 0.194% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.140% | 0.177% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.129% | 0.114% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.124% | 0.137% |
| ZX | Mandate not found or revoked | business | PSP | 17 | 0.092% | 0.080% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 96 | 110 |
| Auto-reversals | 24 | 22 |
| Disputes / chargebacks | 15 | 14 |
| Value returned | ₹3.49 L | ₹1.70 L |

## Customer behaviour

14,722 distinct customers transacted (+23.3% on the 28-day median) at 1.26 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,599 | 5,428 | 1.18 | 96.61% | ₹1,386 |
| power | 3,131 | 4,563 | 1.46 | 95.62% | ₹1,887 |
| merchant_heavy | 3,427 | 4,324 | 1.26 | 96.60% | ₹1,166 |
| small_ticket | 2,107 | 2,693 | 1.28 | 96.77% | ₹570 |
| occasional | 1,197 | 1,273 | 1.06 | 96.07% | ₹1,761 |
| new | 239 | 269 | 1.13 | 96.28% | ₹813 |
| dormant_returning | 22 | 22 | 1.00 | 100.00% | ₹1,523 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

01 July ran on trend at 96.35% success and ₹2.52 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 2,041 attempts, 140% up its trailing median and 15.3% of the day's volume. 8 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-01` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=18,572, successes=17,894, failed=664, pending=14, settled_value_inr=25,204,689.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=2,041; own_median=852; z=11.3
- headline: attempts=18,572; trailing_median=14,446; z=3.52
- geography: region=North; attempts=4,825; own_median=3,624; z=4.48
- psps: payer_psp=PhonePe; attempts=8,688; own_median=6,835; z=2.82
- banks: payer_bank=State Bank of India; attempts=5,895; own_median=4,534.5; z=3.27
- psps: payer_psp=Google Pay; attempts=6,219; own_median=4,781.5; z=3.07
- geography: region=South; attempts=5,428; own_median=4,280.5; z=2.96
- products: product_name=UPI Lite; attempts=3,266; own_median=2,170; z=3.66
- categories: mcc_category=Food & Beverage; attempts=3,166; own_median=2,527; z=3.01
- geography: region=West; attempts=4,574; own_median=3,579; z=2.67

Refs: enterprise_data/warehouse/transactions, RPT-D177-DAILY, enterprise_data/warehouse/reference/incidents.parquet
