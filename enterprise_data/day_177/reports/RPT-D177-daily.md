---
id: RPT-D177-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-30T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 30 Jun 2026)

**Report ID:** RPT-D177-DAILY · **Day 177 of 206** · **Derived from:** 17,361 transaction rows queried live from the warehouse

## Summary

The rail took **17,361 payment attempts** on Tuesday 30 June 2026 (Quarter Close Q1FY27) and settled **₹2.58 Cr** across 16,656 successful payments. Volume was +1.0% on yesterday and +24.0% on the same weekday last week. Success closed at **95.94%**, below the trailing 28-day median of 96.24%.

Retries reached 246 attempts (1.42% of the day, 2.7 sigma above normal). Only 47.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them. Category Bills carried 1,597 attempts, 87% up its trailing median and 12.6% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 17,361 | +1.0% | +24.0% | 14,973 |
| Successful payments | 16,656 | +0.3% | +23.9% | 14,410 |
| Success rate | 95.94% | −0.61pp | −0.12pp | 96.22% |
| Settled value | ₹2.58 Cr | +9.3% | +50.2% | ₹1.95 Cr |
| Average ticket | ₹1,549 | +9.0% | +21.2% | ₹1,350 |
| Technical declines | 0.449% | +0.05pp | −0.09pp | 0.422% |
| Business declines | 3.041% | +0.38pp | +0.07pp | 2.880% |
| Risk declines | 0.098% | +0.02pp | +0.01pp | 0.123% |
| Timeout declines | 0.374% | +0.12pp | +0.11pp | 0.268% |
| Retry share | 1.42% | +0.40pp | +0.29pp | 1.10% |
| Latency p95 | 1,367 ms | +7.4% | +8.8% | 1,279 ms |
| Active customers | 13,958 | +0.6% | +20.1% | 12,296 |
| Active merchants | 1,645 | +1.1% | +8.6% | 1,550 |

## What moved

- Category Bills carried 1,597 attempts, 87% up its trailing median and 12.6% of the day's volume.
- App Google Pay ran at 95.60% success on 5,746 attempts (33.1% of the day), 0.74pp down its own 28-day median.
- Attempt volume ran 2.5 standard deviations up its trailing 28-day median at 17,361, 24.0% up on the same weekday last week.
- Region North carried 4,378 attempts, 21% up its trailing median and 25.2% of the day's volume.
- Category Food & Beverage carried 3,024 attempts, 21% up its trailing median and 23.9% of the day's volume.
- Product UPI Lite carried 2,813 attempts, 32% up its trailing median and 16.2% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,687 | 27.0% | 94.79% | ₹48.65 L | +12.2% |
| UPI Person to Merchant | 3,790 | 21.8% | 95.80% | ₹37.96 L | +9.3% |
| UPI Lite | 2,813 | 16.2% | 98.97% | ₹2.54 L | +31.6% |
| UPI QR Payments | 2,675 | 15.4% | 97.20% | ₹12.42 L | +15.7% |
| UPI Circle | 842 | 4.8% | 96.91% | ₹6.86 L | +17.3% |
| Credit on UPI | 829 | 4.8% | 95.54% | ₹68.84 L | +83.4% |
| RuPay Credit on UPI | 646 | 3.7% | 95.51% | ₹28.66 L | +75.5% |
| UPI AutoPay | 414 | 2.4% | 85.99% | ₹7.02 L | +13.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,400 | 96.17% | 96.30% | ₹85.03 L | normal |
| HDFC Bank | 1,954 | 96.37% | 96.43% | ₹26.45 L | normal |
| Bank of Baroda | 1,370 | 97.08% | 96.22% | ₹22.31 L | normal |
| Union Bank of India | 1,158 | 94.91% | 96.11% | ₹16.11 L | normal |
| Axis Bank | 1,080 | 96.02% | 96.18% | ₹13.56 L | normal |
| ICICI Bank | 1,056 | 94.70% | 96.46% | ₹12.96 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,163 | 96.21% | 96.11% | ₹1.21 Cr | normal |
| Google Pay | 5,746 | 95.60% | 96.34% | ₹84.46 L | ⚠ outlier |
| Paytm | 1,434 | 94.77% | 96.12% | ₹23.48 L | normal |
| Navi | 652 | 96.78% | 96.44% | ₹10.09 L | normal |
| SuperMoney | 343 | 96.21% | 95.97% | ₹5.14 L | normal |
| BHIM | 165 | 96.97% | 95.85% | ₹5.78 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,879 | 96.80% | ₹69.24 L |
| Food & Beverage | 3,024 | 97.12% | ₹15.94 L |
| Bills | 1,597 | 95.55% | ₹14.63 L |
| Mobility | 1,558 | 97.24% | ₹9.40 L |
| Healthcare | 703 | 97.87% | ₹12.46 L |
| Digital | 286 | 91.26% | ₹1.75 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,127 | 29.5% | 95.94% | ₹68.09 L |
| North | 4,378 | 25.2% | 96.28% | ₹68.19 L |
| West | 4,322 | 24.9% | 95.67% | ₹76.16 L |
| East | 2,024 | 11.7% | 95.31% | ₹26.92 L |
| Central | 1,510 | 8.7% | 96.56% | ₹18.67 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 100.00% | ₹3.04 L |
| Vasant Wardrobe | Key Account | Retail | 101 | 97.03% | ₹3.04 L |
| Rapid Bazaar | Key Account | Retail | 470 | 97.02% | ₹2.76 L |
| Hampi Styles | Key Account | Retail | 45 | 100.00% | ₹1.51 L |
| Hampi Stores 2298 | Key Account | Retail | 143 | 99.30% | ₹1.50 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 111 | 97.30% | ₹1.47 L |
| Ujjwal Water Board | Key Account | Bills | 67 | 92.54% | ₹1.36 L |
| Girnar Connect | Key Account | Bills | 272 | 96.69% | ₹1.33 L |

