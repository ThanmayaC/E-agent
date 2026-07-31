---
id: RPT-D114-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 28 Apr 2026)

**Report ID:** RPT-D114-DAILY · **Day 114 of 206** · **Derived from:** 11,805 transaction rows queried live from the warehouse

## Summary

The rail took **11,805 payment attempts** on Tuesday 28 April 2026 (Working day) and settled **₹1.62 Cr** across 11,225 successful payments. Volume was −4.6% on yesterday and −8.6% on the same weekday last week. Success closed at **95.09%**, below the trailing 28-day median of 95.74%.

Decline code ZM (Invalid UPI PIN) fired 156 times — 1.321% of attempts against a trailing 1.030%. Owner: Customer. Retries reached 230 attempts (1.95% of the day, 2.7 sigma above normal). 62.6% of re-presented payments recovered, so the retry path was doing its job.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,805 | −4.6% | −8.6% | 12,658 |
| Successful payments | 11,225 | −4.9% | −9.4% | 12,065 |
| Success rate | 95.09% | −0.30pp | −0.76pp | 95.28% |
| Settled value | ₹1.62 Cr | +1.0% | −10.7% | ₹1.63 Cr |
| Average ticket | ₹1,440 | +6.2% | −1.4% | ₹1,353 |
| Technical declines | 0.618% | −0.00pp | +0.10pp | 0.586% |
| Business declines | 3.770% | +0.30pp | +0.70pp | 3.239% |
| Risk declines | 0.093% | −0.02pp | +0.00pp | 0.139% |
| Timeout declines | 0.347% | +0.01pp | −0.03pp | 0.642% |
| Retry share | 1.95% | +0.49pp | +0.86pp | 1.65% |
| Latency p95 | 1,305 ms | +1.4% | +2.2% | 1,332 ms |
| Active customers | 9,966 | −3.6% | −7.6% | 10,525 |
| Active merchants | 1,422 | +2.0% | +1.4% | 1,388 |

## What moved

- Region North ran at 94.57% success on 3,022 attempts (25.6% of the day), 1.14pp down its own 28-day median.
- Category Mobility ran at 95.59% success on 816 attempts (10.6% of the day), 1.15pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 29% across the trailing window to 343 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,085 | 34.6% | 95.01% | ₹39.52 L | −5.8% |
| UPI Person to Merchant | 2,965 | 25.1% | 95.82% | ₹29.91 L | −11.7% |
| UPI QR Payments | 1,903 | 16.1% | 95.48% | ₹7.70 L | −11.6% |
| UPI Lite | 1,077 | 9.1% | 98.79% | ₹91,107 | −6.1% |
| UPI AutoPay | 366 | 3.1% | 82.24% | ₹5.77 L | +13.1% |
| RuPay Credit on UPI | 354 | 3.0% | 94.63% | ₹16.72 L | +10.6% |
| UPI Circle | 343 | 2.9% | 95.63% | ₹2.96 L | +15.7% |
| Credit on UPI | 318 | 2.7% | 94.34% | ₹27.73 L | +43.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,734 | 95.21% | 95.70% | ₹48.66 L | normal |
| HDFC Bank | 1,284 | 95.72% | 95.95% | ₹14.76 L | normal |
| Bank of Baroda | 862 | 95.71% | 95.83% | ₹13.04 L | normal |
| Union Bank of India | 825 | 94.06% | 95.19% | ₹12.94 L | normal |
| Axis Bank | 712 | 94.24% | 95.87% | ₹12.90 L | ⚠ outlier |
| Punjab National Bank | 700 | 95.57% | 95.33% | ₹9.44 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,530 | 95.30% | 95.78% | ₹79.46 L | normal |
| Google Pay | 3,997 | 95.05% | 95.56% | ₹51.06 L | normal |
| Paytm | 922 | 94.47% | 95.61% | ₹12.43 L | normal |
| Navi | 421 | 95.01% | 96.40% | ₹5.85 L | normal |
| SuperMoney | 203 | 96.55% | 95.13% | ₹1.97 L | normal |
| BHIM | 121 | 95.04% | 96.11% | ₹1.74 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,819 | 95.71% | ₹36.48 L |
| Food & Beverage | 1,962 | 96.53% | ₹9.37 L |
| Bills | 1,052 | 94.39% | ₹12.19 L |
| Mobility | 816 | 95.59% | ₹4.34 L |
| Healthcare | 369 | 96.21% | ₹3.41 L |
| Digital | 247 | 91.50% | ₹1.42 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,575 | 30.3% | 95.47% | ₹53.86 L |
| North | 3,022 | 25.6% | 94.57% | ₹41.77 L |
| West | 2,853 | 24.2% | 95.27% | ₹34.63 L |
| East | 1,379 | 11.7% | 94.34% | ₹17.27 L |
| Central | 976 | 8.3% | 95.80% | ₹14.12 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 76 | 93.42% | ₹2.76 L |
| Vega Electronics | Large | Retail | 31 | 74.19% | ₹2.03 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 63 | 95.24% | ₹1.70 L |
| Rapid Bazaar | Key Account | Retail | 260 | 98.46% | ₹84,475 |
| Girnar Connect | Key Account | Bills | 178 | 94.94% | ₹83,608 |
| Ujjwal Water Board | Key Account | Bills | 53 | 96.23% | ₹80,701 |
| Hampi Stores 2298 | Key Account | Retail | 103 | 92.23% | ₹71,143 |
| Shakti Stores 1531 | Key Account | Retail | 56 | 98.21% | ₹52,523 |

