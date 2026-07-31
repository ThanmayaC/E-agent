---
id: RPT-D63-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 08 Mar 2026)

**Report ID:** RPT-D63-DAILY · **Day 63 of 206** · **Derived from:** 11,731 transaction rows queried live from the warehouse

## Summary

The rail took **11,731 payment attempts** on Sunday 08 March 2026 (Weekend) and settled **₹1.24 Cr** across 11,217 successful payments. Volume was −16.2% on yesterday and −22.0% on the same weekday last week. Success closed at **95.62%**, in line with the trailing 28-day median of 95.56%.

Product UPI Circle is compounding — attempts up 81% across the trailing window to 219 today, with success holding, so the growth is healthy and worth funding. Product UPI QR Payments is compounding — attempts up 51% across the trailing window to 2,160 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,731 | −16.2% | −22.0% | 14,121 |
| Successful payments | 11,217 | −16.4% | −22.2% | 13,544 |
| Success rate | 95.62% | −0.31pp | −0.26pp | 95.91% |
| Settled value | ₹1.24 Cr | −25.9% | −20.0% | ₹1.60 Cr |
| Average ticket | ₹1,105 | −11.3% | +2.8% | ₹1,187 |
| Technical declines | 0.554% | +0.18pp | +0.22pp | 0.399% |
| Business declines | 3.239% | +0.13pp | −0.14pp | 3.172% |
| Risk declines | 0.077% | −0.06pp | −0.02pp | 0.111% |
| Timeout declines | 0.401% | +0.02pp | +0.16pp | 0.313% |
| Retry share | 1.53% | +0.43pp | +0.27pp | 1.20% |
| Latency p95 | 1,205 ms | −3.5% | −0.7% | 1,218 ms |
| Active customers | 9,834 | −14.0% | −18.4% | 11,471 |
| Active merchants | 1,288 | −6.1% | −5.2% | 1,352 |

## What moved

- Product UPI Circle is compounding — attempts up 81% across the trailing window to 219 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments is compounding — attempts up 51% across the trailing window to 2,160 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,348 | 37.1% | 94.78% | ₹46.23 L | +10.5% |
| UPI Person to Merchant | 3,185 | 27.2% | 96.04% | ₹29.02 L | +1.4% |
| UPI QR Payments | 2,160 | 18.4% | 96.25% | ₹8.74 L | +19.0% |
| UPI Lite | 951 | 8.1% | 98.95% | ₹91,427 | +25.2% |
| UPI AutoPay | 345 | 2.9% | 91.01% | ₹6.22 L | +14.6% |
| UPI Circle | 219 | 1.9% | 97.26% | ₹2.01 L | +93.8% |
| RuPay Credit on UPI | 142 | 1.2% | 95.77% | ₹5.31 L | −32.7% |
| Recurring Payments | 82 | 0.7% | 89.02% | ₹3.87 L | −7.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,684 | 95.58% | 95.47% | ₹38.15 L | normal |
| HDFC Bank | 1,293 | 95.59% | 96.16% | ₹11.21 L | normal |
| Bank of Baroda | 913 | 95.62% | 95.40% | ₹7.64 L | normal |
| Union Bank of India | 809 | 94.68% | 95.26% | ₹6.49 L | normal |
| Punjab National Bank | 733 | 95.23% | 94.96% | ₹11.01 L | normal |
| Axis Bank | 729 | 95.75% | 95.79% | ₹9.60 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,517 | 95.47% | 95.66% | ₹55.39 L | normal |
| Google Pay | 3,911 | 95.50% | 95.61% | ₹44.74 L | normal |
| Paytm | 976 | 96.82% | 95.28% | ₹9.04 L | normal |
| Navi | 420 | 96.19% | 95.26% | ₹4.75 L | normal |
| SuperMoney | 236 | 93.22% | 96.01% | ₹2.81 L | normal |
| BHIM | 101 | 92.08% | 95.09% | ₹1.21 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,253 | 96.59% | ₹28.85 L |
| Food & Beverage | 1,788 | 96.64% | ₹7.08 L |
| Mobility | 847 | 96.46% | ₹4.25 L |
| Bills | 633 | 95.73% | ₹6.64 L |
| Healthcare | 352 | 95.74% | ₹2.89 L |
| Digital | 194 | 92.78% | ₹79,207 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,411 | 29.1% | 95.90% | ₹34.47 L |
| North | 2,927 | 25.0% | 96.04% | ₹30.44 L |
| West | 2,905 | 24.8% | 95.56% | ₹31.81 L |
| East | 1,407 | 12.0% | 94.95% | ₹17.47 L |
| Central | 1,081 | 9.2% | 94.63% | ₹9.79 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 402 | 96.27% | ₹1.51 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 98.36% | ₹1.30 L |
| Urban Boutique | Key Account | Retail | 97 | 93.81% | ₹86,411 |
| Hampi Styles | Key Account | Retail | 30 | 96.67% | ₹72,744 |
| Vega Electronics | Large | Retail | 22 | 86.36% | ₹62,862 |
| Ujjwal Water Board | Key Account | Bills | 35 | 97.14% | ₹61,557 |
| Hampi Stores 2298 | Key Account | Retail | 85 | 95.29% | ₹57,612 |
| Girnar Connect | Key Account | Bills | 99 | 96.97% | ₹49,615 |

