---
id: RPT-D161-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 14 Jun 2026)

**Report ID:** RPT-D161-DAILY · **Day 161 of 206** · **Derived from:** 13,277 transaction rows queried live from the warehouse

## Summary

The rail took **13,277 payment attempts** on Sunday 14 June 2026 (Weekend) and settled **₹1.48 Cr** across 12,739 successful payments. Volume was −12.9% on yesterday and −12.8% on the same weekday last week. Success closed at **95.95%**, below the trailing 28-day median of 96.32%.

Decline code XH (Account does not exist / frozen) fired 42 times — 0.316% of attempts against a trailing 0.209%. Owner: Issuer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,277 | −12.9% | −12.8% | 15,095 |
| Successful payments | 12,739 | −13.3% | −13.1% | 14,554 |
| Success rate | 95.95% | −0.45pp | −0.39pp | 96.40% |
| Settled value | ₹1.48 Cr | −11.2% | −18.5% | ₹2.01 Cr |
| Average ticket | ₹1,163 | +2.5% | −6.2% | ₹1,376 |
| Technical declines | 0.580% | +0.17pp | +0.16pp | 0.393% |
| Business declines | 3.058% | +0.28pp | +0.31pp | 2.730% |
| Risk declines | 0.090% | +0.02pp | −0.00pp | 0.129% |
| Timeout declines | 0.271% | +0.02pp | +0.00pp | 0.263% |
| Retry share | 1.25% | +0.23pp | +0.31pp | 1.03% |
| Latency p95 | 1,211 ms | +1.0% | +0.3% | 1,268 ms |
| Active customers | 11,116 | −10.2% | −11.1% | 12,365 |
| Active merchants | 1,451 | −6.8% | −6.3% | 1,547 |

## What moved

- Product UPI Person to Person ran at 94.70% success on 3,718 attempts (28.0% of the day), 0.77pp down its own 28-day median.
- Product UPI Lite ran at 98.37% success on 2,202 attempts (16.6% of the day), 0.68pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,718 | 28.0% | 94.70% | ₹38.29 L | −15.5% |
| UPI Person to Merchant | 3,232 | 24.3% | 96.50% | ₹31.73 L | −15.6% |
| UPI QR Payments | 2,206 | 16.6% | 96.33% | ₹9.13 L | −8.4% |
| UPI Lite | 2,202 | 16.6% | 98.37% | ₹1.98 L | +13.9% |
| UPI Circle | 712 | 5.4% | 96.91% | ₹5.05 L | +4.3% |
| UPI AutoPay | 374 | 2.8% | 87.70% | ₹6.51 L | +7.0% |
| Credit on UPI | 234 | 1.8% | 94.44% | ₹13.29 L | −41.4% |
| RuPay Credit on UPI | 201 | 1.5% | 97.51% | ₹15.21 L | −45.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,175 | 95.78% | 96.22% | ₹48.70 L | normal |
| HDFC Bank | 1,442 | 95.91% | 96.42% | ₹16.61 L | normal |
| Bank of Baroda | 982 | 96.44% | 96.48% | ₹10.78 L | normal |
| Union Bank of India | 890 | 95.06% | 96.40% | ₹10.93 L | ⚠ outlier |
| Punjab National Bank | 841 | 96.79% | 96.27% | ₹8.94 L | normal |
| Axis Bank | 830 | 96.63% | 96.47% | ₹8.76 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,227 | 95.78% | 96.23% | ₹66.99 L | normal |
| Google Pay | 4,432 | 96.37% | 96.32% | ₹52.09 L | normal |
| Paytm | 1,065 | 95.21% | 95.98% | ₹10.62 L | normal |
| Navi | 476 | 95.17% | 96.23% | ₹5.24 L | normal |
| SuperMoney | 242 | 95.04% | 96.32% | ₹2.50 L | normal |
| FamApp | 140 | 96.43% | 96.72% | ₹1.10 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,925 | 96.87% | ₹36.61 L |
| Food & Beverage | 2,514 | 96.74% | ₹10.26 L |
| Mobility | 1,217 | 96.88% | ₹6.53 L |
| Bills | 756 | 95.63% | ₹10.27 L |
| Healthcare | 492 | 98.37% | ₹4.66 L |
| Digital | 242 | 93.80% | ₹1.13 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,928 | 29.6% | 96.26% | ₹43.78 L |
| North | 3,424 | 25.8% | 96.20% | ₹35.35 L |
| West | 3,309 | 24.9% | 95.32% | ₹40.57 L |
| East | 1,516 | 11.4% | 95.58% | ₹18.42 L |
| Central | 1,100 | 8.3% | 96.45% | ₹10.09 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 391 | 98.47% | ₹1.43 L |
| Vasant Wardrobe | Key Account | Retail | 57 | 92.98% | ₹1.34 L |
| Vega Electronics | Large | Retail | 23 | 100.00% | ₹1.10 L |
| Urban Boutique | Key Account | Retail | 114 | 97.37% | ₹98,911 |
| Hampi Styles | Key Account | Retail | 23 | 91.30% | ₹84,841 |
| Ujjwal Water Board | Key Account | Bills | 35 | 97.14% | ₹83,180 |
| Hampi Stores 2298 | Key Account | Retail | 94 | 97.87% | ₹66,410 |
| Girnar Connect | Key Account | Bills | 128 | 94.53% | ₹60,583 |

