---
id: RPT-D201-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 24 Jul 2026)

**Report ID:** RPT-D201-DAILY · **Day 201 of 206** · **Derived from:** 15,460 transaction rows queried live from the warehouse

## Summary

The rail took **15,460 payment attempts** on Friday 24 July 2026 (Working day) and settled **₹2.15 Cr** across 14,852 successful payments. Volume was +10.8% on yesterday and −0.8% on the same weekday last week. Success closed at **96.07%**, in line with the trailing 28-day median of 96.23%.

Decline code U54 (Transaction timed out at beneficiary) fired 35 times — 0.226% of attempts against a trailing 0.132%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,460 | +10.8% | −0.8% | 15,826 |
| Successful payments | 14,852 | +11.0% | −1.0% | 15,211 |
| Success rate | 96.07% | +0.12pp | −0.19pp | 96.14% |
| Settled value | ₹2.15 Cr | +14.8% | −1.1% | ₹2.08 Cr |
| Average ticket | ₹1,444 | +3.5% | −0.1% | ₹1,369 |
| Technical declines | 0.459% | −0.06pp | +0.04pp | 0.453% |
| Business declines | 2.878% | −0.05pp | −0.05pp | 2.829% |
| Risk declines | 0.116% | −0.07pp | +0.03pp | 0.112% |
| Timeout declines | 0.388% | +0.07pp | +0.19pp | 0.377% |
| Retry share | 1.00% | −0.17pp | −0.20pp | 1.29% |
| Latency p95 | 1,309 ms | +1.9% | +0.2% | 1,300 ms |
| Active customers | 12,807 | +8.8% | −0.1% | 12,942 |
| Active merchants | 1,590 | −0.7% | −1.7% | 1,605 |

## What moved

- Issuer State Bank of India ran at 95.75% success on 4,963 attempts (32.1% of the day), 0.57pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,441 | 28.7% | 95.32% | ₹43.18 L | −1.9% |
| UPI Person to Merchant | 3,773 | 24.4% | 96.61% | ₹33.77 L | +3.2% |
| UPI QR Payments | 2,570 | 16.6% | 96.46% | ₹10.93 L | +1.4% |
| UPI Lite | 1,915 | 12.4% | 98.54% | ₹1.74 L | −25.0% |
| UPI Circle | 801 | 5.2% | 98.00% | ₹6.93 L | −2.7% |
| Credit on UPI | 657 | 4.2% | 95.74% | ₹50.06 L | +27.9% |
| RuPay Credit on UPI | 398 | 2.6% | 94.47% | ₹18.18 L | +8.7% |
| UPI AutoPay | 366 | 2.4% | 87.70% | ₹5.80 L | −3.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,963 | 95.75% | 96.32% | ₹65.91 L | ⚠ outlier |
| HDFC Bank | 1,625 | 95.63% | 96.41% | ₹24.44 L | normal |
| Bank of Baroda | 1,199 | 95.83% | 96.45% | ₹16.23 L | normal |
| Union Bank of India | 1,072 | 96.18% | 96.18% | ₹14.83 L | normal |
| Punjab National Bank | 953 | 95.70% | 95.66% | ₹15.82 L | normal |
| Axis Bank | 949 | 96.63% | 96.34% | ₹11.54 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,361 | 95.95% | 96.22% | ₹99.94 L | normal |
| Google Pay | 5,030 | 96.34% | 96.18% | ₹71.88 L | normal |
| Paytm | 1,219 | 95.98% | 96.17% | ₹14.59 L | normal |
| Navi | 559 | 94.99% | 96.51% | ₹6.32 L | normal |
| SuperMoney | 318 | 95.60% | 96.54% | ₹5.54 L | normal |
| BHIM | 158 | 96.84% | 95.69% | ₹1.94 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,738 | 96.22% | ₹60.20 L |
| Food & Beverage | 2,708 | 97.30% | ₹14.99 L |
| Mobility | 1,291 | 97.52% | ₹7.84 L |
| Bills | 948 | 95.68% | ₹9.24 L |
| Healthcare | 583 | 97.26% | ₹12.39 L |
| Digital | 245 | 94.69% | ₹1.50 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,575 | 29.6% | 96.00% | ₹61.08 L |
| North | 3,961 | 25.6% | 95.51% | ₹55.32 L |
| West | 3,787 | 24.5% | 96.46% | ₹58.00 L |
| East | 1,777 | 11.5% | 96.34% | ₹24.26 L |
| Central | 1,360 | 8.8% | 96.47% | ₹15.85 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 90.62% | ₹2.46 L |
| Rapid Bazaar | Key Account | Retail | 424 | 97.88% | ₹2.15 L |
| Vasant Wardrobe | Key Account | Retail | 72 | 94.44% | ₹1.34 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 99 | 97.98% | ₹1.29 L |
| Swift Grill | Large | Food & Beverage | 46 | 97.83% | ₹91,449 |
| Hampi Stores 2298 | Key Account | Retail | 132 | 92.42% | ₹91,254 |
| Hampi Styles | Key Account | Retail | 33 | 96.97% | ₹90,246 |
| Girnar Connect | Key Account | Bills | 172 | 93.60% | ₹90,184 |

