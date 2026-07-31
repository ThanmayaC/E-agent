---
id: RPT-D128-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 12 May 2026)

**Report ID:** RPT-D128-DAILY · **Day 128 of 206** · **Derived from:** 13,778 transaction rows queried live from the warehouse

## Summary

The rail took **13,778 payment attempts** on Tuesday 12 May 2026 (Working day) and settled **₹1.89 Cr** across 13,240 successful payments. Volume was +0.8% on yesterday and −8.6% on the same weekday last week. Success closed at **96.10%**, above the trailing 28-day median of 95.72%.

Product UPI Circle is compounding — attempts up 62% across the trailing window to 598 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,778 | +0.8% | −8.6% | 15,192 |
| Successful payments | 13,240 | +0.5% | −8.4% | 14,591 |
| Success rate | 96.10% | −0.23pp | +0.27pp | 96.04% |
| Settled value | ₹1.89 Cr | −1.7% | −12.3% | ₹2.00 Cr |
| Average ticket | ₹1,429 | −2.2% | −4.3% | ₹1,372 |
| Technical declines | 0.377% | −0.04pp | −0.22pp | 0.486% |
| Business declines | 2.961% | +0.20pp | −0.08pp | 2.915% |
| Risk declines | 0.116% | +0.01pp | −0.01pp | 0.122% |
| Timeout declines | 0.377% | +0.09pp | +0.03pp | 0.329% |
| Retry share | 1.05% | −0.12pp | −0.12pp | 1.28% |
| Latency p95 | 1,252 ms | +0.0% | −1.3% | 1,243 ms |
| Active customers | 11,394 | +0.5% | −7.0% | 12,313 |
| Active merchants | 1,539 | +3.7% | +3.6% | 1,501 |

## What moved

- Product UPI Circle is compounding — attempts up 62% across the trailing window to 598 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 47% across the trailing window to 1,562 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 4,201 | 30.5% | 96.10% | ₹47.16 L | +9.9% |
| UPI Person to Person | 3,790 | 27.5% | 95.28% | ₹38.60 L | −13.5% |
| UPI QR Payments | 2,134 | 15.5% | 96.20% | ₹9.97 L | −9.0% |
| UPI Lite | 1,562 | 11.3% | 98.98% | ₹1.41 L | +13.1% |
| UPI Circle | 598 | 4.3% | 98.49% | ₹5.00 L | +40.4% |
| Credit on UPI | 372 | 2.7% | 95.97% | ₹33.49 L | +38.3% |
| RuPay Credit on UPI | 351 | 2.5% | 94.30% | ₹22.04 L | +0.3% |
| UPI AutoPay | 345 | 2.5% | 92.17% | ₹5.95 L | +5.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,422 | 96.16% | 95.88% | ₹59.98 L | normal |
| HDFC Bank | 1,518 | 96.44% | 95.96% | ₹17.36 L | normal |
| Bank of Baroda | 1,026 | 96.39% | 95.77% | ₹13.15 L | normal |
| Union Bank of India | 919 | 95.10% | 94.90% | ₹14.12 L | normal |
| Axis Bank | 870 | 96.67% | 95.95% | ₹10.73 L | normal |
| ICICI Bank | 832 | 95.91% | 96.41% | ₹8.20 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,487 | 95.95% | 95.83% | ₹86.58 L | normal |
| Google Pay | 4,533 | 95.98% | 95.56% | ₹63.40 L | normal |
| Paytm | 1,158 | 96.89% | 95.86% | ₹20.39 L | normal |
| Navi | 484 | 96.90% | 95.35% | ₹6.73 L | normal |
| SuperMoney | 267 | 97.38% | 95.68% | ₹3.03 L | normal |
| BHIM | 135 | 95.56% | 95.24% | ₹98,784 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,139 | 96.18% | ₹50.12 L |
| Food & Beverage | 2,503 | 97.08% | ₹13.60 L |
| Mobility | 1,170 | 97.86% | ₹6.73 L |
| Bills | 924 | 95.45% | ₹12.17 L |
| Healthcare | 533 | 96.44% | ₹6.36 L |
| Digital | 241 | 95.85% | ₹1.30 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,015 | 29.1% | 96.24% | ₹59.74 L |
| North | 3,442 | 25.0% | 96.05% | ₹47.09 L |
| West | 3,423 | 24.8% | 96.47% | ₹49.51 L |
| East | 1,676 | 12.2% | 95.23% | ₹21.20 L |
| Central | 1,222 | 8.9% | 95.91% | ₹11.62 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 47 | 93.62% | ₹2.18 L |
| Vasant Wardrobe | Key Account | Retail | 82 | 91.46% | ₹1.55 L |
| Rapid Bazaar | Key Account | Retail | 410 | 95.12% | ₹1.23 L |
| Urban Boutique | Key Account | Retail | 109 | 98.17% | ₹1.18 L |
| Hampi Stores 2298 | Key Account | Retail | 112 | 93.75% | ₹1.06 L |
| Girnar Connect | Key Account | Bills | 143 | 93.01% | ₹96,683 |
| Swift Grill | Large | Food & Beverage | 42 | 97.62% | ₹71,845 |
| Trinetra Restaurant | Large | Food & Beverage | 36 | 94.44% | ₹70,891 |

