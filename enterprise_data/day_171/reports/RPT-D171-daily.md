---
id: RPT-D171-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 24 Jun 2026)

**Report ID:** RPT-D171-DAILY · **Day 171 of 206** · **Derived from:** 12,875 transaction rows queried live from the warehouse

## Summary

The rail took **12,875 payment attempts** on Wednesday 24 June 2026 (Working day) and settled **₹1.62 Cr** across 12,285 successful payments. Volume was −8.0% on yesterday and −4.0% on the same weekday last week. Success closed at **95.42%**, below the trailing 28-day median of 96.28%.

Decline code Z9 (Insufficient funds) fired 223 times — 1.732% of attempts against a trailing 1.187%. Owner: Customer. Success rate closed at 95.42%, 0.86pp down the trailing median — a 3.2-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,875 | −8.0% | −4.0% | 14,896 |
| Successful payments | 12,285 | −8.6% | −4.4% | 14,343 |
| Success rate | 95.42% | −0.65pp | −0.44pp | 96.26% |
| Settled value | ₹1.62 Cr | −5.6% | −8.6% | ₹1.95 Cr |
| Average ticket | ₹1,320 | +3.3% | −4.4% | ₹1,360 |
| Technical declines | 0.450% | −0.09pp | −0.06pp | 0.419% |
| Business declines | 3.619% | +0.65pp | +0.42pp | 2.841% |
| Risk declines | 0.078% | −0.02pp | −0.07pp | 0.123% |
| Timeout declines | 0.334% | +0.07pp | +0.15pp | 0.271% |
| Retry share | 1.27% | +0.15pp | +0.23pp | 1.07% |
| Latency p95 | 1,337 ms | +6.4% | +1.8% | 1,276 ms |
| Active customers | 10,807 | −7.0% | −3.3% | 12,238 |
| Active merchants | 1,504 | −0.7% | −1.7% | 1,544 |

## What moved

- Success rate closed at 95.42%, 0.86pp down the trailing median — a 3.2-sigma move.
- Region South ran at 95.39% success on 3,684 attempts (28.6% of the day), 0.89pp down its own 28-day median.
- App PhonePe ran at 95.26% success on 6,013 attempts (46.7% of the day), 0.91pp down its own 28-day median.
- Issuer State Bank of India ran at 95.11% success on 4,114 attempts (32.0% of the day), 1.16pp down its own 28-day median.
- App Google Pay ran at 95.42% success on 4,301 attempts (33.4% of the day), 0.94pp down its own 28-day median.
- Issuer HDFC Bank ran at 95.09% success on 1,344 attempts (10.4% of the day), 1.37pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,550 | 27.6% | 95.01% | ₹35.34 L | −16.0% |
| UPI Person to Merchant | 2,926 | 22.7% | 95.59% | ₹27.47 L | −19.0% |
| UPI QR Payments | 2,005 | 15.6% | 95.76% | ₹8.38 L | −16.7% |
| UPI Lite | 1,981 | 15.4% | 98.69% | ₹1.79 L | −4.0% |
| UPI Circle | 702 | 5.5% | 96.15% | ₹5.77 L | −1.8% |
| Credit on UPI | 445 | 3.5% | 95.73% | ₹30.48 L | −1.1% |
| RuPay Credit on UPI | 403 | 3.1% | 94.54% | ₹20.51 L | +10.0% |
| UPI AutoPay | 379 | 2.9% | 83.11% | ₹6.55 L | +7.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,114 | 95.11% | 96.28% | ₹53.10 L | ⚠ outlier |
| HDFC Bank | 1,344 | 95.09% | 96.46% | ₹17.03 L | ⚠ outlier |
| Bank of Baroda | 958 | 95.82% | 96.48% | ₹13.41 L | normal |
| Union Bank of India | 903 | 95.57% | 96.32% | ₹10.49 L | normal |
| Axis Bank | 821 | 96.10% | 96.26% | ₹10.73 L | normal |
| ICICI Bank | 785 | 94.65% | 96.54% | ₹8.43 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,013 | 95.26% | 96.17% | ₹81.62 L | ⚠ outlier |
| Google Pay | 4,301 | 95.42% | 96.36% | ₹50.54 L | ⚠ outlier |
| Paytm | 1,102 | 95.55% | 96.28% | ₹13.14 L | normal |
| Navi | 486 | 96.30% | 96.61% | ₹4.47 L | normal |
| SuperMoney | 259 | 95.37% | 96.13% | ₹4.25 L | normal |
| BHIM | 126 | 96.83% | 95.69% | ₹83,717 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,863 | 96.48% | ₹50.05 L |
| Food & Beverage | 2,325 | 96.13% | ₹11.57 L |
| Mobility | 1,185 | 96.54% | ₹5.71 L |
| Bills | 795 | 93.71% | ₹8.39 L |
| Healthcare | 502 | 96.41% | ₹7.78 L |
| Digital | 192 | 89.06% | ₹92,572 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,684 | 28.6% | 95.39% | ₹42.26 L |
| North | 3,272 | 25.4% | 95.54% | ₹38.71 L |
| West | 3,221 | 25.0% | 95.28% | ₹41.84 L |
| East | 1,601 | 12.4% | 95.44% | ₹26.38 L |
| Central | 1,097 | 8.5% | 95.53% | ₹12.98 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 23 | 95.65% | ₹2.24 L |
| Hampi Styles | Key Account | Retail | 41 | 95.12% | ₹1.67 L |
| Rapid Bazaar | Key Account | Retail | 337 | 97.03% | ₹1.51 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 95.31% | ₹1.49 L |
| Ujjwal Water Board | Key Account | Bills | 36 | 94.44% | ₹1.10 L |
| Urban Boutique | Key Account | Retail | 127 | 96.06% | ₹89,305 |
| Trinetra Restaurant | Large | Food & Beverage | 27 | 100.00% | ₹83,181 |
| Hampi Stores 2298 | Key Account | Retail | 103 | 96.12% | ₹70,569 |

