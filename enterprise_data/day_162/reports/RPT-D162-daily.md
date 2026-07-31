---
id: RPT-D162-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 15 Jun 2026)

**Report ID:** RPT-D162-DAILY · **Day 162 of 206** · **Derived from:** 13,740 transaction rows queried live from the warehouse

## Summary

The rail took **13,740 payment attempts** on Monday 15 June 2026 (Working day) and settled **₹1.78 Cr** across 13,216 successful payments. Volume was +3.5% on yesterday and −15.8% on the same weekday last week. Success closed at **96.19%**, in line with the trailing 28-day median of 96.32%.

21 disputes were raised, 2.7 sigma above the trailing median of 13.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,740 | +3.5% | −15.8% | 15,004 |
| Successful payments | 13,216 | +3.7% | −16.0% | 14,465 |
| Success rate | 96.19% | +0.24pp | −0.27pp | 96.38% |
| Settled value | ₹1.78 Cr | +19.9% | −23.5% | ₹1.99 Cr |
| Average ticket | ₹1,344 | +15.5% | −8.9% | ₹1,374 |
| Technical declines | 0.378% | −0.20pp | −0.14pp | 0.392% |
| Business declines | 3.006% | −0.05pp | +0.48pp | 2.748% |
| Risk declines | 0.087% | −0.00pp | −0.02pp | 0.126% |
| Timeout declines | 0.240% | −0.03pp | −0.11pp | 0.262% |
| Retry share | 1.08% | −0.17pp | +0.07pp | 1.03% |
| Latency p95 | 1,288 ms | +6.4% | −1.8% | 1,269 ms |
| Active customers | 11,401 | +2.6% | −13.4% | 12,301 |
| Active merchants | 1,540 | +6.1% | −3.0% | 1,547 |

## What moved

- Region South ran at 95.92% success on 4,044 attempts (29.4% of the day), 0.36pp down its own 28-day median.
- Issuer Union Bank of India ran at 94.17% success on 961 attempts (7.0% of the day), 2.23pp down its own 28-day median.
- Issuer Axis Bank ran at 97.95% success on 877 attempts (6.4% of the day), 1.48pp up its own 28-day median.
- Product UPI Lite is compounding — attempts up 29% across the trailing window to 1,977 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,820 | 27.8% | 95.05% | ₹40.58 L | −13.2% |
| UPI Person to Merchant | 3,275 | 23.8% | 96.18% | ₹31.55 L | −14.5% |
| UPI QR Payments | 2,272 | 16.5% | 96.43% | ₹9.98 L | −4.1% |
| UPI Lite | 1,977 | 14.4% | 98.68% | ₹1.79 L | +2.3% |
| UPI Circle | 639 | 4.7% | 96.56% | ₹4.78 L | −6.4% |
| Credit on UPI | 479 | 3.5% | 96.66% | ₹35.24 L | +20.1% |
| RuPay Credit on UPI | 378 | 2.8% | 97.09% | ₹18.04 L | +2.0% |
| UPI AutoPay | 376 | 2.7% | 91.76% | ₹7.27 L | +7.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,386 | 95.74% | 96.22% | ₹60.87 L | normal |
| HDFC Bank | 1,492 | 96.45% | 96.42% | ₹18.69 L | normal |
| Bank of Baroda | 1,056 | 96.21% | 96.48% | ₹11.80 L | normal |
| Union Bank of India | 961 | 94.17% | 96.40% | ₹9.87 L | ⚠ outlier |
| Axis Bank | 877 | 97.95% | 96.47% | ₹9.86 L | ⚠ outlier |
| Punjab National Bank | 828 | 96.14% | 96.31% | ₹11.23 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,401 | 96.23% | 96.23% | ₹85.25 L | normal |
| Google Pay | 4,494 | 96.35% | 96.35% | ₹56.96 L | normal |
| Paytm | 1,222 | 95.34% | 95.98% | ₹13.91 L | normal |
| Navi | 520 | 97.12% | 96.23% | ₹6.13 L | normal |
| SuperMoney | 264 | 96.59% | 96.26% | ₹3.85 L | normal |
| BHIM | 131 | 90.08% | 95.69% | ₹1.46 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,153 | 96.77% | ₹48.49 L |
| Food & Beverage | 2,429 | 96.67% | ₹13.14 L |
| Mobility | 1,283 | 97.97% | ₹7.03 L |
| Bills | 828 | 96.14% | ₹9.64 L |
| Healthcare | 527 | 96.20% | ₹5.42 L |
| Digital | 209 | 97.13% | ₹98,138 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,044 | 29.4% | 95.92% | ₹53.14 L |
| North | 3,561 | 25.9% | 96.57% | ₹46.75 L |
| West | 3,309 | 24.1% | 95.68% | ₹46.09 L |
| East | 1,622 | 11.8% | 96.73% | ₹17.50 L |
| Central | 1,204 | 8.8% | 96.59% | ₹14.18 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 30 | 93.33% | ₹3.19 L |
| Vasant Wardrobe | Key Account | Retail | 75 | 94.67% | ₹2.47 L |
| Rapid Bazaar | Key Account | Retail | 423 | 96.45% | ₹1.91 L |
| Swift Grill | Large | Food & Beverage | 42 | 90.48% | ₹1.65 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 90 | 97.78% | ₹1.12 L |
| Hampi Styles | Key Account | Retail | 40 | 95.00% | ₹1.02 L |
| Hampi Stores 2298 | Key Account | Retail | 96 | 94.79% | ₹93,913 |
| Ujjwal Water Board | Key Account | Bills | 36 | 100.00% | ₹79,526 |

