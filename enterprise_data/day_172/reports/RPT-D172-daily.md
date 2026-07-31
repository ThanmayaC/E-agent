---
id: RPT-D172-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 25 Jun 2026)

**Report ID:** RPT-D172-DAILY · **Day 172 of 206** · **Derived from:** 13,103 transaction rows queried live from the warehouse

## Summary

The rail took **13,103 payment attempts** on Thursday 25 June 2026 (Working day) and settled **₹1.70 Cr** across 12,539 successful payments. Volume was +1.8% on yesterday and −11.3% on the same weekday last week. Success closed at **95.70%**, below the trailing 28-day median of 96.28%.

Decline code Z9 (Insufficient funds) fired 192 times — 1.465% of attempts against a trailing 1.203%. Owner: Customer. Retries reached 201 attempts (1.53% of the day, 3.0 sigma above normal). 66.2% of re-presented payments recovered, so the retry path was doing its job.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,103 | +1.8% | −11.3% | 14,825 |
| Successful payments | 12,539 | +2.1% | −11.8% | 14,270 |
| Success rate | 95.70% | +0.28pp | −0.55pp | 96.23% |
| Settled value | ₹1.70 Cr | +4.6% | −22.4% | ₹1.94 Cr |
| Average ticket | ₹1,353 | +2.5% | −12.1% | ₹1,360 |
| Technical declines | 0.504% | +0.05pp | +0.02pp | 0.422% |
| Business declines | 3.335% | −0.28pp | +0.67pp | 2.860% |
| Risk declines | 0.130% | +0.05pp | −0.02pp | 0.123% |
| Timeout declines | 0.206% | −0.13pp | −0.14pp | 0.269% |
| Retry share | 1.53% | +0.26pp | +0.50pp | 1.09% |
| Latency p95 | 1,322 ms | −1.2% | +1.6% | 1,278 ms |
| Active customers | 10,997 | +1.8% | −10.1% | 12,188 |
| Active merchants | 1,520 | +1.1% | −5.0% | 1,543 |

## What moved

- Success rate closed at 95.70%, 0.58pp down the trailing median — a 2.2-sigma move.
- Region North ran at 95.19% success on 3,327 attempts (25.4% of the day), 1.09pp down its own 28-day median.
- Issuer Bank of Baroda ran at 94.85% success on 932 attempts (7.1% of the day), 1.61pp down its own 28-day median.
- Category Bills ran at 93.94% success on 775 attempts (8.3% of the day), 2.23pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,734 | 28.5% | 95.29% | ₹38.39 L | −10.6% |
| UPI Person to Merchant | 2,787 | 21.3% | 95.73% | ₹22.82 L | −21.6% |
| UPI Lite | 2,114 | 16.1% | 98.96% | ₹1.80 L | +2.4% |
| UPI QR Payments | 1,978 | 15.1% | 96.61% | ₹8.34 L | −15.8% |
| UPI Circle | 698 | 5.3% | 96.56% | ₹5.74 L | −1.6% |
| Credit on UPI | 499 | 3.8% | 93.79% | ₹31.17 L | +10.9% |
| RuPay Credit on UPI | 418 | 3.2% | 95.69% | ₹16.42 L | +12.8% |
| UPI AutoPay | 385 | 2.9% | 85.71% | ₹6.54 L | +8.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,137 | 95.77% | 96.28% | ₹51.58 L | normal |
| HDFC Bank | 1,417 | 96.75% | 96.43% | ₹18.55 L | normal |
| Bank of Baroda | 932 | 94.85% | 96.46% | ₹12.73 L | ⚠ outlier |
| Union Bank of India | 877 | 95.67% | 96.24% | ₹11.40 L | normal |
| Axis Bank | 805 | 95.28% | 96.23% | ₹10.77 L | normal |
| Punjab National Bank | 795 | 95.97% | 96.27% | ₹9.32 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,137 | 95.68% | 96.13% | ₹77.56 L | normal |
| Google Pay | 4,414 | 95.79% | 96.36% | ₹54.62 L | normal |
| Paytm | 1,059 | 95.94% | 96.28% | ₹15.97 L | normal |
| Navi | 490 | 95.51% | 96.61% | ₹10.01 L | normal |
| SuperMoney | 237 | 94.51% | 95.97% | ₹1.71 L | normal |
| BHIM | 134 | 95.52% | 95.86% | ₹2.25 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,822 | 96.23% | ₹48.63 L |
| Food & Beverage | 2,376 | 97.18% | ₹12.76 L |
| Mobility | 1,225 | 97.47% | ₹6.02 L |
| Bills | 775 | 93.94% | ₹6.57 L |
| Healthcare | 477 | 95.60% | ₹7.33 L |
| Digital | 199 | 90.45% | ₹78,007 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,795 | 29.0% | 95.99% | ₹55.45 L |
| North | 3,327 | 25.4% | 95.19% | ₹39.59 L |
| West | 3,244 | 24.8% | 95.96% | ₹37.76 L |
| East | 1,513 | 11.5% | 95.51% | ₹22.20 L |
| Central | 1,224 | 9.3% | 95.67% | ₹14.65 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 29 | 89.66% | ₹1.96 L |
| Vasant Wardrobe | Key Account | Retail | 59 | 100.00% | ₹1.45 L |
| Rapid Bazaar | Key Account | Retail | 369 | 97.56% | ₹1.41 L |
| Kaveri Emporium | Large | Retail | 43 | 95.35% | ₹1.33 L |
| Hampi Styles | Key Account | Retail | 32 | 96.88% | ₹1.07 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 97.06% | ₹1.03 L |
| Girnar Connect | Key Account | Bills | 140 | 93.57% | ₹74,039 |
| Hampi Stores 2298 | Key Account | Retail | 92 | 95.65% | ₹61,966 |

