---
id: RPT-D51-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 24 Feb 2026)

**Report ID:** RPT-D51-DAILY · **Day 51 of 206** · **Derived from:** 9,964 transaction rows queried live from the warehouse

## Summary

The rail took **9,964 payment attempts** on Tuesday 24 February 2026 (Working day) and settled **₹1.09 Cr** across 9,429 successful payments. Volume was −1.6% on yesterday and −2.6% on the same weekday last week. Success closed at **94.63%**, below the trailing 28-day median of 95.54%.

Retries reached 180 attempts (1.81% of the day, 3.9 sigma above normal). Only 45.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them. Category Bills ran at 90.26% success on 657 attempts (10.3% of the day), 5.72pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,964 | −1.6% | −2.6% | 10,714 |
| Successful payments | 9,429 | −2.6% | −3.4% | 10,220 |
| Success rate | 94.63% | −0.93pp | −0.75pp | 95.35% |
| Settled value | ₹1.09 Cr | −1.2% | −7.9% | ₹1.21 Cr |
| Average ticket | ₹1,153 | +1.4% | −4.7% | ₹1,180 |
| Technical declines | 0.612% | +0.37pp | +0.20pp | 0.418% |
| Business declines | 3.984% | +0.29pp | +0.28pp | 3.597% |
| Risk declines | 0.090% | −0.05pp | −0.04pp | 0.133% |
| Timeout declines | 0.512% | +0.29pp | +0.25pp | 0.384% |
| Retry share | 1.81% | +0.58pp | +0.69pp | 1.44% |
| Latency p95 | 1,339 ms | +7.4% | +6.5% | 1,283 ms |
| Active customers | 8,501 | −2.1% | −3.1% | 9,062 |
| Active merchants | 1,209 | −2.5% | −1.1% | 1,252 |

## What moved

- Category Bills ran at 90.26% success on 657 attempts (10.3% of the day), 5.72pp down its own 28-day median.
- Success rate closed at 94.63%, 0.91pp down the trailing median — a 2.3-sigma move.
- Region South ran at 94.03% success on 2,996 attempts (30.1% of the day), 1.46pp down its own 28-day median.
- Issuer State Bank of India ran at 94.60% success on 3,201 attempts (32.1% of the day), 1.08pp down its own 28-day median.
- Region West ran at 93.90% success on 2,394 attempts (24.0% of the day), 1.69pp down its own 28-day median.
- App Google Pay ran at 94.39% success on 3,367 attempts (33.8% of the day), 1.27pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,597 | 36.1% | 94.63% | ₹34.92 L | −7.5% |
| UPI Person to Merchant | 2,851 | 28.6% | 95.26% | ₹25.98 L | −8.4% |
| UPI QR Payments | 1,773 | 17.8% | 96.05% | ₹7.12 L | +4.4% |
| UPI Lite | 637 | 6.4% | 98.27% | ₹52,425 | −11.8% |
| UPI AutoPay | 311 | 3.1% | 76.85% | ₹4.47 L | +4.2% |
| RuPay Credit on UPI | 217 | 2.2% | 97.24% | ₹11.11 L | +8.0% |
| Credit on UPI | 146 | 1.5% | 97.95% | ₹8.15 L | +0.0% |
| UPI Circle | 102 | 1.0% | 93.14% | ₹78,947 | +0.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,201 | 94.60% | 95.68% | ₹36.31 L | ⚠ outlier |
| HDFC Bank | 1,058 | 95.75% | 96.22% | ₹10.56 L | normal |
| Bank of Baroda | 764 | 94.50% | 95.45% | ₹8.08 L | normal |
| Union Bank of India | 677 | 94.83% | 95.39% | ₹6.63 L | normal |
| Punjab National Bank | 662 | 94.71% | 94.23% | ₹7.67 L | normal |
| ICICI Bank | 615 | 95.93% | 96.18% | ₹5.80 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,673 | 94.95% | 95.54% | ₹53.67 L | normal |
| Google Pay | 3,367 | 94.39% | 95.66% | ₹35.18 L | ⚠ outlier |
| Paytm | 782 | 93.48% | 95.43% | ₹8.68 L | normal |
| Navi | 369 | 94.58% | 95.45% | ₹2.88 L | normal |
| SuperMoney | 176 | 93.75% | 96.30% | ₹1.63 L | ⚠ outlier |
| BHIM | 117 | 94.87% | 94.41% | ₹73,442 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,657 | 95.86% | ₹29.31 L |
| Food & Beverage | 1,517 | 96.31% | ₹6.11 L |
| Mobility | 667 | 95.65% | ₹4.03 L |
| Bills | 657 | 90.26% | ₹7.18 L |
| Healthcare | 360 | 96.94% | ₹2.90 L |
| Digital | 194 | 86.08% | ₹80,960 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,996 | 30.1% | 94.03% | ₹30.16 L |
| North | 2,429 | 24.4% | 95.97% | ₹24.47 L |
| West | 2,394 | 24.0% | 93.90% | ₹30.63 L |
| East | 1,217 | 12.2% | 94.66% | ₹15.26 L |
| Central | 928 | 9.3% | 94.94% | ₹8.19 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 24 | 100.00% | ₹1.58 L |
| Vasant Wardrobe | Key Account | Retail | 56 | 94.64% | ₹1.39 L |
| Rapid Bazaar | Key Account | Retail | 297 | 96.97% | ₹1.07 L |
| Ujjwal Water Board | Key Account | Bills | 33 | 96.97% | ₹92,257 |
| Hampi Stores 2298 | Key Account | Retail | 124 | 94.35% | ₹80,209 |
| Kaveri Trading | Large | Retail | 47 | 95.74% | ₹50,402 |
| Girnar Connect | Key Account | Bills | 111 | 91.89% | ₹47,467 |
| Aravalli Pharmacy | Large | Healthcare | 62 | 98.39% | ₹39,407 |

