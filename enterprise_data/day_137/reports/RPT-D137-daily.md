---
id: RPT-D137-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-21T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 21 May 2026)

**Report ID:** RPT-D137-DAILY · **Day 137 of 206** · **Derived from:** 13,158 transaction rows queried live from the warehouse

## Summary

The rail took **13,158 payment attempts** on Thursday 21 May 2026 (Working day) and settled **₹1.82 Cr** across 12,681 successful payments. Volume was −6.5% on yesterday and −3.7% on the same weekday last week. Success closed at **96.37%**, above the trailing 28-day median of 96.01%.

Product UPI International is compounding — attempts up 78% across the trailing window to 165 today, with success holding, so the growth is healthy and worth funding. Product UPI Circle is compounding — attempts up 61% across the trailing window to 577 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,158 | −6.5% | −3.7% | 14,931 |
| Successful payments | 12,681 | −6.4% | −3.6% | 14,324 |
| Success rate | 96.37% | +0.20pp | +0.14pp | 95.93% |
| Settled value | ₹1.82 Cr | −3.1% | −12.4% | ₹1.99 Cr |
| Average ticket | ₹1,437 | +3.4% | −9.1% | ₹1,387 |
| Technical declines | 0.327% | −0.04pp | −0.15pp | 0.512% |
| Business declines | 2.835% | −0.11pp | +0.05pp | 2.909% |
| Risk declines | 0.114% | −0.04pp | −0.01pp | 0.126% |
| Timeout declines | 0.281% | +0.03pp | +0.00pp | 0.416% |
| Retry share | 1.28% | +0.20pp | +0.26pp | 1.39% |
| Latency p95 | 1,257 ms | −2.0% | +0.3% | 1,291 ms |
| Active customers | 11,004 | −5.3% | −3.2% | 12,153 |
| Active merchants | 1,459 | +0.1% | −2.1% | 1,502 |

## What moved

- Product UPI International is compounding — attempts up 78% across the trailing window to 165 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 61% across the trailing window to 577 today, with success holding, so the growth is healthy and worth funding.
- Issuer HDFC Bank ran at 97.16% success on 1,445 attempts (11.0% of the day), 1.01pp up its own 28-day median.
- Region Central ran at 97.11% success on 1,109 attempts (8.4% of the day), 1.14pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,974 | 30.2% | 95.77% | ₹43.06 L | −9.2% |
| UPI Person to Merchant | 3,355 | 25.5% | 96.60% | ₹31.90 L | −13.6% |
| UPI QR Payments | 2,085 | 15.8% | 96.83% | ₹9.39 L | −11.3% |
| UPI Lite | 1,597 | 12.1% | 99.06% | ₹1.42 L | −4.5% |
| UPI Circle | 577 | 4.4% | 97.23% | ₹4.83 L | +15.5% |
| RuPay Credit on UPI | 411 | 3.1% | 94.89% | ₹20.12 L | +13.5% |
| Credit on UPI | 403 | 3.1% | 94.79% | ₹28.72 L | +19.1% |
| UPI AutoPay | 327 | 2.5% | 90.21% | ₹6.69 L | −0.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,112 | 96.25% | 96.00% | ₹56.25 L | normal |
| HDFC Bank | 1,445 | 97.16% | 96.15% | ₹26.16 L | ⚠ outlier |
| Bank of Baroda | 977 | 96.21% | 95.72% | ₹11.49 L | normal |
| Union Bank of India | 910 | 95.82% | 95.19% | ₹9.60 L | normal |
| Punjab National Bank | 822 | 97.08% | 95.52% | ₹12.08 L | normal |
| Axis Bank | 786 | 96.31% | 96.33% | ₹12.31 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,219 | 96.14% | 95.93% | ₹82.69 L | normal |
| Google Pay | 4,293 | 96.41% | 95.78% | ₹57.27 L | normal |
| Paytm | 1,085 | 96.31% | 95.95% | ₹15.09 L | normal |
| Navi | 521 | 96.35% | 95.51% | ₹9.49 L | normal |
| SuperMoney | 228 | 97.81% | 95.83% | ₹2.51 L | normal |
| BHIM | 143 | 97.90% | 95.84% | ₹1.05 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,661 | 96.37% | ₹46.73 L |
| Food & Beverage | 2,322 | 97.37% | ₹12.48 L |
| Mobility | 1,203 | 98.09% | ₹6.16 L |
| Bills | 815 | 96.44% | ₹7.91 L |
| Healthcare | 484 | 98.55% | ₹5.25 L |
| Digital | 210 | 91.43% | ₹1.06 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,933 | 29.9% | 96.64% | ₹60.38 L |
| North | 3,306 | 25.1% | 96.10% | ₹41.38 L |
| West | 3,240 | 24.6% | 96.14% | ₹46.98 L |
| East | 1,570 | 11.9% | 96.24% | ₹23.06 L |
| Central | 1,109 | 8.4% | 97.11% | ₹10.42 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 39 | 97.44% | ₹3.16 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 98.65% | ₹1.92 L |
| Ujjwal Water Board | Key Account | Bills | 36 | 91.67% | ₹1.71 L |
| Rapid Bazaar | Key Account | Retail | 362 | 97.24% | ₹1.70 L |
| Hampi Stores 2298 | Key Account | Retail | 117 | 95.73% | ₹1.12 L |
| Hampi Styles | Key Account | Retail | 32 | 93.75% | ₹80,703 |
| Swift Grill | Large | Food & Beverage | 46 | 97.83% | ₹78,733 |
| Yamuna Restaurant | Key Account | Food & Beverage | 76 | 94.74% | ₹76,816 |

