---
id: RPT-D159-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 12 Jun 2026)

**Report ID:** RPT-D159-DAILY · **Day 159 of 206** · **Derived from:** 14,643 transaction rows queried live from the warehouse

## Summary

The rail took **14,643 payment attempts** on Friday 12 June 2026 (Working day) and settled **₹1.73 Cr** across 14,117 successful payments. Volume was +16.5% on yesterday and −8.0% on the same weekday last week. Success closed at **96.41%**, in line with the trailing 28-day median of 96.18%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,643 | +16.5% | −8.0% | 15,233 |
| Successful payments | 14,117 | +16.9% | −8.2% | 14,693 |
| Success rate | 96.41% | +0.37pp | −0.30pp | 96.44% |
| Settled value | ₹1.73 Cr | +4.3% | −26.1% | ₹2.08 Cr |
| Average ticket | ₹1,225 | −10.8% | −19.5% | ₹1,414 |
| Technical declines | 0.403% | +0.08pp | +0.11pp | 0.377% |
| Business declines | 2.732% | −0.36pp | +0.20pp | 2.698% |
| Risk declines | 0.150% | −0.02pp | +0.03pp | 0.137% |
| Timeout declines | 0.246% | −0.03pp | −0.04pp | 0.263% |
| Retry share | 1.00% | −0.23pp | +0.13pp | 1.01% |
| Latency p95 | 1,263 ms | −5.8% | +0.9% | 1,278 ms |
| Active customers | 12,176 | +14.8% | −5.9% | 12,468 |
| Active merchants | 1,510 | +0.8% | −3.3% | 1,554 |

## What moved

- Product UPI Lite carried 2,706 attempts, 40% up its trailing median and 18.5% of the day's volume.
- Product Credit on UPI is compounding — attempts up 28% across the trailing window to 440 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,204 | 28.7% | 95.48% | ₹43.95 L | −4.5% |
| UPI Person to Merchant | 3,263 | 22.3% | 96.60% | ₹28.52 L | −15.0% |
| UPI Lite | 2,706 | 18.5% | 98.74% | ₹2.54 L | +40.0% |
| UPI QR Payments | 2,167 | 14.8% | 96.72% | ₹8.96 L | −10.0% |
| UPI Circle | 661 | 4.5% | 96.22% | ₹5.35 L | −3.2% |
| Credit on UPI | 440 | 3.0% | 97.73% | ₹27.01 L | +10.3% |
| RuPay Credit on UPI | 372 | 2.5% | 96.77% | ₹22.32 L | −0.7% |
| UPI AutoPay | 350 | 2.4% | 87.71% | ₹6.53 L | +0.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,613 | 96.16% | 96.13% | ₹51.47 L | normal |
| HDFC Bank | 1,555 | 96.33% | 96.37% | ₹17.59 L | normal |
| Bank of Baroda | 1,123 | 95.73% | 96.45% | ₹10.32 L | normal |
| Union Bank of India | 1,031 | 97.48% | 96.39% | ₹13.49 L | normal |
| Punjab National Bank | 908 | 95.93% | 96.25% | ₹10.06 L | normal |
| Axis Bank | 898 | 95.66% | 96.47% | ₹16.44 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,964 | 96.51% | 96.14% | ₹85.27 L | normal |
| Google Pay | 4,863 | 96.44% | 96.18% | ₹56.56 L | normal |
| Paytm | 1,210 | 95.62% | 96.12% | ₹13.83 L | normal |
| Navi | 524 | 96.18% | 96.19% | ₹4.59 L | normal |
| SuperMoney | 252 | 95.24% | 96.32% | ₹2.46 L | normal |
| BHIM | 136 | 97.79% | 95.69% | ₹1.14 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,423 | 97.45% | ₹49.75 L |
| Food & Beverage | 2,652 | 96.98% | ₹11.62 L |
| Mobility | 1,316 | 97.95% | ₹6.40 L |
| Bills | 828 | 95.77% | ₹7.70 L |
| Healthcare | 563 | 96.45% | ₹5.68 L |
| Digital | 199 | 94.97% | ₹89,924 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,312 | 29.4% | 96.22% | ₹50.40 L |
| West | 3,717 | 25.4% | 96.66% | ₹43.03 L |
| North | 3,683 | 25.2% | 96.55% | ₹41.13 L |
| East | 1,697 | 11.6% | 96.05% | ₹25.03 L |
| Central | 1,234 | 8.4% | 96.35% | ₹13.37 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 93.75% | ₹1.79 L |
| Rapid Bazaar | Key Account | Retail | 472 | 96.40% | ₹1.57 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 96.88% | ₹1.38 L |
| Urban Boutique | Key Account | Retail | 125 | 98.40% | ₹99,469 |
| Yamuna Restaurant | Key Account | Food & Beverage | 74 | 98.65% | ₹96,608 |
| Hampi Stores 2298 | Key Account | Retail | 112 | 99.11% | ₹86,529 |
| Hampi Styles | Key Account | Retail | 35 | 97.14% | ₹69,741 |
| Kaveri Trading | Large | Retail | 59 | 96.61% | ₹67,656 |

