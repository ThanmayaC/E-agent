---
id: RPT-D14-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 18 Jan 2026)

**Report ID:** RPT-D14-DAILY · **Day 14 of 206** · **Derived from:** 9,168 transaction rows queried live from the warehouse

## Summary

The rail took **9,168 payment attempts** on Sunday 18 January 2026 (Weekend) and settled **₹93.23 L** across 8,626 successful payments. Volume was −19.9% on yesterday and +2.3% on the same weekday last week. Success closed at **94.09%**, below the trailing 28-day median of 95.45%.

Decline code ZM (Invalid UPI PIN) fired 141 times — 1.538% of attempts against a trailing 1.095%. Owner: Customer. Decline code Z9 (Insufficient funds) fired 170 times — 1.854% of attempts against a trailing 1.459%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,168 | −19.9% | +2.3% | 10,317 |
| Successful payments | 8,626 | −20.8% | +2.1% | 9,820 |
| Success rate | 94.09% | −1.04pp | −0.22pp | 95.16% |
| Settled value | ₹93.23 L | −23.4% | +0.8% | ₹1.17 Cr |
| Average ticket | ₹1,081 | −3.4% | −1.3% | ₹1,186 |
| Technical declines | 0.774% | −0.03pp | +0.00pp | 0.628% |
| Business declines | 4.385% | +0.94pp | +0.05pp | 3.530% |
| Risk declines | 0.196% | +0.08pp | +0.04pp | 0.137% |
| Timeout declines | 0.447% | +0.05pp | +0.12pp | 0.402% |
| Retry share | 1.91% | +0.53pp | +0.15pp | 1.46% |
| Latency p95 | 1,301 ms | +8.4% | +7.9% | 1,243 ms |
| Active customers | 7,865 | −18.0% | +1.7% | 8,745 |
| Active merchants | 1,153 | −7.9% | +0.8% | 1,203 |

## What moved

- App PhonePe ran at 94.36% success on 4,256 attempts (46.4% of the day), 1.18pp down its own 28-day median.
- Region West carried 2,165 attempts, 14% down its trailing median and 23.6% of the day's volume.
- Success rate closed at 94.09%, 1.36pp down the trailing median — a 2.9-sigma move.
- Category Retail ran at 94.76% success on 2,464 attempts (42.6% of the day), 1.23pp down its own 28-day median.
- Attempt volume ran 3.7 standard deviations down its trailing 28-day median at 9,168, 2.3% up on the same weekday last week.
- Issuer HDFC Bank ran at 94.19% success on 981 attempts (10.7% of the day), 1.98pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,379 | 36.9% | 93.61% | ₹35.18 L | −16.0% |
| UPI Person to Merchant | 2,924 | 31.9% | 94.97% | ₹25.24 L | −2.4% |
| UPI QR Payments | 1,466 | 16.0% | 94.27% | ₹5.62 L | −17.7% |
| UPI Lite | 567 | 6.2% | 98.24% | ₹49,068 | −15.5% |
| UPI AutoPay | 307 | 3.3% | 84.04% | ₹4.70 L | +1.0% |
| RuPay Credit on UPI | 109 | 1.2% | 93.58% | ₹5.61 L | −40.4% |
| UPI Circle | 103 | 1.1% | 92.23% | ₹79,440 | +12.0% |
| UPI Lite Auto Top-Up | 87 | 0.9% | 100.00% | ₹98,403 | +4.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 2,950 | 93.86% | 94.93% | ₹27.66 L | normal |
| HDFC Bank | 981 | 94.19% | 96.17% | ₹8.66 L | ⚠ outlier |
| Bank of Baroda | 663 | 93.51% | 94.46% | ₹7.42 L | normal |
| Union Bank of India | 634 | 93.22% | 95.02% | ₹7.64 L | normal |
| ICICI Bank | 568 | 96.30% | 95.92% | ₹6.20 L | normal |
| Axis Bank | 563 | 94.85% | 95.44% | ₹5.16 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,256 | 94.36% | 95.55% | ₹39.92 L | ⚠ outlier |
| Google Pay | 3,071 | 94.17% | 95.24% | ₹33.67 L | normal |
| Paytm | 750 | 92.80% | 94.78% | ₹8.66 L | ⚠ outlier |
| Navi | 360 | 91.94% | 95.56% | ₹3.76 L | ⚠ outlier |
| SuperMoney | 179 | 93.30% | 96.10% | ₹1.87 L | ⚠ outlier |
| BHIM | 97 | 93.81% | 95.50% | ₹74,844 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,464 | 94.76% | ₹19.11 L |
| Food & Beverage | 1,331 | 95.42% | ₹6.44 L |
| Mobility | 621 | 94.52% | ₹2.96 L |
| Bills | 612 | 95.42% | ₹6.24 L |
| Healthcare | 297 | 93.27% | ₹3.08 L |
| Digital | 188 | 93.09% | ₹1.04 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,727 | 29.7% | 94.13% | ₹27.85 L |
| North | 2,374 | 25.9% | 94.02% | ₹25.20 L |
| West | 2,165 | 23.6% | 93.72% | ₹22.74 L |
| East | 1,089 | 11.9% | 94.49% | ₹10.79 L |
| Central | 813 | 8.9% | 94.59% | ₹6.65 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 272 | 94.49% | ₹1.05 L |
| Vega Electronics | Large | Retail | 20 | 80.00% | ₹95,638 |
| Vasant Wardrobe | Key Account | Retail | 56 | 98.21% | ₹85,915 |
| Ujjwal Water Board | Key Account | Bills | 27 | 96.30% | ₹68,730 |
| Yamuna Restaurant | Key Account | Food & Beverage | 60 | 96.67% | ₹66,110 |
| Girnar Connect | Key Account | Bills | 108 | 97.22% | ₹48,906 |
| Urban Boutique | Key Account | Retail | 81 | 96.30% | ₹44,780 |
| Swift Mart 1738 | Key Account | Retail | 96 | 93.75% | ₹44,654 |

