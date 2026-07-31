---
id: RPT-D110-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 24 Apr 2026)

**Report ID:** RPT-D110-DAILY · **Day 110 of 206** · **Derived from:** 11,577 transaction rows queried live from the warehouse

## Summary

The rail took **11,577 payment attempts** on Friday 24 April 2026 (Working day) and settled **₹1.48 Cr** across 10,985 successful payments. Volume was +1.1% on yesterday and −6.1% on the same weekday last week. Success closed at **94.89%**, below the trailing 28-day median of 95.92%.

Success rate closed at 94.89%, 1.03pp down the trailing median — a 2.5-sigma move. Issuer State Bank of India ran at 94.23% success on 3,642 attempts (31.5% of the day), 1.68pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,577 | +1.1% | −6.1% | 12,764 |
| Successful payments | 10,985 | +0.6% | −0.5% | 12,166 |
| Success rate | 94.89% | −0.49pp | +5.35pp | 95.28% |
| Settled value | ₹1.48 Cr | −7.8% | +1.2% | ₹1.65 Cr |
| Average ticket | ₹1,352 | −8.4% | +1.7% | ₹1,358 |
| Technical declines | 0.717% | +0.13pp | −1.33pp | 0.591% |
| Business declines | 3.542% | +0.13pp | +0.12pp | 3.175% |
| Risk declines | 0.138% | −0.05pp | −0.05pp | 0.143% |
| Timeout declines | 0.596% | +0.26pp | −3.97pp | 0.695% |
| Retry share | 1.37% | +0.06pp | −3.62pp | 1.66% |
| Latency p95 | 1,318 ms | +1.7% | −42.4% | 1,345 ms |
| Active customers | 9,843 | +1.2% | −1.6% | 10,590 |
| Active merchants | 1,377 | +0.9% | +0.3% | 1,387 |

## What moved

- Success rate closed at 94.89%, 1.03pp down the trailing median — a 2.5-sigma move.
- Issuer State Bank of India ran at 94.23% success on 3,642 attempts (31.5% of the day), 1.68pp down its own 28-day median.
- Product UPI Person to Person ran at 93.96% success on 3,824 attempts (33.0% of the day), 1.29pp down its own 28-day median.
- Region East ran at 93.27% success on 1,382 attempts (11.9% of the day), 2.46pp down its own 28-day median.
- App Google Pay ran at 94.23% success on 3,864 attempts (33.4% of the day), 1.40pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 38% across the trailing window to 344 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,824 | 33.0% | 93.96% | ₹38.87 L | −13.5% |
| UPI Person to Merchant | 3,084 | 26.6% | 95.43% | ₹26.61 L | −11.1% |
| UPI QR Payments | 1,839 | 15.9% | 96.30% | ₹8.76 L | −15.3% |
| UPI Lite | 1,179 | 10.2% | 98.30% | ₹1.10 L | +5.9% |
| RuPay Credit on UPI | 349 | 3.0% | 94.84% | ₹18.37 L | +10.4% |
| UPI Circle | 344 | 3.0% | 95.64% | ₹2.75 L | +22.6% |
| UPI AutoPay | 322 | 2.8% | 86.65% | ₹5.29 L | +0.5% |
| Credit on UPI | 267 | 2.3% | 94.01% | ₹25.62 L | +20.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,642 | 94.23% | 95.92% | ₹44.87 L | ⚠ outlier |
| HDFC Bank | 1,277 | 95.30% | 96.04% | ₹19.51 L | normal |
| Bank of Baroda | 884 | 95.36% | 95.88% | ₹12.16 L | normal |
| Union Bank of India | 857 | 93.82% | 95.72% | ₹8.55 L | normal |
| Axis Bank | 740 | 96.08% | 95.74% | ₹6.86 L | normal |
| Punjab National Bank | 725 | 94.34% | 95.58% | ₹9.46 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,478 | 95.18% | 95.80% | ₹67.56 L | normal |
| Google Pay | 3,864 | 94.23% | 95.63% | ₹52.44 L | ⚠ outlier |
| Paytm | 927 | 94.07% | 95.85% | ₹15.51 L | normal |
| Navi | 414 | 94.69% | 96.40% | ₹4.50 L | normal |
| SuperMoney | 231 | 97.84% | 94.87% | ₹2.61 L | normal |
| BHIM | 103 | 96.12% | 95.91% | ₹81,191 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,174 | 96.00% | ₹33.69 L |
| Food & Beverage | 1,971 | 96.30% | ₹10.39 L |
| Mobility | 861 | 96.75% | ₹5.09 L |
| Bills | 775 | 93.94% | ₹7.85 L |
| Healthcare | 401 | 95.76% | ₹5.95 L |
| Digital | 193 | 90.67% | ₹1.10 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,377 | 29.2% | 95.03% | ₹46.34 L |
| North | 2,967 | 25.6% | 95.32% | ₹36.47 L |
| West | 2,834 | 24.5% | 94.95% | ₹36.15 L |
| East | 1,382 | 11.9% | 93.27% | ₹18.29 L |
| Central | 1,017 | 8.8% | 95.18% | ₹11.23 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 36 | 94.44% | ₹2.40 L |
| Hampi Stores 2298 | Key Account | Retail | 90 | 96.67% | ₹1.36 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 89.71% | ₹1.23 L |
| Rapid Bazaar | Key Account | Retail | 337 | 96.74% | ₹1.20 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 58 | 96.55% | ₹60,504 |
| Urban Boutique | Key Account | Retail | 82 | 95.12% | ₹59,974 |
| Girnar Connect | Key Account | Bills | 140 | 94.29% | ₹58,969 |
| Hampi Styles | Key Account | Retail | 38 | 92.11% | ₹50,965 |

