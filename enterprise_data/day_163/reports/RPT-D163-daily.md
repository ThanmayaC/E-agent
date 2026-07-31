---
id: RPT-D163-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 16 Jun 2026)

**Report ID:** RPT-D163-DAILY · **Day 163 of 206** · **Derived from:** 13,749 transaction rows queried live from the warehouse

## Summary

The rail took **13,749 payment attempts** on Tuesday 16 June 2026 (Rath Yatra) and settled **₹1.77 Cr** across 13,212 successful payments. Volume was +0.1% on yesterday and −3.2% on the same weekday last week. Success closed at **96.09%**, in line with the trailing 28-day median of 96.25%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,749 | +0.1% | −3.2% | 14,926 |
| Successful payments | 13,212 | −0.0% | −3.3% | 14,386 |
| Success rate | 96.09% | −0.09pp | −0.10pp | 96.37% |
| Settled value | ₹1.77 Cr | −0.3% | −5.9% | ₹1.98 Cr |
| Average ticket | ₹1,341 | −0.2% | −2.7% | ₹1,372 |
| Technical declines | 0.298% | −0.08pp | −0.15pp | 0.386% |
| Business declines | 3.164% | +0.16pp | +0.31pp | 2.774% |
| Risk declines | 0.087% | −0.00pp | −0.01pp | 0.124% |
| Timeout declines | 0.276% | +0.04pp | −0.03pp | 0.263% |
| Retry share | 1.05% | −0.03pp | −0.13pp | 1.03% |
| Latency p95 | 1,299 ms | +0.8% | +0.4% | 1,271 ms |
| Active customers | 11,472 | +0.6% | −2.1% | 12,249 |
| Active merchants | 1,482 | −3.8% | −1.9% | 1,543 |

## What moved

- Issuer Bank of Baroda ran at 94.66% success on 1,012 attempts (7.4% of the day), 1.79pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 28% across the trailing window to 1,864 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,983 | 29.0% | 95.28% | ₹38.31 L | −8.8% |
| UPI Person to Merchant | 3,100 | 22.5% | 96.29% | ₹34.95 L | −16.9% |
| UPI QR Payments | 2,462 | 17.9% | 96.43% | ₹11.25 L | +4.7% |
| UPI Lite | 1,864 | 13.6% | 98.66% | ₹1.73 L | −4.1% |
| UPI Circle | 673 | 4.9% | 96.43% | ₹5.90 L | −1.4% |
| Credit on UPI | 478 | 3.5% | 96.44% | ₹30.35 L | +19.8% |
| UPI AutoPay | 371 | 2.7% | 91.37% | ₹7.78 L | +5.8% |
| RuPay Credit on UPI | 295 | 2.1% | 94.92% | ₹15.77 L | −20.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,281 | 96.40% | 96.22% | ₹58.58 L | normal |
| HDFC Bank | 1,530 | 96.21% | 96.41% | ₹16.98 L | normal |
| Bank of Baroda | 1,012 | 94.66% | 96.46% | ₹11.73 L | ⚠ outlier |
| Union Bank of India | 956 | 95.92% | 96.39% | ₹8.80 L | normal |
| Axis Bank | 885 | 95.82% | 96.47% | ₹9.36 L | normal |
| ICICI Bank | 861 | 95.59% | 96.62% | ₹12.79 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,383 | 96.10% | 96.22% | ₹76.03 L | normal |
| Google Pay | 4,675 | 96.47% | 96.36% | ₹64.41 L | normal |
| Paytm | 1,104 | 95.29% | 95.98% | ₹16.39 L | normal |
| Navi | 486 | 95.06% | 96.27% | ₹5.49 L | normal |
| SuperMoney | 264 | 95.45% | 96.26% | ₹2.84 L | normal |
| BHIM | 145 | 97.24% | 95.50% | ₹5.44 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,283 | 96.59% | ₹52.65 L |
| Food & Beverage | 2,441 | 96.89% | ₹13.71 L |
| Mobility | 1,142 | 97.90% | ₹5.78 L |
| Bills | 787 | 94.79% | ₹7.50 L |
| Healthcare | 477 | 97.06% | ₹7.35 L |
| Digital | 195 | 94.87% | ₹85,297 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,021 | 29.2% | 96.17% | ₹60.47 L |
| North | 3,567 | 25.9% | 96.08% | ₹42.15 L |
| West | 3,357 | 24.4% | 95.80% | ₹39.71 L |
| East | 1,613 | 11.7% | 96.28% | ₹20.56 L |
| Central | 1,191 | 8.7% | 96.47% | ₹14.32 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 42 | 97.62% | ₹3.88 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 95.59% | ₹3.64 L |
| Hampi Styles | Key Account | Retail | 39 | 89.74% | ₹1.48 L |
| Rapid Bazaar | Key Account | Retail | 377 | 98.94% | ₹1.48 L |
| Urban Boutique | Key Account | Retail | 129 | 98.45% | ₹1.36 L |
| Hampi Stores 2298 | Key Account | Retail | 132 | 98.48% | ₹1.24 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 86 | 94.19% | ₹90,029 |
| Swift Mart 1738 | Key Account | Retail | 134 | 99.25% | ₹73,371 |