## Failure analysis

Of 468 declined attempts, 373 were business declines (2.835% of attempts — balances, PINs and limits), 43 technical (0.327%), 37 timeouts (0.281%) and 15 risk declines (0.114%).

168 attempts were re-presentations of an earlier failure (1.28% of the day); 66.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 160 | 1.216% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 109 | 0.828% | 1.032% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.365% | 0.339% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.236% | 0.218% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.160% | 0.159% |
| U30 | Debit failed at remitter bank | technical | Issuer | 15 | 0.114% | 0.209% |
| UX | Mandate execution outside permitted window | business | PSP | 13 | 0.099% | 0.082% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 13 | 0.099% | 0.106% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 94 | 94 |
| Auto-reversals | 21 | 28 |
| Disputes / chargebacks | 16 | 14 |
| Value returned | ₹1.08 L | ₹1.98 L |

## Customer behaviour

11,004 distinct customers transacted (−5.0% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,426 | 3,889 | 1.14 | 96.48% | ₹1,486 |
| merchant_heavy | 2,590 | 3,122 | 1.21 | 96.76% | ₹1,123 |
| power | 2,320 | 3,066 | 1.32 | 96.02% | ₹2,036 |
| small_ticket | 1,617 | 1,976 | 1.22 | 96.51% | ₹611 |
| occasional | 849 | 881 | 1.04 | 95.91% | ₹1,463 |
| new | 174 | 196 | 1.13 | 94.90% | ₹842 |
| dormant_returning | 28 | 28 | 1.00 | 92.86% | ₹1,158 |

## Operational events

- **INC-PSP-0024** (Sev-3) — PhonePe app release regression, scoped to PhonePe between 19:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CMP-0063** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0066** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI International is compounding — attempts up 78% across the trailing window to 165 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 61% across the trailing window to 577 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

21 May ran on trend at 96.37% success and ₹1.82 Cr settled. The movement worth carrying forward is in the product mix: product UPI International is compounding — attempts up 78% across the trailing window to 165 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-21` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,158, successes=12,681, failed=468, pending=9, settled_value_inr=18,221,570.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI International; attempts=165; window_growth_pct=77.7; success_rate=95.15
- products: product_name=UPI Circle; attempts=577; window_growth_pct=61.5; success_rate=97.23
- banks: payer_bank=HDFC Bank; attempts=1,445; success_rate=97.16; own_median=96.15; z=2.49
- geography: region=Central; attempts=1,109; success_rate=97.11; own_median=95.98; z=2.62
- incidents: event_id=INC-PSP-0024; kind=psp_degradation; severity=Sev-3; window=2026-05-21 to 2026-05-24; success_impact_pp=-4.06; volume_impact_pct=-6.35
- incidents: event_id=CMP-0063; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-22; success_impact_pp=-0.19; volume_impact_pct=75.81
- incidents: event_id=CMP-0066; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-21; success_impact_pp=-0.17; volume_impact_pct=66.69

Refs: enterprise_data/warehouse/transactions, RPT-D136-DAILY, enterprise_data/warehouse/reference/incidents.parquet
