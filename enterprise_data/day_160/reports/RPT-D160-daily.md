---
id: RPT-D160-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-13T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 13 Jun 2026)

**Report ID:** RPT-D160-DAILY · **Day 160 of 206** · **Derived from:** 15,251 transaction rows queried live from the warehouse

## Summary

The rail took **15,251 payment attempts** on Saturday 13 June 2026 (Weekend) and settled **₹1.67 Cr** across 14,701 successful payments. Volume was +4.2% on yesterday and −18.2% on the same weekday last week. Success closed at **96.39%**, in line with the trailing 28-day median of 96.25%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,251 | +4.2% | −18.2% | 15,234 |
| Successful payments | 14,701 | +4.1% | −18.5% | 14,693 |
| Success rate | 96.39% | −0.01pp | −0.35pp | 96.43% |
| Settled value | ₹1.67 Cr | −3.5% | −29.6% | ₹2.05 Cr |
| Average ticket | ₹1,136 | −7.3% | −13.6% | ₹1,393 |
| Technical declines | 0.407% | +0.00pp | +0.03pp | 0.379% |
| Business declines | 2.780% | +0.05pp | +0.37pp | 2.704% |
| Risk declines | 0.072% | −0.08pp | −0.06pp | 0.132% |
| Timeout declines | 0.256% | +0.01pp | −0.01pp | 0.263% |
| Retry share | 1.02% | +0.02pp | +0.11pp | 1.01% |
| Latency p95 | 1,200 ms | −5.0% | −2.8% | 1,272 ms |
| Active customers | 12,380 | +1.7% | −15.8% | 12,461 |
| Active merchants | 1,557 | +3.1% | −5.3% | 1,555 |

## What moved

- Issuer HDFC Bank ran at 97.44% success on 1,602 attempts (10.5% of the day), 1.07pp up its own 28-day median.
- Issuer Axis Bank ran at 95.09% success on 978 attempts (6.4% of the day), 1.37pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,457 | 29.2% | 95.65% | ₹45.76 L | +1.2% |
| UPI Person to Merchant | 3,827 | 25.1% | 96.21% | ₹37.04 L | −0.2% |
| UPI QR Payments | 2,535 | 16.6% | 96.80% | ₹10.42 L | +5.3% |
| UPI Lite | 2,395 | 15.7% | 98.58% | ₹2.18 L | +23.9% |
| UPI Circle | 856 | 5.6% | 97.08% | ₹7.44 L | +25.4% |
| UPI AutoPay | 363 | 2.4% | 90.36% | ₹7.33 L | +3.9% |
| RuPay Credit on UPI | 213 | 1.4% | 95.31% | ₹12.69 L | −42.8% |
| Credit on UPI | 211 | 1.4% | 96.68% | ₹14.39 L | −47.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,790 | 96.81% | 96.18% | ₹46.75 L | normal |
| HDFC Bank | 1,602 | 97.44% | 96.37% | ₹19.94 L | ⚠ outlier |
| Bank of Baroda | 1,137 | 96.48% | 96.45% | ₹12.20 L | normal |
| Union Bank of India | 1,066 | 94.93% | 96.40% | ₹10.68 L | ⚠ outlier |
| Axis Bank | 978 | 95.09% | 96.47% | ₹12.85 L | ⚠ outlier |
| ICICI Bank | 964 | 96.37% | 96.62% | ₹9.36 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,180 | 96.28% | 96.17% | ₹73.35 L | normal |
| Google Pay | 5,039 | 96.79% | 96.29% | ₹59.54 L | normal |
| Paytm | 1,270 | 95.75% | 96.12% | ₹14.65 L | normal |
| Navi | 565 | 97.35% | 96.19% | ₹4.78 L | normal |
| SuperMoney | 281 | 95.73% | 96.32% | ₹2.81 L | normal |
| BHIM | 150 | 94.67% | 95.88% | ₹1.65 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,532 | 97.13% | ₹42.16 L |
| Food & Beverage | 2,795 | 96.96% | ₹11.60 L |
| Mobility | 1,382 | 97.32% | ₹6.93 L |
| Bills | 823 | 95.75% | ₹8.46 L |
| Healthcare | 593 | 96.96% | ₹5.54 L |
| Digital | 217 | 92.63% | ₹90,087 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,444 | 29.1% | 96.38% | ₹50.01 L |
| North | 3,892 | 25.5% | 96.56% | ₹43.23 L |
| West | 3,714 | 24.4% | 95.77% | ₹42.75 L |
| East | 1,808 | 11.9% | 96.63% | ₹18.95 L |
| Central | 1,393 | 9.1% | 97.34% | ₹12.00 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 485 | 98.97% | ₹1.88 L |
| Vega Electronics | Large | Retail | 29 | 100.00% | ₹1.70 L |
| Hampi Stores 2298 | Key Account | Retail | 112 | 95.54% | ₹1.10 L |
| Urban Boutique | Key Account | Retail | 124 | 95.97% | ₹82,707 |
| Aravalli Pharmacy | Large | Healthcare | 101 | 99.01% | ₹73,869 |
| Yamuna Restaurant | Key Account | Food & Beverage | 85 | 95.29% | ₹73,420 |
| Vasant Wardrobe | Key Account | Retail | 54 | 100.00% | ₹72,277 |
| Tejas Bites | Key Account | Food & Beverage | 200 | 100.00% | ₹62,335 |

