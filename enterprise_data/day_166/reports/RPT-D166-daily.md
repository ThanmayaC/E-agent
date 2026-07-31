---
id: RPT-D166-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 19 Jun 2026)

**Report ID:** RPT-D166-DAILY · **Day 166 of 206** · **Derived from:** 16,007 transaction rows queried live from the warehouse

## Summary

The rail took **16,007 payment attempts** on Friday 19 June 2026 (Monsoon Sale (build-up)) and settled **₹2.07 Cr** across 15,404 successful payments. Volume was +8.4% on yesterday and +9.3% on the same weekday last week. Success closed at **96.23%**, in line with the trailing 28-day median of 96.22%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,007 | +8.4% | +9.3% | 14,894 |
| Successful payments | 15,404 | +8.4% | +9.1% | 14,350 |
| Success rate | 96.23% | −0.01pp | −0.17pp | 96.33% |
| Settled value | ₹2.07 Cr | −5.2% | +19.9% | ₹1.98 Cr |
| Average ticket | ₹1,346 | −12.5% | +9.9% | ₹1,380 |
| Technical declines | 0.544% | +0.06pp | +0.14pp | 0.406% |
| Business declines | 2.718% | +0.05pp | −0.01pp | 2.788% |
| Risk declines | 0.137% | −0.01pp | −0.01pp | 0.127% |
| Timeout declines | 0.269% | −0.08pp | +0.02pp | 0.263% |
| Retry share | 1.14% | +0.10pp | +0.13pp | 1.04% |
| Latency p95 | 1,314 ms | +1.0% | +4.1% | 1,277 ms |
| Active customers | 13,096 | +7.1% | +7.6% | 12,236 |
| Active merchants | 1,543 | −3.6% | +2.2% | 1,545 |

## What moved

- Region South ran at 95.90% success on 4,585 attempts (28.6% of the day), 0.36pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,057 | 31.6% | 94.94% | ₹52.64 L | +16.0% |
| UPI Person to Merchant | 3,644 | 22.8% | 96.51% | ₹37.39 L | +1.5% |
| UPI QR Payments | 2,557 | 16.0% | 96.28% | ₹11.20 L | +8.8% |
| UPI Lite | 2,160 | 13.5% | 99.17% | ₹2.07 L | +10.4% |
| UPI Circle | 793 | 5.0% | 97.48% | ₹7.89 L | +16.2% |
| Credit on UPI | 583 | 3.6% | 97.26% | ₹47.39 L | +35.3% |
| UPI AutoPay | 351 | 2.2% | 91.45% | ₹6.23 L | −0.1% |
| RuPay Credit on UPI | 332 | 2.1% | 96.99% | ₹19.49 L | −8.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,104 | 96.00% | 96.18% | ₹62.69 L | normal |
| HDFC Bank | 1,701 | 96.41% | 96.41% | ₹20.29 L | normal |
| Bank of Baroda | 1,244 | 96.22% | 96.46% | ₹20.45 L | normal |
| Union Bank of India | 1,112 | 96.13% | 96.36% | ₹17.17 L | normal |
| ICICI Bank | 1,012 | 97.13% | 96.54% | ₹9.99 L | normal |
| Punjab National Bank | 951 | 95.69% | 96.25% | ₹11.28 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,449 | 96.01% | 96.13% | ₹96.58 L | normal |
| Google Pay | 5,324 | 96.22% | 96.36% | ₹68.74 L | normal |
| Paytm | 1,385 | 97.18% | 96.05% | ₹19.65 L | normal |
| Navi | 601 | 97.00% | 96.19% | ₹7.17 L | normal |
| SuperMoney | 311 | 98.71% | 96.21% | ₹3.55 L | ⚠ outlier |
| BHIM | 144 | 97.22% | 95.25% | ₹3.10 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,933 | 96.80% | ₹67.90 L |
| Food & Beverage | 2,671 | 97.75% | ₹13.67 L |
| Mobility | 1,295 | 97.22% | ₹6.14 L |
| Bills | 851 | 95.53% | ₹8.38 L |
| Healthcare | 528 | 97.54% | ₹11.09 L |
| Digital | 217 | 95.39% | ₹1.07 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,585 | 28.6% | 95.90% | ₹64.27 L |
| North | 4,155 | 26.0% | 96.15% | ₹52.48 L |
| West | 4,017 | 25.1% | 96.24% | ₹52.48 L |
| East | 1,880 | 11.7% | 96.91% | ₹22.27 L |
| Central | 1,370 | 8.6% | 96.64% | ₹15.92 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 55 | 96.36% | ₹4.47 L |
| Vasant Wardrobe | Key Account | Retail | 122 | 97.54% | ₹2.93 L |
| Rapid Bazaar | Key Account | Retail | 422 | 95.73% | ₹1.86 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 97 | 100.00% | ₹1.40 L |
| Hampi Stores 2298 | Key Account | Retail | 144 | 95.14% | ₹1.25 L |
| Hampi Styles | Key Account | Retail | 41 | 95.12% | ₹1.07 L |
| Urban Boutique | Key Account | Retail | 138 | 96.38% | ₹79,356 |
| Girnar Connect | Key Account | Bills | 148 | 97.97% | ₹79,180 |

