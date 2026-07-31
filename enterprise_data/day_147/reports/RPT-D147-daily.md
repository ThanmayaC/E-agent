---
id: RPT-D147-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-31T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 31 May 2026)

**Report ID:** RPT-D147-DAILY · **Day 147 of 206** · **Derived from:** 15,018 transaction rows queried live from the warehouse

## Summary

The rail took **15,018 payment attempts** on Sunday 31 May 2026 (Weekend) and settled **₹1.89 Cr** across 14,476 successful payments. Volume was −10.5% on yesterday and +15.7% on the same weekday last week. Success closed at **96.39%**, above the trailing 28-day median of 96.08%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,018 | −10.5% | +15.7% | 14,788 |
| Successful payments | 14,476 | −10.5% | +17.0% | 14,191 |
| Success rate | 96.39% | −0.03pp | +1.05pp | 95.96% |
| Settled value | ₹1.89 Cr | −17.3% | +14.9% | ₹1.97 Cr |
| Average ticket | ₹1,304 | −7.6% | −1.8% | ₹1,387 |
| Technical declines | 0.326% | −0.06pp | −0.20pp | 0.502% |
| Business declines | 2.817% | +0.09pp | −0.52pp | 2.931% |
| Risk declines | 0.153% | +0.02pp | −0.02pp | 0.128% |
| Timeout declines | 0.220% | −0.01pp | −0.25pp | 0.381% |
| Retry share | 0.91% | −0.02pp | −0.39pp | 1.32% |
| Latency p95 | 1,216 ms | −3.6% | −1.5% | 1,282 ms |
| Active customers | 12,291 | −9.3% | +12.1% | 12,081 |
| Active merchants | 1,523 | −4.4% | +3.3% | 1,505 |

## What moved

- Product UPI Person to Person ran at 95.75% success on 4,045 attempts (26.9% of the day), 0.61pp up its own 28-day median.
- Product UPI Circle is compounding — attempts up 30% across the trailing window to 851 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite carried 2,185 attempts, 26% up its trailing median and 14.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,045 | 26.9% | 95.75% | ₹43.93 L | −8.3% |
| UPI Person to Merchant | 3,831 | 25.5% | 96.06% | ₹44.61 L | −2.2% |
| UPI QR Payments | 2,845 | 18.9% | 96.66% | ₹11.81 L | +18.2% |
| UPI Lite | 2,185 | 14.5% | 99.18% | ₹1.90 L | +25.9% |
| UPI Circle | 851 | 5.7% | 97.30% | ₹7.39 L | +46.0% |
| UPI AutoPay | 340 | 2.3% | 89.41% | ₹5.78 L | +1.6% |
| RuPay Credit on UPI | 261 | 1.7% | 93.87% | ₹13.15 L | −29.3% |
| Credit on UPI | 247 | 1.6% | 95.14% | ₹26.31 L | −30.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,777 | 96.27% | 96.04% | ₹65.20 L | normal |
| HDFC Bank | 1,597 | 96.62% | 96.21% | ₹21.70 L | normal |
| Bank of Baroda | 1,148 | 96.69% | 96.01% | ₹16.70 L | normal |
| Union Bank of India | 1,069 | 96.35% | 95.72% | ₹11.12 L | normal |
| Axis Bank | 942 | 96.71% | 96.57% | ₹10.23 L | normal |
| ICICI Bank | 883 | 95.81% | 96.46% | ₹9.40 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,104 | 96.45% | 96.11% | ₹93.01 L | normal |
| Google Pay | 4,945 | 95.98% | 95.99% | ₹62.90 L | normal |
| Paytm | 1,220 | 96.72% | 96.14% | ₹13.79 L | normal |
| Navi | 550 | 97.45% | 95.45% | ₹5.69 L | normal |
| SuperMoney | 258 | 96.51% | 96.33% | ₹3.83 L | normal |
| BHIM | 153 | 96.08% | 95.69% | ₹1.57 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,348 | 96.76% | ₹51.94 L |
| Food & Beverage | 2,698 | 96.92% | ₹11.30 L |
| Mobility | 1,359 | 97.35% | ₹6.66 L |
| Bills | 1,239 | 96.53% | ₹13.17 L |
| Healthcare | 544 | 97.24% | ₹3.69 L |
| Digital | 280 | 95.36% | ₹1.60 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,417 | 29.4% | 96.35% | ₹58.77 L |
| North | 3,803 | 25.3% | 96.24% | ₹44.55 L |
| West | 3,634 | 24.2% | 96.26% | ₹50.37 L |
| East | 1,835 | 12.2% | 96.62% | ₹21.89 L |
| Central | 1,329 | 8.8% | 96.99% | ₹13.12 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 28 | 92.86% | ₹2.12 L |
| Rapid Bazaar | Key Account | Retail | 455 | 98.02% | ₹1.98 L |
| Vasant Wardrobe | Key Account | Retail | 63 | 84.13% | ₹1.36 L |
| Ujjwal Water Board | Key Account | Bills | 53 | 100.00% | ₹90,628 |
| Girnar Connect | Key Account | Bills | 206 | 98.06% | ₹77,785 |
| Yamuna Restaurant | Key Account | Food & Beverage | 81 | 95.06% | ₹77,070 |
| Hampi Stores 2298 | Key Account | Retail | 118 | 96.61% | ₹74,287 |
| Urban Boutique | Key Account | Retail | 127 | 97.64% | ₹73,371 |

