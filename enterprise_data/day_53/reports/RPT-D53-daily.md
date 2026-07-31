---
id: RPT-D53-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 26 Feb 2026)

**Report ID:** RPT-D53-DAILY · **Day 53 of 206** · **Derived from:** 10,032 transaction rows queried live from the warehouse

## Summary

The rail took **10,032 payment attempts** on Thursday 26 February 2026 (Working day) and settled **₹1.19 Cr** across 9,504 successful payments. Volume was −1.7% on yesterday and +0.7% on the same weekday last week. Success closed at **94.74%**, below the trailing 28-day median of 95.54%.

Decline code Z9 (Insufficient funds) fired 190 times — 1.894% of attempts against a trailing 1.466%. Owner: Customer. Retries reached 174 attempts (1.73% of the day, 3.4 sigma above normal). 67.2% of re-presented payments recovered, so the retry path was doing its job.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,032 | −1.7% | +0.7% | 10,668 |
| Successful payments | 9,504 | −1.5% | +0.2% | 10,171 |
| Success rate | 94.74% | +0.22pp | −0.45pp | 95.30% |
| Settled value | ₹1.19 Cr | −4.2% | +6.8% | ₹1.21 Cr |
| Average ticket | ₹1,257 | −2.7% | +6.6% | ₹1,187 |
| Technical declines | 0.498% | −0.17pp | +0.08pp | 0.431% |
| Business declines | 4.266% | +0.03pp | +0.36pp | 3.647% |
| Risk declines | 0.020% | −0.06pp | −0.08pp | 0.127% |
| Timeout declines | 0.379% | −0.04pp | +0.07pp | 0.385% |
| Retry share | 1.73% | −0.26pp | +0.08pp | 1.48% |
| Latency p95 | 1,325 ms | +4.2% | +2.3% | 1,284 ms |
| Active customers | 8,641 | −0.7% | +1.0% | 9,032 |
| Active merchants | 1,260 | +1.4% | +2.0% | 1,252 |

## What moved

- App PhonePe ran at 94.14% success on 4,673 attempts (46.6% of the day), 1.41pp down its own 28-day median.
- Success rate closed at 94.74%, 0.81pp down the trailing median — a 2.1-sigma move.
- Region South ran at 94.37% success on 2,964 attempts (29.5% of the day), 1.12pp down its own 28-day median.
- Issuer State Bank of India ran at 94.67% success on 3,224 attempts (32.1% of the day), 1.01pp down its own 28-day median.
- Category Bills ran at 93.97% success on 829 attempts (14.0% of the day), 2.01pp down its own 28-day median.
- Category Retail carried 2,226 attempts, 17% down its trailing median and 37.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,090 | 40.8% | 94.11% | ₹44.16 L | +5.2% |
| UPI Person to Merchant | 2,454 | 24.5% | 95.76% | ₹26.08 L | −21.1% |
| UPI QR Payments | 1,811 | 18.1% | 95.86% | ₹6.92 L | +2.3% |
| UPI Lite | 586 | 5.8% | 98.29% | ₹53,872 | −18.9% |
| UPI AutoPay | 319 | 3.2% | 84.95% | ₹4.84 L | +6.3% |
| RuPay Credit on UPI | 221 | 2.2% | 96.38% | ₹10.51 L | +8.9% |
| Credit on UPI | 136 | 1.4% | 91.91% | ₹8.61 L | −7.2% |
| UPI International | 94 | 0.9% | 94.68% | ₹11.40 L | +25.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,224 | 94.67% | 95.68% | ₹39.27 L | ⚠ outlier |
| HDFC Bank | 1,072 | 94.50% | 96.22% | ₹14.05 L | ⚠ outlier |
| Bank of Baroda | 757 | 95.38% | 95.45% | ₹6.54 L | normal |
| Union Bank of India | 652 | 94.63% | 95.39% | ₹9.20 L | normal |
| Axis Bank | 625 | 94.08% | 95.47% | ₹6.31 L | normal |
| ICICI Bank | 607 | 95.22% | 96.06% | ₹7.57 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,673 | 94.14% | 95.54% | ₹58.02 L | ⚠ outlier |
| Google Pay | 3,311 | 95.17% | 95.63% | ₹41.47 L | normal |
| Paytm | 816 | 95.83% | 95.43% | ₹7.77 L | normal |
| Navi | 376 | 95.74% | 95.33% | ₹3.53 L | normal |
| SuperMoney | 214 | 95.79% | 96.18% | ₹1.71 L | normal |
| BHIM | 102 | 96.08% | 94.72% | ₹1.96 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,226 | 95.82% | ₹23.41 L |
| Food & Beverage | 1,391 | 96.76% | ₹5.66 L |
| Bills | 829 | 93.97% | ₹9.85 L |
| Mobility | 684 | 95.91% | ₹3.41 L |
| Healthcare | 269 | 94.05% | ₹4.67 L |
| Digital | 219 | 92.24% | ₹1.26 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,964 | 29.5% | 94.37% | ₹35.56 L |
| North | 2,481 | 24.7% | 94.88% | ₹29.17 L |
| West | 2,455 | 24.5% | 95.03% | ₹29.11 L |
| East | 1,264 | 12.6% | 94.38% | ₹15.62 L |
| Central | 868 | 8.7% | 95.28% | ₹10.01 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 41 | 97.56% | ₹1.92 L |
| Vega Electronics | Large | Retail | 19 | 94.74% | ₹1.51 L |
| Vasant Wardrobe | Key Account | Retail | 53 | 98.11% | ₹1.22 L |
| Rapid Bazaar | Key Account | Retail | 224 | 96.43% | ₹84,648 |
| Urban Boutique | Key Account | Retail | 68 | 97.06% | ₹58,324 |
| Girnar Connect | Key Account | Bills | 144 | 93.06% | ₹47,126 |
| Indus Connect | Key Account | Bills | 41 | 100.00% | ₹45,924 |
| Kaveri Trading | Large | Retail | 32 | 96.88% | ₹44,044 |

