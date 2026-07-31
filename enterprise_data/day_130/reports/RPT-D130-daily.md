---
id: RPT-D130-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 14 May 2026)

**Report ID:** RPT-D130-DAILY · **Day 130 of 206** · **Derived from:** 13,667 transaction rows queried live from the warehouse

## Summary

The rail took **13,667 payment attempts** on Thursday 14 May 2026 (Working day) and settled **₹2.08 Cr** across 13,152 successful payments. Volume was −1.8% on yesterday and −11.7% on the same weekday last week. Success closed at **96.23%**, above the trailing 28-day median of 95.84%.

Product UPI Circle is compounding — attempts up 62% across the trailing window to 504 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,667 | −1.8% | −11.7% | 14,993 |
| Successful payments | 13,152 | −2.1% | −11.5% | 14,405 |
| Success rate | 96.23% | −0.26pp | +0.20pp | 96.09% |
| Settled value | ₹2.08 Cr | +11.6% | −10.8% | ₹2.00 Cr |
| Average ticket | ₹1,581 | +14.0% | +0.8% | ₹1,388 |
| Technical declines | 0.476% | +0.07pp | −0.09pp | 0.480% |
| Business declines | 2.780% | +0.22pp | +0.02pp | 2.880% |
| Risk declines | 0.124% | −0.05pp | −0.04pp | 0.126% |
| Timeout declines | 0.278% | −0.00pp | −0.06pp | 0.322% |
| Retry share | 1.02% | +0.04pp | −0.17pp | 1.24% |
| Latency p95 | 1,253 ms | −3.2% | −1.0% | 1,247 ms |
| Active customers | 11,362 | −1.4% | −9.0% | 12,189 |
| Active merchants | 1,490 | +0.5% | −0.9% | 1,499 |

## What moved

- Product UPI Circle is compounding — attempts up 62% across the trailing window to 504 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 45% across the trailing window to 1,659 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,844 | 28.1% | 95.68% | ₹44.31 L | −12.3% |
| UPI Person to Merchant | 3,806 | 27.8% | 95.80% | ₹36.75 L | −1.3% |
| UPI QR Payments | 2,285 | 16.7% | 96.81% | ₹10.59 L | −2.6% |
| UPI Lite | 1,659 | 12.1% | 98.92% | ₹1.48 L | +9.4% |
| UPI Circle | 504 | 3.7% | 96.63% | ₹3.72 L | +7.6% |
| RuPay Credit on UPI | 406 | 3.0% | 96.31% | ₹33.31 L | +15.2% |
| Credit on UPI | 352 | 2.6% | 96.88% | ₹31.27 L | +19.3% |
| UPI AutoPay | 329 | 2.4% | 90.58% | ₹6.56 L | +0.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,365 | 96.43% | 95.95% | ₹79.55 L | normal |
| HDFC Bank | 1,462 | 96.17% | 95.96% | ₹21.10 L | normal |
| Bank of Baroda | 1,020 | 95.88% | 95.88% | ₹10.85 L | normal |
| Union Bank of India | 958 | 95.41% | 94.95% | ₹17.60 L | normal |
| Axis Bank | 860 | 97.44% | 96.14% | ₹12.63 L | normal |
| Punjab National Bank | 848 | 95.05% | 95.57% | ₹9.52 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,514 | 96.21% | 95.90% | ₹88.82 L | normal |
| Google Pay | 4,461 | 96.50% | 95.65% | ₹72.16 L | normal |
| Paytm | 1,090 | 95.96% | 95.90% | ₹20.85 L | normal |
| Navi | 498 | 95.18% | 95.83% | ₹7.96 L | normal |
| SuperMoney | 277 | 94.22% | 96.07% | ₹4.73 L | normal |
| FamApp | 129 | 95.35% | 95.77% | ₹1.92 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,056 | 96.45% | ₹55.06 L |
| Food & Beverage | 2,416 | 97.06% | ₹10.98 L |
| Mobility | 1,252 | 97.36% | ₹6.91 L |
| Bills | 869 | 95.63% | ₹10.33 L |
| Healthcare | 511 | 98.43% | ₹8.09 L |
| Digital | 221 | 91.86% | ₹1.12 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,954 | 28.9% | 96.23% | ₹57.83 L |
| West | 3,455 | 25.3% | 95.69% | ₹54.82 L |
| North | 3,400 | 24.9% | 96.62% | ₹51.54 L |
| East | 1,638 | 12.0% | 96.15% | ₹28.95 L |
| Central | 1,220 | 8.9% | 96.80% | ₹14.77 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹2.27 L |
| Rapid Bazaar | Key Account | Retail | 394 | 97.97% | ₹1.85 L |
| Vasant Wardrobe | Key Account | Retail | 72 | 97.22% | ₹1.82 L |
| Hampi Styles | Key Account | Retail | 36 | 94.44% | ₹1.17 L |
| Hampi Stores 2298 | Key Account | Retail | 111 | 94.59% | ₹1.01 L |
| Ujjwal Water Board | Key Account | Bills | 39 | 100.00% | ₹96,822 |
| Aravalli Pharmacy | Large | Healthcare | 88 | 100.00% | ₹73,697 |
| Tejas Restaurant | Large | Food & Beverage | 26 | 100.00% | ₹72,558 |

