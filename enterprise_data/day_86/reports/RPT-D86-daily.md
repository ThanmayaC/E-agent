---
id: RPT-D86-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-31T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 31 Mar 2026)

**Report ID:** RPT-D86-DAILY · **Day 86 of 206** · **Derived from:** 13,701 transaction rows queried live from the warehouse

## Summary

The rail took **13,701 payment attempts** on Tuesday 31 March 2026 (Financial Year End) and settled **₹2.08 Cr** across 13,198 successful payments. Volume was −2.0% on yesterday and +34.9% on the same weekday last week. Success closed at **96.33%**, above the trailing 28-day median of 95.79%.

Category Bills carried 1,316 attempts, 89% up its trailing median and 14.6% of the day's volume. Success rate closed at 96.33%, 0.54pp up the trailing median — a 2.1-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,701 | −2.0% | +34.9% | 12,477 |
| Successful payments | 13,198 | −1.7% | +36.2% | 11,933 |
| Success rate | 96.33% | +0.36pp | +0.92pp | 95.58% |
| Settled value | ₹2.08 Cr | +13.7% | +69.8% | ₹1.44 Cr |
| Average ticket | ₹1,573 | +15.6% | +24.7% | ₹1,208 |
| Technical declines | 0.460% | +0.05pp | +0.04pp | 0.474% |
| Business declines | 2.671% | −0.39pp | −0.97pp | 3.292% |
| Risk declines | 0.109% | −0.04pp | −0.07pp | 0.123% |
| Timeout declines | 0.336% | +0.02pp | +0.09pp | 0.426% |
| Retry share | 1.26% | +0.18pp | +0.08pp | 1.41% |
| Latency p95 | 1,276 ms | +0.9% | −0.2% | 1,283 ms |
| Active customers | 11,243 | −2.3% | +28.9% | 10,341 |
| Active merchants | 1,409 | −0.5% | +11.0% | 1,325 |

## What moved

- Category Bills carried 1,316 attempts, 89% up its trailing median and 14.6% of the day's volume.
- Success rate closed at 96.33%, 0.54pp up the trailing median — a 2.1-sigma move.
- Product Credit on UPI is compounding — attempts up 37% across the trailing window to 350 today, with success holding, so the growth is healthy and worth funding.
- Settled value moved up while volume moved up — average ticket at ₹1,573 against a trailing ₹1,215, so the day's shape is a mix shift rather than a demand shift.
- Product RuPay Credit on UPI carried 528 attempts, 128% up its trailing median and 3.9% of the day's volume.
- Category Mobility carried 944 attempts, 22% up its trailing median and 10.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,708 | 34.4% | 95.82% | ₹51.55 L | +7.4% |
| UPI Person to Merchant | 4,075 | 29.7% | 96.71% | ₹44.52 L | +17.7% |
| UPI QR Payments | 2,026 | 14.8% | 96.35% | ₹9.55 L | −5.5% |
| UPI Lite | 957 | 7.0% | 99.06% | ₹86,077 | +3.6% |
| RuPay Credit on UPI | 528 | 3.9% | 96.78% | ₹28.18 L | +127.6% |
| Credit on UPI | 350 | 2.6% | 95.71% | ₹34.63 L | +124.4% |
| UPI AutoPay | 321 | 2.3% | 92.52% | ₹5.94 L | +1.4% |
| UPI Circle | 282 | 2.1% | 98.23% | ₹2.63 L | +43.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,233 | 96.29% | 95.79% | ₹58.73 L | normal |
| HDFC Bank | 1,579 | 97.09% | 95.59% | ₹22.40 L | normal |
| Bank of Baroda | 1,031 | 97.28% | 95.94% | ₹12.20 L | normal |
| Union Bank of India | 928 | 96.55% | 95.75% | ₹16.72 L | normal |
| ICICI Bank | 835 | 97.01% | 95.86% | ₹13.57 L | normal |
| Punjab National Bank | 822 | 95.13% | 95.62% | ₹15.26 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,421 | 96.17% | 95.93% | ₹89.53 L | normal |
| Google Pay | 4,601 | 96.46% | 95.68% | ₹77.11 L | normal |
| Paytm | 1,047 | 96.08% | 95.81% | ₹16.07 L | normal |
| Navi | 492 | 96.75% | 95.67% | ₹7.58 L | normal |
| SuperMoney | 262 | 96.56% | 95.09% | ₹3.99 L | normal |
| FamApp | 140 | 97.14% | 96.86% | ₹2.96 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,618 | 96.57% | ₹56.74 L |
| Food & Beverage | 2,016 | 97.22% | ₹11.81 L |
| Bills | 1,316 | 96.88% | ₹14.83 L |
| Mobility | 944 | 96.50% | ₹7.11 L |
| Healthcare | 390 | 97.69% | ₹5.09 L |
| Digital | 293 | 96.59% | ₹1.96 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,044 | 29.5% | 96.46% | ₹65.39 L |
| North | 3,460 | 25.3% | 95.87% | ₹50.63 L |
| West | 3,320 | 24.2% | 96.54% | ₹48.39 L |
| East | 1,725 | 12.6% | 96.93% | ₹24.87 L |
| Central | 1,152 | 8.4% | 95.75% | ₹18.28 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 43 | 88.37% | ₹3.13 L |
| Vasant Wardrobe | Key Account | Retail | 100 | 96.00% | ₹2.74 L |
| Rapid Bazaar | Key Account | Retail | 327 | 98.17% | ₹1.56 L |
| Ujjwal Water Board | Key Account | Bills | 87 | 97.70% | ₹1.52 L |
| Girnar Connect | Key Account | Bills | 219 | 97.26% | ₹1.03 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 91 | 96.70% | ₹87,607 |
| Hampi Styles | Key Account | Retail | 33 | 93.94% | ₹79,048 |
| Hampi Stores 2298 | Key Account | Retail | 97 | 97.94% | ₹70,596 |

