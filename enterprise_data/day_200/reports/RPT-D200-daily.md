---
id: RPT-D200-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 23 Jul 2026)

**Report ID:** RPT-D200-DAILY · **Day 200 of 206** · **Derived from:** 13,950 transaction rows queried live from the warehouse

## Summary

The rail took **13,950 payment attempts** on Thursday 23 July 2026 (Working day) and settled **₹1.87 Cr** across 13,385 successful payments. Volume was +3.2% on yesterday and −4.4% on the same weekday last week. Success closed at **95.95%**, below the trailing 28-day median of 96.23%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,950 | +3.2% | −4.4% | 15,842 |
| Successful payments | 13,385 | +3.1% | −4.5% | 15,226 |
| Success rate | 95.95% | −0.13pp | −0.10pp | 96.14% |
| Settled value | ₹1.87 Cr | −3.6% | −6.5% | ₹2.08 Cr |
| Average ticket | ₹1,396 | −6.5% | −2.1% | ₹1,365 |
| Technical declines | 0.516% | +0.12pp | +0.19pp | 0.453% |
| Business declines | 2.932% | −0.02pp | −0.25pp | 2.827% |
| Risk declines | 0.186% | +0.05pp | +0.07pp | 0.112% |
| Timeout declines | 0.315% | −0.03pp | +0.08pp | 0.376% |
| Retry share | 1.17% | +0.04pp | +0.16pp | 1.30% |
| Latency p95 | 1,285 ms | −0.0% | −2.2% | 1,300 ms |
| Active customers | 11,767 | +3.1% | −3.7% | 12,948 |
| Active merchants | 1,602 | +2.0% | +1.1% | 1,605 |

## What moved

- Product UPI Person to Person ran at 94.33% success on 3,829 attempts (27.4% of the day), 0.91pp down its own 28-day median.
- Issuer Bank of Baroda ran at 93.87% success on 1,060 attempts (7.6% of the day), 2.58pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,829 | 27.4% | 94.33% | ₹40.58 L | −15.4% |
| UPI Person to Merchant | 3,315 | 23.8% | 95.81% | ₹30.71 L | −9.3% |
| UPI QR Payments | 2,328 | 16.7% | 96.86% | ₹10.45 L | −8.1% |
| UPI Lite | 1,891 | 13.6% | 99.47% | ₹1.68 L | −26.0% |
| UPI Circle | 789 | 5.7% | 96.96% | ₹5.62 L | −4.1% |
| Credit on UPI | 577 | 4.1% | 96.01% | ₹45.36 L | +13.9% |
| RuPay Credit on UPI | 400 | 2.9% | 96.00% | ₹26.36 L | +9.3% |
| UPI AutoPay | 372 | 2.7% | 93.28% | ₹7.43 L | −1.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,467 | 96.49% | 96.28% | ₹64.17 L | normal |
| HDFC Bank | 1,505 | 96.15% | 96.41% | ₹18.82 L | normal |
| Bank of Baroda | 1,060 | 93.87% | 96.45% | ₹10.60 L | ⚠ outlier |
| Axis Bank | 913 | 96.28% | 96.34% | ₹12.59 L | normal |
| Union Bank of India | 911 | 96.05% | 96.18% | ₹14.28 L | normal |
| Punjab National Bank | 828 | 94.69% | 95.76% | ₹8.31 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,563 | 95.87% | 96.22% | ₹79.76 L | normal |
| Google Pay | 4,583 | 96.16% | 96.18% | ₹63.74 L | normal |
| Paytm | 1,197 | 95.91% | 96.17% | ₹23.39 L | normal |
| Navi | 494 | 97.57% | 96.37% | ₹6.72 L | normal |
| SuperMoney | 278 | 92.81% | 96.54% | ₹2.37 L | ⚠ outlier |
| BHIM | 153 | 96.08% | 95.54% | ₹1.31 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,258 | 96.62% | ₹61.56 L |
| Food & Beverage | 2,533 | 97.04% | ₹11.69 L |
| Mobility | 1,244 | 97.91% | ₹7.16 L |
| Bills | 863 | 95.37% | ₹9.33 L |
| Healthcare | 543 | 97.42% | ₹8.34 L |
| Digital | 236 | 94.07% | ₹1.13 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,035 | 28.9% | 95.89% | ₹67.44 L |
| North | 3,545 | 25.4% | 95.63% | ₹42.21 L |
| West | 3,528 | 25.3% | 96.15% | ₹43.87 L |
| East | 1,573 | 11.3% | 95.80% | ₹21.28 L |
| Central | 1,269 | 9.1% | 96.69% | ₹12.04 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 89 | 94.38% | ₹2.43 L |
| Vega Electronics | Large | Retail | 33 | 96.97% | ₹2.16 L |
| Rapid Bazaar | Key Account | Retail | 397 | 97.73% | ₹1.71 L |
| Urban Boutique | Key Account | Retail | 115 | 95.65% | ₹1.29 L |
| Hampi Styles | Key Account | Retail | 46 | 95.65% | ₹1.16 L |
| Hampi Stores 2298 | Key Account | Retail | 117 | 94.02% | ₹1.02 L |
| Girnar Connect | Key Account | Bills | 155 | 97.42% | ₹74,068 |
| Yamuna Restaurant | Key Account | Food & Beverage | 80 | 96.25% | ₹73,005 |