## Failure analysis

Of 528 declined attempts, 423 were business declines (2.817% of attempts — balances, PINs and limits), 49 technical (0.326%), 33 timeouts (0.220%) and 23 risk declines (0.153%).

136 attempts were re-presentations of an earlier failure (0.91% of the day); 64.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 174 | 1.159% | 1.207% |
| ZM | Invalid UPI PIN | business | Customer | 141 | 0.939% | 0.980% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.360% | 0.346% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.213% | 0.221% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.140% | 0.150% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.120% | 0.101% |
| U30 | Debit failed at remitter bank | technical | Issuer | 17 | 0.113% | 0.207% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.113% | 0.135% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 108 | 103 |
| Auto-reversals | 30 | 26 |
| Disputes / chargebacks | 11 | 13 |
| Value returned | ₹2.15 L | ₹1.98 L |

## Customer behaviour

12,291 distinct customers transacted (+2.7% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,802 | 4,395 | 1.16 | 96.13% | ₹1,396 |
| power | 2,639 | 3,645 | 1.38 | 96.49% | ₹1,647 |
| merchant_heavy | 2,854 | 3,453 | 1.21 | 96.64% | ₹1,089 |
| small_ticket | 1,858 | 2,314 | 1.25 | 96.97% | ₹443 |
| occasional | 891 | 941 | 1.06 | 95.11% | ₹1,835 |
| new | 214 | 236 | 1.10 | 96.19% | ₹812 |
| dormant_returning | 33 | 34 | 1.03 | 91.18% | ₹838 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Product UPI International is compounding — attempts up 26% across the trailing window to 165 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Circle is compounding — attempts up 30% across the trailing window to 851 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

31 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 96.39% success against a 96.08% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-31` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,018, successes=14,476, failed=528, pending=14, settled_value_inr=18,870,447.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- products: product_name=UPI Person to Person; attempts=4,045; success_rate=95.75; own_median=95.14; z=2.22
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Circle; attempts=851; window_growth_pct=29.8; success_rate=97.3
- products: product_name=UPI Lite; attempts=2,185; own_median=1,735; z=2.72
- products: product_name=UPI International; attempts=165; window_growth_pct=26.3; success_rate=93.94
- products: product_name=UPI Circle; attempts=851; own_median=583; z=2.55
- incidents: event_id=CMP-0059; kind=merchant_campaign; severity=Sev-3; window=2026-05-25 to 2026-06-01; success_impact_pp=-0.15; volume_impact_pct=59.67
- incidents: event_id=DORM-0072; kind=dormancy_wave; severity=Sev-3; window=2026-05-28 to 2026-06-13; success_impact_pp=0.05; volume_impact_pct=-19.27
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5

Refs: enterprise_data/warehouse/transactions, RPT-D146-DAILY, enterprise_data/warehouse/reference/incidents.parquet
