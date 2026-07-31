---
id: RPT-D08-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 12 Jan 2026)

**Report ID:** RPT-D08-DAILY · **Day 8 of 206** · **Derived from:** 10,484 transaction rows queried live from the warehouse

## Summary

The rail took **10,484 payment attempts** on Monday 12 January 2026 (Working day) and settled **₹1.12 Cr** across 9,873 successful payments. Volume was +17.0% on yesterday and −1.2% on the same weekday last week. Success closed at **94.17%**, below the trailing 28-day median of 95.47%.

2 disputes were raised, 2000000000.0 sigma above the trailing median of 0. Retries reached 225 attempts (2.15% of the day, 5.8 sigma above normal). Only 49.3% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,484 | +17.0% | −1.2% | 10,388 |
| Successful payments | 9,873 | +16.9% | −2.9% | 9,896 |
| Success rate | 94.17% | −0.14pp | −1.61pp | 95.25% |
| Settled value | ₹1.12 Cr | +21.0% | −19.8% | ₹1.18 Cr |
| Average ticket | ₹1,134 | +3.6% | −17.5% | ₹1,190 |
| Technical declines | 0.830% | +0.06pp | +0.36pp | 0.599% |
| Business declines | 4.054% | −0.28pp | +0.98pp | 3.462% |
| Risk declines | 0.143% | −0.01pp | −0.04pp | 0.144% |
| Timeout declines | 0.534% | +0.21pp | +0.25pp | 0.390% |
| Retry share | 2.15% | +0.38pp | +1.51pp | 1.37% |
| Latency p95 | 1,267 ms | +5.0% | −0.4% | 1,243 ms |
| Active customers | 8,830 | +14.1% | −1.9% | 8,805 |
| Active merchants | 1,210 | +5.8% | −1.4% | 1,205 |

## What moved

- Success rate closed at 94.17%, 1.30pp down the trailing median — a 4.4-sigma move.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,046 | 38.6% | 93.28% | ₹42.23 L | +0.6% |
| UPI Person to Merchant | 2,996 | 28.6% | 95.36% | ₹24.87 L | +3.7% |
| UPI QR Payments | 1,822 | 17.4% | 94.40% | ₹6.85 L | +4.5% |
| UPI Lite | 614 | 5.9% | 98.53% | ₹55,297 | −14.1% |
| UPI AutoPay | 304 | 2.9% | 87.17% | ₹4.53 L | +2.0% |
| RuPay Credit on UPI | 192 | 1.8% | 94.79% | ₹10.42 L | −1.5% |
| Credit on UPI | 145 | 1.4% | 94.48% | ₹9.84 L | +1.4% |
| Recurring Payments | 91 | 0.9% | 80.22% | ₹3.52 L | +11.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,303 | 94.31% | 95.35% | ₹36.69 L | ⚠ outlier |
| HDFC Bank | 1,131 | 93.72% | 96.17% | ₹15.41 L | ⚠ outlier |
| Bank of Baroda | 777 | 92.66% | 95.74% | ₹8.27 L | ⚠ outlier |
| Union Bank of India | 758 | 94.72% | 95.16% | ₹9.55 L | normal |
| Axis Bank | 629 | 95.71% | 95.44% | ₹7.33 L | normal |
| ICICI Bank | 626 | 94.73% | 95.17% | ₹5.71 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,012 | 94.07% | 95.55% | ₹52.11 L | ⚠ outlier |
| Google Pay | 3,471 | 93.92% | 95.60% | ₹37.20 L | ⚠ outlier |
| Paytm | 846 | 94.21% | 94.78% | ₹9.15 L | normal |
| Navi | 362 | 95.03% | 95.89% | ₹3.43 L | normal |
| SuperMoney | 211 | 94.31% | 96.14% | ₹4.11 L | ⚠ outlier |
| BHIM | 98 | 96.94% | 95.33% | ₹1.06 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,939 | 95.30% | ₹28.45 L |
| Food & Beverage | 1,481 | 95.88% | ₹6.69 L |
| Mobility | 639 | 93.11% | ₹3.49 L |
| Bills | 559 | 95.71% | ₹5.49 L |
| Healthcare | 344 | 94.77% | ₹3.88 L |
| Digital | 180 | 91.67% | ₹76,079 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,085 | 29.4% | 93.42% | ₹35.83 L |
| North | 2,633 | 25.1% | 94.08% | ₹28.36 L |
| West | 2,555 | 24.4% | 94.68% | ₹26.46 L |
| East | 1,237 | 11.8% | 94.10% | ₹13.45 L |
| Central | 974 | 9.3% | 95.59% | ₹7.88 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Hampi Stores 2298 | Key Account | Retail | 80 | 98.75% | ₹2.27 L |
| Vasant Wardrobe | Key Account | Retail | 77 | 96.10% | ₹1.76 L |
| Rapid Bazaar | Key Account | Retail | 310 | 94.19% | ₹1.65 L |
| Vega Electronics | Large | Retail | 28 | 92.86% | ₹1.34 L |
| Shakti Stores 1531 | Key Account | Retail | 78 | 98.72% | ₹52,756 |
| Urban Boutique | Key Account | Retail | 84 | 94.05% | ₹44,147 |
| Girnar Connect | Key Account | Bills | 100 | 96.00% | ₹41,568 |
| Ujjwal Water Board | Key Account | Bills | 28 | 92.86% | ₹39,880 |

