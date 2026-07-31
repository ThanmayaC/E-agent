---
id: RPT-D12-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 16 Jan 2026)

**Report ID:** RPT-D12-DAILY · **Day 12 of 206** · **Derived from:** 9,712 transaction rows queried live from the warehouse

## Summary

The rail took **9,712 payment attempts** on Friday 16 January 2026 (Working day) and settled **₹1.17 Cr** across 9,217 successful payments. Volume was +4.9% on yesterday and −6.5% on the same weekday last week. Success closed at **94.90%**, below the trailing 28-day median of 95.46%.

Decline code UX (Mandate execution outside permitted window) fired 19 times — 0.196% of attempts against a trailing 0.078%. Owner: PSP. Attempt volume ran 3.8 standard deviations down its trailing 28-day median at 9,712, 6.5% down on the same weekday last week.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,712 | +4.9% | −6.5% | 10,319 |
| Successful payments | 9,217 | +4.3% | −7.3% | 9,830 |
| Success rate | 94.90% | −0.55pp | −0.77pp | 95.25% |
| Settled value | ₹1.17 Cr | +12.1% | +3.7% | ₹1.18 Cr |
| Average ticket | ₹1,265 | +7.5% | +11.8% | ₹1,200 |
| Technical declines | 0.783% | +0.37pp | +0.21pp | 0.601% |
| Business declines | 3.614% | +0.02pp | +0.54pp | 3.466% |
| Risk declines | 0.134% | +0.05pp | −0.03pp | 0.134% |
| Timeout declines | 0.422% | +0.12pp | −0.00pp | 0.398% |
| Retry share | 1.45% | +0.16pp | +0.25pp | 1.42% |
| Latency p95 | 1,246 ms | +0.1% | +0.4% | 1,241 ms |
| Active customers | 8,276 | +4.2% | −5.7% | 8,748 |
| Active merchants | 1,184 | +1.4% | +0.8% | 1,203 |

## What moved

- Attempt volume ran 3.8 standard deviations down its trailing 28-day median at 9,712, 6.5% down on the same weekday last week.
- Success rate closed at 94.90%, 0.55pp down the trailing median — a 1.6-sigma move.
- Region East ran at 94.10% success on 1,101 attempts (11.3% of the day), 1.48pp down its own 28-day median.
- Region South carried 2,794 attempts, 11% down its trailing median and 28.8% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,732 | 38.4% | 93.57% | ₹38.16 L | −7.2% |
| UPI Person to Merchant | 2,739 | 28.2% | 96.09% | ₹25.62 L | −8.6% |
| UPI QR Payments | 1,615 | 16.6% | 95.67% | ₹6.55 L | −9.3% |
| UPI Lite | 584 | 6.0% | 97.95% | ₹51,050 | −13.0% |
| UPI AutoPay | 286 | 2.9% | 90.91% | ₹4.53 L | −5.9% |
| RuPay Credit on UPI | 204 | 2.1% | 95.59% | ₹8.04 L | +11.5% |
| Credit on UPI | 162 | 1.7% | 95.06% | ₹16.92 L | +11.7% |
| UPI Circle | 89 | 0.9% | 93.26% | ₹57,683 | −3.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,096 | 94.61% | 95.12% | ₹40.07 L | normal |
| HDFC Bank | 1,089 | 96.14% | 96.18% | ₹11.87 L | normal |
| Bank of Baroda | 719 | 94.44% | 94.72% | ₹6.95 L | normal |
| Union Bank of India | 665 | 93.83% | 95.16% | ₹7.89 L | normal |
| Axis Bank | 593 | 96.80% | 95.39% | ₹6.17 L | ⚠ outlier |
| ICICI Bank | 560 | 96.43% | 95.32% | ₹7.26 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,577 | 95.08% | 95.55% | ₹55.89 L | normal |
| Google Pay | 3,274 | 94.69% | 95.34% | ₹36.90 L | normal |
| Paytm | 756 | 93.92% | 94.78% | ₹11.07 L | normal |
| Navi | 353 | 95.18% | 95.89% | ₹3.51 L | normal |
| SuperMoney | 174 | 96.55% | 96.10% | ₹2.37 L | normal |
| BHIM | 99 | 95.96% | 95.33% | ₹1.26 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,574 | 96.00% | ₹27.10 L |
| Food & Beverage | 1,467 | 96.11% | ₹7.25 L |
| Mobility | 585 | 96.92% | ₹3.78 L |
| Bills | 581 | 95.87% | ₹6.60 L |
| Healthcare | 315 | 96.19% | ₹4.09 L |
| Digital | 165 | 92.73% | ₹61,894 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,794 | 28.8% | 95.17% | ₹34.31 L |
| North | 2,493 | 25.7% | 94.46% | ₹25.22 L |
| West | 2,490 | 25.6% | 95.18% | ₹35.75 L |
| East | 1,101 | 11.3% | 94.10% | ₹13.11 L |
| Central | 834 | 8.6% | 95.56% | ₹8.20 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 27 | 88.89% | ₹2.38 L |
| Rapid Bazaar | Key Account | Retail | 263 | 97.72% | ₹1.69 L |
| Vasant Wardrobe | Key Account | Retail | 56 | 100.00% | ₹1.20 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 73 | 93.15% | ₹92,907 |
| Hampi Stores 2298 | Key Account | Retail | 99 | 93.94% | ₹77,197 |
| Ujjwal Water Board | Key Account | Bills | 22 | 100.00% | ₹72,792 |
| Urban Boutique | Key Account | Retail | 74 | 97.30% | ₹51,571 |
| Girnar Connect | Key Account | Bills | 106 | 93.40% | ₹44,661 |

