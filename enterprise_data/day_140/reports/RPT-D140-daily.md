---
id: RPT-D140-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 24 May 2026)

**Report ID:** RPT-D140-DAILY · **Day 140 of 206** · **Derived from:** 12,977 transaction rows queried live from the warehouse

## Summary

The rail took **12,977 payment attempts** on Sunday 24 May 2026 (Weekend) and settled **₹1.64 Cr** across 12,373 successful payments. Volume was −12.2% on yesterday and −11.3% on the same weekday last week. Success closed at **95.35%**, below the trailing 28-day median of 96.03%.

Decline code Z9 (Insufficient funds) fired 183 times — 1.410% of attempts against a trailing 1.181%. Owner: Customer. Decline code U54 (Transaction timed out at beneficiary) fired 33 times — 0.254% of attempts against a trailing 0.153%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,977 | −12.2% | −11.3% | 14,799 |
| Successful payments | 12,373 | −12.8% | −11.6% | 14,194 |
| Success rate | 95.35% | −0.66pp | −0.36pp | 95.91% |
| Settled value | ₹1.64 Cr | −14.2% | +4.6% | ₹1.98 Cr |
| Average ticket | ₹1,327 | −1.6% | +18.4% | ₹1,395 |
| Technical declines | 0.524% | −0.04pp | +0.06pp | 0.511% |
| Business declines | 3.337% | +0.48pp | −0.04pp | 2.935% |
| Risk declines | 0.170% | +0.00pp | +0.08pp | 0.129% |
| Timeout declines | 0.470% | +0.17pp | +0.19pp | 0.408% |
| Retry share | 1.29% | +0.11pp | −0.63pp | 1.36% |
| Latency p95 | 1,235 ms | −2.1% | −1.5% | 1,288 ms |
| Active customers | 10,962 | −9.1% | −8.2% | 12,071 |
| Active merchants | 1,475 | −0.4% | −0.7% | 1,498 |

## What moved

- Category Food & Beverage ran at 96.12% success on 2,296 attempts (25.3% of the day), 0.89pp down its own 28-day median.
- Success rate closed at 95.35%, 0.68pp down the trailing median — a 2.1-sigma move.
- Issuer State Bank of India ran at 95.26% success on 4,158 attempts (32.0% of the day), 0.78pp down its own 28-day median.
- Product UPI Person to Merchant ran at 95.02% success on 3,457 attempts (26.6% of the day), 1.00pp down its own 28-day median.
- Product UPI International is compounding — attempts up 46% across the trailing window to 172 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 41% across the trailing window to 612 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,895 | 30.0% | 95.22% | ₹41.24 L | −13.2% |
| UPI Person to Merchant | 3,457 | 26.6% | 95.02% | ₹33.85 L | −11.0% |
| UPI QR Payments | 2,106 | 16.2% | 96.06% | ₹9.21 L | −10.3% |
| UPI Lite | 1,684 | 13.0% | 98.40% | ₹1.46 L | −0.7% |
| UPI Circle | 612 | 4.7% | 97.22% | ₹4.75 L | +13.3% |
| UPI AutoPay | 341 | 2.6% | 81.23% | ₹5.32 L | +3.6% |
| Credit on UPI | 244 | 1.9% | 94.67% | ₹24.34 L | −31.4% |
| RuPay Credit on UPI | 213 | 1.6% | 97.65% | ₹14.72 L | −42.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,158 | 95.26% | 96.05% | ₹47.34 L | ⚠ outlier |
| HDFC Bank | 1,409 | 96.24% | 96.18% | ₹18.77 L | normal |
| Bank of Baroda | 976 | 93.95% | 95.81% | ₹14.43 L | ⚠ outlier |
| Union Bank of India | 946 | 94.93% | 95.49% | ₹10.55 L | normal |
| Axis Bank | 774 | 95.74% | 96.52% | ₹9.19 L | normal |
| ICICI Bank | 772 | 95.73% | 96.43% | ₹10.50 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,037 | 95.46% | 95.97% | ₹82.20 L | normal |
| Google Pay | 4,360 | 95.16% | 95.93% | ₹55.00 L | normal |
| Paytm | 1,114 | 95.33% | 96.14% | ₹10.96 L | normal |
| Navi | 519 | 94.22% | 95.62% | ₹6.63 L | normal |
| SuperMoney | 233 | 98.28% | 96.38% | ₹1.82 L | normal |
| BHIM | 132 | 95.45% | 95.87% | ₹1.30 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,781 | 95.85% | ₹39.46 L |
| Food & Beverage | 2,296 | 96.12% | ₹9.89 L |
| Mobility | 1,107 | 97.20% | ₹5.50 L |
| Bills | 795 | 93.58% | ₹8.53 L |
| Healthcare | 447 | 96.42% | ₹6.83 L |
| Digital | 188 | 89.36% | ₹1.00 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,816 | 29.4% | 95.52% | ₹55.30 L |
| West | 3,307 | 25.5% | 95.07% | ₹40.31 L |
| North | 3,202 | 24.7% | 95.50% | ₹37.08 L |
| East | 1,535 | 11.8% | 95.44% | ₹20.65 L |
| Central | 1,117 | 8.6% | 94.99% | ₹10.87 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 59 | 98.31% | ₹1.81 L |
| Rapid Bazaar | Key Account | Retail | 416 | 95.67% | ₹1.43 L |
| Vega Electronics | Large | Retail | 24 | 95.83% | ₹95,796 |
| Ujjwal Water Board | Key Account | Bills | 37 | 97.30% | ₹88,007 |
| Hampi Styles | Key Account | Retail | 39 | 94.87% | ₹85,369 |
| Aravalli Pharmacy | Large | Healthcare | 81 | 91.36% | ₹82,915 |
| Hampi Stores 2298 | Key Account | Retail | 93 | 96.77% | ₹71,699 |
| Urban Boutique | Key Account | Retail | 89 | 94.38% | ₹60,722 |

