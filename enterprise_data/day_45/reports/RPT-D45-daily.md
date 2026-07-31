---
id: RPT-D45-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 18 Feb 2026)

**Report ID:** RPT-D45-DAILY · **Day 45 of 206** · **Derived from:** 9,725 transaction rows queried live from the warehouse

## Summary

The rail took **9,725 payment attempts** on Wednesday 18 February 2026 (Working day) and settled **₹1.11 Cr** across 9,315 successful payments. Volume was −4.9% on yesterday and +5.1% on the same weekday last week. Success closed at **95.78%**, above the trailing 28-day median of 95.44%.

Category Food & Beverage ran at 95.50% success on 1,512 attempts (23.9% of the day), 1.24pp down its own 28-day median. Product UPI Person to Person ran at 95.69% success on 3,390 attempts (34.9% of the day), 0.94pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,725 | −4.9% | +5.1% | 10,838 |
| Successful payments | 9,315 | −4.5% | +6.5% | 10,343 |
| Success rate | 95.78% | +0.40pp | +1.32pp | 95.39% |
| Settled value | ₹1.11 Cr | −5.7% | +0.9% | ₹1.23 Cr |
| Average ticket | ₹1,195 | −1.3% | −5.3% | ₹1,189 |
| Technical declines | 0.319% | −0.09pp | −0.16pp | 0.423% |
| Business declines | 3.373% | −0.33pp | −0.96pp | 3.525% |
| Risk declines | 0.082% | −0.04pp | −0.03pp | 0.138% |
| Timeout declines | 0.308% | +0.04pp | −0.17pp | 0.404% |
| Retry share | 1.25% | +0.14pp | −2.00pp | 1.44% |
| Latency p95 | 1,256 ms | −0.1% | −2.3% | 1,287 ms |
| Active customers | 8,332 | −5.0% | +4.7% | 9,145 |
| Active merchants | 1,239 | +1.3% | +3.3% | 1,256 |

## What moved

- Category Food & Beverage ran at 95.50% success on 1,512 attempts (23.9% of the day), 1.24pp down its own 28-day median.
- Product UPI Person to Person ran at 95.69% success on 3,390 attempts (34.9% of the day), 0.94pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,390 | 34.9% | 95.69% | ₹34.10 L | −13.4% |
| UPI Person to Merchant | 3,016 | 31.0% | 95.79% | ₹25.77 L | −3.1% |
| UPI QR Payments | 1,544 | 15.9% | 96.37% | ₹6.89 L | −12.3% |
| UPI Lite | 716 | 7.4% | 98.74% | ₹59,715 | −1.6% |
| UPI AutoPay | 300 | 3.1% | 91.33% | ₹5.57 L | +1.0% |
| RuPay Credit on UPI | 212 | 2.2% | 94.34% | ₹10.48 L | +5.7% |
| Credit on UPI | 165 | 1.7% | 96.97% | ₹12.07 L | +13.8% |
| Recurring Payments | 84 | 0.9% | 85.71% | ₹4.06 L | +1.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,053 | 95.87% | 95.64% | ₹33.66 L | normal |
| HDFC Bank | 1,031 | 96.31% | 96.02% | ₹10.46 L | normal |
| Bank of Baroda | 773 | 95.99% | 95.28% | ₹8.76 L | normal |
| Union Bank of India | 659 | 96.21% | 95.20% | ₹7.34 L | normal |
| ICICI Bank | 607 | 96.54% | 96.31% | ₹6.01 L | normal |
| Axis Bank | 605 | 96.69% | 95.10% | ₹7.21 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,540 | 95.66% | 95.38% | ₹57.71 L | normal |
| Google Pay | 3,240 | 95.96% | 95.63% | ₹33.80 L | normal |
| Paytm | 775 | 96.77% | 95.32% | ₹7.69 L | normal |
| Navi | 375 | 95.47% | 95.78% | ₹4.01 L | normal |
| SuperMoney | 187 | 94.12% | 96.06% | ₹1.50 L | normal |
| BHIM | 98 | 94.90% | 94.95% | ₹79,097 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,639 | 96.13% | ₹27.20 L |
| Food & Beverage | 1,512 | 95.50% | ₹6.57 L |
| Mobility | 686 | 97.23% | ₹4.06 L |
| Bills | 635 | 96.06% | ₹6.40 L |
| Healthcare | 348 | 97.99% | ₹3.87 L |
| Digital | 194 | 94.33% | ₹80,697 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,871 | 29.5% | 95.51% | ₹36.27 L |
| North | 2,490 | 25.6% | 96.06% | ₹24.54 L |
| West | 2,383 | 24.5% | 95.93% | ₹29.54 L |
| East | 1,141 | 11.7% | 95.00% | ₹12.70 L |
| Central | 840 | 8.6% | 96.55% | ₹8.24 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 67 | 98.51% | ₹1.62 L |
| Vega Electronics | Large | Retail | 24 | 100.00% | ₹1.45 L |
| Hampi Styles | Key Account | Retail | 34 | 100.00% | ₹1.20 L |
| Rapid Bazaar | Key Account | Retail | 265 | 95.47% | ₹1.18 L |
| Ujjwal Water Board | Key Account | Bills | 35 | 97.14% | ₹93,931 |
| Yamuna Restaurant | Key Account | Food & Beverage | 81 | 96.30% | ₹77,567 |
| Hampi Stores 2298 | Key Account | Retail | 95 | 94.74% | ₹73,525 |
| Aravalli Pharmacy | Large | Healthcare | 65 | 100.00% | ₹50,149 |