## Failure analysis

Of 536 declined attempts, 424 were business declines (2.780% of attempts — balances, PINs and limits), 62 technical (0.407%), 39 timeouts (0.256%) and 11 risk declines (0.072%).

156 attempts were re-presentations of an earlier failure (1.02% of the day); 71.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 190 | 1.246% | 1.180% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 0.826% | 0.925% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.328% | 0.348% |
| XH | Account does not exist / frozen | business | Issuer | 36 | 0.236% | 0.209% |
| U30 | Debit failed at remitter bank | technical | Issuer | 30 | 0.197% | 0.187% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.157% | 0.143% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.111% | 0.114% |
| ZX | Mandate not found or revoked | business | PSP | 12 | 0.079% | 0.069% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 122 | 106 |
| Auto-reversals | 24 | 25 |
| Disputes / chargebacks | 13 | 13 |
| Value returned | ₹1.24 L | ₹1.80 L |

## Customer behaviour

12,380 distinct customers transacted (+2.1% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,849 | 4,478 | 1.16 | 96.40% | ₹1,091 |
| power | 2,590 | 3,589 | 1.39 | 96.80% | ₹1,578 |
| merchant_heavy | 2,890 | 3,550 | 1.23 | 95.86% | ₹942 |
| small_ticket | 1,872 | 2,385 | 1.27 | 96.39% | ₹530 |
| occasional | 956 | 1,007 | 1.05 | 96.43% | ₹1,326 |
| new | 198 | 217 | 1.10 | 98.16% | ₹875 |
| dormant_returning | 25 | 25 | 1.00 | 96.00% | ₹437 |

## Operational events

- **INC-BANK-0005** (Sev-2) — AU Small Finance Bank issuer decline spike, scoped to AU Small Finance Bank between 11:00 and 15:00. AU Small Finance Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Issuer Axis Bank ran at 95.09% success on 978 attempts (6.4% of the day), 1.37pp down its own 28-day median.
- Issuer Union Bank of India ran at 94.93% success on 1,066 attempts (7.0% of the day), 1.47pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

13 June was an incident day: INC-BANK-0005 was live and the rail closed at 96.39% success against a 96.25% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-13` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,251, successes=14,701, failed=536, pending=14, settled_value_inr=16,693,573.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0005; kind=bank_outage; severity=Sev-2; window=2026-06-13 to 2026-06-13; success_impact_pp=-14.62; volume_impact_pct=-12.97
- banks: payer_bank=HDFC Bank; attempts=1,602; success_rate=97.44; own_median=96.38; z=3.05
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- banks: payer_bank=Axis Bank; attempts=978; success_rate=95.09; own_median=96.47; z=-3.04
- banks: payer_bank=Union Bank of India; attempts=1,066; success_rate=94.93; own_median=96.4; z=-2.7
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- incidents: event_id=CMP-0060; kind=merchant_campaign; severity=Sev-3; window=2026-06-11 to 2026-06-17; success_impact_pp=-0.07; volume_impact_pct=27.15
- products: product_name=RuPay Credit on UPI; attempts=213; own_median=372.5; z=-2.87

Refs: enterprise_data/warehouse/transactions, RPT-D159-DAILY, enterprise_data/warehouse/reference/incidents.parquet
