---
id: RPT-D204-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 27 Jul 2026)

**Report ID:** RPT-D204-DAILY · **Day 204 of 206** · **Derived from:** 14,783 transaction rows queried live from the warehouse

## Summary

The rail took **14,783 payment attempts** on Monday 27 July 2026 (Working day) and settled **₹1.95 Cr** across 14,224 successful payments. Volume was +6.9% on yesterday and +3.1% on the same weekday last week. Success closed at **96.22%**, in line with the trailing 28-day median of 96.17%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,783 | +6.9% | +3.1% | 15,731 |
| Successful payments | 14,224 | +7.4% | +3.0% | 15,118 |
| Success rate | 96.22% | +0.40pp | −0.10pp | 96.13% |
| Settled value | ₹1.95 Cr | +23.8% | −2.8% | ₹2.05 Cr |
| Average ticket | ₹1,370 | +15.3% | −5.6% | ₹1,359 |
| Technical declines | 0.386% | +0.02pp | −0.15pp | 0.446% |
| Business declines | 2.916% | −0.37pp | +0.26pp | 2.854% |
| Risk declines | 0.135% | +0.07pp | +0.03pp | 0.110% |
| Timeout declines | 0.264% | −0.10pp | −0.00pp | 0.370% |
| Retry share | 1.35% | −0.01pp | +0.14pp | 1.29% |
| Latency p95 | 1,284 ms | +3.5% | −1.9% | 1,293 ms |
| Active customers | 12,279 | +5.6% | +3.0% | 12,885 |
| Active merchants | 1,625 | +5.0% | +4.9% | 1,603 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 3,894 | 26.3% | 96.58% | ₹38.70 L | +3.0% |
| UPI Person to Person | 3,825 | 25.9% | 95.22% | ₹41.70 L | −16.0% |
| UPI QR Payments | 2,470 | 16.7% | 97.13% | ₹11.15 L | −5.1% |
| UPI Lite | 2,081 | 14.1% | 98.89% | ₹1.94 L | −11.5% |
| UPI Circle | 626 | 4.2% | 96.81% | ₹5.54 L | −23.3% |
| Credit on UPI | 591 | 4.0% | 95.94% | ₹44.99 L | +13.4% |
| UPI AutoPay | 409 | 2.8% | 85.82% | ₹6.72 L | +8.2% |
| RuPay Credit on UPI | 392 | 2.7% | 95.92% | ₹20.79 L | +4.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,692 | 96.23% | 96.31% | ₹61.44 L | normal |
| HDFC Bank | 1,574 | 97.14% | 96.40% | ₹26.61 L | normal |
| Bank of Baroda | 1,174 | 95.32% | 96.38% | ₹16.32 L | normal |
| Union Bank of India | 1,035 | 97.10% | 96.16% | ₹13.82 L | ⚠ outlier |
| Axis Bank | 918 | 96.19% | 96.34% | ₹12.88 L | normal |
| Punjab National Bank | 911 | 96.38% | 95.90% | ₹9.17 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,008 | 96.18% | 96.20% | ₹91.57 L | normal |
| Google Pay | 4,864 | 96.32% | 96.30% | ₹63.54 L | normal |
| Paytm | 1,205 | 96.18% | 96.25% | ₹16.77 L | normal |
| Navi | 541 | 94.82% | 96.64% | ₹8.43 L | normal |
| SuperMoney | 293 | 96.93% | 96.34% | ₹3.71 L | normal |
| BHIM | 159 | 96.86% | 95.29% | ₹1.76 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,350 | 97.01% | ₹56.77 L |
| Food & Beverage | 2,573 | 97.20% | ₹11.62 L |
| Bills | 1,414 | 96.04% | ₹13.07 L |
| Mobility | 1,266 | 97.08% | ₹7.88 L |
| Healthcare | 554 | 98.38% | ₹12.41 L |
| Digital | 304 | 93.09% | ₹1.61 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,336 | 29.3% | 96.03% | ₹64.92 L |
| West | 3,705 | 25.1% | 96.17% | ₹47.87 L |
| North | 3,685 | 24.9% | 96.12% | ₹45.22 L |
| East | 1,693 | 11.5% | 96.16% | ₹20.78 L |
| Central | 1,364 | 9.2% | 97.29% | ₹16.05 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 37 | 94.59% | ₹5.23 L |
| Vasant Wardrobe | Key Account | Retail | 84 | 95.24% | ₹2.27 L |
| Rapid Bazaar | Key Account | Retail | 407 | 98.53% | ₹1.63 L |
| Ujjwal Water Board | Key Account | Bills | 51 | 100.00% | ₹91,479 |
| Girnar Connect | Key Account | Bills | 235 | 94.89% | ₹83,486 |
| Yamuna Restaurant | Key Account | Food & Beverage | 82 | 95.12% | ₹82,211 |
| Aravalli Pharmacy | Large | Healthcare | 87 | 97.70% | ₹73,986 |
| Hampi Styles | Key Account | Retail | 37 | 100.00% | ₹69,910 |