## Failure analysis

Of 584 declined attempts, 433 were business declines (3.337% of attempts — balances, PINs and limits), 68 technical (0.524%), 61 timeouts (0.470%) and 22 risk declines (0.170%).

168 attempts were re-presentations of an earlier failure (1.29% of the day); 66.1% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 183 times — 1.410% of attempts against a trailing 1.181%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 33 times — 0.254% of attempts against a trailing 0.153%. Owner: Issuer.
- Decline code ZA (Transaction declined by customer) fired 53 times — 0.408% of attempts against a trailing 0.336%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 183 | 1.410% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 149 | 1.148% | 1.015% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.408% | 0.336% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 33 | 0.254% | 0.153% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.247% | 0.206% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.208% | 0.219% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.139% | 0.106% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.131% | 0.110% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 100 | 96 |
| Auto-reversals | 26 | 28 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹1.73 L | ₹1.88 L |

## Customer behaviour

10,962 distinct customers transacted (−6.7% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,395 | 3,829 | 1.13 | 95.12% | ₹1,336 |
| power | 2,339 | 3,084 | 1.32 | 95.07% | ₹1,753 |
| merchant_heavy | 2,490 | 2,951 | 1.19 | 95.70% | ₹1,036 |
| small_ticket | 1,620 | 1,930 | 1.19 | 95.75% | ₹626 |
| occasional | 898 | 943 | 1.05 | 95.23% | ₹1,538 |
| new | 191 | 210 | 1.10 | 95.24% | ₹636 |
| dormant_returning | 29 | 30 | 1.03 | 96.67% | ₹1,783 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **INC-PSP-0024** (Sev-3) — PhonePe app release regression, scoped to PhonePe between 19:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 183 times — 1.410% of attempts against a trailing 1.181%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 33 times — 0.254% of attempts against a trailing 0.153%. Owner: Issuer.
- Category Food & Beverage ran at 96.12% success on 2,296 attempts (25.3% of the day), 0.89pp down its own 28-day median.
- Success rate closed at 95.35%, 0.68pp down the trailing median — a 2.1-sigma move.
- Issuer State Bank of India ran at 95.26% success on 4,158 attempts (32.0% of the day), 0.78pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 46% across the trailing window to 172 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 41% across the trailing window to 612 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

24 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 95.35% success against a 96.03% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,977, successes=12,373, failed=584, pending=20, settled_value_inr=16,420,939.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=183; rate_pct=1.41; trailing_rate_pct=1.18; owner=Customer; z=2.73
- failures: failure_code=U54; count=33; rate_pct=0.25; trailing_rate_pct=0.15; owner=Issuer; z=4
- categories: mcc_category=Food & Beverage; attempts=2,296; success_rate=96.12; own_median=97.02; z=-3.46
- headline: success_rate=95.35; trailing_median=96.03; z=-2.14
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- banks: payer_bank=State Bank of India; attempts=4,158; success_rate=95.26; own_median=96.05; z=-2.89
- products: product_name=UPI Person to Merchant; attempts=3,457; success_rate=95.02; own_median=96.02; z=-2.73
- products: product_name=UPI International; attempts=172; window_growth_pct=46.4; success_rate=95.35
- failures: failure_code=ZA; count=53; rate_pct=0.41; trailing_rate_pct=0.34; owner=Customer; z=2.24
- products: product_name=UPI Circle; attempts=612; window_growth_pct=41; success_rate=97.22

Refs: enterprise_data/warehouse/transactions, RPT-D139-DAILY, enterprise_data/warehouse/reference/incidents.parquet