## Failure analysis

Of 518 declined attempts, 428 were business declines (4.266% of attempts — balances, PINs and limits), 50 technical (0.498%), 38 timeouts (0.379%) and 2 risk declines (0.020%).

174 attempts were re-presentations of an earlier failure (1.73% of the day); 67.2% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 190 times — 1.894% of attempts against a trailing 1.466%. Owner: Customer.
- Retries reached 174 attempts (1.73% of the day, 3.4 sigma above normal). 67.2% of re-presented payments recovered, so the retry path was doing its job.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 190 | 1.894% | 1.466% |
| ZM | Invalid UPI PIN | business | Customer | 125 | 1.246% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.488% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.329% | 0.239% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.229% | 0.168% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.209% | 0.147% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.150% | 0.104% |
| UX | Mandate execution outside permitted window | business | PSP | 15 | 0.150% | 0.108% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 64 | 70 |
| Auto-reversals | 28 | 16 |
| Disputes / chargebacks | 10 | 6 |
| Value returned | ₹75,842 | ₹97,739 |

## Customer behaviour

8,641 distinct customers transacted (−2.4% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,659 | 2,952 | 1.11 | 94.68% | ₹1,208 |
| power | 1,857 | 2,377 | 1.28 | 94.19% | ₹1,783 |
| merchant_heavy | 1,962 | 2,274 | 1.16 | 95.03% | ₹973 |
| small_ticket | 1,248 | 1,468 | 1.18 | 94.55% | ₹492 |
| occasional | 708 | 740 | 1.05 | 95.81% | ₹1,279 |
| new | 181 | 195 | 1.08 | 95.38% | ₹1,213 |
| dormant_returning | 26 | 26 | 1.00 | 100.00% | ₹1,000 |

## Operational events

- **INC-SETL-0081** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 190 times — 1.894% of attempts against a trailing 1.466%. Owner: Customer.
- App PhonePe ran at 94.14% success on 4,673 attempts (46.6% of the day), 1.41pp down its own 28-day median.
- 28 auto-reversals were raised, 3.9 sigma above the trailing median of 16.
- Success rate closed at 94.74%, 0.81pp down the trailing median — a 2.1-sigma move.
- Region South ran at 94.37% success on 2,964 attempts (29.5% of the day), 1.12pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

26 February was an incident day: INC-SETL-0081 was live and the rail closed at 94.74% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,032, successes=9,504, failed=518, pending=10, settled_value_inr=11,947,392.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=190; rate_pct=1.89; trailing_rate_pct=1.47; owner=Customer; z=2.97
- failures: retries=174; retry_share_pct=1.73; recovery_pct=67.24; z=3.43
- psps: payer_psp=PhonePe; attempts=4,673; success_rate=94.14; own_median=95.54; z=-3.37
- adjustments: reversals=28; trailing_median=16.5; z=3.88
- incidents: event_id=INC-SETL-0081; kind=settlement_delay; severity=Sev-2; window=2026-02-24 to 2026-02-26; success_impact_pp=-4.62; volume_impact_pct=-27.27
- headline: success_rate=94.74; trailing_median=95.54; z=-2.05
- geography: region=South; attempts=2,964; success_rate=94.37; own_median=95.49; z=-2.36
- banks: payer_bank=State Bank of India; attempts=3,224; success_rate=94.67; own_median=95.68; z=-2.23
- categories: mcc_category=Bills; attempts=829; success_rate=93.97; own_median=95.98; z=-3.22
- categories: mcc_category=Retail; attempts=2,226; own_median=2,694.5; z=-2.22

Refs: enterprise_data/warehouse/transactions, RPT-D52-DAILY, enterprise_data/warehouse/reference/incidents.parquet
