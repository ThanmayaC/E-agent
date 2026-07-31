---
id: RPT-D30-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-03T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 03 Feb 2026)

**Report ID:** RPT-D30-DAILY · **Day 30 of 206** · **Derived from:** 11,388 transaction rows queried live from the warehouse

## Summary

The rail took **11,388 payment attempts** on Tuesday 03 February 2026 (Working day) and settled **₹1.35 Cr** across 10,882 successful payments. Volume was −5.9% on yesterday and +26.3% on the same weekday last week. Success closed at **95.56%**, in line with the trailing 28-day median of 95.31%.

Category Bills carried 1,265 attempts, 91% up its trailing median and 17.6% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,388 | −5.9% | +26.3% | 11,851 |
| Successful payments | 10,882 | −6.1% | +27.1% | 11,326 |
| Success rate | 95.56% | −0.16pp | +0.65pp | 95.56% |
| Settled value | ₹1.35 Cr | −6.4% | +28.9% | ₹1.34 Cr |
| Average ticket | ₹1,237 | −0.3% | +1.4% | ₹1,184 |
| Technical declines | 0.395% | +0.05pp | −0.06pp | 0.452% |
| Business declines | 3.591% | +0.35pp | −0.47pp | 3.412% |
| Risk declines | 0.105% | −0.13pp | −0.01pp | 0.173% |
| Timeout declines | 0.272% | −0.01pp | −0.05pp | 0.262% |
| Retry share | 1.26% | +0.04pp | −0.58pp | 1.26% |
| Latency p95 | 1,243 ms | −0.4% | −1.5% | 1,234 ms |
| Active customers | 9,508 | −5.7% | +22.6% | 9,884 |
| Active merchants | 1,276 | +0.0% | +10.5% | 1,279 |

## What moved

- Category Bills carried 1,265 attempts, 91% up its trailing median and 17.6% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,185 | 36.7% | 94.67% | ₹45.37 L | +4.2% |
| UPI Person to Merchant | 3,370 | 29.6% | 95.88% | ₹34.38 L | +14.2% |
| UPI QR Payments | 1,886 | 16.6% | 97.08% | ₹7.82 L | +9.2% |
| UPI Lite | 816 | 7.2% | 98.77% | ₹69,692 | +22.5% |
| UPI AutoPay | 294 | 2.6% | 88.78% | ₹5.01 L | −3.3% |
| RuPay Credit on UPI | 241 | 2.1% | 93.78% | ₹12.15 L | +24.5% |
| Credit on UPI | 145 | 1.3% | 94.48% | ₹15.06 L | +10.3% |
| UPI Circle | 107 | 0.9% | 98.13% | ₹1.18 L | +15.7% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,584 | 96.01% | 95.03% | ₹40.80 L | normal |
| HDFC Bank | 1,277 | 95.54% | 95.95% | ₹19.29 L | normal |
| Bank of Baroda | 838 | 93.32% | 94.70% | ₹8.01 L | normal |
| Union Bank of India | 819 | 95.60% | 94.72% | ₹9.86 L | normal |
| Punjab National Bank | 722 | 96.26% | 94.76% | ₹7.86 L | normal |
| Axis Bank | 698 | 95.56% | 95.18% | ₹7.97 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,430 | 95.54% | 95.14% | ₹64.05 L | normal |
| Google Pay | 3,676 | 95.81% | 95.31% | ₹40.69 L | normal |
| Paytm | 948 | 93.88% | 94.80% | ₹12.97 L | normal |
| Navi | 407 | 95.09% | 95.91% | ₹4.18 L | normal |
| SuperMoney | 225 | 97.33% | 95.62% | ₹2.46 L | normal |
| FamApp | 121 | 95.04% | 95.47% | ₹1.90 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,647 | 96.49% | ₹32.22 L |
| Food & Beverage | 1,654 | 96.92% | ₹7.75 L |
| Bills | 1,265 | 95.81% | ₹14.86 L |
| Mobility | 714 | 96.64% | ₹4.81 L |
| Healthcare | 319 | 96.24% | ₹4.28 L |
| Digital | 283 | 92.58% | ₹1.59 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,441 | 30.2% | 95.64% | ₹42.60 L |
| North | 2,819 | 24.8% | 95.71% | ₹30.96 L |
| West | 2,754 | 24.2% | 95.79% | ₹30.80 L |
| East | 1,388 | 12.2% | 95.24% | ₹17.80 L |
| Central | 986 | 8.7% | 94.62% | ₹12.39 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 22 | 100.00% | ₹1.71 L |
| Ujjwal Water Board | Key Account | Bills | 79 | 96.20% | ₹1.52 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 98.44% | ₹1.51 L |
| Rapid Bazaar | Key Account | Retail | 275 | 96.00% | ₹1.11 L |
| Girnar Connect | Key Account | Bills | 214 | 97.20% | ₹74,817 |
| Hampi Stores 2298 | Key Account | Retail | 98 | 95.92% | ₹65,576 |
| Yamuna Restaurant | Key Account | Food & Beverage | 84 | 96.43% | ₹64,956 |
| Urban Boutique | Key Account | Retail | 78 | 93.59% | ₹62,968 |

## Failure analysis

Of 497 declined attempts, 409 were business declines (3.591% of attempts — balances, PINs and limits), 45 technical (0.395%), 31 timeouts (0.272%) and 12 risk declines (0.105%).

143 attempts were re-presentations of an earlier failure (1.26% of the day); 64.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 177 | 1.554% | 1.460% |
| ZM | Invalid UPI PIN | business | Customer | 145 | 1.273% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.404% | 0.416% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.237% | 0.257% |
| XH | Account does not exist / frozen | business | Issuer | 21 | 0.184% | 0.238% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.158% | 0.183% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 10 | 0.088% | 0.113% |
| UX | Mandate execution outside permitted window | business | PSP | 9 | 0.079% | 0.103% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 74 | 60 |
| Auto-reversals | 17 | 22 |
| Disputes / chargebacks | 4 | 2 |
| Value returned | ₹79,572 | ₹97,625 |

## Customer behaviour

9,508 distinct customers transacted (+7.5% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,936 | 3,343 | 1.14 | 95.18% | ₹1,302 |
| merchant_heavy | 2,199 | 2,669 | 1.21 | 96.07% | ₹900 |
| power | 1,975 | 2,629 | 1.33 | 94.48% | ₹1,736 |
| small_ticket | 1,469 | 1,772 | 1.21 | 96.16% | ₹522 |
| occasional | 726 | 754 | 1.04 | 96.95% | ₹1,237 |
| new | 186 | 202 | 1.09 | 98.51% | ₹1,294 |
| dormant_returning | 17 | 19 | 1.12 | 94.74% | ₹980 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

03 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 95.56% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-03` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,388, successes=10,882, failed=497, pending=9, settled_value_inr=13,455,827.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- categories: mcc_category=Bills; attempts=1,265; own_median=663.5; z=4.98
- categories: mcc_category=Digital; attempts=283; own_median=197; z=3.87
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=UPI 123Pay; attempts=81; own_median=58; z=3.45

Refs: enterprise_data/warehouse/transactions, RPT-D29-DAILY, enterprise_data/warehouse/reference/incidents.parquet
