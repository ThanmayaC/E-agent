---
id: RPT-D165-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 18 Jun 2026)

**Report ID:** RPT-D165-DAILY · **Day 165 of 206** · **Derived from:** 14,764 transaction rows queried live from the warehouse

## Summary

The rail took **14,764 payment attempts** on Thursday 18 June 2026 (Working day) and settled **₹2.19 Cr** across 14,210 successful payments. Volume was +10.1% on yesterday and +17.4% on the same weekday last week. Success closed at **96.25%**, in line with the trailing 28-day median of 96.25%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,764 | +10.1% | +17.4% | 14,832 |
| Successful payments | 14,210 | +10.6% | +17.7% | 14,291 |
| Success rate | 96.25% | +0.39pp | +0.21pp | 96.33% |
| Settled value | ₹2.19 Cr | +23.3% | +31.9% | ₹1.98 Cr |
| Average ticket | ₹1,539 | +11.5% | +12.1% | ₹1,382 |
| Technical declines | 0.481% | −0.03pp | +0.15pp | 0.398% |
| Business declines | 2.669% | −0.53pp | −0.43pp | 2.792% |
| Risk declines | 0.149% | −0.00pp | −0.02pp | 0.126% |
| Timeout declines | 0.345% | +0.17pp | +0.07pp | 0.263% |
| Retry share | 1.04% | −0.01pp | −0.20pp | 1.03% |
| Latency p95 | 1,301 ms | −1.0% | −3.0% | 1,275 ms |
| Active customers | 12,231 | +9.4% | +15.3% | 12,188 |
| Active merchants | 1,600 | +4.6% | +6.8% | 1,545 |

## What moved

- Issuer HDFC Bank ran at 97.27% success on 1,612 attempts (10.9% of the day), 0.86pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,384 | 29.7% | 95.53% | ₹48.01 L | +2.2% |
| UPI Person to Merchant | 3,378 | 22.9% | 96.09% | ₹33.70 L | −5.9% |
| UPI QR Payments | 2,458 | 16.6% | 96.22% | ₹10.80 L | +5.5% |
| UPI Lite | 2,069 | 14.0% | 98.89% | ₹1.84 L | +6.5% |
| UPI Circle | 647 | 4.4% | 97.68% | ₹5.74 L | −5.2% |
| Credit on UPI | 610 | 4.1% | 95.90% | ₹53.46 L | +47.9% |
| RuPay Credit on UPI | 364 | 2.5% | 96.43% | ₹20.55 L | −0.4% |
| UPI AutoPay | 344 | 2.3% | 91.28% | ₹6.75 L | −2.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,688 | 95.67% | 96.22% | ₹69.43 L | normal |
| HDFC Bank | 1,612 | 97.27% | 96.41% | ₹21.62 L | ⚠ outlier |
| Bank of Baroda | 1,164 | 96.22% | 96.46% | ₹19.95 L | normal |
| Axis Bank | 948 | 96.73% | 96.39% | ₹12.46 L | normal |
| Union Bank of India | 944 | 96.08% | 96.36% | ₹14.06 L | normal |
| Punjab National Bank | 888 | 95.16% | 96.27% | ₹12.72 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,999 | 96.11% | 96.14% | ₹95.46 L | normal |
| Google Pay | 4,919 | 96.16% | 96.38% | ₹80.85 L | normal |
| Paytm | 1,147 | 97.12% | 96.05% | ₹16.43 L | normal |
| Navi | 526 | 96.96% | 96.19% | ₹8.95 L | normal |
| SuperMoney | 308 | 95.45% | 96.26% | ₹3.57 L | normal |
| BHIM | 132 | 96.21% | 95.25% | ₹2.79 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,562 | 96.71% | ₹61.86 L |
| Food & Beverage | 2,540 | 97.52% | ₹14.03 L |
| Mobility | 1,252 | 96.73% | ₹6.52 L |
| Bills | 830 | 96.75% | ₹8.10 L |
| Healthcare | 552 | 95.47% | ₹12.61 L |
| Digital | 192 | 93.23% | ₹85,644 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,337 | 29.4% | 96.26% | ₹74.33 L |
| North | 3,739 | 25.3% | 96.23% | ₹49.81 L |
| West | 3,622 | 24.5% | 96.55% | ₹54.59 L |
| East | 1,730 | 11.7% | 96.47% | ₹25.40 L |
| Central | 1,336 | 9.0% | 95.13% | ₹14.63 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 43 | 97.67% | ₹3.85 L |
| Hampi Styles | Key Account | Retail | 53 | 100.00% | ₹1.90 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 97.30% | ₹1.87 L |
| Rapid Bazaar | Key Account | Retail | 428 | 97.20% | ₹1.58 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 95.89% | ₹94,944 |
| Hampi Stores 2298 | Key Account | Retail | 122 | 95.90% | ₹92,110 |
| Girnar Connect | Key Account | Bills | 155 | 96.13% | ₹79,521 |
| Tejas Restaurant | Large | Food & Beverage | 24 | 95.83% | ₹72,096 |

