---
id: RPT-D89-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-03T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 03 Apr 2026)

**Report ID:** RPT-D89-DAILY · **Day 89 of 206** · **Derived from:** 12,881 transaction rows queried live from the warehouse

## Summary

The rail took **12,881 payment attempts** on Friday 03 April 2026 (Working day) and settled **₹1.83 Cr** across 12,389 successful payments. Volume was +7.8% on yesterday and +5.1% on the same weekday last week. Success closed at **96.18%**, above the trailing 28-day median of 95.84%.

Category Bills carried 1,375 attempts, 98% up its trailing median and 16.0% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,881 | +7.8% | +5.1% | 12,681 |
| Successful payments | 12,389 | +8.0% | +5.6% | 12,183 |
| Success rate | 96.18% | +0.15pp | +0.50pp | 96.07% |
| Settled value | ₹1.83 Cr | +13.2% | +22.8% | ₹1.74 Cr |
| Average ticket | ₹1,479 | +4.8% | +16.3% | ₹1,425 |
| Technical declines | 0.365% | −0.07pp | +0.06pp | 0.410% |
| Business declines | 2.795% | −0.25pp | −0.73pp | 2.936% |
| Risk declines | 0.155% | +0.03pp | +0.08pp | 0.136% |
| Timeout declines | 0.357% | +0.09pp | +0.03pp | 0.327% |
| Retry share | 1.02% | −0.12pp | −1.89pp | 1.17% |
| Latency p95 | 1,244 ms | −3.6% | −6.4% | 1,272 ms |
| Active customers | 10,670 | +6.3% | +4.1% | 10,551 |
| Active merchants | 1,397 | +3.6% | +4.6% | 1,380 |

## What moved

- Category Bills carried 1,375 attempts, 98% up its trailing median and 16.0% of the day's volume.
- Product UPI Circle is compounding — attempts up 38% across the trailing window to 278 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 38% across the trailing window to 195 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,299 | 33.4% | 95.23% | ₹46.93 L | −1.6% |
| UPI Person to Merchant | 3,695 | 28.7% | 96.48% | ₹36.81 L | +8.1% |
| UPI QR Payments | 2,159 | 16.8% | 96.80% | ₹9.38 L | +3.7% |
| UPI Lite | 1,203 | 9.3% | 99.33% | ₹1.20 L | +30.2% |
| RuPay Credit on UPI | 341 | 2.6% | 96.19% | ₹30.97 L | +36.7% |
| UPI AutoPay | 302 | 2.3% | 90.73% | ₹5.68 L | −4.9% |
| UPI Circle | 278 | 2.2% | 96.40% | ₹2.67 L | +29.9% |
| Credit on UPI | 195 | 1.5% | 95.90% | ₹19.41 L | +15.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,135 | 96.37% | 95.82% | ₹49.31 L | normal |
| HDFC Bank | 1,409 | 96.31% | 95.59% | ₹20.73 L | normal |
| Bank of Baroda | 970 | 96.91% | 96.02% | ₹22.57 L | normal |
| Union Bank of India | 910 | 96.26% | 95.75% | ₹10.94 L | normal |
| Axis Bank | 794 | 95.34% | 95.83% | ₹12.44 L | normal |
| ICICI Bank | 765 | 95.29% | 95.86% | ₹8.84 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,927 | 95.93% | 95.88% | ₹77.96 L | normal |
| Google Pay | 4,358 | 96.26% | 95.76% | ₹70.51 L | normal |
| Paytm | 1,066 | 97.00% | 96.03% | ₹13.34 L | normal |
| Navi | 498 | 95.78% | 95.67% | ₹5.01 L | normal |
| SuperMoney | 246 | 93.09% | 94.95% | ₹2.44 L | normal |
| FamApp | 124 | 95.16% | 97.13% | ₹1.54 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,218 | 97.33% | ₹39.07 L |
| Food & Beverage | 2,020 | 97.08% | ₹10.29 L |
| Bills | 1,375 | 95.27% | ₹14.68 L |
| Mobility | 858 | 97.55% | ₹4.39 L |
| Healthcare | 411 | 97.08% | ₹6.35 L |
| Digital | 290 | 93.79% | ₹1.56 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,850 | 29.9% | 96.42% | ₹53.62 L |
| North | 3,206 | 24.9% | 96.13% | ₹44.11 L |
| West | 3,203 | 24.9% | 96.44% | ₹47.00 L |
| East | 1,544 | 12.0% | 96.05% | ₹26.04 L |
| Central | 1,078 | 8.4% | 94.90% | ₹12.53 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 96.88% | ₹2.41 L |
| Ujjwal Water Board | Key Account | Bills | 63 | 95.24% | ₹1.63 L |
| Rapid Bazaar | Key Account | Retail | 318 | 98.11% | ₹1.55 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 97.06% | ₹1.55 L |
| Hampi Styles | Key Account | Retail | 49 | 97.96% | ₹1.28 L |
| Girnar Connect | Key Account | Bills | 246 | 95.53% | ₹1.04 L |
| Urban Boutique | Key Account | Retail | 86 | 94.19% | ₹75,965 |
| Yamuna Restaurant | Key Account | Food & Beverage | 63 | 100.00% | ₹70,781 |

