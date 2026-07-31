---
id: RPT-D97-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 11 Apr 2026)

**Report ID:** RPT-D97-DAILY · **Day 97 of 206** · **Derived from:** 13,024 transaction rows queried live from the warehouse

## Summary

The rail took **13,024 payment attempts** on Saturday 11 April 2026 (Weekend) and settled **₹1.55 Cr** across 12,491 successful payments. Volume was +0.7% on yesterday and −11.1% on the same weekday last week. Success closed at **95.91%**, in line with the trailing 28-day median of 95.94%.

96 refunds were raised, 2.9 sigma above the trailing median of 74.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,024 | +0.7% | −11.1% | 13,050 |
| Successful payments | 12,491 | +0.3% | −11.1% | 12,469 |
| Success rate | 95.91% | −0.33pp | −0.04pp | 95.53% |
| Settled value | ₹1.55 Cr | −13.7% | −19.7% | ₹1.69 Cr |
| Average ticket | ₹1,242 | −13.9% | −9.7% | ₹1,350 |
| Technical declines | 0.346% | +0.01pp | −0.08pp | 0.537% |
| Business declines | 3.110% | +0.10pp | +0.17pp | 2.993% |
| Risk declines | 0.169% | +0.08pp | −0.02pp | 0.144% |
| Timeout declines | 0.346% | +0.09pp | −0.01pp | 0.670% |
| Retry share | 1.14% | +0.05pp | +0.02pp | 1.61% |
| Latency p95 | 1,211 ms | −6.6% | −2.9% | 1,347 ms |
| Active customers | 10,845 | +1.1% | −8.8% | 10,783 |
| Active merchants | 1,373 | −0.3% | −4.7% | 1,391 |

## What moved

- Product UPI International is compounding — attempts up 43% across the trailing window to 111 today, with success holding, so the growth is healthy and worth funding.
- Product RuPay Credit on UPI is compounding — attempts up 37% across the trailing window to 195 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,612 | 35.4% | 94.95% | ₹49.34 L | +4.3% |
| UPI Person to Merchant | 3,308 | 25.4% | 95.92% | ₹32.85 L | −5.2% |
| UPI QR Payments | 2,445 | 18.8% | 96.85% | ₹10.33 L | +13.1% |
| UPI Lite | 1,311 | 10.1% | 99.24% | ₹1.12 L | +26.0% |
| UPI Circle | 354 | 2.7% | 96.89% | ₹2.86 L | +50.6% |
| UPI AutoPay | 329 | 2.5% | 92.71% | ₹5.55 L | +3.0% |
| RuPay Credit on UPI | 195 | 1.5% | 94.36% | ₹14.05 L | −24.1% |
| Credit on UPI | 119 | 0.9% | 91.60% | ₹9.97 L | −33.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,060 | 96.13% | 95.96% | ₹46.25 L | normal |
| HDFC Bank | 1,431 | 96.23% | 95.59% | ₹15.49 L | normal |
| Bank of Baroda | 966 | 94.62% | 95.85% | ₹11.11 L | normal |
| Union Bank of India | 866 | 96.19% | 95.86% | ₹11.75 L | normal |
| Axis Bank | 824 | 95.63% | 95.83% | ₹7.86 L | normal |
| ICICI Bank | 811 | 96.55% | 95.85% | ₹8.77 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,105 | 95.81% | 95.93% | ₹67.83 L | normal |
| Google Pay | 4,328 | 95.63% | 95.76% | ₹58.42 L | normal |
| Paytm | 1,060 | 96.98% | 96.01% | ₹14.73 L | normal |
| Navi | 488 | 97.54% | 95.88% | ₹5.10 L | normal |
| SuperMoney | 246 | 94.31% | 95.26% | ₹2.23 L | normal |
| BHIM | 125 | 96.80% | 96.46% | ₹1.09 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,411 | 96.16% | ₹31.89 L |
| Food & Beverage | 2,248 | 97.60% | ₹10.07 L |
| Mobility | 987 | 96.76% | ₹5.81 L |
| Bills | 726 | 97.11% | ₹7.15 L |
| Healthcare | 448 | 95.98% | ₹3.60 L |
| Digital | 210 | 96.19% | ₹1.69 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,818 | 29.3% | 95.84% | ₹44.19 L |
| North | 3,320 | 25.5% | 96.08% | ₹41.91 L |
| West | 3,277 | 25.2% | 95.97% | ₹40.66 L |
| East | 1,525 | 11.7% | 95.34% | ₹19.30 L |
| Central | 1,084 | 8.3% | 96.22% | ₹9.02 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 336 | 97.02% | ₹1.54 L |
| Vega Electronics | Large | Retail | 25 | 88.00% | ₹1.42 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 96.88% | ₹1.27 L |
| Urban Boutique | Key Account | Retail | 127 | 95.28% | ₹1.05 L |
| Ujjwal Water Board | Key Account | Bills | 37 | 94.59% | ₹81,093 |
| Hampi Stores 2298 | Key Account | Retail | 89 | 96.63% | ₹72,855 |
| Yamuna Restaurant | Key Account | Food & Beverage | 49 | 91.84% | ₹60,121 |
| Girnar Connect | Key Account | Bills | 120 | 96.67% | ₹54,398 |

