---
id: RPT-D98-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 12 Apr 2026)

**Report ID:** RPT-D98-DAILY · **Day 98 of 206** · **Derived from:** 11,340 transaction rows queried live from the warehouse

## Summary

The rail took **11,340 payment attempts** on Sunday 12 April 2026 (Weekend) and settled **₹1.23 Cr** across 10,814 successful payments. Volume was −12.9% on yesterday and −9.7% on the same weekday last week. Success closed at **95.36%**, below the trailing 28-day median of 95.94%.

Decline code ZM (Invalid UPI PIN) fired 143 times — 1.261% of attempts against a trailing 1.013%. Owner: Customer. Success rate closed at 95.36%, 0.58pp down the trailing median — a 2.6-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,340 | −12.9% | −9.7% | 12,908 |
| Successful payments | 10,814 | −13.4% | −4.8% | 12,332 |
| Success rate | 95.36% | −0.55pp | +4.99pp | 95.52% |
| Settled value | ₹1.23 Cr | −20.9% | −3.6% | ₹1.65 Cr |
| Average ticket | ₹1,134 | −8.6% | +1.2% | ₹1,332 |
| Technical declines | 0.441% | +0.10pp | −1.34pp | 0.529% |
| Business declines | 3.580% | +0.47pp | +0.05pp | 3.042% |
| Risk declines | 0.123% | −0.05pp | −0.10pp | 0.142% |
| Timeout declines | 0.397% | +0.05pp | −3.45pp | 0.647% |
| Retry share | 1.40% | +0.27pp | −3.12pp | 1.60% |
| Latency p95 | 1,250 ms | +3.2% | −42.4% | 1,339 ms |
| Active customers | 9,577 | −11.7% | −5.8% | 10,683 |
| Active merchants | 1,348 | −1.8% | −2.0% | 1,387 |

## What moved

- Success rate closed at 95.36%, 0.58pp down the trailing median — a 2.6-sigma move.
- Product UPI Person to Person ran at 94.39% success on 3,726 attempts (32.9% of the day), 0.95pp down its own 28-day median.
- App PhonePe ran at 95.12% success on 5,288 attempts (46.6% of the day), 0.81pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 29% across the trailing window to 311 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI International is compounding — attempts up 29% across the trailing window to 101 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,726 | 32.9% | 94.39% | ₹36.11 L | −16.3% |
| UPI Person to Merchant | 3,094 | 27.3% | 95.64% | ₹25.72 L | −11.1% |
| UPI QR Payments | 2,102 | 18.5% | 96.29% | ₹7.94 L | −3.2% |
| UPI Lite | 1,131 | 10.0% | 98.32% | ₹1.01 L | +7.6% |
| UPI AutoPay | 325 | 2.9% | 92.00% | ₹5.40 L | +1.6% |
| UPI Circle | 311 | 2.7% | 93.57% | ₹2.45 L | +29.9% |
| RuPay Credit on UPI | 188 | 1.7% | 95.21% | ₹7.78 L | −26.8% |
| Credit on UPI | 134 | 1.2% | 94.78% | ₹8.80 L | −24.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,587 | 95.57% | 95.99% | ₹38.13 L | normal |
| HDFC Bank | 1,218 | 95.98% | 95.67% | ₹15.11 L | normal |
| Bank of Baroda | 905 | 93.59% | 95.81% | ₹8.45 L | ⚠ outlier |
| Union Bank of India | 792 | 95.33% | 95.89% | ₹9.70 L | normal |
| Axis Bank | 740 | 94.59% | 95.83% | ₹7.62 L | normal |
| Punjab National Bank | 689 | 94.63% | 95.48% | ₹6.46 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,288 | 95.12% | 95.93% | ₹57.49 L | ⚠ outlier |
| Google Pay | 3,771 | 95.81% | 95.75% | ₹40.34 L | normal |
| Paytm | 917 | 94.77% | 96.01% | ₹10.91 L | normal |
| Navi | 394 | 97.46% | 96.03% | ₹4.00 L | normal |
| SuperMoney | 239 | 93.72% | 95.09% | ₹1.54 L | normal |
| BHIM | 128 | 96.09% | 96.55% | ₹1.17 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,090 | 95.99% | ₹25.73 L |
| Food & Beverage | 2,011 | 96.77% | ₹7.99 L |
| Mobility | 889 | 95.84% | ₹3.60 L |
| Bills | 688 | 95.06% | ₹6.99 L |
| Healthcare | 385 | 96.10% | ₹4.98 L |
| Digital | 188 | 92.55% | ₹85,514 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,295 | 29.1% | 95.51% | ₹36.49 L |
| North | 2,902 | 25.6% | 95.73% | ₹29.72 L |
| West | 2,801 | 24.7% | 95.00% | ₹30.55 L |
| East | 1,370 | 12.1% | 95.04% | ₹17.84 L |
| Central | 972 | 8.6% | 95.27% | ₹8.07 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 326 | 94.17% | ₹1.43 L |
| Vasant Wardrobe | Key Account | Retail | 55 | 96.36% | ₹1.05 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 74 | 97.30% | ₹82,066 |
| Vega Electronics | Large | Retail | 23 | 95.65% | ₹70,484 |
| Girnar Connect | Key Account | Bills | 109 | 95.41% | ₹69,169 |
| Hampi Styles | Key Account | Retail | 27 | 96.30% | ₹64,807 |
| Swift Tiffin | Key Account | Food & Beverage | 98 | 98.98% | ₹61,613 |
| Urban Boutique | Key Account | Retail | 80 | 92.50% | ₹49,345 |