## Failure analysis

Of 577 declined attempts, 466 were business declines (3.619% of attempts — balances, PINs and limits), 58 technical (0.450%), 43 timeouts (0.334%) and 10 risk declines (0.078%).

164 attempts were re-presentations of an earlier failure (1.27% of the day); 67.1% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 223 times — 1.732% of attempts against a trailing 1.187%. Owner: Customer.
- Decline code XH (Account does not exist / frozen) fired 33 times — 0.256% of attempts against a trailing 0.200%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 223 | 1.732% | 1.187% |
| ZM | Invalid UPI PIN | business | Customer | 146 | 1.134% | 0.943% |
| ZA | Transaction declined by customer | business | Customer | 39 | 0.303% | 0.348% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.256% | 0.200% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 24 | 0.186% | 0.141% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.179% | 0.173% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.109% | 0.088% |
| U69 | Beneficiary bank offline | technical | Issuer | 13 | 0.101% | 0.080% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 111 | 106 |
| Auto-reversals | 22 | 24 |
| Disputes / chargebacks | 12 | 14 |
| Value returned | ₹2.57 L | ₹1.70 L |

## Customer behaviour

10,807 distinct customers transacted (−11.4% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,340 | 3,778 | 1.13 | 95.05% | ₹1,353 |
| power | 2,340 | 3,125 | 1.34 | 95.46% | ₹1,699 |
| merchant_heavy | 2,547 | 3,050 | 1.20 | 95.80% | ₹1,119 |
| small_ticket | 1,609 | 1,909 | 1.19 | 95.44% | ₹675 |
| occasional | 782 | 814 | 1.04 | 95.70% | ₹1,072 |
| new | 162 | 169 | 1.04 | 94.67% | ₹1,040 |
| dormant_returning | 27 | 30 | 1.11 | 93.33% | ₹1,637 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **MKT-0077** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 223 times — 1.732% of attempts against a trailing 1.187%. Owner: Customer.
- Success rate closed at 95.42%, 0.86pp down the trailing median — a 3.2-sigma move.
- Region South ran at 95.39% success on 3,684 attempts (28.6% of the day), 0.89pp down its own 28-day median.
- App PhonePe ran at 95.26% success on 6,013 attempts (46.7% of the day), 0.91pp down its own 28-day median.
- Issuer State Bank of India ran at 95.11% success on 4,114 attempts (32.0% of the day), 1.16pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 24 June: success came in 0.86pp below baseline at 95.42% on 12,875 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,875, successes=12,285, failed=577, pending=13, settled_value_inr=16,216,571.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=223; rate_pct=1.73; trailing_rate_pct=1.19; owner=Customer; z=6.37
- headline: success_rate=95.42; trailing_median=96.28; z=-3.24
- geography: region=South; attempts=3,684; success_rate=95.39; own_median=96.27; z=-4.16
- psps: payer_psp=PhonePe; attempts=6,013; success_rate=95.26; own_median=96.17; z=-3.14
- banks: payer_bank=State Bank of India; attempts=4,114; success_rate=95.11; own_median=96.28; z=-2.59
- psps: payer_psp=Google Pay; attempts=4,301; success_rate=95.42; own_median=96.36; z=-2.33
- banks: payer_bank=HDFC Bank; attempts=1,344; success_rate=95.09; own_median=96.45; z=-3.96
- geography: region=North; attempts=3,272; success_rate=95.54; own_median=96.31; z=-2.14
- categories: mcc_category=Bills; attempts=795; success_rate=93.71; own_median=96.25; z=-3.43
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07

Refs: enterprise_data/warehouse/transactions, RPT-D170-DAILY, enterprise_data/warehouse/reference/incidents.parquet
