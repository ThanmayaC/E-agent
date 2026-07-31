---
id: RPT-D111-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 25 Apr 2026)

**Report ID:** RPT-D111-DAILY · **Day 111 of 206** · **Derived from:** 13,074 transaction rows queried live from the warehouse

## Summary

The rail took **13,074 payment attempts** on Saturday 25 April 2026 (Weekend) and settled **₹1.58 Cr** across 12,477 successful payments. Volume was +12.9% on yesterday and −19.2% on the same weekday last week. Success closed at **95.43%**, below the trailing 28-day median of 95.92%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,074 | +12.9% | −19.2% | 12,776 |
| Successful payments | 12,477 | +13.6% | −19.8% | 12,178 |
| Success rate | 95.43% | +0.55pp | −0.67pp | 95.28% |
| Settled value | ₹1.58 Cr | +6.5% | −17.7% | ₹1.65 Cr |
| Average ticket | ₹1,267 | −6.2% | +2.6% | ₹1,354 |
| Technical declines | 0.474% | −0.24pp | +0.16pp | 0.587% |
| Business declines | 3.442% | −0.10pp | +0.49pp | 3.186% |
| Risk declines | 0.145% | +0.01pp | +0.06pp | 0.143% |
| Timeout declines | 0.421% | −0.18pp | −0.03pp | 0.684% |
| Retry share | 1.42% | +0.04pp | −1.27pp | 1.65% |
| Latency p95 | 1,225 ms | −7.1% | −1.8% | 1,340 ms |
| Active customers | 10,930 | +11.0% | −15.8% | 10,604 |
| Active merchants | 1,395 | +1.3% | −5.0% | 1,387 |

## What moved

- Category Food & Beverage carried 2,352 attempts, 17% up its trailing median and 26.3% of the day's volume.
- Product UPI QR Payments ran at 95.19% success on 2,349 attempts (18.0% of the day), 1.19pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 35% across the trailing window to 495 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle carried 495 attempts, 74% up its trailing median and 3.8% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,119 | 31.5% | 94.85% | ₹42.53 L | −6.1% |
| UPI Person to Merchant | 3,481 | 26.6% | 96.29% | ₹35.30 L | +1.4% |
| UPI QR Payments | 2,349 | 18.0% | 95.19% | ₹9.02 L | +8.2% |
| UPI Lite | 1,520 | 11.6% | 98.82% | ₹1.25 L | +34.7% |
| UPI Circle | 495 | 3.8% | 96.97% | ₹3.67 L | +73.7% |
| UPI AutoPay | 350 | 2.7% | 87.43% | ₹5.61 L | +9.2% |
| RuPay Credit on UPI | 220 | 1.7% | 97.27% | ₹17.47 L | −31.2% |
| Credit on UPI | 184 | 1.4% | 90.22% | ₹16.02 L | −16.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,166 | 95.78% | 95.89% | ₹49.20 L | normal |
| HDFC Bank | 1,476 | 95.66% | 96.04% | ₹19.67 L | normal |
| Bank of Baroda | 965 | 93.78% | 95.88% | ₹11.75 L | ⚠ outlier |
| Union Bank of India | 916 | 94.98% | 95.53% | ₹14.85 L | normal |
| ICICI Bank | 817 | 97.06% | 96.36% | ₹6.64 L | normal |
| Axis Bank | 786 | 95.67% | 95.80% | ₹13.20 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,104 | 95.41% | 95.78% | ₹68.03 L | normal |
| Google Pay | 4,319 | 95.00% | 95.63% | ₹60.61 L | normal |
| Paytm | 1,103 | 95.38% | 95.85% | ₹14.11 L | normal |
| Navi | 521 | 96.55% | 96.40% | ₹3.48 L | normal |
| SuperMoney | 235 | 95.32% | 94.87% | ₹2.08 L | normal |
| FamApp | 130 | 96.92% | 95.97% | ₹2.95 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,686 | 96.26% | ₹44.60 L |
| Food & Beverage | 2,352 | 96.26% | ₹10.34 L |
| Mobility | 1,069 | 96.45% | ₹4.62 L |
| Bills | 753 | 96.15% | ₹6.99 L |
| Healthcare | 485 | 96.29% | ₹5.94 L |
| Digital | 212 | 90.09% | ₹1.02 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,755 | 28.7% | 95.34% | ₹52.17 L |
| West | 3,343 | 25.6% | 95.63% | ₹37.43 L |
| North | 3,252 | 24.9% | 95.69% | ₹36.81 L |
| East | 1,590 | 12.2% | 94.53% | ₹19.24 L |
| Central | 1,134 | 8.7% | 95.68% | ₹12.47 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 30 | 96.67% | ₹2.97 L |
| Rapid Bazaar | Key Account | Retail | 434 | 96.54% | ₹1.43 L |
| Urban Boutique | Key Account | Retail | 101 | 95.05% | ₹87,740 |
| Ujjwal Water Board | Key Account | Bills | 36 | 94.44% | ₹75,300 |
| Vasant Wardrobe | Key Account | Retail | 46 | 97.83% | ₹66,653 |
| Yamuna Restaurant | Key Account | Food & Beverage | 70 | 97.14% | ₹62,554 |
| Trinetra Restaurant | Large | Food & Beverage | 28 | 85.71% | ₹60,436 |
| Swift Mart 1738 | Key Account | Retail | 111 | 99.10% | ₹54,243 |