## Failure analysis

Of 490 declined attempts, 366 were business declines (2.671% of attempts — balances, PINs and limits), 63 technical (0.460%), 46 timeouts (0.336%) and 15 risk declines (0.109%).

173 attempts were re-presentations of an earlier failure (1.26% of the day); 71.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 148 | 1.080% | 1.341% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 0.985% | 1.082% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.314% | 0.370% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.190% | 0.186% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.182% | 0.154% |
| XH | Account does not exist / frozen | business | Issuer | 19 | 0.139% | 0.224% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.131% | 0.114% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.109% | 0.101% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 69 | 78 |
| Auto-reversals | 19 | 24 |
| Disputes / chargebacks | 12 | 10 |
| Value returned | ₹1.76 L | ₹1.31 L |

## Customer behaviour

11,243 distinct customers transacted (+13.1% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,532 | 4,068 | 1.15 | 96.41% | ₹1,655 |
| power | 2,336 | 3,221 | 1.38 | 96.46% | ₹2,270 |
| merchant_heavy | 2,526 | 3,087 | 1.22 | 96.44% | ₹1,141 |
| small_ticket | 1,699 | 2,097 | 1.23 | 95.61% | ₹595 |
| occasional | 898 | 957 | 1.07 | 96.66% | ₹1,552 |
| new | 221 | 240 | 1.09 | 97.08% | ₹1,820 |
| dormant_returning | 31 | 31 | 1.00 | 93.55% | ₹679 |

## Operational events

- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product Credit on UPI is compounding — attempts up 37% across the trailing window to 350 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 31 March: success came in 0.54pp above baseline at 96.33% on 13,701 attempts. Worth understanding what went right — a sustained gain here is worth more than a volume campaign.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-31` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,701, successes=13,198, failed=490, pending=13, settled_value_inr=20,756,785.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,316; own_median=694.5; z=6.99
- headline: success_rate=96.33; trailing_median=95.79; z=2.07
- products: product_name=Credit on UPI; attempts=350; window_growth_pct=36.8; success_rate=95.71
- headline: value_inr=20,756,785; avg_ticket=1,572.72; trailing_avg_ticket=1,214.78
- products: product_name=RuPay Credit on UPI; attempts=528; own_median=232; z=6.44
- categories: mcc_category=Mobility; attempts=944; own_median=773; z=3.25
- products: product_name=Credit on UPI; attempts=350; own_median=156; z=4.94
- categories: mcc_category=Travel; attempts=132; own_median=63; z=4.43
- products: product_name=UPI International; attempts=193; own_median=97; z=4.47
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31

Refs: enterprise_data/warehouse/transactions, RPT-D85-DAILY, enterprise_data/warehouse/reference/incidents.parquet