## Failure analysis

Of 515 declined attempts, 406 were business declines (3.580% of attempts — balances, PINs and limits), 50 technical (0.441%), 45 timeouts (0.397%) and 14 risk declines (0.123%).

159 attempts were re-presentations of an earlier failure (1.40% of the day); 66.0% of them succeeded.

- Decline code ZM (Invalid UPI PIN) fired 143 times — 1.261% of attempts against a trailing 1.013%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 33 times — 0.291% of attempts against a trailing 0.159%. Owner: Issuer.
- Decline code U28 (Remitter bank unavailable) fired 18 times — 0.159% of attempts against a trailing 0.103%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 168 | 1.481% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 143 | 1.261% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.397% | 0.358% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 33 | 0.291% | 0.159% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.256% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 19 | 0.168% | 0.188% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.159% | 0.103% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 11 | 0.097% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 97 | 74 |
| Auto-reversals | 22 | 23 |
| Disputes / chargebacks | 14 | 11 |
| Value returned | ₹1.15 L | ₹1.55 L |

## Customer behaviour

9,577 distinct customers transacted (−9.7% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,928 | 3,315 | 1.13 | 95.35% | ₹1,248 |
| power | 2,101 | 2,746 | 1.31 | 94.83% | ₹1,370 |
| merchant_heavy | 2,179 | 2,576 | 1.18 | 95.57% | ₹807 |
| small_ticket | 1,409 | 1,685 | 1.20 | 96.02% | ₹586 |
| occasional | 749 | 790 | 1.05 | 94.94% | ₹1,412 |
| new | 187 | 202 | 1.08 | 95.54% | ₹853 |
| dormant_returning | 24 | 26 | 1.08 | 100.00% | ₹506 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 143 times — 1.261% of attempts against a trailing 1.013%. Owner: Customer.
- Success rate closed at 95.36%, 0.58pp down the trailing median — a 2.6-sigma move.
- 97 refunds were raised, 3.0 sigma above the trailing median of 74.
- Product UPI Person to Person ran at 94.39% success on 3,726 attempts (32.9% of the day), 0.95pp down its own 28-day median.
- App PhonePe ran at 95.12% success on 5,288 attempts (46.6% of the day), 0.81pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 12 April: success came in 0.58pp below baseline at 95.36% on 11,340 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,340, successes=10,814, failed=515, pending=11, settled_value_inr=12,268,174.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZM; count=143; rate_pct=1.26; trailing_rate_pct=1.01; owner=Customer; z=2.55
- headline: success_rate=95.36; trailing_median=95.94; z=-2.56
- adjustments: refunds=97; trailing_median=74.5; z=3.04
- products: product_name=UPI Person to Person; attempts=3,726; success_rate=94.39; own_median=95.34; z=-2.7
- psps: payer_psp=PhonePe; attempts=5,288; success_rate=95.12; own_median=95.93; z=-2.26
- failures: failure_code=U54; count=33; rate_pct=0.29; trailing_rate_pct=0.16; owner=Issuer; z=2.48
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- failures: failure_code=U28; count=18; rate_pct=0.16; trailing_rate_pct=0.1; owner=Issuer; z=2.44
- products: product_name=UPI Circle; attempts=311; window_growth_pct=28.7; success_rate=93.57
- products: product_name=UPI International; attempts=101; window_growth_pct=28.7; success_rate=94.06

Refs: enterprise_data/warehouse/transactions, RPT-D97-DAILY, enterprise_data/warehouse/reference/incidents.parquet