## Failure analysis

Of 583 declined attempts, 425 were business declines (4.054% of attempts — balances, PINs and limits), 87 technical (0.830%), 56 timeouts (0.534%) and 15 risk declines (0.143%).

225 attempts were re-presentations of an earlier failure (2.15% of the day); 49.3% of them succeeded.

- Retries reached 225 attempts (2.15% of the day, 5.8 sigma above normal). Only 49.3% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.669% | 1.459% |
| ZM | Invalid UPI PIN | business | Customer | 162 | 1.545% | 1.088% |
| U30 | Debit failed at remitter bank | technical | Issuer | 43 | 0.410% | 0.260% |
| ZA | Transaction declined by customer | business | Customer | 40 | 0.382% | 0.361% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.296% | 0.234% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.248% | 0.181% |
| U28 | Remitter bank unavailable | technical | Issuer | 22 | 0.210% | 0.152% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 21 | 0.200% | 0.131% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 32 | 17 |
| Auto-reversals | 22 | 21 |
| Disputes / chargebacks | 2 | 0 |
| Value returned | ₹99,753 | ₹26,925 |

## Customer behaviour

8,830 distinct customers transacted (−0.5% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,639 | 3,007 | 1.14 | 95.08% | ₹1,212 |
| power | 1,885 | 2,478 | 1.31 | 93.46% | ₹1,519 |
| merchant_heavy | 2,008 | 2,386 | 1.19 | 93.80% | ₹813 |
| small_ticket | 1,343 | 1,611 | 1.20 | 94.17% | ₹514 |
| occasional | 737 | 770 | 1.04 | 93.64% | ₹1,129 |
| new | 189 | 203 | 1.07 | 95.07% | ₹657 |
| dormant_returning | 29 | 29 | 1.00 | 100.00% | ₹666 |

## Operational events

- **INC-BANK-0017** (Sev-2) — State Bank of India issuer decline spike, scoped to State Bank of India between 19:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-PSP-0034** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-PSP-0023** (Sev-3) — FamApp app release regression, scoped to FamApp between 19:00 and 23:00. A FamApp client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.

## Risks and opportunities

### Risks

- 2 disputes were raised, 2000000000.0 sigma above the trailing median of 0.
- Retries reached 225 attempts (2.15% of the day, 5.8 sigma above normal). Only 49.3% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Success rate closed at 94.17%, 1.30pp down the trailing median — a 4.4-sigma move.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

12 January was an incident day: INC-BANK-0017, INC-PSP-0034 were live and the rail closed at 94.17% success against a 95.47% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,484, successes=9,873, failed=583, pending=28, settled_value_inr=11,197,620.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=2; trailing_median=0; z=2,000,000,000
- failures: retries=225; retry_share_pct=2.15; recovery_pct=49.33; z=5.79
- headline: success_rate=94.17; trailing_median=95.47; z=-4.38
- incidents: event_id=INC-BANK-0017; kind=bank_outage; severity=Sev-2; window=2026-01-12 to 2026-01-14; success_impact_pp=-16.02; volume_impact_pct=-14.21
- incidents: event_id=INC-PSP-0034; kind=psp_degradation; severity=Sev-2; window=2026-01-12 to 2026-01-15; success_impact_pp=-6.55; volume_impact_pct=-10.26
- incidents: event_id=INC-PSP-0023; kind=psp_degradation; severity=Sev-3; window=2026-01-10 to 2026-01-12; success_impact_pp=-3.76; volume_impact_pct=-5.89

Refs: enterprise_data/warehouse/transactions, RPT-D07-DAILY, enterprise_data/warehouse/reference/incidents.parquet
