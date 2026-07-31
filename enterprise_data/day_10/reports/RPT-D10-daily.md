---
id: RPT-D10-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 14 Jan 2026)

**Report ID:** RPT-D10-DAILY · **Day 10 of 206** · **Derived from:** 11,131 transaction rows queried live from the warehouse

## Summary

The rail took **11,131 payment attempts** on Wednesday 14 January 2026 (Makar Sankranti / Pongal) and settled **₹1.31 Cr** across 10,668 successful payments. Volume was +4.8% on yesterday and +6.3% on the same weekday last week. Success closed at **95.84%**, above the trailing 28-day median of 95.46%.

Product UPI Person to Person carried 4,408 attempts, 10% up its trailing median and 39.6% of the day's volume. App Google Pay carried 3,629 attempts, 5% up its trailing median and 32.6% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,131 | +4.8% | +6.3% | 10,486 |
| Successful payments | 10,668 | +5.9% | +6.5% | 9,991 |
| Success rate | 95.84% | +0.97pp | +0.15pp | 95.27% |
| Settled value | ₹1.31 Cr | +7.1% | +4.8% | ₹1.20 Cr |
| Average ticket | ₹1,230 | +1.2% | −1.6% | ₹1,196 |
| Technical declines | 0.557% | −0.11pp | +0.03pp | 0.602% |
| Business declines | 3.081% | −0.52pp | −0.15pp | 3.437% |
| Risk declines | 0.090% | −0.05pp | +0.00pp | 0.139% |
| Timeout declines | 0.305% | −0.32pp | −0.07pp | 0.405% |
| Retry share | 1.34% | −0.73pp | +0.14pp | 1.43% |
| Latency p95 | 1,224 ms | −1.0% | −3.5% | 1,240 ms |
| Active customers | 9,331 | +3.9% | +5.1% | 8,876 |
| Active merchants | 1,207 | −2.1% | −0.5% | 1,208 |

## What moved

- Product UPI Person to Person carried 4,408 attempts, 10% up its trailing median and 39.6% of the day's volume.
- App Google Pay carried 3,629 attempts, 5% up its trailing median and 32.6% of the day's volume.
- Region North carried 2,886 attempts, 9% up its trailing median and 25.9% of the day's volume.
- Attempt volume ran 3.4 standard deviations up its trailing 28-day median at 11,131, 6.3% up on the same weekday last week.
- App Paytm ran at 97.08% success on 890 attempts (8.0% of the day), 2.49pp up its own 28-day median.
- Region West ran at 95.92% success on 2,623 attempts (23.6% of the day), 1.03pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,408 | 39.6% | 95.21% | ₹47.05 L | +9.6% |
| UPI Person to Merchant | 3,215 | 28.9% | 96.67% | ₹32.36 L | +7.3% |
| UPI QR Payments | 1,843 | 16.6% | 96.09% | ₹7.96 L | +3.5% |
| UPI Lite | 637 | 5.7% | 98.27% | ₹61,024 | −8.5% |
| UPI AutoPay | 304 | 2.7% | 90.46% | ₹5.69 L | +0.0% |
| RuPay Credit on UPI | 180 | 1.6% | 96.11% | ₹7.11 L | −6.2% |
| Credit on UPI | 158 | 1.4% | 95.57% | ₹13.33 L | +9.0% |
| UPI Circle | 84 | 0.8% | 97.62% | ₹69,249 | −8.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,508 | 95.38% | 95.12% | ₹43.09 L | normal |
| HDFC Bank | 1,230 | 96.34% | 96.17% | ₹17.07 L | normal |
| Bank of Baroda | 849 | 96.00% | 94.72% | ₹9.46 L | normal |
| Union Bank of India | 803 | 96.39% | 95.02% | ₹10.11 L | normal |
| Axis Bank | 704 | 95.03% | 95.44% | ₹7.69 L | normal |
| ICICI Bank | 672 | 97.47% | 95.17% | ₹8.46 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,288 | 95.97% | 95.47% | ₹60.99 L | normal |
| Google Pay | 3,629 | 95.34% | 95.56% | ₹45.94 L | normal |
| Paytm | 890 | 97.08% | 94.59% | ₹9.27 L | ⚠ outlier |
| Navi | 415 | 96.39% | 95.03% | ₹5.61 L | normal |
| SuperMoney | 220 | 92.73% | 96.10% | ₹1.72 L | ⚠ outlier |
| BHIM | 131 | 99.24% | 95.33% | ₹1.39 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,244 | 96.24% | ₹38.75 L |
| Food & Beverage | 1,470 | 97.48% | ₹7.80 L |
| Mobility | 596 | 96.81% | ₹3.42 L |
| Bills | 582 | 96.56% | ₹5.61 L |
| Healthcare | 323 | 96.59% | ₹2.48 L |
| Digital | 184 | 95.65% | ₹1.06 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,259 | 29.3% | 95.98% | ₹39.36 L |
| North | 2,886 | 25.9% | 95.70% | ₹34.95 L |
| West | 2,623 | 23.6% | 95.92% | ₹31.43 L |
| East | 1,312 | 11.8% | 95.58% | ₹16.72 L |
| Central | 1,051 | 9.4% | 95.91% | ₹8.77 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 103 | 94.17% | ₹1.51 L |
| Rapid Bazaar | Key Account | Retail | 346 | 97.11% | ₹1.31 L |
| Hampi Stores 2298 | Key Account | Retail | 107 | 97.20% | ₹99,584 |
| Vega Electronics | Large | Retail | 29 | 89.66% | ₹94,657 |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 97.26% | ₹69,985 |
| Ujjwal Water Board | Key Account | Bills | 27 | 92.59% | ₹55,590 |
| Urban Boutique | Key Account | Retail | 92 | 95.65% | ₹52,457 |
| Trinetra Restaurant | Large | Food & Beverage | 25 | 100.00% | ₹50,735 |

