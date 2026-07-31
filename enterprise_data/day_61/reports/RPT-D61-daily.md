---
id: RPT-D61-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-06T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 06 Mar 2026)

**Report ID:** RPT-D61-DAILY · **Day 61 of 206** · **Derived from:** 13,303 transaction rows queried live from the warehouse

## Summary

The rail took **13,303 payment attempts** on Friday 06 March 2026 (Working day) and settled **₹1.68 Cr** across 12,788 successful payments. Volume was +1.3% on yesterday and +5.3% on the same weekday last week. Success closed at **96.13%**, above the trailing 28-day median of 95.56%.

Category Bills carried 1,253 attempts, 88% up its trailing median and 15.1% of the day's volume. Product UPI Circle is compounding — attempts up 60% across the trailing window to 169 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,303 | +1.3% | +5.3% | 14,540 |
| Successful payments | 12,788 | +1.6% | +5.9% | 13,952 |
| Success rate | 96.13% | +0.26pp | +0.57pp | 95.95% |
| Settled value | ₹1.68 Cr | +2.9% | +15.2% | ₹1.65 Cr |
| Average ticket | ₹1,312 | +1.4% | +8.8% | ₹1,190 |
| Technical declines | 0.413% | +0.06pp | −0.08pp | 0.376% |
| Business declines | 3.022% | −0.28pp | −0.33pp | 3.172% |
| Risk declines | 0.090% | −0.04pp | −0.02pp | 0.112% |
| Timeout declines | 0.218% | +0.02pp | −0.16pp | 0.288% |
| Retry share | 0.96% | −0.24pp | −0.39pp | 1.16% |
| Latency p95 | 1,252 ms | +4.7% | +0.3% | 1,215 ms |
| Active customers | 10,941 | +1.6% | +4.7% | 11,750 |
| Active merchants | 1,379 | +4.6% | +5.0% | 1,360 |

## What moved

- Category Bills carried 1,253 attempts, 88% up its trailing median and 15.1% of the day's volume.
- Product UPI Circle is compounding — attempts up 60% across the trailing window to 169 today, with success holding, so the growth is healthy and worth funding.
- Attempt volume ran 2.5 standard deviations up its trailing 28-day median at 13,303, 5.3% up on the same weekday last week.
- App PhonePe carried 6,378 attempts, 29% up its trailing median and 47.9% of the day's volume.
- Product UPI Person to Person is compounding — attempts up 47% across the trailing window to 4,997 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Merchant ran at 96.52% success on 3,502 attempts (26.3% of the day), 0.59pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,997 | 37.6% | 95.50% | ₹57.77 L | +27.0% |
| UPI Person to Merchant | 3,502 | 26.3% | 96.52% | ₹36.74 L | +11.5% |
| UPI QR Payments | 2,597 | 19.5% | 96.88% | ₹12.25 L | +43.0% |
| UPI Lite | 924 | 6.9% | 98.92% | ₹89,968 | +21.7% |
| UPI AutoPay | 295 | 2.2% | 91.53% | ₹5.79 L | −1.7% |
| RuPay Credit on UPI | 268 | 2.0% | 94.78% | ₹14.90 L | +27.0% |
| Credit on UPI | 179 | 1.3% | 94.97% | ₹16.42 L | +22.6% |
| UPI Circle | 169 | 1.3% | 97.63% | ₹1.92 L | +49.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,203 | 95.96% | 95.48% | ₹58.50 L | normal |
| HDFC Bank | 1,488 | 96.10% | 96.22% | ₹18.38 L | normal |
| Bank of Baroda | 970 | 96.60% | 95.40% | ₹11.35 L | ⚠ outlier |
| Union Bank of India | 936 | 96.05% | 95.26% | ₹11.10 L | normal |
| ICICI Bank | 819 | 95.60% | 95.97% | ₹7.87 L | normal |
| Axis Bank | 800 | 96.12% | 95.75% | ₹10.84 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,378 | 96.17% | 95.66% | ₹77.30 L | normal |
| Google Pay | 4,351 | 95.77% | 95.59% | ₹52.21 L | normal |
| Paytm | 1,059 | 96.13% | 95.36% | ₹14.77 L | normal |
| Navi | 516 | 97.67% | 95.45% | ₹11.87 L | normal |
| SuperMoney | 253 | 97.63% | 96.01% | ₹2.81 L | normal |
| BHIM | 120 | 95.83% | 94.88% | ₹1.22 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,163 | 96.43% | ₹36.56 L |
| Food & Beverage | 1,904 | 96.85% | ₹9.35 L |
| Bills | 1,253 | 96.65% | ₹15.62 L |
| Mobility | 972 | 96.81% | ₹5.51 L |
| Healthcare | 387 | 98.71% | ₹5.51 L |
| Digital | 284 | 95.07% | ₹1.46 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,931 | 29.5% | 96.36% | ₹50.57 L |
| North | 3,342 | 25.1% | 96.29% | ₹41.42 L |
| West | 3,281 | 24.7% | 95.79% | ₹44.30 L |
| East | 1,578 | 11.9% | 95.56% | ₹20.65 L |
| Central | 1,171 | 8.8% | 96.58% | ₹10.87 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 27 | 92.59% | ₹3.52 L |
| Ujjwal Water Board | Key Account | Bills | 73 | 95.89% | ₹2.64 L |
| Rapid Bazaar | Key Account | Retail | 369 | 97.02% | ₹1.67 L |
| Vasant Wardrobe | Key Account | Retail | 87 | 90.80% | ₹1.11 L |
| Girnar Connect | Key Account | Bills | 218 | 97.25% | ₹89,344 |
| Yamuna Restaurant | Key Account | Food & Beverage | 91 | 96.70% | ₹87,448 |
| Hampi Stores 2298 | Key Account | Retail | 100 | 95.00% | ₹85,248 |
| Urban Boutique | Key Account | Retail | 100 | 98.00% | ₹68,589 |