## Failure analysis

Of 538 declined attempts, 394 were business declines (2.669% of attempts — balances, PINs and limits), 71 technical (0.481%), 51 timeouts (0.345%) and 22 risk declines (0.149%).

153 attempts were re-presentations of an earlier failure (1.04% of the day); 72.5% of them succeeded.

- Decline code UX (Mandate execution outside permitted window) fired 15 times — 0.102% of attempts against a trailing 0.056%. Owner: PSP.
- Decline code BT (Acquirer / NPCI switch timeout) fired 22 times — 0.149% of attempts against a trailing 0.090%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 176 | 1.192% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 124 | 0.840% | 0.933% |
| ZA | Transaction declined by customer | business | Customer | 33 | 0.224% | 0.363% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.190% | 0.172% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.190% | 0.211% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.176% | 0.139% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 22 | 0.149% | 0.090% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.142% | 0.108% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 95 | 106 |
| Auto-reversals | 27 | 24 |
| Disputes / chargebacks | 14 | 13 |
| Value returned | ₹3.67 L | ₹1.70 L |

## Customer behaviour

12,231 distinct customers transacted (+1.6% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,858 | 4,430 | 1.15 | 96.46% | ₹1,634 |
| power | 2,631 | 3,549 | 1.35 | 95.72% | ₹2,042 |
| merchant_heavy | 2,771 | 3,315 | 1.20 | 96.53% | ₹1,106 |
| small_ticket | 1,825 | 2,257 | 1.24 | 96.28% | ₹617 |
| occasional | 936 | 982 | 1.05 | 96.13% | ₹2,179 |
| new | 184 | 205 | 1.11 | 96.10% | ₹863 |
| dormant_returning | 26 | 26 | 1.00 | 100.00% | ₹513 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.

## Risks and opportunities

### Risks

- Decline code UX (Mandate execution outside permitted window) fired 15 times — 0.102% of attempts against a trailing 0.056%. Owner: PSP.
- Decline code BT (Acquirer / NPCI switch timeout) fired 22 times — 0.149% of attempts against a trailing 0.090%. Owner: NPCI.
- Category Healthcare ran at 95.47% success on 552 attempts (5.3% of the day), 1.92pp down its own 28-day median.
- Region Central ran at 95.13% success on 1,336 attempts (9.0% of the day), 1.33pp down its own 28-day median.
- Issuer IndusInd Bank ran at 94.81% success on 308 attempts (2.1% of the day), 2.03pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

18 June was an unremarkable day, and that is the finding: 14,764 attempts, 96.25% success, ₹2.19 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,764, successes=14,210, failed=538, pending=16, settled_value_inr=21,875,120.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- banks: payer_bank=HDFC Bank; attempts=1,612; success_rate=97.27; own_median=96.41; z=2.83
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- failures: failure_code=UX; count=15; rate_pct=0.1; trailing_rate_pct=0.06; owner=PSP; z=2.64
- headline: value_inr=21,875,120; avg_ticket=1,539.42; trailing_avg_ticket=1,375.81
- failures: failure_code=BT; count=22; rate_pct=0.15; trailing_rate_pct=0.09; owner=NPCI; z=2.04
- categories: mcc_category=Healthcare; attempts=552; success_rate=95.47; own_median=97.4; z=-2.85
- geography: region=Central; attempts=1,336; success_rate=95.13; own_median=96.47; z=-2
- banks: payer_bank=IDFC First Bank; attempts=408; success_rate=98.53; own_median=96.25; z=2.59
- banks: payer_bank=IndusInd Bank; attempts=308; success_rate=94.81; own_median=96.84; z=-2.91
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5

Refs: enterprise_data/warehouse/transactions, RPT-D164-DAILY, enterprise_data/warehouse/reference/incidents.parquet
