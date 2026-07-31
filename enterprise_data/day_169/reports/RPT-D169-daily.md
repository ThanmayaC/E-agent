---
id: RPT-D169-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 22 Jun 2026)

**Report ID:** RPT-D169-DAILY · **Day 169 of 206** · **Derived from:** 14,268 transaction rows queried live from the warehouse

## Summary

The rail took **14,268 payment attempts** on Monday 22 June 2026 (Working day) and settled **₹1.88 Cr** across 13,716 successful payments. Volume was +1.4% on yesterday and +3.8% on the same weekday last week. Success closed at **96.13%**, in line with the trailing 28-day median of 96.28%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,268 | +1.4% | +3.8% | 15,029 |
| Successful payments | 13,716 | +1.8% | +3.8% | 14,477 |
| Success rate | 96.13% | +0.37pp | −0.06pp | 96.30% |
| Settled value | ₹1.88 Cr | +30.9% | +5.9% | ₹1.98 Cr |
| Average ticket | ₹1,371 | +28.5% | +2.0% | ₹1,366 |
| Technical declines | 0.435% | −0.02pp | +0.06pp | 0.412% |
| Business declines | 2.902% | −0.33pp | −0.10pp | 2.799% |
| Risk declines | 0.119% | −0.02pp | +0.03pp | 0.126% |
| Timeout declines | 0.329% | −0.01pp | +0.09pp | 0.269% |
| Retry share | 1.27% | −0.03pp | +0.19pp | 1.06% |
| Latency p95 | 1,284 ms | +5.8% | −0.3% | 1,274 ms |
| Active customers | 11,859 | +1.2% | +4.0% | 12,331 |
| Active merchants | 1,515 | +0.8% | −1.6% | 1,547 |

## What moved

- Product Credit on UPI is compounding — attempts up 38% across the trailing window to 452 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Person to Merchant ran at 95.66% success on 3,200 attempts (22.4% of the day), 0.63pp down its own 28-day median.
- Issuer Bank of Baroda ran at 95.19% success on 1,102 attempts (7.7% of the day), 1.29pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,016 | 28.1% | 95.09% | ₹41.95 L | −7.9% |
| UPI Person to Merchant | 3,200 | 22.4% | 95.66% | ₹28.88 L | −14.3% |
| UPI QR Payments | 2,501 | 17.5% | 96.52% | ₹10.45 L | +1.8% |
| UPI Lite | 2,109 | 14.8% | 99.38% | ₹1.99 L | +4.0% |
| UPI Circle | 768 | 5.4% | 96.09% | ₹6.22 L | +9.1% |
| Credit on UPI | 452 | 3.2% | 95.58% | ₹37.63 L | +4.9% |
| RuPay Credit on UPI | 391 | 2.7% | 97.95% | ₹20.69 L | +8.2% |
| UPI AutoPay | 345 | 2.4% | 91.59% | ₹6.06 L | −2.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,421 | 96.36% | 96.23% | ₹55.69 L | normal |
| HDFC Bank | 1,545 | 96.38% | 96.46% | ₹20.05 L | normal |
| Bank of Baroda | 1,102 | 95.19% | 96.48% | ₹13.89 L | ⚠ outlier |
| Union Bank of India | 986 | 96.75% | 96.27% | ₹10.13 L | normal |
| Axis Bank | 916 | 95.85% | 96.43% | ₹10.18 L | normal |
| Punjab National Bank | 861 | 95.82% | 96.27% | ₹15.23 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,743 | 96.03% | 96.17% | ₹90.89 L | normal |
| Google Pay | 4,596 | 96.04% | 96.38% | ₹60.69 L | normal |
| Paytm | 1,235 | 96.52% | 96.23% | ₹15.17 L | normal |
| Navi | 557 | 96.77% | 96.39% | ₹8.23 L | normal |
| SuperMoney | 281 | 94.66% | 96.19% | ₹3.00 L | normal |
| BHIM | 152 | 98.03% | 95.42% | ₹1.14 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,330 | 96.58% | ₹58.04 L |
| Food & Beverage | 2,597 | 97.15% | ₹11.71 L |
| Mobility | 1,287 | 97.36% | ₹6.18 L |
| Bills | 804 | 95.15% | ₹8.14 L |
| Healthcare | 547 | 98.17% | ₹8.16 L |
| Digital | 212 | 94.34% | ₹93,297 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,213 | 29.5% | 96.15% | ₹63.36 L |
| North | 3,580 | 25.1% | 96.01% | ₹44.15 L |
| West | 3,566 | 25.0% | 95.82% | ₹46.59 L |
| East | 1,677 | 11.8% | 96.18% | ₹20.13 L |
| Central | 1,232 | 8.6% | 97.24% | ₹13.89 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 100.00% | ₹2.08 L |
| Vasant Wardrobe | Key Account | Retail | 90 | 93.33% | ₹2.01 L |
| Rapid Bazaar | Key Account | Retail | 421 | 98.34% | ₹1.43 L |
| Hampi Stores 2298 | Key Account | Retail | 114 | 93.86% | ₹97,878 |
| Yamuna Restaurant | Key Account | Food & Beverage | 59 | 98.31% | ₹84,717 |
| Ujjwal Water Board | Key Account | Bills | 34 | 85.29% | ₹71,382 |
| Swift Mart 1738 | Key Account | Retail | 130 | 96.92% | ₹66,699 |
| Girnar Connect | Key Account | Bills | 138 | 97.10% | ₹64,468 |

