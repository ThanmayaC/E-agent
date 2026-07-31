---
id: RPT-D189-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 12 Jul 2026)

**Report ID:** RPT-D189-DAILY · **Day 189 of 206** · **Derived from:** 14,283 transaction rows queried live from the warehouse

## Summary

The rail took **14,283 payment attempts** on Sunday 12 July 2026 (Weekend) and settled **₹1.61 Cr** across 13,701 successful payments. Volume was −12.9% on yesterday and −11.5% on the same weekday last week. Success closed at **95.93%**, in line with the trailing 28-day median of 96.11%.

142 refunds were raised, 3.1 sigma above the trailing median of 110.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,283 | −12.9% | −11.5% | 16,938 |
| Successful payments | 13,701 | −13.0% | −11.4% | 16,266 |
| Success rate | 95.93% | −0.08pp | +0.14pp | 96.08% |
| Settled value | ₹1.61 Cr | −13.3% | −3.0% | ₹2.13 Cr |
| Average ticket | ₹1,172 | −0.4% | +9.5% | ₹1,303 |
| Technical declines | 0.413% | −0.03pp | −0.01pp | 0.491% |
| Business declines | 3.242% | +0.12pp | +0.19pp | 2.745% |
| Risk declines | 0.098% | +0.01pp | −0.02pp | 0.110% |
| Timeout declines | 0.203% | −0.04pp | −0.34pp | 0.489% |
| Retry share | 1.41% | −0.04pp | −1.53pp | 1.46% |
| Latency p95 | 1,244 ms | +3.8% | +1.4% | 1,306 ms |
| Active customers | 11,886 | −11.0% | −9.6% | 13,651 |
| Active merchants | 1,528 | −4.6% | −5.0% | 1,630 |

## What moved

- Product UPI Lite is compounding — attempts up 27% across the trailing window to 2,242 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,656 | 32.6% | 95.10% | ₹46.66 L | +5.2% |
| UPI Person to Merchant | 3,137 | 22.0% | 96.05% | ₹32.20 L | −13.3% |
| UPI QR Payments | 2,303 | 16.1% | 96.18% | ₹9.52 L | −10.8% |
| UPI Lite | 2,242 | 15.7% | 98.80% | ₹2.02 L | −12.6% |
| UPI Circle | 765 | 5.4% | 97.39% | ₹5.76 L | −5.3% |
| UPI AutoPay | 353 | 2.5% | 87.25% | ₹6.58 L | −6.5% |
| Credit on UPI | 235 | 1.6% | 93.62% | ₹20.26 L | −50.5% |
| RuPay Credit on UPI | 178 | 1.2% | 97.19% | ₹6.57 L | −52.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,432 | 96.03% | 96.16% | ₹54.40 L | normal |
| HDFC Bank | 1,603 | 95.76% | 96.37% | ₹18.57 L | normal |
| Bank of Baroda | 1,093 | 95.88% | 96.22% | ₹10.20 L | normal |
| Union Bank of India | 1,020 | 96.08% | 96.12% | ₹11.08 L | normal |
| Punjab National Bank | 919 | 95.87% | 95.95% | ₹10.80 L | normal |
| Axis Bank | 867 | 96.66% | 96.17% | ₹11.02 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,796 | 95.79% | 96.15% | ₹72.21 L | normal |
| Google Pay | 4,676 | 95.94% | 96.16% | ₹53.82 L | normal |
| Paytm | 1,162 | 96.30% | 96.16% | ₹16.94 L | normal |
| Navi | 533 | 95.68% | 96.37% | ₹5.46 L | normal |
| SuperMoney | 255 | 96.08% | 95.86% | ₹2.37 L | normal |
| BHIM | 143 | 97.90% | 95.69% | ₹3.56 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,841 | 96.85% | ₹35.62 L |
| Food & Beverage | 2,574 | 97.36% | ₹10.51 L |
| Mobility | 1,294 | 96.83% | ₹6.07 L |
| Bills | 828 | 95.89% | ₹9.31 L |
| Healthcare | 484 | 96.69% | ₹4.58 L |
| Digital | 189 | 87.30% | ₹89,395 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,197 | 29.4% | 96.16% | ₹45.48 L |
| North | 3,639 | 25.5% | 95.93% | ₹42.76 L |
| West | 3,463 | 24.2% | 95.87% | ₹42.74 L |
| East | 1,722 | 12.1% | 95.24% | ₹18.72 L |
| Central | 1,262 | 8.8% | 96.20% | ₹10.87 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 400 | 97.75% | ₹1.23 L |
| Vasant Wardrobe | Key Account | Retail | 46 | 95.65% | ₹1.23 L |
| Ujjwal Water Board | Key Account | Bills | 25 | 92.00% | ₹1.14 L |
| Hampi Styles | Key Account | Retail | 26 | 88.46% | ₹78,810 |
| Girnar Connect | Key Account | Bills | 148 | 93.24% | ₹68,890 |
| Hampi Stores 2298 | Key Account | Retail | 84 | 97.62% | ₹67,718 |
| Urban Boutique | Key Account | Retail | 103 | 93.20% | ₹64,199 |
| Tejas Bites | Key Account | Food & Beverage | 169 | 97.04% | ₹61,478 |