## Failure analysis

Of 501 declined attempts, 380 were business declines (3.239% of attempts — balances, PINs and limits), 65 technical (0.554%), 47 timeouts (0.401%) and 9 risk declines (0.077%).

179 attempts were re-presentations of an earlier failure (1.53% of the day); 68.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 154 | 1.313% | 1.468% |
| ZM | Invalid UPI PIN | business | Customer | 127 | 1.083% | 1.143% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.375% | 0.410% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.247% | 0.155% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.213% | 0.164% |
| XH | Account does not exist / frozen | business | Issuer | 23 | 0.196% | 0.248% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.153% | 0.111% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.145% | 0.104% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 67 | 68 |
| Auto-reversals | 28 | 20 |
| Disputes / chargebacks | 9 | 8 |
| Value returned | ₹68,806 | ₹89,740 |

## Customer behaviour

9,834 distinct customers transacted (+9.9% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,076 | 3,525 | 1.15 | 95.94% | ₹1,315 |
| power | 2,068 | 2,713 | 1.31 | 95.69% | ₹1,390 |
| merchant_heavy | 2,231 | 2,665 | 1.19 | 95.42% | ₹732 |
| small_ticket | 1,437 | 1,738 | 1.21 | 95.57% | ₹468 |
| occasional | 796 | 841 | 1.06 | 94.53% | ₹1,260 |
| new | 192 | 214 | 1.11 | 97.20% | ₹655 |
| dormant_returning | 34 | 35 | 1.03 | 91.43% | ₹865 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **CMP-0058** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Issuer IDFC First Bank ran at 94.06% success on 320 attempts (2.7% of the day), 1.55pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 81% across the trailing window to 219 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments is compounding — attempts up 51% across the trailing window to 2,160 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

08 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.62% success against a 95.56% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,731, successes=11,217, failed=501, pending=13, settled_value_inr=12,398,648.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=219; window_growth_pct=80.6; success_rate=97.26
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI QR Payments; attempts=2,160; window_growth_pct=50.8; success_rate=96.25
- banks: payer_bank=IDFC First Bank; attempts=320; success_rate=94.06; own_median=95.62; z=-2.66
- banks: payer_bank=Indian Bank; attempts=336; success_rate=97.92; own_median=95.18; z=2.37
- incidents: event_id=ADOPT-0075; kind=adoption_surge; severity=Sev-3; window=2026-02-24 to 2026-03-08; success_impact_pp=-0.32; volume_impact_pct=22.24
- incidents: event_id=CMP-0058; kind=merchant_campaign; severity=Sev-3; window=2026-03-07 to 2026-03-10; success_impact_pp=-0.16; volume_impact_pct=63.89
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- products: product_name=UPI Circle; attempts=219; own_median=113; z=3.4
- products: product_name=UPI AutoPay; attempts=345; own_median=301; z=2.7

Refs: enterprise_data/warehouse/transactions, RPT-D62-DAILY, enterprise_data/warehouse/reference/incidents.parquet
