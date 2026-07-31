---
id: RPT-D48-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-21T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 21 Feb 2026)

**Report ID:** RPT-D48-DAILY · **Day 48 of 206** · **Derived from:** 11,905 transaction rows queried live from the warehouse

## Summary

The rail took **11,905 payment attempts** on Saturday 21 February 2026 (Weekend) and settled **₹1.32 Cr** across 11,373 successful payments. Volume was +8.9% on yesterday and +1.3% on the same weekday last week. Success closed at **95.53%**, in line with the trailing 28-day median of 95.53%.

11 disputes were raised, 2.5 sigma above the trailing median of 6. Issuer HDFC Bank ran at 94.25% success on 1,269 attempts (10.7% of the day), 1.98pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,905 | +8.9% | +1.3% | 10,852 |
| Successful payments | 11,373 | +8.8% | +1.0% | 10,357 |
| Success rate | 95.53% | −0.09pp | −0.30pp | 95.40% |
| Settled value | ₹1.32 Cr | +5.1% | +12.7% | ₹1.23 Cr |
| Average ticket | ₹1,163 | −3.4% | +11.6% | ₹1,188 |
| Technical declines | 0.361% | −0.09pp | −0.06pp | 0.421% |
| Business declines | 3.511% | +0.10pp | +0.27pp | 3.537% |
| Risk declines | 0.151% | +0.03pp | −0.01pp | 0.136% |
| Timeout declines | 0.353% | +0.01pp | +0.04pp | 0.394% |
| Retry share | 1.30% | −0.04pp | +0.20pp | 1.44% |
| Latency p95 | 1,217 ms | −4.7% | −0.4% | 1,283 ms |
| Active customers | 9,952 | +7.6% | +1.5% | 9,161 |
| Active merchants | 1,292 | +1.2% | +1.1% | 1,257 |

## What moved

- Issuer HDFC Bank ran at 94.25% success on 1,269 attempts (10.7% of the day), 1.98pp down its own 28-day median.
- Product UPI Person to Merchant carried 4,152 attempts, 33% up its trailing median and 34.9% of the day's volume.
- Category Retail carried 3,390 attempts, 26% up its trailing median and 42.8% of the day's volume.
- Product RuPay Credit on UPI is compounding — attempts up 37% across the trailing window to 199 today, with success holding, so the growth is healthy and worth funding.
- Category Food & Beverage carried 2,052 attempts, 28% up its trailing median and 25.9% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 4,152 | 34.9% | 96.15% | ₹40.25 L | +33.5% |
| UPI Person to Person | 3,988 | 33.5% | 94.61% | ₹43.54 L | +1.9% |
| UPI QR Payments | 1,767 | 14.8% | 96.32% | ₹6.20 L | +4.1% |
| UPI Lite | 901 | 7.6% | 98.45% | ₹77,587 | +23.8% |
| UPI AutoPay | 295 | 2.5% | 92.20% | ₹5.17 L | −1.7% |
| RuPay Credit on UPI | 199 | 1.7% | 94.47% | ₹9.72 L | −0.7% |
| UPI Circle | 138 | 1.2% | 96.38% | ₹98,463 | +36.0% |
| Credit on UPI | 136 | 1.1% | 91.91% | ₹10.11 L | −6.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,736 | 95.99% | 95.68% | ₹43.72 L | normal |
| HDFC Bank | 1,269 | 94.25% | 96.22% | ₹14.46 L | ⚠ outlier |
| Bank of Baroda | 903 | 95.90% | 95.30% | ₹9.60 L | normal |
| Union Bank of India | 880 | 96.93% | 95.21% | ₹9.68 L | normal |
| ICICI Bank | 723 | 94.47% | 96.31% | ₹7.93 L | ⚠ outlier |
| Axis Bank | 716 | 95.39% | 95.20% | ₹8.15 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,562 | 95.56% | 95.54% | ₹62.51 L | normal |
| Google Pay | 3,985 | 95.51% | 95.65% | ₹44.22 L | normal |
| Paytm | 995 | 94.97% | 95.68% | ₹9.70 L | normal |
| Navi | 456 | 94.96% | 95.52% | ₹5.70 L | normal |
| SuperMoney | 218 | 96.33% | 96.30% | ₹2.52 L | normal |
| BHIM | 119 | 98.32% | 94.41% | ₹2.00 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,390 | 95.81% | ₹35.10 L |
| Food & Beverage | 2,052 | 96.83% | ₹11.84 L |
| Bills | 765 | 95.03% | ₹8.66 L |
| Mobility | 723 | 96.82% | ₹3.36 L |
| Healthcare | 436 | 97.02% | ₹3.24 L |
| Digital | 201 | 94.53% | ₹1.76 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,492 | 29.3% | 95.30% | ₹41.53 L |
| North | 3,079 | 25.9% | 95.75% | ₹34.45 L |
| West | 2,977 | 25.0% | 95.03% | ₹33.03 L |
| East | 1,311 | 11.0% | 96.49% | ₹14.30 L |
| Central | 1,046 | 8.8% | 95.89% | ₹8.92 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 42 | 95.24% | ₹2.75 L |
| Rapid Bazaar | Key Account | Retail | 372 | 96.24% | ₹1.32 L |
| Vasant Wardrobe | Key Account | Retail | 56 | 96.43% | ₹86,710 |
| Urban Boutique | Key Account | Retail | 110 | 95.45% | ₹80,367 |
| Yamuna Restaurant | Key Account | Food & Beverage | 92 | 95.65% | ₹79,279 |
| Hampi Stores 2298 | Key Account | Retail | 108 | 93.52% | ₹75,884 |
| Hampi Styles | Key Account | Retail | 41 | 90.24% | ₹68,572 |
| Shakti Stores 1531 | Key Account | Retail | 92 | 100.00% | ₹59,939 |