## Failure analysis

Of 586 declined attempts, 450 were business declines (3.442% of attempts — balances, PINs and limits), 62 technical (0.474%), 55 timeouts (0.421%) and 19 risk declines (0.145%).

185 attempts were re-presentations of an earlier failure (1.42% of the day); 65.9% of them succeeded.

- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 19 times — 0.145% of attempts against a trailing 0.044%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 208 | 1.591% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 1.056% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 52 | 0.398% | 0.384% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.260% | 0.220% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.222% | 0.203% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.168% | 0.199% |
| U67 | Debit reversal timeout — credit not confirmed | timeout | NPCI | 19 | 0.145% | 0.044% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.115% | 0.117% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 97 | 80 |
| Auto-reversals | 29 | 28 |
| Disputes / chargebacks | 10 | 11 |
| Value returned | ₹1.20 L | ₹1.61 L |

## Customer behaviour

10,930 distinct customers transacted (+3.1% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,378 | 3,855 | 1.14 | 95.43% | ₹1,207 |
| merchant_heavy | 2,494 | 3,006 | 1.21 | 95.31% | ₹856 |
| power | 2,260 | 3,005 | 1.33 | 95.34% | ₹2,013 |
| small_ticket | 1,658 | 2,003 | 1.21 | 95.76% | ₹516 |
| occasional | 890 | 940 | 1.06 | 95.11% | ₹1,420 |
| new | 219 | 234 | 1.07 | 96.58% | ₹589 |
| dormant_returning | 31 | 31 | 1.00 | 96.77% | ₹1,066 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0056** (Sev-3) — EdTech cashback campaign, scoped to 8299. A cashback campaign across EdTech merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code U67 (Debit reversal timeout — credit not confirmed) fired 19 times — 0.145% of attempts against a trailing 0.044%. Owner: NPCI.
- Product UPI QR Payments ran at 95.19% success on 2,349 attempts (18.0% of the day), 1.19pp down its own 28-day median.
- Product Credit on UPI is compounding — attempts up 25% across the trailing window to 184 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer Bank of Baroda ran at 93.78% success on 965 attempts (7.4% of the day), 2.10pp down its own 28-day median.
- Category Financial Services ran at 76.92% success on 156 attempts (1.7% of the day), 10.37pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 35% across the trailing window to 495 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

Reliability, not demand, is the story of 25 April: success came in 0.49pp below baseline at 95.43% on 13,074 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,074, successes=12,477, failed=586, pending=11, settled_value_inr=15,812,632.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Food & Beverage; attempts=2,352; own_median=2,017; z=3.27
- failures: failure_code=U67; count=19; rate_pct=0.15; trailing_rate_pct=0.04; owner=NPCI; z=3.72
- products: product_name=UPI QR Payments; attempts=2,349; success_rate=95.19; own_median=96.38; z=-2.72
- products: product_name=UPI Circle; attempts=495; window_growth_pct=34.8; success_rate=96.97
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- products: product_name=UPI Circle; attempts=495; own_median=285; z=5.15
- products: product_name=Credit on UPI; attempts=184; window_growth_pct=25.3; success_rate=90.22
- banks: payer_bank=Bank of Baroda; attempts=965; success_rate=93.78; own_median=95.88; z=-2.5
- categories: mcc_category=Mobility; attempts=1,069; own_median=907.5; z=2.32
- categories: mcc_category=Financial Services; attempts=156; success_rate=76.92; own_median=87.3; z=-3.59

Refs: enterprise_data/warehouse/transactions, RPT-D110-DAILY, enterprise_data/warehouse/reference/incidents.parquet
