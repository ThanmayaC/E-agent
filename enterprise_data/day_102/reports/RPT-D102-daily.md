---
id: RPT-D102-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 16 Apr 2026)

**Report ID:** RPT-D102-DAILY · **Day 102 of 206** · **Derived from:** 11,650 transaction rows queried live from the warehouse

## Summary

The rail took **11,650 payment attempts** on Thursday 16 April 2026 (Working day) and settled **₹1.65 Cr** across 11,113 successful payments. Volume was +7.2% on yesterday and −4.9% on the same weekday last week. Success closed at **95.39%**, below the trailing 28-day median of 95.94%.

Decline code U30 (Debit failed at remitter bank) fired 38 times — 0.326% of attempts against a trailing 0.190%. Owner: Issuer. Decline code ZA (Transaction declined by customer) fired 58 times — 0.498% of attempts against a trailing 0.359%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,650 | +7.2% | −4.9% | 12,568 |
| Successful payments | 11,113 | +7.3% | −5.5% | 12,002 |
| Success rate | 95.39% | +0.07pp | −0.67pp | 95.48% |
| Settled value | ₹1.65 Cr | +10.8% | +3.8% | ₹1.63 Cr |
| Average ticket | ₹1,480 | +3.3% | +10.0% | ₹1,354 |
| Technical declines | 0.670% | +0.15pp | +0.26pp | 0.539% |
| Business declines | 3.270% | −0.22pp | +0.38pp | 3.140% |
| Risk declines | 0.189% | +0.01pp | +0.07pp | 0.148% |
| Timeout declines | 0.386% | −0.03pp | −0.01pp | 0.579% |
| Retry share | 1.30% | −0.36pp | +0.15pp | 1.55% |
| Latency p95 | 1,259 ms | −1.6% | −1.3% | 1,319 ms |
| Active customers | 9,845 | +6.3% | −3.8% | 10,452 |
| Active merchants | 1,380 | +7.6% | +1.5% | 1,377 |

## What moved

- Issuer State Bank of India ran at 94.53% success on 3,731 attempts (32.0% of the day), 1.40pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 262 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 36% across the trailing window to 267 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,049 | 34.8% | 94.96% | ₹44.17 L | −8.4% |
| UPI Person to Merchant | 3,077 | 26.4% | 95.42% | ₹31.56 L | −11.3% |
| UPI QR Payments | 1,983 | 17.0% | 96.12% | ₹8.26 L | −8.3% |
| UPI Lite | 964 | 8.3% | 98.44% | ₹86,798 | −9.4% |
| RuPay Credit on UPI | 342 | 2.9% | 94.15% | ₹22.89 L | +28.1% |
| UPI AutoPay | 301 | 2.6% | 91.69% | ₹5.85 L | −5.9% |
| UPI Circle | 267 | 2.3% | 94.76% | ₹1.90 L | +5.3% |
| Credit on UPI | 262 | 2.2% | 95.04% | ₹22.49 L | +45.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,731 | 94.53% | 95.94% | ₹49.02 L | ⚠ outlier |
| HDFC Bank | 1,265 | 95.34% | 96.04% | ₹17.54 L | normal |
| Bank of Baroda | 848 | 95.05% | 95.83% | ₹12.64 L | normal |
| ICICI Bank | 754 | 96.68% | 96.29% | ₹8.42 L | normal |
| Union Bank of India | 737 | 94.17% | 95.90% | ₹11.48 L | ⚠ outlier |
| Axis Bank | 735 | 96.19% | 95.62% | ₹11.55 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,374 | 95.31% | 95.82% | ₹72.59 L | normal |
| Google Pay | 3,947 | 95.62% | 95.75% | ₹53.28 L | normal |
| Paytm | 980 | 95.20% | 95.91% | ₹21.37 L | normal |
| Navi | 392 | 96.43% | 95.77% | ₹5.38 L | normal |
| SuperMoney | 222 | 94.14% | 95.08% | ₹3.11 L | normal |
| BHIM | 139 | 95.68% | 96.12% | ₹1.16 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,210 | 96.07% | ₹39.48 L |
| Food & Beverage | 1,822 | 96.16% | ₹7.66 L |
| Mobility | 827 | 96.86% | ₹5.53 L |
| Bills | 777 | 94.47% | ₹11.32 L |
| Healthcare | 368 | 93.48% | ₹3.57 L |
| Digital | 184 | 94.57% | ₹96,218 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,437 | 29.5% | 95.46% | ₹50.27 L |
| North | 3,052 | 26.2% | 95.35% | ₹42.24 L |
| West | 2,785 | 23.9% | 95.30% | ₹41.22 L |
| East | 1,385 | 11.9% | 95.96% | ₹18.40 L |
| Central | 991 | 8.5% | 94.75% | ₹12.38 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 38 | 97.37% | ₹2.52 L |
| Rapid Bazaar | Key Account | Retail | 309 | 97.41% | ₹1.47 L |
| Hampi Styles | Key Account | Retail | 35 | 97.14% | ₹1.32 L |
| Vasant Wardrobe | Key Account | Retail | 50 | 94.00% | ₹99,637 |
| Yamuna Restaurant | Key Account | Food & Beverage | 80 | 97.50% | ₹73,612 |
| Hampi Stores 2298 | Key Account | Retail | 109 | 97.25% | ₹71,477 |
| Girnar Connect | Key Account | Bills | 127 | 96.06% | ₹55,938 |
| Urban Boutique | Key Account | Retail | 91 | 96.70% | ₹51,510 |

