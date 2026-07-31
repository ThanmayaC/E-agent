---
id: RPT-D119-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-03T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 03 May 2026)

**Report ID:** RPT-D119-DAILY · **Day 119 of 206** · **Derived from:** 14,525 transaction rows queried live from the warehouse

## Summary

The rail took **14,525 payment attempts** on Sunday 03 May 2026 (Weekend) and settled **₹1.65 Cr** across 13,962 successful payments. Volume was −16.7% on yesterday and +33.9% on the same weekday last week. Success closed at **96.12%**, above the trailing 28-day median of 95.42%.

Product UPI Circle is compounding — attempts up 65% across the trailing window to 480 today, with success holding, so the growth is healthy and worth funding. Product Credit on UPI is compounding — attempts up 57% across the trailing window to 190 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,525 | −16.7% | +33.9% | 15,579 |
| Successful payments | 13,962 | −16.9% | +35.2% | 14,979 |
| Success rate | 96.12% | −0.15pp | +0.87pp | 96.14% |
| Settled value | ₹1.65 Cr | −33.9% | +28.5% | ₹1.94 Cr |
| Average ticket | ₹1,179 | −20.4% | −4.9% | ₹1,283 |
| Technical declines | 0.468% | +0.05pp | −0.04pp | 0.413% |
| Business declines | 2.795% | +0.08pp | −1.01pp | 2.858% |
| Risk declines | 0.096% | −0.06pp | −0.01pp | 0.131% |
| Timeout declines | 0.392% | +0.02pp | +0.21pp | 0.339% |
| Retry share | 1.41% | +0.27pp | +0.01pp | 1.39% |
| Latency p95 | 1,209 ms | −2.4% | −0.3% | 1,222 ms |
| Active customers | 11,886 | −13.7% | +27.8% | 12,552 |
| Active merchants | 1,464 | −7.8% | +7.1% | 1,506 |

## What moved

- Product UPI Circle is compounding — attempts up 65% across the trailing window to 480 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 57% across the trailing window to 190 today, with success holding, so the growth is healthy and worth funding.
- Category Bills carried 1,521 attempts, 90% up its trailing median and 15.0% of the day's volume.
- Product UPI Person to Merchant carried 4,119 attempts, 24% up its trailing median and 28.4% of the day's volume.
- Category Food & Beverage carried 2,378 attempts, 18% up its trailing median and 23.4% of the day's volume.
- Category Digital carried 358 attempts, 77% up its trailing median and 3.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,362 | 30.0% | 95.14% | ₹45.25 L | −0.5% |
| UPI Person to Merchant | 4,119 | 28.4% | 96.43% | ₹40.72 L | +24.4% |
| UPI QR Payments | 2,664 | 18.3% | 97.11% | ₹11.14 L | +16.3% |
| UPI Lite | 1,742 | 12.0% | 98.74% | ₹1.56 L | +50.3% |
| UPI Circle | 480 | 3.3% | 97.29% | ₹3.77 L | +45.2% |
| UPI AutoPay | 346 | 2.4% | 87.86% | ₹6.34 L | +6.5% |
| RuPay Credit on UPI | 240 | 1.7% | 95.83% | ₹13.17 L | −28.3% |
| Credit on UPI | 190 | 1.3% | 96.84% | ₹18.40 L | −24.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,597 | 96.21% | 95.52% | ₹56.99 L | normal |
| HDFC Bank | 1,576 | 96.26% | 95.87% | ₹14.87 L | normal |
| Bank of Baroda | 1,083 | 96.31% | 95.62% | ₹12.50 L | normal |
| Union Bank of India | 990 | 95.76% | 94.95% | ₹11.15 L | normal |
| ICICI Bank | 898 | 96.44% | 96.36% | ₹9.31 L | normal |
| Axis Bank | 894 | 96.64% | 95.93% | ₹8.59 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,940 | 95.89% | 95.73% | ₹79.25 L | normal |
| Google Pay | 4,746 | 96.00% | 95.49% | ₹56.01 L | normal |
| Paytm | 1,228 | 97.48% | 95.27% | ₹14.71 L | ⚠ outlier |
| Navi | 507 | 96.25% | 96.03% | ₹3.88 L | normal |
| SuperMoney | 249 | 97.19% | 95.51% | ₹3.35 L | normal |
| BHIM | 149 | 94.63% | 95.70% | ₹1.44 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,741 | 96.44% | ₹36.61 L |
| Food & Beverage | 2,378 | 97.01% | ₹10.13 L |
| Bills | 1,521 | 96.98% | ₹14.78 L |
| Mobility | 1,180 | 97.88% | ₹6.43 L |
| Healthcare | 591 | 98.65% | ₹5.75 L |
| Digital | 358 | 92.74% | ₹2.55 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,254 | 29.3% | 95.79% | ₹49.32 L |
| North | 3,717 | 25.6% | 96.26% | ₹38.79 L |
| West | 3,511 | 24.2% | 96.33% | ₹39.95 L |
| East | 1,780 | 12.3% | 96.46% | ₹25.65 L |
| Central | 1,263 | 8.7% | 95.80% | ₹10.85 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 66 | 95.45% | ₹1.96 L |
| Rapid Bazaar | Key Account | Retail | 393 | 96.95% | ₹1.57 L |
| Vega Electronics | Large | Retail | 38 | 89.47% | ₹1.47 L |
| Ujjwal Water Board | Key Account | Bills | 80 | 96.25% | ₹1.41 L |
| Girnar Connect | Key Account | Bills | 251 | 97.61% | ₹1.18 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 69 | 100.00% | ₹84,640 |
| Hampi Stores 2298 | Key Account | Retail | 118 | 99.15% | ₹83,695 |
| Urban Boutique | Key Account | Retail | 105 | 97.14% | ₹64,462 |

