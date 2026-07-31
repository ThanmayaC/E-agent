---
id: RPT-D182-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 05 Jul 2026)

**Report ID:** RPT-D182-DAILY · **Day 182 of 206** · **Derived from:** 16,140 transaction rows queried live from the warehouse

## Summary

The rail took **16,140 payment attempts** on Sunday 05 July 2026 (Weekend) and settled **₹1.66 Cr** across 15,460 successful payments. Volume was −18.6% on yesterday and +14.9% on the same weekday last week. Success closed at **95.79%**, below the trailing 28-day median of 96.19%.

Retries reached 474 attempts (2.94% of the day, 10.5 sigma above normal). 72.4% of re-presented payments recovered, so the retry path was doing its job. 88 auto-reversals were raised, 12.3 sigma above the trailing median of 24.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,140 | −18.6% | +14.9% | 18,013 |
| Successful payments | 15,460 | −16.0% | +14.5% | 17,225 |
| Success rate | 95.79% | +2.94pp | −0.31pp | 95.69% |
| Settled value | ₹1.66 Cr | −29.5% | +5.0% | ₹2.24 Cr |
| Average ticket | ₹1,071 | −16.1% | −8.3% | ₹1,293 |
| Technical declines | 0.421% | −0.94pp | +0.03pp | 0.564% |
| Business declines | 3.048% | +0.35pp | −0.01pp | 2.726% |
| Risk declines | 0.118% | −0.02pp | −0.02pp | 0.112% |
| Timeout declines | 0.539% | −2.31pp | +0.31pp | 0.828% |
| Retry share | 2.94% | −0.43pp | +1.76pp | 1.91% |
| Latency p95 | 1,227 ms | −33.5% | −0.6% | 1,357 ms |
| Active customers | 13,144 | −14.0% | +12.7% | 14,340 |
| Active merchants | 1,609 | −4.7% | +5.2% | 1,658 |

## What moved

- Category Bills carried 1,709 attempts, 101% up its trailing median and 14.5% of the day's volume.
- Region North ran at 95.39% success on 4,166 attempts (25.8% of the day), 0.86pp down its own 28-day median.
- App Google Pay ran at 95.52% success on 5,357 attempts (33.2% of the day), 0.75pp down its own 28-day median.
- Product UPI Person to Person ran at 94.33% success on 4,320 attempts (26.8% of the day), 0.85pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 41% across the trailing window to 3,197 today, with success holding, so the growth is healthy and worth funding.
- Category Mobility ran at 96.32% success on 1,630 attempts (13.8% of the day), 1.17pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,320 | 26.8% | 94.33% | ₹44.92 L | +3.4% |
| UPI Person to Merchant | 3,462 | 21.4% | 95.98% | ₹32.95 L | −0.2% |
| UPI Lite | 3,197 | 19.8% | 98.56% | ₹2.86 L | +43.6% |
| UPI QR Payments | 2,915 | 18.1% | 95.78% | ₹12.14 L | +18.5% |
| UPI Circle | 958 | 5.9% | 96.03% | ₹9.29 L | +25.8% |
| UPI AutoPay | 394 | 2.4% | 89.09% | ₹6.74 L | +5.6% |
| RuPay Credit on UPI | 236 | 1.5% | 95.34% | ₹14.11 L | −35.9% |
| Credit on UPI | 212 | 1.3% | 95.75% | ₹17.05 L | −55.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,147 | 95.96% | 96.16% | ₹52.26 L | normal |
| HDFC Bank | 1,725 | 96.35% | 96.39% | ₹17.24 L | normal |
| Bank of Baroda | 1,211 | 96.28% | 96.21% | ₹17.25 L | normal |
| Union Bank of India | 1,113 | 96.23% | 95.90% | ₹9.29 L | normal |
| Punjab National Bank | 998 | 95.09% | 95.91% | ₹10.11 L | normal |
| Axis Bank | 987 | 94.33% | 96.12% | ₹11.96 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,579 | 96.19% | 96.08% | ₹74.78 L | normal |
| Google Pay | 5,357 | 95.52% | 96.27% | ₹55.04 L | ⚠ outlier |
| Paytm | 1,290 | 95.19% | 96.03% | ₹12.20 L | normal |
| Navi | 581 | 96.39% | 96.24% | ₹6.63 L | normal |
| SuperMoney | 293 | 94.20% | 95.64% | ₹1.97 L | normal |
| BHIM | 170 | 93.53% | 95.91% | ₹1.71 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,225 | 96.43% | ₹37.16 L |
| Food & Beverage | 2,953 | 97.02% | ₹11.87 L |
| Bills | 1,709 | 96.61% | ₹15.18 L |
| Mobility | 1,630 | 96.32% | ₹7.38 L |
| Healthcare | 538 | 97.77% | ₹5.10 L |
| Digital | 309 | 92.88% | ₹1.81 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,679 | 29.0% | 95.92% | ₹52.00 L |
| North | 4,166 | 25.8% | 95.39% | ₹41.07 L |
| West | 4,059 | 25.1% | 95.79% | ₹43.14 L |
| East | 1,878 | 11.6% | 95.90% | ₹18.14 L |
| Central | 1,358 | 8.4% | 96.39% | ₹11.18 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 29 | 96.55% | ₹1.92 L |
| Rapid Bazaar | Key Account | Retail | 445 | 97.30% | ₹1.50 L |
| Ujjwal Water Board | Key Account | Bills | 63 | 96.83% | ₹1.21 L |
| Girnar Connect | Key Account | Bills | 276 | 96.74% | ₹1.17 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 93.44% | ₹1.16 L |
| Hampi Styles | Key Account | Retail | 24 | 95.83% | ₹96,927 |
| Yamuna Restaurant | Key Account | Food & Beverage | 57 | 98.25% | ₹83,871 |
| Hampi Stores 2298 | Key Account | Retail | 104 | 96.15% | ₹71,860 |