## Failure analysis

Of 532 declined attempts, 402 were business declines (4.385% of attempts — balances, PINs and limits), 71 technical (0.774%), 41 timeouts (0.447%) and 18 risk declines (0.196%).

175 attempts were re-presentations of an earlier failure (1.91% of the day); 67.4% of them succeeded.

- Decline code ZM (Invalid UPI PIN) fired 141 times — 1.538% of attempts against a trailing 1.095%. Owner: Customer.
- Decline code Z9 (Insufficient funds) fired 170 times — 1.854% of attempts against a trailing 1.459%. Owner: Customer.
- Retries reached 175 attempts (1.91% of the day, 3.4 sigma above normal). 67.4% of re-presented payments recovered, so the retry path was doing its job.
- Decline code ZA (Transaction declined by customer) fired 45 times — 0.491% of attempts against a trailing 0.371%. Owner: Customer.
- Decline code U16 (Risk threshold exceeded at remitter) fired 18 times — 0.196% of attempts against a trailing 0.113%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 170 | 1.854% | 1.459% |
| ZM | Invalid UPI PIN | business | Customer | 141 | 1.538% | 1.095% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.491% | 0.371% |
| U30 | Debit failed at remitter bank | technical | Issuer | 30 | 0.327% | 0.262% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.273% | 0.262% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.229% | 0.184% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.207% | 0.173% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.196% | 0.113% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 70 | 26 |
| Auto-reversals | 21 | 23 |
| Disputes / chargebacks | 1 | 0 |
| Value returned | ₹1.18 L | ₹50,185 |

## Customer behaviour

7,865 distinct customers transacted (−11.4% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,400 | 2,690 | 1.12 | 94.28% | ₹1,210 |
| power | 1,724 | 2,208 | 1.28 | 93.39% | ₹1,398 |
| merchant_heavy | 1,812 | 2,100 | 1.16 | 94.48% | ₹720 |
| small_ticket | 1,154 | 1,362 | 1.18 | 94.13% | ₹460 |
| occasional | 596 | 619 | 1.04 | 94.35% | ₹1,189 |
| new | 157 | 167 | 1.06 | 94.01% | ₹524 |
| dormant_returning | 22 | 22 | 1.00 | 95.45% | ₹843 |

## Operational events

No incident, campaign or maintenance window overlapped this date in the operational record.

## Risks and opportunities

### Risks

- Decline code ZM (Invalid UPI PIN) fired 141 times — 1.538% of attempts against a trailing 1.095%. Owner: Customer.
- Decline code Z9 (Insufficient funds) fired 170 times — 1.854% of attempts against a trailing 1.459%. Owner: Customer.
- App PhonePe ran at 94.36% success on 4,256 attempts (46.4% of the day), 1.18pp down its own 28-day median.
- Success rate closed at 94.09%, 1.36pp down the trailing median — a 2.9-sigma move.
- Category Retail ran at 94.76% success on 2,464 attempts (42.6% of the day), 1.23pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 18 January: success came in 1.36pp below baseline at 94.09% on 9,168 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,168, successes=8,626, failed=532, pending=10, settled_value_inr=9,323,248.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=ZM; count=141; rate_pct=1.54; trailing_rate_pct=1.1; owner=Customer; z=3.74
- failures: failure_code=Z9; count=170; rate_pct=1.85; trailing_rate_pct=1.46; owner=Customer; z=3.08
- psps: payer_psp=PhonePe; attempts=4,256; success_rate=94.36; own_median=95.55; z=-4.82
- failures: retries=175; retry_share_pct=1.91; recovery_pct=67.43; z=3.4
- geography: region=West; attempts=2,165; own_median=2,519; z=-6.63
- headline: success_rate=94.09; trailing_median=95.45; z=-2.88
- categories: mcc_category=Retail; attempts=2,464; success_rate=94.76; own_median=96; z=-3.46
- headline: attempts=9,168; trailing_median=10,484; z=-3.65
- banks: payer_bank=HDFC Bank; attempts=981; success_rate=94.19; own_median=96.17; z=-5.4
- geography: region=South; attempts=2,727; success_rate=94.13; own_median=95.55; z=-2.51

Refs: enterprise_data/warehouse/transactions, RPT-D13-DAILY, enterprise_data/warehouse/reference/incidents.parquet