## Failure analysis

Of 397 declined attempts, 328 were business declines (3.373% of attempts — balances, PINs and limits), 31 technical (0.319%), 30 timeouts (0.308%) and 8 risk declines (0.082%).

122 attempts were re-presentations of an earlier failure (1.25% of the day); 67.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 136 | 1.398% | 1.447% |
| ZM | Invalid UPI PIN | business | Customer | 121 | 1.244% | 1.135% |
| ZA | Transaction declined by customer | business | Customer | 36 | 0.370% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 17 | 0.175% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 16 | 0.165% | 0.203% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.134% | 0.107% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 13 | 0.134% | 0.150% |
| UX | Mandate execution outside permitted window | business | PSP | 10 | 0.103% | 0.105% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 68 | 70 |
| Auto-reversals | 12 | 18 |
| Disputes / chargebacks | 6 | 4 |
| Value returned | ₹1.02 L | ₹1.05 L |

## Customer behaviour

8,332 distinct customers transacted (−6.3% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,544 | 2,861 | 1.12 | 95.60% | ₹1,214 |
| power | 1,731 | 2,230 | 1.29 | 94.98% | ₹1,608 |
| merchant_heavy | 1,878 | 2,167 | 1.15 | 96.17% | ₹928 |
| small_ticket | 1,311 | 1,574 | 1.20 | 96.12% | ₹617 |
| occasional | 680 | 694 | 1.02 | 97.41% | ₹1,271 |
| new | 162 | 173 | 1.07 | 94.80% | ₹1,064 |
| dormant_returning | 26 | 26 | 1.00 | 96.15% | ₹817 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Category Food & Beverage ran at 95.50% success on 1,512 attempts (23.9% of the day), 1.24pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

18 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.78% success against a 95.44% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,725, successes=9,315, failed=397, pending=13, settled_value_inr=11,129,868.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- categories: mcc_category=Food & Beverage; attempts=1,512; success_rate=95.5; own_median=96.74; z=-3.58
- products: product_name=UPI Person to Person; attempts=3,390; success_rate=95.69; own_median=94.75; z=2.32
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=Credit on UPI; attempts=165; success_rate=96.97; own_median=93.76; z=2.12
- categories: mcc_category=Services; attempts=85; success_rate=98.82; own_median=93.54; z=2.28

Refs: enterprise_data/warehouse/transactions, RPT-D44-DAILY, enterprise_data/warehouse/reference/incidents.parquet
