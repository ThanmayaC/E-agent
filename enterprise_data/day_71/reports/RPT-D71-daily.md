---
id: RPT-D71-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 16 Mar 2026)

**Report ID:** RPT-D71-DAILY · **Day 71 of 206** · **Derived from:** 11,668 transaction rows queried live from the warehouse

## Summary

The rail took **11,668 payment attempts** on Monday 16 March 2026 (Working day) and settled **₹1.34 Cr** across 11,177 successful payments. Volume was +12.6% on yesterday and −1.3% on the same weekday last week. Success closed at **95.79%**, in line with the trailing 28-day median of 95.62%.

Product UPI Circle is compounding — attempts up 81% across the trailing window to 190 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,668 | +12.6% | −1.3% | 12,721 |
| Successful payments | 11,177 | +13.6% | −1.4% | 12,179 |
| Success rate | 95.79% | +0.84pp | −0.11pp | 95.71% |
| Settled value | ₹1.34 Cr | +27.9% | −4.6% | ₹1.45 Cr |
| Average ticket | ₹1,203 | +12.6% | −3.2% | ₹1,189 |
| Technical declines | 0.420% | −0.06pp | −0.10pp | 0.457% |
| Business declines | 3.265% | −0.70pp | +0.24pp | 3.263% |
| Risk declines | 0.163% | +0.08pp | +0.01pp | 0.120% |
| Timeout declines | 0.283% | −0.10pp | −0.02pp | 0.350% |
| Retry share | 1.34% | −0.23pp | +0.26pp | 1.32% |
| Latency p95 | 1,241 ms | +1.2% | −4.9% | 1,247 ms |
| Active customers | 9,774 | +11.3% | −1.5% | 10,498 |
| Active merchants | 1,320 | +5.3% | +3.7% | 1,326 |

## What moved

- Product UPI Circle is compounding — attempts up 81% across the trailing window to 190 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI 123Pay is compounding — attempts up 45% across the trailing window to 67 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,126 | 35.4% | 95.35% | ₹42.56 L | −0.2% |
| UPI Person to Merchant | 3,470 | 29.7% | 95.85% | ₹34.59 L | +8.4% |
| UPI QR Payments | 1,936 | 16.6% | 96.59% | ₹8.42 L | −4.6% |
| UPI Lite | 842 | 7.2% | 98.69% | ₹77,680 | +10.8% |
| UPI AutoPay | 285 | 2.4% | 92.63% | ₹5.00 L | −8.4% |
| RuPay Credit on UPI | 269 | 2.3% | 96.28% | ₹10.87 L | +22.8% |
| Credit on UPI | 196 | 1.7% | 94.90% | ₹14.83 L | +28.9% |
| UPI Circle | 190 | 1.6% | 95.26% | ₹1.43 L | +25.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,710 | 95.74% | 95.59% | ₹38.31 L | normal |
| HDFC Bank | 1,258 | 95.47% | 96.03% | ₹15.16 L | normal |
| Bank of Baroda | 883 | 94.90% | 95.64% | ₹9.95 L | normal |
| Union Bank of India | 784 | 94.90% | 95.09% | ₹9.14 L | normal |
| ICICI Bank | 729 | 95.75% | 95.71% | ₹8.83 L | normal |
| Axis Bank | 722 | 95.84% | 95.79% | ₹8.56 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,541 | 95.96% | 95.64% | ₹61.48 L | normal |
| Google Pay | 3,908 | 95.52% | 95.59% | ₹45.95 L | normal |
| Paytm | 932 | 95.92% | 95.50% | ₹11.25 L | normal |
| Navi | 408 | 96.08% | 95.52% | ₹6.08 L | normal |
| SuperMoney | 217 | 92.63% | 95.88% | ₹2.25 L | normal |
| BHIM | 118 | 96.61% | 94.88% | ₹1.64 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,327 | 96.15% | ₹37.64 L |
| Food & Beverage | 1,821 | 96.71% | ₹8.61 L |
| Mobility | 758 | 96.97% | ₹3.92 L |
| Bills | 682 | 95.75% | ₹6.97 L |
| Healthcare | 423 | 96.93% | ₹5.03 L |
| Digital | 196 | 92.35% | ₹1.13 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,503 | 30.0% | 95.52% | ₹39.09 L |
| North | 3,053 | 26.2% | 96.17% | ₹34.23 L |
| West | 2,805 | 24.0% | 95.94% | ₹35.01 L |
| East | 1,314 | 11.3% | 95.59% | ₹16.67 L |
| Central | 993 | 8.5% | 95.47% | ₹9.49 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 72 | 95.83% | ₹2.41 L |
| Vega Electronics | Large | Retail | 30 | 90.00% | ₹2.19 L |
| Rapid Bazaar | Key Account | Retail | 327 | 94.50% | ₹1.31 L |
| Hampi Stores 2298 | Key Account | Retail | 88 | 97.73% | ₹74,205 |
| Yamuna Restaurant | Key Account | Food & Beverage | 71 | 94.37% | ₹70,863 |
| Ujjwal Water Board | Key Account | Bills | 30 | 93.33% | ₹68,311 |
| Urban Boutique | Key Account | Retail | 74 | 95.95% | ₹67,313 |
| Girnar Connect | Key Account | Bills | 115 | 96.52% | ₹62,600 |

