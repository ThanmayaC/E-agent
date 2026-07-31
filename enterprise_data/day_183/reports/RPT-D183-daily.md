---
id: RPT-D183-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-06T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 06 Jul 2026)

**Report ID:** RPT-D183-DAILY · **Day 183 of 206** · **Derived from:** 16,750 transaction rows queried live from the warehouse

## Summary

The rail took **16,750 payment attempts** on Monday 06 July 2026 (Working day) and settled **₹2.34 Cr** across 16,211 successful payments. Volume was +3.8% on yesterday and −2.6% on the same weekday last week. Success closed at **96.78%**, above the trailing 28-day median of 96.16%.

84 auto-reversals were raised, 11.6 sigma above the trailing median of 24. Category Bills carried 1,885 attempts, 121% up its trailing median and 15.3% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,750 | +3.8% | −2.6% | 17,802 |
| Successful payments | 16,211 | +4.9% | −2.3% | 17,056 |
| Success rate | 96.78% | +1.00pp | +0.23pp | 95.87% |
| Settled value | ₹2.34 Cr | +41.4% | −0.8% | ₹2.25 Cr |
| Average ticket | ₹1,444 | +34.9% | +1.6% | ₹1,319 |
| Technical declines | 0.454% | +0.03pp | +0.06pp | 0.545% |
| Business declines | 2.316% | −0.73pp | −0.35pp | 2.658% |
| Risk declines | 0.149% | +0.03pp | +0.07pp | 0.118% |
| Timeout declines | 0.245% | −0.29pp | −0.01pp | 0.731% |
| Retry share | 0.93% | −2.01pp | −0.09pp | 1.74% |
| Latency p95 | 1,273 ms | +3.7% | −0.0% | 1,343 ms |
| Active customers | 13,560 | +3.2% | −2.3% | 14,210 |
| Active merchants | 1,634 | +1.6% | +0.4% | 1,654 |

## What moved

- Category Bills carried 1,885 attempts, 121% up its trailing median and 15.3% of the day's volume.
- App PhonePe ran at 96.91% success on 7,941 attempts (47.4% of the day), 0.81pp up its own 28-day median.
- Success rate closed at 96.78%, 0.62pp up the trailing median — a 1.9-sigma move.
- Issuer State Bank of India ran at 97.04% success on 5,330 attempts (31.8% of the day), 0.87pp up its own 28-day median.
- Product UPI Lite is compounding — attempts up 45% across the trailing window to 2,845 today, with success holding, so the growth is healthy and worth funding.
- Region West ran at 96.92% success on 4,063 attempts (24.3% of the day), 0.96pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,460 | 26.6% | 95.85% | ₹50.27 L | +6.8% |
| UPI Person to Merchant | 3,965 | 23.7% | 96.72% | ₹39.02 L | +15.3% |
| UPI Lite | 2,845 | 17.0% | 98.98% | ₹2.61 L | +26.6% |
| UPI QR Payments | 2,735 | 16.3% | 97.44% | ₹13.11 L | +11.2% |
| UPI Circle | 911 | 5.4% | 97.80% | ₹9.70 L | +16.7% |
| Credit on UPI | 470 | 2.8% | 95.11% | ₹42.88 L | −0.9% |
| UPI AutoPay | 401 | 2.4% | 91.27% | ₹7.68 L | +6.9% |
| RuPay Credit on UPI | 389 | 2.3% | 96.40% | ₹27.77 L | +5.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,330 | 97.04% | 96.16% | ₹73.51 L | ⚠ outlier |
| HDFC Bank | 1,791 | 95.81% | 96.37% | ₹28.33 L | normal |
| Bank of Baroda | 1,294 | 96.83% | 96.21% | ₹14.06 L | normal |
| Union Bank of India | 1,159 | 96.46% | 96.00% | ₹16.10 L | normal |
| ICICI Bank | 1,050 | 98.29% | 96.34% | ₹14.91 L | normal |
| Punjab National Bank | 1,050 | 97.14% | 95.86% | ₹13.95 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,941 | 96.91% | 96.11% | ₹1.11 Cr | ⚠ outlier |
| Google Pay | 5,486 | 96.72% | 96.21% | ₹76.25 L | normal |
| Paytm | 1,331 | 96.54% | 95.98% | ₹19.91 L | normal |
| Navi | 638 | 96.71% | 96.34% | ₹8.21 L | normal |
| SuperMoney | 343 | 96.79% | 95.51% | ₹6.09 L | normal |
| BHIM | 180 | 95.56% | 95.91% | ₹2.54 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,516 | 96.90% | ₹60.47 L |
| Food & Beverage | 2,888 | 98.13% | ₹14.35 L |
| Bills | 1,885 | 96.82% | ₹18.33 L |
| Mobility | 1,507 | 98.14% | ₹9.54 L |
| Healthcare | 605 | 97.69% | ₹9.00 L |
| Digital | 341 | 93.84% | ₹2.49 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,935 | 29.5% | 96.78% | ₹70.71 L |
| North | 4,263 | 25.5% | 96.62% | ₹57.92 L |
| West | 4,063 | 24.3% | 96.92% | ₹60.05 L |
| East | 2,059 | 12.3% | 96.84% | ₹27.02 L |
| Central | 1,430 | 8.5% | 96.78% | ₹18.36 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 93.75% | ₹3.99 L |
| Vasant Wardrobe | Key Account | Retail | 88 | 90.91% | ₹3.27 L |
| Rapid Bazaar | Key Account | Retail | 460 | 97.83% | ₹2.08 L |
| Girnar Connect | Key Account | Bills | 370 | 97.03% | ₹1.41 L |
| Ujjwal Water Board | Key Account | Bills | 82 | 97.56% | ₹1.23 L |
| Hampi Stores 2298 | Key Account | Retail | 99 | 94.95% | ₹1.06 L |
| Swift Grill | Large | Food & Beverage | 46 | 100.00% | ₹95,021 |
| Yamuna Restaurant | Key Account | Food & Beverage | 74 | 98.65% | ₹80,856 |