## Failure analysis

Of 449 declined attempts, 343 were business declines (3.081% of attempts — balances, PINs and limits), 62 technical (0.557%), 34 timeouts (0.305%) and 10 risk declines (0.090%).

149 attempts were re-presentations of an earlier failure (1.34% of the day); 69.1% of them succeeded.

- Decline code U69 (Beneficiary bank offline) fired 19 times — 0.171% of attempts against a trailing 0.105%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 153 | 1.375% | 1.459% |
| ZM | Invalid UPI PIN | business | Customer | 113 | 1.015% | 1.095% |
| ZA | Transaction declined by customer | business | Customer | 35 | 0.314% | 0.371% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.216% | 0.262% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.216% | 0.264% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.189% | 0.183% |
| U69 | Beneficiary bank offline | technical | Issuer | 19 | 0.171% | 0.105% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.126% | 0.173% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 41 | 19 |
| Auto-reversals | 36 | 22 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹3.44 L | ₹40,132 |

## Customer behaviour

9,331 distinct customers transacted (+5.1% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,866 | 3,238 | 1.13 | 95.65% | ₹1,384 |
| power | 1,996 | 2,695 | 1.35 | 96.03% | ₹1,549 |
| merchant_heavy | 2,112 | 2,497 | 1.18 | 96.56% | ₹997 |
| small_ticket | 1,393 | 1,681 | 1.21 | 94.94% | ₹506 |
| occasional | 743 | 783 | 1.05 | 95.02% | ₹1,232 |
| new | 191 | 206 | 1.08 | 97.57% | ₹675 |
| dormant_returning | 30 | 31 | 1.03 | 100.00% | ₹672 |

## Operational events

- **INC-BANK-0017** (Sev-2) — State Bank of India issuer decline spike, scoped to State Bank of India between 19:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-PSP-0034** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.

## Risks and opportunities

### Risks

- 36 auto-reversals were raised, 3.1 sigma above the trailing median of 22.
- Decline code U69 (Beneficiary bank offline) fired 19 times — 0.171% of attempts against a trailing 0.105%. Owner: Issuer.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

14 January was an incident day: INC-BANK-0017, INC-PSP-0034 were live and the rail closed at 95.84% success against a 95.46% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,131, successes=10,668, failed=449, pending=14, settled_value_inr=13,124,341.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Person to Person; attempts=4,408; own_median=4,021; z=7.68
- psps: payer_psp=Google Pay; attempts=3,629; own_median=3,461; z=8.09
- geography: region=North; attempts=2,886; own_median=2,639; z=8.33
- headline: attempts=11,131; trailing_median=10,484; z=3.44
- adjustments: reversals=36; trailing_median=22; z=3.15
- incidents: event_id=INC-BANK-0017; kind=bank_outage; severity=Sev-2; window=2026-01-12 to 2026-01-14; success_impact_pp=-16.02; volume_impact_pct=-14.21
- incidents: event_id=INC-PSP-0034; kind=psp_degradation; severity=Sev-2; window=2026-01-12 to 2026-01-15; success_impact_pp=-6.55; volume_impact_pct=-10.26
- psps: payer_psp=Paytm; attempts=890; success_rate=97.08; own_median=94.59; z=4.41
- geography: region=West; attempts=2,623; success_rate=95.92; own_median=94.89; z=2.56
- products: product_name=UPI Person to Merchant; attempts=3,215; success_rate=96.67; own_median=95.74; z=2.09

Refs: enterprise_data/warehouse/transactions, RPT-D09-DAILY, enterprise_data/warehouse/reference/incidents.parquet
