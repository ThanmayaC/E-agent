---
id: RPT-D164-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 17 Jun 2026)

**Report ID:** RPT-D164-DAILY · **Day 164 of 206** · **Derived from:** 13,407 transaction rows queried live from the warehouse

## Summary

The rail took **13,407 payment attempts** on Wednesday 17 June 2026 (Working day) and settled **₹1.77 Cr** across 12,852 successful payments. Volume was −2.5% on yesterday and −3.1% on the same weekday last week. Success closed at **95.86%**, below the trailing 28-day median of 96.25%.

Decline code Z9 (Insufficient funds) fired 194 times — 1.447% of attempts against a trailing 1.215%. Owner: Customer. Category Retail ran at 95.99% success on 3,941 attempts (42.6% of the day), 0.88pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,407 | −2.5% | −3.1% | 14,837 |
| Successful payments | 12,852 | −2.7% | −3.6% | 14,296 |
| Success rate | 95.86% | −0.23pp | −0.50pp | 96.34% |
| Settled value | ₹1.77 Cr | +0.1% | −10.2% | ₹1.96 Cr |
| Average ticket | ₹1,380 | +2.9% | −6.8% | ₹1,373 |
| Technical declines | 0.507% | +0.21pp | +0.22pp | 0.393% |
| Business declines | 3.200% | +0.04pp | +0.32pp | 2.799% |
| Risk declines | 0.149% | +0.06pp | −0.02pp | 0.125% |
| Timeout declines | 0.179% | −0.10pp | −0.02pp | 0.258% |
| Retry share | 1.04% | −0.00pp | −0.09pp | 1.03% |
| Latency p95 | 1,314 ms | +1.2% | +3.7% | 1,273 ms |
| Active customers | 11,176 | −2.6% | −3.3% | 12,186 |
| Active merchants | 1,530 | +3.2% | +0.3% | 1,542 |

## What moved

- Category Retail ran at 95.99% success on 3,941 attempts (42.6% of the day), 0.88pp down its own 28-day median.
- Region West ran at 94.77% success on 3,248 attempts (24.2% of the day), 1.29pp down its own 28-day median.
- Issuer HDFC Bank ran at 95.17% success on 1,450 attempts (10.8% of the day), 1.24pp down its own 28-day median.
- Success rate closed at 95.86%, 0.39pp down the trailing median — a 1.5-sigma move.
- Product UPI QR Payments ran at 95.80% success on 2,071 attempts (15.4% of the day), 1.02pp down its own 28-day median.
- Issuer Axis Bank ran at 95.10% success on 877 attempts (6.5% of the day), 1.33pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,150 | 31.0% | 94.72% | ₹42.83 L | −4.5% |
| UPI Person to Merchant | 2,987 | 22.3% | 95.85% | ₹27.86 L | −16.8% |
| UPI QR Payments | 2,071 | 15.4% | 95.80% | ₹9.10 L | −11.9% |
| UPI Lite | 1,852 | 13.8% | 99.08% | ₹1.63 L | −4.7% |
| UPI Circle | 642 | 4.8% | 97.35% | ₹5.60 L | −5.9% |
| Credit on UPI | 483 | 3.6% | 96.27% | ₹38.89 L | +18.7% |
| UPI AutoPay | 381 | 2.8% | 91.34% | ₹7.17 L | +8.7% |
| RuPay Credit on UPI | 325 | 2.4% | 94.77% | ₹13.59 L | −12.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,134 | 95.74% | 96.26% | ₹50.35 L | normal |
| HDFC Bank | 1,450 | 95.17% | 96.41% | ₹19.23 L | ⚠ outlier |
| Bank of Baroda | 1,088 | 96.05% | 96.46% | ₹15.84 L | normal |
| Union Bank of India | 935 | 94.87% | 96.38% | ₹9.78 L | ⚠ outlier |
| Axis Bank | 877 | 95.10% | 96.43% | ₹11.36 L | ⚠ outlier |
| Punjab National Bank | 823 | 95.38% | 96.27% | ₹12.10 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,361 | 95.99% | 96.17% | ₹81.65 L | normal |
| Google Pay | 4,376 | 95.96% | 96.38% | ₹58.96 L | normal |
| Paytm | 1,103 | 96.01% | 95.98% | ₹15.09 L | normal |
| Navi | 495 | 96.16% | 96.19% | ₹6.59 L | normal |
| SuperMoney | 270 | 94.44% | 96.26% | ₹3.43 L | normal |
| BHIM | 129 | 91.47% | 95.50% | ₹1.32 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,941 | 95.99% | ₹45.95 L |
| Food & Beverage | 2,204 | 96.96% | ₹10.86 L |
| Mobility | 1,141 | 97.63% | ₹6.51 L |
| Bills | 817 | 96.45% | ₹7.14 L |
| Healthcare | 518 | 97.88% | ₹13.73 L |
| Digital | 206 | 94.66% | ₹1.16 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,959 | 29.5% | 96.06% | ₹53.21 L |
| North | 3,517 | 26.2% | 96.73% | ₹43.13 L |
| West | 3,248 | 24.2% | 94.77% | ₹47.09 L |
| East | 1,510 | 11.3% | 95.83% | ₹21.70 L |
| Central | 1,173 | 8.7% | 95.65% | ₹12.27 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 90.91% | ₹2.05 L |
| Rapid Bazaar | Key Account | Retail | 362 | 97.24% | ₹1.63 L |
| Vasant Wardrobe | Key Account | Retail | 60 | 81.67% | ₹1.52 L |
| Hampi Stores 2298 | Key Account | Retail | 128 | 98.44% | ₹88,131 |
| Yamuna Restaurant | Key Account | Food & Beverage | 59 | 94.92% | ₹83,165 |
| Kaveri Trading | Large | Retail | 58 | 94.83% | ₹67,490 |
| Hampi Styles | Key Account | Retail | 30 | 93.33% | ₹66,323 |
| Ujjwal Water Board | Key Account | Bills | 27 | 96.30% | ₹66,266 |

