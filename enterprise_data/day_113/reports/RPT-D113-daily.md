---
id: RPT-D113-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 27 Apr 2026)

**Report ID:** RPT-D113-DAILY · **Day 113 of 206** · **Derived from:** 12,378 transaction rows queried live from the warehouse

## Summary

The rail took **12,378 payment attempts** on Monday 27 April 2026 (Working day) and settled **₹1.60 Cr** across 11,807 successful payments. Volume was +14.1% on yesterday and −22.2% on the same weekday last week. Success closed at **95.39%**, below the trailing 28-day median of 95.88%.

Decline code U28 (Remitter bank unavailable) fired 27 times — 0.218% of attempts against a trailing 0.116%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,378 | +14.1% | −22.2% | 12,690 |
| Successful payments | 11,807 | +14.3% | −23.0% | 12,096 |
| Success rate | 95.39% | +0.14pp | −0.97pp | 95.28% |
| Settled value | ₹1.60 Cr | +25.0% | −23.4% | ₹1.63 Cr |
| Average ticket | ₹1,356 | +9.3% | −0.5% | ₹1,350 |
| Technical declines | 0.622% | +0.11pp | +0.18pp | 0.585% |
| Business declines | 3.474% | −0.33pp | +0.80pp | 3.220% |
| Risk declines | 0.113% | +0.00pp | −0.01pp | 0.141% |
| Timeout declines | 0.339% | +0.15pp | +0.02pp | 0.653% |
| Retry share | 1.45% | +0.05pp | +0.49pp | 1.63% |
| Latency p95 | 1,287 ms | +6.1% | +1.3% | 1,333 ms |
| Active customers | 10,343 | +11.2% | −19.1% | 10,546 |
| Active merchants | 1,394 | +2.0% | −5.8% | 1,387 |

## What moved

- Product UPI Circle is compounding — attempts up 31% across the trailing window to 333 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,387 | 35.4% | 94.62% | ₹46.25 L | +1.1% |
| UPI Person to Merchant | 2,934 | 23.7% | 95.57% | ₹26.86 L | −14.5% |
| UPI QR Payments | 2,026 | 16.4% | 96.59% | ₹8.56 L | −6.7% |
| UPI Lite | 1,322 | 10.7% | 98.79% | ₹1.22 L | +15.5% |
| UPI Circle | 333 | 2.7% | 96.10% | ₹2.75 L | +14.2% |
| RuPay Credit on UPI | 333 | 2.7% | 95.80% | ₹16.90 L | +4.1% |
| UPI AutoPay | 324 | 2.6% | 84.57% | ₹5.45 L | +0.5% |
| Credit on UPI | 320 | 2.6% | 95.94% | ₹21.92 L | +44.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,875 | 95.28% | 95.83% | ₹60.64 L | normal |
| HDFC Bank | 1,326 | 96.46% | 95.95% | ₹14.87 L | normal |
| Bank of Baroda | 993 | 96.37% | 95.83% | ₹11.84 L | normal |
| Union Bank of India | 858 | 93.71% | 95.41% | ₹9.05 L | normal |
| Canara Bank | 757 | 94.32% | 96.07% | ₹9.22 L | ⚠ outlier |
| Axis Bank | 741 | 95.82% | 95.93% | ₹7.86 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,919 | 95.08% | 95.78% | ₹75.35 L | normal |
| Google Pay | 4,023 | 95.58% | 95.59% | ₹52.64 L | normal |
| Paytm | 1,011 | 96.74% | 95.61% | ₹13.91 L | normal |
| Navi | 436 | 94.72% | 96.40% | ₹6.94 L | normal |
| SuperMoney | 251 | 93.63% | 95.32% | ₹2.62 L | normal |
| FamApp | 113 | 97.35% | 95.89% | ₹87,134 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,070 | 95.99% | ₹35.76 L |
| Food & Beverage | 1,823 | 96.93% | ₹9.09 L |
| Bills | 1,092 | 95.79% | ₹11.44 L |
| Mobility | 926 | 96.98% | ₹4.67 L |
| Healthcare | 421 | 97.15% | ₹5.32 L |
| Digital | 231 | 90.04% | ₹1.19 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,608 | 29.1% | 94.93% | ₹47.83 L |
| West | 3,125 | 25.2% | 95.74% | ₹43.34 L |
| North | 3,064 | 24.8% | 95.20% | ₹37.89 L |
| East | 1,517 | 12.3% | 95.85% | ₹18.41 L |
| Central | 1,064 | 8.6% | 95.77% | ₹12.60 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 37 | 89.19% | ₹2.19 L |
| Hampi Styles | Key Account | Retail | 31 | 96.77% | ₹1.63 L |
| Vasant Wardrobe | Key Account | Retail | 63 | 95.24% | ₹1.37 L |
| Rapid Bazaar | Key Account | Retail | 298 | 96.64% | ₹1.34 L |
| Hampi Stores 2298 | Key Account | Retail | 104 | 97.12% | ₹91,312 |
| Urban Boutique | Key Account | Retail | 72 | 93.06% | ₹85,510 |
| Ujjwal Water Board | Key Account | Bills | 42 | 97.62% | ₹82,342 |
| Yamuna Restaurant | Key Account | Food & Beverage | 53 | 98.11% | ₹73,490 |

