---
id: RPT-D28-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-01T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 01 Feb 2026)

**Report ID:** RPT-D28-DAILY · **Day 28 of 206** · **Derived from:** 12,060 transaction rows queried live from the warehouse

## Summary

The rail took **12,060 payment attempts** on Sunday 01 February 2026 (Weekend) and settled **₹1.24 Cr** across 11,507 successful payments. Volume was +2.5% on yesterday and +14.8% on the same weekday last week. Success closed at **95.41%**, in line with the trailing 28-day median of 95.27%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,060 | +2.5% | +14.8% | 12,060 |
| Successful payments | 11,507 | +2.0% | +15.4% | 11,507 |
| Success rate | 95.41% | −0.50pp | +0.46pp | 95.41% |
| Settled value | ₹1.24 Cr | −1.7% | +16.3% | ₹1.24 Cr |
| Average ticket | ₹1,076 | −3.6% | +0.8% | ₹1,076 |
| Technical declines | 0.614% | +0.20pp | −0.04pp | 0.614% |
| Business declines | 3.400% | +0.37pp | −0.41pp | 3.400% |
| Risk declines | 0.182% | −0.02pp | +0.07pp | 0.182% |
| Timeout declines | 0.232% | −0.05pp | −0.11pp | 0.232% |
| Retry share | 1.30% | +0.29pp | −0.11pp | 1.30% |
| Latency p95 | 1,210 ms | −0.4% | −1.0% | 1,210 ms |
| Active customers | 10,056 | +2.3% | +13.2% | 10,056 |
| Active merchants | 1,286 | −0.7% | +8.1% | 1,286 |

## What moved

- Category Bills carried 1,150 attempts, 75% up its trailing median and 15.8% of the day's volume.
- Region West carried 2,952 attempts, 17% up its trailing median and 24.5% of the day's volume.
- Product UPI Lite carried 1,016 attempts, 54% up its trailing median and 8.4% of the day's volume.
- Category Food & Beverage carried 1,723 attempts, 17% up its trailing median and 23.7% of the day's volume.
- Category Mobility carried 840 attempts, 30% up its trailing median and 11.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,785 | 39.7% | 94.75% | ₹52.76 L | +20.0% |
| UPI Person to Merchant | 3,221 | 26.7% | 95.68% | ₹32.06 L | +10.2% |
| UPI QR Payments | 2,166 | 18.0% | 96.03% | ₹8.56 L | +29.4% |
| UPI Lite | 1,016 | 8.4% | 99.21% | ₹89,187 | +53.7% |
| UPI AutoPay | 312 | 2.6% | 89.42% | ₹5.45 L | +2.6% |
| UPI Circle | 113 | 0.9% | 100.00% | ₹1.40 L | +22.8% |
| RuPay Credit on UPI | 105 | 0.9% | 95.24% | ₹5.56 L | −45.3% |
| UPI Lite Auto Top-Up | 83 | 0.7% | 95.18% | ₹90,260 | −1.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,804 | 95.77% | 94.93% | ₹39.48 L | normal |
| HDFC Bank | 1,337 | 96.71% | 95.92% | ₹13.28 L | normal |
| Bank of Baroda | 933 | 94.43% | 94.67% | ₹9.38 L | normal |
| Union Bank of India | 821 | 93.42% | 94.72% | ₹8.23 L | normal |
| ICICI Bank | 747 | 94.78% | 96.09% | ₹7.16 L | normal |
| Punjab National Bank | 736 | 94.29% | 94.81% | ₹8.30 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,651 | 95.26% | 95.09% | ₹57.40 L | normal |
| Google Pay | 4,002 | 95.28% | 95.34% | ₹41.52 L | normal |
| Paytm | 1,004 | 96.51% | 94.78% | ₹10.94 L | normal |
| Navi | 445 | 96.18% | 95.89% | ₹4.47 L | normal |
| SuperMoney | 269 | 96.28% | 95.49% | ₹2.61 L | normal |
| BHIM | 112 | 92.86% | 95.10% | ₹1.76 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,658 | 96.50% | ₹25.45 L |
| Food & Beverage | 1,723 | 96.63% | ₹7.51 L |
| Bills | 1,150 | 94.70% | ₹12.28 L |
| Mobility | 840 | 96.55% | ₹3.71 L |
| Healthcare | 352 | 96.88% | ₹2.27 L |
| Digital | 265 | 92.08% | ₹1.54 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,518 | 29.2% | 95.28% | ₹36.89 L |
| North | 3,112 | 25.8% | 95.37% | ₹31.48 L |
| West | 2,952 | 24.5% | 95.16% | ₹30.77 L |
| East | 1,384 | 11.5% | 96.10% | ₹14.53 L |
| Central | 1,094 | 9.1% | 95.80% | ₹10.15 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 22 | 95.45% | ₹1.41 L |
| Rapid Bazaar | Key Account | Retail | 306 | 97.71% | ₹1.30 L |
| Ujjwal Water Board | Key Account | Bills | 72 | 91.67% | ₹1.07 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 59 | 93.22% | ₹95,526 |
| Hampi Stores 2298 | Key Account | Retail | 104 | 97.12% | ₹92,122 |
| Vasant Wardrobe | Key Account | Retail | 38 | 94.74% | ₹70,387 |
| Girnar Connect | Key Account | Bills | 186 | 96.24% | ₹69,835 |
| Indus Connect | Key Account | Bills | 66 | 93.94% | ₹69,498 |

