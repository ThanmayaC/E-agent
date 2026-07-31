---
id: RPT-D186-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-09T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 09 Jul 2026)

**Report ID:** RPT-D186-DAILY · **Day 186 of 206** · **Derived from:** 15,209 transaction rows queried live from the warehouse

## Summary

The rail took **15,209 payment attempts** on Thursday 09 July 2026 (Working day) and settled **₹1.88 Cr** across 14,673 successful payments. Volume was −8.5% on yesterday and −16.2% on the same weekday last week. Success closed at **96.48%**, above the trailing 28-day median of 96.16%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,209 | −8.5% | −16.2% | 17,238 |
| Successful payments | 14,673 | −8.8% | −16.5% | 16,561 |
| Success rate | 96.48% | −0.32pp | −0.30pp | 96.13% |
| Settled value | ₹1.88 Cr | −12.5% | −21.8% | ₹2.21 Cr |
| Average ticket | ₹1,283 | −4.0% | −6.4% | ₹1,332 |
| Technical declines | 0.388% | −0.02pp | +0.07pp | 0.496% |
| Business declines | 2.676% | +0.22pp | +0.23pp | 2.620% |
| Risk declines | 0.092% | −0.02pp | −0.01pp | 0.109% |
| Timeout declines | 0.270% | +0.08pp | −0.01pp | 0.568% |
| Retry share | 0.99% | +0.08pp | +0.02pp | 1.47% |
| Latency p95 | 1,271 ms | +1.6% | +5.0% | 1,321 ms |
| Active customers | 12,556 | −6.5% | −13.4% | 13,848 |
| Active merchants | 1,580 | −3.1% | −5.8% | 1,644 |

## What moved

- Product UPI Lite is compounding — attempts up 44% across the trailing window to 2,130 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 789 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,403 | 28.9% | 95.93% | ₹47.55 L | +1.2% |
| UPI Person to Merchant | 3,817 | 25.1% | 96.23% | ₹32.63 L | +8.2% |
| UPI QR Payments | 2,463 | 16.2% | 96.39% | ₹10.35 L | −2.2% |
| UPI Lite | 2,130 | 14.0% | 99.34% | ₹2.04 L | −13.8% |
| UPI Circle | 789 | 5.2% | 97.72% | ₹6.43 L | −1.1% |
| Credit on UPI | 464 | 3.1% | 96.34% | ₹39.94 L | −1.4% |
| UPI AutoPay | 358 | 2.4% | 88.83% | ₹6.06 L | −5.2% |
| RuPay Credit on UPI | 319 | 2.1% | 97.18% | ₹15.70 L | −14.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,828 | 96.19% | 96.16% | ₹61.69 L | normal |
| HDFC Bank | 1,618 | 95.86% | 96.39% | ₹20.76 L | normal |
| Bank of Baroda | 1,146 | 96.86% | 96.22% | ₹11.43 L | normal |
| Union Bank of India | 1,043 | 96.64% | 96.10% | ₹16.17 L | normal |
| Punjab National Bank | 1,011 | 96.54% | 95.93% | ₹10.79 L | normal |
| Axis Bank | 909 | 96.37% | 96.13% | ₹14.17 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,174 | 96.36% | 96.20% | ₹90.39 L | normal |
| Google Pay | 5,056 | 96.86% | 96.21% | ₹58.04 L | normal |
| Paytm | 1,230 | 96.91% | 96.03% | ₹17.50 L | normal |
| Navi | 550 | 96.36% | 96.55% | ₹6.06 L | normal |
| SuperMoney | 292 | 96.92% | 95.51% | ₹2.04 L | normal |
| BHIM | 157 | 94.27% | 95.85% | ₹1.14 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,479 | 97.10% | ₹51.26 L |
| Food & Beverage | 2,755 | 97.06% | ₹13.64 L |
| Mobility | 1,379 | 97.10% | ₹8.06 L |
| Bills | 921 | 95.66% | ₹7.77 L |
| Healthcare | 583 | 97.60% | ₹7.83 L |
| Digital | 231 | 93.94% | ₹85,690 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,440 | 29.2% | 95.83% | ₹55.14 L |
| North | 3,927 | 25.8% | 96.94% | ₹53.63 L |
| West | 3,768 | 24.8% | 96.52% | ₹43.78 L |
| East | 1,815 | 11.9% | 96.86% | ₹23.80 L |
| Central | 1,259 | 8.3% | 96.58% | ₹11.99 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 100.00% | ₹2.13 L |
| Vasant Wardrobe | Key Account | Retail | 85 | 98.82% | ₹2.08 L |
| Rapid Bazaar | Key Account | Retail | 360 | 97.22% | ₹1.39 L |
| Girnar Connect | Key Account | Bills | 179 | 96.65% | ₹1.03 L |
| Zenith Diner | Large | Food & Beverage | 23 | 91.30% | ₹78,323 |
| Hampi Stores 2298 | Key Account | Retail | 123 | 96.75% | ₹77,061 |
| Hampi Styles | Key Account | Retail | 41 | 100.00% | ₹74,844 |
| Urban Boutique | Key Account | Retail | 120 | 97.50% | ₹69,536 |

