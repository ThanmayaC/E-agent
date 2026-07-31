---
id: RPT-D145-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-29T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 29 May 2026)

**Report ID:** RPT-D145-DAILY · **Day 145 of 206** · **Derived from:** 13,257 transaction rows queried live from the warehouse

## Summary

The rail took **13,257 payment attempts** on Friday 29 May 2026 (Working day) and settled **₹1.81 Cr** across 12,736 successful payments. Volume was −0.2% on yesterday and −4.3% on the same weekday last week. Success closed at **96.07%**, in line with the trailing 28-day median of 96.08%.

Product UPI Person to Person ran at 94.37% success on 3,499 attempts (26.4% of the day), 0.80pp down its own 28-day median. Issuer State Bank of India ran at 95.29% success on 4,161 attempts (31.4% of the day), 0.76pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,257 | −0.2% | −4.3% | 14,711 |
| Successful payments | 12,736 | +0.3% | −4.2% | 14,112 |
| Success rate | 96.07% | +0.48pp | +0.18pp | 95.92% |
| Settled value | ₹1.81 Cr | −0.8% | −18.9% | ₹1.96 Cr |
| Average ticket | ₹1,420 | −1.1% | −15.4% | ₹1,389 |
| Technical declines | 0.581% | +0.03pp | +0.14pp | 0.513% |
| Business declines | 2.829% | −0.51pp | −0.32pp | 2.942% |
| Risk declines | 0.106% | −0.01pp | −0.01pp | 0.127% |
| Timeout declines | 0.362% | +0.06pp | +0.08pp | 0.391% |
| Retry share | 1.38% | +0.05pp | +0.28pp | 1.35% |
| Latency p95 | 1,268 ms | −2.6% | −2.7% | 1,285 ms |
| Active customers | 11,068 | −0.7% | −3.6% | 12,024 |
| Active merchants | 1,503 | +0.1% | +2.5% | 1,501 |

## What moved

- Product UPI Person to Person ran at 94.37% success on 3,499 attempts (26.4% of the day), 0.80pp down its own 28-day median.
- Issuer State Bank of India ran at 95.29% success on 4,161 attempts (31.4% of the day), 0.76pp down its own 28-day median.
- Product UPI Person to Merchant carried 3,340 attempts, 15% down its trailing median and 25.2% of the day's volume.
- Product UPI International is compounding — attempts up 29% across the trailing window to 194 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer Axis Bank ran at 95.08% success on 834 attempts (6.3% of the day), 1.53pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,499 | 26.4% | 94.37% | ₹36.36 L | −21.3% |
| UPI Person to Merchant | 3,340 | 25.2% | 96.50% | ₹33.96 L | −14.8% |
| UPI QR Payments | 2,265 | 17.1% | 96.73% | ₹9.96 L | −6.7% |
| UPI Lite | 1,878 | 14.2% | 99.04% | ₹1.69 L | +8.7% |
| UPI Circle | 677 | 5.1% | 96.75% | ₹5.54 L | +19.0% |
| Credit on UPI | 382 | 2.9% | 98.43% | ₹35.37 L | +8.7% |
| RuPay Credit on UPI | 369 | 2.8% | 95.66% | ₹18.63 L | +1.2% |
| UPI AutoPay | 346 | 2.6% | 89.31% | ₹6.72 L | +4.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,161 | 95.29% | 96.05% | ₹58.10 L | ⚠ outlier |
| HDFC Bank | 1,463 | 96.38% | 96.20% | ₹20.45 L | normal |
| Bank of Baroda | 1,000 | 96.70% | 95.88% | ₹11.69 L | normal |
| Union Bank of India | 894 | 96.20% | 95.72% | ₹11.34 L | normal |
| Axis Bank | 834 | 95.08% | 96.62% | ₹10.19 L | ⚠ outlier |
| Punjab National Bank | 826 | 95.40% | 95.73% | ₹11.45 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,216 | 96.20% | 96.01% | ₹85.06 L | normal |
| Google Pay | 4,399 | 95.98% | 95.99% | ₹64.16 L | normal |
| Paytm | 1,140 | 95.35% | 96.14% | ₹15.21 L | normal |
| Navi | 491 | 95.32% | 95.71% | ₹5.38 L | normal |
| SuperMoney | 244 | 96.31% | 96.26% | ₹3.09 L | normal |
| BHIM | 120 | 95.83% | 95.51% | ₹1.36 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,757 | 96.67% | ₹40.04 L |
| Food & Beverage | 2,279 | 97.37% | ₹10.37 L |
| Bills | 1,281 | 96.41% | ₹14.84 L |
| Mobility | 1,182 | 98.14% | ₹6.44 L |
| Healthcare | 487 | 97.74% | ₹10.96 L |
| Digital | 253 | 97.23% | ₹1.29 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,923 | 29.6% | 96.28% | ₹60.81 L |
| North | 3,413 | 25.7% | 95.75% | ₹43.49 L |
| West | 3,237 | 24.4% | 96.01% | ₹43.76 L |
| East | 1,556 | 11.7% | 96.79% | ₹20.03 L |
| Central | 1,128 | 8.5% | 95.48% | ₹12.70 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 67 | 95.52% | ₹1.78 L |
| Rapid Bazaar | Key Account | Retail | 390 | 96.92% | ₹1.68 L |
| Vega Electronics | Large | Retail | 25 | 92.00% | ₹1.08 L |
| Urban Boutique | Key Account | Retail | 111 | 98.20% | ₹1.04 L |
| Ujjwal Water Board | Key Account | Bills | 58 | 98.28% | ₹93,246 |
| Girnar Connect | Key Account | Bills | 217 | 98.16% | ₹83,096 |
| Swift Grill | Large | Food & Beverage | 40 | 95.00% | ₹74,579 |
| Hampi Styles | Key Account | Retail | 32 | 96.88% | ₹70,684 |

