---
id: RPT-D170-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 23 Jun 2026)

**Report ID:** RPT-D170-DAILY · **Day 170 of 206** · **Derived from:** 13,999 transaction rows queried live from the warehouse

## Summary

The rail took **13,999 payment attempts** on Tuesday 23 June 2026 (Working day) and settled **₹1.72 Cr** across 13,448 successful payments. Volume was −1.9% on yesterday and +1.8% on the same weekday last week. Success closed at **96.06%**, in line with the trailing 28-day median of 96.28%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,999 | −1.9% | +1.8% | 14,984 |
| Successful payments | 13,448 | −2.0% | +1.8% | 14,432 |
| Success rate | 96.06% | −0.07pp | −0.03pp | 96.29% |
| Settled value | ₹1.72 Cr | −8.7% | −3.0% | ₹1.97 Cr |
| Average ticket | ₹1,278 | −6.8% | −4.7% | ₹1,362 |
| Technical declines | 0.536% | +0.10pp | +0.24pp | 0.417% |
| Business declines | 2.972% | +0.07pp | −0.19pp | 2.807% |
| Risk declines | 0.093% | −0.03pp | +0.01pp | 0.125% |
| Timeout declines | 0.264% | −0.07pp | −0.01pp | 0.269% |
| Retry share | 1.13% | −0.14pp | +0.08pp | 1.06% |
| Latency p95 | 1,257 ms | −2.1% | −3.2% | 1,273 ms |
| Active customers | 11,622 | −2.0% | +1.3% | 12,300 |
| Active merchants | 1,515 | +0.0% | +2.2% | 1,546 |

## What moved

- Product UPI Lite ran at 98.29% success on 2,221 attempts (15.9% of the day), 0.75pp down its own 28-day median.
- Issuer Bank of Baroda ran at 94.96% success on 1,072 attempts (7.7% of the day), 1.52pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 33% across the trailing window to 471 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer HDFC Bank ran at 97.13% success on 1,497 attempts (10.7% of the day), 0.70pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,065 | 29.0% | 95.10% | ₹43.59 L | −5.3% |
| UPI Person to Merchant | 2,935 | 21.0% | 95.95% | ₹27.54 L | −19.4% |
| UPI QR Payments | 2,274 | 16.2% | 96.57% | ₹10.21 L | −7.6% |
| UPI Lite | 2,221 | 15.9% | 98.29% | ₹1.98 L | +8.2% |
| UPI Circle | 755 | 5.4% | 97.88% | ₹6.46 L | +6.5% |
| Credit on UPI | 471 | 3.4% | 95.33% | ₹30.45 L | +6.1% |
| RuPay Credit on UPI | 408 | 2.9% | 95.59% | ₹16.73 L | +12.4% |
| UPI AutoPay | 372 | 2.7% | 91.13% | ₹7.12 L | +5.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,383 | 95.94% | 96.28% | ₹52.78 L | normal |
| HDFC Bank | 1,497 | 97.13% | 96.43% | ₹18.32 L | ⚠ outlier |
| Bank of Baroda | 1,072 | 94.96% | 96.48% | ₹15.63 L | ⚠ outlier |
| Union Bank of India | 995 | 96.28% | 96.35% | ₹11.52 L | normal |
| Axis Bank | 870 | 96.09% | 96.32% | ₹11.84 L | normal |
| Punjab National Bank | 850 | 96.35% | 96.20% | ₹11.56 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,662 | 95.92% | 96.17% | ₹81.95 L | normal |
| Google Pay | 4,572 | 96.11% | 96.36% | ₹58.88 L | normal |
| Paytm | 1,079 | 96.20% | 96.44% | ₹13.09 L | normal |
| Navi | 499 | 96.99% | 96.61% | ₹4.80 L | normal |
| SuperMoney | 298 | 92.95% | 96.13% | ₹3.99 L | ⚠ outlier |
| BHIM | 166 | 97.59% | 95.42% | ₹2.33 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,053 | 96.40% | ₹54.70 L |
| Food & Beverage | 2,546 | 96.58% | ₹10.02 L |
| Mobility | 1,305 | 97.85% | ₹7.02 L |
| Bills | 853 | 97.07% | ₹8.53 L |
| Healthcare | 582 | 96.91% | ₹5.26 L |
| Financial Services | 186 | 89.78% | ₹10.36 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,054 | 29.0% | 96.42% | ₹50.32 L |
| North | 3,632 | 25.9% | 96.15% | ₹43.28 L |
| West | 3,386 | 24.2% | 95.63% | ₹43.82 L |
| East | 1,681 | 12.0% | 95.95% | ₹21.27 L |
| Central | 1,246 | 8.9% | 95.99% | ₹13.14 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 82 | 95.12% | ₹2.70 L |
| Rapid Bazaar | Key Account | Retail | 435 | 97.47% | ₹2.20 L |
| Vega Electronics | Large | Retail | 35 | 97.14% | ₹2.00 L |
| Hampi Styles | Key Account | Retail | 45 | 95.56% | ₹86,517 |
| Urban Boutique | Key Account | Retail | 117 | 97.44% | ₹74,415 |
| Girnar Connect | Key Account | Bills | 140 | 97.14% | ₹67,558 |
| Tejas Bites | Key Account | Food & Beverage | 189 | 97.35% | ₹61,188 |
| Shakti Stores 1531 | Key Account | Retail | 88 | 94.32% | ₹59,742 |

