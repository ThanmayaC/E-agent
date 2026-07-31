---
id: RPT-D109-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 23 Apr 2026)

**Report ID:** RPT-D109-DAILY · **Day 109 of 206** · **Derived from:** 11,451 transaction rows queried live from the warehouse

## Summary

The rail took **11,451 payment attempts** on Thursday 23 April 2026 (Working day) and settled **₹1.61 Cr** across 10,921 successful payments. Volume was +4.8% on yesterday and −1.7% on the same weekday last week. Success closed at **95.37%**, below the trailing 28-day median of 95.92%.

19 disputes were raised, 2.7 sigma above the trailing median of 11.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,451 | +4.8% | −1.7% | 12,815 |
| Successful payments | 10,921 | +4.9% | −1.7% | 12,217 |
| Success rate | 95.37% | +0.13pp | −0.02pp | 95.29% |
| Settled value | ₹1.61 Cr | +0.8% | −2.1% | ₹1.65 Cr |
| Average ticket | ₹1,475 | −4.0% | −0.3% | ₹1,358 |
| Technical declines | 0.585% | +0.06pp | −0.08pp | 0.586% |
| Business declines | 3.415% | −0.10pp | +0.14pp | 3.159% |
| Risk declines | 0.183% | +0.06pp | −0.01pp | 0.143% |
| Timeout declines | 0.332% | −0.14pp | −0.05pp | 0.699% |
| Retry share | 1.31% | −0.18pp | +0.01pp | 1.67% |
| Latency p95 | 1,296 ms | +3.7% | +2.9% | 1,346 ms |
| Active customers | 9,729 | +4.4% | −1.2% | 10,623 |
| Active merchants | 1,365 | +0.2% | −1.1% | 1,387 |

## What moved

- Product UPI Circle is compounding — attempts up 44% across the trailing window to 332 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 31% across the trailing window to 1,142 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,605 | 31.5% | 94.65% | ₹40.17 L | −18.5% |
| UPI Person to Merchant | 3,136 | 27.4% | 95.41% | ₹30.44 L | −9.6% |
| UPI QR Payments | 1,912 | 16.7% | 96.08% | ₹8.08 L | −11.9% |
| UPI Lite | 1,142 | 10.0% | 98.95% | ₹1.01 L | +3.8% |
| RuPay Credit on UPI | 365 | 3.2% | 92.60% | ₹22.05 L | +16.8% |
| UPI Circle | 332 | 2.9% | 96.69% | ₹3.11 L | +19.2% |
| UPI AutoPay | 304 | 2.7% | 89.14% | ₹5.40 L | −5.6% |
| Credit on UPI | 257 | 2.2% | 94.55% | ₹22.90 L | +21.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,601 | 95.47% | 95.92% | ₹46.25 L | normal |
| HDFC Bank | 1,267 | 96.13% | 95.95% | ₹17.77 L | normal |
| Bank of Baroda | 900 | 95.11% | 95.88% | ₹9.11 L | normal |
| Union Bank of India | 775 | 94.45% | 95.72% | ₹14.86 L | normal |
| Punjab National Bank | 723 | 95.30% | 95.58% | ₹9.59 L | normal |
| ICICI Bank | 714 | 95.38% | 96.36% | ₹16.31 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,415 | 95.59% | 95.80% | ₹74.98 L | normal |
| Google Pay | 3,756 | 94.99% | 95.63% | ₹49.63 L | normal |
| Paytm | 944 | 95.87% | 95.75% | ₹14.06 L | normal |
| Navi | 419 | 96.66% | 96.24% | ₹6.71 L | normal |
| SuperMoney | 206 | 92.72% | 94.87% | ₹3.48 L | normal |
| BHIM | 127 | 94.49% | 95.91% | ₹1.33 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,177 | 95.91% | ₹39.52 L |
| Food & Beverage | 1,992 | 96.23% | ₹10.01 L |
| Mobility | 909 | 96.81% | ₹5.80 L |
| Bills | 711 | 95.36% | ₹7.30 L |
| Healthcare | 430 | 96.05% | ₹7.27 L |
| Digital | 183 | 95.08% | ₹1.00 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,369 | 29.4% | 94.78% | ₹46.78 L |
| North | 2,981 | 26.0% | 95.50% | ₹41.23 L |
| West | 2,848 | 24.9% | 95.65% | ₹44.55 L |
| East | 1,292 | 11.3% | 95.59% | ₹15.34 L |
| Central | 961 | 8.4% | 95.94% | ₹13.23 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 100.00% | ₹2.80 L |
| Rapid Bazaar | Key Account | Retail | 296 | 95.95% | ₹1.46 L |
| Urban Boutique | Key Account | Retail | 85 | 97.65% | ₹1.11 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 65 | 96.92% | ₹1.06 L |
| Hampi Styles | Key Account | Retail | 38 | 94.74% | ₹69,433 |
| Vasant Wardrobe | Key Account | Retail | 57 | 92.98% | ₹63,589 |
| Hampi Stores 2298 | Key Account | Retail | 101 | 94.06% | ₹61,599 |
| Ujjwal Water Board | Key Account | Bills | 38 | 89.47% | ₹56,405 |

