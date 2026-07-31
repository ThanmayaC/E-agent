---
id: RPT-D146-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-30T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 30 May 2026)

**Report ID:** RPT-D146-DAILY · **Day 146 of 206** · **Derived from:** 16,783 transaction rows queried live from the warehouse

## Summary

The rail took **16,783 payment attempts** on Saturday 30 May 2026 (Weekend) and settled **₹2.28 Cr** across 16,183 successful payments. Volume was +26.6% on yesterday and +13.6% on the same weekday last week. Success closed at **96.42%**, above the trailing 28-day median of 96.08%.

App PhonePe ran at 96.68% success on 7,917 attempts (47.2% of the day), 0.62pp up its own 28-day median. Category Retail ran at 97.25% success on 4,805 attempts (39.1% of the day), 0.76pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,783 | +26.6% | +13.6% | 14,780 |
| Successful payments | 16,183 | +27.1% | +14.1% | 14,181 |
| Success rate | 96.42% | +0.35pp | +0.42pp | 95.94% |
| Settled value | ₹2.28 Cr | +26.3% | +19.3% | ₹1.97 Cr |
| Average ticket | ₹1,411 | −0.6% | +4.6% | ₹1,390 |
| Technical declines | 0.381% | −0.20pp | −0.18pp | 0.508% |
| Business declines | 2.729% | −0.10pp | −0.13pp | 2.935% |
| Risk declines | 0.137% | +0.03pp | −0.03pp | 0.127% |
| Timeout declines | 0.232% | −0.13pp | −0.07pp | 0.386% |
| Retry share | 0.93% | −0.45pp | −0.25pp | 1.34% |
| Latency p95 | 1,262 ms | −0.5% | +0.0% | 1,284 ms |
| Active customers | 13,544 | +22.4% | +12.3% | 12,074 |
| Active merchants | 1,593 | +6.0% | +7.6% | 1,505 |

## What moved

- App PhonePe ran at 96.68% success on 7,917 attempts (47.2% of the day), 0.62pp up its own 28-day median.
- Category Retail ran at 97.25% success on 4,805 attempts (39.1% of the day), 0.76pp up its own 28-day median.
- Region South ran at 96.67% success on 4,957 attempts (29.5% of the day), 0.63pp up its own 28-day median.
- Category Food & Beverage carried 3,059 attempts, 27% up its trailing median and 24.9% of the day's volume.
- Product UPI Lite carried 2,349 attempts, 35% up its trailing median and 14.0% of the day's volume.
- Region Central carried 1,553 attempts, 24% up its trailing median and 9.3% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,505 | 26.8% | 94.89% | ₹47.84 L | +2.1% |
| UPI Person to Merchant | 4,176 | 24.9% | 96.67% | ₹42.60 L | +6.6% |
| UPI QR Payments | 3,230 | 19.2% | 97.21% | ₹13.20 L | +34.2% |
| UPI Lite | 2,349 | 14.0% | 98.77% | ₹2.18 L | +35.4% |
| UPI Circle | 965 | 5.7% | 97.51% | ₹8.87 L | +65.5% |
| RuPay Credit on UPI | 409 | 2.4% | 94.62% | ₹31.22 L | +11.1% |
| UPI AutoPay | 330 | 2.0% | 92.42% | ₹6.70 L | −1.3% |
| Credit on UPI | 319 | 1.9% | 96.55% | ₹34.63 L | −10.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,357 | 96.19% | 96.04% | ₹70.31 L | normal |
| HDFC Bank | 1,759 | 96.99% | 96.21% | ₹19.96 L | ⚠ outlier |
| Bank of Baroda | 1,256 | 96.66% | 95.91% | ₹15.71 L | normal |
| Union Bank of India | 1,141 | 97.11% | 95.72% | ₹15.47 L | normal |
| Axis Bank | 1,088 | 97.24% | 96.57% | ₹15.31 L | normal |
| Punjab National Bank | 1,037 | 96.53% | 95.70% | ₹13.06 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,917 | 96.68% | 96.06% | ₹1.02 Cr | ⚠ outlier |
| Google Pay | 5,460 | 96.06% | 95.99% | ₹78.40 L | normal |
| Paytm | 1,410 | 96.81% | 96.14% | ₹17.98 L | normal |
| Navi | 630 | 96.19% | 95.45% | ₹8.99 L | normal |
| SuperMoney | 315 | 92.70% | 96.33% | ₹4.38 L | ⚠ outlier |
| BHIM | 174 | 97.70% | 95.69% | ₹3.40 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,805 | 97.25% | ₹50.73 L |
| Food & Beverage | 3,059 | 97.25% | ₹14.94 L |
| Mobility | 1,518 | 97.50% | ₹7.35 L |
| Bills | 1,418 | 96.90% | ₹15.46 L |
| Healthcare | 601 | 97.00% | ₹8.43 L |
| Digital | 287 | 94.77% | ₹1.73 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,957 | 29.5% | 96.67% | ₹66.22 L |
| West | 4,138 | 24.7% | 96.11% | ₹57.78 L |
| North | 4,128 | 24.6% | 96.12% | ₹63.90 L |
| East | 2,007 | 12.0% | 96.31% | ₹24.58 L |
| Central | 1,553 | 9.3% | 97.42% | ₹15.81 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 49 | 95.92% | ₹10.06 L |
| Rapid Bazaar | Key Account | Retail | 562 | 98.22% | ₹1.97 L |
| Vasant Wardrobe | Key Account | Retail | 62 | 93.55% | ₹1.85 L |
| Ujjwal Water Board | Key Account | Bills | 74 | 95.95% | ₹1.77 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 88 | 96.59% | ₹1.41 L |
| Hampi Stores 2298 | Key Account | Retail | 140 | 97.14% | ₹1.33 L |
| Hampi Styles | Key Account | Retail | 34 | 94.12% | ₹1.13 L |
| Girnar Connect | Key Account | Bills | 227 | 97.36% | ₹88,095 |

