---
id: RPT-D115-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-29T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 29 Apr 2026)

**Report ID:** RPT-D115-DAILY · **Day 115 of 206** · **Derived from:** 13,571 transaction rows queried live from the warehouse

## Summary

The rail took **13,571 payment attempts** on Wednesday 29 April 2026 (Working day) and settled **₹1.94 Cr** across 13,027 successful payments. Volume was +15.0% on yesterday and +24.2% on the same weekday last week. Success closed at **95.99%**, above the trailing 28-day median of 95.53%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,571 | +15.0% | +24.2% | 12,690 |
| Successful payments | 13,027 | +16.1% | +25.2% | 12,098 |
| Success rate | 95.99% | +0.90pp | +0.75pp | 95.30% |
| Settled value | ₹1.94 Cr | +20.2% | +21.5% | ₹1.64 Cr |
| Average ticket | ₹1,492 | +3.6% | −2.9% | ₹1,358 |
| Technical declines | 0.494% | −0.12pp | −0.03pp | 0.583% |
| Business declines | 2.889% | −0.88pp | −0.63pp | 3.227% |
| Risk declines | 0.177% | +0.08pp | +0.05pp | 0.140% |
| Timeout declines | 0.309% | −0.04pp | −0.17pp | 0.630% |
| Retry share | 1.40% | −0.55pp | −0.09pp | 1.64% |
| Latency p95 | 1,278 ms | −2.1% | +2.2% | 1,330 ms |
| Active customers | 11,264 | +13.0% | +20.9% | 10,551 |
| Active merchants | 1,479 | +4.0% | +8.6% | 1,391 |

## What moved

- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 380 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 465 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,633 | 34.1% | 95.49% | ₹48.67 L | +9.9% |
| UPI Person to Merchant | 3,312 | 24.4% | 96.14% | ₹30.43 L | −0.3% |
| UPI QR Payments | 2,342 | 17.3% | 96.63% | ₹9.63 L | +8.9% |
| UPI Lite | 1,329 | 9.8% | 98.42% | ₹1.20 L | +15.8% |
| UPI Circle | 465 | 3.4% | 96.34% | ₹3.89 L | +55.5% |
| Credit on UPI | 380 | 2.8% | 93.42% | ₹39.22 L | +71.6% |
| RuPay Credit on UPI | 358 | 2.6% | 96.37% | ₹22.55 L | +11.9% |
| UPI AutoPay | 351 | 2.6% | 90.60% | ₹7.43 L | +8.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,240 | 95.97% | 95.59% | ₹56.77 L | normal |
| HDFC Bank | 1,429 | 96.85% | 95.87% | ₹17.86 L | normal |
| Bank of Baroda | 1,034 | 96.32% | 95.76% | ₹13.74 L | normal |
| Union Bank of India | 962 | 94.80% | 95.03% | ₹16.98 L | normal |
| Axis Bank | 867 | 95.96% | 95.87% | ₹13.87 L | normal |
| Punjab National Bank | 838 | 97.37% | 95.47% | ₹10.81 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,387 | 96.18% | 95.73% | ₹88.71 L | normal |
| Google Pay | 4,581 | 95.74% | 95.50% | ₹66.01 L | normal |
| Paytm | 1,089 | 95.87% | 95.36% | ₹14.96 L | normal |
| Navi | 478 | 95.19% | 96.24% | ₹6.67 L | normal |
| SuperMoney | 252 | 97.22% | 95.13% | ₹6.14 L | normal |
| YONO SBI | 125 | 94.40% | 95.69% | ₹3.42 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,288 | 96.38% | ₹37.11 L |
| Food & Beverage | 2,332 | 96.70% | ₹9.68 L |
| Bills | 1,124 | 96.53% | ₹11.07 L |
| Mobility | 1,006 | 96.42% | ₹5.23 L |
| Healthcare | 413 | 97.09% | ₹8.35 L |
| Digital | 273 | 94.14% | ₹1.47 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,984 | 29.4% | 96.06% | ₹61.26 L |
| North | 3,449 | 25.4% | 96.17% | ₹47.48 L |
| West | 3,320 | 24.5% | 95.69% | ₹49.36 L |
| East | 1,682 | 12.4% | 95.90% | ₹24.41 L |
| Central | 1,136 | 8.4% | 96.21% | ₹11.84 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 72 | 98.61% | ₹2.73 L |
| Rapid Bazaar | Key Account | Retail | 344 | 96.22% | ₹2.00 L |
| Vega Electronics | Large | Retail | 35 | 100.00% | ₹1.44 L |
| Ujjwal Water Board | Key Account | Bills | 65 | 95.38% | ₹1.23 L |
| Girnar Connect | Key Account | Bills | 183 | 94.54% | ₹82,745 |
| Urban Boutique | Key Account | Retail | 81 | 97.53% | ₹76,604 |
| Hampi Styles | Key Account | Retail | 28 | 89.29% | ₹52,423 |
| Hampi Stores 2298 | Key Account | Retail | 105 | 94.29% | ₹50,517 |

