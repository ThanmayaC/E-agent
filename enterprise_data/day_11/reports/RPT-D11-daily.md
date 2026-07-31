---
id: RPT-D11-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-15T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 15 Jan 2026)

**Report ID:** RPT-D11-DAILY · **Day 11 of 206** · **Derived from:** 9,255 transaction rows queried live from the warehouse

## Summary

The rail took **9,255 payment attempts** on Thursday 15 January 2026 (Working day) and settled **₹1.04 Cr** across 8,834 successful payments. Volume was −16.9% on yesterday and −9.6% on the same weekday last week. Success closed at **95.45%**, in line with the trailing 28-day median of 95.46%.

Attempt volume ran 6.8 standard deviations down its trailing 28-day median at 9,255, 9.6% down on the same weekday last week. Region South carried 2,369 attempts, 24% down its trailing median and 25.6% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,255 | −16.9% | −9.6% | 10,374 |
| Successful payments | 8,834 | −17.2% | −9.6% | 9,886 |
| Success rate | 95.45% | −0.39pp | −0.02pp | 95.29% |
| Settled value | ₹1.04 Cr | −20.8% | −13.7% | ₹1.18 Cr |
| Average ticket | ₹1,177 | −4.3% | −4.5% | ₹1,195 |
| Technical declines | 0.411% | −0.15pp | −0.10pp | 0.584% |
| Business declines | 3.598% | +0.52pp | +0.36pp | 3.452% |
| Risk declines | 0.086% | −0.00pp | −0.09pp | 0.134% |
| Timeout declines | 0.303% | −0.00pp | −0.13pp | 0.396% |
| Retry share | 1.30% | −0.04pp | −0.01pp | 1.42% |
| Latency p95 | 1,245 ms | +1.8% | +0.3% | 1,241 ms |
| Active customers | 7,940 | −14.9% | −9.0% | 8,791 |
| Active merchants | 1,168 | −3.2% | −3.5% | 1,204 |

## What moved

- Attempt volume ran 6.8 standard deviations down its trailing 28-day median at 9,255, 9.6% down on the same weekday last week.
- Region South carried 2,369 attempts, 24% down its trailing median and 25.6% of the day's volume.
- App Google Pay carried 3,027 attempts, 13% down its trailing median and 32.7% of the day's volume.
- Settled value moved down while volume moved down — average ticket at ₹1,177 against a trailing ₹1,209, so the day's shape is a mix shift rather than a demand shift.
- Issuer State Bank of India carried 2,847 attempts, 15% down its trailing median and 30.8% of the day's volume.
- Product UPI Person to Person carried 3,496 attempts, 13% down its trailing median and 37.8% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,496 | 37.8% | 94.62% | ₹38.21 L | −13.1% |
| UPI Person to Merchant | 2,822 | 30.5% | 95.85% | ₹26.10 L | −7.2% |
| UPI QR Payments | 1,394 | 15.1% | 96.99% | ₹5.90 L | −22.6% |
| UPI Lite | 626 | 6.8% | 98.88% | ₹54,991 | −8.4% |
| UPI AutoPay | 281 | 3.0% | 88.97% | ₹4.20 L | −7.6% |
| RuPay Credit on UPI | 164 | 1.8% | 95.12% | ₹8.25 L | −12.5% |
| Credit on UPI | 124 | 1.3% | 91.94% | ₹7.16 L | −15.1% |
| UPI Circle | 92 | 1.0% | 97.83% | ₹62,655 | +0.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,847 | 94.91% | 95.23% | ₹32.58 L | normal |
| HDFC Bank | 1,030 | 96.50% | 96.17% | ₹9.81 L | normal |
| Bank of Baroda | 717 | 93.72% | 95.23% | ₹10.33 L | normal |
| Axis Bank | 620 | 94.35% | 95.41% | ₹7.03 L | ⚠ outlier |
| Union Bank of India | 610 | 96.07% | 95.09% | ₹7.66 L | normal |
| Punjab National Bank | 565 | 94.69% | 95.51% | ₹5.76 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,363 | 95.62% | 95.51% | ₹48.00 L | normal |
| Google Pay | 3,027 | 95.24% | 95.45% | ₹35.60 L | normal |
| Paytm | 801 | 95.38% | 94.68% | ₹8.57 L | normal |
| Navi | 322 | 95.96% | 95.46% | ₹4.36 L | normal |
| SuperMoney | 169 | 98.82% | 95.93% | ₹2.31 L | ⚠ outlier |
| BHIM | 109 | 90.83% | 95.41% | ₹1.05 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,536 | 96.29% | ₹28.18 L |
| Food & Beverage | 1,346 | 97.33% | ₹6.98 L |
| Bills | 582 | 96.05% | ₹5.82 L |
| Mobility | 535 | 97.76% | ₹2.88 L |
| Healthcare | 306 | 94.77% | ₹2.02 L |
| Digital | 184 | 91.85% | ₹86,066 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| North | 2,424 | 26.2% | 95.50% | ₹25.34 L |
| West | 2,403 | 26.0% | 95.05% | ₹25.14 L |
| South | 2,369 | 25.6% | 95.74% | ₹30.92 L |
| East | 1,135 | 12.3% | 95.33% | ₹15.02 L |
| Central | 924 | 10.0% | 95.78% | ₹7.59 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 27 | 96.30% | ₹2.02 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 95.08% | ₹2.02 L |
| Rapid Bazaar | Key Account | Retail | 275 | 95.64% | ₹1.31 L |
| Hampi Stores 2298 | Key Account | Retail | 83 | 96.39% | ₹78,342 |
| Malabar Supermart 1818 | Large | Retail | 45 | 95.56% | ₹73,200 |
| Trinetra Restaurant | Large | Food & Beverage | 22 | 100.00% | ₹61,104 |
| Yamuna Restaurant | Key Account | Food & Beverage | 50 | 94.00% | ₹60,173 |
| Urban Boutique | Key Account | Retail | 71 | 92.96% | ₹52,260 |

