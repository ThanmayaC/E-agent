---
id: RPT-D74-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 19 Mar 2026)

**Report ID:** RPT-D74-DAILY · **Day 74 of 206** · **Derived from:** 13,627 transaction rows queried live from the warehouse

## Summary

The rail took **13,627 payment attempts** on Thursday 19 March 2026 (Ugadi / Gudi Padwa) and settled **₹1.51 Cr** across 13,111 successful payments. Volume was +5.2% on yesterday and +26.3% on the same weekday last week. Success closed at **96.21%**, above the trailing 28-day median of 95.65%.

Product UPI Circle is compounding — attempts up 88% across the trailing window to 225 today, but success is slipping as it scales, so the growth is outrunning its reliability. Category Retail carried 4,510 attempts, 41% up its trailing median and 51.3% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,627 | +5.2% | +26.3% | 12,733 |
| Successful payments | 13,111 | +5.6% | +27.6% | 12,196 |
| Success rate | 96.21% | +0.42pp | +0.99pp | 95.76% |
| Settled value | ₹1.51 Cr | +1.2% | +19.8% | ₹1.45 Cr |
| Average ticket | ₹1,155 | −4.2% | −6.1% | ₹1,191 |
| Technical declines | 0.389% | −0.10pp | −0.12pp | 0.456% |
| Business declines | 2.884% | −0.29pp | −0.73pp | 3.231% |
| Risk declines | 0.139% | +0.01pp | −0.04pp | 0.120% |
| Timeout declines | 0.286% | −0.01pp | −0.07pp | 0.338% |
| Retry share | 1.17% | −0.02pp | −0.83pp | 1.29% |
| Latency p95 | 1,233 ms | −1.1% | −5.6% | 1,245 ms |
| Active customers | 11,072 | +3.5% | +20.7% | 10,506 |
| Active merchants | 1,346 | +2.3% | +4.3% | 1,325 |

## What moved

- Product UPI Circle is compounding — attempts up 88% across the trailing window to 225 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Category Retail carried 4,510 attempts, 41% up its trailing median and 51.3% of the day's volume.
- Success rate closed at 96.21%, 0.57pp up the trailing median — a 1.5-sigma move.
- Category Food & Beverage ran at 97.56% success on 2,049 attempts (23.3% of the day), 0.97pp up its own 28-day median.
- Product UPI 123Pay is compounding — attempts up 33% across the trailing window to 101 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,835 | 35.5% | 95.49% | ₹56.30 L | +11.0% |
| UPI Person to Merchant | 3,921 | 28.8% | 96.00% | ₹44.84 L | +14.4% |
| UPI QR Payments | 2,550 | 18.7% | 97.18% | ₹10.65 L | +25.6% |
| UPI Lite | 1,101 | 8.1% | 99.46% | ₹1.04 L | +34.8% |
| UPI AutoPay | 305 | 2.2% | 93.11% | ₹5.31 L | −1.9% |
| UPI Circle | 225 | 1.7% | 95.56% | ₹1.66 L | +35.5% |
| RuPay Credit on UPI | 206 | 1.5% | 97.09% | ₹9.24 L | −8.6% |
| Credit on UPI | 130 | 1.0% | 96.15% | ₹11.25 L | −14.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,391 | 96.38% | 95.59% | ₹45.54 L | normal |
| HDFC Bank | 1,556 | 96.27% | 95.79% | ₹16.17 L | normal |
| Bank of Baroda | 1,008 | 96.53% | 95.58% | ₹10.00 L | normal |
| Union Bank of India | 928 | 95.91% | 95.13% | ₹10.19 L | normal |
| Punjab National Bank | 851 | 94.95% | 95.15% | ₹8.40 L | normal |
| ICICI Bank | 794 | 96.60% | 95.70% | ₹10.36 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,479 | 95.97% | 95.72% | ₹72.29 L | normal |
| Google Pay | 4,462 | 96.50% | 95.57% | ₹51.95 L | normal |
| Paytm | 1,105 | 96.38% | 95.48% | ₹11.32 L | normal |
| Navi | 530 | 96.23% | 95.57% | ₹4.68 L | normal |
| SuperMoney | 286 | 95.45% | 95.85% | ₹2.39 L | normal |
| FamApp | 126 | 97.62% | 96.39% | ₹2.00 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,510 | 96.70% | ₹49.88 L |
| Food & Beverage | 2,049 | 97.56% | ₹9.66 L |
| Mobility | 774 | 97.03% | ₹5.05 L |
| Bills | 636 | 95.91% | ₹7.54 L |
| Healthcare | 337 | 95.85% | ₹4.96 L |
| Digital | 181 | 92.82% | ₹91,710 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,111 | 30.2% | 96.42% | ₹41.92 L |
| North | 3,412 | 25.0% | 96.01% | ₹40.85 L |
| West | 3,270 | 24.0% | 96.06% | ₹38.31 L |
| East | 1,567 | 11.5% | 95.98% | ₹16.63 L |
| Central | 1,267 | 9.3% | 96.76% | ₹13.71 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 495 | 97.17% | ₹2.21 L |
| Vega Electronics | Large | Retail | 23 | 100.00% | ₹1.32 L |
| Hampi Styles | Key Account | Retail | 67 | 95.52% | ₹1.05 L |
| Vasant Wardrobe | Key Account | Retail | 87 | 98.85% | ₹1.03 L |
| Ujjwal Water Board | Key Account | Bills | 29 | 96.55% | ₹80,385 |
| Hampi Stores 2298 | Key Account | Retail | 96 | 95.83% | ₹76,971 |
| Shakti Stores 1531 | Key Account | Retail | 96 | 97.92% | ₹68,385 |
| Urban Boutique | Key Account | Retail | 102 | 95.10% | ₹64,978 |

