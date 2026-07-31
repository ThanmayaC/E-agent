---
id: RPT-D158-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 11 Jun 2026)

**Report ID:** RPT-D158-DAILY · **Day 158 of 206** · **Derived from:** 12,574 transaction rows queried live from the warehouse

## Summary

The rail took **12,574 payment attempts** on Thursday 11 June 2026 (Working day) and settled **₹1.66 Cr** across 12,076 successful payments. Volume was −9.1% on yesterday and −14.0% on the same weekday last week. Success closed at **96.04%**, in line with the trailing 28-day median of 96.21%.

Decline code ZA (Transaction declined by customer) fired 60 times — 0.477% of attempts against a trailing 0.348%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,574 | −9.1% | −14.0% | 15,287 |
| Successful payments | 12,076 | −9.4% | −14.4% | 14,745 |
| Success rate | 96.04% | −0.33pp | −0.40pp | 96.44% |
| Settled value | ₹1.66 Cr | −16.0% | −27.7% | ₹2.11 Cr |
| Average ticket | ₹1,373 | −7.3% | −15.6% | ₹1,431 |
| Technical declines | 0.326% | +0.04pp | −0.15pp | 0.374% |
| Business declines | 3.094% | +0.21pp | +0.54pp | 2.695% |
| Risk declines | 0.167% | −0.01pp | +0.00pp | 0.135% |
| Timeout declines | 0.278% | +0.08pp | +0.03pp | 0.265% |
| Retry share | 1.23% | +0.10pp | +0.18pp | 1.01% |
| Latency p95 | 1,341 ms | +5.8% | +0.3% | 1,279 ms |
| Active customers | 10,606 | −8.2% | −11.7% | 12,494 |
| Active merchants | 1,498 | −1.8% | −3.7% | 1,558 |

## What moved

- Product UPI Lite ran at 99.71% success on 1,714 attempts (13.6% of the day), 0.67pp up its own 28-day median.
- Issuer HDFC Bank ran at 95.44% success on 1,381 attempts (11.0% of the day), 0.94pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 31% across the trailing window to 448 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,607 | 28.7% | 95.56% | ₹35.14 L | −18.1% |
| UPI Person to Merchant | 2,963 | 23.6% | 95.58% | ₹28.67 L | −22.8% |
| UPI QR Payments | 2,099 | 16.7% | 96.57% | ₹8.75 L | −12.8% |
| UPI Lite | 1,714 | 13.6% | 99.71% | ₹1.57 L | −11.3% |
| UPI Circle | 557 | 4.4% | 96.23% | ₹4.93 L | −18.4% |
| Credit on UPI | 448 | 3.6% | 95.09% | ₹34.69 L | +14.4% |
| UPI AutoPay | 384 | 3.1% | 89.58% | ₹6.92 L | +10.8% |
| RuPay Credit on UPI | 353 | 2.8% | 93.77% | ₹17.76 L | −8.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,938 | 96.42% | 96.13% | ₹58.53 L | normal |
| HDFC Bank | 1,381 | 95.44% | 96.37% | ₹16.21 L | ⚠ outlier |
| Bank of Baroda | 924 | 95.35% | 96.45% | ₹10.89 L | ⚠ outlier |
| Union Bank of India | 875 | 95.20% | 96.39% | ₹9.87 L | ⚠ outlier |
| Axis Bank | 769 | 96.75% | 96.47% | ₹9.86 L | normal |
| ICICI Bank | 768 | 96.22% | 96.62% | ₹11.44 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,882 | 96.04% | 96.17% | ₹74.79 L | normal |
| Google Pay | 4,211 | 96.32% | 96.18% | ₹59.22 L | normal |
| Paytm | 1,041 | 95.87% | 96.12% | ₹12.93 L | normal |
| Navi | 457 | 95.62% | 96.19% | ₹4.64 L | normal |
| SuperMoney | 227 | 96.48% | 96.26% | ₹6.29 L | normal |
| BHIM | 121 | 95.04% | 95.88% | ₹1.56 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,843 | 96.20% | ₹50.30 L |
| Food & Beverage | 2,176 | 97.38% | ₹12.61 L |
| Mobility | 1,093 | 97.71% | ₹6.01 L |
| Bills | 722 | 95.15% | ₹7.33 L |
| Healthcare | 501 | 96.21% | ₹8.34 L |
| Digital | 226 | 93.81% | ₹99,143 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,603 | 28.7% | 96.14% | ₹46.47 L |
| North | 3,187 | 25.3% | 95.64% | ₹41.08 L |
| West | 3,112 | 24.7% | 96.05% | ₹43.30 L |
| East | 1,564 | 12.4% | 96.42% | ₹21.78 L |
| Central | 1,108 | 8.8% | 96.30% | ₹13.21 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Hampi Styles | Key Account | Retail | 50 | 94.00% | ₹1.77 L |
| Rapid Bazaar | Key Account | Retail | 412 | 95.39% | ₹1.76 L |
| Vega Electronics | Large | Retail | 25 | 96.00% | ₹1.36 L |
| Vasant Wardrobe | Key Account | Retail | 57 | 92.98% | ₹1.32 L |
| Kaveri Trading | Large | Retail | 47 | 100.00% | ₹91,396 |
| Hampi Stores 2298 | Key Account | Retail | 93 | 97.85% | ₹87,025 |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 100.00% | ₹80,040 |
| Ujjwal Water Board | Key Account | Bills | 35 | 88.57% | ₹64,045 |

