---
id: RPT-D199-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 22 Jul 2026)

**Report ID:** RPT-D199-DAILY · **Day 199 of 206** · **Derived from:** 13,513 transaction rows queried live from the warehouse

## Summary

The rail took **13,513 payment attempts** on Wednesday 22 July 2026 (Working day) and settled **₹1.94 Cr** across 12,983 successful payments. Volume was +0.0% on yesterday and −9.2% on the same weekday last week. Success closed at **96.08%**, in line with the trailing 28-day median of 96.23%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,513 | +0.0% | −9.2% | 15,928 |
| Successful payments | 12,983 | −0.1% | −9.6% | 15,310 |
| Success rate | 96.08% | −0.13pp | −0.45pp | 96.15% |
| Settled value | ₹1.94 Cr | +0.7% | −10.8% | ₹2.09 Cr |
| Average ticket | ₹1,492 | +0.8% | −1.3% | ₹1,364 |
| Technical declines | 0.392% | −0.03pp | +0.06pp | 0.450% |
| Business declines | 2.953% | +0.11pp | +0.14pp | 2.822% |
| Risk declines | 0.133% | −0.01pp | +0.06pp | 0.109% |
| Timeout declines | 0.348% | +0.08pp | +0.21pp | 0.379% |
| Retry share | 1.13% | −0.03pp | +0.14pp | 1.31% |
| Latency p95 | 1,285 ms | −2.4% | −1.2% | 1,300 ms |
| Active customers | 11,413 | +0.1% | −7.6% | 13,001 |
| Active merchants | 1,571 | +1.6% | +0.1% | 1,606 |

## What moved

- Product UPI QR Payments ran at 95.55% success on 2,200 attempts (16.3% of the day), 1.09pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,936 | 29.1% | 95.58% | ₹40.62 L | −13.1% |
| UPI Person to Merchant | 2,771 | 20.5% | 96.14% | ₹24.40 L | −24.2% |
| UPI QR Payments | 2,200 | 16.3% | 95.55% | ₹8.68 L | −13.2% |
| UPI Lite | 2,011 | 14.9% | 99.10% | ₹1.79 L | −21.3% |
| UPI Circle | 756 | 5.6% | 98.41% | ₹6.36 L | −8.1% |
| Credit on UPI | 612 | 4.5% | 95.75% | ₹48.67 L | +22.5% |
| UPI AutoPay | 384 | 2.8% | 86.46% | ₹6.87 L | +1.5% |
| RuPay Credit on UPI | 372 | 2.8% | 95.43% | ₹22.15 L | +0.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,323 | 96.69% | 96.24% | ₹61.48 L | normal |
| HDFC Bank | 1,418 | 96.40% | 96.41% | ₹21.06 L | normal |
| Bank of Baroda | 1,057 | 94.42% | 96.45% | ₹11.83 L | ⚠ outlier |
| Union Bank of India | 938 | 95.63% | 96.18% | ₹16.30 L | normal |
| Punjab National Bank | 853 | 95.66% | 95.90% | ₹10.44 L | normal |
| Axis Bank | 852 | 95.07% | 96.34% | ₹14.04 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,430 | 95.88% | 96.22% | ₹96.77 L | normal |
| Google Pay | 4,456 | 96.36% | 96.12% | ₹53.98 L | normal |
| Paytm | 1,076 | 96.10% | 96.17% | ₹17.09 L | normal |
| Navi | 467 | 97.00% | 96.33% | ₹8.55 L | normal |
| SuperMoney | 283 | 95.05% | 96.54% | ₹3.89 L | normal |
| BHIM | 138 | 92.75% | 95.69% | ₹1.83 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,907 | 96.52% | ₹50.69 L |
| Food & Beverage | 2,483 | 96.98% | ₹13.11 L |
| Mobility | 1,165 | 96.82% | ₹5.98 L |
| Bills | 803 | 95.77% | ₹7.23 L |
| Healthcare | 536 | 97.39% | ₹10.28 L |
| Digital | 222 | 92.34% | ₹92,298 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,986 | 29.5% | 96.24% | ₹56.39 L |
| North | 3,451 | 25.5% | 96.09% | ₹43.54 L |
| West | 3,346 | 24.8% | 95.37% | ₹56.49 L |
| East | 1,569 | 11.6% | 96.30% | ₹23.59 L |
| Central | 1,161 | 8.6% | 97.24% | ₹13.75 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 96.88% | ₹2.70 L |
| Rapid Bazaar | Key Account | Retail | 366 | 96.99% | ₹1.41 L |
| Vasant Wardrobe | Key Account | Retail | 71 | 94.37% | ₹1.35 L |
| Swift Grill | Large | Food & Beverage | 45 | 95.56% | ₹1.33 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 64 | 98.44% | ₹1.09 L |
| Hampi Styles | Key Account | Retail | 36 | 94.44% | ₹97,113 |
| Hampi Stores 2298 | Key Account | Retail | 96 | 95.83% | ₹89,031 |
| Urban Boutique | Key Account | Retail | 104 | 94.23% | ₹70,341 |

