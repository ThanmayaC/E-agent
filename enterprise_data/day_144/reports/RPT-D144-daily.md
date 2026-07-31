---
id: RPT-D144-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-28T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 28 May 2026)

**Report ID:** RPT-D144-DAILY · **Day 144 of 206** · **Derived from:** 13,277 transaction rows queried live from the warehouse

## Summary

The rail took **13,277 payment attempts** on Thursday 28 May 2026 (Working day) and settled **₹1.82 Cr** across 12,692 successful payments. Volume was −13.6% on yesterday and +0.9% on the same weekday last week. Success closed at **95.59%**, below the trailing 28-day median of 96.08%.

Decline code Z9 (Insufficient funds) fired 208 times — 1.567% of attempts against a trailing 1.181%. Owner: Customer. Issuer State Bank of India ran at 95.03% success on 4,227 attempts (31.8% of the day), 1.01pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,277 | −13.6% | +0.9% | 14,763 |
| Successful payments | 12,692 | −14.1% | +0.1% | 14,161 |
| Success rate | 95.59% | −0.49pp | −0.78pp | 95.92% |
| Settled value | ₹1.82 Cr | −7.0% | +0.0% | ₹1.97 Cr |
| Average ticket | ₹1,436 | +8.2% | −0.1% | ₹1,388 |
| Technical declines | 0.550% | +0.03pp | +0.22pp | 0.510% |
| Business declines | 3.337% | +0.42pp | +0.50pp | 2.946% |
| Risk declines | 0.121% | +0.02pp | +0.01pp | 0.128% |
| Timeout declines | 0.301% | −0.03pp | +0.02pp | 0.392% |
| Retry share | 1.33% | +0.02pp | +0.05pp | 1.35% |
| Latency p95 | 1,302 ms | +3.1% | +3.6% | 1,285 ms |
| Active customers | 11,141 | −11.1% | +1.2% | 12,058 |
| Active merchants | 1,502 | −2.5% | +2.9% | 1,501 |

## What moved

- Issuer State Bank of India ran at 95.03% success on 4,227 attempts (31.8% of the day), 1.01pp down its own 28-day median.
- Region West ran at 94.66% success on 3,335 attempts (25.1% of the day), 1.32pp down its own 28-day median.
- Success rate closed at 95.59%, 0.49pp down the trailing median — a 2.0-sigma move.
- Product UPI Person to Person ran at 94.56% success on 3,568 attempts (26.9% of the day), 0.61pp down its own 28-day median.
- Product UPI International is compounding — attempts up 28% across the trailing window to 210 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,568 | 26.9% | 94.56% | ₹35.88 L | −20.6% |
| UPI Person to Merchant | 3,516 | 26.5% | 95.42% | ₹31.85 L | −10.3% |
| UPI QR Payments | 2,347 | 17.7% | 97.02% | ₹10.41 L | −3.4% |
| UPI Lite | 1,701 | 12.8% | 98.94% | ₹1.49 L | −1.6% |
| UPI Circle | 603 | 4.5% | 95.69% | ₹4.67 L | +7.5% |
| RuPay Credit on UPI | 362 | 2.7% | 96.13% | ₹26.72 L | −1.6% |
| UPI AutoPay | 357 | 2.7% | 83.47% | ₹6.38 L | +8.3% |
| Credit on UPI | 346 | 2.6% | 96.82% | ₹25.72 L | −2.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,227 | 95.03% | 96.05% | ₹51.59 L | ⚠ outlier |
| HDFC Bank | 1,440 | 95.69% | 96.20% | ₹20.04 L | normal |
| Bank of Baroda | 1,061 | 97.08% | 95.88% | ₹20.07 L | normal |
| Union Bank of India | 919 | 95.21% | 95.72% | ₹12.81 L | normal |
| Punjab National Bank | 855 | 96.02% | 95.70% | ₹11.17 L | normal |
| Axis Bank | 831 | 96.27% | 96.62% | ₹11.82 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,191 | 96.01% | 96.00% | ₹83.53 L | normal |
| Google Pay | 4,504 | 95.20% | 95.99% | ₹55.21 L | normal |
| Paytm | 1,075 | 94.70% | 96.14% | ₹16.46 L | ⚠ outlier |
| Navi | 506 | 95.06% | 95.71% | ₹6.61 L | normal |
| SuperMoney | 263 | 95.44% | 96.26% | ₹9.58 L | normal |
| BHIM | 114 | 94.74% | 95.51% | ₹2.86 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,742 | 96.63% | ₹43.85 L |
| Food & Beverage | 2,308 | 96.62% | ₹11.38 L |
| Bills | 1,256 | 94.43% | ₹10.90 L |
| Mobility | 1,124 | 97.15% | ₹5.53 L |
| Healthcare | 492 | 97.76% | ₹4.55 L |
| Digital | 268 | 89.55% | ₹1.56 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,908 | 29.4% | 95.93% | ₹57.38 L |
| North | 3,344 | 25.2% | 95.84% | ₹42.60 L |
| West | 3,335 | 25.1% | 94.66% | ₹51.08 L |
| East | 1,590 | 12.0% | 95.91% | ₹15.97 L |
| Central | 1,100 | 8.3% | 96.00% | ₹15.20 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Trinetra Restaurant | Large | Food & Beverage | 20 | 95.00% | ₹2.10 L |
| Ujjwal Water Board | Key Account | Bills | 68 | 89.71% | ₹1.93 L |
| Vega Electronics | Large | Retail | 26 | 92.31% | ₹1.56 L |
| Rapid Bazaar | Key Account | Retail | 328 | 97.87% | ₹1.52 L |
| Hampi Styles | Key Account | Retail | 46 | 95.65% | ₹1.35 L |
| Vasant Wardrobe | Key Account | Retail | 75 | 97.33% | ₹1.22 L |
| Girnar Connect | Key Account | Bills | 214 | 98.13% | ₹88,948 |
| Urban Boutique | Key Account | Retail | 106 | 98.11% | ₹66,327 |