## Failure analysis

Of 570 declined attempts, 445 were business declines (3.770% of attempts — balances, PINs and limits), 73 technical (0.618%), 41 timeouts (0.347%) and 11 risk declines (0.093%).

230 attempts were re-presentations of an earlier failure (1.95% of the day); 62.6% of them succeeded.

- Decline code ZM (Invalid UPI PIN) fired 156 times — 1.321% of attempts against a trailing 1.030%. Owner: Customer.
- Retries reached 230 attempts (1.95% of the day, 2.7 sigma above normal). 62.6% of re-presented payments recovered, so the retry path was doing its job.
- Decline code Z9 (Insufficient funds) fired 197 times — 1.669% of attempts against a trailing 1.303%. Owner: Customer.
- Decline code UX (Mandate execution outside permitted window) fired 17 times — 0.144% of attempts against a trailing 0.083%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 197 | 1.669% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 156 | 1.321% | 1.030% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.313% | 0.393% |
| U30 | Debit failed at remitter bank | technical | Issuer | 35 | 0.296% | 0.212% |
| XH | Account does not exist / frozen | business | Issuer | 26 | 0.220% | 0.212% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 19 | 0.161% | 0.109% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.152% | 0.199% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.144% | 0.083% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 89 | 81 |
| Auto-reversals | 21 | 28 |
| Disputes / chargebacks | 19 | 11 |
| Value returned | ₹1.43 L | ₹1.55 L |

## Customer behaviour

9,966 distinct customers transacted (−5.1% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,093 | 3,480 | 1.13 | 95.37% | ₹1,302 |
| power | 2,139 | 2,812 | 1.31 | 94.56% | ₹2,182 |
| merchant_heavy | 2,270 | 2,706 | 1.19 | 95.38% | ₹1,196 |
| small_ticket | 1,475 | 1,768 | 1.20 | 95.36% | ₹518 |
| occasional | 776 | 814 | 1.05 | 94.35% | ₹1,433 |
| new | 192 | 204 | 1.06 | 94.12% | ₹812 |
| dormant_returning | 21 | 21 | 1.00 | 95.24% | ₹827 |

## Operational events

- **INC-PSP-0027** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MAINT-0087** (Sev-3) — Union Bank of India scheduled CBS maintenance, scoped to Union Bank of India between 01:00 and 05:00. Union Bank of India runs its announced core-banking maintenance slot every 35 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0050** (Sev-3) — Food Delivery cashback campaign, scoped to 5814. A cashback campaign across Food Delivery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 156 times — 1.321% of attempts against a trailing 1.030%. Owner: Customer.
- Decline code Z9 (Insufficient funds) fired 197 times — 1.669% of attempts against a trailing 1.303%. Owner: Customer.
- Region North ran at 94.57% success on 3,022 attempts (25.6% of the day), 1.14pp down its own 28-day median.
- Category Mobility ran at 95.59% success on 816 attempts (10.6% of the day), 1.15pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 29% across the trailing window to 343 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

28 April was an incident day: INC-PSP-0027 was live and the rail closed at 95.09% success against a 95.74% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,805, successes=11,225, failed=570, pending=10, settled_value_inr=16,166,555.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZM; count=156; rate_pct=1.32; trailing_rate_pct=1.03; owner=Customer; z=3.27
- failures: retries=230; retry_share_pct=1.95; recovery_pct=62.61; z=2.68
- failures: failure_code=Z9; count=197; rate_pct=1.67; trailing_rate_pct=1.3; owner=Customer; z=2.11
- incidents: event_id=INC-PSP-0027; kind=psp_degradation; severity=Sev-2; window=2026-04-27 to 2026-04-30; success_impact_pp=-11.27; volume_impact_pct=-17.63
- geography: region=North; attempts=3,022; success_rate=94.57; own_median=95.72; z=-2.09
- categories: mcc_category=Mobility; attempts=816; success_rate=95.59; own_median=96.73; z=-3.09
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- products: product_name=UPI Circle; attempts=343; window_growth_pct=29; success_rate=95.63
- failures: failure_code=UX; count=17; rate_pct=0.14; trailing_rate_pct=0.08; owner=PSP; z=2.1
- incidents: event_id=MAINT-0087; kind=maintenance_window; severity=Sev-3; window=2026-01-13 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55

Refs: enterprise_data/warehouse/transactions, RPT-D113-DAILY, enterprise_data/warehouse/reference/incidents.parquet