## Failure analysis

Of 540 declined attempts, 414 were business declines (2.902% of attempts — balances, PINs and limits), 62 technical (0.435%), 47 timeouts (0.329%) and 17 risk declines (0.119%).

181 attempts were re-presentations of an earlier failure (1.27% of the day); 65.2% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 31 times — 0.217% of attempts against a trailing 0.139%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 174 | 1.220% | 1.187% |
| ZM | Invalid UPI PIN | business | Customer | 152 | 1.065% | 0.930% |
| ZA | Transaction declined by customer | business | Customer | 34 | 0.238% | 0.354% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 31 | 0.217% | 0.139% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.203% | 0.201% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.175% | 0.173% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.140% | 0.113% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 14 | 0.098% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 109 | 106 |
| Auto-reversals | 30 | 24 |
| Disputes / chargebacks | 16 | 13 |
| Value returned | ₹1.08 L | ₹1.70 L |

## Customer behaviour

11,859 distinct customers transacted (−3.1% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,652 | 4,173 | 1.14 | 96.00% | ₹1,368 |
| merchant_heavy | 2,814 | 3,411 | 1.21 | 96.28% | ₹1,126 |
| power | 2,506 | 3,365 | 1.34 | 96.14% | ₹1,810 |
| small_ticket | 1,721 | 2,100 | 1.22 | 96.10% | ₹620 |
| occasional | 950 | 991 | 1.04 | 96.27% | ₹1,582 |
| new | 196 | 208 | 1.06 | 96.15% | ₹1,330 |
| dormant_returning | 20 | 20 | 1.00 | 95.00% | ₹1,301 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code U54 (Transaction timed out at beneficiary) fired 31 times — 0.217% of attempts against a trailing 0.139%. Owner: Issuer.
- Product Credit on UPI is compounding — attempts up 38% across the trailing window to 452 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Person to Merchant ran at 95.66% success on 3,200 attempts (22.4% of the day), 0.63pp down its own 28-day median.
- Issuer Bank of Baroda ran at 95.19% success on 1,102 attempts (7.7% of the day), 1.29pp down its own 28-day median.
- Issuer Federal Bank ran at 94.18% success on 361 attempts (2.5% of the day), 2.07pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

22 June ran on trend at 96.13% success and ₹1.88 Cr settled. The movement worth carrying forward is in the decline profile: decline code U54 (Transaction timed out at beneficiary) fired 31 times — 0.217% of attempts against a trailing 0.139%. Owner: Issuer. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,268, successes=13,716, failed=540, pending=12, settled_value_inr=18,811,372.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U54; count=31; rate_pct=0.22; trailing_rate_pct=0.14; owner=Issuer; z=3.01
- products: product_name=Credit on UPI; attempts=452; window_growth_pct=38.4; success_rate=95.58
- products: product_name=UPI Person to Merchant; attempts=3,200; success_rate=95.66; own_median=96.28; z=-2.04
- banks: payer_bank=Bank of Baroda; attempts=1,102; success_rate=95.19; own_median=96.48; z=-3.3
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- banks: payer_bank=Federal Bank; attempts=361; success_rate=94.18; own_median=96.25; z=-2.6
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- incidents: event_id=MKT-0077; kind=market_correction; severity=Sev-3; window=2026-06-17 to 2026-06-25; success_impact_pp=-0.15; volume_impact_pct=-13.55
- incidents: event_id=ADOPT-0074; kind=adoption_surge; severity=Sev-3; window=2026-06-22 to 2026-07-05; success_impact_pp=-0.45; volume_impact_pct=40.31
- products: product_name=UPI International; attempts=194; success_rate=97.94; own_median=95.55; z=2.66

Refs: enterprise_data/warehouse/transactions, RPT-D168-DAILY, enterprise_data/warehouse/reference/incidents.parquet