## Failure analysis

Of 594 declined attempts, 445 were business declines (2.878% of attempts — balances, PINs and limits), 71 technical (0.459%), 60 timeouts (0.388%) and 18 risk declines (0.116%).

154 attempts were re-presentations of an earlier failure (1.00% of the day); 70.8% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 35 times — 0.226% of attempts against a trailing 0.132%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 199 | 1.287% | 1.191% |
| ZM | Invalid UPI PIN | business | Customer | 132 | 0.854% | 0.959% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.343% | 0.326% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 35 | 0.226% | 0.132% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.220% | 0.185% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.201% | 0.171% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.123% | 0.115% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.103% | 0.087% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 134 | 112 |
| Auto-reversals | 23 | 23 |
| Disputes / chargebacks | 15 | 16 |
| Value returned | ₹1.65 L | ₹1.80 L |

## Customer behaviour

12,807 distinct customers transacted (−1.9% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,844 | 4,427 | 1.15 | 95.62% | ₹1,299 |
| power | 2,767 | 3,706 | 1.34 | 96.09% | ₹1,940 |
| merchant_heavy | 3,067 | 3,693 | 1.20 | 96.10% | ₹1,232 |
| small_ticket | 1,873 | 2,309 | 1.23 | 96.75% | ₹771 |
| occasional | 1,012 | 1,067 | 1.05 | 96.53% | ₹1,711 |
| new | 212 | 224 | 1.06 | 95.54% | ₹1,341 |
| dormant_returning | 32 | 34 | 1.06 | 91.18% | ₹1,594 |

## Operational events

- **CMP-0064** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U54 (Transaction timed out at beneficiary) fired 35 times — 0.226% of attempts against a trailing 0.132%. Owner: Issuer.
- Issuer State Bank of India ran at 95.75% success on 4,963 attempts (32.1% of the day), 0.57pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

24 July ran on trend at 96.07% success and ₹2.15 Cr settled. The movement worth carrying forward is in the decline profile: decline code U54 (Transaction timed out at beneficiary) fired 35 times — 0.226% of attempts against a trailing 0.132%. Owner: Issuer. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,460, successes=14,852, failed=594, pending=14, settled_value_inr=21,451,313.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U54; count=35; rate_pct=0.23; trailing_rate_pct=0.13; owner=Issuer; z=3.44
- banks: payer_bank=State Bank of India; attempts=4,963; success_rate=95.75; own_median=96.32; z=-2.14
- incidents: event_id=CMP-0064; kind=merchant_campaign; severity=Sev-3; window=2026-07-22 to 2026-07-27; success_impact_pp=-0.11; volume_impact_pct=44.38
- banks: payer_bank=IndusInd Bank; attempts=344; success_rate=98.26; own_median=95.79; z=2.35

Refs: enterprise_data/warehouse/transactions, RPT-D200-DAILY, enterprise_data/warehouse/reference/incidents.parquet
