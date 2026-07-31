---
id: RPT-D52-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 25 Feb 2026)

**Report ID:** RPT-D52-DAILY · **Day 52 of 206** · **Derived from:** 10,206 transaction rows queried live from the warehouse

## Summary

The rail took **10,206 payment attempts** on Wednesday 25 February 2026 (Working day) and settled **₹1.25 Cr** across 9,646 successful payments. Volume was +2.4% on yesterday and +4.9% on the same weekday last week. Success closed at **94.51%**, below the trailing 28-day median of 95.54%.

Retries reached 204 attempts (2.00% of the day, 5.3 sigma above normal). 65.2% of re-presented payments recovered, so the retry path was doing its job. Decline code Z9 (Insufficient funds) fired 207 times — 2.028% of attempts against a trailing 1.466%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,206 | +2.4% | +4.9% | 10,694 |
| Successful payments | 9,646 | +2.3% | +3.6% | 10,197 |
| Success rate | 94.51% | −0.12pp | −1.27pp | 95.32% |
| Settled value | ₹1.25 Cr | +14.7% | +12.0% | ₹1.21 Cr |
| Average ticket | ₹1,292 | +12.1% | +8.2% | ₹1,184 |
| Technical declines | 0.666% | +0.05pp | +0.35pp | 0.428% |
| Business declines | 4.233% | +0.25pp | +0.86pp | 3.622% |
| Risk declines | 0.078% | −0.01pp | −0.00pp | 0.131% |
| Timeout declines | 0.421% | −0.09pp | +0.11pp | 0.386% |
| Retry share | 2.00% | +0.19pp | +0.74pp | 1.47% |
| Latency p95 | 1,272 ms | −5.0% | +1.3% | 1,282 ms |
| Active customers | 8,698 | +2.3% | +4.4% | 9,048 |
| Active merchants | 1,242 | +2.7% | +0.2% | 1,252 |

## What moved

- Success rate closed at 94.51%, 1.03pp down the trailing median — a 2.6-sigma move.
- App PhonePe ran at 94.27% success on 4,786 attempts (46.9% of the day), 1.27pp down its own 28-day median.
- Issuer State Bank of India ran at 94.11% success on 3,227 attempts (31.6% of the day), 1.57pp down its own 28-day median.
- Category Food & Beverage ran at 95.50% success on 1,535 attempts (23.9% of the day), 1.23pp down its own 28-day median.
- Product UPI Person to Merchant ran at 95.05% success on 2,810 attempts (27.5% of the day), 0.82pp down its own 28-day median.
- Category Bills ran at 93.67% success on 663 attempts (10.3% of the day), 2.32pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,771 | 36.9% | 94.17% | ₹39.61 L | −3.0% |
| UPI Person to Merchant | 2,810 | 27.5% | 95.05% | ₹23.74 L | −9.7% |
| UPI QR Payments | 1,880 | 18.4% | 96.49% | ₹8.02 L | +7.4% |
| UPI Lite | 585 | 5.7% | 97.78% | ₹52,258 | −19.0% |
| UPI AutoPay | 328 | 3.2% | 81.10% | ₹5.36 L | +9.9% |
| RuPay Credit on UPI | 249 | 2.4% | 94.38% | ₹12.43 L | +23.9% |
| Credit on UPI | 162 | 1.6% | 96.30% | ₹17.51 L | +11.0% |
| UPI Circle | 101 | 1.0% | 94.06% | ₹80,502 | −1.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,227 | 94.11% | 95.68% | ₹44.13 L | ⚠ outlier |
| HDFC Bank | 1,148 | 95.56% | 96.22% | ₹12.82 L | normal |
| Bank of Baroda | 807 | 94.30% | 95.45% | ₹8.67 L | normal |
| Union Bank of India | 709 | 95.06% | 95.39% | ₹9.91 L | normal |
| Punjab National Bank | 622 | 95.02% | 94.50% | ₹6.37 L | normal |
| ICICI Bank | 602 | 94.85% | 96.06% | ₹8.00 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,786 | 94.27% | 95.54% | ₹59.24 L | ⚠ outlier |
| Google Pay | 3,345 | 94.83% | 95.63% | ₹41.42 L | normal |
| Paytm | 820 | 94.27% | 95.43% | ₹9.43 L | normal |
| Navi | 401 | 95.51% | 95.33% | ₹3.67 L | normal |
| SuperMoney | 208 | 95.67% | 96.27% | ₹2.48 L | normal |
| BHIM | 122 | 95.90% | 94.72% | ₹1.64 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,683 | 95.68% | ₹33.54 L |
| Food & Beverage | 1,535 | 95.50% | ₹6.95 L |
| Mobility | 698 | 96.70% | ₹4.87 L |
| Bills | 663 | 93.67% | ₹6.69 L |
| Healthcare | 338 | 94.38% | ₹2.88 L |
| Digital | 191 | 83.25% | ₹60,571 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,967 | 29.1% | 94.98% | ₹40.15 L |
| North | 2,632 | 25.8% | 94.15% | ₹27.93 L |
| West | 2,549 | 25.0% | 94.12% | ₹32.80 L |
| East | 1,208 | 11.8% | 94.78% | ₹16.31 L |
| Central | 850 | 8.3% | 94.82% | ₹7.49 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 57 | 91.23% | ₹1.90 L |
| Vega Electronics | Large | Retail | 25 | 96.00% | ₹1.61 L |
| Rapid Bazaar | Key Account | Retail | 263 | 95.82% | ₹1.06 L |
| Ujjwal Water Board | Key Account | Bills | 33 | 96.97% | ₹70,951 |
| Hampi Stores 2298 | Key Account | Retail | 89 | 97.75% | ₹70,764 |
| Urban Boutique | Key Account | Retail | 92 | 98.91% | ₹59,581 |
| Yamuna Restaurant | Key Account | Food & Beverage | 75 | 93.33% | ₹53,153 |
| Dhruva Supermart | Large | Retail | 47 | 93.62% | ₹46,849 |