## Failure analysis

Of 541 declined attempts, 429 were business declines (3.200% of attempts — balances, PINs and limits), 68 technical (0.507%), 24 timeouts (0.179%) and 20 risk declines (0.149%).

140 attempts were re-presentations of an earlier failure (1.04% of the day); 62.1% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 194 times — 1.447% of attempts against a trailing 1.215%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 194 | 1.447% | 1.215% |
| ZM | Invalid UPI PIN | business | Customer | 127 | 0.947% | 0.933% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.380% | 0.361% |
| U30 | Debit failed at remitter bank | technical | Issuer | 34 | 0.254% | 0.172% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.239% | 0.209% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.134% | 0.108% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.112% | 0.112% |
| U69 | Beneficiary bank offline | technical | Issuer | 14 | 0.104% | 0.075% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 105 | 106 |
| Auto-reversals | 12 | 24 |
| Disputes / chargebacks | 14 | 13 |
| Value returned | ₹2.40 L | ₹1.70 L |

## Customer behaviour

11,176 distinct customers transacted (−7.2% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,421 | 3,853 | 1.13 | 95.56% | ₹1,678 |
| power | 2,476 | 3,294 | 1.33 | 95.48% | ₹1,667 |
| merchant_heavy | 2,569 | 3,077 | 1.20 | 96.17% | ₹941 |
| small_ticket | 1,672 | 2,077 | 1.24 | 96.39% | ₹578 |
| occasional | 828 | 870 | 1.05 | 96.32% | ₹1,619 |
| new | 189 | 214 | 1.13 | 96.26% | ₹1,182 |
| dormant_returning | 21 | 22 | 1.05 | 90.91% | ₹1,025 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 194 times — 1.447% of attempts against a trailing 1.215%. Owner: Customer.
- Category Retail ran at 95.99% success on 3,941 attempts (42.6% of the day), 0.88pp down its own 28-day median.
- Region West ran at 94.77% success on 3,248 attempts (24.2% of the day), 1.29pp down its own 28-day median.
- Issuer HDFC Bank ran at 95.17% success on 1,450 attempts (10.8% of the day), 1.24pp down its own 28-day median.
- Success rate closed at 95.86%, 0.39pp down the trailing median — a 1.5-sigma move.

### Opportunities

- Product UPI Lite is compounding — attempts up 27% across the trailing window to 1,852 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

17 June ran on trend at 95.86% success and ₹1.77 Cr settled. The movement worth carrying forward is in the decline profile: decline code Z9 (Insufficient funds) fired 194 times — 1.447% of attempts against a trailing 1.215%. Owner: Customer. 5 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,407, successes=12,852, failed=541, pending=14, settled_value_inr=17,740,407.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=194; rate_pct=1.45; trailing_rate_pct=1.22; owner=Customer; z=2.38
- categories: mcc_category=Retail; attempts=3,941; success_rate=95.99; own_median=96.87; z=-2.54
- geography: region=West; attempts=3,248; success_rate=94.77; own_median=96.05; z=-3.23
- banks: payer_bank=HDFC Bank; attempts=1,450; success_rate=95.17; own_median=96.41; z=-4.09
- headline: success_rate=95.86; trailing_median=96.25; z=-1.53
- products: product_name=UPI QR Payments; attempts=2,071; success_rate=95.8; own_median=96.81; z=-2.95
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- banks: payer_bank=Axis Bank; attempts=877; success_rate=95.1; own_median=96.43; z=-2.95
- products: product_name=UPI Lite; attempts=1,852; window_growth_pct=26.8; success_rate=99.08
- banks: payer_bank=Union Bank of India; attempts=935; success_rate=94.87; own_median=96.38; z=-2.65

Refs: enterprise_data/warehouse/transactions, RPT-D163-DAILY, enterprise_data/warehouse/reference/incidents.parquet