## Failure analysis

Of 688 declined attempts, 528 were business declines (3.041% of attempts — balances, PINs and limits), 78 technical (0.449%), 65 timeouts (0.374%) and 17 risk declines (0.098%).

246 attempts were re-presentations of an earlier failure (1.42% of the day); 47.6% of them succeeded.

- Retries reached 246 attempts (1.42% of the day, 2.7 sigma above normal). Only 47.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 217 | 1.250% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 185 | 1.066% | 0.942% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.323% | 0.328% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 32 | 0.184% | 0.137% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.184% | 0.200% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.179% | 0.176% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 25 | 0.144% | 0.090% |
| U28 | Remitter bank unavailable | technical | Issuer | 23 | 0.132% | 0.112% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 125 | 108 |
| Auto-reversals | 24 | 22 |
| Disputes / chargebacks | 16 | 14 |
| Value returned | ₹1.63 L | ₹1.70 L |

## Customer behaviour

13,958 distinct customers transacted (+16.9% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,388 | 5,114 | 1.17 | 95.80% | ₹1,779 |
| power | 2,934 | 4,200 | 1.43 | 95.86% | ₹2,028 |
| merchant_heavy | 3,251 | 4,029 | 1.24 | 96.08% | ₹1,062 |
| small_ticket | 2,040 | 2,596 | 1.27 | 96.46% | ₹722 |
| occasional | 1,056 | 1,112 | 1.05 | 94.96% | ₹1,551 |
| new | 253 | 272 | 1.08 | 96.32% | ₹919 |
| dormant_returning | 36 | 38 | 1.06 | 100.00% | ₹1,407 |

## Operational events

- **INC-SETL-0079** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Retries reached 246 attempts (1.42% of the day, 2.7 sigma above normal). Only 47.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- App Google Pay ran at 95.60% success on 5,746 attempts (33.1% of the day), 0.74pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

30 June was an incident day: INC-SETL-0079 was live and the rail closed at 95.94% success against a 96.24% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-30` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=17,361, successes=16,656, failed=688, pending=17, settled_value_inr=25,802,616.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=246; retry_share_pct=1.42; recovery_pct=47.56; z=2.73
- categories: mcc_category=Bills; attempts=1,597; own_median=852; z=7.08
- incidents: event_id=INC-SETL-0079; kind=settlement_delay; severity=Sev-2; window=2026-06-30 to 2026-06-30; success_impact_pp=-3.05; volume_impact_pct=-25.52
- psps: payer_psp=Google Pay; attempts=5,746; success_rate=95.6; own_median=96.34; z=-2.82
- headline: attempts=17,361; trailing_median=14,446; z=2.49
- geography: region=North; attempts=4,378; own_median=3,624; z=2.81
- categories: mcc_category=Food & Beverage; attempts=3,024; own_median=2,507.5; z=2.68
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Lite; attempts=2,813; own_median=2,137; z=2.52
- categories: mcc_category=Mobility; attempts=1,558; own_median=1,254.5; z=2.82

Refs: enterprise_data/warehouse/transactions, RPT-D176-DAILY, enterprise_data/warehouse/reference/incidents.parquet
