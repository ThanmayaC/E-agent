---
id: RPT-D13-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-17T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 17 Jan 2026)

**Report ID:** RPT-D13-DAILY · **Day 13 of 206** · **Derived from:** 11,442 transaction rows queried live from the warehouse

## Summary

The rail took **11,442 payment attempts** on Saturday 17 January 2026 (Weekend) and settled **₹1.22 Cr** across 10,885 successful payments. Volume was +17.8% on yesterday and −0.1% on the same weekday last week. Success closed at **95.13%**, below the trailing 28-day median of 95.45%.

Category Food & Beverage carried 1,793 attempts, 22% up its trailing median and 24.9% of the day's volume. Attempt volume ran 3.4 standard deviations up its trailing 28-day median at 11,442, 0.1% down on the same weekday last week.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,442 | +17.8% | −0.1% | 10,405 |
| Successful payments | 10,885 | +18.1% | −0.4% | 9,912 |
| Success rate | 95.13% | +0.23pp | −0.30pp | 95.24% |
| Settled value | ₹1.22 Cr | +4.4% | +1.4% | ₹1.18 Cr |
| Average ticket | ₹1,118 | −11.6% | +1.8% | ₹1,194 |
| Technical declines | 0.804% | +0.02pp | +0.24pp | 0.617% |
| Business declines | 3.443% | −0.17pp | +0.00pp | 3.464% |
| Risk declines | 0.114% | −0.02pp | +0.05pp | 0.132% |
| Timeout declines | 0.402% | −0.02pp | +0.04pp | 0.398% |
| Retry share | 1.38% | −0.07pp | +0.08pp | 1.42% |
| Latency p95 | 1,200 ms | −3.7% | +0.7% | 1,238 ms |
| Active customers | 9,595 | +15.9% | +0.3% | 8,813 |
| Active merchants | 1,252 | +5.7% | +0.8% | 1,206 |

## What moved

- Category Food & Beverage carried 1,793 attempts, 22% up its trailing median and 24.9% of the day's volume.
- Attempt volume ran 3.4 standard deviations up its trailing 28-day median at 11,442, 0.1% down on the same weekday last week.
- Category Bills ran at 94.12% success on 697 attempts (9.7% of the day), 1.93pp down its own 28-day median.
- Issuer HDFC Bank ran at 94.86% success on 1,284 attempts (11.2% of the day), 1.31pp down its own 28-day median.
- Region West carried 2,707 attempts, 8% up its trailing median and 23.7% of the day's volume.
- Product UPI Person to Merchant carried 3,532 attempts, 20% up its trailing median and 30.9% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,238 | 37.0% | 94.45% | ₹42.83 L | +5.5% |
| UPI Person to Merchant | 3,532 | 30.9% | 95.75% | ₹32.56 L | +20.1% |
| UPI QR Payments | 1,863 | 16.3% | 96.14% | ₹7.00 L | +5.7% |
| UPI Lite | 774 | 6.8% | 97.67% | ₹66,845 | +18.3% |
| UPI AutoPay | 312 | 2.7% | 87.18% | ₹4.99 L | +3.7% |
| RuPay Credit on UPI | 159 | 1.4% | 96.86% | ₹8.57 L | −15.2% |
| UPI Circle | 147 | 1.3% | 95.24% | ₹1.26 L | +60.7% |
| Credit on UPI | 109 | 1.0% | 94.50% | ₹8.28 L | −25.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,593 | 94.93% | 95.01% | ₹38.45 L | normal |
| HDFC Bank | 1,284 | 94.86% | 96.17% | ₹14.07 L | ⚠ outlier |
| Bank of Baroda | 854 | 94.38% | 94.59% | ₹9.25 L | normal |
| Union Bank of India | 758 | 94.72% | 95.09% | ₹9.28 L | normal |
| Axis Bank | 724 | 96.27% | 95.41% | ₹6.72 L | normal |
| ICICI Bank | 701 | 96.15% | 95.62% | ₹6.82 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,419 | 95.57% | 95.51% | ₹56.45 L | normal |
| Google Pay | 3,832 | 94.75% | 95.29% | ₹42.26 L | normal |
| Paytm | 898 | 94.88% | 94.68% | ₹10.06 L | normal |
| Navi | 383 | 95.56% | 95.54% | ₹4.46 L | normal |
| SuperMoney | 219 | 93.61% | 96.12% | ₹2.05 L | ⚠ outlier |
| BHIM | 116 | 95.69% | 95.41% | ₹1.07 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,044 | 96.29% | ₹26.29 L |
| Food & Beverage | 1,793 | 95.98% | ₹7.67 L |
| Mobility | 740 | 95.68% | ₹3.91 L |
| Bills | 697 | 94.12% | ₹8.25 L |
| Healthcare | 394 | 95.94% | ₹4.92 L |
| Digital | 198 | 90.40% | ₹88,737 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,424 | 29.9% | 95.06% | ₹36.31 L |
| North | 2,913 | 25.5% | 95.13% | ₹30.18 L |
| West | 2,707 | 23.7% | 95.23% | ₹25.16 L |
| East | 1,360 | 11.9% | 95.22% | ₹20.17 L |
| Central | 1,038 | 9.1% | 94.99% | ₹9.93 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 30 | 93.33% | ₹1.44 L |
| Rapid Bazaar | Key Account | Retail | 339 | 96.46% | ₹1.16 L |
| Urban Boutique | Key Account | Retail | 85 | 94.12% | ₹95,576 |
| Vasant Wardrobe | Key Account | Retail | 66 | 95.45% | ₹82,935 |
| Ujjwal Water Board | Key Account | Bills | 36 | 94.44% | ₹76,593 |
| Hampi Stores 2298 | Key Account | Retail | 96 | 95.83% | ₹69,736 |
| Yamuna Restaurant | Key Account | Food & Beverage | 69 | 92.75% | ₹62,492 |
| Girnar Connect | Key Account | Bills | 113 | 93.81% | ₹52,523 |