## Failure analysis

Of 518 declined attempts, 397 were business declines (3.984% of attempts — balances, PINs and limits), 61 technical (0.612%), 51 timeouts (0.512%) and 9 risk declines (0.090%).

180 attempts were re-presentations of an earlier failure (1.81% of the day); 45.6% of them succeeded.

- Retries reached 180 attempts (1.81% of the day, 3.9 sigma above normal). Only 45.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U30 (Debit failed at remitter bank) fired 31 times — 0.311% of attempts against a trailing 0.166%. Owner: Issuer.
- Decline code UX (Mandate execution outside permitted window) fired 20 times — 0.201% of attempts against a trailing 0.107%. Owner: PSP.
- Decline code U54 (Transaction timed out at beneficiary) fired 23 times — 0.231% of attempts against a trailing 0.141%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 169 | 1.696% | 1.466% |
| ZM | Invalid UPI PIN | business | Customer | 124 | 1.244% | 1.201% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.472% | 0.428% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.311% | 0.166% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.271% | 0.236% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.231% | 0.141% |
| UX | Mandate execution outside permitted window | business | PSP | 20 | 0.201% | 0.107% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.171% | 0.102% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 66 | 70 |
| Auto-reversals | 12 | 17 |
| Disputes / chargebacks | 6 | 6 |
| Value returned | ₹93,202 | ₹97,282 |

## Customer behaviour

8,501 distinct customers transacted (−4.0% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,591 | 2,898 | 1.12 | 94.58% | ₹1,206 |
| power | 1,822 | 2,342 | 1.29 | 94.36% | ₹1,467 |
| merchant_heavy | 1,994 | 2,337 | 1.17 | 95.16% | ₹882 |
| small_ticket | 1,250 | 1,491 | 1.19 | 94.37% | ₹580 |
| occasional | 653 | 687 | 1.05 | 94.61% | ₹1,214 |
| new | 170 | 188 | 1.11 | 94.15% | ₹796 |
| dormant_returning | 21 | 21 | 1.00 | 95.24% | ₹1,545 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-SETL-0081** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Retries reached 180 attempts (1.81% of the day, 3.9 sigma above normal). Only 45.6% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Category Bills ran at 90.26% success on 657 attempts (10.3% of the day), 5.72pp down its own 28-day median.
- Success rate closed at 94.63%, 0.91pp down the trailing median — a 2.3-sigma move.
- Region South ran at 94.03% success on 2,996 attempts (30.1% of the day), 1.46pp down its own 28-day median.
- Issuer State Bank of India ran at 94.60% success on 3,201 attempts (32.1% of the day), 1.08pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

24 February was an incident day: INC-FRAUD-0048, INC-SETL-0081 were live and the rail closed at 94.63% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,964, successes=9,429, failed=518, pending=17, settled_value_inr=10,872,627.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=180; retry_share_pct=1.81; recovery_pct=45.56; z=3.94
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- categories: mcc_category=Bills; attempts=657; success_rate=90.26; own_median=95.98; z=-9.15
- headline: success_rate=94.63; trailing_median=95.54; z=-2.32
- geography: region=South; attempts=2,996; success_rate=94.03; own_median=95.49; z=-3.08
- incidents: event_id=INC-SETL-0081; kind=settlement_delay; severity=Sev-2; window=2026-02-24 to 2026-02-26; success_impact_pp=-4.62; volume_impact_pct=-27.27
- banks: payer_bank=State Bank of India; attempts=3,201; success_rate=94.6; own_median=95.68; z=-2.38
- geography: region=West; attempts=2,394; success_rate=93.9; own_median=95.59; z=-2.7
- psps: payer_psp=Google Pay; attempts=3,367; success_rate=94.39; own_median=95.66; z=-2.25
- failures: failure_code=U30; count=31; rate_pct=0.31; trailing_rate_pct=0.17; owner=Issuer; z=2.34

Refs: enterprise_data/warehouse/transactions, RPT-D50-DAILY, enterprise_data/warehouse/reference/incidents.parquet
