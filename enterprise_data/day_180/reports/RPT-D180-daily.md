---
id: RPT-D180-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-03T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 03 Jul 2026)

**Report ID:** RPT-D180-DAILY · **Day 180 of 206** · **Derived from:** 17,368 transaction rows queried live from the warehouse

## Summary

The rail took **17,368 payment attempts** on Friday 03 July 2026 (Working day) and settled **₹2.25 Cr** across 16,791 successful payments. Volume was −4.3% on yesterday and +25.7% on the same weekday last week. Success closed at **96.68%**, above the trailing 28-day median of 96.21%.

Category Bills carried 1,891 attempts, 122% up its trailing median and 15.0% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 17,368 | −4.3% | +25.7% | 18,031 |
| Successful payments | 16,791 | −4.4% | +26.8% | 17,417 |
| Success rate | 96.68% | −0.10pp | +0.85pp | 96.60% |
| Settled value | ₹2.25 Cr | −6.4% | +55.0% | ₹2.39 Cr |
| Average ticket | ₹1,342 | −2.1% | +22.2% | ₹1,374 |
| Technical declines | 0.345% | +0.03pp | −0.05pp | 0.345% |
| Business declines | 2.551% | +0.10pp | −0.75pp | 2.628% |
| Risk declines | 0.127% | +0.02pp | −0.05pp | 0.100% |
| Timeout declines | 0.236% | −0.04pp | +0.00pp | 0.251% |
| Retry share | 0.96% | −0.01pp | −0.29pp | 1.08% |
| Latency p95 | 1,257 ms | +3.8% | −2.1% | 1,238 ms |
| Active customers | 14,050 | −3.1% | +21.6% | 14,425 |
| Active merchants | 1,656 | −1.3% | +9.9% | 1,664 |

## What moved

- Category Bills carried 1,891 attempts, 122% up its trailing median and 15.0% of the day's volume.
- Success rate closed at 96.68%, 0.47pp up the trailing median — a 1.7-sigma move.
- Product UPI Lite is compounding — attempts up 35% across the trailing window to 2,912 today, with success holding, so the growth is healthy and worth funding.
- Category Bills ran at 97.73% success on 1,891 attempts (15.0% of the day), 1.83pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,720 | 27.2% | 95.38% | ₹53.28 L | +13.0% |
| UPI Person to Merchant | 4,044 | 23.3% | 96.74% | ₹44.26 L | +16.6% |
| UPI QR Payments | 3,052 | 17.6% | 96.69% | ₹13.66 L | +24.1% |
| UPI Lite | 2,912 | 16.8% | 98.76% | ₹2.77 L | +31.7% |
| UPI Circle | 831 | 4.8% | 98.19% | ₹8.50 L | +12.4% |
| Credit on UPI | 513 | 3.0% | 96.30% | ₹43.90 L | +11.2% |
| RuPay Credit on UPI | 431 | 2.5% | 96.06% | ₹16.89 L | +17.1% |
| UPI AutoPay | 357 | 2.1% | 94.40% | ₹6.96 L | −3.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,599 | 96.84% | 96.18% | ₹81.58 L | normal |
| HDFC Bank | 1,855 | 97.20% | 96.39% | ₹21.53 L | normal |
| Bank of Baroda | 1,338 | 97.38% | 96.22% | ₹15.16 L | normal |
| Union Bank of India | 1,159 | 96.12% | 96.00% | ₹15.39 L | normal |
| Axis Bank | 1,062 | 97.36% | 96.15% | ₹15.14 L | normal |
| Punjab National Bank | 1,056 | 95.93% | 95.95% | ₹13.37 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,072 | 96.48% | 96.11% | ₹99.46 L | normal |
| Google Pay | 5,788 | 96.91% | 96.33% | ₹81.04 L | normal |
| Paytm | 1,426 | 96.70% | 96.12% | ₹18.30 L | normal |
| Navi | 677 | 96.90% | 96.47% | ₹9.58 L | normal |
| SuperMoney | 378 | 96.30% | 95.97% | ₹4.60 L | normal |
| BHIM | 186 | 97.31% | 95.91% | ₹3.62 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,720 | 97.10% | ₹56.82 L |
| Food & Beverage | 2,962 | 97.60% | ₹15.67 L |
| Bills | 1,891 | 97.73% | ₹20.21 L |
| Mobility | 1,600 | 97.50% | ₹8.48 L |
| Healthcare | 641 | 96.88% | ₹9.94 L |
| Digital | 332 | 96.69% | ₹1.89 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,113 | 29.4% | 96.48% | ₹62.13 L |
| North | 4,417 | 25.4% | 96.56% | ₹59.21 L |
| West | 4,241 | 24.4% | 96.75% | ₹58.65 L |
| East | 2,139 | 12.3% | 96.49% | ₹28.17 L |
| Central | 1,458 | 8.4% | 97.81% | ₹17.20 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 90.91% | ₹3.78 L |
| Hampi Stores 2298 | Key Account | Retail | 116 | 100.00% | ₹2.44 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 76 | 96.05% | ₹2.26 L |
| Ujjwal Water Board | Key Account | Bills | 73 | 95.89% | ₹1.68 L |
| Vasant Wardrobe | Key Account | Retail | 56 | 92.86% | ₹1.43 L |
| Rapid Bazaar | Key Account | Retail | 438 | 97.49% | ₹1.28 L |
| Girnar Connect | Key Account | Bills | 310 | 98.39% | ₹1.24 L |
| Urban Boutique | Key Account | Retail | 103 | 95.15% | ₹92,077 |

