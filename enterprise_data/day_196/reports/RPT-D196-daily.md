---
id: RPT-D196-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 19 Jul 2026)

**Report ID:** RPT-D196-DAILY · **Day 196 of 206** · **Derived from:** 13,849 transaction rows queried live from the warehouse

## Summary

The rail took **13,849 payment attempts** on Sunday 19 July 2026 (Weekend) and settled **₹1.50 Cr** across 13,283 successful payments. Volume was −16.4% on yesterday and −3.0% on the same weekday last week. Success closed at **95.91%**, in line with the trailing 28-day median of 96.13%.

Product UPI Person to Person ran at 94.33% success on 3,529 attempts (25.5% of the day), 0.86pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,849 | −16.4% | −3.0% | 16,266 |
| Successful payments | 13,283 | −16.9% | −3.1% | 15,634 |
| Success rate | 95.91% | −0.65pp | −0.01pp | 96.14% |
| Settled value | ₹1.50 Cr | −33.5% | −6.7% | ₹2.11 Cr |
| Average ticket | ₹1,127 | −19.9% | −3.8% | ₹1,346 |
| Technical declines | 0.383% | +0.05pp | −0.03pp | 0.450% |
| Business declines | 3.220% | +0.53pp | −0.02pp | 2.823% |
| Risk declines | 0.130% | +0.03pp | +0.03pp | 0.106% |
| Timeout declines | 0.274% | +0.08pp | +0.07pp | 0.393% |
| Retry share | 1.18% | +0.17pp | −0.23pp | 1.33% |
| Latency p95 | 1,247 ms | −1.4% | +0.2% | 1,300 ms |
| Active customers | 11,597 | −13.8% | −2.4% | 13,226 |
| Active merchants | 1,538 | −5.9% | +0.7% | 1,613 |

## What moved

- Product UPI Person to Person ran at 94.33% success on 3,529 attempts (25.5% of the day), 0.86pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 41% across the trailing window to 262 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 3,540 | 25.6% | 95.99% | ₹33.39 L | −3.1% |
| UPI Person to Person | 3,529 | 25.5% | 94.33% | ₹35.99 L | −22.1% |
| UPI QR Payments | 2,334 | 16.9% | 96.36% | ₹9.83 L | −8.6% |
| UPI Lite | 2,221 | 16.0% | 98.51% | ₹1.94 L | −13.0% |
| UPI Circle | 990 | 7.1% | 97.17% | ₹6.89 L | +22.6% |
| UPI AutoPay | 352 | 2.5% | 88.92% | ₹5.89 L | −6.9% |
| Credit on UPI | 262 | 1.9% | 96.18% | ₹22.47 L | −45.9% |
| RuPay Credit on UPI | 201 | 1.5% | 95.52% | ₹8.68 L | −47.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,345 | 96.29% | 96.19% | ₹50.44 L | normal |
| HDFC Bank | 1,504 | 95.94% | 96.39% | ₹13.09 L | normal |
| Bank of Baroda | 1,056 | 95.45% | 96.35% | ₹11.89 L | normal |
| Union Bank of India | 917 | 96.29% | 96.25% | ₹12.51 L | normal |
| Axis Bank | 888 | 95.83% | 96.25% | ₹7.85 L | normal |
| ICICI Bank | 867 | 95.96% | 96.34% | ₹10.46 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,467 | 95.52% | 96.21% | ₹73.59 L | normal |
| Google Pay | 4,673 | 96.02% | 96.09% | ₹43.62 L | normal |
| Paytm | 1,101 | 95.00% | 96.17% | ₹12.42 L | normal |
| Navi | 487 | 98.36% | 96.37% | ₹8.94 L | ⚠ outlier |
| SuperMoney | 263 | 97.72% | 96.22% | ₹3.50 L | normal |
| BHIM | 149 | 98.66% | 95.69% | ₹1.17 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,197 | 96.33% | ₹41.39 L |
| Food & Beverage | 2,757 | 96.99% | ₹10.44 L |
| Mobility | 1,286 | 97.51% | ₹5.90 L |
| Bills | 871 | 97.24% | ₹7.50 L |
| Healthcare | 570 | 97.37% | ₹7.96 L |
| Digital | 208 | 90.87% | ₹86,635 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,028 | 29.1% | 96.40% | ₹43.28 L |
| North | 3,532 | 25.5% | 95.53% | ₹41.77 L |
| West | 3,475 | 25.1% | 95.77% | ₹37.95 L |
| East | 1,581 | 11.4% | 95.89% | ₹16.78 L |
| Central | 1,233 | 8.9% | 95.86% | ₹9.96 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 70 | 97.14% | ₹2.23 L |
| Rapid Bazaar | Key Account | Retail | 425 | 96.47% | ₹1.57 L |
| Vega Electronics | Large | Retail | 29 | 89.66% | ₹1.37 L |
| Konark Boutique | Large | Retail | 36 | 100.00% | ₹72,289 |
| Girnar Connect | Key Account | Bills | 162 | 98.77% | ₹68,692 |
| Hampi Stores 2298 | Key Account | Retail | 97 | 95.88% | ₹67,078 |
| Aravalli Pharmacy | Large | Healthcare | 99 | 96.97% | ₹64,540 |
| Hampi Styles | Key Account | Retail | 33 | 100.00% | ₹62,963 |

