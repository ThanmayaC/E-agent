---
id: RPT-D07-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 11 Jan 2026)

**Report ID:** RPT-D07-DAILY · **Day 7 of 206** · **Derived from:** 8,959 transaction rows queried live from the warehouse

## Summary

The rail took **8,959 payment attempts** on Sunday 11 January 2026 (Weekend) and settled **₹92.51 L** across 8,449 successful payments. Volume was −21.7% on yesterday and — on the same weekday last week. Success closed at **94.31%**, below the trailing 28-day median of 95.57%.

Success rate closed at 94.31%, 1.26pp down the trailing median — a 7.3-sigma move. Retries reached 158 attempts (1.76% of the day, 6.0 sigma above normal). 66.5% of re-presented payments recovered, so the retry path was doing its job.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 8,959 | −21.7% | — | 10,374 |
| Successful payments | 8,449 | −22.7% | — | 9,900 |
| Success rate | 94.31% | −1.12pp | — | 95.40% |
| Settled value | ₹92.51 L | −23.0% | — | ₹1.19 Cr |
| Average ticket | ₹1,095 | −0.4% | — | ₹1,198 |
| Technical declines | 0.770% | +0.20pp | — | 0.566% |
| Business declines | 4.331% | +0.89pp | — | 3.377% |
| Risk declines | 0.156% | +0.10pp | — | 0.145% |
| Timeout declines | 0.324% | −0.04pp | — | 0.370% |
| Retry share | 1.76% | +0.46pp | — | 1.26% |
| Latency p95 | 1,206 ms | +1.2% | — | 1,239 ms |
| Active customers | 7,736 | −19.2% | — | 8,802 |
| Active merchants | 1,144 | −7.9% | — | 1,204 |

## What moved

- Success rate closed at 94.31%, 1.26pp down the trailing median — a 7.3-sigma move.
- Attempt volume ran 9.3 standard deviations down its trailing 28-day median at 8,959, nan% down on the same weekday last week.
- Settled value moved down while volume moved down — average ticket at ₹1,095 against a trailing ₹1,217, so the day's shape is a mix shift rather than a demand shift.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,303 | 36.9% | 93.61% | ₹33.70 L | −17.9% |
| UPI Person to Merchant | 2,609 | 29.1% | 95.17% | ₹25.02 L | −12.7% |
| UPI QR Payments | 1,524 | 17.0% | 95.21% | ₹5.33 L | −13.5% |
| UPI Lite | 671 | 7.5% | 98.66% | ₹56,456 | −6.7% |
| UPI AutoPay | 298 | 3.3% | 86.24% | ₹4.83 L | −0.7% |
| RuPay Credit on UPI | 116 | 1.3% | 90.52% | ₹5.25 L | −42.4% |
| UPI Circle | 92 | 1.0% | 95.65% | ₹80,081 | −6.1% |
| Recurring Payments | 92 | 1.0% | 84.78% | ₹4.09 L | +13.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,891 | 94.64% | 95.36% | ₹27.37 L | ⚠ outlier |
| HDFC Bank | 990 | 94.24% | 96.17% | ₹11.25 L | ⚠ outlier |
| Bank of Baroda | 625 | 94.72% | 95.76% | ₹6.57 L | normal |
| Union Bank of India | 611 | 93.29% | 95.66% | ₹5.48 L | ⚠ outlier |
| ICICI Bank | 556 | 94.42% | 95.64% | ₹7.07 L | normal |
| Axis Bank | 526 | 95.25% | 95.72% | ₹9.32 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,212 | 93.78% | 95.58% | ₹42.41 L | ⚠ outlier |
| Google Pay | 2,977 | 94.86% | 95.66% | ₹31.50 L | ⚠ outlier |
| Paytm | 755 | 93.91% | 95.35% | ₹6.94 L | normal |
| Navi | 321 | 94.39% | 95.95% | ₹4.67 L | ⚠ outlier |
| SuperMoney | 199 | 96.48% | 95.95% | ₹2.82 L | normal |
| BHIM | 84 | 92.86% | 95.41% | ₹58,472 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,268 | 94.84% | ₹21.02 L |
| Food & Beverage | 1,405 | 95.94% | ₹5.97 L |
| Mobility | 647 | 96.29% | ₹3.43 L |
| Bills | 560 | 95.71% | ₹7.31 L |
| Healthcare | 303 | 94.06% | ₹1.46 L |
| Digital | 188 | 88.83% | ₹1.15 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,677 | 29.9% | 94.77% | ₹27.47 L |
| North | 2,251 | 25.1% | 93.91% | ₹24.55 L |
| West | 2,211 | 24.7% | 93.58% | ₹21.62 L |
| East | 1,054 | 11.8% | 94.69% | ₹12.90 L |
| Central | 766 | 8.6% | 95.43% | ₹5.98 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 26 | 100.00% | ₹3.88 L |
| Rapid Bazaar | Key Account | Retail | 245 | 96.73% | ₹92,959 |
| Vasant Wardrobe | Key Account | Retail | 46 | 82.61% | ₹68,970 |
| Ujjwal Water Board | Key Account | Bills | 27 | 92.59% | ₹53,950 |
| Swift Mart 1738 | Key Account | Retail | 75 | 93.33% | ₹48,814 |
| Girnar Connect | Key Account | Bills | 82 | 97.56% | ₹43,700 |
| Yamuna Restaurant | Key Account | Food & Beverage | 56 | 92.86% | ₹42,269 |
| Hampi Stores 2298 | Key Account | Retail | 85 | 95.29% | ₹38,262 |

