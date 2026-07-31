---
id: RPT-D197-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-20T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 20 Jul 2026)

**Report ID:** RPT-D197-DAILY · **Day 197 of 206** · **Derived from:** 14,333 transaction rows queried live from the warehouse

## Summary

The rail took **14,333 payment attempts** on Monday 20 July 2026 (Working day) and settled **₹2.00 Cr** across 13,805 successful payments. Volume was +3.5% on yesterday and −1.5% on the same weekday last week. Success closed at **96.32%**, in line with the trailing 28-day median of 96.13%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,333 | +3.5% | −1.5% | 16,169 |
| Successful payments | 13,805 | +3.9% | −1.4% | 15,542 |
| Success rate | 96.32% | +0.40pp | +0.05pp | 96.15% |
| Settled value | ₹2.00 Cr | +33.8% | −2.6% | ₹2.10 Cr |
| Average ticket | ₹1,452 | +28.8% | −1.2% | ₹1,352 |
| Technical declines | 0.537% | +0.15pp | +0.05pp | 0.454% |
| Business declines | 2.658% | −0.56pp | −0.14pp | 2.814% |
| Risk declines | 0.105% | −0.03pp | +0.00pp | 0.106% |
| Timeout declines | 0.265% | −0.01pp | −0.00pp | 0.386% |
| Retry share | 1.21% | +0.04pp | +0.07pp | 1.32% |
| Latency p95 | 1,308 ms | +4.9% | +0.8% | 1,300 ms |
| Active customers | 11,919 | +2.8% | −1.2% | 13,161 |
| Active merchants | 1,549 | +0.7% | −2.3% | 1,610 |

## What moved

- Product Credit on UPI is compounding — attempts up 37% across the trailing window to 579 today, with success holding, so the growth is healthy and worth funding.
- Issuer Yes Bank ran at 93.60% success on 531 attempts (3.7% of the day), 2.61pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,105 | 28.6% | 95.64% | ₹42.54 L | −9.3% |
| UPI Person to Merchant | 3,237 | 22.6% | 96.20% | ₹29.49 L | −11.4% |
| UPI QR Payments | 2,323 | 16.2% | 96.86% | ₹9.86 L | −9.0% |
| UPI Lite | 1,974 | 13.8% | 99.04% | ₹1.77 L | −22.7% |
| UPI Circle | 863 | 6.0% | 97.80% | ₹7.07 L | +6.9% |
| Credit on UPI | 579 | 4.0% | 95.34% | ₹55.16 L | +19.5% |
| UPI AutoPay | 368 | 2.6% | 87.77% | ₹6.44 L | −2.6% |
| RuPay Credit on UPI | 336 | 2.3% | 96.73% | ₹16.70 L | −12.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,597 | 96.21% | 96.22% | ₹63.04 L | normal |
| HDFC Bank | 1,561 | 96.41% | 96.39% | ₹19.08 L | normal |
| Bank of Baroda | 1,182 | 96.70% | 96.35% | ₹16.82 L | normal |
| Union Bank of India | 951 | 96.00% | 96.29% | ₹12.37 L | normal |
| Punjab National Bank | 863 | 96.52% | 95.90% | ₹12.32 L | normal |
| Axis Bank | 853 | 96.72% | 96.25% | ₹11.89 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,786 | 96.05% | 96.21% | ₹94.37 L | normal |
| Google Pay | 4,734 | 96.37% | 96.09% | ₹64.83 L | normal |
| Paytm | 1,170 | 97.52% | 96.17% | ₹19.39 L | normal |
| Navi | 538 | 95.72% | 96.37% | ₹6.83 L | normal |
| SuperMoney | 281 | 98.22% | 96.26% | ₹3.46 L | normal |
| BHIM | 141 | 97.16% | 95.85% | ₹2.32 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,311 | 96.66% | ₹55.66 L |
| Food & Beverage | 2,492 | 97.27% | ₹12.88 L |
| Mobility | 1,263 | 97.70% | ₹5.79 L |
| Bills | 886 | 96.05% | ₹8.46 L |
| Healthcare | 581 | 97.25% | ₹11.57 L |
| Digital | 222 | 95.05% | ₹1.05 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,254 | 29.7% | 96.22% | ₹59.45 L |
| North | 3,612 | 25.2% | 96.04% | ₹42.31 L |
| West | 3,507 | 24.5% | 96.41% | ₹55.94 L |
| East | 1,692 | 11.8% | 96.81% | ₹29.59 L |
| Central | 1,268 | 8.8% | 96.53% | ₹13.11 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 34 | 97.06% | ₹4.45 L |
| Rapid Bazaar | Key Account | Retail | 452 | 97.12% | ₹2.20 L |
| Hampi Styles | Key Account | Retail | 48 | 97.92% | ₹1.13 L |
| Vasant Wardrobe | Key Account | Retail | 73 | 94.52% | ₹1.04 L |
| Tejas Restaurant | Large | Food & Beverage | 22 | 100.00% | ₹1.03 L |
| Hampi Stores 2298 | Key Account | Retail | 109 | 93.58% | ₹1.01 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 66 | 95.45% | ₹99,394 |
| Girnar Connect | Key Account | Bills | 172 | 97.67% | ₹98,463 |