## Failure analysis

Of 565 declined attempts, 463 were business declines (3.242% of attempts — balances, PINs and limits), 59 technical (0.413%), 29 timeouts (0.203%) and 14 risk declines (0.098%).

201 attempts were re-presentations of an earlier failure (1.41% of the day); 65.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 190 | 1.330% | 1.220% |
| ZM | Invalid UPI PIN | business | Customer | 165 | 1.155% | 0.970% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.364% | 0.325% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.217% | 0.175% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.210% | 0.187% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 14 | 0.098% | 0.131% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.098% | 0.122% |
| ZX | Mandate not found or revoked | business | PSP | 14 | 0.098% | 0.080% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 142 | 110 |
| Auto-reversals | 25 | 24 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹5.17 L | ₹1.71 L |

## Customer behaviour

11,886 distinct customers transacted (−9.3% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,679 | 4,173 | 1.13 | 95.71% | ₹1,350 |
| power | 2,585 | 3,498 | 1.35 | 95.85% | ₹1,467 |
| merchant_heavy | 2,740 | 3,273 | 1.19 | 96.06% | ₹859 |
| small_ticket | 1,770 | 2,171 | 1.23 | 96.13% | ₹476 |
| occasional | 902 | 949 | 1.05 | 96.21% | ₹1,309 |
| new | 185 | 194 | 1.05 | 95.88% | ₹827 |
| dormant_returning | 25 | 25 | 1.00 | 96.00% | ₹1,611 |

## Operational events

- **INC-SETL-0082** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.

## Risks and opportunities

### Risks

- 142 refunds were raised, 3.1 sigma above the trailing median of 110.
- Category Digital ran at 87.30% success on 189 attempts (2.0% of the day), 6.59pp down its own 28-day median.
- Issuer Yes Bank ran at 94.60% success on 556 attempts (3.9% of the day), 1.54pp down its own 28-day median.
- Product Credit on UPI ran at 93.62% success on 235 attempts (1.6% of the day), 2.09pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 27% across the trailing window to 2,242 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

12 July was an incident day: INC-SETL-0082 was live and the rail closed at 95.93% success against a 96.11% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,283, successes=13,701, failed=565, pending=17, settled_value_inr=16,055,915.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: refunds=142; trailing_median=109.5; z=3.13
- incidents: event_id=INC-SETL-0082; kind=settlement_delay; severity=Sev-2; window=2026-07-10 to 2026-07-12; success_impact_pp=-6.29; volume_impact_pct=-22.54
- products: product_name=UPI Lite; attempts=2,242; window_growth_pct=27; success_rate=98.8
- categories: mcc_category=Digital; attempts=189; success_rate=87.3; own_median=93.89; z=-3.98
- banks: payer_bank=Yes Bank; attempts=556; success_rate=94.6; own_median=96.14; z=-2.16
- products: product_name=Credit on UPI; attempts=235; success_rate=93.62; own_median=95.71; z=-2.51
- products: product_name=RuPay Credit on UPI; attempts=178; own_median=371; z=-2.86
- products: product_name=UPI International; attempts=149; own_median=216; z=-2.2

Refs: enterprise_data/warehouse/transactions, RPT-D188-DAILY, enterprise_data/warehouse/reference/incidents.parquet