## Failure analysis

Of 547 declined attempts, 431 were business declines (2.916% of attempts — balances, PINs and limits), 57 technical (0.386%), 39 timeouts (0.264%) and 20 risk declines (0.135%).

200 attempts were re-presentations of an earlier failure (1.35% of the day); 75.5% of them succeeded.

- Decline code XH (Account does not exist / frozen) fired 38 times — 0.257% of attempts against a trailing 0.188%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.272% | 1.191% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 0.920% | 0.959% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.298% | 0.325% |
| XH | Account does not exist / frozen | business | Issuer | 38 | 0.257% | 0.188% |
| U28 | Remitter bank unavailable | technical | Issuer | 22 | 0.149% | 0.115% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.122% | 0.171% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.115% | 0.135% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.115% | 0.092% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 100 | 114 |
| Auto-reversals | 23 | 23 |
| Disputes / chargebacks | 15 | 15 |
| Value returned | ₹1.58 L | ₹1.68 L |

## Customer behaviour

12,279 distinct customers transacted (−6.0% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,934 | 4,499 | 1.14 | 96.29% | ₹1,348 |
| power | 2,673 | 3,610 | 1.35 | 96.34% | ₹1,723 |
| merchant_heavy | 2,800 | 3,342 | 1.19 | 96.05% | ₹1,197 |
| small_ticket | 1,763 | 2,170 | 1.23 | 96.41% | ₹613 |
| occasional | 858 | 896 | 1.04 | 95.98% | ₹1,805 |
| new | 230 | 245 | 1.07 | 95.10% | ₹921 |
| dormant_returning | 21 | 21 | 1.00 | 90.48% | ₹1,230 |

## Operational events

- **INC-BANK-0019** (Sev-2) — Yes Bank issuer decline spike, scoped to Yes Bank between 17:00 and 20:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0064** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code XH (Account does not exist / frozen) fired 38 times — 0.257% of attempts against a trailing 0.188%. Owner: Issuer.
- Issuer Federal Bank ran at 94.00% success on 350 attempts (2.4% of the day), 2.13pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

27 July was an incident day: INC-BANK-0019 was live and the rail closed at 96.22% success against a 96.17% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,783, successes=14,224, failed=547, pending=12, settled_value_inr=19,484,928.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0019; kind=bank_outage; severity=Sev-2; window=2026-07-25 to 2026-07-27; success_impact_pp=-14.88; volume_impact_pct=-13.2
- failures: failure_code=XH; count=38; rate_pct=0.26; trailing_rate_pct=0.19; owner=Issuer; z=2.09
- categories: mcc_category=Bills; attempts=1,414; own_median=976; z=2.71
- banks: payer_bank=Union Bank of India; attempts=1,035; success_rate=97.1; own_median=96.16; z=2.46
- categories: mcc_category=Healthcare; attempts=554; success_rate=98.38; own_median=97.31; z=2.15
- incidents: event_id=CMP-0064; kind=merchant_campaign; severity=Sev-3; window=2026-07-22 to 2026-07-27; success_impact_pp=-0.11; volume_impact_pct=44.38
- banks: payer_bank=Federal Bank; attempts=350; success_rate=94; own_median=96.13; z=-2.24
- categories: mcc_category=Financial Services; attempts=201; own_median=179; z=2.97

Refs: enterprise_data/warehouse/transactions, RPT-D203-DAILY, enterprise_data/warehouse/reference/incidents.parquet
