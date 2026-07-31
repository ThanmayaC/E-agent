---
id: RPT-D112-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 26 Apr 2026)

**Report ID:** RPT-D112-DAILY · **Day 112 of 206** · **Derived from:** 10,845 transaction rows queried live from the warehouse

## Summary

The rail took **10,845 payment attempts** on Sunday 26 April 2026 (Weekend) and settled **₹1.28 Cr** across 10,330 successful payments. Volume was −17.0% on yesterday and −22.2% on the same weekday last week. Success closed at **95.25%**, below the trailing 28-day median of 95.88%.

Decline code Z9 (Insufficient funds) fired 196 times — 1.807% of attempts against a trailing 1.303%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,845 | −17.0% | −22.2% | 12,702 |
| Successful payments | 10,330 | −17.2% | −22.5% | 12,107 |
| Success rate | 95.25% | −0.18pp | −0.38pp | 95.28% |
| Settled value | ₹1.28 Cr | −19.0% | −17.1% | ₹1.63 Cr |
| Average ticket | ₹1,240 | −2.2% | +7.0% | ₹1,350 |
| Technical declines | 0.507% | +0.03pp | +0.09pp | 0.584% |
| Business declines | 3.808% | +0.37pp | +0.41pp | 3.210% |
| Risk declines | 0.111% | −0.03pp | −0.02pp | 0.142% |
| Timeout declines | 0.184% | −0.24pp | −0.12pp | 0.665% |
| Retry share | 1.40% | −0.01pp | +0.22pp | 1.64% |
| Latency p95 | 1,213 ms | −1.0% | −1.0% | 1,335 ms |
| Active customers | 9,299 | −14.9% | −19.0% | 10,554 |
| Active merchants | 1,367 | −2.0% | −3.5% | 1,386 |

## What moved

- Product UPI Circle is compounding — attempts up 35% across the trailing window to 356 today, with success holding, so the growth is healthy and worth funding.
- Category Food & Beverage carried 1,698 attempts, 16% down its trailing median and 23.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,611 | 33.3% | 94.82% | ₹36.21 L | −16.8% |
| UPI Person to Merchant | 2,767 | 25.5% | 95.99% | ₹25.66 L | −19.4% |
| UPI QR Payments | 1,969 | 18.2% | 95.38% | ₹8.91 L | −9.3% |
| UPI Lite | 1,158 | 10.7% | 98.79% | ₹98,749 | +1.9% |
| UPI Circle | 356 | 3.3% | 96.63% | ₹3.11 L | +24.9% |
| UPI AutoPay | 331 | 3.1% | 86.40% | ₹5.18 L | +3.0% |
| RuPay Credit on UPI | 215 | 2.0% | 94.42% | ₹14.21 L | −32.8% |
| Credit on UPI | 128 | 1.2% | 92.97% | ₹11.81 L | −42.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,354 | 95.23% | 95.83% | ₹45.71 L | normal |
| HDFC Bank | 1,195 | 95.56% | 95.95% | ₹12.17 L | normal |
| Bank of Baroda | 786 | 94.91% | 95.86% | ₹8.70 L | normal |
| Union Bank of India | 760 | 93.55% | 95.41% | ₹8.05 L | normal |
| Punjab National Bank | 697 | 94.69% | 95.47% | ₹8.90 L | normal |
| Axis Bank | 663 | 95.93% | 95.80% | ₹7.45 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,046 | 95.42% | 95.78% | ₹58.42 L | normal |
| Google Pay | 3,612 | 95.13% | 95.59% | ₹42.38 L | normal |
| Paytm | 893 | 94.74% | 95.61% | ₹7.51 L | normal |
| Navi | 419 | 95.70% | 96.40% | ₹6.27 L | normal |
| SuperMoney | 190 | 95.79% | 95.12% | ₹4.55 L | normal |
| FamApp | 117 | 94.02% | 95.97% | ₹68,614 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,732 | 95.72% | ₹28.00 L |
| Food & Beverage | 1,698 | 96.64% | ₹7.49 L |
| Bills | 928 | 95.15% | ₹9.55 L |
| Mobility | 859 | 96.97% | ₹5.00 L |
| Healthcare | 407 | 95.58% | ₹2.65 L |
| Digital | 240 | 90.83% | ₹1.12 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,245 | 29.9% | 94.95% | ₹42.54 L |
| West | 2,722 | 25.1% | 95.22% | ₹32.14 L |
| North | 2,644 | 24.4% | 95.80% | ₹30.48 L |
| East | 1,303 | 12.0% | 94.63% | ₹14.59 L |
| Central | 931 | 8.6% | 95.70% | ₹8.32 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 47 | 100.00% | ₹81,489 |
| Rapid Bazaar | Key Account | Retail | 290 | 97.24% | ₹76,461 |
| Girnar Connect | Key Account | Bills | 182 | 96.70% | ₹74,091 |
| Aravalli Pharmacy | Large | Healthcare | 73 | 97.26% | ₹72,946 |
| Ujjwal Water Board | Key Account | Bills | 42 | 92.86% | ₹72,327 |
| Vega Electronics | Large | Retail | 17 | 100.00% | ₹63,490 |
| Hampi Stores 2298 | Key Account | Retail | 76 | 93.42% | ₹47,880 |
| Yamuna Restaurant | Key Account | Food & Beverage | 34 | 94.12% | ₹46,297 |

