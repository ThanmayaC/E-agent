---
id: RPT-D60-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-05T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 05 Mar 2026)

**Report ID:** RPT-D60-DAILY · **Day 60 of 206** · **Derived from:** 13,132 transaction rows queried live from the warehouse

## Summary

The rail took **13,132 payment attempts** on Thursday 05 March 2026 (Working day) and settled **₹1.63 Cr** across 12,590 successful payments. Volume was −17.8% on yesterday and +30.9% on the same weekday last week. Success closed at **95.87%**, above the trailing 28-day median of 95.54%.

Category Bills carried 1,179 attempts, 77% up its trailing median and 15.0% of the day's volume. Attempt volume ran 3.2 standard deviations up its trailing 28-day median at 13,132, 30.9% up on the same weekday last week.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,132 | −17.8% | +30.9% | 14,788 |
| Successful payments | 12,590 | −18.1% | +32.5% | 14,184 |
| Success rate | 95.87% | −0.28pp | +1.14pp | 95.91% |
| Settled value | ₹1.63 Cr | −6.0% | +36.4% | ₹1.65 Cr |
| Average ticket | ₹1,295 | +14.8% | +3.0% | ₹1,166 |
| Technical declines | 0.358% | −0.04pp | −0.14pp | 0.369% |
| Business declines | 3.305% | +0.36pp | −0.96pp | 3.202% |
| Risk declines | 0.129% | −0.00pp | +0.11pp | 0.117% |
| Timeout declines | 0.198% | −0.11pp | −0.18pp | 0.302% |
| Retry share | 1.20% | +0.02pp | −0.53pp | 1.20% |
| Latency p95 | 1,195 ms | −1.1% | −9.8% | 1,208 ms |
| Active customers | 10,769 | −15.5% | +24.6% | 11,911 |
| Active merchants | 1,318 | −2.8% | +4.6% | 1,356 |

## What moved

- Category Bills carried 1,179 attempts, 77% up its trailing median and 15.0% of the day's volume.
- Attempt volume ran 3.2 standard deviations up its trailing 28-day median at 13,132, 30.9% up on the same weekday last week.
- Region West carried 3,443 attempts, 34% up its trailing median and 26.2% of the day's volume.
- Product UPI Circle is compounding — attempts up 48% across the trailing window to 163 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- App PhonePe carried 6,187 attempts, 25% up its trailing median and 47.1% of the day's volume.
- App Google Pay carried 4,331 attempts, 25% up its trailing median and 33.0% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,288 | 40.3% | 95.37% | ₹57.31 L | +34.9% |
| UPI Person to Merchant | 3,575 | 27.2% | 96.00% | ₹37.94 L | +14.2% |
| UPI QR Payments | 2,240 | 17.1% | 96.70% | ₹9.81 L | +25.0% |
| UPI Lite | 930 | 7.1% | 98.49% | ₹89,155 | +26.8% |
| UPI AutoPay | 287 | 2.2% | 93.03% | ₹5.31 L | −4.3% |
| RuPay Credit on UPI | 228 | 1.7% | 96.05% | ₹19.95 L | +8.3% |
| UPI Circle | 163 | 1.2% | 95.09% | ₹1.31 L | +48.2% |
| Credit on UPI | 116 | 0.9% | 92.24% | ₹9.81 L | −20.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,211 | 96.27% | 95.48% | ₹57.81 L | normal |
| HDFC Bank | 1,463 | 95.22% | 96.22% | ₹16.90 L | normal |
| Bank of Baroda | 997 | 95.19% | 95.40% | ₹11.13 L | normal |
| Union Bank of India | 869 | 95.86% | 95.26% | ₹11.03 L | normal |
| Axis Bank | 833 | 96.76% | 95.75% | ₹11.28 L | normal |
| Punjab National Bank | 781 | 95.65% | 94.87% | ₹9.63 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,187 | 96.02% | 95.61% | ₹74.76 L | normal |
| Google Pay | 4,331 | 95.80% | 95.59% | ₹58.79 L | normal |
| Paytm | 1,116 | 94.18% | 95.41% | ₹12.33 L | normal |
| Navi | 482 | 97.30% | 95.33% | ₹4.53 L | normal |
| SuperMoney | 237 | 96.62% | 96.01% | ₹3.73 L | normal |
| BHIM | 127 | 97.64% | 94.61% | ₹1.43 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,084 | 96.24% | ₹32.27 L |
| Food & Beverage | 1,899 | 96.89% | ₹9.03 L |
| Bills | 1,179 | 96.52% | ₹16.24 L |
| Mobility | 787 | 96.82% | ₹5.89 L |
| Healthcare | 334 | 95.21% | ₹2.54 L |
| Digital | 259 | 92.66% | ₹1.16 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,029 | 30.7% | 95.76% | ₹49.82 L |
| West | 3,443 | 26.2% | 95.50% | ₹46.36 L |
| North | 3,007 | 22.9% | 96.57% | ₹34.93 L |
| East | 1,495 | 11.4% | 95.45% | ₹20.09 L |
| Central | 1,158 | 8.8% | 96.11% | ₹11.82 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 72 | 94.44% | ₹1.88 L |
| Ujjwal Water Board | Key Account | Bills | 72 | 97.22% | ₹1.64 L |
| Rapid Bazaar | Key Account | Retail | 365 | 96.71% | ₹1.45 L |
| Vega Electronics | Large | Retail | 17 | 94.12% | ₹1.43 L |
| Hampi Stores 2298 | Key Account | Retail | 95 | 96.84% | ₹1.00 L |
| Tejas Restaurant | Large | Food & Beverage | 32 | 100.00% | ₹93,425 |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 92.65% | ₹78,767 |
| Girnar Connect | Key Account | Bills | 206 | 98.06% | ₹76,655 |