## Failure analysis

Of 517 declined attempts, 405 were business declines (3.110% of attempts — balances, PINs and limits), 45 technical (0.346%), 45 timeouts (0.346%) and 22 risk declines (0.169%).

148 attempts were re-presentations of an earlier failure (1.14% of the day); 66.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 164 | 1.259% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 0.967% | 1.015% |
| ZA | Transaction declined by customer | business | Customer | 58 | 0.445% | 0.358% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.261% | 0.220% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 27 | 0.207% | 0.159% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.138% | 0.113% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.138% | 0.190% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.100% | 0.108% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 96 | 74 |
| Auto-reversals | 20 | 24 |
| Disputes / chargebacks | 14 | 10 |
| Value returned | ₹2.18 L | ₹1.47 L |

## Customer behaviour

10,845 distinct customers transacted (+4.4% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,364 | 3,863 | 1.15 | 95.42% | ₹1,382 |
| power | 2,248 | 3,035 | 1.35 | 96.28% | ₹1,599 |
| merchant_heavy | 2,434 | 2,920 | 1.20 | 95.92% | ₹1,040 |
| small_ticket | 1,703 | 2,054 | 1.21 | 96.01% | ₹504 |
| occasional | 864 | 910 | 1.05 | 96.37% | ₹1,152 |
| new | 197 | 206 | 1.05 | 95.63% | ₹855 |
| dormant_returning | 35 | 36 | 1.03 | 100.00% | ₹614 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- 96 refunds were raised, 2.9 sigma above the trailing median of 74.
- Product RuPay Credit on UPI is compounding — attempts up 37% across the trailing window to 195 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Category Services ran at 88.57% success on 105 attempts (1.2% of the day), 7.14pp down its own 28-day median.
- Product Credit on UPI ran at 91.60% success on 119 attempts (0.9% of the day), 3.50pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 43% across the trailing window to 111 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

11 April ran on trend at 95.91% success and ₹1.55 Cr settled. The movement worth carrying forward is in money moving back: 96 refunds were raised, 2.9 sigma above the trailing median of 74. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,024, successes=12,491, failed=517, pending=16, settled_value_inr=15,507,947.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: refunds=96; trailing_median=74.5; z=2.9
- products: product_name=UPI International; attempts=111; window_growth_pct=42.9; success_rate=97.3
- products: product_name=RuPay Credit on UPI; attempts=195; window_growth_pct=37.1; success_rate=94.36
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=MAINT-0086; kind=maintenance_window; severity=Sev-3; window=2026-01-11 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- categories: mcc_category=Services; attempts=105; success_rate=88.57; own_median=95.71; z=-2.97
- products: product_name=Credit on UPI; attempts=119; success_rate=91.6; own_median=95.1; z=-2.1

Refs: enterprise_data/warehouse/transactions, RPT-D96-DAILY, enterprise_data/warehouse/reference/incidents.parquet