## Failure analysis

Of 563 declined attempts, 430 were business declines (3.474% of attempts — balances, PINs and limits), 77 technical (0.622%), 42 timeouts (0.339%) and 14 risk declines (0.113%).

180 attempts were re-presentations of an earlier failure (1.45% of the day); 59.4% of them succeeded.

- Decline code U28 (Remitter bank unavailable) fired 27 times — 0.218% of attempts against a trailing 0.116%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 194 | 1.567% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 139 | 1.123% | 1.021% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.428% | 0.389% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.259% | 0.212% |
| U28 | Remitter bank unavailable | technical | Issuer | 27 | 0.218% | 0.116% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.186% | 0.220% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.145% | 0.199% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.137% | 0.109% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 81 | 82 |
| Auto-reversals | 28 | 28 |
| Disputes / chargebacks | 17 | 11 |
| Value returned | ₹1.02 L | ₹1.55 L |

## Customer behaviour

10,343 distinct customers transacted (−3.3% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,189 | 3,629 | 1.14 | 95.70% | ₹1,377 |
| power | 2,206 | 2,923 | 1.33 | 95.11% | ₹1,761 |
| merchant_heavy | 2,360 | 2,829 | 1.20 | 95.33% | ₹1,118 |
| small_ticket | 1,566 | 1,905 | 1.22 | 95.38% | ₹530 |
| occasional | 788 | 836 | 1.06 | 95.45% | ₹1,510 |
| new | 204 | 224 | 1.10 | 95.98% | ₹1,615 |
| dormant_returning | 30 | 32 | 1.07 | 84.38% | ₹2,048 |

## Operational events

- **INC-BANK-0018** (Sev-2) — Union Bank of India issuer decline spike, scoped to Union Bank of India between 09:00 and 14:00. Union Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-PSP-0027** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0050** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U28 (Remitter bank unavailable) fired 27 times — 0.218% of attempts against a trailing 0.116%. Owner: Issuer.
- Issuer Canara Bank ran at 94.32% success on 757 attempts (6.1% of the day), 1.75pp down its own 28-day median.
- Product UPI AutoPay ran at 84.57% success on 324 attempts (2.6% of the day), 5.88pp down its own 28-day median.
- Issuer IDFC First Bank ran at 92.64% success on 326 attempts (2.6% of the day), 3.42pp down its own 28-day median.
- Category Services ran at 92.39% success on 92 attempts (1.2% of the day), 3.76pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 31% across the trailing window to 333 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

27 April was an incident day: INC-BANK-0018, INC-PSP-0027 were live and the rail closed at 95.39% success against a 95.88% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,378, successes=11,807, failed=563, pending=8, settled_value_inr=16,006,965.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U28; count=27; rate_pct=0.22; trailing_rate_pct=0.12; owner=Issuer; z=4.18
- incidents: event_id=INC-BANK-0018; kind=bank_outage; severity=Sev-2; window=2026-04-27 to 2026-04-27; success_impact_pp=-15.16; volume_impact_pct=-13.45
- incidents: event_id=INC-PSP-0027; kind=psp_degradation; severity=Sev-2; window=2026-04-27 to 2026-04-30; success_impact_pp=-11.27; volume_impact_pct=-17.63
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- products: product_name=UPI Circle; attempts=333; window_growth_pct=30.6; success_rate=96.1
- banks: payer_bank=Canara Bank; attempts=757; success_rate=94.32; own_median=96.07; z=-2.17
- products: product_name=UPI AutoPay; attempts=324; success_rate=84.57; own_median=90.45; z=-2.78
- banks: payer_bank=IDFC First Bank; attempts=326; success_rate=92.64; own_median=96.06; z=-2.34
- banks: payer_bank=Kotak Mahindra Bank; attempts=422; success_rate=97.39; own_median=95.76; z=2.02
- incidents: event_id=CMP-0056; kind=merchant_campaign; severity=Sev-3; window=2026-04-24 to 2026-04-30; success_impact_pp=-0.17; volume_impact_pct=66.88

Refs: enterprise_data/warehouse/transactions, RPT-D112-DAILY, enterprise_data/warehouse/reference/incidents.parquet