## Failure analysis

Of 584 declined attempts, 458 were business declines (2.729% of attempts — balances, PINs and limits), 64 technical (0.381%), 39 timeouts (0.232%) and 23 risk declines (0.137%).

156 attempts were re-presentations of an earlier failure (0.93% of the day); 66.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 210 | 1.251% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 137 | 0.816% | 0.981% |
| ZA | Transaction declined by customer | business | Customer | 63 | 0.375% | 0.343% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.167% | 0.223% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.155% | 0.207% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.125% | 0.101% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.107% | 0.135% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.107% | 0.152% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 86 | 103 |
| Auto-reversals | 25 | 27 |
| Disputes / chargebacks | 16 | 13 |
| Value returned | ₹1.55 L | ₹2.09 L |

## Customer behaviour

13,544 distinct customers transacted (+13.2% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,211 | 4,958 | 1.18 | 96.27% | ₹1,345 |
| power | 2,851 | 4,003 | 1.40 | 95.95% | ₹2,082 |
| merchant_heavy | 3,094 | 3,794 | 1.23 | 96.76% | ₹989 |
| small_ticket | 2,005 | 2,548 | 1.27 | 96.82% | ₹700 |
| occasional | 1,102 | 1,177 | 1.07 | 96.69% | ₹1,598 |
| new | 251 | 273 | 1.09 | 97.07% | ₹1,391 |
| dormant_returning | 30 | 30 | 1.00 | 93.33% | ₹874 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

30 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 96.42% success against a 96.08% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-30` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,783, successes=16,183, failed=584, pending=16, settled_value_inr=22,828,660.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- psps: payer_psp=PhonePe; attempts=7,917; success_rate=96.68; own_median=96.06; z=2.73
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- categories: mcc_category=Retail; attempts=4,805; success_rate=97.25; own_median=96.49; z=2.38
- geography: region=South; attempts=4,957; success_rate=96.67; own_median=96.04; z=2.49
- categories: mcc_category=Food & Beverage; attempts=3,059; own_median=2,403; z=3.48
- products: product_name=UPI Lite; attempts=2,349; own_median=1,735; z=3.71
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- geography: region=Central; attempts=1,553; own_median=1,254.5; z=4.11
- banks: payer_bank=HDFC Bank; attempts=1,759; success_rate=96.99; own_median=96.21; z=2.75
- geography: region=Central; attempts=1,553; success_rate=97.42; own_median=96.09; z=2.91

Refs: enterprise_data/warehouse/transactions, RPT-D145-DAILY, enterprise_data/warehouse/reference/incidents.parquet
