---
id: RPT-D31-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-04T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 04 Feb 2026)

**Report ID:** RPT-D31-DAILY · **Day 31 of 206** · **Derived from:** 10,905 transaction rows queried live from the warehouse

## Summary

The rail took **10,905 payment attempts** on Wednesday 04 February 2026 (Working day) and settled **₹1.38 Cr** across 10,447 successful payments. Volume was −4.2% on yesterday and +23.8% on the same weekday last week. Success closed at **95.80%**, above the trailing 28-day median of 95.31%.

Category Bills carried 1,199 attempts, 81% up its trailing median and 17.0% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,905 | −4.2% | +23.8% | 11,615 |
| Successful payments | 10,447 | −4.0% | +25.5% | 11,106 |
| Success rate | 95.80% | +0.24pp | +1.32pp | 95.62% |
| Settled value | ₹1.38 Cr | +2.5% | +32.5% | ₹1.35 Cr |
| Average ticket | ₹1,321 | +6.8% | +5.6% | ₹1,218 |
| Technical declines | 0.358% | −0.04pp | −0.04pp | 0.428% |
| Business declines | 3.356% | −0.24pp | −1.07pp | 3.398% |
| Risk declines | 0.156% | +0.05pp | +0.02pp | 0.169% |
| Timeout declines | 0.229% | −0.04pp | −0.22pp | 0.254% |
| Retry share | 1.25% | −0.01pp | −0.43pp | 1.25% |
| Latency p95 | 1,236 ms | −0.5% | −3.3% | 1,234 ms |
| Active customers | 9,160 | −3.7% | +19.8% | 9,703 |
| Active merchants | 1,267 | −0.7% | +7.9% | 1,276 |

## What moved

- Category Bills carried 1,199 attempts, 81% up its trailing median and 17.0% of the day's volume.
- Category Digital carried 307 attempts, 56% up its trailing median and 4.4% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,871 | 35.5% | 94.96% | ₹42.12 L | −3.7% |
| UPI Person to Merchant | 3,394 | 31.1% | 96.29% | ₹35.11 L | +13.6% |
| UPI QR Payments | 1,790 | 16.4% | 96.59% | ₹7.60 L | +3.3% |
| UPI Lite | 728 | 6.7% | 98.08% | ₹64,298 | +9.3% |
| UPI AutoPay | 310 | 2.8% | 90.97% | ₹5.80 L | +2.1% |
| RuPay Credit on UPI | 192 | 1.8% | 97.40% | ₹9.96 L | −2.0% |
| Credit on UPI | 168 | 1.5% | 94.05% | ₹13.06 L | +27.8% |
| UPI International | 108 | 1.0% | 95.37% | ₹17.71 L | +52.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,468 | 95.76% | 95.06% | ₹42.17 L | normal |
| HDFC Bank | 1,162 | 96.82% | 95.95% | ₹17.41 L | normal |
| Union Bank of India | 799 | 95.87% | 94.72% | ₹9.50 L | normal |
| Bank of Baroda | 791 | 95.95% | 94.56% | ₹9.75 L | normal |
| ICICI Bank | 680 | 96.47% | 96.12% | ₹8.74 L | normal |
| Axis Bank | 678 | 95.13% | 95.18% | ₹6.67 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,186 | 95.74% | 95.14% | ₹66.96 L | normal |
| Google Pay | 3,560 | 96.04% | 95.31% | ₹44.19 L | normal |
| Paytm | 903 | 95.57% | 94.80% | ₹11.55 L | normal |
| Navi | 388 | 94.59% | 95.86% | ₹3.64 L | normal |
| SuperMoney | 200 | 94.50% | 95.79% | ₹2.69 L | normal |
| BHIM | 112 | 97.32% | 94.59% | ₹1.96 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,558 | 96.36% | ₹29.73 L |
| Food & Beverage | 1,598 | 97.06% | ₹8.76 L |
| Bills | 1,199 | 96.33% | ₹14.47 L |
| Mobility | 728 | 97.12% | ₹4.43 L |
| Healthcare | 333 | 97.00% | ₹2.40 L |
| Digital | 307 | 94.46% | ₹1.73 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,260 | 29.9% | 95.15% | ₹42.06 L |
| North | 2,694 | 24.7% | 96.07% | ₹31.87 L |
| West | 2,601 | 23.9% | 96.00% | ₹36.43 L |
| East | 1,414 | 13.0% | 95.97% | ₹17.86 L |
| Central | 936 | 8.6% | 96.47% | ₹9.73 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 22 | 100.00% | ₹2.04 L |
| Ujjwal Water Board | Key Account | Bills | 72 | 100.00% | ₹1.89 L |
| Vasant Wardrobe | Key Account | Retail | 75 | 98.67% | ₹1.43 L |
| Rapid Bazaar | Key Account | Retail | 267 | 97.00% | ₹1.40 L |
| Girnar Connect | Key Account | Bills | 199 | 96.48% | ₹73,454 |
| Yamuna Restaurant | Key Account | Food & Beverage | 64 | 98.44% | ₹73,236 |
| Urban Boutique | Key Account | Retail | 80 | 96.25% | ₹55,083 |
| Swift Mart 1738 | Key Account | Retail | 78 | 100.00% | ₹54,157 |

## Failure analysis

Of 447 declined attempts, 366 were business declines (3.356% of attempts — balances, PINs and limits), 39 technical (0.358%), 25 timeouts (0.229%) and 17 risk declines (0.156%).

136 attempts were re-presentations of an earlier failure (1.25% of the day); 64.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 140 | 1.284% | 1.482% |
| ZM | Invalid UPI PIN | business | Customer | 131 | 1.201% | 1.117% |
| ZA | Transaction declined by customer | business | Customer | 38 | 0.348% | 0.416% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.202% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.193% | 0.257% |
| UX | Mandate execution outside permitted window | business | PSP | 18 | 0.165% | 0.103% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.147% | 0.111% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 15 | 0.138% | 0.182% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 73 | 60 |
| Auto-reversals | 16 | 22 |
| Disputes / chargebacks | 4 | 3 |
| Value returned | ₹1.23 L | ₹97,625 |

## Customer behaviour

9,160 distinct customers transacted (+3.5% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,799 | 3,163 | 1.13 | 96.24% | ₹1,367 |
| power | 1,965 | 2,618 | 1.33 | 95.65% | ₹1,670 |
| merchant_heavy | 2,064 | 2,453 | 1.19 | 95.39% | ₹1,089 |
| small_ticket | 1,390 | 1,680 | 1.21 | 95.54% | ₹601 |
| occasional | 746 | 781 | 1.05 | 95.77% | ₹1,269 |
| new | 176 | 190 | 1.08 | 98.42% | ₹2,004 |
| dormant_returning | 20 | 20 | 1.00 | 95.00% | ₹2,250 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

04 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 95.80% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-04` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,905, successes=10,447, failed=447, pending=11, settled_value_inr=13,795,649.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- categories: mcc_category=Bills; attempts=1,199; own_median=663.5; z=4.43
- categories: mcc_category=Digital; attempts=307; own_median=197; z=4.95
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- products: product_name=UPI International; attempts=108; own_median=71; z=2.38
- products: product_name=UPI 123Pay; attempts=78; own_median=58; z=2.45

Refs: enterprise_data/warehouse/transactions, RPT-D30-DAILY, enterprise_data/warehouse/reference/incidents.parquet