## Failure analysis

Of 521 declined attempts, 418 were business declines (3.511% of attempts — balances, PINs and limits), 43 technical (0.361%), 42 timeouts (0.353%) and 18 risk declines (0.151%).

155 attempts were re-presentations of an earlier failure (1.30% of the day); 63.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 180 | 1.512% | 1.447% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 1.159% | 1.168% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.361% | 0.431% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.252% | 0.233% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.185% | 0.147% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.134% | 0.101% |
| U30 | Debit failed at remitter bank | technical | Issuer | 15 | 0.126% | 0.182% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 14 | 0.118% | 0.105% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 65 | 68 |
| Auto-reversals | 19 | 17 |
| Disputes / chargebacks | 11 | 6 |
| Value returned | ₹1.02 L | ₹97,625 |

## Customer behaviour

9,952 distinct customers transacted (+12.1% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,087 | 3,511 | 1.14 | 95.64% | ₹1,240 |
| merchant_heavy | 2,311 | 2,762 | 1.20 | 95.80% | ₹850 |
| power | 2,025 | 2,733 | 1.35 | 95.35% | ₹1,586 |
| small_ticket | 1,512 | 1,827 | 1.21 | 95.07% | ₹470 |
| occasional | 795 | 827 | 1.04 | 95.41% | ₹1,262 |
| new | 201 | 223 | 1.11 | 96.41% | ₹1,149 |
| dormant_returning | 21 | 22 | 1.05 | 100.00% | ₹1,220 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 11 disputes were raised, 2.5 sigma above the trailing median of 6.
- Issuer HDFC Bank ran at 94.25% success on 1,269 attempts (10.7% of the day), 1.98pp down its own 28-day median.
- Issuer ICICI Bank ran at 94.47% success on 723 attempts (6.1% of the day), 1.84pp down its own 28-day median.

### Opportunities

- Product RuPay Credit on UPI is compounding — attempts up 37% across the trailing window to 199 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

21 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.53% success against a 95.53% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-21` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,905, successes=11,373, failed=521, pending=11, settled_value_inr=13,223,621.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- adjustments: chargebacks=11; trailing_median=5.5; z=2.47
- banks: payer_bank=HDFC Bank; attempts=1,269; success_rate=94.25; own_median=96.22; z=-5.57
- products: product_name=UPI Person to Merchant; attempts=4,152; own_median=3,111; z=3.43
- categories: mcc_category=Retail; attempts=3,390; own_median=2,694.5; z=2.5
- products: product_name=RuPay Credit on UPI; attempts=199; window_growth_pct=36.6; success_rate=94.47
- categories: mcc_category=Food & Beverage; attempts=2,052; own_median=1,598.5; z=2.61
- categories: mcc_category=Healthcare; attempts=436; own_median=332.5; z=3.88
- banks: payer_bank=ICICI Bank; attempts=723; success_rate=94.47; own_median=96.31; z=-2.3
- psps: payer_psp=Navi; attempts=456; own_median=377; z=2.6

Refs: enterprise_data/warehouse/transactions, RPT-D47-DAILY, enterprise_data/warehouse/reference/incidents.parquet
