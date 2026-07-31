---
id: RPT-D32-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 05 Feb 2026)

**Report ID:** RPT-D32-DAILY · **Day 32 of 206** · **Derived from:** 10,488 transaction rows queried live from the warehouse

## Summary

The rail took **10,488 payment attempts** on Thursday 05 February 2026 (Working day) and settled **₹1.34 Cr** across 10,017 successful payments. Volume was −3.8% on yesterday and +22.5% on the same weekday last week. Success closed at **95.51%**, in line with the trailing 28-day median of 95.31%.

7 disputes were raised, 2.7 sigma above the trailing median of 3.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,488 | −3.8% | +22.5% | 11,389 |
| Successful payments | 10,017 | −4.1% | +22.8% | 10,888 |
| Success rate | 95.51% | −0.29pp | +0.24pp | 95.60% |
| Settled value | ₹1.34 Cr | −3.2% | +39.9% | ₹1.35 Cr |
| Average ticket | ₹1,333 | +1.0% | +13.9% | ₹1,241 |
| Technical declines | 0.448% | +0.09pp | −0.02pp | 0.432% |
| Business declines | 3.576% | +0.22pp | −0.13pp | 3.434% |
| Risk declines | 0.124% | −0.03pp | +0.02pp | 0.160% |
| Timeout declines | 0.257% | +0.03pp | −0.08pp | 0.254% |
| Retry share | 1.21% | −0.04pp | −0.45pp | 1.25% |
| Latency p95 | 1,288 ms | +4.2% | −2.2% | 1,245 ms |
| Active customers | 8,894 | −2.9% | +20.0% | 9,541 |
| Active merchants | 1,253 | −1.1% | +9.0% | 1,272 |

## What moved

- Category Bills carried 1,142 attempts, 72% up its trailing median and 17.3% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,904 | 37.2% | 95.13% | ₹43.47 L | −2.9% |
| UPI Person to Merchant | 3,138 | 29.9% | 95.83% | ₹30.71 L | +5.1% |
| UPI QR Payments | 1,650 | 15.7% | 96.24% | ₹7.13 L | −4.7% |
| UPI Lite | 718 | 6.8% | 99.03% | ₹68,814 | +3.6% |
| UPI AutoPay | 297 | 2.8% | 90.24% | ₹4.40 L | −2.1% |
| RuPay Credit on UPI | 211 | 2.0% | 93.36% | ₹13.27 L | +9.9% |
| Credit on UPI | 161 | 1.5% | 94.41% | ₹17.08 L | +22.4% |
| UPI Circle | 107 | 1.0% | 93.46% | ₹1.19 L | +14.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,388 | 95.84% | 95.06% | ₹43.79 L | normal |
| HDFC Bank | 1,127 | 95.21% | 95.95% | ₹11.48 L | normal |
| Bank of Baroda | 815 | 95.21% | 94.56% | ₹14.58 L | normal |
| Union Bank of India | 737 | 96.07% | 94.72% | ₹9.14 L | normal |
| Axis Bank | 624 | 95.83% | 95.19% | ₹7.40 L | normal |
| Canara Bank | 621 | 95.65% | 94.59% | ₹8.56 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,962 | 95.57% | 95.14% | ₹65.44 L | normal |
| Google Pay | 3,447 | 95.62% | 95.31% | ₹45.91 L | normal |
| Paytm | 879 | 95.79% | 94.80% | ₹10.44 L | normal |
| Navi | 397 | 95.21% | 95.70% | ₹4.13 L | normal |
| SuperMoney | 206 | 96.60% | 95.79% | ₹2.35 L | normal |
| BHIM | 102 | 94.12% | 94.59% | ₹1.06 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,447 | 95.55% | ₹34.99 L |
| Food & Beverage | 1,411 | 96.95% | ₹6.76 L |
| Bills | 1,142 | 96.32% | ₹12.08 L |
| Mobility | 682 | 95.60% | ₹3.92 L |
| Healthcare | 333 | 97.00% | ₹3.13 L |
| Digital | 267 | 95.13% | ₹1.82 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,123 | 29.8% | 95.55% | ₹38.61 L |
| North | 2,636 | 25.1% | 95.07% | ₹34.40 L |
| West | 2,531 | 24.1% | 95.65% | ₹31.89 L |
| East | 1,291 | 12.3% | 95.89% | ₹19.02 L |
| Central | 907 | 8.6% | 95.70% | ₹9.64 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 287 | 97.56% | ₹1.43 L |
| Vasant Wardrobe | Key Account | Retail | 56 | 92.86% | ₹1.32 L |
| Ujjwal Water Board | Key Account | Bills | 68 | 94.12% | ₹97,736 |
| Girnar Connect | Key Account | Bills | 167 | 96.41% | ₹84,555 |
| Yamuna Restaurant | Key Account | Food & Beverage | 67 | 95.52% | ₹80,762 |
| Vega Electronics | Large | Retail | 22 | 81.82% | ₹64,430 |
| Hampi Stores 2298 | Key Account | Retail | 73 | 93.15% | ₹60,105 |
| Aravalli Pharmacy | Large | Healthcare | 65 | 96.92% | ₹47,980 |

## Failure analysis

Of 462 declined attempts, 375 were business declines (3.576% of attempts — balances, PINs and limits), 47 technical (0.448%), 27 timeouts (0.257%) and 13 risk declines (0.124%).

127 attempts were re-presentations of an earlier failure (1.21% of the day); 57.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.478% | 1.481% |
| ZM | Invalid UPI PIN | business | Customer | 130 | 1.240% | 1.132% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.429% | 0.416% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.238% | 0.237% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.210% | 0.257% |
| UX | Mandate execution outside permitted window | business | PSP | 15 | 0.143% | 0.107% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.124% | 0.158% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 12 | 0.114% | 0.176% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 72 | 61 |
| Auto-reversals | 20 | 22 |
| Disputes / chargebacks | 7 | 3 |
| Value returned | ₹2.08 L | ₹99,264 |

## Customer behaviour

8,894 distinct customers transacted (+0.5% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,660 | 2,974 | 1.12 | 95.43% | ₹1,379 |
| power | 1,906 | 2,500 | 1.31 | 94.76% | ₹1,925 |
| merchant_heavy | 2,049 | 2,402 | 1.17 | 95.67% | ₹968 |
| small_ticket | 1,357 | 1,647 | 1.21 | 95.69% | ₹627 |
| occasional | 706 | 736 | 1.04 | 97.01% | ₹1,187 |
| new | 181 | 194 | 1.07 | 96.91% | ₹859 |
| dormant_returning | 35 | 35 | 1.00 | 97.14% | ₹1,257 |

## Operational events

- **INC-FRAUD-0049** (Sev-2) — Fraud pattern on Credit on UPI — Travel Booking, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Travel Booking merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 7 disputes were raised, 2.7 sigma above the trailing median of 3.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

05 February was an incident day: INC-FRAUD-0049 was live and the rail closed at 95.51% success against a 95.31% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,488, successes=10,017, failed=462, pending=9, settled_value_inr=13,356,055.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=7; trailing_median=3; z=2.7
- incidents: event_id=INC-FRAUD-0049; kind=fraud_spike; severity=Sev-2; window=2026-02-02 to 2026-02-12; success_impact_pp=-1.95; volume_impact_pct=17.33
- categories: mcc_category=Bills; attempts=1,142; own_median=663.5; z=3.96
- categories: mcc_category=Digital; attempts=267; own_median=197; z=3.15
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24

Refs: enterprise_data/warehouse/transactions, RPT-D31-DAILY, enterprise_data/warehouse/reference/incidents.parquet