## Failure analysis

Of 517 declined attempts, 399 were business declines (2.953% of attempts — balances, PINs and limits), 53 technical (0.392%), 47 timeouts (0.348%) and 18 risk declines (0.133%).

153 attempts were re-presentations of an earlier failure (1.13% of the day); 69.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 180 | 1.332% | 1.193% |
| ZM | Invalid UPI PIN | business | Customer | 129 | 0.955% | 0.977% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.326% | 0.326% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.207% | 0.184% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.192% | 0.171% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.170% | 0.131% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.126% | 0.113% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.126% | 0.087% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 117 | 112 |
| Auto-reversals | 30 | 23 |
| Disputes / chargebacks | 20 | 15 |
| Value returned | ₹1.54 L | ₹1.97 L |

## Customer behaviour

11,413 distinct customers transacted (−12.6% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,557 | 3,986 | 1.12 | 95.99% | ₹1,385 |
| power | 2,531 | 3,315 | 1.31 | 95.84% | ₹2,002 |
| merchant_heavy | 2,596 | 3,078 | 1.19 | 95.97% | ₹1,233 |
| small_ticket | 1,664 | 2,001 | 1.20 | 96.75% | ₹568 |
| occasional | 846 | 888 | 1.05 | 96.17% | ₹2,306 |
| new | 191 | 217 | 1.14 | 96.31% | ₹957 |
| dormant_returning | 28 | 28 | 1.00 | 96.43% | ₹1,073 |

## Operational events

- **INC-BANK-0012** (Sev-3) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 23:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0064** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI QR Payments ran at 95.55% success on 2,200 attempts (16.3% of the day), 1.09pp down its own 28-day median.
- Issuer Bank of Baroda ran at 94.42% success on 1,057 attempts (7.8% of the day), 2.03pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

22 July ran on trend at 96.08% success and ₹1.94 Cr settled. The movement worth carrying forward is in the product mix: product UPI QR Payments ran at 95.55% success on 2,200 attempts (16.3% of the day), 1.09pp down its own 28-day median. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,513, successes=12,983, failed=517, pending=13, settled_value_inr=19,375,678.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI QR Payments; attempts=2,200; success_rate=95.55; own_median=96.64; z=-2.76
- incidents: event_id=INC-BANK-0012; kind=bank_outage; severity=Sev-3; window=2026-07-20 to 2026-07-23; success_impact_pp=-4.37; volume_impact_pct=-3.88
- banks: payer_bank=Bank of Baroda; attempts=1,057; success_rate=94.42; own_median=96.44; z=-2.31
- incidents: event_id=CMP-0064; kind=merchant_campaign; severity=Sev-3; window=2026-07-22 to 2026-07-27; success_impact_pp=-0.11; volume_impact_pct=44.38

Refs: enterprise_data/warehouse/transactions, RPT-D198-DAILY, enterprise_data/warehouse/reference/incidents.parquet
