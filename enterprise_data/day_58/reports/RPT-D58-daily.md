---
id: RPT-D58-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-03T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 03 Mar 2026)

**Report ID:** RPT-D58-DAILY · **Day 58 of 206** · **Derived from:** 14,785 transaction rows queried live from the warehouse

## Summary

The rail took **14,785 payment attempts** on Tuesday 03 March 2026 (Holi (build-up)) and settled **₹1.62 Cr** across 14,161 successful payments. Volume was −1.5% on yesterday and +48.4% on the same weekday last week. Success closed at **95.78%**, in line with the trailing 28-day median of 95.54%.

Attempt volume ran 5.7 standard deviations up its trailing 28-day median at 14,785, 48.4% up on the same weekday last week. App Google Pay carried 4,867 attempts, 41% up its trailing median and 32.9% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,785 | −1.5% | +48.4% | 14,942 |
| Successful payments | 14,161 | −1.6% | +50.2% | 14,322 |
| Success rate | 95.78% | −0.11pp | +1.15pp | 95.85% |
| Settled value | ₹1.62 Cr | −4.6% | +49.4% | ₹1.63 Cr |
| Average ticket | ₹1,147 | −3.1% | −0.6% | ₹1,135 |
| Technical declines | 0.372% | −0.01pp | −0.24pp | 0.361% |
| Business declines | 3.219% | +0.05pp | −0.76pp | 3.254% |
| Risk declines | 0.156% | +0.08pp | +0.07pp | 0.107% |
| Timeout declines | 0.372% | −0.02pp | −0.14pp | 0.335% |
| Retry share | 1.16% | −0.04pp | −0.65pp | 1.20% |
| Latency p95 | 1,220 ms | +1.5% | −8.9% | 1,211 ms |
| Active customers | 11,945 | −0.9% | +40.5% | 12,013 |
| Active merchants | 1,380 | +0.8% | +14.1% | 1,369 |

## What moved

- Attempt volume ran 5.7 standard deviations up its trailing 28-day median at 14,785, 48.4% up on the same weekday last week.
- App Google Pay carried 4,867 attempts, 41% up its trailing median and 32.9% of the day's volume.
- Category Bills carried 1,384 attempts, 108% up its trailing median and 14.9% of the day's volume.
- App PhonePe carried 7,007 attempts, 42% up its trailing median and 47.4% of the day's volume.
- Region West carried 3,679 attempts, 43% up its trailing median and 24.9% of the day's volume.
- Issuer State Bank of India carried 4,685 attempts, 38% up its trailing median and 31.7% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,510 | 37.3% | 95.17% | ₹62.95 L | +40.8% |
| UPI Person to Merchant | 4,608 | 31.2% | 96.07% | ₹49.04 L | +47.2% |
| UPI QR Payments | 2,493 | 16.9% | 96.39% | ₹11.36 L | +39.9% |
| UPI Lite | 965 | 6.5% | 98.13% | ₹88,211 | +33.5% |
| UPI AutoPay | 313 | 2.1% | 90.73% | ₹6.06 L | +4.7% |
| RuPay Credit on UPI | 212 | 1.4% | 96.23% | ₹7.71 L | +0.7% |
| UPI Circle | 201 | 1.4% | 96.52% | ₹1.37 L | +92.3% |
| Credit on UPI | 155 | 1.0% | 95.48% | ₹10.16 L | +6.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,685 | 95.39% | 95.54% | ₹54.72 L | normal |
| HDFC Bank | 1,625 | 96.37% | 96.15% | ₹15.99 L | normal |
| Bank of Baroda | 1,109 | 95.40% | 95.38% | ₹10.82 L | normal |
| Union Bank of India | 1,033 | 94.68% | 95.39% | ₹12.14 L | normal |
| Punjab National Bank | 911 | 96.27% | 94.87% | ₹8.89 L | normal |
| Axis Bank | 905 | 95.58% | 95.70% | ₹10.36 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,007 | 96.00% | 95.56% | ₹77.95 L | normal |
| Google Pay | 4,867 | 95.36% | 95.61% | ₹50.80 L | normal |
| Paytm | 1,174 | 96.68% | 95.41% | ₹11.42 L | normal |
| Navi | 539 | 96.29% | 95.09% | ₹7.33 L | normal |
| SuperMoney | 293 | 95.90% | 96.01% | ₹4.21 L | normal |
| BHIM | 154 | 91.56% | 94.88% | ₹1.85 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,919 | 96.22% | ₹40.79 L |
| Food & Beverage | 2,220 | 96.44% | ₹10.95 L |
| Bills | 1,384 | 96.97% | ₹17.33 L |
| Mobility | 773 | 97.02% | ₹4.31 L |
| Healthcare | 393 | 95.67% | ₹4.80 L |
| Digital | 288 | 92.36% | ₹1.85 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,238 | 28.7% | 95.92% | ₹45.45 L |
| North | 3,832 | 25.9% | 95.75% | ₹46.13 L |
| West | 3,679 | 24.9% | 95.92% | ₹39.80 L |
| East | 1,705 | 11.5% | 94.90% | ₹18.12 L |
| Central | 1,331 | 9.0% | 96.17% | ₹12.89 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹2.32 L |
| Vasant Wardrobe | Key Account | Retail | 106 | 96.23% | ₹2.21 L |
| Rapid Bazaar | Key Account | Retail | 400 | 97.00% | ₹1.82 L |
| Ujjwal Water Board | Key Account | Bills | 66 | 93.94% | ₹1.59 L |
| Girnar Connect | Key Account | Bills | 226 | 98.23% | ₹1.12 L |
| Urban Boutique | Key Account | Retail | 98 | 98.98% | ₹1.10 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 88 | 96.59% | ₹1.01 L |
| Hampi Stores 2298 | Key Account | Retail | 107 | 96.26% | ₹81,357 |