## Failure analysis

Of 547 declined attempts, 437 were business declines (3.335% of attempts — balances, PINs and limits), 66 technical (0.504%), 27 timeouts (0.206%) and 17 risk declines (0.130%).

201 attempts were re-presentations of an earlier failure (1.53% of the day); 66.2% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 192 times — 1.465% of attempts against a trailing 1.203%. Owner: Customer.
- Retries reached 201 attempts (1.53% of the day, 3.0 sigma above normal). 66.2% of re-presented payments recovered, so the retry path was doing its job.
- Decline code UX (Mandate execution outside permitted window) fired 17 times — 0.130% of attempts against a trailing 0.059%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 192 | 1.465% | 1.203% |
| ZM | Invalid UPI PIN | business | Customer | 154 | 1.175% | 0.943% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.359% | 0.337% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.214% | 0.173% |
| XH | Account does not exist / frozen | business | Issuer | 18 | 0.137% | 0.200% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.130% | 0.112% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.130% | 0.143% |
| U69 | Beneficiary bank offline | technical | Issuer | 17 | 0.130% | 0.082% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 106 | 107 |
| Auto-reversals | 23 | 24 |
| Disputes / chargebacks | 13 | 13 |
| Value returned | ₹1.22 L | ₹1.70 L |

## Customer behaviour

10,997 distinct customers transacted (−9.1% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,396 | 3,850 | 1.13 | 95.74% | ₹1,374 |
| power | 2,437 | 3,241 | 1.33 | 95.43% | ₹1,621 |
| merchant_heavy | 2,540 | 3,000 | 1.18 | 95.87% | ₹1,183 |
| small_ticket | 1,583 | 1,913 | 1.21 | 95.97% | ₹635 |
| occasional | 815 | 848 | 1.04 | 95.52% | ₹1,665 |
| new | 193 | 216 | 1.12 | 94.91% | ₹1,062 |
| dormant_returning | 33 | 35 | 1.06 | 94.29% | ₹468 |

## Operational events

- **INC-BANK-0010** (Sev-2) — Kotak Mahindra Bank issuer decline spike, scoped to Kotak Mahindra Bank between 10:00 and 15:00. Kotak Mahindra Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 192 times — 1.465% of attempts against a trailing 1.203%. Owner: Customer.
- Success rate closed at 95.70%, 0.58pp down the trailing median — a 2.2-sigma move.
- Region North ran at 95.19% success on 3,327 attempts (25.4% of the day), 1.09pp down its own 28-day median.
- Decline code UX (Mandate execution outside permitted window) fired 17 times — 0.130% of attempts against a trailing 0.059%. Owner: PSP.
- Issuer Bank of Baroda ran at 94.85% success on 932 attempts (7.1% of the day), 1.61pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

25 June was an incident day: INC-BANK-0010 was live and the rail closed at 95.70% success against a 96.28% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,103, successes=12,539, failed=547, pending=17, settled_value_inr=16,965,599.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=192; rate_pct=1.47; trailing_rate_pct=1.2; owner=Customer; z=2.93
- failures: retries=201; retry_share_pct=1.53; recovery_pct=66.17; z=2.96
- headline: success_rate=95.7; trailing_median=96.28; z=-2.2
- incidents: event_id=INC-BANK-0010; kind=bank_outage; severity=Sev-2; window=2026-06-25 to 2026-06-27; success_impact_pp=-19.68; volume_impact_pct=-17.46
- geography: region=North; attempts=3,327; success_rate=95.19; own_median=96.28; z=-2.7
- failures: failure_code=UX; count=17; rate_pct=0.13; trailing_rate_pct=0.06; owner=PSP; z=3.25
- banks: payer_bank=Bank of Baroda; attempts=932; success_rate=94.85; own_median=96.45; z=-3.76
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- categories: mcc_category=Bills; attempts=775; success_rate=93.94; own_median=96.17; z=-2.71
- products: product_name=Credit on UPI; attempts=499; success_rate=93.79; own_median=96.18; z=-3.31

Refs: enterprise_data/warehouse/transactions, RPT-D171-DAILY, enterprise_data/warehouse/reference/incidents.parquet
