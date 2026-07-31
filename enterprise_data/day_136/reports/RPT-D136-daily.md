---
id: RPT-D136-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 20 May 2026)

**Report ID:** RPT-D136-DAILY · **Day 136 of 206** · **Derived from:** 14,079 transaction rows queried live from the warehouse

## Summary

The rail took **14,079 payment attempts** on Wednesday 20 May 2026 (Working day) and settled **₹1.88 Cr** across 13,541 successful payments. Volume was −3.6% on yesterday and +1.1% on the same weekday last week. Success closed at **96.18%**, above the trailing 28-day median of 95.91%.

Product UPI International is compounding — attempts up 72% across the trailing window to 206 today, with success holding, so the growth is healthy and worth funding. Product UPI Circle is compounding — attempts up 73% across the trailing window to 535 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,079 | −3.6% | +1.1% | 15,020 |
| Successful payments | 13,541 | −3.6% | +0.8% | 14,406 |
| Success rate | 96.18% | +0.01pp | −0.32pp | 95.91% |
| Settled value | ₹1.88 Cr | −5.9% | +0.9% | ₹2.00 Cr |
| Average ticket | ₹1,389 | −2.3% | +0.1% | ₹1,384 |
| Technical declines | 0.362% | −0.10pp | −0.05pp | 0.521% |
| Business declines | 2.941% | +0.13pp | +0.38pp | 2.913% |
| Risk declines | 0.149% | +0.02pp | −0.02pp | 0.126% |
| Timeout declines | 0.256% | −0.07pp | −0.02pp | 0.423% |
| Retry share | 1.07% | −0.10pp | +0.10pp | 1.39% |
| Latency p95 | 1,283 ms | +0.8% | −0.9% | 1,293 ms |
| Active customers | 11,621 | −3.6% | +0.8% | 12,210 |
| Active merchants | 1,458 | −1.6% | −1.6% | 1,504 |

## What moved

- Product UPI International is compounding — attempts up 72% across the trailing window to 206 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 73% across the trailing window to 535 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,349 | 30.9% | 95.06% | ₹44.04 L | −0.6% |
| UPI Person to Merchant | 3,487 | 24.8% | 96.44% | ₹34.89 L | −10.2% |
| UPI QR Payments | 2,386 | 16.9% | 97.11% | ₹10.79 L | +1.7% |
| UPI Lite | 1,707 | 12.1% | 99.24% | ₹1.50 L | +4.9% |
| UPI Circle | 535 | 3.8% | 97.76% | ₹4.79 L | +9.7% |
| Credit on UPI | 411 | 2.9% | 95.13% | ₹30.43 L | +26.5% |
| RuPay Credit on UPI | 376 | 2.7% | 97.07% | ₹25.55 L | +4.9% |
| UPI AutoPay | 328 | 2.3% | 87.80% | ₹6.12 L | −0.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,403 | 96.34% | 95.96% | ₹61.38 L | normal |
| HDFC Bank | 1,509 | 96.09% | 96.15% | ₹17.21 L | normal |
| Bank of Baroda | 1,102 | 95.74% | 95.79% | ₹15.02 L | normal |
| Union Bank of India | 949 | 96.42% | 95.12% | ₹14.45 L | normal |
| ICICI Bank | 864 | 96.06% | 96.41% | ₹9.39 L | normal |
| Axis Bank | 840 | 96.67% | 96.33% | ₹14.06 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,746 | 96.28% | 95.90% | ₹80.58 L | normal |
| Google Pay | 4,554 | 96.27% | 95.71% | ₹68.56 L | normal |
| Paytm | 1,198 | 95.74% | 95.95% | ₹16.24 L | normal |
| Navi | 511 | 94.52% | 95.51% | ₹8.43 L | normal |
| SuperMoney | 242 | 95.87% | 96.07% | ₹3.06 L | normal |
| BHIM | 146 | 96.58% | 95.64% | ₹1.75 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,134 | 96.90% | ₹45.71 L |
| Food & Beverage | 2,346 | 97.31% | ₹13.96 L |
| Mobility | 1,309 | 98.24% | ₹7.84 L |
| Bills | 771 | 94.68% | ₹9.33 L |
| Healthcare | 494 | 97.98% | ₹4.89 L |
| Digital | 194 | 93.30% | ₹90,274 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,128 | 29.3% | 96.17% | ₹55.61 L |
| West | 3,586 | 25.5% | 96.10% | ₹51.83 L |
| North | 3,444 | 24.5% | 96.54% | ₹47.34 L |
| East | 1,691 | 12.0% | 95.80% | ₹21.54 L |
| Central | 1,230 | 8.7% | 95.93% | ₹11.78 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 441 | 95.92% | ₹1.81 L |
| Hampi Stores 2298 | Key Account | Retail | 98 | 93.88% | ₹1.56 L |
| Vasant Wardrobe | Key Account | Retail | 77 | 97.40% | ₹1.46 L |
| Vega Electronics | Large | Retail | 39 | 100.00% | ₹1.31 L |
| Ujjwal Water Board | Key Account | Bills | 35 | 88.57% | ₹1.00 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 79 | 97.47% | ₹98,260 |
| Aravalli Pharmacy | Large | Healthcare | 90 | 100.00% | ₹88,527 |
| Kaveri Trading | Large | Retail | 50 | 96.00% | ₹71,077 |