## Failure analysis

Of 531 declined attempts, 406 were business declines (3.058% of attempts — balances, PINs and limits), 77 technical (0.580%), 36 timeouts (0.271%) and 12 risk declines (0.090%).

166 attempts were re-presentations of an earlier failure (1.25% of the day); 72.3% of them succeeded.

- Decline code XH (Account does not exist / frozen) fired 42 times — 0.316% of attempts against a trailing 0.209%. Owner: Issuer.
- Decline code YA (PSP not available) fired 17 times — 0.128% of attempts against a trailing 0.047%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 162 | 1.220% | 1.198% |
| ZM | Invalid UPI PIN | business | Customer | 135 | 1.017% | 0.904% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.346% | 0.348% |
| XH | Account does not exist / frozen | business | Issuer | 42 | 0.316% | 0.209% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.233% | 0.187% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.136% | 0.143% |
| YA | PSP not available | technical | PSP | 17 | 0.128% | 0.047% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.128% | 0.113% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 101 | 106 |
| Auto-reversals | 30 | 24 |
| Disputes / chargebacks | 10 | 13 |
| Value returned | ₹2.72 L | ₹1.72 L |

## Customer behaviour

11,116 distinct customers transacted (−8.3% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,442 | 3,946 | 1.15 | 96.38% | ₹1,224 |
| power | 2,441 | 3,216 | 1.32 | 95.65% | ₹1,397 |
| merchant_heavy | 2,562 | 3,058 | 1.19 | 95.09% | ₹882 |
| small_ticket | 1,614 | 1,938 | 1.20 | 96.90% | ₹503 |
| occasional | 846 | 894 | 1.06 | 95.53% | ₹1,814 |
| new | 192 | 206 | 1.07 | 97.57% | ₹947 |
| dormant_returning | 19 | 19 | 1.00 | 100.00% | ₹513 |

## Operational events

- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ONBRD-0089** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0060** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code XH (Account does not exist / frozen) fired 42 times — 0.316% of attempts against a trailing 0.209%. Owner: Issuer.
- Decline code YA (PSP not available) fired 17 times — 0.128% of attempts against a trailing 0.047%. Owner: PSP.
- Product UPI Person to Person ran at 94.70% success on 3,718 attempts (28.0% of the day), 0.77pp down its own 28-day median.
- Product UPI Lite ran at 98.37% success on 2,202 attempts (16.6% of the day), 0.68pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 25% across the trailing window to 2,202 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

14 June ran on trend at 95.95% success and ₹1.48 Cr settled. The movement worth carrying forward is in the decline profile: decline code XH (Account does not exist / frozen) fired 42 times — 0.316% of attempts against a trailing 0.209%. Owner: Issuer. 3 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,277, successes=12,739, failed=531, pending=7, settled_value_inr=14,821,134.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=XH; count=42; rate_pct=0.32; trailing_rate_pct=0.21; owner=Issuer; z=3.14
- failures: failure_code=YA; count=17; rate_pct=0.13; trailing_rate_pct=0.05; owner=PSP; z=3.86
- products: product_name=UPI Person to Person; attempts=3,718; success_rate=94.7; own_median=95.47; z=-2.13
- products: product_name=UPI Lite; attempts=2,202; success_rate=98.37; own_median=99.05; z=-2.67
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Lite; attempts=2,202; window_growth_pct=25.3; success_rate=98.37
- banks: payer_bank=Union Bank of India; attempts=890; success_rate=95.06; own_median=96.4; z=-2.48
- banks: payer_bank=ICICI Bank; attempts=770; success_rate=94.94; own_median=96.62; z=-2.32
- banks: payer_bank=Union Bank of India; attempts=890; own_median=1,041; z=-2.37
- incidents: event_id=ONBRD-0089; kind=merchant_onboarding; severity=Sev-3; window=2026-05-30 to 2026-06-23; success_impact_pp=-0.82; volume_impact_pct=21.5

Refs: enterprise_data/warehouse/transactions, RPT-D160-DAILY, enterprise_data/warehouse/reference/incidents.parquet