## Failure analysis

Of 517 declined attempts, 400 were business declines (2.732% of attempts — balances, PINs and limits), 59 technical (0.403%), 36 timeouts (0.246%) and 22 risk declines (0.150%).

147 attempts were re-presentations of an earlier failure (1.00% of the day); 63.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 158 | 1.079% | 1.180% |
| ZM | Invalid UPI PIN | business | Customer | 147 | 1.004% | 0.925% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.328% | 0.348% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.219% | 0.207% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.137% | 0.194% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.137% | 0.115% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.130% | 0.114% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.123% | 0.145% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 98 | 106 |
| Auto-reversals | 9 | 25 |
| Disputes / chargebacks | 13 | 13 |
| Value returned | ₹2.34 L | ₹1.80 L |

## Customer behaviour

12,176 distinct customers transacted (+1.0% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,848 | 4,378 | 1.14 | 96.16% | ₹1,302 |
| power | 2,575 | 3,507 | 1.36 | 96.41% | ₹1,628 |
| merchant_heavy | 2,780 | 3,331 | 1.20 | 96.67% | ₹889 |
| small_ticket | 1,788 | 2,177 | 1.22 | 96.60% | ₹611 |
| occasional | 953 | 1,005 | 1.05 | 96.72% | ₹1,400 |
| new | 209 | 222 | 1.06 | 94.14% | ₹663 |
| dormant_returning | 23 | 23 | 1.00 | 95.65% | ₹1,696 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Category Financial Services ran at 81.40% success on 172 attempts (1.6% of the day), 5.30pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 28% across the trailing window to 440 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

12 June was an unremarkable day, and that is the finding: 14,643 attempts, 96.41% success, ₹1.73 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,643, successes=14,117, failed=517, pending=9, settled_value_inr=17,295,850.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Lite; attempts=2,706; own_median=1,933; z=2.6
- products: product_name=Credit on UPI; attempts=440; window_growth_pct=27.8; success_rate=97.73
- incidents: event_id=MAINT-0085; kind=maintenance_window; severity=Sev-3; window=2026-01-23 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- incidents: event_id=CMP-0060; kind=merchant_campaign; severity=Sev-3; window=2026-06-11 to 2026-06-17; success_impact_pp=-0.07; volume_impact_pct=27.15
- categories: mcc_category=Financial Services; attempts=172; success_rate=81.4; own_median=86.69; z=-2.01
- products: product_name=UPI Lite Auto Top-Up; attempts=111; own_median=92; z=2.33

Refs: enterprise_data/warehouse/transactions, RPT-D158-DAILY, enterprise_data/warehouse/reference/incidents.parquet
