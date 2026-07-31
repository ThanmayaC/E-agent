---
id: RPT-D18-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-22T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 22 Jan 2026)

**Report ID:** RPT-D18-DAILY · **Day 18 of 206** · **Derived from:** 11,096 transaction rows queried live from the warehouse

## Summary

The rail took **11,096 payment attempts** on Thursday 22 January 2026 (Republic Day Sale (build-up)) and settled **₹1.22 Cr** across 10,580 successful payments. Volume was +10.9% on yesterday and +19.9% on the same weekday last week. Success closed at **95.35%**, in line with the trailing 28-day median of 95.13%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,096 | +10.9% | +19.9% | 10,271 |
| Successful payments | 10,580 | +11.3% | +19.8% | 9,770 |
| Success rate | 95.35% | +0.35pp | −0.10pp | 95.11% |
| Settled value | ₹1.22 Cr | +10.6% | +17.4% | ₹1.16 Cr |
| Average ticket | ₹1,153 | −0.7% | −2.0% | ₹1,185 |
| Technical declines | 0.514% | −0.09pp | +0.10pp | 0.631% |
| Business declines | 3.479% | −0.28pp | −0.12pp | 3.603% |
| Risk declines | 0.126% | −0.01pp | +0.04pp | 0.131% |
| Timeout declines | 0.397% | −0.03pp | +0.09pp | 0.397% |
| Retry share | 1.40% | −0.15pp | +0.10pp | 1.50% |
| Latency p95 | 1,262 ms | +1.0% | +1.4% | 1,248 ms |
| Active customers | 9,309 | +9.6% | +17.2% | 8,709 |
| Active merchants | 1,207 | +1.7% | +3.3% | 1,200 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,620 | 41.6% | 94.61% | ₹50.40 L | +15.9% |
| UPI Person to Merchant | 3,098 | 27.9% | 95.71% | ₹31.80 L | +6.0% |
| UPI QR Payments | 1,674 | 15.1% | 97.01% | ₹7.49 L | +1.5% |
| UPI Lite | 661 | 6.0% | 98.64% | ₹62,643 | +3.8% |
| UPI AutoPay | 292 | 2.6% | 88.36% | ₹4.88 L | −4.6% |
| RuPay Credit on UPI | 245 | 2.2% | 96.73% | ₹9.15 L | +27.6% |
| Credit on UPI | 130 | 1.2% | 96.15% | ₹8.51 L | −9.1% |
| UPI Circle | 109 | 1.0% | 89.91% | ₹73,082 | +18.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,487 | 95.30% | 94.89% | ₹38.66 L | normal |
| HDFC Bank | 1,192 | 95.89% | 95.92% | ₹12.69 L | normal |
| Bank of Baroda | 870 | 95.86% | 94.67% | ₹8.37 L | normal |
| Union Bank of India | 809 | 93.82% | 94.72% | ₹9.45 L | normal |
| Axis Bank | 712 | 94.80% | 95.39% | ₹8.45 L | normal |
| ICICI Bank | 647 | 96.91% | 95.71% | ₹5.82 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,239 | 95.09% | 95.24% | ₹55.59 L | normal |
| Google Pay | 3,684 | 95.55% | 95.24% | ₹41.38 L | normal |
| Paytm | 881 | 94.44% | 94.54% | ₹11.09 L | normal |
| Navi | 391 | 96.42% | 95.18% | ₹4.29 L | normal |
| SuperMoney | 235 | 95.32% | 95.75% | ₹2.66 L | normal |
| BHIM | 130 | 94.62% | 95.50% | ₹1.20 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,912 | 95.84% | ₹35.39 L |
| Food & Beverage | 1,478 | 97.02% | ₹7.98 L |
| Mobility | 652 | 97.70% | ₹3.40 L |
| Bills | 582 | 95.19% | ₹5.56 L |
| Healthcare | 350 | 95.71% | ₹2.48 L |
| Digital | 192 | 94.79% | ₹1.51 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,259 | 29.4% | 95.12% | ₹35.73 L |
| North | 2,858 | 25.8% | 95.35% | ₹32.54 L |
| West | 2,669 | 24.1% | 95.20% | ₹29.03 L |
| East | 1,370 | 12.3% | 95.69% | ₹14.39 L |
| Central | 940 | 8.5% | 96.06% | ₹10.35 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 100.00% | ₹2.00 L |
| Vasant Wardrobe | Key Account | Retail | 104 | 97.12% | ₹1.99 L |
| Rapid Bazaar | Key Account | Retail | 275 | 96.73% | ₹1.18 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 89 | 96.63% | ₹1.11 L |
| Ujjwal Water Board | Key Account | Bills | 27 | 100.00% | ₹88,730 |
| Hampi Stores 2298 | Key Account | Retail | 122 | 95.90% | ₹63,791 |
| Urban Boutique | Key Account | Retail | 90 | 95.56% | ₹63,740 |
| Girnar Connect | Key Account | Bills | 106 | 96.23% | ₹54,744 |

## Failure analysis

Of 501 declined attempts, 386 were business declines (3.479% of attempts — balances, PINs and limits), 57 technical (0.514%), 44 timeouts (0.397%) and 14 risk declines (0.126%).

155 attempts were re-presentations of an earlier failure (1.40% of the day); 70.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 171 | 1.541% | 1.503% |
| ZM | Invalid UPI PIN | business | Customer | 122 | 1.099% | 1.130% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.324% | 0.385% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.216% | 0.267% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.207% | 0.262% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.207% | 0.184% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.162% | 0.183% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.153% | 0.140% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 61 | 40 |
| Auto-reversals | 28 | 23 |
| Disputes / chargebacks | 2 | 0 |
| Value returned | ₹1.77 L | ₹85,277 |

## Customer behaviour

9,309 distinct customers transacted (+6.1% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,830 | 3,208 | 1.13 | 95.48% | ₹1,194 |
| power | 1,979 | 2,601 | 1.31 | 95.35% | ₹1,482 |
| merchant_heavy | 2,079 | 2,501 | 1.20 | 95.20% | ₹949 |
| small_ticket | 1,435 | 1,744 | 1.22 | 95.30% | ₹488 |
| occasional | 748 | 792 | 1.06 | 94.57% | ₹1,234 |
| new | 193 | 205 | 1.06 | 98.05% | ₹1,284 |
| dormant_returning | 45 | 45 | 1.00 | 97.78% | ₹1,206 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Product UPI Circle ran at 89.91% success on 109 attempts (1.0% of the day), 7.71pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

22 January was an unremarkable day, and that is the finding: 11,096 attempts, 95.35% success, ₹1.22 Cr settled, every dimension inside its own 28-day band. Days like this are the ones to spend on capacity and roadmap work, because nothing is competing for the operations bandwidth.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-22` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,096, successes=10,580, failed=501, pending=15, settled_value_inr=12,203,615.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=109; success_rate=89.91; own_median=97.62; z=-4.06
- categories: mcc_category=Services; attempts=120; own_median=90; z=3.37
- banks: payer_bank=Kotak Mahindra Bank; attempts=401; own_median=351; z=2.41
- psps: payer_psp=SuperMoney; attempts=235; own_median=205; z=2.25
- products: product_name=UPI Circle; attempts=109; own_median=92; z=2.29

Refs: enterprise_data/warehouse/transactions, RPT-D17-DAILY, enterprise_data/warehouse/reference/incidents.parquet
