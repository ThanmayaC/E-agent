---
id: RPT-D168-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-21T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 21 Jun 2026)

**Report ID:** RPT-D168-DAILY · **Day 168 of 206** · **Derived from:** 14,065 transaction rows queried live from the warehouse

## Summary

The rail took **14,065 payment attempts** on Sunday 21 June 2026 (Weekend) and settled **₹1.44 Cr** across 13,469 successful payments. Volume was −27.2% on yesterday and +5.9% on the same weekday last week. Success closed at **95.76%**, below the trailing 28-day median of 96.28%.

App PhonePe ran at 95.43% success on 6,537 attempts (46.5% of the day), 0.75pp down its own 28-day median. Success rate closed at 95.76%, 0.52pp down the trailing median — a 1.9-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,065 | −27.2% | +5.9% | 15,065 |
| Successful payments | 13,469 | −27.8% | +5.7% | 14,513 |
| Success rate | 95.76% | −0.84pp | −0.19pp | 96.31% |
| Settled value | ₹1.44 Cr | −44.3% | −3.0% | ₹1.98 Cr |
| Average ticket | ₹1,067 | −22.8% | −8.3% | ₹1,365 |
| Technical declines | 0.455% | −0.01pp | −0.12pp | 0.411% |
| Business declines | 3.228% | +0.74pp | +0.17pp | 2.794% |
| Risk declines | 0.135% | +0.03pp | +0.04pp | 0.127% |
| Timeout declines | 0.341% | +0.10pp | +0.07pp | 0.266% |
| Retry share | 1.29% | +0.33pp | +0.04pp | 1.05% |
| Latency p95 | 1,214 ms | −4.6% | +0.2% | 1,274 ms |
| Active customers | 11,718 | −22.9% | +5.4% | 12,353 |
| Active merchants | 1,503 | −9.8% | +3.6% | 1,549 |

## What moved

- App PhonePe ran at 95.43% success on 6,537 attempts (46.5% of the day), 0.75pp down its own 28-day median.
- Success rate closed at 95.76%, 0.52pp down the trailing median — a 1.9-sigma move.
- Region South ran at 95.67% success on 4,109 attempts (29.2% of the day), 0.59pp down its own 28-day median.
- Category Retail ran at 96.17% success on 4,281 attempts (42.3% of the day), 0.70pp down its own 28-day median.
- Category Food & Beverage ran at 96.13% success on 2,636 attempts (26.0% of the day), 1.13pp down its own 28-day median.
- Product UPI Person to Person ran at 94.69% success on 3,938 attempts (28.0% of the day), 0.78pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,938 | 28.0% | 94.69% | ₹40.20 L | −9.7% |
| UPI Person to Merchant | 3,594 | 25.6% | 95.66% | ₹35.24 L | −3.8% |
| UPI QR Payments | 2,323 | 16.5% | 96.17% | ₹9.17 L | −5.5% |
| UPI Lite | 2,180 | 15.5% | 98.53% | ₹1.86 L | +9.4% |
| UPI Circle | 861 | 6.1% | 96.52% | ₹6.12 L | +23.9% |
| UPI AutoPay | 357 | 2.5% | 89.64% | ₹6.36 L | +1.4% |
| Credit on UPI | 220 | 1.6% | 95.91% | ₹12.76 L | −49.0% |
| RuPay Credit on UPI | 199 | 1.4% | 94.97% | ₹8.80 L | −45.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,456 | 95.83% | 96.23% | ₹46.65 L | normal |
| HDFC Bank | 1,579 | 95.69% | 96.46% | ₹15.82 L | ⚠ outlier |
| Bank of Baroda | 1,082 | 95.47% | 96.48% | ₹9.30 L | ⚠ outlier |
| Union Bank of India | 954 | 95.60% | 96.27% | ₹8.44 L | normal |
| Axis Bank | 901 | 95.45% | 96.43% | ₹11.04 L | normal |
| Punjab National Bank | 865 | 96.42% | 96.20% | ₹10.57 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,537 | 95.43% | 96.17% | ₹71.77 L | ⚠ outlier |
| Google Pay | 4,692 | 95.97% | 96.38% | ₹43.10 L | normal |
| Paytm | 1,185 | 95.19% | 96.23% | ₹11.99 L | normal |
| Navi | 513 | 97.08% | 96.19% | ₹4.52 L | normal |
| SuperMoney | 269 | 94.80% | 96.21% | ₹2.22 L | normal |
| BHIM | 149 | 95.30% | 95.50% | ₹2.33 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,281 | 96.17% | ₹42.23 L |
| Food & Beverage | 2,636 | 96.13% | ₹11.23 L |
| Mobility | 1,272 | 97.88% | ₹6.04 L |
| Bills | 820 | 97.68% | ₹7.42 L |
| Healthcare | 507 | 96.84% | ₹3.83 L |
| Digital | 198 | 91.92% | ₹1.07 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,109 | 29.2% | 95.67% | ₹45.03 L |
| North | 3,600 | 25.6% | 95.92% | ₹34.38 L |
| West | 3,411 | 24.3% | 95.72% | ₹34.31 L |
| East | 1,671 | 11.9% | 95.33% | ₹19.99 L |
| Central | 1,274 | 9.1% | 96.31% | ₹10.03 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 82 | 96.34% | ₹1.77 L |
| Rapid Bazaar | Key Account | Retail | 449 | 96.44% | ₹1.51 L |
| Vega Electronics | Large | Retail | 27 | 96.30% | ₹1.17 L |
| Hampi Styles | Key Account | Retail | 31 | 90.32% | ₹83,256 |
| Urban Boutique | Key Account | Retail | 123 | 94.31% | ₹82,032 |
| Ujjwal Water Board | Key Account | Bills | 48 | 100.00% | ₹81,765 |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 95.89% | ₹75,346 |
| Girnar Connect | Key Account | Bills | 138 | 97.83% | ₹58,942 |