## Failure analysis

Of 528 declined attempts, 408 were business declines (2.961% of attempts — balances, PINs and limits), 52 technical (0.377%), 52 timeouts (0.377%) and 16 risk declines (0.116%).

144 attempts were re-presentations of an earlier failure (1.05% of the day); 69.4% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 170 | 1.234% | 1.246% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 0.980% | 1.050% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.341% | 0.373% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.240% | 0.219% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 27 | 0.196% | 0.173% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.174% | 0.216% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.123% | 0.116% |
| UX | Mandate execution outside permitted window | business | PSP | 12 | 0.087% | 0.083% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 106 | 90 |
| Auto-reversals | 18 | 28 |
| Disputes / chargebacks | 13 | 11 |
| Value returned | ₹1.11 L | ₹1.51 L |

## Customer behaviour

11,394 distinct customers transacted (+0.7% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,529 | 4,016 | 1.14 | 96.24% | ₹1,459 |
| power | 2,409 | 3,266 | 1.36 | 95.96% | ₹2,025 |
| merchant_heavy | 2,587 | 3,136 | 1.21 | 95.82% | ₹1,041 |
| small_ticket | 1,739 | 2,149 | 1.24 | 96.74% | ₹568 |
| occasional | 886 | 946 | 1.07 | 95.24% | ₹1,747 |
| new | 222 | 243 | 1.09 | 97.12% | ₹1,230 |
| dormant_returning | 22 | 22 | 1.00 | 90.91% | ₹422 |

## Operational events

- **INC-BANK-0001** (Sev-3) — Yes Bank issuer decline spike, scoped to Yes Bank between 23:00 and 05:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0061** (Sev-3) — Wealth & SIP cashback campaign, scoped to 6211. A cashback campaign across Wealth & SIP merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 62% across the trailing window to 598 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 47% across the trailing window to 1,562 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

12 May ran on trend at 96.10% success and ₹1.89 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 62% across the trailing window to 598 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,778, successes=13,240, failed=528, pending=10, settled_value_inr=18,916,215.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=598; window_growth_pct=61.8; success_rate=98.49
- products: product_name=UPI Lite; attempts=1,562; window_growth_pct=47; success_rate=98.98
- incidents: event_id=INC-BANK-0001; kind=bank_outage; severity=Sev-3; window=2026-05-08 to 2026-05-12; success_impact_pp=-6.2; volume_impact_pct=-5.5
- products: product_name=UPI Circle; attempts=598; success_rate=98.49; own_median=96.56; z=2.04
- incidents: event_id=CMP-0061; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-17; success_impact_pp=-0.14; volume_impact_pct=57.92
- incidents: event_id=CMP-0067; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-19; success_impact_pp=-0.12; volume_impact_pct=49.99
- categories: mcc_category=Services; attempts=137; own_median=104; z=2.47

Refs: enterprise_data/warehouse/transactions, RPT-D127-DAILY, enterprise_data/warehouse/reference/incidents.parquet