## Failure analysis

Of 525 declined attempts, 392 were business declines (2.889% of attempts — balances, PINs and limits), 67 technical (0.494%), 42 timeouts (0.309%) and 24 risk declines (0.177%).

190 attempts were re-presentations of an earlier failure (1.40% of the day); 61.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 151 | 1.113% | 1.313% |
| ZM | Invalid UPI PIN | business | Customer | 149 | 1.098% | 1.032% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.273% | 0.393% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.184% | 0.212% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.184% | 0.220% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.169% | 0.199% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.147% | 0.114% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.147% | 0.118% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 78 | 82 |
| Auto-reversals | 18 | 28 |
| Disputes / chargebacks | 9 | 11 |
| Value returned | ₹1.33 L | ₹1.46 L |

## Customer behaviour

11,264 distinct customers transacted (+9.5% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,496 | 4,026 | 1.15 | 96.00% | ₹1,549 |
| power | 2,376 | 3,186 | 1.34 | 96.20% | ₹1,778 |
| merchant_heavy | 2,519 | 3,021 | 1.20 | 95.76% | ₹1,364 |
| small_ticket | 1,735 | 2,142 | 1.23 | 96.55% | ₹685 |
| occasional | 898 | 939 | 1.05 | 95.53% | ₹1,882 |
| new | 213 | 229 | 1.08 | 93.89% | ₹519 |
| dormant_returning | 27 | 28 | 1.04 | 85.71% | ₹2,112 |

## Operational events

- **INC-PSP-0027** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **INC-PSP-0032** (Sev-3) — Google Pay app release regression, scoped to Google Pay between 19:00 and 23:00. A Google Pay client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0050** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 380 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Circle is compounding — attempts up 34% across the trailing window to 465 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

29 April was an incident day: INC-PSP-0027 was live and the rail closed at 95.99% success against a 95.53% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-29` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,571, successes=13,027, failed=525, pending=19, settled_value_inr=19,433,510.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-PSP-0027; kind=psp_degradation; severity=Sev-2; window=2026-04-27 to 2026-04-30; success_impact_pp=-11.27; volume_impact_pct=-17.63
- products: product_name=Credit on UPI; attempts=380; window_growth_pct=36.2; success_rate=93.42
- products: product_name=UPI Circle; attempts=465; window_growth_pct=34.2; success_rate=96.34
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=INC-PSP-0032; kind=psp_degradation; severity=Sev-3; window=2026-04-29 to 2026-04-30; success_impact_pp=-2.05; volume_impact_pct=-3.21
- banks: payer_bank=Punjab National Bank; attempts=838; success_rate=97.37; own_median=95.47; z=2.53
- products: product_name=UPI Circle; attempts=465; own_median=299; z=3.03
- incidents: event_id=CMP-0056; kind=merchant_campaign; severity=Sev-3; window=2026-04-24 to 2026-04-30; success_impact_pp=-0.17; volume_impact_pct=66.88
- incidents: event_id=CMP-0050; kind=merchant_campaign; severity=Sev-3; window=2026-04-27 to 2026-04-30; success_impact_pp=-0.2; volume_impact_pct=80.19
- categories: mcc_category=Digital; attempts=273; own_median=202; z=2.82

Refs: enterprise_data/warehouse/transactions, RPT-D114-DAILY, enterprise_data/warehouse/reference/incidents.parquet