## Failure analysis

Of 585 declined attempts, 454 were business declines (3.228% of attempts — balances, PINs and limits), 64 technical (0.455%), 48 timeouts (0.341%) and 19 risk declines (0.135%).

182 attempts were re-presentations of an earlier failure (1.29% of the day); 67.0% of them succeeded.

- Decline code UX (Mandate execution outside permitted window) fired 15 times — 0.107% of attempts against a trailing 0.058%. Owner: PSP.
- Decline code ZX (Mandate not found or revoked) fired 16 times — 0.114% of attempts against a trailing 0.071%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.244% | 1.187% |
| ZM | Invalid UPI PIN | business | Customer | 158 | 1.123% | 0.930% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.391% | 0.354% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.242% | 0.201% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.171% | 0.180% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.142% | 0.139% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.142% | 0.113% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.128% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 116 | 106 |
| Auto-reversals | 27 | 24 |
| Disputes / chargebacks | 13 | 13 |
| Value returned | ₹1.28 L | ₹1.71 L |

## Customer behaviour

11,718 distinct customers transacted (−4.2% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,628 | 4,149 | 1.14 | 95.88% | ₹1,053 |
| power | 2,494 | 3,321 | 1.33 | 95.51% | ₹1,495 |
| merchant_heavy | 2,744 | 3,296 | 1.20 | 95.96% | ₹861 |
| small_ticket | 1,766 | 2,159 | 1.22 | 95.28% | ₹436 |
| occasional | 857 | 894 | 1.04 | 96.09% | ₹1,182 |
| new | 204 | 221 | 1.08 | 97.29% | ₹749 |
| dormant_returning | 25 | 25 | 1.00 | 100.00% | ₹1,613 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.

## Risks and opportunities

### Risks

- App PhonePe ran at 95.43% success on 6,537 attempts (46.5% of the day), 0.75pp down its own 28-day median.
- Success rate closed at 95.76%, 0.52pp down the trailing median — a 1.9-sigma move.
- Region South ran at 95.67% success on 4,109 attempts (29.2% of the day), 0.59pp down its own 28-day median.
- Category Retail ran at 96.17% success on 4,281 attempts (42.3% of the day), 0.70pp down its own 28-day median.
- Category Food & Beverage ran at 96.13% success on 2,636 attempts (26.0% of the day), 1.13pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 21 June: success came in 0.52pp below baseline at 95.76% on 14,065 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-21` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,065, successes=13,469, failed=585, pending=11, settled_value_inr=14,374,112.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- psps: payer_psp=PhonePe; attempts=6,537; success_rate=95.43; own_median=96.17; z=-2.92
- headline: success_rate=95.76; trailing_median=96.28; z=-1.94
- geography: region=South; attempts=4,109; success_rate=95.67; own_median=96.26; z=-2.68
- categories: mcc_category=Retail; attempts=4,281; success_rate=96.17; own_median=96.87; z=-2.22
- categories: mcc_category=Food & Beverage; attempts=2,636; success_rate=96.13; own_median=97.26; z=-2.38
- products: product_name=UPI Person to Person; attempts=3,938; success_rate=94.69; own_median=95.47; z=-2.15
- products: product_name=Credit on UPI; attempts=220; window_growth_pct=39.2; success_rate=95.91
- products: product_name=UPI Person to Merchant; attempts=3,594; success_rate=95.66; own_median=96.28; z=-2.03
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- geography: region=East; attempts=1,671; success_rate=95.33; own_median=96.44; z=-2.32

Refs: enterprise_data/warehouse/transactions, RPT-D167-DAILY, enterprise_data/warehouse/reference/incidents.parquet