## Failure analysis

Of 526 declined attempts, 381 were business declines (3.270% of attempts — balances, PINs and limits), 78 technical (0.670%), 45 timeouts (0.386%) and 22 risk declines (0.189%).

151 attempts were re-presentations of an earlier failure (1.30% of the day); 74.2% of them succeeded.

- Decline code U30 (Debit failed at remitter bank) fired 38 times — 0.326% of attempts against a trailing 0.190%. Owner: Issuer.
- Decline code ZA (Transaction declined by customer) fired 58 times — 0.498% of attempts against a trailing 0.359%. Owner: Customer.
- Decline code YA (PSP not available) fired 12 times — 0.103% of attempts against a trailing 0.059%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 167 | 1.433% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 115 | 0.987% | 1.015% |
| ZA | Transaction declined by customer | business | Customer | 58 | 0.498% | 0.359% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.326% | 0.190% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.223% | 0.180% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.197% | 0.221% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 19 | 0.163% | 0.117% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.137% | 0.100% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 97 | 76 |
| Auto-reversals | 14 | 22 |
| Disputes / chargebacks | 9 | 11 |
| Value returned | ₹1.01 L | ₹1.55 L |

## Customer behaviour

9,845 distinct customers transacted (−5.3% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,000 | 3,353 | 1.12 | 95.11% | ₹1,621 |
| power | 2,106 | 2,761 | 1.31 | 95.36% | ₹1,908 |
| merchant_heavy | 2,267 | 2,694 | 1.19 | 95.92% | ₹1,113 |
| small_ticket | 1,529 | 1,848 | 1.21 | 95.67% | ₹653 |
| occasional | 744 | 775 | 1.04 | 94.58% | ₹1,722 |
| new | 174 | 194 | 1.11 | 93.81% | ₹932 |
| dormant_returning | 25 | 25 | 1.00 | 96.00% | ₹1,135 |

## Operational events

- **INC-PSP-0033** (Sev-1) — SuperMoney app release regression, scoped to SuperMoney between 18:00 and 23:00. A SuperMoney client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-PSP-0030** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 16:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U30 (Debit failed at remitter bank) fired 38 times — 0.326% of attempts against a trailing 0.190%. Owner: Issuer.
- Decline code ZA (Transaction declined by customer) fired 58 times — 0.498% of attempts against a trailing 0.359%. Owner: Customer.
- Issuer State Bank of India ran at 94.53% success on 3,731 attempts (32.0% of the day), 1.40pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 36% across the trailing window to 267 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code YA (PSP not available) fired 12 times — 0.103% of attempts against a trailing 0.059%. Owner: PSP.

### Opportunities

- Product Credit on UPI is compounding — attempts up 36% across the trailing window to 262 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

16 April was an incident day: INC-PSP-0033, INC-PSP-0030 were live and the rail closed at 95.39% success against a 95.94% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,650, successes=11,113, failed=526, pending=11, settled_value_inr=16,451,805.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-PSP-0033; kind=psp_degradation; severity=Sev-1; window=2026-04-15 to 2026-04-18; success_impact_pp=-23.53; volume_impact_pct=-36.83
- incidents: event_id=INC-PSP-0030; kind=psp_degradation; severity=Sev-2; window=2026-04-14 to 2026-04-16; success_impact_pp=-7.77; volume_impact_pct=-12.17
- failures: failure_code=U30; count=38; rate_pct=0.33; trailing_rate_pct=0.19; owner=Issuer; z=3.1
- failures: failure_code=ZA; count=58; rate_pct=0.5; trailing_rate_pct=0.36; owner=Customer; z=2.41
- banks: payer_bank=State Bank of India; attempts=3,731; success_rate=94.53; own_median=95.94; z=-2.52
- products: product_name=Credit on UPI; attempts=262; window_growth_pct=36.4; success_rate=95.04
- products: product_name=UPI Circle; attempts=267; window_growth_pct=35.7; success_rate=94.76
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- failures: failure_code=YA; count=12; rate_pct=0.1; trailing_rate_pct=0.06; owner=PSP; z=2.36
- categories: mcc_category=Healthcare; attempts=368; success_rate=93.48; own_median=96.99; z=-2.84

Refs: enterprise_data/warehouse/transactions, RPT-D101-DAILY, enterprise_data/warehouse/reference/incidents.parquet