## Failure analysis

Of 514 declined attempts, 375 were business declines (2.829% of attempts — balances, PINs and limits), 77 technical (0.581%), 48 timeouts (0.362%) and 14 risk declines (0.106%).

183 attempts were re-presentations of an earlier failure (1.38% of the day); 68.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 144 | 1.086% | 1.207% |
| ZM | Invalid UPI PIN | business | Customer | 134 | 1.011% | 0.981% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.385% | 0.343% |
| U30 | Debit failed at remitter bank | technical | Issuer | 36 | 0.272% | 0.206% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.196% | 0.223% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.181% | 0.132% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.166% | 0.150% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.128% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 90 | 103 |
| Auto-reversals | 30 | 27 |
| Disputes / chargebacks | 12 | 13 |
| Value returned | ₹2.66 L | ₹1.98 L |

## Customer behaviour

11,068 distinct customers transacted (−7.7% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,439 | 3,946 | 1.15 | 96.00% | ₹1,468 |
| power | 2,446 | 3,246 | 1.33 | 95.84% | ₹1,853 |
| merchant_heavy | 2,480 | 2,967 | 1.20 | 96.16% | ₹952 |
| small_ticket | 1,662 | 2,016 | 1.21 | 96.28% | ₹759 |
| occasional | 833 | 864 | 1.04 | 96.41% | ₹1,915 |
| new | 182 | 192 | 1.05 | 95.83% | ₹1,286 |
| dormant_returning | 26 | 26 | 1.00 | 100.00% | ₹617 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Product UPI Person to Person ran at 94.37% success on 3,499 attempts (26.4% of the day), 0.80pp down its own 28-day median.
- Issuer State Bank of India ran at 95.29% success on 4,161 attempts (31.4% of the day), 0.76pp down its own 28-day median.
- Product UPI International is compounding — attempts up 29% across the trailing window to 194 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer Axis Bank ran at 95.08% success on 834 attempts (6.3% of the day), 1.53pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

29 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 96.07% success against a 96.08% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-29` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,257, successes=12,736, failed=514, pending=7, settled_value_inr=18,078,976.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Person to Person; attempts=3,499; success_rate=94.37; own_median=95.17; z=-3.49
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- banks: payer_bank=State Bank of India; attempts=4,161; success_rate=95.29; own_median=96.05; z=-2.52
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Person to Merchant; attempts=3,340; own_median=3,920.5; z=-2.26
- products: product_name=UPI International; attempts=194; window_growth_pct=28.6; success_rate=92.78
- banks: payer_bank=Axis Bank; attempts=834; success_rate=95.08; own_median=96.61; z=-3.04
- banks: payer_bank=Canara Bank; attempts=758; success_rate=97.76; own_median=95.61; z=2.94
- categories: mcc_category=Bills; attempts=1,281; own_median=913; z=2.41
- products: product_name=Credit on UPI; attempts=382; success_rate=98.43; own_median=95.69; z=2.32

Refs: enterprise_data/warehouse/transactions, RPT-D144-DAILY, enterprise_data/warehouse/reference/incidents.parquet
