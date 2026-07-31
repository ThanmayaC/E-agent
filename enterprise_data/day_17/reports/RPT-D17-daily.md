---
id: RPT-D17-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-21T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 21 Jan 2026)

**Report ID:** RPT-D17-DAILY · **Day 17 of 206** · **Derived from:** 10,003 transaction rows queried live from the warehouse

## Summary

The rail took **10,003 payment attempts** on Wednesday 21 January 2026 (Working day) and settled **₹1.10 Cr** across 9,503 successful payments. Volume was +7.0% on yesterday and −10.1% on the same weekday last week. Success closed at **95.00%**, below the trailing 28-day median of 95.28%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,003 | +7.0% | −10.1% | 10,222 |
| Successful payments | 9,503 | +7.4% | −10.9% | 9,723 |
| Success rate | 95.00% | +0.40pp | −0.84pp | 95.09% |
| Settled value | ₹1.10 Cr | +1.0% | −15.9% | ₹1.15 Cr |
| Average ticket | ₹1,161 | −5.9% | −5.6% | ₹1,187 |
| Technical declines | 0.600% | −0.01pp | +0.04pp | 0.638% |
| Business declines | 3.759% | −0.50pp | +0.68pp | 3.610% |
| Risk declines | 0.140% | +0.04pp | +0.05pp | 0.131% |
| Timeout declines | 0.430% | +0.11pp | +0.12pp | 0.397% |
| Retry share | 1.55% | −0.29pp | +0.21pp | 1.51% |
| Latency p95 | 1,251 ms | −3.7% | +2.2% | 1,247 ms |
| Active customers | 8,497 | +5.9% | −8.9% | 8,674 |
| Active merchants | 1,187 | +1.2% | −1.7% | 1,199 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,895 | 38.9% | 94.48% | ₹39.59 L | −2.6% |
| UPI Person to Merchant | 2,768 | 27.7% | 95.56% | ₹28.31 L | −6.5% |
| UPI QR Payments | 1,649 | 16.5% | 95.33% | ₹6.96 L | −1.8% |
| UPI Lite | 641 | 6.4% | 98.75% | ₹57,880 | +0.6% |
| UPI AutoPay | 311 | 3.1% | 89.71% | ₹6.18 L | +2.0% |
| RuPay Credit on UPI | 227 | 2.3% | 92.07% | ₹8.30 L | +21.1% |
| Credit on UPI | 126 | 1.3% | 92.86% | ₹10.21 L | −12.5% |
| UPI International | 88 | 0.9% | 93.18% | ₹4.91 L | +18.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,170 | 94.89% | 94.89% | ₹35.02 L | normal |
| HDFC Bank | 1,136 | 95.16% | 96.03% | ₹12.06 L | normal |
| Bank of Baroda | 772 | 95.34% | 94.57% | ₹7.96 L | normal |
| Union Bank of India | 692 | 94.22% | 94.75% | ₹8.64 L | normal |
| Punjab National Bank | 610 | 94.59% | 94.84% | ₹7.64 L | normal |
| Axis Bank | 609 | 96.22% | 95.37% | ₹7.69 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,714 | 94.68% | 95.35% | ₹51.81 L | normal |
| Google Pay | 3,332 | 95.35% | 95.22% | ₹36.91 L | normal |
| Paytm | 804 | 94.03% | 94.57% | ₹9.38 L | normal |
| Navi | 373 | 95.98% | 95.11% | ₹4.30 L | normal |
| SuperMoney | 202 | 94.55% | 95.93% | ₹2.46 L | normal |
| BHIM | 106 | 96.23% | 95.41% | ₹87,961 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,551 | 95.30% | ₹30.74 L |
| Food & Beverage | 1,484 | 95.75% | ₹6.97 L |
| Mobility | 683 | 97.51% | ₹4.14 L |
| Bills | 599 | 95.83% | ₹7.61 L |
| Healthcare | 308 | 94.48% | ₹2.43 L |
| Digital | 188 | 92.55% | ₹96,904 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,014 | 30.1% | 94.76% | ₹33.18 L |
| North | 2,519 | 25.2% | 95.51% | ₹28.47 L |
| West | 2,438 | 24.4% | 94.91% | ₹28.67 L |
| East | 1,162 | 11.6% | 94.84% | ₹11.77 L |
| Central | 870 | 8.7% | 94.83% | ₹8.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 87 | 89.66% | ₹2.84 L |
| Vega Electronics | Large | Retail | 34 | 97.06% | ₹1.92 L |
| Rapid Bazaar | Key Account | Retail | 241 | 96.68% | ₹1.01 L |
| Girnar Connect | Key Account | Bills | 117 | 96.58% | ₹75,616 |
| Hampi Stores 2298 | Key Account | Retail | 75 | 94.67% | ₹52,425 |
| Yamuna Restaurant | Key Account | Food & Beverage | 75 | 89.33% | ₹48,268 |
| Swift Mart 1738 | Key Account | Retail | 87 | 93.10% | ₹45,021 |
| Tejas Bites | Key Account | Food & Beverage | 104 | 95.19% | ₹41,702 |

## Failure analysis

Of 493 declined attempts, 376 were business declines (3.759% of attempts — balances, PINs and limits), 60 technical (0.600%), 43 timeouts (0.430%) and 14 risk declines (0.140%).

155 attempts were re-presentations of an earlier failure (1.55% of the day); 60.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 169 | 1.689% | 1.482% |
| ZM | Invalid UPI PIN | business | Customer | 125 | 1.250% | 1.117% |
| ZA | Transaction declined by customer | business | Customer | 40 | 0.400% | 0.383% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.250% | 0.270% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.240% | 0.183% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.230% | 0.263% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.190% | 0.178% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.140% | 0.137% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 77 | 36 |
| Auto-reversals | 26 | 22 |
| Disputes / chargebacks | 2 | 0 |
| Value returned | ₹2.04 L | ₹75,089 |

## Customer behaviour

8,497 distinct customers transacted (−3.5% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,610 | 2,953 | 1.13 | 94.62% | ₹1,172 |
| power | 1,766 | 2,330 | 1.32 | 95.06% | ₹1,597 |
| merchant_heavy | 1,931 | 2,233 | 1.16 | 94.94% | ₹886 |
| small_ticket | 1,313 | 1,577 | 1.20 | 95.43% | ₹462 |
| occasional | 675 | 700 | 1.04 | 94.57% | ₹1,289 |
| new | 174 | 181 | 1.04 | 98.90% | ₹1,065 |
| dormant_returning | 28 | 29 | 1.04 | 96.55% | ₹1,892 |

## Operational events

- **INC-BANK-0016** (Sev-1) — ICICI Bank issuer decline spike, scoped to ICICI Bank between 18:00 and 21:00. ICICI Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Product RuPay Credit on UPI ran at 92.07% success on 227 attempts (2.3% of the day), 3.06pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

21 January was an incident day: INC-BANK-0016 was live and the rail closed at 95.00% success against a 95.28% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-21` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,003, successes=9,503, failed=493, pending=7, settled_value_inr=11,037,183.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0016; kind=bank_outage; severity=Sev-1; window=2026-01-21 to 2026-01-21; success_impact_pp=-33.37; volume_impact_pct=-29.61
- products: product_name=RuPay Credit on UPI; attempts=227; success_rate=92.07; own_median=95.13; z=-3.03
- banks: payer_bank=Yes Bank; attempts=329; own_median=385; z=-3.02

Refs: enterprise_data/warehouse/transactions, RPT-D16-DAILY, enterprise_data/warehouse/reference/incidents.parquet