## Failure analysis

Of 486 declined attempts, 389 were business declines (3.094% of attempts — balances, PINs and limits), 41 technical (0.326%), 35 timeouts (0.278%) and 21 risk declines (0.167%).

155 attempts were re-presentations of an earlier failure (1.23% of the day); 69.0% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 60 times — 0.477% of attempts against a trailing 0.348%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 148 | 1.177% | 1.171% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 1.074% | 0.922% |
| ZA | Transaction declined by customer | business | Customer | 60 | 0.477% | 0.348% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.223% | 0.205% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.151% | 0.194% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 19 | 0.151% | 0.111% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.135% | 0.096% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 16 | 0.127% | 0.146% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 119 | 106 |
| Auto-reversals | 24 | 25 |
| Disputes / chargebacks | 15 | 13 |
| Value returned | ₹1.70 L | ₹1.88 L |

## Customer behaviour

10,606 distinct customers transacted (−12.0% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,263 | 3,696 | 1.13 | 95.86% | ₹1,347 |
| power | 2,315 | 3,009 | 1.30 | 96.14% | ₹1,728 |
| merchant_heavy | 2,408 | 2,870 | 1.19 | 96.41% | ₹1,237 |
| small_ticket | 1,633 | 1,964 | 1.20 | 96.08% | ₹569 |
| occasional | 786 | 824 | 1.05 | 95.27% | ₹1,931 |
| new | 177 | 186 | 1.05 | 95.16% | ₹701 |
| dormant_returning | 24 | 25 | 1.04 | 96.00% | ₹805 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **REG-0071** (Sev-2) — MDR reinstated on RuPay Credit above ₹2,000, scoped to RUPAY_CREDIT. Merchant discount rate reinstated on higher-value RuPay Credit transactions. Large-ticket volume moved back to debit-funded rails; the product's average ticket falls.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 60 times — 0.477% of attempts against a trailing 0.348%. Owner: Customer.
- Issuer HDFC Bank ran at 95.44% success on 1,381 attempts (11.0% of the day), 0.94pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 31% across the trailing window to 448 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer Bank of Baroda ran at 95.35% success on 924 attempts (7.3% of the day), 1.11pp down its own 28-day median.
- Issuer Union Bank of India ran at 95.20% success on 875 attempts (7.0% of the day), 1.19pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

11 June ran on trend at 96.04% success and ₹1.66 Cr settled. The movement worth carrying forward is in the decline profile: decline code ZA (Transaction declined by customer) fired 60 times — 0.477% of attempts against a trailing 0.348%. Owner: Customer. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,574, successes=12,076, failed=486, pending=12, settled_value_inr=16,584,832.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZA; count=60; rate_pct=0.48; trailing_rate_pct=0.35; owner=Customer; z=2.77
- products: product_name=UPI Lite; attempts=1,714; success_rate=99.71; own_median=99.04; z=2.97
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- incidents: event_id=REG-0071; kind=pricing_change; severity=Sev-2; window=2026-06-08 to 2026-07-29; success_impact_pp=0.1; volume_impact_pct=-17
- banks: payer_bank=HDFC Bank; attempts=1,381; success_rate=95.44; own_median=96.38; z=-2.68
- products: product_name=Credit on UPI; attempts=448; window_growth_pct=30.9; success_rate=95.09
- banks: payer_bank=Bank of Baroda; attempts=924; success_rate=95.35; own_median=96.45; z=-2.08
- banks: payer_bank=Union Bank of India; attempts=875; success_rate=95.2; own_median=96.39; z=-2.14
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5

Refs: enterprise_data/warehouse/transactions, RPT-D157-DAILY, enterprise_data/warehouse/reference/incidents.parquet
