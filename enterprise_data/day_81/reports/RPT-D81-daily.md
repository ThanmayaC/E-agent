---
id: RPT-D81-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 26 Mar 2026)

**Report ID:** RPT-D81-DAILY · **Day 81 of 206** · **Derived from:** 10,280 transaction rows queried live from the warehouse

## Summary

The rail took **10,280 payment attempts** on Thursday 26 March 2026 (Working day) and settled **₹1.28 Cr** across 9,264 successful payments. Volume was +3.1% on yesterday and −24.6% on the same weekday last week. Success closed at **90.12%**, below the trailing 28-day median of 95.79%.

Decline code BT (Acquirer / NPCI switch timeout) fired 146 times — 1.420% of attempts against a trailing 0.101%. Owner: NPCI. Decline code U54 (Transaction timed out at beneficiary) fired 182 times — 1.770% of attempts against a trailing 0.158%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,280 | +3.1% | −24.6% | 12,437 |
| Successful payments | 9,264 | −2.4% | −29.3% | 11,889 |
| Success rate | 90.12% | −5.10pp | −6.10pp | 95.53% |
| Settled value | ₹1.28 Cr | +7.8% | −15.3% | ₹1.41 Cr |
| Average ticket | ₹1,385 | +10.4% | +19.9% | ₹1,189 |
| Technical declines | 1.663% | +1.35pp | +1.27pp | 0.489% |
| Business declines | 4.105% | +0.15pp | +1.22pp | 3.306% |
| Risk declines | 0.165% | +0.04pp | +0.03pp | 0.125% |
| Timeout declines | 3.774% | +3.52pp | +3.49pp | 0.453% |
| Retry share | 4.87% | +3.63pp | +3.71pp | 1.39% |
| Latency p95 | 2,309 ms | +74.4% | +87.2% | 1,286 ms |
| Active customers | 8,487 | −1.2% | −23.3% | 10,299 |
| Active merchants | 1,270 | −0.3% | −5.6% | 1,318 |

## What moved

- Success rate closed at 90.12%, 5.68pp down the trailing median — a 22.0-sigma move.
- App PhonePe ran at 90.30% success on 4,763 attempts (46.3% of the day), 5.65pp down its own 28-day median.
- Region North ran at 89.91% success on 2,607 attempts (25.4% of the day), 6.01pp down its own 28-day median.
- App Google Pay ran at 90.18% success on 3,360 attempts (32.7% of the day), 5.53pp down its own 28-day median.
- Issuer State Bank of India ran at 89.94% success on 3,329 attempts (32.4% of the day), 5.79pp down its own 28-day median.
- Product UPI Person to Person ran at 89.80% success on 3,548 attempts (34.5% of the day), 5.43pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,548 | 34.5% | 89.80% | ₹36.98 L | −20.5% |
| UPI Person to Merchant | 3,009 | 29.3% | 90.50% | ₹27.39 L | −13.8% |
| UPI QR Payments | 1,744 | 17.0% | 91.06% | ₹7.30 L | −19.3% |
| UPI Lite | 700 | 6.8% | 93.86% | ₹58,867 | −23.5% |
| UPI AutoPay | 323 | 3.1% | 79.57% | ₹4.94 L | +2.7% |
| RuPay Credit on UPI | 255 | 2.5% | 88.24% | ₹9.72 L | +14.6% |
| Credit on UPI | 205 | 2.0% | 92.20% | ₹22.01 L | +34.9% |
| UPI Circle | 153 | 1.5% | 90.20% | ₹1.56 L | −15.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,329 | 89.94% | 95.72% | ₹42.63 L | ⚠ outlier |
| HDFC Bank | 1,104 | 89.95% | 95.71% | ₹13.77 L | ⚠ outlier |
| Bank of Baroda | 737 | 93.08% | 95.64% | ₹9.88 L | ⚠ outlier |
| Union Bank of India | 688 | 91.86% | 95.43% | ₹6.98 L | ⚠ outlier |
| Punjab National Bank | 625 | 91.20% | 95.41% | ₹6.22 L | ⚠ outlier |
| Axis Bank | 604 | 87.09% | 96.12% | ₹10.06 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,763 | 90.30% | 95.95% | ₹64.91 L | ⚠ outlier |
| Google Pay | 3,360 | 90.18% | 95.71% | ₹38.77 L | ⚠ outlier |
| Paytm | 864 | 90.86% | 95.77% | ₹9.41 L | ⚠ outlier |
| Navi | 408 | 88.97% | 95.75% | ₹5.11 L | ⚠ outlier |
| SuperMoney | 216 | 89.81% | 95.62% | ₹2.76 L | ⚠ outlier |
| BHIM | 107 | 88.79% | 95.53% | ₹1.32 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,754 | 91.25% | ₹30.84 L |
| Food & Beverage | 1,480 | 91.49% | ₹7.52 L |
| Bills | 899 | 90.10% | ₹10.14 L |
| Mobility | 693 | 90.48% | ₹3.85 L |
| Healthcare | 319 | 90.28% | ₹4.80 L |
| Digital | 252 | 82.54% | ₹1.25 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,965 | 28.8% | 90.99% | ₹40.68 L |
| North | 2,607 | 25.4% | 89.91% | ₹30.25 L |
| West | 2,572 | 25.0% | 90.09% | ₹32.30 L |
| East | 1,233 | 12.0% | 89.78% | ₹17.47 L |
| Central | 903 | 8.8% | 88.37% | ₹7.60 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 22 | 72.73% | ₹2.30 L |
| Rapid Bazaar | Key Account | Retail | 300 | 88.67% | ₹1.35 L |
| Ujjwal Water Board | Key Account | Bills | 36 | 83.33% | ₹1.18 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 91.80% | ₹1.17 L |
| Hampi Styles | Key Account | Retail | 31 | 93.55% | ₹77,503 |
| Girnar Connect | Key Account | Bills | 165 | 88.48% | ₹63,087 |
| Trinetra Restaurant | Large | Food & Beverage | 13 | 92.31% | ₹50,951 |
| Urban Boutique | Key Account | Retail | 86 | 90.70% | ₹49,111 |