## Failure analysis

Of 666 declined attempts, 492 were business declines (3.048% of attempts — balances, PINs and limits), 68 technical (0.421%), 87 timeouts (0.539%) and 19 risk declines (0.118%).

474 attempts were re-presentations of an earlier failure (2.94% of the day); 72.4% of them succeeded.

- Retries reached 474 attempts (2.94% of the day, 10.5 sigma above normal). 72.4% of re-presented payments recovered, so the retry path was doing its job.
- Decline code U54 (Transaction timed out at beneficiary) fired 45 times — 0.279% of attempts against a trailing 0.133%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 31 times — 0.192% of attempts against a trailing 0.096%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 200 | 1.239% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 182 | 1.128% | 0.963% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.335% | 0.325% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 45 | 0.279% | 0.133% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.211% | 0.199% |
| U30 | Debit failed at remitter bank | technical | Issuer | 34 | 0.211% | 0.177% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 31 | 0.192% | 0.096% |
| U28 | Remitter bank unavailable | technical | Issuer | 16 | 0.099% | 0.122% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 104 | 110 |
| Auto-reversals | 88 | 24 |
| Disputes / chargebacks | 13 | 14 |
| Value returned | ₹2.79 L | ₹1.71 L |

## Customer behaviour

13,144 distinct customers transacted (+9.4% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,091 | 4,694 | 1.15 | 96.46% | ₹1,028 |
| power | 2,795 | 3,880 | 1.39 | 95.67% | ₹1,592 |
| merchant_heavy | 3,048 | 3,760 | 1.23 | 95.96% | ₹809 |
| small_ticket | 1,962 | 2,464 | 1.26 | 94.76% | ₹413 |
| occasional | 1,007 | 1,083 | 1.08 | 95.11% | ₹1,197 |
| new | 210 | 228 | 1.09 | 95.18% | ₹718 |
| dormant_returning | 31 | 31 | 1.00 | 96.77% | ₹956 |

## Operational events

- **INC-NET-0040** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 20:00 and 24:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **CMP-0052** (Sev-3) — Hospitals cashback campaign, scoped to 8062. A cashback campaign across Hospitals merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 88 auto-reversals were raised, 12.3 sigma above the trailing median of 24.
- Decline code U54 (Transaction timed out at beneficiary) fired 45 times — 0.279% of attempts against a trailing 0.133%. Owner: Issuer.
- Region North ran at 95.39% success on 4,166 attempts (25.8% of the day), 0.86pp down its own 28-day median.
- App Google Pay ran at 95.52% success on 5,357 attempts (33.2% of the day), 0.75pp down its own 28-day median.
- Product UPI Person to Person ran at 94.33% success on 4,320 attempts (26.8% of the day), 0.85pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 41% across the trailing window to 3,197 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

05 July was an incident day: INC-NET-0040 was live and the rail closed at 95.79% success against a 96.19% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,140, successes=15,460, failed=666, pending=14, settled_value_inr=16,552,131.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=474; retry_share_pct=2.94; recovery_pct=72.36; z=10.48
- adjustments: reversals=88; trailing_median=24; z=12.33
- incidents: event_id=INC-NET-0040; kind=network_latency; severity=Sev-1; window=2026-07-04 to 2026-07-06; success_impact_pp=-14.23; volume_impact_pct=-13.13
- categories: mcc_category=Bills; attempts=1,709; own_median=852; z=8.14
- failures: failure_code=U54; count=45; rate_pct=0.28; trailing_rate_pct=0.13; owner=Issuer; z=4.04
- geography: region=North; attempts=4,166; success_rate=95.39; own_median=96.25; z=-2.44
- psps: payer_psp=Google Pay; attempts=5,357; success_rate=95.52; own_median=96.27; z=-2.15
- products: product_name=UPI Person to Person; attempts=4,320; success_rate=94.33; own_median=95.17; z=-2.27
- products: product_name=UPI Lite; attempts=3,197; window_growth_pct=41.2; success_rate=98.56
- categories: mcc_category=Mobility; attempts=1,630; success_rate=96.32; own_median=97.48; z=-2.51

Refs: enterprise_data/warehouse/transactions, RPT-D181-DAILY, enterprise_data/warehouse/reference/incidents.parquet