## Failure analysis

Of 551 declined attempts, 409 were business declines (2.932% of attempts — balances, PINs and limits), 72 technical (0.516%), 44 timeouts (0.315%) and 26 risk declines (0.186%).

163 attempts were re-presentations of an earlier failure (1.17% of the day); 68.1% of them succeeded.

- Decline code U16 (Risk threshold exceeded at remitter) fired 24 times — 0.172% of attempts against a trailing 0.095%. Owner: Issuer.
- Decline code U28 (Remitter bank unavailable) fired 24 times — 0.172% of attempts against a trailing 0.115%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 167 | 1.197% | 1.193% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 0.975% | 0.959% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.387% | 0.326% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.201% | 0.184% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.179% | 0.131% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.172% | 0.115% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.172% | 0.171% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 24 | 0.172% | 0.095% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 109 | 112 |
| Auto-reversals | 25 | 23 |
| Disputes / chargebacks | 16 | 15 |
| Value returned | ₹92,379 | ₹1.80 L |

## Customer behaviour

11,767 distinct customers transacted (−9.9% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,758 | 4,259 | 1.13 | 95.82% | ₹1,474 |
| power | 2,561 | 3,383 | 1.32 | 95.71% | ₹1,980 |
| merchant_heavy | 2,688 | 3,169 | 1.18 | 96.06% | ₹976 |
| small_ticket | 1,686 | 2,010 | 1.19 | 96.17% | ₹604 |
| occasional | 861 | 899 | 1.04 | 96.66% | ₹1,366 |
| new | 193 | 210 | 1.09 | 96.19% | ₹763 |
| dormant_returning | 20 | 20 | 1.00 | 90.00% | ₹577 |

## Operational events

- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **INC-BANK-0012** (Sev-3) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 23:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0064** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI Person to Person ran at 94.33% success on 3,829 attempts (27.4% of the day), 0.91pp down its own 28-day median.
- Decline code U16 (Risk threshold exceeded at remitter) fired 24 times — 0.172% of attempts against a trailing 0.095%. Owner: Issuer.
- Issuer Bank of Baroda ran at 93.87% success on 1,060 attempts (7.6% of the day), 2.58pp down its own 28-day median.
- Decline code U28 (Remitter bank unavailable) fired 24 times — 0.172% of attempts against a trailing 0.115%. Owner: Issuer.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

23 July ran on trend at 95.95% success and ₹1.87 Cr settled. The movement worth carrying forward is in the product mix: product UPI Person to Person ran at 94.33% success on 3,829 attempts (27.4% of the day), 0.91pp down its own 28-day median. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,950, successes=13,385, failed=551, pending=14, settled_value_inr=18,683,550.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Person to Person; attempts=3,829; success_rate=94.33; own_median=95.25; z=-2.51
- failures: failure_code=U16; count=24; rate_pct=0.17; trailing_rate_pct=0.09; owner=Issuer; z=2.71
- banks: payer_bank=Bank of Baroda; attempts=1,060; success_rate=93.87; own_median=96.44; z=-2.9
- failures: failure_code=U28; count=24; rate_pct=0.17; trailing_rate_pct=0.12; owner=Issuer; z=2.22
- incidents: event_id=MAINT-0084; kind=maintenance_window; severity=Sev-3; window=2026-01-24 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- incidents: event_id=INC-BANK-0012; kind=bank_outage; severity=Sev-3; window=2026-07-20 to 2026-07-23; success_impact_pp=-4.37; volume_impact_pct=-3.88
- incidents: event_id=CMP-0064; kind=merchant_campaign; severity=Sev-3; window=2026-07-22 to 2026-07-27; success_impact_pp=-0.11; volume_impact_pct=44.38

Refs: enterprise_data/warehouse/transactions, RPT-D199-DAILY, enterprise_data/warehouse/reference/incidents.parquet