## Failure analysis

Of 498 declined attempts, 402 were business declines (3.022% of attempts — balances, PINs and limits), 55 technical (0.413%), 29 timeouts (0.218%) and 12 risk declines (0.090%).

128 attempts were re-presentations of an earlier failure (0.96% of the day); 58.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.165% | 1.468% |
| ZM | Invalid UPI PIN | business | Customer | 146 | 1.097% | 1.143% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.406% | 0.423% |
| XH | Account does not exist / frozen | business | Issuer | 29 | 0.218% | 0.248% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.165% | 0.152% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.128% | 0.159% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.105% | 0.115% |
| U69 | Beneficiary bank offline | technical | Issuer | 13 | 0.098% | 0.076% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 86 | 68 |
| Auto-reversals | 20 | 18 |
| Disputes / chargebacks | 7 | 8 |
| Value returned | ₹88,273 | ₹94,495 |

## Customer behaviour

10,941 distinct customers transacted (+22.2% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,428 | 3,906 | 1.14 | 95.83% | ₹1,307 |
| power | 2,234 | 3,080 | 1.38 | 96.23% | ₹1,871 |
| merchant_heavy | 2,458 | 3,003 | 1.22 | 95.87% | ₹1,037 |
| small_ticket | 1,649 | 2,084 | 1.26 | 96.26% | ₹624 |
| occasional | 910 | 953 | 1.05 | 97.48% | ₹1,307 |
| new | 227 | 242 | 1.07 | 96.69% | ₹891 |
| dormant_returning | 35 | 35 | 1.00 | 94.29% | ₹1,102 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0009** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 17:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **REG-0070** (Sev-3) — UPI Circle full-delegation rollout to all PSPs, scoped to UPI_CIRCLE. Full-delegation Circle became available across every major PSP, converting the pilot cohort into mainstream volume.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 60% across the trailing window to 169 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Person is compounding — attempts up 47% across the trailing window to 4,997 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

06 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 96.13% success against a 95.56% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-06` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,303, successes=12,788, failed=498, pending=17, settled_value_inr=16,781,395.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,253; own_median=665.5; z=7.01
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI Circle; attempts=169; window_growth_pct=59.8; success_rate=97.63
- headline: attempts=13,303; trailing_median=10,531.5; z=2.54
- psps: payer_psp=PhonePe; attempts=6,378; own_median=4,951; z=2.64
- products: product_name=UPI Person to Person; attempts=4,997; window_growth_pct=47.3; success_rate=95.5
- products: product_name=UPI Person to Merchant; attempts=3,502; success_rate=96.52; own_median=95.92; z=2.13
- psps: payer_psp=Google Pay; attempts=4,351; own_median=3,502; z=2.37
- geography: region=West; attempts=3,281; own_median=2,585; z=2.39
- geography: region=North; attempts=3,342; own_median=2,676; z=2.22

Refs: enterprise_data/warehouse/transactions, RPT-D60-DAILY, enterprise_data/warehouse/reference/incidents.parquet