## Failure analysis

Of 555 declined attempts, 446 were business declines (3.220% of attempts — balances, PINs and limits), 53 technical (0.383%), 38 timeouts (0.274%) and 18 risk declines (0.130%).

163 attempts were re-presentations of an earlier failure (1.18% of the day); 63.8% of them succeeded.

- Decline code XH (Account does not exist / frozen) fired 36 times — 0.260% of attempts against a trailing 0.185%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 184 | 1.329% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 154 | 1.112% | 0.995% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.325% | 0.325% |
| XH | Account does not exist / frozen | business | Issuer | 36 | 0.260% | 0.185% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.166% | 0.172% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.144% | 0.131% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.116% | 0.093% |
| UX | Mandate execution outside permitted window | business | PSP | 16 | 0.116% | 0.086% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 107 | 112 |
| Auto-reversals | 19 | 23 |
| Disputes / chargebacks | 15 | 15 |
| Value returned | ₹1.38 L | ₹1.97 L |

## Customer behaviour

11,597 distinct customers transacted (−11.2% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,649 | 4,160 | 1.14 | 95.79% | ₹1,150 |
| power | 2,523 | 3,357 | 1.33 | 95.65% | ₹1,586 |
| merchant_heavy | 2,629 | 3,115 | 1.18 | 96.28% | ₹822 |
| small_ticket | 1,708 | 2,065 | 1.21 | 96.13% | ₹481 |
| occasional | 873 | 921 | 1.05 | 95.98% | ₹1,202 |
| new | 183 | 199 | 1.09 | 95.48% | ₹921 |
| dormant_returning | 32 | 32 | 1.00 | 90.62% | ₹566 |

## Operational events

- **INC-BANK-0020** (Sev-2) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 24:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Product UPI Person to Person ran at 94.33% success on 3,529 attempts (25.5% of the day), 0.86pp down its own 28-day median.
- Decline code XH (Account does not exist / frozen) fired 36 times — 0.260% of attempts against a trailing 0.185%. Owner: Issuer.
- Issuer Yes Bank ran at 94.11% success on 543 attempts (3.9% of the day), 2.10pp down its own 28-day median.
- Issuer IndusInd Bank ran at 93.40% success on 288 attempts (2.1% of the day), 2.39pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 41% across the trailing window to 262 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

19 July was an incident day: INC-BANK-0020 was live and the rail closed at 95.91% success against a 96.13% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,849, successes=13,283, failed=555, pending=11, settled_value_inr=14,974,027.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0020; kind=bank_outage; severity=Sev-2; window=2026-07-17 to 2026-07-19; success_impact_pp=-11.07; volume_impact_pct=-9.82
- products: product_name=UPI Person to Person; attempts=3,529; success_rate=94.33; own_median=95.19; z=-3.16
- products: product_name=Credit on UPI; attempts=262; window_growth_pct=40.9; success_rate=96.18
- failures: failure_code=XH; count=36; rate_pct=0.26; trailing_rate_pct=0.18; owner=Issuer; z=2.38
- banks: payer_bank=Yes Bank; attempts=543; success_rate=94.11; own_median=96.21; z=-3.1
- products: product_name=UPI Circle; attempts=990; own_median=807.5; z=2.22
- psps: payer_psp=Navi; attempts=487; success_rate=98.36; own_median=96.38; z=2.16
- banks: payer_bank=IndusInd Bank; attempts=288; success_rate=93.4; own_median=95.79; z=-2.75
- products: product_name=RuPay Credit on UPI; attempts=201; own_median=383.5; z=-3.33

Refs: enterprise_data/warehouse/transactions, RPT-D195-DAILY, enterprise_data/warehouse/reference/incidents.parquet
