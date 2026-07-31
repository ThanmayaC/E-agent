---
id: RPT-D69-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 14 Mar 2026)

**Report ID:** RPT-D69-DAILY · **Day 69 of 206** · **Derived from:** 12,311 transaction rows queried live from the warehouse

## Summary

The rail took **12,311 payment attempts** on Saturday 14 March 2026 (Weekend) and settled **₹1.33 Cr** across 11,789 successful payments. Volume was +3.4% on yesterday and −12.0% on the same weekday last week. Success closed at **95.76%**, in line with the trailing 28-day median of 95.64%.

Product UPI Circle is compounding — attempts up 82% across the trailing window to 222 today, with success holding, so the growth is healthy and worth funding. Product UPI International is compounding — attempts up 48% across the trailing window to 72 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,311 | +3.4% | −12.0% | 12,964 |
| Successful payments | 11,789 | +3.4% | −12.2% | 12,418 |
| Success rate | 95.76% | +0.08pp | −0.17pp | 95.76% |
| Settled value | ₹1.33 Cr | −6.0% | −20.7% | ₹1.48 Cr |
| Average ticket | ₹1,125 | −9.2% | −9.7% | ₹1,197 |
| Technical declines | 0.455% | −0.03pp | +0.08pp | 0.457% |
| Business declines | 3.241% | −0.04pp | +0.13pp | 3.213% |
| Risk declines | 0.089% | −0.05pp | −0.05pp | 0.119% |
| Timeout declines | 0.317% | −0.05pp | −0.06pp | 0.352% |
| Retry share | 1.26% | +0.20pp | +0.16pp | 1.30% |
| Latency p95 | 1,188 ms | −3.7% | −4.9% | 1,249 ms |
| Active customers | 10,230 | +2.7% | −10.6% | 10,672 |
| Active merchants | 1,323 | −0.5% | −3.5% | 1,332 |

## What moved

- Product UPI Circle is compounding — attempts up 82% across the trailing window to 222 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 48% across the trailing window to 72 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,379 | 35.6% | 95.00% | ₹46.60 L | +6.0% |
| UPI Person to Merchant | 3,682 | 29.9% | 95.68% | ₹33.35 L | +14.3% |
| UPI QR Payments | 2,126 | 17.3% | 96.71% | ₹8.72 L | +5.1% |
| UPI Lite | 1,040 | 8.4% | 99.04% | ₹96,027 | +33.8% |
| UPI AutoPay | 308 | 2.5% | 90.58% | ₹6.23 L | +0.2% |
| UPI Circle | 222 | 1.8% | 96.40% | ₹1.61 L | +53.1% |
| RuPay Credit on UPI | 150 | 1.2% | 96.67% | ₹11.50 L | −31.5% |
| Credit on UPI | 95 | 0.8% | 96.84% | ₹6.07 L | −37.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,922 | 95.82% | 95.59% | ₹39.66 L | normal |
| HDFC Bank | 1,314 | 95.59% | 96.17% | ₹13.19 L | normal |
| Bank of Baroda | 949 | 96.10% | 95.58% | ₹8.79 L | normal |
| Union Bank of India | 840 | 95.83% | 95.26% | ₹14.57 L | normal |
| Axis Bank | 753 | 95.75% | 95.88% | ₹8.13 L | normal |
| Punjab National Bank | 750 | 95.87% | 95.03% | ₹7.92 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,831 | 95.58% | 95.72% | ₹57.90 L | normal |
| Google Pay | 4,084 | 96.03% | 95.67% | ₹46.99 L | normal |
| Paytm | 990 | 96.06% | 95.41% | ₹13.54 L | normal |
| Navi | 430 | 93.49% | 95.49% | ₹5.03 L | normal |
| SuperMoney | 243 | 97.12% | 95.88% | ₹2.23 L | normal |
| BHIM | 116 | 94.83% | 95.18% | ₹1.81 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,395 | 96.23% | ₹32.22 L |
| Food & Beverage | 2,001 | 96.55% | ₹8.95 L |
| Mobility | 859 | 97.67% | ₹3.71 L |
| Bills | 706 | 96.18% | ₹7.33 L |
| Healthcare | 403 | 96.53% | ₹3.48 L |
| Digital | 212 | 92.92% | ₹1.13 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,590 | 29.2% | 95.52% | ₹36.63 L |
| North | 3,099 | 25.2% | 95.77% | ₹30.69 L |
| West | 3,093 | 25.1% | 95.76% | ₹37.61 L |
| East | 1,469 | 11.9% | 95.78% | ₹18.62 L |
| Central | 1,060 | 8.6% | 96.51% | ₹9.13 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹1.93 L |
| Rapid Bazaar | Key Account | Retail | 386 | 98.19% | ₹1.62 L |
| Hampi Styles | Key Account | Retail | 39 | 92.31% | ₹1.29 L |
| Urban Boutique | Key Account | Retail | 87 | 97.70% | ₹1.05 L |
| Ujjwal Water Board | Key Account | Bills | 37 | 86.49% | ₹86,721 |
| Vasant Wardrobe | Key Account | Retail | 50 | 90.00% | ₹82,313 |
| Girnar Connect | Key Account | Bills | 125 | 97.60% | ₹73,200 |
| Konark Boutique | Large | Retail | 38 | 97.37% | ₹64,303 |

