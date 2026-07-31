---
id: RPT-D21-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 25 Jan 2026)

**Report ID:** RPT-D21-DAILY · **Day 21 of 206** · **Derived from:** 10,501 transaction rows queried live from the warehouse

## Summary

The rail took **10,501 payment attempts** on Sunday 25 January 2026 (Republic Day (build-up)) and settled **₹1.06 Cr** across 9,971 successful payments. Volume was −13.1% on yesterday and +14.5% on the same weekday last week. Success closed at **94.95%**, below the trailing 28-day median of 95.39%.

3 disputes were raised, 3.4 sigma above the trailing median of 0.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,501 | −13.1% | +14.5% | 10,482 |
| Successful payments | 9,971 | −13.7% | +15.6% | 9,976 |
| Success rate | 94.95% | −0.67pp | +0.86pp | 95.14% |
| Settled value | ₹1.06 Cr | −22.4% | +14.2% | ₹1.18 Cr |
| Average ticket | ₹1,068 | −10.1% | −1.2% | ₹1,183 |
| Technical declines | 0.657% | +0.11pp | −0.12pp | 0.634% |
| Business declines | 3.809% | +0.61pp | −0.58pp | 3.573% |
| Risk declines | 0.114% | −0.03pp | −0.08pp | 0.130% |
| Timeout declines | 0.343% | −0.01pp | −0.10pp | 0.390% |
| Retry share | 1.41% | +0.12pp | −0.50pp | 1.48% |
| Latency p95 | 1,222 ms | +4.9% | −6.1% | 1,242 ms |
| Active customers | 8,884 | −10.6% | +13.0% | 8,859 |
| Active merchants | 1,190 | −4.2% | +3.2% | 1,206 |

## What moved

- Category Bills ran at 93.55% success on 605 attempts (9.5% of the day), 2.27pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,148 | 39.5% | 93.88% | ₹43.68 L | +3.2% |
| UPI Person to Merchant | 2,978 | 28.4% | 96.00% | ₹27.47 L | −2.1% |
| UPI QR Payments | 1,793 | 17.1% | 96.60% | ₹8.27 L | +4.9% |
| UPI Lite | 779 | 7.4% | 98.59% | ₹63,835 | +19.7% |
| UPI AutoPay | 292 | 2.8% | 85.62% | ₹4.32 L | −4.3% |
| UPI Circle | 112 | 1.1% | 95.54% | ₹85,939 | +21.1% |
| Recurring Payments | 87 | 0.8% | 82.76% | ₹3.88 L | +3.6% |
| UPI Lite Auto Top-Up | 87 | 0.8% | 90.80% | ₹90,077 | +4.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,391 | 94.84% | 94.92% | ₹36.10 L | normal |
| HDFC Bank | 1,108 | 94.77% | 95.90% | ₹10.10 L | normal |
| Bank of Baroda | 788 | 94.42% | 94.70% | ₹7.47 L | normal |
| Union Bank of India | 722 | 94.60% | 94.72% | ₹6.98 L | normal |
| Axis Bank | 682 | 95.01% | 95.37% | ₹5.92 L | normal |
| ICICI Bank | 618 | 94.66% | 96.00% | ₹5.79 L | ⚠ outlier |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,967 | 95.19% | 95.16% | ₹49.18 L | normal |
| Google Pay | 3,383 | 94.74% | 95.29% | ₹34.16 L | normal |
| Paytm | 901 | 94.89% | 94.57% | ₹11.00 L | normal |
| Navi | 388 | 97.16% | 95.56% | ₹3.74 L | normal |
| SuperMoney | 205 | 93.17% | 95.40% | ₹1.41 L | normal |
| BHIM | 132 | 91.67% | 95.46% | ₹2.09 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,734 | 96.12% | ₹26.85 L |
| Food & Beverage | 1,638 | 96.70% | ₹6.45 L |
| Mobility | 640 | 97.66% | ₹4.10 L |
| Bills | 605 | 93.55% | ₹6.29 L |
| Healthcare | 303 | 98.02% | ₹2.70 L |
| Digital | 169 | 90.53% | ₹81,220 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,179 | 30.3% | 94.87% | ₹28.73 L |
| North | 2,632 | 25.1% | 94.72% | ₹31.60 L |
| West | 2,556 | 24.3% | 95.34% | ₹25.71 L |
| East | 1,260 | 12.0% | 94.76% | ₹11.57 L |
| Central | 874 | 8.3% | 95.08% | ₹8.86 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 35 | 97.14% | ₹3.83 L |
| Vasant Wardrobe | Key Account | Retail | 69 | 97.10% | ₹1.23 L |
| Rapid Bazaar | Key Account | Retail | 274 | 95.62% | ₹74,456 |
| Yamuna Restaurant | Key Account | Food & Beverage | 65 | 96.92% | ₹58,459 |
| Urban Boutique | Key Account | Retail | 87 | 97.70% | ₹57,591 |
| Ujjwal Water Board | Key Account | Bills | 30 | 83.33% | ₹52,680 |
| Girnar Connect | Key Account | Bills | 106 | 93.40% | ₹47,868 |
| Aravalli Pharmacy | Large | Healthcare | 49 | 100.00% | ₹35,383 |

