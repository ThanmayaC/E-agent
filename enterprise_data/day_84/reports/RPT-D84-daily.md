---
id: RPT-D84-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-29T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 29 Mar 2026)

**Report ID:** RPT-D84-DAILY · **Day 84 of 206** · **Derived from:** 10,816 transaction rows queried live from the warehouse

## Summary

The rail took **10,816 payment attempts** on Sunday 29 March 2026 (Financial Year End (build-up)) and settled **₹1.19 Cr** across 10,298 successful payments. Volume was −14.6% on yesterday and −4.4% on the same weekday last week. Success closed at **95.21%**, below the trailing 28-day median of 95.83%.

Decline code ZA (Transaction declined by customer) fired 60 times — 0.555% of attempts against a trailing 0.384%. Owner: Customer. Success rate closed at 95.21%, 0.62pp down the trailing median — a 2.7-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,816 | −14.6% | −4.4% | 12,383 |
| Successful payments | 10,298 | −15.4% | −5.1% | 11,838 |
| Success rate | 95.21% | −0.89pp | −0.73pp | 95.54% |
| Settled value | ₹1.19 Cr | −15.2% | +11.9% | ₹1.40 Cr |
| Average ticket | ₹1,159 | +0.2% | +17.9% | ₹1,190 |
| Technical declines | 0.425% | +0.01pp | +0.05pp | 0.477% |
| Business declines | 3.846% | +0.84pp | +0.52pp | 3.322% |
| Risk declines | 0.148% | +0.07pp | +0.09pp | 0.123% |
| Timeout declines | 0.203% | −0.05pp | +0.00pp | 0.433% |
| Retry share | 1.26% | +0.29pp | +0.23pp | 1.43% |
| Latency p95 | 1,212 ms | −3.0% | −0.3% | 1,284 ms |
| Active customers | 9,240 | −12.3% | −3.4% | 10,269 |
| Active merchants | 1,313 | −2.3% | +3.1% | 1,319 |

## What moved

- Success rate closed at 95.21%, 0.62pp down the trailing median — a 2.7-sigma move.
- App PhonePe ran at 94.97% success on 5,045 attempts (46.6% of the day), 0.99pp down its own 28-day median.
- Product UPI QR Payments ran at 95.59% success on 1,791 attempts (16.6% of the day), 1.04pp down its own 28-day median.
- Category Bills carried 971 attempts, 40% up its trailing median and 13.7% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,722 | 34.4% | 94.73% | ₹37.25 L | −15.8% |
| UPI Person to Merchant | 3,231 | 29.9% | 95.64% | ₹31.88 L | −7.0% |
| UPI QR Payments | 1,791 | 16.6% | 95.59% | ₹6.69 L | −17.2% |
| UPI Lite | 918 | 8.5% | 98.69% | ₹83,005 | −0.6% |
| UPI AutoPay | 320 | 3.0% | 86.56% | ₹4.98 L | +1.1% |
| UPI Circle | 239 | 2.2% | 96.23% | ₹2.02 L | +25.1% |
| RuPay Credit on UPI | 176 | 1.6% | 94.32% | ₹11.93 L | −22.0% |
| Recurring Payments | 108 | 1.0% | 87.96% | ₹5.33 L | +16.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,370 | 95.76% | 95.78% | ₹39.82 L | normal |
| HDFC Bank | 1,182 | 95.77% | 95.59% | ₹15.13 L | normal |
| Union Bank of India | 771 | 92.87% | 95.69% | ₹6.54 L | ⚠ outlier |
| Bank of Baroda | 752 | 96.01% | 95.73% | ₹9.66 L | normal |
| Punjab National Bank | 681 | 95.01% | 95.67% | ₹7.11 L | normal |
| ICICI Bank | 649 | 95.07% | 95.86% | ₹5.32 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,045 | 94.97% | 95.95% | ₹56.48 L | ⚠ outlier |
| Google Pay | 3,578 | 95.50% | 95.76% | ₹38.21 L | normal |
| Paytm | 897 | 95.09% | 95.81% | ₹10.73 L | normal |
| Navi | 427 | 95.32% | 95.68% | ₹4.24 L | normal |
| SuperMoney | 209 | 93.78% | 95.32% | ₹1.77 L | normal |
| BHIM | 113 | 94.69% | 95.72% | ₹1.22 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,904 | 95.52% | ₹27.99 L |
| Food & Beverage | 1,644 | 96.78% | ₹7.58 L |
| Bills | 971 | 95.37% | ₹10.43 L |
| Mobility | 695 | 95.97% | ₹3.38 L |
| Healthcare | 310 | 95.81% | ₹1.64 L |
| Digital | 236 | 92.37% | ₹1.35 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,237 | 29.9% | 95.06% | ₹34.88 L |
| North | 2,698 | 24.9% | 95.48% | ₹29.95 L |
| West | 2,621 | 24.2% | 94.93% | ₹31.97 L |
| East | 1,311 | 12.1% | 94.97% | ₹14.35 L |
| Central | 949 | 8.8% | 96.10% | ₹8.21 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 84.38% | ₹2.25 L |
| Vasant Wardrobe | Key Account | Retail | 63 | 92.06% | ₹1.71 L |
| Rapid Bazaar | Key Account | Retail | 316 | 95.89% | ₹96,610 |
| Hampi Stores 2298 | Key Account | Retail | 93 | 92.47% | ₹76,965 |
| Girnar Connect | Key Account | Bills | 159 | 94.34% | ₹64,711 |
| Ujjwal Water Board | Key Account | Bills | 44 | 93.18% | ₹64,521 |
| Urban Boutique | Key Account | Retail | 81 | 96.30% | ₹52,776 |
| Indus Retail | Large | Retail | 23 | 95.65% | ₹49,546 |