## Failure analysis

Of 481 declined attempts, 351 were business declines (3.614% of attempts — balances, PINs and limits), 76 technical (0.783%), 41 timeouts (0.422%) and 13 risk declines (0.134%).

141 attempts were re-presentations of an earlier failure (1.45% of the day); 75.9% of them succeeded.

- Decline code UX (Mandate execution outside permitted window) fired 19 times — 0.196% of attempts against a trailing 0.078%. Owner: PSP.
- Decline code U30 (Debit failed at remitter bank) fired 32 times — 0.329% of attempts against a trailing 0.260%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 146 | 1.503% | 1.459% |
| ZM | Invalid UPI PIN | business | Customer | 96 | 0.988% | 1.095% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.484% | 0.371% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.329% | 0.260% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.309% | 0.238% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 19 | 0.196% | 0.131% |
| UX | Mandate execution outside permitted window | business | PSP | 19 | 0.196% | 0.078% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.185% | 0.152% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 60 | 22 |
| Auto-reversals | 21 | 23 |
| Disputes / chargebacks | 3 | 0 |
| Value returned | ₹64,902 | ₹50,185 |

## Customer behaviour

8,276 distinct customers transacted (−6.8% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,536 | 2,829 | 1.12 | 94.66% | ₹1,184 |
| power | 1,760 | 2,263 | 1.29 | 94.56% | ₹1,910 |
| merchant_heavy | 1,867 | 2,201 | 1.18 | 95.27% | ₹865 |
| small_ticket | 1,257 | 1,515 | 1.21 | 95.31% | ₹558 |
| occasional | 648 | 681 | 1.05 | 95.59% | ₹1,487 |
| new | 175 | 189 | 1.08 | 92.06% | ₹997 |
| dormant_returning | 33 | 34 | 1.03 | 97.06% | ₹1,109 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Decline code UX (Mandate execution outside permitted window) fired 19 times — 0.196% of attempts against a trailing 0.078%. Owner: PSP.
- 3 disputes were raised, 2.5 sigma above the trailing median of 0.
- Success rate closed at 94.90%, 0.55pp down the trailing median — a 1.6-sigma move.
- Decline code U30 (Debit failed at remitter bank) fired 32 times — 0.329% of attempts against a trailing 0.260%. Owner: Issuer.
- Region East ran at 94.10% success on 1,101 attempts (11.3% of the day), 1.48pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 16 January: success came in 0.55pp below baseline at 94.90% on 9,712 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,712, successes=9,217, failed=481, pending=14, settled_value_inr=11,659,497.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=UX; count=19; rate_pct=0.2; trailing_rate_pct=0.08; owner=PSP; z=8.59
- headline: attempts=9,712; trailing_median=10,484; z=-3.8
- adjustments: chargebacks=3; trailing_median=0; z=2.47
- headline: success_rate=94.9; trailing_median=95.46; z=-1.59
- failures: failure_code=U30; count=32; rate_pct=0.33; trailing_rate_pct=0.26; owner=Issuer; z=2.12
- geography: region=East; attempts=1,101; success_rate=94.1; own_median=95.58; z=-2.92
- geography: region=South; attempts=2,794; own_median=3,123; z=-2.39
- categories: mcc_category=Mobility; attempts=585; own_median=662; z=-3.06
- banks: payer_bank=Axis Bank; attempts=593; success_rate=96.8; own_median=95.39; z=2.65
- banks: payer_bank=HDFC Bank; attempts=1,089; own_median=1,148; z=-2.34

Refs: enterprise_data/warehouse/transactions, RPT-D11-DAILY, enterprise_data/warehouse/reference/incidents.parquet
