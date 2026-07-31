---
id: RPT-D141-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 25 May 2026)

**Report ID:** RPT-D141-DAILY · **Day 141 of 206** · **Derived from:** 14,891 transaction rows queried live from the warehouse

## Summary

The rail took **14,891 payment attempts** on Monday 25 May 2026 (Working day) and settled **₹1.94 Cr** across 14,316 successful payments. Volume was +14.7% on yesterday and −5.4% on the same weekday last week. Success closed at **96.14%**, in line with the trailing 28-day median of 96.03%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,891 | +14.7% | −5.4% | 14,803 |
| Successful payments | 14,316 | +15.7% | −5.6% | 14,199 |
| Success rate | 96.14% | +0.79pp | −0.23pp | 95.92% |
| Settled value | ₹1.94 Cr | +17.9% | −12.0% | ₹1.98 Cr |
| Average ticket | ₹1,352 | +1.9% | −6.7% | ₹1,393 |
| Technical declines | 0.450% | −0.07pp | +0.02pp | 0.509% |
| Business declines | 2.921% | −0.42pp | +0.29pp | 2.934% |
| Risk declines | 0.121% | −0.05pp | +0.02pp | 0.129% |
| Timeout declines | 0.275% | −0.19pp | −0.07pp | 0.403% |
| Retry share | 1.22% | −0.07pp | +0.30pp | 1.36% |
| Latency p95 | 1,271 ms | +2.9% | −3.0% | 1,287 ms |
| Active customers | 12,239 | +11.6% | −3.7% | 12,078 |
| Active merchants | 1,515 | +2.7% | −2.9% | 1,499 |

## What moved

- Product UPI International is compounding — attempts up 44% across the trailing window to 179 today, with success holding, so the growth is healthy and worth funding.
- Category Food & Beverage ran at 97.66% success on 2,475 attempts (23.7% of the day), 0.64pp up its own 28-day median.
- Category Retail carried 4,782 attempts, 22% up its trailing median and 45.8% of the day's volume.
- Product UPI Person to Person ran at 95.71% success on 4,452 attempts (29.9% of the day), 0.57pp up its own 28-day median.
- Product UPI Circle is compounding — attempts up 33% across the trailing window to 608 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,452 | 29.9% | 95.71% | ₹48.29 L | −0.8% |
| UPI Person to Merchant | 4,141 | 27.8% | 96.18% | ₹44.24 L | +6.6% |
| UPI QR Payments | 2,457 | 16.5% | 96.74% | ₹10.27 L | +4.7% |
| UPI Lite | 1,650 | 11.1% | 98.91% | ₹1.52 L | −2.7% |
| UPI Circle | 608 | 4.1% | 96.71% | ₹4.66 L | +11.2% |
| Credit on UPI | 395 | 2.7% | 96.96% | ₹27.12 L | +11.1% |
| RuPay Credit on UPI | 361 | 2.4% | 97.23% | ₹19.58 L | −1.9% |
| UPI AutoPay | 358 | 2.4% | 84.92% | ₹6.31 L | +8.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,699 | 95.72% | 96.05% | ₹60.54 L | normal |
| HDFC Bank | 1,635 | 96.57% | 96.20% | ₹20.24 L | normal |
| Bank of Baroda | 1,176 | 96.43% | 95.81% | ₹15.60 L | normal |
| Union Bank of India | 1,038 | 95.57% | 95.49% | ₹13.94 L | normal |
| Axis Bank | 948 | 97.47% | 96.52% | ₹13.81 L | normal |
| ICICI Bank | 897 | 96.21% | 96.43% | ₹9.96 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,031 | 96.12% | 95.97% | ₹88.88 L | normal |
| Google Pay | 4,953 | 96.41% | 95.93% | ₹68.87 L | normal |
| Paytm | 1,206 | 95.11% | 96.14% | ₹13.84 L | normal |
| Navi | 561 | 95.37% | 95.43% | ₹8.09 L | normal |
| SuperMoney | 287 | 96.17% | 96.43% | ₹4.75 L | normal |
| BHIM | 152 | 97.37% | 95.87% | ₹2.70 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,782 | 96.88% | ₹59.32 L |
| Food & Beverage | 2,475 | 97.66% | ₹12.25 L |
| Mobility | 1,122 | 96.52% | ₹6.28 L |
| Bills | 801 | 93.76% | ₹9.41 L |
| Healthcare | 553 | 96.75% | ₹7.27 L |
| Digital | 222 | 91.89% | ₹83,621 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,353 | 29.2% | 96.26% | ₹60.27 L |
| North | 3,761 | 25.3% | 95.93% | ₹43.70 L |
| West | 3,688 | 24.8% | 95.77% | ₹53.60 L |
| East | 1,761 | 11.8% | 96.54% | ₹21.61 L |
| Central | 1,328 | 8.9% | 96.84% | ₹14.37 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 44 | 97.73% | ₹5.38 L |
| Vasant Wardrobe | Key Account | Retail | 87 | 94.25% | ₹4.34 L |
| Rapid Bazaar | Key Account | Retail | 490 | 97.55% | ₹2.07 L |
| Hampi Styles | Key Account | Retail | 50 | 98.00% | ₹94,135 |
| Hampi Stores 2298 | Key Account | Retail | 119 | 97.48% | ₹87,731 |
| Swift Mart 1738 | Key Account | Retail | 131 | 98.47% | ₹79,376 |
| Yamuna Restaurant | Key Account | Food & Beverage | 82 | 96.34% | ₹69,243 |
| Shakti Stores 1531 | Key Account | Retail | 105 | 94.29% | ₹64,557 |