## Failure analysis

Of 504 declined attempts, 393 were business declines (2.884% of attempts — balances, PINs and limits), 53 technical (0.389%), 39 timeouts (0.286%) and 19 risk declines (0.139%).

159 attempts were re-presentations of an earlier failure (1.17% of the day); 65.4% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 167 | 1.226% | 1.413% |
| ZM | Invalid UPI PIN | business | Customer | 143 | 1.049% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.316% | 0.403% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.176% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.169% | 0.178% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.154% | 0.178% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.125% | 0.092% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 12 | 0.088% | 0.107% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 74 | 75 |
| Auto-reversals | 24 | 24 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹2.51 L | ₹99,240 |

## Customer behaviour

11,072 distinct customers transacted (+11.8% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,426 | 4,009 | 1.17 | 95.91% | ₹1,232 |
| power | 2,366 | 3,286 | 1.39 | 95.92% | ₹1,533 |
| merchant_heavy | 2,464 | 3,051 | 1.24 | 96.26% | ₹904 |
| small_ticket | 1,668 | 2,074 | 1.24 | 96.62% | ₹555 |
| occasional | 905 | 943 | 1.04 | 97.03% | ₹1,141 |
| new | 224 | 244 | 1.09 | 98.36% | ₹683 |
| dormant_returning | 19 | 20 | 1.05 | 90.00% | ₹817 |

## Operational events

- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 88% across the trailing window to 225 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI 123Pay is compounding — attempts up 33% across the trailing window to 101 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 19 March: success came in 0.57pp above baseline at 96.21% on 13,627 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,627, successes=13,111, failed=504, pending=12, settled_value_inr=15,142,957.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=225; window_growth_pct=88.1; success_rate=95.56
- categories: mcc_category=Retail; attempts=4,510; own_median=3,208; z=3.05
- headline: success_rate=96.21; trailing_median=95.65; z=1.53
- categories: mcc_category=Food & Beverage; attempts=2,049; success_rate=97.56; own_median=96.59; z=2.25
- products: product_name=UPI 123Pay; attempts=101; window_growth_pct=32.7; success_rate=95.05
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- products: product_name=UPI 123Pay; attempts=101; own_median=66.5; z=2.33

Refs: enterprise_data/warehouse/transactions, RPT-D73-DAILY, enterprise_data/warehouse/reference/incidents.parquet