## Failure analysis

Of 505 declined attempts, 399 were business declines (3.241% of attempts — balances, PINs and limits), 56 technical (0.455%), 39 timeouts (0.317%) and 11 risk declines (0.089%).

155 attempts were re-presentations of an earlier failure (1.26% of the day); 60.0% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 65 times — 0.528% of attempts against a trailing 0.403%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 154 | 1.251% | 1.404% |
| ZM | Invalid UPI PIN | business | Customer | 148 | 1.202% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 65 | 0.528% | 0.403% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.219% | 0.166% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.203% | 0.168% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.179% | 0.240% |
| U28 | Remitter bank unavailable | technical | Issuer | 17 | 0.138% | 0.122% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 10 | 0.081% | 0.109% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 84 | 68 |
| Auto-reversals | 26 | 21 |
| Disputes / chargebacks | 10 | 10 |
| Value returned | ₹1.45 L | ₹89,740 |

## Customer behaviour

10,230 distinct customers transacted (+6.8% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,178 | 3,631 | 1.14 | 95.62% | ₹1,122 |
| merchant_heavy | 2,366 | 2,867 | 1.21 | 95.54% | ₹1,017 |
| power | 2,116 | 2,836 | 1.34 | 95.77% | ₹1,451 |
| small_ticket | 1,559 | 1,915 | 1.23 | 96.24% | ₹522 |
| occasional | 803 | 836 | 1.04 | 96.05% | ₹1,189 |
| new | 177 | 195 | 1.10 | 95.90% | ₹747 |
| dormant_returning | 31 | 31 | 1.00 | 93.55% | ₹733 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0065** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code ZA (Transaction declined by customer) fired 65 times — 0.528% of attempts against a trailing 0.403%. Owner: Customer.

### Opportunities

- Product UPI Circle is compounding — attempts up 82% across the trailing window to 222 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 48% across the trailing window to 72 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

14 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.76% success against a 95.64% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,311, successes=11,789, failed=505, pending=17, settled_value_inr=13,267,706.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=222; window_growth_pct=81.6; success_rate=96.4
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI International; attempts=72; window_growth_pct=48.5; success_rate=97.22
- failures: failure_code=ZA; count=65; rate_pct=0.53; trailing_rate_pct=0.4; owner=Customer; z=2.13
- categories: mcc_category=Mobility; attempts=859; success_rate=97.67; own_median=96.81; z=2.22
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=CMP-0065; kind=merchant_campaign; severity=Sev-3; window=2026-03-10 to 2026-03-15; success_impact_pp=-0.19; volume_impact_pct=76.56
- categories: mcc_category=Services; attempts=117; own_median=99; z=2.21
- products: product_name=Credit on UPI; attempts=95; own_median=152; z=-2.4

Refs: enterprise_data/warehouse/transactions, RPT-D68-DAILY, enterprise_data/warehouse/reference/incidents.parquet
