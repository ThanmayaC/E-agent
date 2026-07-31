---
id: RPT-D91-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 05 Apr 2026)

**Report ID:** RPT-D91-DAILY · **Day 91 of 206** · **Derived from:** 12,563 transaction rows queried live from the warehouse

## Summary

The rail took **12,563 payment attempts** on Sunday 05 April 2026 (Weekend) and settled **₹1.27 Cr** across 11,354 successful payments. Volume was −14.2% on yesterday and +16.2% on the same weekday last week. Success closed at **90.38%**, below the trailing 28-day median of 95.84%.

Decline code U54 (Transaction timed out at beneficiary) fired 259 times — 2.062% of attempts against a trailing 0.155%. Owner: Issuer. Decline code BT (Acquirer / NPCI switch timeout) fired 161 times — 1.282% of attempts against a trailing 0.103%. Owner: NPCI.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,563 | −14.2% | +16.2% | 13,050 |
| Successful payments | 11,354 | −19.2% | +10.3% | 12,391 |
| Success rate | 90.38% | −5.57pp | −4.83pp | 94.91% |
| Settled value | ₹1.27 Cr | −34.1% | +6.7% | ₹1.68 Cr |
| Average ticket | ₹1,121 | −18.5% | −3.3% | ₹1,354 |
| Technical declines | 1.783% | +1.35pp | +1.36pp | 0.689% |
| Business declines | 3.526% | +0.58pp | −0.32pp | 3.055% |
| Risk declines | 0.223% | +0.03pp | +0.07pp | 0.165% |
| Timeout declines | 3.845% | +3.49pp | +3.64pp | 1.036% |
| Retry share | 4.52% | +3.40pp | +3.26pp | 1.83% |
| Latency p95 | 2,169 ms | +73.9% | +78.9% | 1,446 ms |
| Active customers | 10,172 | −14.5% | +10.1% | 10,744 |
| Active merchants | 1,375 | −4.5% | +4.7% | 1,391 |

## What moved

- Success rate closed at 90.38%, 5.46pp down the trailing median — a 18.1-sigma move.
- App PhonePe ran at 90.43% success on 6,041 attempts (48.1% of the day), 5.45pp down its own 28-day median.
- Product UPI Person to Person ran at 89.51% success on 3,993 attempts (31.8% of the day), 5.77pp down its own 28-day median.
- Issuer State Bank of India ran at 90.65% success on 4,011 attempts (31.9% of the day), 5.17pp down its own 28-day median.
- Region North ran at 91.23% success on 3,055 attempts (24.3% of the day), 4.65pp down its own 28-day median.
- Category Food & Beverage ran at 90.17% success on 2,014 attempts (23.5% of the day), 6.58pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,993 | 31.8% | 89.51% | ₹39.64 L | −8.3% |
| UPI Person to Merchant | 3,497 | 27.8% | 90.19% | ₹31.90 L | +2.3% |
| UPI QR Payments | 2,343 | 18.7% | 90.74% | ₹9.48 L | +12.6% |
| UPI Lite | 1,468 | 11.7% | 94.28% | ₹1.21 L | +56.6% |
| UPI AutoPay | 358 | 2.8% | 86.59% | ₹6.15 L | +12.2% |
| UPI Circle | 288 | 2.3% | 88.89% | ₹2.39 L | +30.6% |
| RuPay Credit on UPI | 167 | 1.3% | 88.62% | ₹13.11 L | −33.3% |
| Credit on UPI | 119 | 0.9% | 87.39% | ₹8.33 L | −29.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,011 | 90.65% | 95.82% | ₹40.97 L | ⚠ outlier |
| HDFC Bank | 1,351 | 90.60% | 95.59% | ₹14.88 L | ⚠ outlier |
| Bank of Baroda | 958 | 90.81% | 96.02% | ₹10.43 L | ⚠ outlier |
| Union Bank of India | 880 | 88.64% | 95.64% | ₹11.05 L | ⚠ outlier |
| ICICI Bank | 795 | 89.18% | 95.76% | ₹6.96 L | ⚠ outlier |
| Punjab National Bank | 754 | 89.66% | 95.23% | ₹6.81 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,041 | 90.43% | 95.88% | ₹59.37 L | ⚠ outlier |
| Google Pay | 4,104 | 90.52% | 95.68% | ₹42.87 L | ⚠ outlier |
| Paytm | 975 | 89.44% | 96.03% | ₹11.32 L | ⚠ outlier |
| Navi | 452 | 92.26% | 95.74% | ₹4.26 L | ⚠ outlier |
| SuperMoney | 249 | 87.95% | 94.77% | ₹2.15 L | ⚠ outlier |
| BHIM | 145 | 88.97% | 95.88% | ₹1.90 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,157 | 91.35% | ₹24.84 L |
| Food & Beverage | 2,014 | 90.17% | ₹9.21 L |
| Bills | 1,343 | 90.69% | ₹13.31 L |
| Mobility | 992 | 91.83% | ₹5.13 L |
| Healthcare | 376 | 92.29% | ₹3.41 L |
| Digital | 305 | 88.85% | ₹1.55 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,816 | 30.4% | 90.67% | ₹37.72 L |
| North | 3,055 | 24.3% | 91.23% | ₹30.42 L |
| West | 3,047 | 24.3% | 89.86% | ₹31.99 L |
| East | 1,578 | 12.6% | 88.78% | ₹17.35 L |
| Central | 1,067 | 8.5% | 90.72% | ₹9.81 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 308 | 90.91% | ₹1.13 L |
| Ujjwal Water Board | Key Account | Bills | 75 | 88.00% | ₹94,289 |
| Girnar Connect | Key Account | Bills | 223 | 90.58% | ₹85,623 |
| Vasant Wardrobe | Key Account | Retail | 39 | 87.18% | ₹66,870 |
| Yamuna Restaurant | Key Account | Food & Beverage | 63 | 93.65% | ₹62,361 |
| Hampi Stores 2298 | Key Account | Retail | 102 | 89.22% | ₹51,295 |
| Vega Electronics | Large | Retail | 12 | 100.00% | ₹50,062 |
| Urban Boutique | Key Account | Retail | 93 | 92.47% | ₹49,237 |

