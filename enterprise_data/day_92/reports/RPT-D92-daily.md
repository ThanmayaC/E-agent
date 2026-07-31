---
id: RPT-D92-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-06T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 06 Apr 2026)

**Report ID:** RPT-D92-DAILY · **Day 92 of 206** · **Derived from:** 13,667 transaction rows queried live from the warehouse

## Summary

The rail took **13,667 payment attempts** on Monday 06 April 2026 (Working day) and settled **₹1.74 Cr** across 13,146 successful payments. Volume was +8.8% on yesterday and −2.3% on the same weekday last week. Success closed at **96.19%**, above the trailing 28-day median of 95.84%.

Retries reached 381 attempts (2.79% of the day, 7.6 sigma above normal). 76.9% of re-presented payments recovered, so the retry path was doing its job. 80 auto-reversals were raised, 6.9 sigma above the trailing median of 24.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,667 | +8.8% | −2.3% | 13,153 |
| Successful payments | 13,146 | +15.8% | −2.0% | 12,517 |
| Success rate | 96.19% | +5.81pp | +0.22pp | 95.12% |
| Settled value | ₹1.74 Cr | +36.4% | −4.9% | ₹1.69 Cr |
| Average ticket | ₹1,320 | +17.8% | −2.9% | ₹1,348 |
| Technical declines | 0.446% | −1.34pp | +0.04pp | 0.648% |
| Business declines | 2.780% | −0.75pp | −0.28pp | 3.010% |
| Risk declines | 0.146% | −0.08pp | −0.00pp | 0.162% |
| Timeout declines | 0.380% | −3.46pp | +0.07pp | 0.927% |
| Retry share | 2.79% | −1.73pp | +1.71pp | 1.99% |
| Latency p95 | 1,270 ms | −41.5% | +0.4% | 1,417 ms |
| Active customers | 11,227 | +10.4% | −2.4% | 10,825 |
| Active merchants | 1,426 | +3.7% | +0.7% | 1,397 |

## What moved

- Category Bills carried 1,415 attempts, 100% up its trailing median and 16.0% of the day's volume.
- Product UPI Lite is compounding — attempts up 53% across the trailing window to 1,280 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Person ran at 96.17% success on 4,826 attempts (35.3% of the day), 0.89pp up its own 28-day median.
- Product UPI Circle is compounding — attempts up 47% across the trailing window to 231 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,826 | 35.3% | 96.17% | ₹50.65 L | +11.4% |
| UPI Person to Merchant | 3,698 | 27.1% | 96.19% | ₹39.95 L | +6.8% |
| UPI QR Payments | 2,452 | 17.9% | 96.00% | ₹11.50 L | +17.8% |
| UPI Lite | 1,280 | 9.4% | 98.52% | ₹1.13 L | +36.1% |
| UPI AutoPay | 334 | 2.4% | 91.92% | ₹5.66 L | +4.7% |
| RuPay Credit on UPI | 288 | 2.1% | 95.49% | ₹24.55 L | +15.0% |
| UPI Circle | 231 | 1.7% | 94.81% | ₹2.38 L | +3.4% |
| Credit on UPI | 178 | 1.3% | 97.19% | ₹14.50 L | +5.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,315 | 96.34% | 95.82% | ₹56.09 L | normal |
| HDFC Bank | 1,570 | 96.18% | 95.53% | ₹18.43 L | normal |
| Bank of Baroda | 1,031 | 96.51% | 96.02% | ₹10.62 L | normal |
| Union Bank of India | 944 | 96.50% | 95.64% | ₹11.30 L | normal |
| ICICI Bank | 827 | 96.37% | 95.73% | ₹7.39 L | normal |
| Axis Bank | 790 | 95.95% | 95.78% | ₹7.73 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,439 | 96.40% | 95.88% | ₹77.03 L | normal |
| Google Pay | 4,543 | 96.04% | 95.68% | ₹57.62 L | normal |
| Paytm | 1,122 | 95.19% | 95.97% | ₹15.07 L | normal |
| Navi | 507 | 96.45% | 95.67% | ₹5.98 L | normal |
| SuperMoney | 290 | 97.24% | 94.77% | ₹7.60 L | ⚠ outlier |
| BHIM | 139 | 96.40% | 95.88% | ₹1.58 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,280 | 96.43% | ₹35.54 L |
| Food & Beverage | 2,066 | 96.18% | ₹11.20 L |
| Bills | 1,415 | 96.47% | ₹15.84 L |
| Mobility | 961 | 96.77% | ₹5.84 L |
| Healthcare | 421 | 96.91% | ₹2.94 L |
| Digital | 295 | 93.56% | ₹1.82 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,018 | 29.4% | 96.54% | ₹52.74 L |
| North | 3,486 | 25.5% | 95.50% | ₹49.04 L |
| West | 3,360 | 24.6% | 96.31% | ₹41.43 L |
| East | 1,725 | 12.6% | 96.41% | ₹19.63 L |
| Central | 1,078 | 7.9% | 96.38% | ₹10.72 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 85 | 97.65% | ₹1.69 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 75 | 92.00% | ₹1.50 L |
| Vega Electronics | Large | Retail | 24 | 95.83% | ₹1.47 L |
| Vasant Wardrobe | Key Account | Retail | 48 | 91.67% | ₹1.30 L |
| Swift Grill | Large | Food & Beverage | 51 | 94.12% | ₹1.26 L |
| Hampi Stores 2298 | Key Account | Retail | 112 | 96.43% | ₹1.18 L |
| Rapid Bazaar | Key Account | Retail | 325 | 96.31% | ₹1.13 L |
| Girnar Connect | Key Account | Bills | 236 | 95.34% | ₹82,283 |