## Failure analysis

Of 500 declined attempts, 388 were business declines (4.331% of attempts — balances, PINs and limits), 69 technical (0.770%), 29 timeouts (0.324%) and 14 risk declines (0.156%).

158 attempts were re-presentations of an earlier failure (1.76% of the day); 66.5% of them succeeded.

- Retries reached 158 attempts (1.76% of the day, 6.0 sigma above normal). 66.5% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.730% | 1.434% |
| ZM | Invalid UPI PIN | business | Customer | 133 | 1.485% | 1.072% |
| ZA | Transaction declined by customer | business | Customer | 40 | 0.446% | 0.355% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.368% | 0.222% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.346% | 0.257% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.201% | 0.143% |
| ZX | Mandate not found or revoked | business | PSP | 14 | 0.156% | 0.067% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.145% | 0.124% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 26 | 12 |
| Auto-reversals | 28 | 20 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹40,132 | ₹26,845 |

## Customer behaviour

7,736 distinct customers transacted (−13.1% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,370 | 2,659 | 1.12 | 94.36% | ₹1,085 |
| power | 1,688 | 2,158 | 1.28 | 94.25% | ₹1,427 |
| merchant_heavy | 1,703 | 1,943 | 1.14 | 93.77% | ₹945 |
| small_ticket | 1,166 | 1,358 | 1.16 | 94.99% | ₹445 |
| occasional | 648 | 670 | 1.03 | 94.18% | ₹991 |
| new | 144 | 153 | 1.06 | 96.73% | ₹986 |
| dormant_returning | 17 | 18 | 1.06 | 83.33% | ₹1,797 |

## Operational events

- **INC-PSP-0023** (Sev-3) — FamApp app release regression, scoped to FamApp between 19:00 and 23:00. A FamApp client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.

## Risks and opportunities

### Risks

- Success rate closed at 94.31%, 1.26pp down the trailing median — a 7.3-sigma move.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 11 January: success came in 1.26pp below baseline at 94.31% on 8,959 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=8,959, successes=8,449, failed=500, pending=10, settled_value_inr=9,250,945.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: success_rate=94.31; trailing_median=95.57; z=-7.26
- failures: retries=158; retry_share_pct=1.76; recovery_pct=66.46; z=6.03
- headline: attempts=8,959; trailing_median=10,485; z=-9.31
- headline: value_inr=9,250,945; avg_ticket=1,094.92; trailing_avg_ticket=1,217.02
- incidents: event_id=INC-PSP-0023; kind=psp_degradation; severity=Sev-3; window=2026-01-10 to 2026-01-12; success_impact_pp=-3.76; volume_impact_pct=-5.89
- incidents: event_id=MAINT-0086; kind=maintenance_window; severity=Sev-3; window=2026-01-11 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55

Refs: enterprise_data/warehouse/transactions, RPT-D06-DAILY, enterprise_data/warehouse/reference/incidents.parquet