## Failure analysis

Of 517 declined attempts, 400 were business declines (3.809% of attempts — balances, PINs and limits), 69 technical (0.657%), 36 timeouts (0.343%) and 12 risk declines (0.114%).

148 attempts were re-presentations of an earlier failure (1.41% of the day); 69.6% of them succeeded.

- Decline code U69 (Beneficiary bank offline) fired 20 times — 0.190% of attempts against a trailing 0.106%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 185 | 1.762% | 1.482% |
| ZM | Invalid UPI PIN | business | Customer | 120 | 1.143% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 50 | 0.476% | 0.383% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.305% | 0.249% |
| U30 | Debit failed at remitter bank | technical | Issuer | 32 | 0.305% | 0.265% |
| U69 | Beneficiary bank offline | technical | Issuer | 20 | 0.190% | 0.106% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 15 | 0.143% | 0.185% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.124% | 0.177% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 66 | 45 |
| Auto-reversals | 29 | 24 |
| Disputes / chargebacks | 3 | 0 |
| Value returned | ₹1.72 L | ₹92,515 |

## Customer behaviour

8,884 distinct customers transacted (+0.4% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,685 | 3,040 | 1.13 | 94.44% | ₹939 |
| power | 1,876 | 2,433 | 1.30 | 94.70% | ₹1,683 |
| merchant_heavy | 2,032 | 2,407 | 1.18 | 95.39% | ₹730 |
| small_ticket | 1,348 | 1,627 | 1.21 | 95.88% | ₹488 |
| occasional | 716 | 754 | 1.05 | 94.16% | ₹1,311 |
| new | 185 | 198 | 1.07 | 96.46% | ₹615 |
| dormant_returning | 42 | 42 | 1.00 | 92.86% | ₹910 |

## Operational events

- **INC-FRAUD-0047** (Sev-1) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 3 disputes were raised, 3.4 sigma above the trailing median of 0.
- Category Bills ran at 93.55% success on 605 attempts (9.5% of the day), 2.27pp down its own 28-day median.
- Decline code U69 (Beneficiary bank offline) fired 20 times — 0.190% of attempts against a trailing 0.106%. Owner: Issuer.
- Issuer ICICI Bank ran at 94.66% success on 618 attempts (5.9% of the day), 1.34pp down its own 28-day median.
- Product UPI Lite Auto Top-Up ran at 90.80% success on 87 attempts (0.8% of the day), 5.67pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

25 January was an incident day: INC-FRAUD-0047 was live and the rail closed at 94.95% success against a 95.39% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,501, successes=9,971, failed=517, pending=13, settled_value_inr=10,647,078.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0047; kind=fraud_spike; severity=Sev-1; window=2026-01-25 to 2026-01-29; success_impact_pp=-2.24; volume_impact_pct=10.81
- adjustments: chargebacks=3; trailing_median=0.5; z=3.37
- categories: mcc_category=Bills; attempts=605; success_rate=93.55; own_median=95.82; z=-3.77
- failures: failure_code=U69; count=20; rate_pct=0.19; trailing_rate_pct=0.11; owner=Issuer; z=2.84
- banks: payer_bank=ICICI Bank; attempts=618; success_rate=94.66; own_median=96; z=-2.12
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=UPI Lite Auto Top-Up; attempts=87; success_rate=90.8; own_median=96.47; z=-3.33
- products: product_name=RuPay Credit on UPI; attempts=67; own_median=193.5; z=-3.28

Refs: enterprise_data/warehouse/transactions, RPT-D20-DAILY, enterprise_data/warehouse/reference/incidents.parquet