## Failure analysis

Of 510 declined attempts, 413 were business declines (3.006% of attempts — balances, PINs and limits), 52 technical (0.378%), 33 timeouts (0.240%) and 12 risk declines (0.087%).

148 attempts were re-presentations of an earlier failure (1.08% of the day); 70.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 177 | 1.288% | 1.198% |
| ZM | Invalid UPI PIN | business | Customer | 134 | 0.975% | 0.904% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.393% | 0.348% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.182% | 0.211% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.138% | 0.187% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.109% | 0.113% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.102% | 0.090% |
| ZX | Mandate not found or revoked | business | PSP | 14 | 0.102% | 0.068% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 120 | 105 |
| Auto-reversals | 17 | 24 |
| Disputes / chargebacks | 21 | 13 |
| Value returned | ₹1.24 L | ₹1.72 L |

## Customer behaviour

11,401 distinct customers transacted (−5.9% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,509 | 4,013 | 1.14 | 96.26% | ₹1,220 |
| power | 2,485 | 3,325 | 1.34 | 95.94% | ₹2,056 |
| merchant_heavy | 2,636 | 3,155 | 1.20 | 96.39% | ₹968 |
| small_ticket | 1,706 | 2,129 | 1.25 | 96.67% | ₹667 |
| occasional | 859 | 898 | 1.05 | 94.54% | ₹1,394 |
| new | 172 | 186 | 1.08 | 97.31% | ₹1,448 |
| dormant_returning | 34 | 34 | 1.00 | 100.00% | ₹1,031 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 21 disputes were raised, 2.7 sigma above the trailing median of 13.
- Region South ran at 95.92% success on 4,044 attempts (29.4% of the day), 0.36pp down its own 28-day median.
- Issuer Union Bank of India ran at 94.17% success on 961 attempts (7.0% of the day), 2.23pp down its own 28-day median.
- Issuer ICICI Bank ran at 95.14% success on 803 attempts (5.8% of the day), 1.48pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 29% across the trailing window to 1,977 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

15 June ran on trend at 96.19% success and ₹1.78 Cr settled. The movement worth carrying forward is in money moving back: 21 disputes were raised, 2.7 sigma above the trailing median of 13. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,740, successes=13,216, failed=510, pending=14, settled_value_inr=17,765,603.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=21; trailing_median=13; z=2.7
- geography: region=South; attempts=4,044; success_rate=95.92; own_median=96.28; z=-2.12
- banks: payer_bank=Union Bank of India; attempts=961; success_rate=94.17; own_median=96.4; z=-4.1
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- banks: payer_bank=Axis Bank; attempts=877; success_rate=97.95; own_median=96.47; z=3.53
- products: product_name=UPI Lite; attempts=1,977; window_growth_pct=29.1; success_rate=98.68
- banks: payer_bank=ICICI Bank; attempts=803; success_rate=95.14; own_median=96.62; z=-2.03
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- incidents: event_id=CMP-0060; kind=merchant_campaign; severity=Sev-3; window=2026-06-11 to 2026-06-17; success_impact_pp=-0.07; volume_impact_pct=27.15
- categories: mcc_category=Financial Services; attempts=189; own_median=163.5; z=2.29

Refs: enterprise_data/warehouse/transactions, RPT-D161-DAILY, enterprise_data/warehouse/reference/incidents.parquet