## Failure analysis

Of 500 declined attempts, 380 were business declines (2.780% of attempts — balances, PINs and limits), 65 technical (0.476%), 38 timeouts (0.278%) and 17 risk declines (0.124%).

139 attempts were re-presentations of an earlier failure (1.02% of the day); 66.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 156 | 1.141% | 1.224% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 0.922% | 1.032% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.366% | 0.355% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.161% | 0.212% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.154% | 0.219% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.146% | 0.169% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.146% | 0.136% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.110% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 117 | 90 |
| Auto-reversals | 27 | 28 |
| Disputes / chargebacks | 16 | 12 |
| Value returned | ₹4.05 L | ₹1.43 L |

## Customer behaviour

11,362 distinct customers transacted (−0.5% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,475 | 3,985 | 1.15 | 96.16% | ₹1,708 |
| power | 2,475 | 3,286 | 1.33 | 96.50% | ₹2,061 |
| merchant_heavy | 2,599 | 3,127 | 1.20 | 96.00% | ₹1,076 |
| small_ticket | 1,721 | 2,099 | 1.22 | 96.33% | ₹566 |
| occasional | 874 | 930 | 1.06 | 96.13% | ₹2,548 |
| new | 189 | 211 | 1.12 | 96.21% | ₹1,275 |
| dormant_returning | 29 | 29 | 1.00 | 96.55% | ₹763 |

## Operational events

- **CMP-0061** (Sev-3) — Wealth & SIP cashback campaign, scoped to 6211. A cashback campaign across Wealth & SIP merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **REG-0069** (Sev-3) — UPI International — two new acceptance corridors live, scoped to UPI_INTL. Two new cross-border acceptance corridors went live. Volume steps up; early-corridor settlement immaturity temporarily depresses the success rate.

## Risks and opportunities

### Risks

- 117 refunds were raised, 2.3 sigma above the trailing median of 90.

### Opportunities

- Product UPI Circle is compounding — attempts up 62% across the trailing window to 504 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 45% across the trailing window to 1,659 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

14 May ran on trend at 96.23% success and ₹2.08 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 62% across the trailing window to 504 today, with success holding, so the growth is healthy and worth funding. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,667, successes=13,152, failed=500, pending=15, settled_value_inr=20,790,727.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=504; window_growth_pct=61.6; success_rate=96.63
- adjustments: refunds=117; trailing_median=89.5; z=2.32
- products: product_name=UPI Lite; attempts=1,659; window_growth_pct=44.7; success_rate=98.92
- incidents: event_id=CMP-0061; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-17; success_impact_pp=-0.14; volume_impact_pct=57.92
- incidents: event_id=CMP-0067; kind=merchant_campaign; severity=Sev-3; window=2026-05-12 to 2026-05-19; success_impact_pp=-0.12; volume_impact_pct=49.99
- incidents: event_id=REG-0069; kind=corridor_launch; severity=Sev-3; window=2026-05-14 to 2026-07-29; success_impact_pp=-0.55; volume_impact_pct=54
- products: product_name=UPI International; attempts=206; own_median=137; z=3.1

Refs: enterprise_data/warehouse/transactions, RPT-D129-DAILY, enterprise_data/warehouse/reference/incidents.parquet