## Failure analysis

Of 526 declined attempts, 435 were business declines (3.164% of attempts — balances, PINs and limits), 41 technical (0.298%), 38 timeouts (0.276%) and 12 risk declines (0.087%).

144 attempts were re-presentations of an earlier failure (1.05% of the day); 61.1% of them succeeded.

- Decline code ZX (Mandate not found or revoked) fired 16 times — 0.116% of attempts against a trailing 0.068%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.273% | 1.215% |
| ZM | Invalid UPI PIN | business | Customer | 149 | 1.084% | 0.925% |
| ZA | Transaction declined by customer | business | Customer | 53 | 0.385% | 0.354% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.218% | 0.209% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.160% | 0.187% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.131% | 0.143% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.131% | 0.090% |
| ZX | Mandate not found or revoked | business | PSP | 16 | 0.116% | 0.068% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 106 | 106 |
| Auto-reversals | 19 | 24 |
| Disputes / chargebacks | 12 | 13 |
| Value returned | ₹1.47 L | ₹1.71 L |

## Customer behaviour

11,472 distinct customers transacted (−4.9% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,570 | 4,095 | 1.15 | 96.04% | ₹1,306 |
| power | 2,441 | 3,242 | 1.33 | 95.77% | ₹1,840 |
| merchant_heavy | 2,645 | 3,180 | 1.20 | 96.01% | ₹1,025 |
| small_ticket | 1,733 | 2,093 | 1.21 | 96.66% | ₹724 |
| occasional | 873 | 913 | 1.05 | 96.39% | ₹1,547 |
| new | 192 | 206 | 1.07 | 97.09% | ₹1,010 |
| dormant_returning | 18 | 20 | 1.11 | 90.00% | ₹632 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Issuer Bank of Baroda ran at 94.66% success on 1,012 attempts (7.4% of the day), 1.79pp down its own 28-day median.
- Decline code ZX (Mandate not found or revoked) fired 16 times — 0.116% of attempts against a trailing 0.068%. Owner: PSP.

### Opportunities

- Product UPI Lite is compounding — attempts up 28% across the trailing window to 1,864 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

16 June ran on trend at 96.09% success and ₹1.77 Cr settled. The movement worth carrying forward is in issuer performance: issuer Bank of Baroda ran at 94.66% success on 1,012 attempts (7.4% of the day), 1.79pp down its own 28-day median. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,749, successes=13,212, failed=526, pending=11, settled_value_inr=17,720,786.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- banks: payer_bank=Bank of Baroda; attempts=1,012; success_rate=94.66; own_median=96.45; z=-4.2
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- failures: failure_code=ZX; count=16; rate_pct=0.12; trailing_rate_pct=0.07; owner=PSP; z=2.69
- products: product_name=UPI Lite; attempts=1,864; window_growth_pct=28.1; success_rate=98.66
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5
- incidents: event_id=CMP-0060; kind=merchant_campaign; severity=Sev-3; window=2026-06-11 to 2026-06-17; success_impact_pp=-0.07; volume_impact_pct=27.15
- products: product_name=Recurring Payments; attempts=133; own_median=101; z=3.92
- categories: mcc_category=Financial Services; attempts=190; own_median=165.5; z=2.2

Refs: enterprise_data/warehouse/transactions, RPT-D162-DAILY, enterprise_data/warehouse/reference/incidents.parquet