## Failure analysis

Of 561 declined attempts, 435 were business declines (2.921% of attempts — balances, PINs and limits), 67 technical (0.450%), 41 timeouts (0.275%) and 18 risk declines (0.121%).

182 attempts were re-presentations of an earlier failure (1.22% of the day); 72.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 194 | 1.303% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 132 | 0.886% | 1.015% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.363% | 0.336% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.235% | 0.218% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.208% | 0.206% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.121% | 0.112% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.114% | 0.136% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.107% | 0.106% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 111 | 98 |
| Auto-reversals | 26 | 28 |
| Disputes / chargebacks | 11 | 13 |
| Value returned | ₹2.84 L | ₹1.88 L |

## Customer behaviour

12,239 distinct customers transacted (+4.1% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,853 | 4,440 | 1.15 | 96.28% | ₹1,374 |
| power | 2,614 | 3,560 | 1.36 | 96.21% | ₹1,744 |
| merchant_heavy | 2,755 | 3,350 | 1.22 | 96.06% | ₹1,131 |
| small_ticket | 1,812 | 2,263 | 1.25 | 95.89% | ₹682 |
| occasional | 962 | 1,012 | 1.05 | 95.85% | ₹1,454 |
| new | 209 | 232 | 1.11 | 96.55% | ₹720 |
| dormant_returning | 34 | 34 | 1.00 | 100.00% | ₹2,176 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI AutoPay ran at 84.92% success on 358 attempts (2.4% of the day), 5.48pp down its own 28-day median.
- Category Financial Services ran at 81.03% success on 174 attempts (1.7% of the day), 6.20pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 44% across the trailing window to 179 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 33% across the trailing window to 608 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

25 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 96.14% success against a 96.03% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,891, successes=14,316, failed=561, pending=14, settled_value_inr=19,356,032.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- products: product_name=UPI International; attempts=179; window_growth_pct=44.4; success_rate=95.53
- categories: mcc_category=Food & Beverage; attempts=2,475; success_rate=97.66; own_median=97.02; z=2.48
- categories: mcc_category=Retail; attempts=4,782; own_median=3,921; z=2.43
- products: product_name=UPI Person to Person; attempts=4,452; success_rate=95.71; own_median=95.14; z=2.08
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Circle; attempts=608; window_growth_pct=32.7; success_rate=96.71
- incidents: event_id=CMP-0059; kind=merchant_campaign; severity=Sev-3; window=2026-05-25 to 2026-06-01; success_impact_pp=-0.15; volume_impact_pct=59.67
- products: product_name=UPI AutoPay; attempts=358; success_rate=84.92; own_median=90.4; z=-2.1
- categories: mcc_category=Financial Services; attempts=174; success_rate=81.03; own_median=87.24; z=-2.34

Refs: enterprise_data/warehouse/transactions, RPT-D140-DAILY, enterprise_data/warehouse/reference/incidents.parquet
