---
id: RPT-D06-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 10 Jan 2026)

**Report ID:** RPT-D06-DAILY · **Day 6 of 206** · **Derived from:** 11,449 transaction rows queried live from the warehouse

## Summary

The rail took **11,449 payment attempts** on Saturday 10 January 2026 (Weekend) and settled **₹1.20 Cr** across 10,926 successful payments. Volume was +10.2% on yesterday and — on the same weekday last week. Success closed at **95.43%**, in line with the trailing 28-day median of 95.67%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,449 | +10.2% | — | 10,610 |
| Successful payments | 10,926 | +9.9% | — | 10,141 |
| Success rate | 95.43% | −0.24pp | — | 95.58% |
| Settled value | ₹1.20 Cr | +6.8% | — | ₹1.23 Cr |
| Average ticket | ₹1,099 | −2.8% | — | ₹1,215 |
| Technical declines | 0.568% | −0.01pp | — | 0.532% |
| Business declines | 3.441% | +0.37pp | — | 3.219% |
| Risk declines | 0.061% | −0.10pp | — | 0.143% |
| Timeout declines | 0.367% | −0.06pp | — | 0.378% |
| Retry share | 1.30% | +0.10pp | — | 1.17% |
| Latency p95 | 1,192 ms | −4.0% | — | 1,245 ms |
| Active customers | 9,569 | +9.0% | — | 8,980 |
| Active merchants | 1,242 | +5.7% | — | 1,214 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,313 | 37.7% | 94.74% | ₹42.77 L | +7.3% |
| UPI Person to Merchant | 3,182 | 27.8% | 96.04% | ₹36.82 L | +10.2% |
| UPI QR Payments | 2,111 | 18.4% | 95.97% | ₹8.01 L | +21.0% |
| UPI Lite | 904 | 7.9% | 98.34% | ₹81,708 | +26.4% |
| UPI AutoPay | 337 | 2.9% | 89.32% | ₹4.83 L | +14.6% |
| RuPay Credit on UPI | 133 | 1.2% | 95.49% | ₹4.59 L | −36.1% |
| UPI Circle | 126 | 1.1% | 98.41% | ₹1.07 L | +31.2% |
| UPI Lite Auto Top-Up | 80 | 0.7% | 96.25% | ₹80,382 | −4.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,624 | 94.87% | 95.38% | ₹38.43 L | normal |
| HDFC Bank | 1,308 | 96.25% | 96.17% | ₹13.53 L | normal |
| Bank of Baroda | 830 | 95.78% | 95.74% | ₹8.50 L | normal |
| Union Bank of India | 762 | 96.19% | 95.16% | ₹7.71 L | normal |
| Axis Bank | 723 | 95.44% | 96.01% | ₹10.52 L | normal |
| ICICI Bank | 704 | 94.03% | 96.11% | ₹6.20 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,415 | 95.24% | 95.62% | ₹53.16 L | normal |
| Google Pay | 3,835 | 95.72% | 95.60% | ₹46.06 L | normal |
| Paytm | 900 | 94.78% | 95.92% | ₹8.47 L | normal |
| Navi | 401 | 96.51% | 95.89% | ₹3.80 L | normal |
| SuperMoney | 230 | 96.52% | 95.75% | ₹1.82 L | normal |
| BHIM | 127 | 91.34% | 95.50% | ₹1.28 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,975 | 95.76% | ₹29.57 L |
| Food & Beverage | 1,776 | 96.90% | ₹7.70 L |
| Mobility | 792 | 96.59% | ₹3.76 L |
| Bills | 670 | 96.27% | ₹7.86 L |
| Healthcare | 395 | 95.95% | ₹4.40 L |
| Digital | 209 | 93.78% | ₹1.25 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,372 | 29.5% | 95.67% | ₹36.72 L |
| North | 2,886 | 25.2% | 95.22% | ₹28.64 L |
| West | 2,813 | 24.6% | 95.17% | ₹31.23 L |
| East | 1,373 | 12.0% | 95.92% | ₹14.55 L |
| Central | 1,005 | 8.8% | 95.32% | ₹8.94 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 319 | 96.55% | ₹1.69 L |
| Ujjwal Water Board | Key Account | Bills | 44 | 100.00% | ₹1.36 L |
| Vega Electronics | Large | Retail | 15 | 100.00% | ₹1.32 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 76 | 98.68% | ₹71,268 |
| Girnar Connect | Key Account | Bills | 99 | 94.95% | ₹48,553 |
| Urban Boutique | Key Account | Retail | 74 | 94.59% | ₹48,212 |
| Swift Mart 1738 | Key Account | Retail | 110 | 98.18% | ₹44,619 |
| Hampi Stores 2298 | Key Account | Retail | 89 | 94.38% | ₹44,207 |

## Failure analysis

Of 508 declined attempts, 394 were business declines (3.441% of attempts — balances, PINs and limits), 65 technical (0.568%), 42 timeouts (0.367%) and 7 risk declines (0.061%).

149 attempts were re-presentations of an earlier failure (1.30% of the day); 71.8% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 167 | 1.459% | 1.409% |
| ZM | Invalid UPI PIN | business | Customer | 121 | 1.057% | 1.088% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.480% | 0.349% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.288% | 0.210% |
| U30 | Debit failed at remitter bank | technical | Issuer | 30 | 0.262% | 0.254% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.183% | 0.134% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.148% | 0.183% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.131% | 0.117% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 22 | 7 |
| Auto-reversals | 25 | 19 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹50,185 | ₹26,765 |

## Customer behaviour

9,569 distinct customers transacted (+7.8% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,914 | 3,329 | 1.14 | 95.43% | ₹1,139 |
| power | 1,993 | 2,655 | 1.33 | 95.89% | ₹1,354 |
| merchant_heavy | 2,165 | 2,589 | 1.20 | 95.52% | ₹1,004 |
| small_ticket | 1,489 | 1,815 | 1.22 | 95.65% | ₹521 |
| occasional | 785 | 832 | 1.06 | 93.27% | ₹1,166 |
| new | 198 | 204 | 1.03 | 96.08% | ₹460 |
| dormant_returning | 25 | 25 | 1.00 | 88.00% | ₹504 |

## Operational events

- **INC-PSP-0023** (Sev-3) — FamApp app release regression, scoped to FamApp between 19:00 and 23:00. A FamApp client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

10 January was an unremarkable day, and that is the finding: 11,449 attempts, 95.43% success, ₹1.20 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,449, successes=10,926, failed=508, pending=15, settled_value_inr=12,008,246.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-PSP-0023; kind=psp_degradation; severity=Sev-3; window=2026-01-10 to 2026-01-12; success_impact_pp=-3.76; volume_impact_pct=-5.89

Refs: enterprise_data/warehouse/transactions, RPT-D05-DAILY, enterprise_data/warehouse/reference/incidents.parquet
