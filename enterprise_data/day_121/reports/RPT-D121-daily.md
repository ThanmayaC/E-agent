---
id: RPT-D121-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 05 May 2026)

**Report ID:** RPT-D121-DAILY · **Day 121 of 206** · **Derived from:** 15,078 transaction rows queried live from the warehouse

## Summary

The rail took **15,078 payment attempts** on Tuesday 05 May 2026 (Working day) and settled **₹2.16 Cr** across 14,449 successful payments. Volume was −2.1% on yesterday and +27.7% on the same weekday last week. Success closed at **95.83%**, above the trailing 28-day median of 95.53%.

Product UPI Circle is compounding — attempts up 71% across the trailing window to 433 today, with success holding, so the growth is healthy and worth funding. Category Bills carried 1,590 attempts, 99% up its trailing median and 16.5% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,078 | −2.1% | +27.7% | 15,445 |
| Successful payments | 14,449 | −2.4% | +28.7% | 14,838 |
| Success rate | 95.83% | −0.24pp | +0.74pp | 96.06% |
| Settled value | ₹2.16 Cr | +1.0% | +33.4% | ₹2.02 Cr |
| Average ticket | ₹1,492 | +3.5% | +3.6% | ₹1,356 |
| Technical declines | 0.597% | +0.05pp | −0.02pp | 0.476% |
| Business declines | 3.044% | +0.12pp | −0.73pp | 2.908% |
| Risk declines | 0.126% | +0.07pp | +0.03pp | 0.115% |
| Timeout declines | 0.352% | +0.09pp | +0.00pp | 0.325% |
| Retry share | 1.17% | +0.04pp | −0.78pp | 1.29% |
| Latency p95 | 1,269 ms | +3.0% | −2.7% | 1,233 ms |
| Active customers | 12,253 | −2.4% | +22.9% | 12,493 |
| Active merchants | 1,485 | +0.7% | +4.4% | 1,496 |

## What moved

- Product UPI Circle is compounding — attempts up 71% across the trailing window to 433 today, with success holding, so the growth is healthy and worth funding.
- Category Bills carried 1,590 attempts, 99% up its trailing median and 16.5% of the day's volume.
- Product Credit on UPI is compounding — attempts up 55% across the trailing window to 359 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,452 | 36.2% | 94.96% | ₹60.95 L | +24.4% |
| UPI Person to Merchant | 3,867 | 25.6% | 95.97% | ₹38.28 L | +16.8% |
| UPI QR Payments | 2,296 | 15.2% | 96.86% | ₹8.88 L | +0.2% |
| UPI Lite | 1,532 | 10.2% | 98.89% | ₹1.49 L | +32.2% |
| UPI Circle | 433 | 2.9% | 96.30% | ₹3.94 L | +28.1% |
| RuPay Credit on UPI | 396 | 2.6% | 94.19% | ₹25.37 L | +17.7% |
| Credit on UPI | 359 | 2.4% | 93.59% | ₹45.35 L | +40.8% |
| UPI AutoPay | 326 | 2.2% | 93.87% | ₹5.61 L | +0.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,681 | 95.88% | 95.67% | ₹68.22 L | normal |
| HDFC Bank | 1,624 | 95.94% | 95.87% | ₹19.20 L | normal |
| Bank of Baroda | 1,188 | 95.88% | 95.66% | ₹17.66 L | normal |
| Union Bank of India | 1,057 | 94.80% | 94.99% | ₹12.66 L | normal |
| Axis Bank | 918 | 96.95% | 95.95% | ₹14.88 L | normal |
| Punjab National Bank | 916 | 96.72% | 95.57% | ₹12.61 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,231 | 95.91% | 95.76% | ₹1.02 Cr | normal |
| Google Pay | 4,950 | 95.54% | 95.56% | ₹63.89 L | normal |
| Paytm | 1,170 | 96.24% | 95.42% | ₹19.04 L | normal |
| Navi | 553 | 96.56% | 96.03% | ₹12.14 L | normal |
| SuperMoney | 303 | 94.39% | 95.63% | ₹3.94 L | normal |
| BHIM | 166 | 95.18% | 95.52% | ₹5.07 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,550 | 95.92% | ₹43.25 L |
| Food & Beverage | 2,118 | 96.69% | ₹8.86 L |
| Bills | 1,590 | 96.29% | ₹17.47 L |
| Mobility | 1,053 | 97.82% | ₹5.60 L |
| Healthcare | 542 | 97.42% | ₹11.06 L |
| Digital | 310 | 95.81% | ₹1.64 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,505 | 29.9% | 95.98% | ₹65.90 L |
| North | 3,813 | 25.3% | 95.65% | ₹50.66 L |
| West | 3,714 | 24.6% | 96.10% | ₹57.83 L |
| East | 1,836 | 12.2% | 95.10% | ₹27.89 L |
| Central | 1,210 | 8.0% | 96.12% | ₹13.34 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 90.32% | ₹3.31 L |
| Ujjwal Water Board | Key Account | Bills | 98 | 95.92% | ₹1.92 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 97.06% | ₹1.86 L |
| Rapid Bazaar | Key Account | Retail | 340 | 96.18% | ₹1.78 L |
| Girnar Connect | Key Account | Bills | 290 | 97.24% | ₹1.47 L |
| Urban Boutique | Key Account | Retail | 104 | 93.27% | ₹80,707 |
| Hampi Stores 2298 | Key Account | Retail | 111 | 94.59% | ₹78,853 |
| Yamuna Restaurant | Key Account | Food & Beverage | 85 | 98.82% | ₹78,030 |

