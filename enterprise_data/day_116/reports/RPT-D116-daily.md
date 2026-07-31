---
id: RPT-D116-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-30T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 30 Apr 2026)

**Report ID:** RPT-D116-DAILY · **Day 116 of 206** · **Derived from:** 13,971 transaction rows queried live from the warehouse

## Summary

The rail took **13,971 payment attempts** on Thursday 30 April 2026 (Working day) and settled **₹2.00 Cr** across 13,203 successful payments. Volume was +2.9% on yesterday and +22.0% on the same weekday last week. Success closed at **94.50%**, below the trailing 28-day median of 95.53%.

Decline code U54 (Transaction timed out at beneficiary) fired 114 times — 0.816% of attempts against a trailing 0.199%. Owner: Issuer. Decline code BT (Acquirer / NPCI switch timeout) fired 62 times — 0.444% of attempts against a trailing 0.109%. Owner: NPCI.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,971 | +2.9% | +22.0% | 12,732 |
| Successful payments | 13,203 | +1.4% | +20.9% | 12,135 |
| Success rate | 94.50% | −1.49pp | −0.87pp | 95.28% |
| Settled value | ₹2.00 Cr | +2.7% | +23.8% | ₹1.65 Cr |
| Average ticket | ₹1,511 | +1.3% | +2.4% | ₹1,363 |
| Technical declines | 0.930% | +0.44pp | +0.35pp | 0.595% |
| Business declines | 2.899% | +0.01pp | −0.52pp | 3.216% |
| Risk declines | 0.115% | −0.06pp | −0.07pp | 0.139% |
| Timeout declines | 1.474% | +1.16pp | +1.14pp | 0.659% |
| Retry share | 2.39% | +0.99pp | +1.08pp | 1.66% |
| Latency p95 | 1,548 ms | +21.2% | +19.5% | 1,338 ms |
| Active customers | 11,437 | +1.5% | +17.6% | 10,580 |
| Active merchants | 1,463 | −1.1% | +7.2% | 1,393 |

## What moved

- Product UPI Person to Person ran at 93.64% success on 4,922 attempts (35.2% of the day), 1.31pp down its own 28-day median.
- Success rate closed at 94.50%, 1.03pp down the trailing median — a 1.7-sigma move.
- Product Credit on UPI is compounding — attempts up 47% across the trailing window to 402 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- App Google Pay ran at 94.18% success on 4,620 attempts (33.1% of the day), 1.32pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 43% across the trailing window to 419 today, with success holding, so the growth is healthy and worth funding.
- Category Mobility ran at 95.37% success on 1,036 attempts (11.4% of the day), 1.37pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,922 | 35.2% | 93.64% | ₹53.76 L | +16.7% |
| UPI Person to Merchant | 3,487 | 25.0% | 94.84% | ₹36.71 L | +5.3% |
| UPI QR Payments | 2,353 | 16.8% | 95.16% | ₹9.73 L | +8.4% |
| UPI Lite | 1,289 | 9.2% | 97.52% | ₹1.20 L | +11.8% |
| UPI Circle | 419 | 3.0% | 96.18% | ₹3.74 L | +39.7% |
| Credit on UPI | 402 | 2.9% | 92.29% | ₹34.54 L | +81.5% |
| RuPay Credit on UPI | 400 | 2.9% | 94.00% | ₹27.94 L | +22.0% |
| UPI AutoPay | 304 | 2.2% | 88.82% | ₹5.85 L | −6.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,374 | 94.86% | 95.59% | ₹67.06 L | normal |
| HDFC Bank | 1,542 | 93.97% | 95.95% | ₹19.81 L | ⚠ outlier |
| Bank of Baroda | 1,080 | 93.98% | 95.83% | ₹15.64 L | ⚠ outlier |
| Union Bank of India | 992 | 92.84% | 94.99% | ₹12.92 L | normal |
| Punjab National Bank | 874 | 94.51% | 95.57% | ₹9.84 L | normal |
| ICICI Bank | 852 | 95.66% | 96.26% | ₹17.28 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,615 | 94.83% | 95.78% | ₹95.80 L | normal |
| Google Pay | 4,620 | 94.18% | 95.50% | ₹65.02 L | ⚠ outlier |
| Paytm | 1,122 | 94.47% | 95.36% | ₹18.21 L | normal |
| Navi | 547 | 93.60% | 95.94% | ₹6.19 L | normal |
| SuperMoney | 271 | 95.57% | 95.13% | ₹3.06 L | normal |
| BHIM | 126 | 89.68% | 96.11% | ₹1.41 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,641 | 95.39% | ₹50.19 L |
| Food & Beverage | 2,085 | 95.44% | ₹10.21 L |
| Bills | 1,160 | 95.09% | ₹12.88 L |
| Mobility | 1,036 | 95.37% | ₹7.24 L |
| Healthcare | 448 | 94.64% | ₹6.97 L |
| Digital | 248 | 92.34% | ₹1.67 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,058 | 29.0% | 94.48% | ₹58.06 L |
| North | 3,606 | 25.8% | 94.59% | ₹42.94 L |
| West | 3,446 | 24.7% | 94.69% | ₹63.02 L |
| East | 1,650 | 11.8% | 94.97% | ₹21.64 L |
| Central | 1,211 | 8.7% | 93.15% | ₹13.88 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 67 | 94.03% | ₹2.06 L |
| Ujjwal Water Board | Key Account | Bills | 63 | 96.83% | ₹1.84 L |
| Rapid Bazaar | Key Account | Retail | 369 | 93.77% | ₹1.61 L |
| Vega Electronics | Large | Retail | 28 | 92.86% | ₹1.19 L |
| Girnar Connect | Key Account | Bills | 196 | 94.90% | ₹94,308 |
| Hampi Stores 2298 | Key Account | Retail | 122 | 95.90% | ₹76,581 |
| Yamuna Restaurant | Key Account | Food & Beverage | 64 | 90.62% | ₹67,268 |
| Hampi Styles | Key Account | Retail | 39 | 84.62% | ₹66,577 |