## Failure analysis

Of 587 declined attempts, 435 were business declines (2.718% of attempts — balances, PINs and limits), 87 technical (0.544%), 43 timeouts (0.269%) and 22 risk declines (0.137%).

182 attempts were re-presentations of an earlier failure (1.14% of the day); 68.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 187 | 1.168% | 1.217% |
| ZM | Invalid UPI PIN | business | Customer | 150 | 0.937% | 0.933% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.287% | 0.361% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.237% | 0.186% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.181% | 0.209% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.162% | 0.139% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.131% | 0.113% |
| U69 | Beneficiary bank offline | technical | Issuer | 20 | 0.125% | 0.078% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 103 | 106 |
| Auto-reversals | 26 | 24 |
| Disputes / chargebacks | 14 | 13 |
| Value returned | ₹1.72 L | ₹1.71 L |

## Customer behaviour

13,096 distinct customers transacted (+8.0% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,119 | 4,758 | 1.16 | 96.36% | ₹1,466 |
| power | 2,769 | 3,824 | 1.38 | 95.97% | ₹1,772 |
| merchant_heavy | 3,035 | 3,685 | 1.21 | 96.39% | ₹958 |
| small_ticket | 1,872 | 2,345 | 1.25 | 96.16% | ₹673 |
| occasional | 1,033 | 1,099 | 1.06 | 95.63% | ₹1,501 |
| new | 228 | 255 | 1.12 | 98.04% | ₹742 |
| dormant_returning | 40 | 41 | 1.02 | 100.00% | ₹1,024 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.

## Risks and opportunities

### Risks

- Region South ran at 95.90% success on 4,585 attempts (28.6% of the day), 0.36pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 26% across the trailing window to 2,160 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 26% across the trailing window to 583 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

19 June ran on trend at 96.23% success and ₹2.07 Cr settled. The movement worth carrying forward is in geography: region South ran at 95.90% success on 4,585 attempts (28.6% of the day), 0.36pp down its own 28-day median. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,007, successes=15,404, failed=587, pending=16, settled_value_inr=20,741,383.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- geography: region=South; attempts=4,585; success_rate=95.9; own_median=96.26; z=-2.03
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Lite; attempts=2,160; window_growth_pct=26.2; success_rate=99.17
- products: product_name=Credit on UPI; attempts=583; window_growth_pct=25.6; success_rate=97.26
- banks: payer_bank=IDFC First Bank; attempts=448; success_rate=98.44; own_median=96.33; z=2.44
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- incidents: event_id=MKT-0077; kind=market_correction; severity=Sev-3; window=2026-06-17 to 2026-06-25; success_impact_pp=-0.15; volume_impact_pct=-13.55
- products: product_name=UPI Lite Auto Top-Up; attempts=111; own_median=92.5; z=2.27

Refs: enterprise_data/warehouse/transactions, RPT-D165-DAILY, enterprise_data/warehouse/reference/incidents.parquet
