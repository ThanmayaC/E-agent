---
id: RPT-D65-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 10 Mar 2026)

**Report ID:** RPT-D65-DAILY · **Day 65 of 206** · **Derived from:** 10,562 transaction rows queried live from the warehouse

## Summary

The rail took **10,562 payment attempts** on Tuesday 10 March 2026 (Working day) and settled **₹1.24 Cr** across 10,168 successful payments. Volume was −10.6% on yesterday and −28.6% on the same weekday last week. Success closed at **96.27%**, above the trailing 28-day median of 95.59%.

Product UPI Circle is compounding — attempts up 87% across the trailing window to 156 today, with success holding, so the growth is healthy and worth funding. Product UPI Person to Merchant ran at 96.73% success on 3,215 attempts (30.4% of the day), 0.81pp up its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,562 | −10.6% | −28.6% | 13,535 |
| Successful payments | 10,168 | −10.3% | −28.2% | 12,985 |
| Success rate | 96.27% | +0.37pp | +0.49pp | 95.94% |
| Settled value | ₹1.24 Cr | −11.9% | −23.5% | ₹1.55 Cr |
| Average ticket | ₹1,222 | −1.8% | +6.5% | ₹1,196 |
| Technical declines | 0.502% | −0.01pp | +0.13pp | 0.421% |
| Business declines | 2.850% | −0.17pp | −0.37pp | 3.125% |
| Risk declines | 0.104% | −0.05pp | −0.05pp | 0.114% |
| Timeout declines | 0.189% | −0.12pp | −0.18pp | 0.300% |
| Retry share | 1.15% | +0.07pp | −0.01pp | 1.18% |
| Latency p95 | 1,267 ms | −2.9% | +3.9% | 1,232 ms |
| Active customers | 8,995 | −9.3% | −24.7% | 11,068 |
| Active merchants | 1,309 | +2.8% | −5.1% | 1,340 |

## What moved

- Product UPI Circle is compounding — attempts up 87% across the trailing window to 156 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Merchant ran at 96.73% success on 3,215 attempts (30.4% of the day), 0.81pp up its own 28-day median.
- App Google Pay ran at 96.86% success on 3,506 attempts (33.2% of the day), 1.24pp up its own 28-day median.
- Success rate closed at 96.27%, 0.68pp up the trailing median — a 1.7-sigma move.
- Product UPI QR Payments is compounding — attempts up 41% across the trailing window to 2,130 today, with success holding, so the growth is healthy and worth funding.
- Category Food & Beverage ran at 97.41% success on 1,851 attempts (25.1% of the day), 0.84pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 3,215 | 30.4% | 96.73% | ₹33.99 L | +1.4% |
| UPI Person to Person | 3,197 | 30.3% | 95.28% | ₹33.22 L | −20.8% |
| UPI QR Payments | 2,130 | 20.2% | 97.18% | ₹9.32 L | +15.1% |
| UPI Lite | 784 | 7.4% | 98.98% | ₹72,881 | +4.7% |
| UPI AutoPay | 317 | 3.0% | 91.80% | ₹6.27 L | +5.3% |
| RuPay Credit on UPI | 236 | 2.2% | 95.34% | ₹13.28 L | +11.3% |
| Credit on UPI | 170 | 1.6% | 96.47% | ₹12.90 L | +15.6% |
| UPI Circle | 156 | 1.5% | 98.72% | ₹1.36 L | +36.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,401 | 95.82% | 95.48% | ₹41.04 L | normal |
| HDFC Bank | 1,114 | 96.23% | 96.17% | ₹10.57 L | normal |
| Bank of Baroda | 809 | 96.29% | 95.41% | ₹15.48 L | normal |
| Union Bank of India | 740 | 96.49% | 95.26% | ₹9.49 L | normal |
| ICICI Bank | 665 | 97.14% | 95.85% | ₹6.50 L | normal |
| Punjab National Bank | 618 | 95.15% | 94.96% | ₹5.86 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,971 | 96.00% | 95.61% | ₹59.48 L | normal |
| Google Pay | 3,506 | 96.86% | 95.63% | ₹38.81 L | ⚠ outlier |
| Paytm | 809 | 96.17% | 95.36% | ₹11.64 L | normal |
| Navi | 400 | 96.00% | 95.47% | ₹3.50 L | normal |
| SuperMoney | 218 | 94.50% | 95.88% | ₹3.38 L | normal |
| BHIM | 110 | 95.45% | 94.88% | ₹78,694 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,115 | 96.66% | ₹33.59 L |
| Food & Beverage | 1,851 | 97.41% | ₹8.03 L |
| Mobility | 781 | 97.95% | ₹4.77 L |
| Bills | 659 | 96.81% | ₹8.40 L |
| Healthcare | 443 | 97.97% | ₹6.71 L |
| Digital | 195 | 89.74% | ₹1.11 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,122 | 29.6% | 96.44% | ₹32.02 L |
| North | 2,703 | 25.6% | 96.00% | ₹34.49 L |
| West | 2,521 | 23.9% | 96.15% | ₹31.97 L |
| East | 1,275 | 12.1% | 96.31% | ₹17.65 L |
| Central | 941 | 8.9% | 96.71% | ₹8.09 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 100.00% | ₹4.30 L |
| Ujjwal Water Board | Key Account | Bills | 34 | 85.29% | ₹1.81 L |
| Rapid Bazaar | Key Account | Retail | 331 | 97.58% | ₹1.61 L |
| Vasant Wardrobe | Key Account | Retail | 62 | 91.94% | ₹1.49 L |
| Hampi Styles | Key Account | Retail | 32 | 93.75% | ₹92,947 |
| Yamuna Restaurant | Key Account | Food & Beverage | 78 | 89.74% | ₹81,373 |
| Urban Boutique | Key Account | Retail | 92 | 95.65% | ₹70,714 |
| Hampi Stores 2298 | Key Account | Retail | 107 | 99.07% | ₹65,266 |