## Failure analysis

Of 541 declined attempts, 416 were business declines (2.972% of attempts — balances, PINs and limits), 75 technical (0.536%), 37 timeouts (0.264%) and 13 risk declines (0.093%).

158 attempts were re-presentations of an earlier failure (1.13% of the day); 72.2% of them succeeded.

- Decline code U30 (Debit failed at remitter bank) fired 40 times — 0.286% of attempts against a trailing 0.173%. Owner: Issuer.
- Decline code UX (Mandate execution outside permitted window) fired 16 times — 0.114% of attempts against a trailing 0.059%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 180 | 1.286% | 1.187% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 0.964% | 0.938% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.321% | 0.348% |
| U30 | Debit failed at remitter bank | technical | Issuer | 40 | 0.286% | 0.173% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.207% | 0.200% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.121% | 0.141% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.114% | 0.059% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.100% | 0.088% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 87 | 106 |
| Auto-reversals | 30 | 24 |
| Disputes / chargebacks | 16 | 14 |
| Value returned | ₹1.70 L | ₹1.67 L |

## Customer behaviour

11,622 distinct customers transacted (−4.8% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,554 | 4,073 | 1.15 | 95.75% | ₹1,241 |
| power | 2,536 | 3,408 | 1.34 | 95.63% | ₹1,853 |
| merchant_heavy | 2,668 | 3,233 | 1.21 | 96.32% | ₹930 |
| small_ticket | 1,780 | 2,143 | 1.20 | 96.92% | ₹671 |
| occasional | 878 | 914 | 1.04 | 96.28% | ₹1,228 |
| new | 185 | 207 | 1.12 | 95.17% | ₹1,111 |
| dormant_returning | 21 | 21 | 1.00 | 100.00% | ₹954 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Product UPI Lite ran at 98.29% success on 2,221 attempts (15.9% of the day), 0.75pp down its own 28-day median.
- Issuer Bank of Baroda ran at 94.96% success on 1,072 attempts (7.7% of the day), 1.52pp down its own 28-day median.
- Decline code U30 (Debit failed at remitter bank) fired 40 times — 0.286% of attempts against a trailing 0.173%. Owner: Issuer.
- Product Credit on UPI is compounding — attempts up 33% across the trailing window to 471 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code UX (Mandate execution outside permitted window) fired 16 times — 0.114% of attempts against a trailing 0.059%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

23 June ran on trend at 96.06% success and ₹1.72 Cr settled. The movement worth carrying forward is in the product mix: product UPI Lite ran at 98.29% success on 2,221 attempts (15.9% of the day), 0.75pp down its own 28-day median. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,999, successes=13,448, failed=541, pending=10, settled_value_inr=17,183,203.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Lite; attempts=2,221; success_rate=98.29; own_median=99.04; z=-3.23
- banks: payer_bank=Bank of Baroda; attempts=1,072; success_rate=94.96; own_median=96.48; z=-3.82
- failures: failure_code=U30; count=40; rate_pct=0.29; trailing_rate_pct=0.17; owner=Issuer; z=2.23
- products: product_name=Credit on UPI; attempts=471; window_growth_pct=33.3; success_rate=95.33
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- failures: failure_code=UX; count=16; rate_pct=0.11; trailing_rate_pct=0.06; owner=PSP; z=2.71
- banks: payer_bank=HDFC Bank; attempts=1,497; success_rate=97.13; own_median=96.43; z=2.34
- incidents: event_id=MAINT-0084; kind=maintenance_window; severity=Sev-3; window=2026-01-24 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- categories: mcc_category=Digital; attempts=175; success_rate=90.86; own_median=94.64; z=-3.46
- psps: payer_psp=SuperMoney; attempts=298; success_rate=92.95; own_median=96.13; z=-2.79

Refs: enterprise_data/warehouse/transactions, RPT-D169-DAILY, enterprise_data/warehouse/reference/incidents.parquet
