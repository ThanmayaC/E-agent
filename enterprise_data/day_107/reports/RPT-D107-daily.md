---
id: RPT-D107-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-21T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 21 Apr 2026)

**Report ID:** RPT-D107-DAILY · **Day 107 of 206** · **Derived from:** 12,921 transaction rows queried live from the warehouse

## Summary

The rail took **12,921 payment attempts** on Tuesday 21 April 2026 (Working day) and settled **₹1.81 Cr** across 12,384 successful payments. Volume was −18.8% on yesterday and +7.9% on the same weekday last week. Success closed at **95.84%**, in line with the trailing 28-day median of 95.92%.

Product UPI Circle is compounding — attempts up 57% across the trailing window to 300 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,921 | −18.8% | +7.9% | 12,970 |
| Successful payments | 12,384 | −19.2% | +8.4% | 12,365 |
| Success rate | 95.84% | −0.51pp | +0.43pp | 95.29% |
| Settled value | ₹1.81 Cr | −13.4% | +27.8% | ₹1.66 Cr |
| Average ticket | ₹1,461 | +7.2% | +17.9% | ₹1,344 |
| Technical declines | 0.519% | +0.08pp | −0.02pp | 0.589% |
| Business declines | 3.065% | +0.39pp | −0.39pp | 3.130% |
| Risk declines | 0.093% | −0.03pp | −0.05pp | 0.142% |
| Timeout declines | 0.379% | +0.06pp | +0.05pp | 0.728% |
| Retry share | 1.09% | +0.12pp | −0.40pp | 1.70% |
| Latency p95 | 1,277 ms | +0.5% | +4.3% | 1,353 ms |
| Active customers | 10,788 | −15.6% | +8.1% | 10,728 |
| Active merchants | 1,402 | −5.3% | +3.2% | 1,389 |

## What moved

- Product UPI Circle is compounding — attempts up 57% across the trailing window to 300 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 41% across the trailing window to 1,099 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,378 | 33.9% | 95.20% | ₹46.33 L | −1.0% |
| UPI Person to Merchant | 3,337 | 25.8% | 95.89% | ₹33.80 L | −3.8% |
| UPI QR Payments | 2,429 | 18.8% | 96.83% | ₹9.95 L | +12.9% |
| UPI Lite | 1,099 | 8.5% | 98.36% | ₹97,982 | +1.4% |
| RuPay Credit on UPI | 362 | 2.8% | 96.13% | ₹20.48 L | +24.0% |
| Credit on UPI | 319 | 2.5% | 93.73% | ₹24.66 L | +58.7% |
| UPI AutoPay | 305 | 2.4% | 90.16% | ₹5.54 L | −5.6% |
| UPI Circle | 300 | 2.3% | 96.67% | ₹2.43 L | +11.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,078 | 95.88% | 95.92% | ₹56.18 L | normal |
| HDFC Bank | 1,410 | 95.82% | 96.04% | ₹19.89 L | normal |
| Bank of Baroda | 997 | 95.89% | 95.85% | ₹12.65 L | normal |
| Union Bank of India | 942 | 95.01% | 95.72% | ₹13.89 L | normal |
| Axis Bank | 791 | 96.46% | 95.65% | ₹11.62 L | normal |
| Punjab National Bank | 772 | 95.60% | 95.59% | ₹13.73 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,055 | 96.25% | 95.78% | ₹89.37 L | normal |
| Google Pay | 4,359 | 95.39% | 95.63% | ₹59.80 L | normal |
| Paytm | 1,044 | 95.11% | 95.85% | ₹14.91 L | normal |
| Navi | 434 | 96.77% | 96.04% | ₹5.60 L | normal |
| SuperMoney | 255 | 96.47% | 94.47% | ₹2.76 L | normal |
| BHIM | 135 | 96.30% | 96.12% | ₹1.02 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,863 | 95.83% | ₹45.73 L |
| Food & Beverage | 2,082 | 97.21% | ₹9.47 L |
| Mobility | 887 | 96.96% | ₹4.74 L |
| Bills | 730 | 95.34% | ₹7.36 L |
| Healthcare | 386 | 98.96% | ₹8.50 L |
| Digital | 187 | 95.19% | ₹89,136 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,868 | 29.9% | 96.07% | ₹63.96 L |
| North | 3,357 | 26.0% | 95.08% | ₹44.74 L |
| West | 3,118 | 24.1% | 96.18% | ₹41.21 L |
| East | 1,458 | 11.3% | 95.75% | ₹18.79 L |
| Central | 1,120 | 8.7% | 96.52% | ₹12.26 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 38 | 97.37% | ₹2.30 L |
| Vasant Wardrobe | Key Account | Retail | 79 | 97.47% | ₹2.05 L |
| Rapid Bazaar | Key Account | Retail | 348 | 95.40% | ₹1.30 L |
| Urban Boutique | Key Account | Retail | 111 | 90.09% | ₹99,943 |
| Hampi Stores 2298 | Key Account | Retail | 129 | 93.80% | ₹78,413 |
| Girnar Connect | Key Account | Bills | 148 | 96.62% | ₹77,298 |
| Swift Grill | Large | Food & Beverage | 37 | 91.89% | ₹59,289 |
| Swift Mart 1738 | Key Account | Retail | 109 | 97.25% | ₹57,284 |