## Failure analysis

Of 545 declined attempts, 406 were business declines (2.795% of attempts — balances, PINs and limits), 68 technical (0.468%), 57 timeouts (0.392%) and 14 risk declines (0.096%).

205 attempts were re-presentations of an earlier failure (1.41% of the day); 64.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 167 | 1.150% | 1.313% |
| ZM | Invalid UPI PIN | business | Customer | 140 | 0.964% | 1.054% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.351% | 0.378% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 34 | 0.234% | 0.201% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.227% | 0.218% |
| U30 | Debit failed at remitter bank | technical | Issuer | 30 | 0.207% | 0.212% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.145% | 0.120% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.117% | 0.112% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 96 | 86 |
| Auto-reversals | 26 | 29 |
| Disputes / chargebacks | 8 | 11 |
| Value returned | ₹1.60 L | ₹1.46 L |

## Customer behaviour

11,886 distinct customers transacted (+12.8% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,641 | 4,236 | 1.16 | 95.66% | ₹1,260 |
| power | 2,485 | 3,408 | 1.37 | 96.24% | ₹1,636 |
| merchant_heavy | 2,743 | 3,348 | 1.22 | 96.06% | ₹919 |
| small_ticket | 1,826 | 2,274 | 1.25 | 96.92% | ₹423 |
| occasional | 950 | 992 | 1.04 | 96.57% | ₹1,299 |
| new | 226 | 252 | 1.12 | 94.44% | ₹779 |
| dormant_returning | 15 | 15 | 1.00 | 93.33% | ₹1,255 |

## Operational events

- **INC-PSP-0029** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 65% across the trailing window to 480 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 57% across the trailing window to 190 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

03 May was an incident day: INC-PSP-0029 was live and the rail closed at 96.12% success against a 95.42% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-03` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,525, successes=13,962, failed=545, pending=18, settled_value_inr=16,456,031.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=480; window_growth_pct=64.9; success_rate=97.29
- incidents: event_id=INC-PSP-0029; kind=psp_degradation; severity=Sev-2; window=2026-05-02 to 2026-05-04; success_impact_pp=-10.68; volume_impact_pct=-16.71
- products: product_name=Credit on UPI; attempts=190; window_growth_pct=56.7; success_rate=96.84
- categories: mcc_category=Bills; attempts=1,521; own_median=798.5; z=4.82
- products: product_name=UPI Person to Merchant; attempts=4,119; own_median=3,310; z=2.38
- categories: mcc_category=Food & Beverage; attempts=2,378; own_median=2,021.5; z=2.42
- categories: mcc_category=Digital; attempts=358; own_median=202; z=6.19
- psps: payer_psp=Paytm; attempts=1,228; success_rate=97.48; own_median=95.27; z=2.35
- products: product_name=UPI Lite; attempts=1,742; own_median=1,159; z=2.5
- incidents: event_id=CMP-0055; kind=merchant_campaign; severity=Sev-3; window=2026-04-30 to 2026-05-08; success_impact_pp=-0.17; volume_impact_pct=67.55

Refs: enterprise_data/warehouse/transactions, RPT-D118-DAILY, enterprise_data/warehouse/reference/incidents.parquet