## Failure analysis

Of 545 declined attempts, 394 were business declines (3.443% of attempts — balances, PINs and limits), 92 technical (0.804%), 46 timeouts (0.402%) and 13 risk declines (0.114%).

158 attempts were re-presentations of an earlier failure (1.38% of the day); 74.1% of them succeeded.

- Decline code U30 (Debit failed at remitter bank) fired 41 times — 0.358% of attempts against a trailing 0.261%. Owner: Issuer.
- Decline code YA (PSP not available) fired 13 times — 0.114% of attempts against a trailing 0.062%. Owner: PSP.
- Decline code UX (Mandate execution outside permitted window) fired 14 times — 0.122% of attempts against a trailing 0.082%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 157 | 1.372% | 1.460% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 1.189% | 1.091% |
| U30 | Debit failed at remitter bank | technical | Issuer | 41 | 0.358% | 0.261% |
| ZA | Transaction declined by customer | business | Customer | 40 | 0.350% | 0.376% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.262% | 0.251% |
| U28 | Remitter bank unavailable | technical | Issuer | 24 | 0.210% | 0.163% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 21 | 0.184% | 0.137% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.166% | 0.185% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 59 | 24 |
| Auto-reversals | 26 | 22 |
| Disputes / chargebacks | 1 | 0 |
| Value returned | ₹40,432 | ₹57,544 |

## Customer behaviour

9,595 distinct customers transacted (+8.4% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,889 | 3,275 | 1.13 | 95.73% | ₹1,169 |
| power | 1,995 | 2,642 | 1.32 | 94.89% | ₹1,509 |
| merchant_heavy | 2,152 | 2,575 | 1.20 | 94.80% | ₹893 |
| small_ticket | 1,542 | 1,877 | 1.22 | 95.05% | ₹530 |
| occasional | 790 | 829 | 1.05 | 95.30% | ₹1,065 |
| new | 199 | 215 | 1.08 | 92.56% | ₹744 |
| dormant_returning | 28 | 29 | 1.04 | 100.00% | ₹817 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Category Bills ran at 94.12% success on 697 attempts (9.7% of the day), 1.93pp down its own 28-day median.
- Issuer HDFC Bank ran at 94.86% success on 1,284 attempts (11.2% of the day), 1.31pp down its own 28-day median.
- Decline code U30 (Debit failed at remitter bank) fired 41 times — 0.358% of attempts against a trailing 0.261%. Owner: Issuer.
- Decline code YA (PSP not available) fired 13 times — 0.114% of attempts against a trailing 0.062%. Owner: PSP.
- Decline code UX (Mandate execution outside permitted window) fired 14 times — 0.122% of attempts against a trailing 0.082%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

17 January ran on trend at 95.13% success and ₹1.22 Cr settled. The movement worth carrying forward is in merchant categories: category Food & Beverage carried 1,793 attempts, 22% up its trailing median and 24.9% of the day's volume. 7 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-17` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,442, successes=10,885, failed=545, pending=12, settled_value_inr=12,174,514.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Food & Beverage; attempts=1,793; own_median=1,468.5; z=7.3
- headline: attempts=11,442; trailing_median=10,476.5; z=3.43
- categories: mcc_category=Bills; attempts=697; success_rate=94.12; own_median=96.05; z=-4.58
- banks: payer_bank=HDFC Bank; attempts=1,284; success_rate=94.86; own_median=96.17; z=-4.2
- geography: region=West; attempts=2,707; own_median=2,517; z=3.83
- failures: failure_code=U30; count=41; rate_pct=0.36; trailing_rate_pct=0.26; owner=Issuer; z=2.39
- products: product_name=UPI Person to Merchant; attempts=3,532; own_median=2,942; z=2.76
- banks: payer_bank=HDFC Bank; attempts=1,284; own_median=1,141.5; z=4.09
- products: product_name=UPI Circle; attempts=147; own_median=91.5; z=9.36
- failures: failure_code=YA; count=13; rate_pct=0.11; trailing_rate_pct=0.06; owner=PSP; z=2.32

Refs: enterprise_data/warehouse/transactions, RPT-D12-DAILY, enterprise_data/warehouse/reference/incidents.parquet