## Failure analysis

Of 522 declined attempts, 414 were business declines (2.941% of attempts — balances, PINs and limits), 51 technical (0.362%), 36 timeouts (0.256%) and 21 risk declines (0.149%).

151 attempts were re-presentations of an earlier failure (1.07% of the day); 63.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 162 | 1.151% | 1.207% |
| ZM | Invalid UPI PIN | business | Customer | 144 | 1.023% | 1.040% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.348% | 0.339% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.206% | 0.219% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.199% | 0.212% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.149% | 0.165% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.128% | 0.106% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.114% | 0.082% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 118 | 92 |
| Auto-reversals | 30 | 28 |
| Disputes / chargebacks | 16 | 13 |
| Value returned | ₹3.08 L | ₹1.98 L |

## Customer behaviour

11,621 distinct customers transacted (+0.7% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,602 | 4,159 | 1.15 | 96.15% | ₹1,265 |
| power | 2,491 | 3,349 | 1.34 | 95.67% | ₹1,978 |
| merchant_heavy | 2,596 | 3,149 | 1.21 | 96.38% | ₹1,035 |
| small_ticket | 1,741 | 2,150 | 1.23 | 96.47% | ₹670 |
| occasional | 931 | 993 | 1.07 | 96.27% | ₹1,923 |
| new | 226 | 244 | 1.08 | 98.36% | ₹1,125 |
| dormant_returning | 34 | 35 | 1.03 | 94.29% | ₹1,089 |

## Operational events

- **CMP-0063** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0066** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI International is compounding — attempts up 72% across the trailing window to 206 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 73% across the trailing window to 535 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

20 May ran on trend at 96.18% success and ₹1.88 Cr settled. The movement worth carrying forward is in the product mix: product UPI International is compounding — attempts up 72% across the trailing window to 206 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,079, successes=13,541, failed=522, pending=16, settled_value_inr=18,810,035.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI International; attempts=206; window_growth_pct=72.3; success_rate=94.17
- products: product_name=UPI Circle; attempts=535; window_growth_pct=72.5; success_rate=97.76
- banks: payer_bank=Canara Bank; attempts=795; success_rate=97.36; own_median=95.3; z=2.14
- incidents: event_id=CMP-0063; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-22; success_impact_pp=-0.19; volume_impact_pct=75.81
- incidents: event_id=CMP-0066; kind=merchant_campaign; severity=Sev-3; window=2026-05-17 to 2026-05-21; success_impact_pp=-0.17; volume_impact_pct=66.69

Refs: enterprise_data/warehouse/transactions, RPT-D135-DAILY, enterprise_data/warehouse/reference/incidents.parquet