## Failure analysis

Of 517 declined attempts, 391 were business declines (3.415% of attempts — balances, PINs and limits), 67 technical (0.585%), 38 timeouts (0.332%) and 21 risk declines (0.183%).

150 attempts were re-presentations of an earlier failure (1.31% of the day); 68.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 169 | 1.476% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 120 | 1.048% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.419% | 0.378% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.262% | 0.220% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.245% | 0.194% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.210% | 0.195% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 19 | 0.166% | 0.117% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.157% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 89 | 80 |
| Auto-reversals | 23 | 29 |
| Disputes / chargebacks | 19 | 11 |
| Value returned | ₹2.14 L | ₹1.55 L |

## Customer behaviour

9,729 distinct customers transacted (−8.2% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,988 | 3,340 | 1.12 | 94.94% | ₹1,426 |
| power | 2,039 | 2,669 | 1.31 | 95.58% | ₹2,050 |
| merchant_heavy | 2,180 | 2,569 | 1.18 | 95.25% | ₹1,215 |
| small_ticket | 1,519 | 1,820 | 1.20 | 95.88% | ₹609 |
| occasional | 783 | 818 | 1.04 | 95.84% | ₹1,795 |
| new | 185 | 200 | 1.08 | 95.00% | ₹800 |
| dormant_returning | 35 | 35 | 1.00 | 94.29% | ₹642 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.

## Risks and opportunities

### Risks

- 19 disputes were raised, 2.7 sigma above the trailing median of 11.
- Product RuPay Credit on UPI ran at 92.60% success on 365 attempts (3.2% of the day), 2.85pp down its own 28-day median.
- Category Travel ran at 88.11% success on 143 attempts (1.8% of the day), 6.32pp down its own 28-day median.
- Category Services ran at 91.51% success on 106 attempts (1.4% of the day), 4.55pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 44% across the trailing window to 332 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 31% across the trailing window to 1,142 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 23 April: success came in 0.55pp below baseline at 95.37% on 11,451 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,451, successes=10,921, failed=517, pending=13, settled_value_inr=16,113,255.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=19; trailing_median=11; z=2.7
- products: product_name=UPI Circle; attempts=332; window_growth_pct=43.6; success_rate=96.69
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- products: product_name=UPI Lite; attempts=1,142; window_growth_pct=30.8; success_rate=98.95
- products: product_name=RuPay Credit on UPI; attempts=365; success_rate=92.6; own_median=95.45; z=-2.22
- categories: mcc_category=Travel; attempts=143; success_rate=88.11; own_median=94.43; z=-2.71
- categories: mcc_category=Services; attempts=106; success_rate=91.51; own_median=96.06; z=-2.41

Refs: enterprise_data/warehouse/transactions, RPT-D108-DAILY, enterprise_data/warehouse/reference/incidents.parquet
