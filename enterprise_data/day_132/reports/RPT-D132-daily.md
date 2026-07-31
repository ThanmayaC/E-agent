---
id: RPT-D132-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 16 May 2026)

**Report ID:** RPT-D132-DAILY · **Day 132 of 206** · **Derived from:** 17,220 transaction rows queried live from the warehouse

## Summary

The rail took **17,220 payment attempts** on Saturday 16 May 2026 (Summer Travel Peak (build-up)) and settled **₹2.29 Cr** across 16,462 successful payments. Volume was +21.0% on yesterday and +4.6% on the same weekday last week. Success closed at **95.60%**, below the trailing 28-day median of 95.92%.

Retries reached 390 attempts (2.26% of the day, 3.0 sigma above normal). Only 47.4% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them. Decline code ZM (Invalid UPI PIN) fired 215 times — 1.249% of attempts against a trailing 1.032%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 17,220 | +21.0% | +4.6% | 15,084 |
| Successful payments | 16,462 | +24.4% | +4.6% | 14,461 |
| Success rate | 95.60% | +2.61pp | −0.05pp | 95.86% |
| Settled value | ₹2.29 Cr | +16.4% | +23.1% | ₹2.02 Cr |
| Average ticket | ₹1,390 | −6.4% | +17.7% | ₹1,394 |
| Technical declines | 0.633% | −0.72pp | +0.08pp | 0.544% |
| Business declines | 3.101% | +0.04pp | −0.09pp | 2.906% |
| Risk declines | 0.139% | −0.02pp | +0.03pp | 0.128% |
| Timeout declines | 0.418% | −1.91pp | +0.01pp | 0.454% |
| Retry share | 2.26% | −0.93pp | +0.64pp | 1.42% |
| Latency p95 | 1,292 ms | −34.7% | +4.1% | 1,296 ms |
| Active customers | 13,681 | +18.4% | +4.7% | 12,242 |
| Active merchants | 1,599 | +6.1% | +4.4% | 1,506 |

## What moved

- Product UPI Circle is compounding — attempts up 58% across the trailing window to 808 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Category Food & Beverage carried 3,216 attempts, 41% up its trailing median and 25.6% of the day's volume.
- Product UPI Lite is compounding — attempts up 40% across the trailing window to 2,591 today, with success holding, so the growth is healthy and worth funding.
- Category Retail carried 5,249 attempts, 37% up its trailing median and 41.8% of the day's volume.
- Product UPI Lite carried 2,591 attempts, 68% up its trailing median and 15.0% of the day's volume.
- Category Mobility carried 1,687 attempts, 57% up its trailing median and 13.4% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 4,749 | 27.6% | 95.64% | ₹48.40 L | +22.3% |
| UPI Person to Person | 4,655 | 27.0% | 94.50% | ₹49.91 L | +6.2% |
| UPI QR Payments | 2,822 | 16.4% | 97.09% | ₹12.29 L | +20.3% |
| UPI Lite | 2,591 | 15.0% | 98.46% | ₹2.35 L | +67.8% |
| UPI Circle | 808 | 4.7% | 95.30% | ₹6.25 L | +69.7% |
| RuPay Credit on UPI | 393 | 2.3% | 94.91% | ₹28.78 L | +9.6% |
| UPI AutoPay | 353 | 2.0% | 86.69% | ₹6.49 L | +7.6% |
| Credit on UPI | 293 | 1.7% | 94.54% | ₹28.46 L | −8.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,461 | 95.90% | 95.96% | ₹73.07 L | normal |
| HDFC Bank | 1,845 | 96.10% | 96.01% | ₹25.26 L | normal |
| Bank of Baroda | 1,344 | 95.09% | 95.88% | ₹17.26 L | normal |
| Union Bank of India | 1,185 | 95.70% | 94.99% | ₹16.50 L | normal |
| Punjab National Bank | 1,059 | 95.66% | 95.52% | ₹13.68 L | normal |
| ICICI Bank | 1,032 | 95.93% | 96.43% | ₹11.17 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,271 | 96.00% | 95.93% | ₹1.06 Cr | normal |
| Google Pay | 5,577 | 95.10% | 95.71% | ₹75.90 L | normal |
| Paytm | 1,388 | 96.47% | 95.95% | ₹20.27 L | normal |
| Navi | 625 | 94.88% | 95.54% | ₹9.91 L | normal |
| SuperMoney | 335 | 94.03% | 96.07% | ₹4.79 L | normal |
| BHIM | 192 | 93.75% | 95.46% | ₹4.25 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,249 | 96.15% | ₹57.71 L |
| Food & Beverage | 3,216 | 97.39% | ₹16.30 L |
| Mobility | 1,687 | 97.04% | ₹8.63 L |
| Bills | 988 | 93.52% | ₹9.53 L |
| Healthcare | 597 | 96.31% | ₹7.05 L |
| Travel | 228 | 89.91% | ₹57.41 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,080 | 29.5% | 95.89% | ₹71.44 L |
| North | 4,308 | 25.0% | 95.43% | ₹53.00 L |
| West | 4,231 | 24.6% | 95.63% | ₹60.19 L |
| East | 2,094 | 12.2% | 95.03% | ₹28.07 L |
| Central | 1,507 | 8.8% | 95.82% | ₹16.19 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 129 | 98.45% | ₹4.35 L |
| Vega Electronics | Large | Retail | 37 | 91.89% | ₹3.78 L |
| Rapid Bazaar | Key Account | Retail | 527 | 97.15% | ₹1.95 L |
| Ujjwal Water Board | Key Account | Bills | 51 | 98.04% | ₹1.47 L |
| Swift Grill | Large | Food & Beverage | 46 | 100.00% | ₹1.21 L |
| Hampi Styles | Key Account | Retail | 58 | 87.93% | ₹1.07 L |
| Hampi Stores 2298 | Key Account | Retail | 146 | 94.52% | ₹93,151 |
| Trinetra Restaurant | Large | Food & Beverage | 44 | 95.45% | ₹90,428 |

