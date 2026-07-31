---
id: RPT-D29-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-02T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 02 Feb 2026)

**Report ID:** RPT-D29-DAILY · **Day 29 of 206** · **Derived from:** 12,106 transaction rows queried live from the warehouse

## Summary

The rail took **12,106 payment attempts** on Monday 02 February 2026 (Working day) and settled **₹1.44 Cr** across 11,588 successful payments. Volume was +0.4% on yesterday and +24.9% on the same weekday last week. Success closed at **95.72%**, above the trailing 28-day median of 95.31%.

Category Bills carried 1,211 attempts, 83% up its trailing median and 16.5% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,106 | +0.4% | +24.9% | 12,083 |
| Successful payments | 11,588 | +0.7% | +25.6% | 11,548 |
| Success rate | 95.72% | +0.31pp | +0.57pp | 95.57% |
| Settled value | ₹1.44 Cr | +16.1% | +47.3% | ₹1.34 Cr |
| Average ticket | ₹1,241 | +15.3% | +17.3% | ₹1,158 |
| Technical declines | 0.347% | −0.27pp | −0.29pp | 0.480% |
| Business declines | 3.246% | −0.15pp | −0.16pp | 3.323% |
| Risk declines | 0.231% | +0.05pp | +0.01pp | 0.207% |
| Timeout declines | 0.281% | +0.05pp | −0.11pp | 0.257% |
| Retry share | 1.21% | −0.09pp | −0.47pp | 1.26% |
| Latency p95 | 1,248 ms | +3.1% | +0.4% | 1,229 ms |
| Active customers | 10,088 | +0.3% | +21.0% | 10,072 |
| Active merchants | 1,276 | −0.8% | +8.8% | 1,281 |

## What moved

- Category Bills carried 1,211 attempts, 83% up its trailing median and 16.5% of the day's volume.
- Region West carried 2,964 attempts, 18% up its trailing median and 24.5% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,761 | 39.3% | 94.79% | ₹54.55 L | +19.0% |
| UPI Person to Merchant | 3,324 | 27.5% | 96.27% | ₹32.78 L | +12.6% |
| UPI QR Payments | 2,035 | 16.8% | 96.86% | ₹8.42 L | +19.1% |
| UPI Lite | 870 | 7.2% | 98.74% | ₹80,116 | +30.6% |
| UPI AutoPay | 286 | 2.4% | 92.31% | ₹5.02 L | −5.9% |
| RuPay Credit on UPI | 223 | 1.8% | 92.38% | ₹9.38 L | +16.8% |
| Credit on UPI | 157 | 1.3% | 94.90% | ₹20.30 L | +19.4% |
| UPI Circle | 136 | 1.1% | 97.79% | ₹1.02 L | +47.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,795 | 96.13% | 95.03% | ₹43.14 L | normal |
| HDFC Bank | 1,337 | 96.41% | 95.95% | ₹18.35 L | normal |
| Bank of Baroda | 899 | 96.33% | 94.57% | ₹10.83 L | normal |
| Axis Bank | 800 | 93.88% | 95.26% | ₹7.89 L | normal |
| Union Bank of India | 795 | 95.72% | 94.72% | ₹11.53 L | normal |
| ICICI Bank | 754 | 96.29% | 96.00% | ₹9.03 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,784 | 95.44% | 95.14% | ₹66.95 L | normal |
| Google Pay | 3,966 | 96.14% | 95.31% | ₹46.80 L | normal |
| Paytm | 976 | 95.90% | 94.80% | ₹10.68 L | normal |
| Navi | 405 | 96.54% | 95.91% | ₹4.77 L | normal |
| SuperMoney | 241 | 96.27% | 95.62% | ₹2.92 L | normal |
| BHIM | 134 | 97.01% | 94.86% | ₹1.21 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,693 | 96.14% | ₹30.50 L |
| Food & Beverage | 1,660 | 97.71% | ₹8.28 L |
| Bills | 1,211 | 96.04% | ₹14.53 L |
| Mobility | 845 | 96.80% | ₹4.92 L |
| Healthcare | 375 | 95.73% | ₹3.39 L |
| Digital | 279 | 96.42% | ₹1.90 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,591 | 29.7% | 95.57% | ₹42.96 L |
| North | 3,084 | 25.5% | 95.10% | ₹36.26 L |
| West | 2,964 | 24.5% | 95.88% | ₹38.00 L |
| East | 1,481 | 12.2% | 96.89% | ₹16.23 L |
| Central | 986 | 8.1% | 95.94% | ₹10.33 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 87.10% | ₹2.62 L |
| Rapid Bazaar | Key Account | Retail | 254 | 94.88% | ₹1.12 L |
| Ujjwal Water Board | Key Account | Bills | 62 | 93.55% | ₹1.03 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 98.36% | ₹97,889 |
| Hampi Stores 2298 | Key Account | Retail | 92 | 95.65% | ₹92,726 |
| Girnar Connect | Key Account | Bills | 202 | 95.05% | ₹88,727 |
| Yamuna Restaurant | Key Account | Food & Beverage | 75 | 100.00% | ₹86,360 |
| Urban Boutique | Key Account | Retail | 77 | 93.51% | ₹47,758 |

## Failure analysis

Of 497 declined attempts, 393 were business declines (3.246% of attempts — balances, PINs and limits), 42 technical (0.347%), 34 timeouts (0.281%) and 28 risk declines (0.231%).

147 attempts were re-presentations of an earlier failure (1.21% of the day); 63.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 152 | 1.256% | 1.482% |
| ZM | Invalid UPI PIN | business | Customer | 129 | 1.066% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.454% | 0.405% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.198% | 0.238% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 21 | 0.173% | 0.113% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.165% | 0.261% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.149% | 0.183% |
| UX | Mandate execution outside permitted window | business | PSP | 18 | 0.149% | 0.097% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 71 | 60 |
| Auto-reversals | 16 | 22 |
| Disputes / chargebacks | 5 | 2 |
| Value returned | ₹98,776 | ₹93,909 |

## Customer behaviour

10,088 distinct customers transacted (+14.0% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,109 | 3,543 | 1.14 | 95.51% | ₹1,299 |
| power | 2,063 | 2,764 | 1.34 | 95.30% | ₹1,660 |
| merchant_heavy | 2,266 | 2,751 | 1.21 | 95.60% | ₹1,067 |
| small_ticket | 1,562 | 1,899 | 1.22 | 96.21% | ₹517 |
| occasional | 843 | 884 | 1.05 | 96.61% | ₹1,210 |
| new | 212 | 232 | 1.09 | 97.41% | ₹761 |
| dormant_returning | 33 | 33 | 1.00 | 100.00% | ₹715 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

02 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 95.72% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-02` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,106, successes=11,588, failed=497, pending=21, settled_value_inr=14,378,361.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- categories: mcc_category=Bills; attempts=1,211; own_median=663.5; z=4.53
- geography: region=West; attempts=2,964; own_median=2,517; z=2.38
- categories: mcc_category=Mobility; attempts=845; own_median=649.5; z=2.66
- categories: mcc_category=Digital; attempts=279; own_median=197; z=3.69
- products: product_name=UPI Lite; attempts=870; own_median=666; z=2.37
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- banks: payer_bank=Kotak Mahindra Bank; attempts=457; own_median=365; z=2.3
- products: product_name=UPI Circle; attempts=136; own_median=92.5; z=3.67

Refs: enterprise_data/warehouse/transactions, RPT-D28-DAILY, enterprise_data/warehouse/reference/incidents.parquet