## Failure analysis

Of 385 declined attempts, 301 were business declines (2.850% of attempts — balances, PINs and limits), 53 technical (0.502%), 20 timeouts (0.189%) and 11 risk declines (0.104%).

121 attempts were re-presentations of an earlier failure (1.15% of the day); 65.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 129 | 1.221% | 1.452% |
| ZM | Invalid UPI PIN | business | Customer | 95 | 0.899% | 1.109% |
| ZA | Transaction declined by customer | business | Customer | 33 | 0.312% | 0.410% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.227% | 0.248% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.189% | 0.165% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.123% | 0.119% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 13 | 0.123% | 0.167% |
| U69 | Beneficiary bank offline | technical | Issuer | 13 | 0.123% | 0.080% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 82 | 68 |
| Auto-reversals | 23 | 20 |
| Disputes / chargebacks | 10 | 9 |
| Value returned | ₹3.54 L | ₹89,740 |

## Customer behaviour

8,995 distinct customers transacted (−2.6% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,738 | 3,079 | 1.12 | 95.84% | ₹1,112 |
| power | 1,875 | 2,446 | 1.30 | 96.57% | ₹1,747 |
| merchant_heavy | 2,083 | 2,403 | 1.15 | 96.25% | ₹959 |
| small_ticket | 1,387 | 1,685 | 1.21 | 96.74% | ₹630 |
| occasional | 721 | 746 | 1.03 | 95.98% | ₹1,615 |
| new | 169 | 181 | 1.07 | 96.13% | ₹676 |
| dormant_returning | 22 | 22 | 1.00 | 100.00% | ₹1,371 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CMP-0058** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0065** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 87% across the trailing window to 156 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments is compounding — attempts up 41% across the trailing window to 2,130 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

10 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 96.27% success against a 95.59% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,562, successes=10,168, failed=385, pending=9, settled_value_inr=12,420,695.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=156; window_growth_pct=86.6; success_rate=98.72
- products: product_name=UPI Person to Merchant; attempts=3,215; success_rate=96.73; own_median=95.92; z=3.32
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- psps: payer_psp=Google Pay; attempts=3,506; success_rate=96.86; own_median=95.63; z=2.62
- headline: success_rate=96.27; trailing_median=95.59; z=1.68
- products: product_name=UPI QR Payments; attempts=2,130; window_growth_pct=40.8; success_rate=97.18
- categories: mcc_category=Food & Beverage; attempts=1,851; success_rate=97.41; own_median=96.57; z=2.08
- categories: mcc_category=Mobility; attempts=781; success_rate=97.95; own_median=96.8; z=3.13
- banks: payer_bank=IDFC First Bank; attempts=308; success_rate=98.38; own_median=95.62; z=3.83
- categories: mcc_category=Healthcare; attempts=443; own_median=350; z=2.32

Refs: enterprise_data/warehouse/transactions, RPT-D64-DAILY, enterprise_data/warehouse/reference/incidents.parquet