## Failure analysis

Of 609 declined attempts, 476 were business declines (3.219% of attempts — balances, PINs and limits), 55 technical (0.372%), 55 timeouts (0.372%) and 23 risk declines (0.156%).

171 attempts were re-presentations of an earlier failure (1.16% of the day); 66.7% of them succeeded.

- Decline code U16 (Risk threshold exceeded at remitter) fired 23 times — 0.156% of attempts against a trailing 0.093%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 189 | 1.278% | 1.484% |
| ZM | Invalid UPI PIN | business | Customer | 160 | 1.082% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 60 | 0.406% | 0.426% |
| XH | Account does not exist / frozen | business | Issuer | 38 | 0.257% | 0.243% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 34 | 0.230% | 0.158% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 23 | 0.156% | 0.093% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.135% | 0.165% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.135% | 0.114% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 67 | 68 |
| Auto-reversals | 29 | 18 |
| Disputes / chargebacks | 10 | 7 |
| Value returned | ₹2.69 L | ₹94,495 |

## Customer behaviour

11,945 distinct customers transacted (+34.7% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,678 | 4,311 | 1.17 | 95.94% | ₹1,170 |
| merchant_heavy | 2,768 | 3,426 | 1.24 | 95.21% | ₹929 |
| power | 2,420 | 3,370 | 1.39 | 95.52% | ₹1,527 |
| small_ticket | 1,767 | 2,280 | 1.29 | 96.10% | ₹468 |
| occasional | 1,019 | 1,076 | 1.06 | 96.84% | ₹1,479 |
| new | 267 | 294 | 1.10 | 96.94% | ₹615 |
| dormant_returning | 26 | 28 | 1.08 | 92.86% | ₹1,103 |

## Operational events

- **INC-PSP-0026** (Sev-2) — YONO SBI app release regression, scoped to YONO SBI between 18:00 and 23:00. A YONO SBI client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-BANK-0009** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 17:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **REG-0070** (Sev-3) — UPI Circle full-delegation rollout to all PSPs, scoped to UPI_CIRCLE. Full-delegation Circle became available across every major PSP, converting the pilot cohort into mainstream volume.

## Risks and opportunities

### Risks

- 29 auto-reversals were raised, 2.6 sigma above the trailing median of 18.
- Decline code U16 (Risk threshold exceeded at remitter) fired 23 times — 0.156% of attempts against a trailing 0.093%. Owner: Issuer.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

03 March was an incident day: INC-PSP-0026 was live and the rail closed at 95.78% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-03` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,785, successes=14,161, failed=609, pending=15, settled_value_inr=16,239,226.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: attempts=14,785; trailing_median=10,454; z=5.7
- psps: payer_psp=Google Pay; attempts=4,867; own_median=3,457.5; z=5.85
- categories: mcc_category=Bills; attempts=1,384; own_median=665.5; z=8.58
- psps: payer_psp=PhonePe; attempts=7,007; own_median=4,951; z=4.67
- geography: region=West; attempts=3,679; own_median=2,572; z=5.55
- banks: payer_bank=State Bank of India; attempts=4,685; own_median=3,383; z=4.53
- categories: mcc_category=Retail; attempts=3,919; own_median=2,737.5; z=3.74
- geography: region=North; attempts=3,832; own_median=2,664; z=4.76
- headline: value_inr=16,239,226; avg_ticket=1,146.76; trailing_avg_ticket=1,189.88
- incidents: event_id=INC-PSP-0026; kind=psp_degradation; severity=Sev-2; window=2026-03-02 to 2026-03-05; success_impact_pp=-9.44; volume_impact_pct=-14.77

Refs: enterprise_data/warehouse/transactions, RPT-D57-DAILY, enterprise_data/warehouse/reference/incidents.parquet