## Failure analysis

Of 521 declined attempts, 407 were business declines (2.676% of attempts — balances, PINs and limits), 59 technical (0.388%), 41 timeouts (0.270%) and 14 risk declines (0.092%).

150 attempts were re-presentations of an earlier failure (0.99% of the day); 62.0% of them succeeded.

- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 12 times — 0.079% of attempts against a trailing 0.038%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 187 | 1.230% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 121 | 0.796% | 0.970% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.237% | 0.328% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.184% | 0.194% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.138% | 0.176% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.118% | 0.132% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.112% | 0.074% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.112% | 0.122% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 128 | 108 |
| Auto-reversals | 23 | 24 |
| Disputes / chargebacks | 16 | 14 |
| Value returned | ₹1.44 L | ₹1.71 L |

## Customer behaviour

12,556 distinct customers transacted (+2.0% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,941 | 4,523 | 1.15 | 96.46% | ₹1,202 |
| power | 2,732 | 3,720 | 1.36 | 96.69% | ₹1,686 |
| merchant_heavy | 2,813 | 3,419 | 1.22 | 95.93% | ₹979 |
| small_ticket | 1,894 | 2,302 | 1.22 | 96.92% | ₹517 |
| occasional | 955 | 1,001 | 1.05 | 96.80% | ₹2,366 |
| new | 196 | 217 | 1.11 | 95.39% | ₹749 |
| dormant_returning | 25 | 27 | 1.08 | 96.30% | ₹2,057 |

## Operational events

- **INC-BANK-0022** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 11:00 and 14:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 12 times — 0.079% of attempts against a trailing 0.038%. Owner: NPCI.

### Opportunities

- Product UPI Lite is compounding — attempts up 44% across the trailing window to 2,130 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 789 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

09 July ran on trend at 96.48% success and ₹1.88 Cr settled. The movement worth carrying forward is in the product mix: product UPI Lite is compounding — attempts up 44% across the trailing window to 2,130 today, with success holding, so the growth is healthy and worth funding. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-09` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,209, successes=14,673, failed=521, pending=15, settled_value_inr=18,832,595.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Lite; attempts=2,130; window_growth_pct=44.3; success_rate=99.34
- products: product_name=UPI Circle; attempts=789; window_growth_pct=34; success_rate=97.72
- incidents: event_id=INC-BANK-0022; kind=bank_outage; severity=Sev-3; window=2026-07-08 to 2026-07-09; success_impact_pp=-5.53; volume_impact_pct=-4.91
- failures: failure_code=U67; count=12; rate_pct=0.08; trailing_rate_pct=0.04; owner=NPCI; z=2.01
- banks: payer_bank=Indian Bank; attempts=455; success_rate=97.8; own_median=96.15; z=2.08

Refs: enterprise_data/warehouse/transactions, RPT-D185-DAILY, enterprise_data/warehouse/reference/incidents.parquet