## Failure analysis

Of 757 declined attempts, 405 were business declines (2.899% of attempts — balances, PINs and limits), 130 technical (0.930%), 206 timeouts (1.474%) and 16 risk declines (0.115%).

334 attempts were re-presentations of an earlier failure (2.39% of the day); 48.8% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 114 times — 0.816% of attempts against a trailing 0.199%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 62 times — 0.444% of attempts against a trailing 0.109%. Owner: NPCI.
- Retries reached 334 attempts (2.39% of the day, 3.7 sigma above normal). Only 48.8% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 30 times — 0.215% of attempts against a trailing 0.047%. Owner: NPCI.
- Decline code U30 (Debit failed at remitter bank) fired 53 times — 0.379% of attempts against a trailing 0.212%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 161 | 1.152% | 1.313% |
| ZM | Invalid UPI PIN | business | Customer | 147 | 1.052% | 1.040% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 114 | 0.816% | 0.199% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 62 | 0.444% | 0.109% |
| U30 | Debit failed at remitter bank | technical | Issuer | 53 | 0.379% | 0.212% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.322% | 0.393% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 30 | 0.215% | 0.047% |
| U28 | Remitter bank unavailable | technical | Issuer | 30 | 0.215% | 0.119% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 84 | 81 |
| Auto-reversals | 52 | 27 |
| Disputes / chargebacks | 10 | 11 |
| Value returned | ₹2.31 L | ₹1.41 L |

## Customer behaviour

11,437 distinct customers transacted (+11.1% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,520 | 4,046 | 1.15 | 94.83% | ₹1,416 |
| power | 2,443 | 3,311 | 1.36 | 94.35% | ₹1,895 |
| merchant_heavy | 2,630 | 3,269 | 1.24 | 94.25% | ₹1,167 |
| small_ticket | 1,692 | 2,116 | 1.25 | 94.33% | ₹791 |
| occasional | 912 | 974 | 1.07 | 94.46% | ₹2,023 |
| new | 199 | 213 | 1.07 | 96.71% | ₹1,999 |
| dormant_returning | 41 | 42 | 1.02 | 92.86% | ₹1,565 |

## Operational events

- **INC-PSP-0027** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-NET-0041** (Sev-2) — NPCI switch latency degradation, scoped to ecosystem-wide between 18:00 and 20:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **INC-PSP-0032** (Sev-3) — Google Pay app release regression, scoped to Google Pay between 19:00 and 23:00. A Google Pay client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0050** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U54 (Transaction timed out at beneficiary) fired 114 times — 0.816% of attempts against a trailing 0.199%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 62 times — 0.444% of attempts against a trailing 0.109%. Owner: NPCI.
- Retries reached 334 attempts (2.39% of the day, 3.7 sigma above normal). Only 48.8% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 30 times — 0.215% of attempts against a trailing 0.047%. Owner: NPCI.
- Decline code U30 (Debit failed at remitter bank) fired 53 times — 0.379% of attempts against a trailing 0.212%. Owner: Issuer.

### Opportunities

- Product UPI Circle is compounding — attempts up 43% across the trailing window to 419 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

30 April was an incident day: INC-PSP-0027, INC-NET-0041 were live and the rail closed at 94.50% success against a 95.53% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-30` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,971, successes=13,203, failed=757, pending=11, settled_value_inr=19,953,471.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U54; count=114; rate_pct=0.82; trailing_rate_pct=0.2; owner=Issuer; z=11.1
- failures: failure_code=BT; count=62; rate_pct=0.44; trailing_rate_pct=0.11; owner=NPCI; z=7.6
- failures: retries=334; retry_share_pct=2.39; recovery_pct=48.8; z=3.66
- failures: failure_code=U67; count=30; rate_pct=0.21; trailing_rate_pct=0.05; owner=NPCI; z=5.86
- failures: failure_code=U30; count=53; rate_pct=0.38; trailing_rate_pct=0.21; owner=Issuer; z=3.59
- incidents: event_id=INC-PSP-0027; kind=psp_degradation; severity=Sev-2; window=2026-04-27 to 2026-04-30; success_impact_pp=-11.27; volume_impact_pct=-17.63
- incidents: event_id=INC-NET-0041; kind=network_latency; severity=Sev-2; window=2026-04-30 to 2026-05-01; success_impact_pp=-9.26; volume_impact_pct=-8.54
- products: product_name=UPI Person to Person; attempts=4,922; success_rate=93.64; own_median=94.95; z=-2.56
- adjustments: reversals=52; trailing_median=27; z=2.59
- headline: success_rate=94.5; trailing_median=95.53; z=-1.7

Refs: enterprise_data/warehouse/transactions, RPT-D115-DAILY, enterprise_data/warehouse/reference/incidents.parquet