## Failure analysis

Of 534 declined attempts, 410 were business declines (3.400% of attempts — balances, PINs and limits), 74 technical (0.614%), 28 timeouts (0.232%) and 22 risk declines (0.182%).

157 attempts were re-presentations of an earlier failure (1.30% of the day); 64.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 162 | 1.343% | 1.503% |
| ZM | Invalid UPI PIN | business | Customer | 132 | 1.095% | 1.103% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.456% | 0.400% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.315% | 0.260% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.240% | 0.238% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.166% | 0.155% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.149% | 0.113% |
| UX | Mandate execution outside permitted window | business | PSP | 17 | 0.141% | 0.093% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 70 | 60 |
| Auto-reversals | 25 | 22 |
| Disputes / chargebacks | 3 | 2 |
| Value returned | ₹1.17 L | ₹91,345 |

## Customer behaviour

10,056 distinct customers transacted (+13.9% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,086 | 3,502 | 1.13 | 95.66% | ₹1,081 |
| merchant_heavy | 2,324 | 2,832 | 1.22 | 95.20% | ₹795 |
| power | 2,070 | 2,770 | 1.34 | 95.49% | ₹1,561 |
| small_ticket | 1,485 | 1,806 | 1.22 | 95.85% | ₹411 |
| occasional | 830 | 866 | 1.04 | 94.46% | ₹1,310 |
| new | 217 | 239 | 1.10 | 94.56% | ₹492 |
| dormant_returning | 44 | 45 | 1.02 | 91.11% | ₹570 |

## Operational events

- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

01 February ran on trend at 95.41% success and ₹1.24 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 1,150 attempts, 75% up its trailing median and 15.8% of the day's volume. Nothing else in the day cleared the materiality threshold.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-01` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,060, successes=11,507, failed=534, pending=19, settled_value_inr=12,382,179.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,150; own_median=657; z=4.43
- geography: region=West; attempts=2,952; own_median=2,515; z=2.63
- products: product_name=UPI Lite; attempts=1,016; own_median=661; z=3.8
- categories: mcc_category=Food & Beverage; attempts=1,723; own_median=1,478; z=2.26
- categories: mcc_category=Mobility; attempts=840; own_median=647; z=3.03
- banks: payer_bank=IDFC First Bank; attempts=334; success_rate=97.9; own_median=95.68; z=2.32
- psps: payer_psp=Navi; attempts=445; own_median=369; z=2.7
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- psps: payer_psp=SuperMoney; attempts=269; own_median=205; z=2.88
- products: product_name=RuPay Credit on UPI; attempts=105; own_median=192; z=-2.55

Refs: enterprise_data/warehouse/transactions, RPT-D27-DAILY, enterprise_data/warehouse/reference/incidents.parquet