## Failure analysis

Of 551 declined attempts, 432 were business declines (4.233% of attempts — balances, PINs and limits), 68 technical (0.666%), 43 timeouts (0.421%) and 8 risk declines (0.078%).

204 attempts were re-presentations of an earlier failure (2.00% of the day); 65.2% of them succeeded.

- Retries reached 204 attempts (2.00% of the day, 5.3 sigma above normal). 65.2% of re-presented payments recovered, so the retry path was doing its job.
- Decline code Z9 (Insufficient funds) fired 207 times — 2.028% of attempts against a trailing 1.466%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 207 | 2.028% | 1.466% |
| ZM | Invalid UPI PIN | business | Customer | 123 | 1.205% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 48 | 0.470% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.304% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.274% | 0.166% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.225% | 0.147% |
| U28 | Remitter bank unavailable | technical | Issuer | 21 | 0.206% | 0.119% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.157% | 0.102% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 72 | 70 |
| Auto-reversals | 20 | 16 |
| Disputes / chargebacks | 12 | 6 |
| Value returned | ₹96,703 | ₹97,282 |

## Customer behaviour

8,698 distinct customers transacted (−1.8% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,661 | 2,975 | 1.12 | 94.49% | ₹1,159 |
| power | 1,860 | 2,397 | 1.29 | 94.49% | ₹1,771 |
| merchant_heavy | 1,986 | 2,332 | 1.17 | 94.55% | ₹1,024 |
| small_ticket | 1,280 | 1,530 | 1.20 | 94.97% | ₹492 |
| occasional | 691 | 731 | 1.06 | 94.25% | ₹1,992 |
| new | 184 | 205 | 1.11 | 91.71% | ₹661 |
| dormant_returning | 36 | 36 | 1.00 | 97.22% | ₹1,200 |

## Operational events

- **INC-SETL-0081** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 207 times — 2.028% of attempts against a trailing 1.466%. Owner: Customer.
- Success rate closed at 94.51%, 1.03pp down the trailing median — a 2.6-sigma move.
- App PhonePe ran at 94.27% success on 4,786 attempts (46.9% of the day), 1.27pp down its own 28-day median.
- Issuer State Bank of India ran at 94.11% success on 3,227 attempts (31.6% of the day), 1.57pp down its own 28-day median.
- Category Food & Beverage ran at 95.50% success on 1,535 attempts (23.9% of the day), 1.23pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

25 February was an incident day: INC-SETL-0081 was live and the rail closed at 94.51% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,206, successes=9,646, failed=551, pending=9, settled_value_inr=12,466,676.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=204; retry_share_pct=2; recovery_pct=65.2; z=5.32
- failures: failure_code=Z9; count=207; rate_pct=2.03; trailing_rate_pct=1.47; owner=Customer; z=3.9
- headline: success_rate=94.51; trailing_median=95.54; z=-2.62
- psps: payer_psp=PhonePe; attempts=4,786; success_rate=94.27; own_median=95.54; z=-3.04
- banks: payer_bank=State Bank of India; attempts=3,227; success_rate=94.11; own_median=95.68; z=-3.45
- incidents: event_id=INC-SETL-0081; kind=settlement_delay; severity=Sev-2; window=2026-02-24 to 2026-02-26; success_impact_pp=-4.62; volume_impact_pct=-27.27
- categories: mcc_category=Food & Beverage; attempts=1,535; success_rate=95.5; own_median=96.74; z=-2.82
- products: product_name=UPI Person to Merchant; attempts=2,810; success_rate=95.05; own_median=95.87; z=-2.27
- categories: mcc_category=Bills; attempts=663; success_rate=93.67; own_median=95.98; z=-3.7
- geography: region=North; attempts=2,632; success_rate=94.15; own_median=95.47; z=-2.25

Refs: enterprise_data/warehouse/transactions, RPT-D51-DAILY, enterprise_data/warehouse/reference/incidents.parquet