## Failure analysis

Of 473 declined attempts, 360 were business declines (2.795% of attempts — balances, PINs and limits), 47 technical (0.365%), 46 timeouts (0.357%) and 20 risk declines (0.155%).

131 attempts were re-presentations of an earlier failure (1.02% of the day); 69.5% of them succeeded.

- Decline code BT (Acquirer / NPCI switch timeout) fired 21 times — 0.163% of attempts against a trailing 0.102%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.203% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 102 | 0.792% | 1.081% |
| ZA | Transaction declined by customer | business | Customer | 59 | 0.458% | 0.364% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.194% | 0.224% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 21 | 0.163% | 0.102% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.155% | 0.155% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.140% | 0.190% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.132% | 0.111% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 72 | 78 |
| Auto-reversals | 22 | 24 |
| Disputes / chargebacks | 14 | 10 |
| Value returned | ₹1.07 L | ₹1.33 L |

## Customer behaviour

10,670 distinct customers transacted (+7.3% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,174 | 3,670 | 1.16 | 96.21% | ₹1,695 |
| power | 2,259 | 3,052 | 1.35 | 96.20% | ₹1,745 |
| merchant_heavy | 2,476 | 2,953 | 1.19 | 96.17% | ₹1,199 |
| small_ticket | 1,670 | 2,040 | 1.22 | 96.67% | ₹546 |
| occasional | 858 | 910 | 1.06 | 95.16% | ₹1,986 |
| new | 197 | 219 | 1.11 | 95.89% | ₹1,274 |
| dormant_returning | 36 | 37 | 1.03 | 91.89% | ₹1,202 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-PSP-0028** (Sev-3) — Axis Mobile app release regression, scoped to Axis Mobile between 19:00 and 23:00. A Axis Mobile client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **REG-0068** (Sev-3) — UPI Lite per-transaction cap raised to ₹1,000, scoped to UPI_LITE. The Lite per-transaction cap was raised, moving a band of small-ticket payments off the full UPI rail onto Lite. Lite volume steps up permanently and average ticket rises.

## Risks and opportunities

### Risks

- Decline code BT (Acquirer / NPCI switch timeout) fired 21 times — 0.163% of attempts against a trailing 0.102%. Owner: NPCI.

### Opportunities

- Product UPI Circle is compounding — attempts up 38% across the trailing window to 278 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 38% across the trailing window to 195 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

03 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 96.18% success against a 95.84% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-03` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,881, successes=12,389, failed=473, pending=19, settled_value_inr=18,329,485.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- categories: mcc_category=Bills; attempts=1,375; own_median=694.5; z=7.65
- products: product_name=UPI Circle; attempts=278; window_growth_pct=38.4; success_rate=96.4
- products: product_name=Credit on UPI; attempts=195; window_growth_pct=37.9; success_rate=95.9
- failures: failure_code=BT; count=21; rate_pct=0.16; trailing_rate_pct=0.1; owner=NPCI; z=2.37
- incidents: event_id=INC-PSP-0028; kind=psp_degradation; severity=Sev-3; window=2026-04-02 to 2026-04-05; success_impact_pp=-3.75; volume_impact_pct=-5.87
- banks: payer_bank=IDFC First Bank; attempts=355; success_rate=98.87; own_median=95.51; z=2.32
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41

Refs: enterprise_data/warehouse/transactions, RPT-D88-DAILY, enterprise_data/warehouse/reference/incidents.parquet