## Failure analysis

Of 572 declined attempts, 443 were business declines (3.337% of attempts — balances, PINs and limits), 73 technical (0.550%), 40 timeouts (0.301%) and 16 risk declines (0.121%).

176 attempts were re-presentations of an earlier failure (1.33% of the day); 64.2% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 208 times — 1.567% of attempts against a trailing 1.181%. Owner: Customer.
- Decline code U30 (Debit failed at remitter bank) fired 38 times — 0.286% of attempts against a trailing 0.206%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 208 | 1.567% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 144 | 1.085% | 0.981% |
| ZA | Transaction declined by customer | business | Customer | 51 | 0.384% | 0.339% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.286% | 0.206% |
| XH | Account does not exist / frozen | business | Issuer | 20 | 0.151% | 0.223% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.143% | 0.152% |
| U28 | Remitter bank unavailable | technical | Issuer | 15 | 0.113% | 0.135% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 13 | 0.098% | 0.106% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 114 | 102 |
| Auto-reversals | 23 | 28 |
| Disputes / chargebacks | 10 | 13 |
| Value returned | ₹3.45 L | ₹1.98 L |

## Customer behaviour

11,141 distinct customers transacted (−7.1% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,389 | 3,821 | 1.13 | 95.94% | ₹1,676 |
| power | 2,380 | 3,149 | 1.32 | 95.49% | ₹1,924 |
| merchant_heavy | 2,548 | 3,036 | 1.19 | 95.29% | ₹965 |
| small_ticket | 1,681 | 2,055 | 1.22 | 95.91% | ₹634 |
| occasional | 926 | 977 | 1.06 | 94.37% | ₹1,304 |
| new | 188 | 208 | 1.11 | 97.12% | ₹1,080 |
| dormant_returning | 29 | 31 | 1.07 | 100.00% | ₹943 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **DORM-0072** (Sev-3) — East region customer dormancy wave, scoped to East. A cohort of East-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 208 times — 1.567% of attempts against a trailing 1.181%. Owner: Customer.
- Issuer State Bank of India ran at 95.03% success on 4,227 attempts (31.8% of the day), 1.01pp down its own 28-day median.
- Region West ran at 94.66% success on 3,335 attempts (25.1% of the day), 1.32pp down its own 28-day median.
- Success rate closed at 95.59%, 0.49pp down the trailing median — a 2.0-sigma move.
- Product UPI Person to Person ran at 94.56% success on 3,568 attempts (26.9% of the day), 0.61pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 28% across the trailing window to 210 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

28 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 95.59% success against a 96.08% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-28` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,277, successes=12,692, failed=572, pending=13, settled_value_inr=18,223,036.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=208; rate_pct=1.57; trailing_rate_pct=1.18; owner=Customer; z=5
- banks: payer_bank=State Bank of India; attempts=4,227; success_rate=95.03; own_median=96.05; z=-3.38
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- geography: region=West; attempts=3,335; success_rate=94.66; own_median=95.98; z=-3.19
- headline: success_rate=95.59; trailing_median=96.08; z=-1.96
- products: product_name=UPI Person to Person; attempts=3,568; success_rate=94.56; own_median=95.17; z=-2.65
- failures: failure_code=U30; count=38; rate_pct=0.29; trailing_rate_pct=0.21; owner=Issuer; z=2.17
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI International; attempts=210; window_growth_pct=27.9; success_rate=95.71
- psps: payer_psp=Paytm; attempts=1,075; success_rate=94.7; own_median=96.14; z=-2.39

Refs: enterprise_data/warehouse/transactions, RPT-D143-DAILY, enterprise_data/warehouse/reference/incidents.parquet