## Failure analysis

Of 511 declined attempts, 381 were business declines (2.658% of attempts — balances, PINs and limits), 77 technical (0.537%), 38 timeouts (0.265%) and 15 risk declines (0.105%).

174 attempts were re-presentations of an earlier failure (1.21% of the day); 66.1% of them succeeded.

- Decline code U28 (Remitter bank unavailable) fired 26 times — 0.181% of attempts against a trailing 0.111%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 159 | 1.109% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 0.963% | 0.995% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.300% | 0.324% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.216% | 0.172% |
| U28 | Remitter bank unavailable | technical | Issuer | 26 | 0.181% | 0.111% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.147% | 0.185% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.126% | 0.131% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.119% | 0.084% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 106 | 112 |
| Auto-reversals | 23 | 23 |
| Disputes / chargebacks | 20 | 15 |
| Value returned | ₹1.41 L | ₹1.97 L |

## Customer behaviour

11,919 distinct customers transacted (−8.7% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,679 | 4,187 | 1.14 | 95.89% | ₹1,376 |
| power | 2,629 | 3,487 | 1.33 | 96.33% | ₹2,261 |
| merchant_heavy | 2,823 | 3,415 | 1.21 | 96.63% | ₹1,052 |
| small_ticket | 1,713 | 2,113 | 1.23 | 96.92% | ₹527 |
| occasional | 874 | 915 | 1.05 | 95.96% | ₹1,640 |
| new | 176 | 189 | 1.07 | 94.71% | ₹880 |
| dormant_returning | 25 | 27 | 1.08 | 96.30% | ₹708 |

## Operational events

- **INC-BANK-0012** (Sev-3) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 23:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Decline code U28 (Remitter bank unavailable) fired 26 times — 0.181% of attempts against a trailing 0.111%. Owner: Issuer.
- Issuer Yes Bank ran at 93.60% success on 531 attempts (3.7% of the day), 2.61pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 37% across the trailing window to 579 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

20 July ran on trend at 96.32% success and ₹2.00 Cr settled. The movement worth carrying forward is in the product mix: product Credit on UPI is compounding — attempts up 37% across the trailing window to 579 today, with success holding, so the growth is healthy and worth funding. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-20` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,333, successes=13,805, failed=511, pending=17, settled_value_inr=20,039,736.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=Credit on UPI; attempts=579; window_growth_pct=37.4; success_rate=95.34
- failures: failure_code=U28; count=26; rate_pct=0.18; trailing_rate_pct=0.11; owner=Issuer; z=2.77
- banks: payer_bank=Yes Bank; attempts=531; success_rate=93.6; own_median=96.21; z=-3.86
- incidents: event_id=INC-BANK-0012; kind=bank_outage; severity=Sev-3; window=2026-07-20 to 2026-07-23; success_impact_pp=-4.37; volume_impact_pct=-3.88

Refs: enterprise_data/warehouse/transactions, RPT-D196-DAILY, enterprise_data/warehouse/reference/incidents.parquet