## Failure analysis

Of 524 declined attempts, 396 were business declines (3.065% of attempts — balances, PINs and limits), 67 technical (0.519%), 49 timeouts (0.379%) and 12 risk declines (0.093%).

141 attempts were re-presentations of an earlier failure (1.09% of the day); 63.8% of them succeeded.

- Decline code U69 (Beneficiary bank offline) fired 17 times — 0.132% of attempts against a trailing 0.065%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 166 | 1.285% | 1.313% |
| ZM | Invalid UPI PIN | business | Customer | 123 | 0.952% | 1.021% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.356% | 0.378% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.263% | 0.220% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 28 | 0.217% | 0.183% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.186% | 0.194% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.139% | 0.110% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.139% | 0.104% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 100 | 80 |
| Auto-reversals | 29 | 24 |
| Disputes / chargebacks | 9 | 11 |
| Value returned | ₹1.40 L | ₹1.55 L |

## Customer behaviour

10,788 distinct customers transacted (+3.8% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,294 | 3,812 | 1.16 | 95.25% | ₹1,693 |
| power | 2,249 | 3,011 | 1.34 | 95.78% | ₹1,880 |
| merchant_heavy | 2,476 | 2,953 | 1.19 | 96.21% | ₹1,080 |
| small_ticket | 1,664 | 1,980 | 1.19 | 96.31% | ₹486 |
| occasional | 860 | 902 | 1.05 | 96.23% | ₹1,648 |
| new | 208 | 224 | 1.08 | 95.54% | ₹1,442 |
| dormant_returning | 37 | 39 | 1.05 | 100.00% | ₹553 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0062** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U69 (Beneficiary bank offline) fired 17 times — 0.132% of attempts against a trailing 0.065%. Owner: Issuer.

### Opportunities

- Product UPI Circle is compounding — attempts up 57% across the trailing window to 300 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 41% across the trailing window to 1,099 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

21 April ran on trend at 95.84% success and ₹1.81 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 57% across the trailing window to 300 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-21` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,921, successes=12,384, failed=524, pending=13, settled_value_inr=18,094,910.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=300; window_growth_pct=56.7; success_rate=96.67
- products: product_name=UPI Lite; attempts=1,099; window_growth_pct=41.5; success_rate=98.36
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- failures: failure_code=U69; count=17; rate_pct=0.13; trailing_rate_pct=0.06; owner=Issuer; z=2.74
- incidents: event_id=CMP-0053; kind=merchant_campaign; severity=Sev-3; window=2026-04-14 to 2026-04-21; success_impact_pp=-0.2; volume_impact_pct=80.12
- incidents: event_id=CMP-0054; kind=merchant_campaign; severity=Sev-3; window=2026-04-15 to 2026-04-22; success_impact_pp=-0.17; volume_impact_pct=66.38
- incidents: event_id=CMP-0062; kind=merchant_campaign; severity=Sev-3; window=2026-04-20 to 2026-04-22; success_impact_pp=-0.09; volume_impact_pct=36.4

Refs: enterprise_data/warehouse/transactions, RPT-D106-DAILY, enterprise_data/warehouse/reference/incidents.parquet