## Failure analysis

Of 1,178 declined attempts, 443 were business declines (3.526% of attempts — balances, PINs and limits), 224 technical (1.783%), 483 timeouts (3.845%) and 28 risk declines (0.223%).

568 attempts were re-presentations of an earlier failure (4.52% of the day); 38.7% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 259 times — 2.062% of attempts against a trailing 0.155%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 161 times — 1.282% of attempts against a trailing 0.103%. Owner: NPCI.
- Retries reached 568 attempts (4.52% of the day, 15.7 sigma above normal). Only 38.7% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 63 times — 0.501% of attempts against a trailing 0.045%. Owner: NPCI.
- Decline code U30 (Debit failed at remitter bank) fired 96 times — 0.764% of attempts against a trailing 0.191%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 259 | 2.062% | 0.155% |
| ZM | Invalid UPI PIN | business | Customer | 172 | 1.369% | 1.056% |
| Z9 | Insufficient funds | business | Customer | 169 | 1.345% | 1.332% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 161 | 1.282% | 0.103% |
| U30 | Debit failed at remitter bank | technical | Issuer | 96 | 0.764% | 0.191% |
| U28 | Remitter bank unavailable | technical | Issuer | 70 | 0.557% | 0.116% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 63 | 0.501% | 0.045% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.342% | 0.364% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 76 | 74 |
| Auto-reversals | 78 | 24 |
| Disputes / chargebacks | 8 | 10 |
| Value returned | ₹3.11 L | ₹1.33 L |

## Customer behaviour

10,172 distinct customers transacted (+2.3% on the 28-day median) at 1.24 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,101 | 3,639 | 1.17 | 90.19% | ₹1,044 |
| power | 2,189 | 2,945 | 1.35 | 90.90% | ₹1,534 |
| merchant_heavy | 2,328 | 2,918 | 1.25 | 90.37% | ₹783 |
| small_ticket | 1,521 | 1,917 | 1.26 | 91.08% | ₹551 |
| occasional | 828 | 909 | 1.10 | 89.22% | ₹1,045 |
| new | 181 | 211 | 1.17 | 85.31% | ₹554 |
| dormant_returning | 24 | 24 | 1.00 | 87.50% | ₹211 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-NET-0043** (Sev-1) — NPCI switch latency degradation, scoped to ecosystem-wide between 10:00 and 13:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **INC-NET-0039** (Sev-2) — NPCI switch latency degradation, scoped to ecosystem-wide between 20:00 and 24:00. Central switch p95 response time degraded across all PSPs. Timeout-class declines (BT, U54) rose ecosystem-wide with no single issuer or app responsible.
- **INC-PSP-0028** (Sev-3) — Axis Mobile app release regression, scoped to Axis Mobile between 19:00 and 23:00. A Axis Mobile client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U54 (Transaction timed out at beneficiary) fired 259 times — 2.062% of attempts against a trailing 0.155%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 161 times — 1.282% of attempts against a trailing 0.103%. Owner: NPCI.
- Retries reached 568 attempts (4.52% of the day, 15.7 sigma above normal). Only 38.7% of re-presented payments eventually succeeded, so the queue was absorbing failures rather than clearing them.
- Success rate closed at 90.38%, 5.46pp down the trailing median — a 18.1-sigma move.
- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 63 times — 0.501% of attempts against a trailing 0.045%. Owner: NPCI.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

05 April was an incident day: INC-FRAUD-0044, INC-NET-0043 were live and the rail closed at 90.38% success against a 95.84% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,563, successes=11,354, failed=1,178, pending=31, settled_value_inr=12,729,256.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=U54; count=259; rate_pct=2.06; trailing_rate_pct=0.16; owner=Issuer; z=39.84
- failures: failure_code=BT; count=161; rate_pct=1.28; trailing_rate_pct=0.1; owner=NPCI; z=45.99
- failures: retries=568; retry_share_pct=4.52; recovery_pct=38.73; z=15.72
- headline: success_rate=90.38; trailing_median=95.84; z=-18.15
- failures: failure_code=U67; count=63; rate_pct=0.5; trailing_rate_pct=0.05; owner=NPCI; z=17.99
- failures: failure_code=U30; count=96; rate_pct=0.76; trailing_rate_pct=0.19; owner=Issuer; z=14.06
- psps: payer_psp=PhonePe; attempts=6,041; success_rate=90.43; own_median=95.88; z=-12.38
- products: product_name=UPI Person to Person; attempts=3,993; success_rate=89.51; own_median=95.28; z=-14.59
- banks: payer_bank=State Bank of India; attempts=4,011; success_rate=90.65; own_median=95.82; z=-13.01
- geography: region=North; attempts=3,055; success_rate=91.23; own_median=95.87; z=-13.9

Refs: enterprise_data/warehouse/transactions, RPT-D90-DAILY, enterprise_data/warehouse/reference/incidents.parquet
