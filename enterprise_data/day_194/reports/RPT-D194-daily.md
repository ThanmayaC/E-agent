---
id: RPT-D194-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 17 Jul 2026)

**Report ID:** RPT-D194-DAILY · **Day 194 of 206** · **Derived from:** 15,586 transaction rows queried live from the warehouse

## Summary

The rail took **15,586 payment attempts** on Friday 17 July 2026 (Working day) and settled **₹2.17 Cr** across 15,003 successful payments. Volume was +6.8% on yesterday and −10.5% on the same weekday last week. Success closed at **96.26%**, in line with the trailing 28-day median of 96.13%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,586 | +6.8% | −10.5% | 16,391 |
| Successful payments | 15,003 | +7.1% | −10.2% | 15,751 |
| Success rate | 96.26% | +0.21pp | +0.38pp | 96.13% |
| Settled value | ₹2.17 Cr | +8.6% | +0.4% | ₹2.13 Cr |
| Average ticket | ₹1,446 | +1.4% | +11.7% | ₹1,356 |
| Technical declines | 0.417% | +0.09pp | −0.16pp | 0.461% |
| Business declines | 2.932% | −0.25pp | −0.06pp | 2.807% |
| Risk declines | 0.090% | −0.03pp | −0.06pp | 0.105% |
| Timeout declines | 0.199% | −0.04pp | −0.11pp | 0.411% |
| Retry share | 1.20% | +0.19pp | −0.24pp | 1.35% |
| Latency p95 | 1,306 ms | −0.5% | −2.1% | 1,305 ms |
| Active customers | 12,816 | +4.9% | −8.0% | 13,308 |
| Active merchants | 1,618 | +2.1% | −1.0% | 1,617 |

## What moved

- Issuer Union Bank of India ran at 97.86% success on 1,075 attempts (6.9% of the day), 1.68pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,929 | 31.6% | 95.37% | ₹51.94 L | +7.2% |
| UPI Person to Merchant | 3,818 | 24.5% | 95.89% | ₹36.73 L | +5.5% |
| UPI QR Payments | 2,143 | 13.7% | 97.06% | ₹10.34 L | −17.0% |
| UPI Lite | 2,051 | 13.2% | 99.12% | ₹1.92 L | −20.1% |
| UPI Circle | 782 | 5.0% | 98.34% | ₹5.98 L | −3.2% |
| Credit on UPI | 627 | 4.0% | 94.90% | ₹50.83 L | +30.9% |
| UPI AutoPay | 367 | 2.4% | 92.10% | ₹6.89 L | −2.9% |
| RuPay Credit on UPI | 332 | 2.1% | 96.08% | ₹15.12 L | −13.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,940 | 96.15% | 96.19% | ₹72.19 L | normal |
| HDFC Bank | 1,756 | 96.41% | 96.39% | ₹25.56 L | normal |
| Bank of Baroda | 1,227 | 95.68% | 96.35% | ₹17.83 L | normal |
| Union Bank of India | 1,075 | 97.86% | 96.18% | ₹16.90 L | ⚠ outlier |
| Axis Bank | 950 | 97.37% | 96.17% | ₹14.01 L | normal |
| Punjab National Bank | 929 | 95.48% | 95.92% | ₹9.98 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,339 | 96.20% | 96.21% | ₹1.09 Cr | normal |
| Google Pay | 5,177 | 96.47% | 96.09% | ₹70.89 L | normal |
| Paytm | 1,300 | 96.15% | 96.24% | ₹14.94 L | normal |
| Navi | 576 | 95.31% | 96.37% | ₹7.94 L | normal |
| SuperMoney | 292 | 96.23% | 96.25% | ₹3.84 L | normal |
| BHIM | 153 | 94.77% | 95.87% | ₹2.11 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,531 | 96.62% | ₹60.20 L |
| Food & Beverage | 2,609 | 97.28% | ₹12.55 L |
| Mobility | 1,213 | 98.27% | ₹7.04 L |
| Bills | 1,007 | 95.73% | ₹10.46 L |
| Healthcare | 589 | 98.64% | ₹11.17 L |
| Digital | 226 | 95.58% | ₹1.19 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,681 | 30.0% | 96.13% | ₹69.36 L |
| North | 4,017 | 25.8% | 96.39% | ₹48.90 L |
| West | 3,694 | 23.7% | 96.43% | ₹47.92 L |
| East | 1,774 | 11.4% | 96.05% | ₹34.13 L |
| Central | 1,420 | 9.1% | 96.13% | ₹16.67 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 42 | 92.86% | ₹3.53 L |
| Rapid Bazaar | Key Account | Retail | 447 | 97.32% | ₹2.77 L |
| Vasant Wardrobe | Key Account | Retail | 84 | 94.05% | ₹2.69 L |
| Hampi Stores 2298 | Key Account | Retail | 117 | 97.44% | ₹1.69 L |
| Kaveri Trading | Large | Retail | 55 | 94.55% | ₹1.07 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 95.59% | ₹79,328 |
| Girnar Connect | Key Account | Bills | 157 | 98.09% | ₹72,935 |
| Urban Boutique | Key Account | Retail | 111 | 98.20% | ₹65,815 |