## Failure analysis

Of 482 declined attempts, 381 were business declines (3.265% of attempts — balances, PINs and limits), 49 technical (0.420%), 33 timeouts (0.283%) and 19 risk declines (0.163%).

156 attempts were re-presentations of an earlier failure (1.34% of the day); 63.5% of them succeeded.

- Decline code U16 (Risk threshold exceeded at remitter) fired 17 times — 0.146% of attempts against a trailing 0.091%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 171 | 1.466% | 1.413% |
| ZM | Invalid UPI PIN | business | Customer | 132 | 1.131% | 1.109% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.309% | 0.406% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.214% | 0.240% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.171% | 0.176% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.154% | 0.178% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.146% | 0.091% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.111% | 0.124% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 82 | 70 |
| Auto-reversals | 24 | 22 |
| Disputes / chargebacks | 5 | 10 |
| Value returned | ₹1.34 L | ₹94,495 |

## Customer behaviour

9,774 distinct customers transacted (+1.9% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,913 | 3,315 | 1.14 | 95.63% | ₹1,205 |
| power | 2,062 | 2,743 | 1.33 | 95.44% | ₹1,637 |
| merchant_heavy | 2,287 | 2,734 | 1.20 | 95.90% | ₹856 |
| small_ticket | 1,503 | 1,814 | 1.21 | 95.98% | ₹577 |
| occasional | 776 | 812 | 1.05 | 96.55% | ₹1,683 |
| new | 207 | 224 | 1.08 | 97.77% | ₹886 |
| dormant_returning | 26 | 26 | 1.00 | 88.46% | ₹462 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 81% across the trailing window to 190 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI 123Pay is compounding — attempts up 45% across the trailing window to 67 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code U16 (Risk threshold exceeded at remitter) fired 17 times — 0.146% of attempts against a trailing 0.091%. Owner: Issuer.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

16 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.79% success against a 95.62% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,668, successes=11,177, failed=482, pending=9, settled_value_inr=13,448,620.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=190; window_growth_pct=81.4; success_rate=95.26
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI 123Pay; attempts=67; window_growth_pct=44.6; success_rate=92.54
- failures: failure_code=U16; count=17; rate_pct=0.15; trailing_rate_pct=0.09; owner=Issuer; z=2.05
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- products: product_name=UPI International; attempts=116; own_median=79; z=2.5

Refs: enterprise_data/warehouse/transactions, RPT-D70-DAILY, enterprise_data/warehouse/reference/incidents.parquet