## Failure analysis

Of 407 declined attempts, 333 were business declines (3.598% of attempts — balances, PINs and limits), 38 technical (0.411%), 28 timeouts (0.303%) and 8 risk declines (0.086%).

120 attempts were re-presentations of an earlier failure (1.30% of the day); 61.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 144 | 1.556% | 1.454% |
| ZM | Invalid UPI PIN | business | Customer | 105 | 1.135% | 1.091% |
| ZA | Transaction declined by customer | business | Customer | 38 | 0.411% | 0.366% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.238% | 0.261% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.238% | 0.249% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.184% | 0.186% |
| UX | Mandate execution outside permitted window | business | PSP | 10 | 0.108% | 0.078% |
| ZX | Mandate not found or revoked | business | PSP | 10 | 0.108% | 0.074% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 49 | 20 |
| Auto-reversals | 23 | 23 |
| Disputes / chargebacks | 3 | 0 |
| Value returned | ₹1.42 L | ₹45,159 |

## Customer behaviour

7,940 distinct customers transacted (−10.8% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,424 | 2,708 | 1.12 | 95.38% | ₹1,238 |
| power | 1,728 | 2,221 | 1.29 | 95.27% | ₹1,519 |
| merchant_heavy | 1,817 | 2,101 | 1.16 | 95.86% | ₹866 |
| small_ticket | 1,185 | 1,399 | 1.18 | 95.43% | ₹529 |
| occasional | 625 | 658 | 1.05 | 95.44% | ₹1,332 |
| new | 135 | 141 | 1.04 | 92.91% | ₹1,538 |
| dormant_returning | 26 | 27 | 1.04 | 100.00% | ₹765 |

## Operational events

- **INC-PSP-0034** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.

## Risks and opportunities

### Risks

- 3 disputes were raised, 2.9 sigma above the trailing median of 0.
- Category Services ran at 90.32% success on 93 attempts (1.6% of the day), 3.53pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

15 January was an incident day: INC-PSP-0034 was live and the rail closed at 95.45% success against a 95.46% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-15` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,255, successes=8,834, failed=407, pending=14, settled_value_inr=10,398,911.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- headline: attempts=9,255; trailing_median=10,492.5; z=-6.76
- geography: region=South; attempts=2,369; own_median=3,132; z=-6.95
- psps: payer_psp=Google Pay; attempts=3,027; own_median=3,466; z=-6.04
- headline: value_inr=10,398,911; avg_ticket=1,177.15; trailing_avg_ticket=1,208.71
- adjustments: chargebacks=3; trailing_median=0; z=2.93
- banks: payer_bank=State Bank of India; attempts=2,847; own_median=3,366; z=-5.34
- products: product_name=UPI Person to Person; attempts=3,496; own_median=4,024; z=-4.63
- psps: payer_psp=PhonePe; attempts=4,363; own_median=5,004.5; z=-3.59
- incidents: event_id=INC-PSP-0034; kind=psp_degradation; severity=Sev-2; window=2026-01-12 to 2026-01-15; success_impact_pp=-6.55; volume_impact_pct=-10.26
- products: product_name=UPI QR Payments; attempts=1,394; own_median=1,800.5; z=-4.94

Refs: enterprise_data/warehouse/transactions, RPT-D10-DAILY, enterprise_data/warehouse/reference/incidents.parquet