## Failure analysis

Of 998 declined attempts, 422 were business declines (4.105% of attempts — balances, PINs and limits), 171 technical (1.663%), 388 timeouts (3.774%) and 17 risk declines (0.165%).

501 attempts were re-presentations of an earlier failure (4.87% of the day); 38.3% of them succeeded.

- Decline code BT (Acquirer / NPCI switch timeout) fired 146 times — 1.420% of attempts against a trailing 0.101%. Owner: NPCI.
- Decline code U54 (Transaction timed out at beneficiary) fired 182 times — 1.770% of attempts against a trailing 0.158%. Owner: Issuer.
- Retries reached 501 attempts (4.87% of the day, 18.2 sigma above normal). Only 38.3% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 60 times — 0.584% of attempts against a trailing 0.045%. Owner: NPCI.
- Decline code U30 (Debit failed at remitter bank) fired 73 times — 0.710% of attempts against a trailing 0.179%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 191 | 1.858% | 1.082% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 182 | 1.770% | 0.158% |
| Z9 | Insufficient funds | business | Customer | 150 | 1.459% | 1.332% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 146 | 1.420% | 0.101% |
| U30 | Debit failed at remitter bank | technical | Issuer | 73 | 0.710% | 0.179% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 60 | 0.584% | 0.045% |
| U28 | Remitter bank unavailable | technical | Issuer | 47 | 0.457% | 0.114% |
| ZA | Transaction declined by customer | business | Customer | 41 | 0.399% | 0.391% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 79 | 78 |
| Auto-reversals | 67 | 24 |
| Disputes / chargebacks | 12 | 10 |
| Value returned | ₹1.94 L | ₹1.22 L |

## Customer behaviour

8,487 distinct customers transacted (−15.9% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,643 | 3,084 | 1.17 | 88.94% | ₹1,380 |
| power | 1,848 | 2,436 | 1.32 | 91.26% | ₹1,787 |
| merchant_heavy | 1,926 | 2,313 | 1.20 | 90.36% | ₹1,067 |
| small_ticket | 1,307 | 1,603 | 1.23 | 90.64% | ₹529 |
| occasional | 600 | 659 | 1.10 | 90.44% | ₹1,212 |
| new | 144 | 166 | 1.15 | 84.94% | ₹574 |
| dormant_returning | 19 | 19 | 1.00 | 94.74% | ₹687 |

## Operational events

- **INC-NET-0035** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 19:00 and 24:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code BT (Acquirer / NPCI switch timeout) fired 146 times — 1.420% of attempts against a trailing 0.101%. Owner: NPCI.
- Decline code U54 (Transaction timed out at beneficiary) fired 182 times — 1.770% of attempts against a trailing 0.158%. Owner: Issuer.
- Success rate closed at 90.12%, 5.68pp down the trailing median — a 22.0-sigma move.
- Retries reached 501 attempts (4.87% of the day, 18.2 sigma above normal). Only 38.3% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 60 times — 0.584% of attempts against a trailing 0.045%. Owner: NPCI.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

26 March was an incident day: INC-NET-0035 was live and the rail closed at 90.12% success against a 95.79% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,280, successes=9,264, failed=998, pending=18, settled_value_inr=12,830,642.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=BT; count=146; rate_pct=1.42; trailing_rate_pct=0.1; owner=NPCI; z=42.96
- failures: failure_code=U54; count=182; rate_pct=1.77; trailing_rate_pct=0.16; owner=Issuer; z=34.65
- headline: success_rate=90.12; trailing_median=95.79; z=-21.96
- failures: retries=501; retry_share_pct=4.87; recovery_pct=38.32; z=18.22
- failures: failure_code=U67; count=60; rate_pct=0.58; trailing_rate_pct=0.05; owner=NPCI; z=24.11
- psps: payer_psp=PhonePe; attempts=4,763; success_rate=90.3; own_median=95.95; z=-16.63
- failures: failure_code=U30; count=73; rate_pct=0.71; trailing_rate_pct=0.18; owner=Issuer; z=13.58
- geography: region=North; attempts=2,607; success_rate=89.91; own_median=95.92; z=-19.37
- psps: payer_psp=Google Pay; attempts=3,360; success_rate=90.18; own_median=95.71; z=-15.56
- banks: payer_bank=State Bank of India; attempts=3,329; success_rate=89.94; own_median=95.72; z=-15.4

Refs: enterprise_data/warehouse/transactions, RPT-D80-DAILY, enterprise_data/warehouse/reference/incidents.parquet