## Failure analysis

Of 524 declined attempts, 434 were business declines (3.305% of attempts — balances, PINs and limits), 47 technical (0.358%), 26 timeouts (0.198%) and 17 risk declines (0.129%).

158 attempts were re-presentations of an earlier failure (1.20% of the day); 66.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 186 | 1.416% | 1.479% |
| ZM | Invalid UPI PIN | business | Customer | 138 | 1.051% | 1.176% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.419% | 0.426% |
| XH | Account does not exist / frozen | business | Issuer | 30 | 0.228% | 0.248% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.137% | 0.153% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.129% | 0.159% |
| ZX | Mandate not found or revoked | business | PSP | 15 | 0.114% | 0.089% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 14 | 0.107% | 0.097% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 82 | 68 |
| Auto-reversals | 21 | 18 |
| Disputes / chargebacks | 12 | 7 |
| Value returned | ₹1.32 L | ₹94,495 |

## Customer behaviour

10,769 distinct customers transacted (+21.4% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,385 | 3,874 | 1.14 | 96.21% | ₹1,450 |
| merchant_heavy | 2,483 | 3,064 | 1.23 | 95.79% | ₹919 |
| power | 2,220 | 3,014 | 1.36 | 95.45% | ₹1,674 |
| small_ticket | 1,633 | 2,051 | 1.26 | 96.34% | ₹558 |
| occasional | 835 | 897 | 1.07 | 94.98% | ₹1,601 |
| new | 190 | 206 | 1.08 | 96.12% | ₹899 |
| dormant_returning | 23 | 26 | 1.13 | 96.15% | ₹2,117 |

## Operational events

- **INC-PSP-0026** (Sev-2) — YONO SBI app release regression, scoped to YONO SBI between 18:00 and 23:00. A YONO SBI client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0009** (Sev-3) — State Bank of India issuer decline spike, scoped to State Bank of India between 17:00 and 23:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **REG-0070** (Sev-3) — UPI Circle full-delegation rollout to all PSPs, scoped to UPI_CIRCLE. Full-delegation Circle became available across every major PSP, converting the pilot cohort into mainstream volume.

## Risks and opportunities

### Risks

- Product UPI Circle is compounding — attempts up 48% across the trailing window to 163 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Person to Person is compounding — attempts up 41% across the trailing window to 5,288 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

05 March was an incident day: INC-PSP-0026, INC-FRAUD-0046 were live and the rail closed at 95.87% success against a 95.54% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-05` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,132, successes=12,590, failed=524, pending=18, settled_value_inr=16,300,821.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,179; own_median=665.5; z=6.13
- headline: attempts=13,132; trailing_median=10,454; z=3.22
- incidents: event_id=INC-PSP-0026; kind=psp_degradation; severity=Sev-2; window=2026-03-02 to 2026-03-05; success_impact_pp=-9.44; volume_impact_pct=-14.77
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- geography: region=West; attempts=3,443; own_median=2,572; z=3.72
- products: product_name=UPI Circle; attempts=163; window_growth_pct=47.8; success_rate=95.09
- psps: payer_psp=PhonePe; attempts=6,187; own_median=4,951; z=2.63
- psps: payer_psp=Google Pay; attempts=4,331; own_median=3,457.5; z=2.99
- products: product_name=UPI Person to Person; attempts=5,288; own_median=3,920.5; z=2.64
- products: product_name=UPI Person to Person; attempts=5,288; window_growth_pct=40.8; success_rate=95.37

Refs: enterprise_data/warehouse/transactions, RPT-D59-DAILY, enterprise_data/warehouse/reference/incidents.parquet
