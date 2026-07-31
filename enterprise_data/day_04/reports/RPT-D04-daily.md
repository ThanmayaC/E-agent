---
id: RPT-D04-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 08 Jan 2026)

**Report ID:** RPT-D04-DAILY · **Day 4 of 206** · **Derived from:** 10,241 transaction rows queried live from the warehouse

## Summary

The rail took **10,241 payment attempts** on Thursday 08 January 2026 (Working day) and settled **₹1.20 Cr** across 9,777 successful payments. Volume was −2.2% on yesterday and — on the same weekday last week. Success closed at **95.47%**, in line with the trailing 28-day median of 95.69%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,241 | −2.2% | — | 10,456 |
| Successful payments | 9,777 | −2.4% | — | 9,996 |
| Success rate | 95.47% | −0.22pp | — | 95.60% |
| Settled value | ₹1.20 Cr | −3.8% | — | ₹1.26 Cr |
| Average ticket | ₹1,232 | −1.4% | — | ₹1,265 |
| Technical declines | 0.508% | −0.02pp | — | 0.512% |
| Business declines | 3.242% | +0.01pp | — | 3.200% |
| Risk declines | 0.176% | +0.09pp | — | 0.158% |
| Timeout declines | 0.430% | +0.06pp | — | 0.369% |
| Retry share | 1.31% | +0.11pp | — | 1.13% |
| Latency p95 | 1,242 ms | −2.1% | — | 1,259 ms |
| Active customers | 8,730 | −1.6% | — | 8,883 |
| Active merchants | 1,210 | −0.2% | — | 1,217 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,027 | 39.3% | 95.06% | ₹42.88 L | +1.0% |
| UPI Person to Merchant | 2,888 | 28.2% | 95.53% | ₹28.84 L | −6.4% |
| UPI QR Payments | 1,581 | 15.4% | 96.84% | ₹7.14 L | −11.2% |
| UPI Lite | 715 | 7.0% | 97.62% | ₹67,142 | +2.7% |
| UPI AutoPay | 284 | 2.8% | 91.90% | ₹4.39 L | −7.2% |
| RuPay Credit on UPI | 216 | 2.1% | 95.37% | ₹12.71 L | +10.8% |
| Credit on UPI | 143 | 1.4% | 94.41% | ₹8.92 L | −14.9% |
| UPI Circle | 96 | 0.9% | 95.83% | ₹78,929 | −4.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,200 | 95.38% | 95.50% | ₹36.38 L | normal |
| HDFC Bank | 1,135 | 97.00% | 96.17% | ₹15.30 L | normal |
| Bank of Baroda | 759 | 94.07% | 95.74% | ₹10.40 L | normal |
| Union Bank of India | 703 | 95.02% | 95.16% | ₹8.19 L | normal |
| Axis Bank | 677 | 96.01% | 95.39% | ₹6.70 L | normal |
| ICICI Bank | 618 | 96.28% | 95.17% | ₹8.56 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,868 | 95.71% | 95.55% | ₹56.72 L | normal |
| Google Pay | 3,294 | 95.20% | 95.60% | ₹41.13 L | normal |
| Paytm | 852 | 96.71% | 95.92% | ₹10.08 L | normal |
| Navi | 376 | 94.41% | 96.00% | ₹3.63 L | normal |
| SuperMoney | 196 | 94.90% | 95.75% | ₹2.32 L | normal |
| BHIM | 107 | 95.33% | 96.64% | ₹79,793 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,628 | 95.43% | ₹32.41 L |
| Food & Beverage | 1,488 | 96.44% | ₹6.53 L |
| Mobility | 665 | 98.05% | ₹3.83 L |
| Bills | 622 | 95.82% | ₹7.27 L |
| Healthcare | 335 | 95.52% | ₹1.96 L |
| Digital | 184 | 94.02% | ₹76,893 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,068 | 30.0% | 96.19% | ₹36.67 L |
| North | 2,539 | 24.8% | 95.31% | ₹32.65 L |
| West | 2,519 | 24.6% | 94.84% | ₹27.86 L |
| East | 1,230 | 12.0% | 95.61% | ₹16.18 L |
| Central | 885 | 8.6% | 95.03% | ₹7.12 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 268 | 94.78% | ₹1.13 L |
| Vega Electronics | Large | Retail | 21 | 85.71% | ₹1.10 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 93.44% | ₹91,459 |
| Yamuna Restaurant | Key Account | Food & Beverage | 67 | 97.01% | ₹59,973 |
| Urban Boutique | Key Account | Retail | 82 | 97.56% | ₹53,784 |
| Kaveri Trading | Large | Retail | 46 | 95.65% | ₹53,000 |
| Girnar Connect | Key Account | Bills | 113 | 96.46% | ₹48,444 |
| Ujjwal Water Board | Key Account | Bills | 31 | 90.32% | ₹43,156 |

## Failure analysis

Of 446 declined attempts, 332 were business declines (3.242% of attempts — balances, PINs and limits), 52 technical (0.508%), 44 timeouts (0.430%) and 18 risk declines (0.176%).

134 attempts were re-presentations of an earlier failure (1.31% of the day); 70.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 138 | 1.348% | 1.461% |
| ZM | Invalid UPI PIN | business | Customer | 113 | 1.103% | 0.955% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.361% | 0.349% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 29 | 0.283% | 0.181% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.254% | 0.229% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.234% | 0.210% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.146% | 0.170% |
| U28 | Remitter bank unavailable | technical | Issuer | 12 | 0.117% | 0.134% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 17 | 2 |
| Auto-reversals | 35 | 9 |
| Disputes / chargebacks | 0 | 0 |
| Value returned | ₹85,277 | ₹5,345 |

## Customer behaviour

8,730 distinct customers transacted (−2.2% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,684 | 2,998 | 1.12 | 95.76% | ₹1,309 |
| power | 1,837 | 2,385 | 1.30 | 95.30% | ₹1,477 |
| merchant_heavy | 1,987 | 2,328 | 1.17 | 95.75% | ₹868 |
| small_ticket | 1,339 | 1,601 | 1.20 | 95.19% | ₹535 |
| occasional | 666 | 700 | 1.05 | 94.29% | ₹1,821 |
| new | 194 | 206 | 1.06 | 96.60% | ₹2,074 |
| dormant_returning | 23 | 23 | 1.00 | 91.30% | ₹1,103 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

08 January was an unremarkable day, and that is the finding: 10,241 attempts, 95.47% success, ₹1.20 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,241, successes=9,777, failed=446, pending=18, settled_value_inr=12,049,151.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.

Refs: enterprise_data/warehouse/transactions, RPT-D03-DAILY, enterprise_data/warehouse/reference/incidents.parquet