## Failure analysis

Of 578 declined attempts, 410 were business declines (3.542% of attempts — balances, PINs and limits), 83 technical (0.717%), 69 timeouts (0.596%) and 16 risk declines (0.138%).

159 attempts were re-presentations of an earlier failure (1.37% of the day); 70.4% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 37 times — 0.320% of attempts against a trailing 0.195%. Owner: Issuer.
- Decline code ZA (Transaction declined by customer) fired 56 times — 0.484% of attempts against a trailing 0.378%. Owner: Customer.
- Decline code U30 (Debit failed at remitter bank) fired 33 times — 0.285% of attempts against a trailing 0.194%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 23 times — 0.199% of attempts against a trailing 0.107%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 182 | 1.572% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 123 | 1.062% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.484% | 0.378% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 37 | 0.320% | 0.195% |
| U30 | Debit failed at remitter bank | technical | Issuer | 33 | 0.285% | 0.194% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 23 | 0.199% | 0.107% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.181% | 0.116% |
| XH | Account does not exist / frozen | business | Issuer | 20 | 0.173% | 0.220% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 77 | 80 |
| Auto-reversals | 30 | 28 |
| Disputes / chargebacks | 16 | 11 |
| Value returned | ₹3.48 L | ₹1.55 L |

## Customer behaviour

9,843 distinct customers transacted (−7.2% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,016 | 3,423 | 1.13 | 94.74% | ₹1,292 |
| power | 2,128 | 2,760 | 1.30 | 95.51% | ₹1,768 |
| merchant_heavy | 2,209 | 2,586 | 1.17 | 94.47% | ₹1,182 |
| small_ticket | 1,521 | 1,794 | 1.18 | 94.37% | ₹519 |
| occasional | 763 | 794 | 1.04 | 95.21% | ₹1,734 |
| new | 189 | 203 | 1.07 | 97.04% | ₹751 |
| dormant_returning | 17 | 17 | 1.00 | 100.00% | ₹1,714 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Success rate closed at 94.89%, 1.03pp down the trailing median — a 2.5-sigma move.
- Issuer State Bank of India ran at 94.23% success on 3,642 attempts (31.5% of the day), 1.68pp down its own 28-day median.
- Product UPI Person to Person ran at 93.96% success on 3,824 attempts (33.0% of the day), 1.29pp down its own 28-day median.
- Decline code U54 (Transaction timed out at beneficiary) fired 37 times — 0.320% of attempts against a trailing 0.195%. Owner: Issuer.
- Region East ran at 93.27% success on 1,382 attempts (11.9% of the day), 2.46pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 25% across the trailing window to 1,179 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 24 April: success came in 1.03pp below baseline at 94.89% on 11,577 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,577, successes=10,985, failed=578, pending=14, settled_value_inr=14,848,414.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: success_rate=94.89; trailing_median=95.92; z=-2.5
- banks: payer_bank=State Bank of India; attempts=3,642; success_rate=94.23; own_median=95.92; z=-2.66
- products: product_name=UPI Person to Person; attempts=3,824; success_rate=93.96; own_median=95.25; z=-2.46
- failures: failure_code=U54; count=37; rate_pct=0.32; trailing_rate_pct=0.19; owner=Issuer; z=2.7
- geography: region=East; attempts=1,382; success_rate=93.27; own_median=95.73; z=-3.73
- failures: failure_code=ZA; count=56; rate_pct=0.48; trailing_rate_pct=0.38; owner=Customer; z=2.12
- psps: payer_psp=Google Pay; attempts=3,864; success_rate=94.23; own_median=95.62; z=-2.11
- failures: failure_code=U30; count=33; rate_pct=0.28; trailing_rate_pct=0.19; owner=Issuer; z=2.36
- failures: failure_code=BT; count=23; rate_pct=0.2; trailing_rate_pct=0.11; owner=NPCI; z=2.82
- products: product_name=UPI Circle; attempts=344; window_growth_pct=37.8; success_rate=95.64

Refs: enterprise_data/warehouse/transactions, RPT-D109-DAILY, enterprise_data/warehouse/reference/incidents.parquet