## Failure analysis

Of 739 declined attempts, 534 were business declines (3.101% of attempts — balances, PINs and limits), 109 technical (0.633%), 72 timeouts (0.418%) and 24 risk declines (0.139%).

390 attempts were re-presentations of an earlier failure (2.26% of the day); 47.4% of them succeeded.

- Retries reached 390 attempts (2.26% of the day, 3.0 sigma above normal). Only 47.4% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code ZM (Invalid UPI PIN) fired 215 times — 1.249% of attempts against a trailing 1.032%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 215 | 1.249% | 1.032% |
| Z9 | Insufficient funds | business | Customer | 193 | 1.121% | 1.210% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.302% | 0.353% |
| U30 | Debit failed at remitter bank | technical | Issuer | 42 | 0.244% | 0.209% |
| XH | Account does not exist / frozen | business | Issuer | 37 | 0.215% | 0.219% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 31 | 0.180% | 0.165% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 31 | 0.180% | 0.116% |
| U28 | Remitter bank unavailable | technical | Issuer | 29 | 0.168% | 0.137% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 108 | 90 |
| Auto-reversals | 46 | 28 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹4.43 L | ₹1.51 L |

## Customer behaviour

13,681 distinct customers transacted (+19.4% on the 28-day median) at 1.26 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,352 | 5,198 | 1.19 | 95.02% | ₹1,429 |
| power | 2,808 | 3,981 | 1.42 | 95.73% | ₹1,872 |
| merchant_heavy | 3,053 | 3,919 | 1.28 | 95.84% | ₹1,146 |
| small_ticket | 2,036 | 2,584 | 1.27 | 96.25% | ₹593 |
| occasional | 1,120 | 1,197 | 1.07 | 95.41% | ₹1,464 |
| new | 274 | 302 | 1.10 | 95.70% | ₹675 |
| dormant_returning | 38 | 39 | 1.03 | 97.44% | ₹712 |

## Operational events

- **INC-SETL-0083** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **CMP-0061** (Sev-3) — Wealth & SIP cashback campaign, scoped to 6211. A cashback campaign across Wealth & SIP merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0067** (Sev-3) — Fashion cashback campaign, scoped to 5691. A cashback campaign across Fashion merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **REG-0069** (Sev-3) — UPI International — two new acceptance corridors live, scoped to UPI_INTL. Two new cross-border acceptance corridors went live. Volume steps up; early-corridor settlement immaturity temporarily depresses the success rate.

## Risks and opportunities

### Risks

- Retries reached 390 attempts (2.26% of the day, 3.0 sigma above normal). Only 47.4% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code ZM (Invalid UPI PIN) fired 215 times — 1.249% of attempts against a trailing 1.032%. Owner: Customer.
- Product UPI Circle is compounding — attempts up 58% across the trailing window to 808 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer IndusInd Bank ran at 93.50% success on 369 attempts (2.1% of the day), 2.29pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 40% across the trailing window to 2,591 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

16 May was an incident day: INC-SETL-0083 was live and the rail closed at 95.60% success against a 95.92% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=17,220, successes=16,462, failed=739, pending=19, settled_value_inr=22,887,606.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=390; retry_share_pct=2.26; recovery_pct=47.44; z=2.98
- failures: failure_code=ZM; count=215; rate_pct=1.25; trailing_rate_pct=1.03; owner=Customer; z=2.47
- incidents: event_id=INC-SETL-0083; kind=settlement_delay; severity=Sev-2; window=2026-05-16 to 2026-05-16; success_impact_pp=-6.29; volume_impact_pct=-25.9
- products: product_name=UPI Circle; attempts=808; window_growth_pct=58.2; success_rate=95.3
- categories: mcc_category=Food & Beverage; attempts=3,216; own_median=2,285; z=3.05
- products: product_name=UPI Lite; attempts=2,591; window_growth_pct=39.7; success_rate=98.46
- categories: mcc_category=Retail; attempts=5,249; own_median=3,838.5; z=2.28
- products: product_name=UPI Lite; attempts=2,591; own_median=1,544; z=3.23
- categories: mcc_category=Mobility; attempts=1,687; own_median=1,072; z=2.92
- products: product_name=UPI International; attempts=281; own_median=139; z=5.63

Refs: enterprise_data/warehouse/transactions, RPT-D131-DAILY, enterprise_data/warehouse/reference/incidents.parquet