## Failure analysis

Of 566 declined attempts, 443 were business declines (2.551% of attempts — balances, PINs and limits), 60 technical (0.345%), 41 timeouts (0.236%) and 22 risk declines (0.127%).

166 attempts were re-presentations of an earlier failure (0.96% of the day); 69.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 185 | 1.065% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 139 | 0.800% | 0.954% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.317% | 0.325% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.202% | 0.193% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.144% | 0.133% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.127% | 0.176% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.115% | 0.098% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.092% | 0.067% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 128 | 110 |
| Auto-reversals | 25 | 24 |
| Disputes / chargebacks | 9 | 14 |
| Value returned | ₹1.32 L | ₹1.70 L |

## Customer behaviour

14,050 distinct customers transacted (+16.9% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,425 | 5,175 | 1.17 | 96.77% | ₹1,377 |
| power | 2,975 | 4,128 | 1.39 | 96.71% | ₹1,824 |
| merchant_heavy | 3,263 | 4,098 | 1.26 | 96.56% | ₹1,089 |
| small_ticket | 2,027 | 2,540 | 1.25 | 96.65% | ₹556 |
| occasional | 1,099 | 1,154 | 1.05 | 96.27% | ₹1,476 |
| new | 233 | 245 | 1.05 | 97.96% | ₹1,145 |
| dormant_returning | 28 | 28 | 1.00 | 100.00% | ₹631 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Lite is compounding — attempts up 35% across the trailing window to 2,912 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 03 July: success came in 0.47pp above baseline at 96.68% on 17,368 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-03` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=17,368, successes=16,791, failed=566, pending=11, settled_value_inr=22,535,668.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,891; own_median=852; z=9.87
- headline: success_rate=96.68; trailing_median=96.21; z=1.66
- products: product_name=UPI Lite; attempts=2,912; window_growth_pct=35.4; success_rate=98.76
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- categories: mcc_category=Bills; attempts=1,891; success_rate=97.73; own_median=95.89; z=2.25
- geography: region=East; attempts=2,139; own_median=1,692.5; z=2.47
- categories: mcc_category=Mobility; attempts=1,600; own_median=1,277.5; z=2.21
- psps: payer_psp=Navi; attempts=677; own_median=526; z=2.58
- incidents: event_id=ADOPT-0074; kind=adoption_surge; severity=Sev-3; window=2026-06-22 to 2026-07-05; success_impact_pp=-0.45; volume_impact_pct=40.31
- products: product_name=UPI AutoPay; attempts=357; success_rate=94.4; own_median=90.77; z=2.27

Refs: enterprise_data/warehouse/transactions, RPT-D179-DAILY, enterprise_data/warehouse/reference/incidents.parquet