## Failure analysis

Of 567 declined attempts, 457 were business declines (2.932% of attempts — balances, PINs and limits), 65 technical (0.417%), 31 timeouts (0.199%) and 14 risk declines (0.090%).

187 attempts were re-presentations of an earlier failure (1.20% of the day); 60.4% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 176 | 1.129% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 171 | 1.097% | 0.978% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.334% | 0.323% |
| U30 | Debit failed at remitter bank | technical | Issuer | 34 | 0.218% | 0.174% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.173% | 0.185% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.109% | 0.083% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 16 | 0.103% | 0.131% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.083% | 0.088% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 112 | 113 |
| Auto-reversals | 15 | 24 |
| Disputes / chargebacks | 19 | 15 |
| Value returned | ₹2.21 L | ₹1.72 L |

## Customer behaviour

12,816 distinct customers transacted (−2.2% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,984 | 4,632 | 1.16 | 95.96% | ₹1,457 |
| power | 2,771 | 3,735 | 1.35 | 96.25% | ₹2,147 |
| merchant_heavy | 2,931 | 3,570 | 1.22 | 96.41% | ₹1,004 |
| small_ticket | 1,926 | 2,382 | 1.24 | 96.47% | ₹609 |
| occasional | 954 | 995 | 1.04 | 96.48% | ₹1,637 |
| new | 220 | 240 | 1.09 | 96.67% | ₹989 |
| dormant_returning | 30 | 32 | 1.07 | 96.88% | ₹877 |

## Operational events

- **INC-BANK-0020** (Sev-2) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 24:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Issuer IndusInd Bank ran at 93.80% success on 355 attempts (2.3% of the day), 2.19pp down its own 28-day median.
- Category Travel ran at 89.78% success on 137 attempts (1.3% of the day), 5.30pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

17 July was an incident day: INC-BANK-0020 was live and the rail closed at 96.26% success against a 96.13% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,586, successes=15,003, failed=567, pending=16, settled_value_inr=21,699,274.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0020; kind=bank_outage; severity=Sev-2; window=2026-07-17 to 2026-07-19; success_impact_pp=-11.07; volume_impact_pct=-9.82
- banks: payer_bank=Union Bank of India; attempts=1,075; success_rate=97.86; own_median=96.18; z=3.62
- categories: mcc_category=Healthcare; attempts=589; success_rate=98.64; own_median=97.15; z=2.19
- banks: payer_bank=IndusInd Bank; attempts=355; success_rate=93.8; own_median=95.99; z=-2.52
- categories: mcc_category=Travel; attempts=137; success_rate=89.78; own_median=95.08; z=-2.55

Refs: enterprise_data/warehouse/transactions, RPT-D193-DAILY, enterprise_data/warehouse/reference/incidents.parquet