## Failure analysis

Of 621 declined attempts, 459 were business declines (3.044% of attempts — balances, PINs and limits), 90 technical (0.597%), 53 timeouts (0.352%) and 19 risk declines (0.126%).

176 attempts were re-presentations of an earlier failure (1.17% of the day); 63.6% of them succeeded.

- Decline code U28 (Remitter bank unavailable) fired 28 times — 0.186% of attempts against a trailing 0.120%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 190 | 1.260% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 150 | 0.995% | 1.050% |
| ZA | Transaction declined by customer | business | Customer | 62 | 0.411% | 0.378% |
| XH | Account does not exist / frozen | business | Issuer | 36 | 0.239% | 0.218% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.212% | 0.209% |
| U28 | Remitter bank unavailable | technical | Issuer | 28 | 0.186% | 0.120% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 23 | 0.153% | 0.112% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.146% | 0.201% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 86 | 88 |
| Auto-reversals | 27 | 28 |
| Disputes / chargebacks | 15 | 11 |
| Value returned | ₹1.33 L | ₹1.46 L |

## Customer behaviour

12,253 distinct customers transacted (+14.2% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,773 | 4,378 | 1.16 | 96.48% | ₹1,493 |
| power | 2,565 | 3,571 | 1.39 | 95.72% | ₹2,119 |
| merchant_heavy | 2,760 | 3,404 | 1.23 | 95.39% | ₹983 |
| small_ticket | 1,896 | 2,374 | 1.25 | 95.49% | ₹565 |
| occasional | 994 | 1,054 | 1.06 | 95.92% | ₹2,380 |
| new | 239 | 270 | 1.13 | 94.44% | ₹923 |
| dormant_returning | 26 | 27 | 1.04 | 100.00% | ₹426 |

## Operational events

- **INC-BANK-0008** (Sev-3) — Canara Bank issuer decline spike, scoped to Canara Bank between 20:00 and 24:00. Canara Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product Credit on UPI is compounding — attempts up 55% across the trailing window to 359 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code U28 (Remitter bank unavailable) fired 28 times — 0.186% of attempts against a trailing 0.120%. Owner: Issuer.

### Opportunities

- Product UPI Circle is compounding — attempts up 71% across the trailing window to 433 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

05 May ran on trend at 95.83% success and ₹2.16 Cr settled. The movement worth carrying forward is in the product mix: product UPI Circle is compounding — attempts up 71% across the trailing window to 433 today, with success holding, so the growth is healthy and worth funding. 2 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,078, successes=14,449, failed=621, pending=8, settled_value_inr=21,561,519.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=433; window_growth_pct=71; success_rate=96.3
- categories: mcc_category=Bills; attempts=1,590; own_median=798.5; z=5.29
- products: product_name=Credit on UPI; attempts=359; window_growth_pct=54.7; success_rate=93.59
- failures: failure_code=U28; count=28; rate_pct=0.19; trailing_rate_pct=0.12; owner=Issuer; z=2.29
- incidents: event_id=INC-BANK-0008; kind=bank_outage; severity=Sev-3; window=2026-05-05 to 2026-05-07; success_impact_pp=-5.9; volume_impact_pct=-5.23
- categories: mcc_category=Digital; attempts=310; own_median=202; z=4.29
- categories: mcc_category=Healthcare; attempts=542; own_median=423; z=2.59
- incidents: event_id=CMP-0055; kind=merchant_campaign; severity=Sev-3; window=2026-04-30 to 2026-05-08; success_impact_pp=-0.17; volume_impact_pct=67.55

Refs: enterprise_data/warehouse/transactions, RPT-D120-DAILY, enterprise_data/warehouse/reference/incidents.parquet