## Failure analysis

Of 500 declined attempts, 416 were business declines (3.846% of attempts — balances, PINs and limits), 46 technical (0.425%), 22 timeouts (0.203%) and 16 risk declines (0.148%).

136 attempts were re-presentations of an earlier failure (1.26% of the day); 58.8% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 60 times — 0.555% of attempts against a trailing 0.384%. Owner: Customer.
- Decline code XH (Account does not exist / frozen) fired 34 times — 0.314% of attempts against a trailing 0.221%. Owner: Issuer.
- Decline code U30 (Debit failed at remitter bank) fired 26 times — 0.240% of attempts against a trailing 0.172%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 166 | 1.535% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 142 | 1.313% | 1.082% |
| ZA | Transaction declined by customer | business | Customer | 60 | 0.555% | 0.384% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.314% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.240% | 0.172% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 13 | 0.120% | 0.104% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 11 | 0.102% | 0.101% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 9 | 0.083% | 0.154% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 65 | 78 |
| Auto-reversals | 15 | 24 |
| Disputes / chargebacks | 6 | 10 |
| Value returned | ₹61,819 | ₹1.31 L |

## Customer behaviour

9,240 distinct customers transacted (−8.5% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,795 | 3,139 | 1.12 | 95.13% | ₹1,240 |
| power | 2,027 | 2,601 | 1.28 | 94.81% | ₹1,439 |
| merchant_heavy | 2,067 | 2,409 | 1.17 | 95.39% | ₹914 |
| small_ticket | 1,432 | 1,695 | 1.18 | 95.93% | ₹467 |
| occasional | 729 | 767 | 1.05 | 95.05% | ₹1,485 |
| new | 169 | 184 | 1.09 | 94.02% | ₹835 |
| dormant_returning | 21 | 21 | 1.00 | 95.24% | ₹625 |

## Operational events

- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 60 times — 0.555% of attempts against a trailing 0.384%. Owner: Customer.
- Success rate closed at 95.21%, 0.62pp down the trailing median — a 2.7-sigma move.
- App PhonePe ran at 94.97% success on 5,045 attempts (46.6% of the day), 0.99pp down its own 28-day median.
- Decline code XH (Account does not exist / frozen) fired 34 times — 0.314% of attempts against a trailing 0.221%. Owner: Issuer.
- Product UPI QR Payments ran at 95.59% success on 1,791 attempts (16.6% of the day), 1.04pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 29 March: success came in 0.62pp below baseline at 95.21% on 10,816 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-29` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,816, successes=10,298, failed=500, pending=18, settled_value_inr=11,935,086.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZA; count=60; rate_pct=0.55; trailing_rate_pct=0.38; owner=Customer; z=3.39
- headline: success_rate=95.21; trailing_median=95.83; z=-2.67
- psps: payer_psp=PhonePe; attempts=5,045; success_rate=94.97; own_median=95.95; z=-2.9
- failures: failure_code=XH; count=34; rate_pct=0.31; trailing_rate_pct=0.22; owner=Issuer; z=2.36
- products: product_name=UPI QR Payments; attempts=1,791; success_rate=95.59; own_median=96.63; z=-2.66
- failures: failure_code=U30; count=26; rate_pct=0.24; trailing_rate_pct=0.17; owner=Issuer; z=2.07
- categories: mcc_category=Bills; attempts=971; own_median=694.5; z=3.11
- banks: payer_bank=Union Bank of India; attempts=771; success_rate=92.87; own_median=95.69; z=-2.56
- products: product_name=UPI AutoPay; attempts=320; success_rate=86.56; own_median=90.81; z=-2.64
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31

Refs: enterprise_data/warehouse/transactions, RPT-D83-DAILY, enterprise_data/warehouse/reference/incidents.parquet