## Failure analysis

Of 513 declined attempts, 380 were business declines (2.780% of attempts — balances, PINs and limits), 61 technical (0.446%), 52 timeouts (0.380%) and 20 risk declines (0.146%).

381 attempts were re-presentations of an earlier failure (2.79% of the day); 76.9% of them succeeded.

- Retries reached 381 attempts (2.79% of the day, 7.6 sigma above normal). 76.9% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.134% | 1.341% |
| ZM | Invalid UPI PIN | business | Customer | 132 | 0.966% | 1.056% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.351% | 0.363% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.220% | 0.224% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.212% | 0.191% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 27 | 0.198% | 0.155% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.124% | 0.116% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.110% | 0.117% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 90 | 76 |
| Auto-reversals | 80 | 24 |
| Disputes / chargebacks | 9 | 10 |
| Value returned | ₹1.98 L | ₹1.40 L |

## Customer behaviour

11,227 distinct customers transacted (+12.3% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,474 | 4,001 | 1.15 | 96.30% | ₹1,397 |
| power | 2,356 | 3,238 | 1.37 | 95.46% | ₹1,963 |
| merchant_heavy | 2,531 | 3,086 | 1.22 | 96.60% | ₹885 |
| small_ticket | 1,721 | 2,134 | 1.24 | 96.58% | ₹523 |
| occasional | 896 | 946 | 1.06 | 95.88% | ₹1,322 |
| new | 224 | 237 | 1.06 | 96.62% | ₹1,272 |
| dormant_returning | 25 | 25 | 1.00 | 96.00% | ₹518 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 80 auto-reversals were raised, 6.9 sigma above the trailing median of 24.
- Product UPI Circle is compounding — attempts up 47% across the trailing window to 231 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Lite is compounding — attempts up 53% across the trailing window to 1,280 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

06 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 96.19% success against a 95.84% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-06` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,667, successes=13,146, failed=513, pending=8, settled_value_inr=17,356,771.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=381; retry_share_pct=2.79; recovery_pct=76.9; z=7.55
- adjustments: reversals=80; trailing_median=23.5; z=6.93
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- categories: mcc_category=Bills; attempts=1,415; own_median=706; z=6.09
- products: product_name=UPI Lite; attempts=1,280; window_growth_pct=53; success_rate=98.52
- products: product_name=UPI Person to Person; attempts=4,826; success_rate=96.17; own_median=95.28; z=2.24
- products: product_name=UPI Circle; attempts=231; window_growth_pct=47.1; success_rate=94.81
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41

Refs: enterprise_data/warehouse/transactions, RPT-D91-DAILY, enterprise_data/warehouse/reference/incidents.parquet