## Failure analysis

Of 530 declined attempts, 388 were business declines (2.316% of attempts — balances, PINs and limits), 76 technical (0.454%), 41 timeouts (0.245%) and 25 risk declines (0.149%).

155 attempts were re-presentations of an earlier failure (0.93% of the day); 74.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 184 | 1.099% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 109 | 0.651% | 0.970% |
| ZA | Transaction declined by customer | business | Customer | 38 | 0.227% | 0.328% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.191% | 0.199% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.173% | 0.179% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.125% | 0.118% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.119% | 0.098% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.113% | 0.133% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 102 | 110 |
| Auto-reversals | 84 | 24 |
| Disputes / chargebacks | 17 | 14 |
| Value returned | ₹1.65 L | ₹1.71 L |

## Customer behaviour

13,560 distinct customers transacted (+12.8% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,262 | 4,996 | 1.17 | 97.00% | ₹1,635 |
| power | 2,863 | 3,978 | 1.39 | 96.38% | ₹1,885 |
| merchant_heavy | 3,164 | 3,920 | 1.24 | 97.02% | ₹1,124 |
| small_ticket | 1,965 | 2,454 | 1.25 | 96.86% | ₹569 |
| occasional | 1,062 | 1,132 | 1.07 | 96.55% | ₹1,437 |
| new | 218 | 243 | 1.11 | 95.47% | ₹1,181 |
| dormant_returning | 26 | 27 | 1.04 | 96.30% | ₹791 |

## Operational events

- **INC-NET-0040** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 20:00 and 24:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **CMP-0052** (Sev-3) — Hospitals cashback campaign, scoped to 8062. A cashback campaign across Hospitals merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 84 auto-reversals were raised, 11.6 sigma above the trailing median of 24.
- Product UPI 123Pay is compounding — attempts up 39% across the trailing window to 109 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Lite is compounding — attempts up 45% across the trailing window to 2,845 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

06 July was an incident day: INC-NET-0040 was live and the rail closed at 96.78% success against a 96.16% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-06` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,750, successes=16,211, failed=530, pending=9, settled_value_inr=23,406,709.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: reversals=84; trailing_median=24; z=11.56
- incidents: event_id=INC-NET-0040; kind=network_latency; severity=Sev-1; window=2026-07-04 to 2026-07-06; success_impact_pp=-14.23; volume_impact_pct=-13.13
- categories: mcc_category=Bills; attempts=1,885; own_median=852; z=9.81
- psps: payer_psp=PhonePe; attempts=7,941; success_rate=96.91; own_median=96.11; z=3.11
- headline: success_rate=96.78; trailing_median=96.16; z=1.85
- banks: payer_bank=State Bank of India; attempts=5,330; success_rate=97.04; own_median=96.17; z=2.36
- products: product_name=UPI Lite; attempts=2,845; window_growth_pct=45.3; success_rate=98.98
- geography: region=West; attempts=4,063; success_rate=96.92; own_median=95.96; z=2.49
- products: product_name=UPI 123Pay; attempts=109; window_growth_pct=39.3; success_rate=92.66
- products: product_name=UPI QR Payments; attempts=2,735; success_rate=97.44; own_median=96.53; z=2.4

Refs: enterprise_data/warehouse/transactions, RPT-D182-DAILY, enterprise_data/warehouse/reference/incidents.parquet