## Failure analysis

Of 500 declined attempts, 413 were business declines (3.808% of attempts — balances, PINs and limits), 55 technical (0.507%), 20 timeouts (0.184%) and 12 risk declines (0.111%).

152 attempts were re-presentations of an earlier failure (1.40% of the day); 71.7% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 196 times — 1.807% of attempts against a trailing 1.303%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 196 | 1.807% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 112 | 1.033% | 1.021% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.489% | 0.389% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.295% | 0.220% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.212% | 0.212% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 12 | 0.111% | 0.117% |
| U69 | Beneficiary bank offline | technical | Issuer | 12 | 0.111% | 0.076% |
| U28 | Remitter bank unavailable | technical | Issuer | 11 | 0.101% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 81 | 82 |
| Auto-reversals | 23 | 28 |
| Disputes / chargebacks | 18 | 11 |
| Value returned | ₹1.00 L | ₹1.55 L |

## Customer behaviour

9,299 distinct customers transacted (−13.1% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,870 | 3,194 | 1.11 | 95.87% | ₹1,359 |
| power | 2,056 | 2,608 | 1.27 | 95.28% | ₹1,550 |
| merchant_heavy | 2,089 | 2,424 | 1.16 | 94.68% | ₹903 |
| small_ticket | 1,407 | 1,690 | 1.20 | 96.15% | ₹610 |
| occasional | 687 | 729 | 1.06 | 92.46% | ₹1,312 |
| new | 165 | 175 | 1.06 | 94.29% | ₹1,305 |
| dormant_returning | 25 | 25 | 1.00 | 96.00% | ₹782 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 196 times — 1.807% of attempts against a trailing 1.303%. Owner: Customer.

### Opportunities

- Product UPI Circle is compounding — attempts up 35% across the trailing window to 356 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 26 April: success came in 0.62pp below baseline at 95.25% on 10,845 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,845, successes=10,330, failed=500, pending=15, settled_value_inr=12,807,248.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=196; rate_pct=1.81; trailing_rate_pct=1.3; owner=Customer; z=3.34
- products: product_name=UPI Circle; attempts=356; window_growth_pct=35.2; success_rate=96.63
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- categories: mcc_category=Food & Beverage; attempts=1,698; own_median=2,019; z=-2.35
- incidents: event_id=CMP-0056; kind=merchant_campaign; severity=Sev-3; window=2026-04-24 to 2026-04-30; success_impact_pp=-0.17; volume_impact_pct=66.88

Refs: enterprise_data/warehouse/transactions, RPT-D111-DAILY, enterprise_data/warehouse/reference/incidents.parquet
