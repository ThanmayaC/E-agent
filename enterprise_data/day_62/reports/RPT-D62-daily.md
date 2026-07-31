---
id: RPT-D62-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 07 Mar 2026)

**Report ID:** RPT-D62-DAILY · **Day 62 of 206** · **Derived from:** 13,993 transaction rows queried live from the warehouse

## Summary

The rail took **13,993 payment attempts** on Saturday 07 March 2026 (Weekend) and settled **₹1.67 Cr** across 13,423 successful payments. Volume was +5.2% on yesterday and +2.7% on the same weekday last week. Success closed at **95.93%**, above the trailing 28-day median of 95.56%.

Category Bills carried 1,436 attempts, 116% up its trailing median and 15.6% of the day's volume. Product UPI Circle is compounding — attempts up 71% across the trailing window to 250 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,993 | +5.2% | +2.7% | 14,462 |
| Successful payments | 13,423 | +5.0% | +3.1% | 13,876 |
| Success rate | 95.93% | −0.20pp | +0.42pp | 95.95% |
| Settled value | ₹1.67 Cr | −0.3% | +8.4% | ₹1.66 Cr |
| Average ticket | ₹1,246 | −5.1% | +5.2% | ₹1,198 |
| Technical declines | 0.379% | −0.03pp | −0.10pp | 0.376% |
| Business declines | 3.109% | +0.09pp | −0.40pp | 3.163% |
| Risk declines | 0.136% | +0.05pp | +0.05pp | 0.116% |
| Timeout declines | 0.379% | +0.16pp | +0.07pp | 0.301% |
| Retry share | 1.10% | +0.14pp | −0.26pp | 1.15% |
| Latency p95 | 1,248 ms | −0.3% | +3.7% | 1,220 ms |
| Active customers | 11,437 | +4.5% | +2.8% | 11,705 |
| Active merchants | 1,371 | −0.6% | +0.1% | 1,362 |

## What moved

- Category Bills carried 1,436 attempts, 116% up its trailing median and 15.6% of the day's volume.
- Product UPI Circle is compounding — attempts up 71% across the trailing window to 250 today, with success holding, so the growth is healthy and worth funding.
- Attempt volume ran 3.2 standard deviations up its trailing 28-day median at 13,993, 2.7% up on the same weekday last week.
- App PhonePe carried 6,524 attempts, 32% up its trailing median and 46.6% of the day's volume.
- Product UPI Person to Person is compounding — attempts up 50% across the trailing window to 4,779 today, with success holding, so the growth is healthy and worth funding.
- App Google Pay carried 4,657 attempts, 33% up its trailing median and 33.3% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,779 | 34.2% | 95.02% | ₹53.55 L | +21.4% |
| UPI Person to Merchant | 4,053 | 29.0% | 96.20% | ₹39.86 L | +29.1% |
| UPI QR Payments | 2,790 | 19.9% | 96.56% | ₹11.98 L | +53.7% |
| UPI Lite | 1,103 | 7.9% | 99.18% | ₹1.03 L | +45.2% |
| UPI AutoPay | 312 | 2.2% | 90.71% | ₹4.58 L | +4.0% |
| UPI Circle | 250 | 1.8% | 99.20% | ₹2.37 L | +121.2% |
| RuPay Credit on UPI | 199 | 1.4% | 94.47% | ₹14.28 L | −5.7% |
| Credit on UPI | 149 | 1.1% | 94.63% | ₹16.30 L | +2.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,466 | 95.39% | 95.48% | ₹50.97 L | normal |
| HDFC Bank | 1,518 | 95.85% | 96.16% | ₹16.90 L | normal |
| Bank of Baroda | 1,086 | 96.04% | 95.40% | ₹12.34 L | normal |
| Union Bank of India | 1,019 | 95.78% | 95.26% | ₹15.17 L | normal |
| ICICI Bank | 849 | 96.35% | 95.93% | ₹10.83 L | normal |
| Axis Bank | 821 | 97.20% | 95.79% | ₹12.13 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,524 | 96.15% | 95.66% | ₹76.97 L | normal |
| Google Pay | 4,657 | 95.98% | 95.61% | ₹58.79 L | normal |
| Paytm | 1,145 | 95.20% | 95.36% | ₹10.05 L | normal |
| Navi | 540 | 94.81% | 95.45% | ₹5.90 L | normal |
| SuperMoney | 281 | 96.09% | 96.01% | ₹3.28 L | normal |
| BHIM | 141 | 96.45% | 95.09% | ₹2.48 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,501 | 96.86% | ₹36.09 L |
| Food & Beverage | 2,148 | 96.42% | ₹8.67 L |
| Bills | 1,436 | 96.31% | ₹16.69 L |
| Mobility | 1,070 | 97.01% | ₹6.06 L |
| Healthcare | 402 | 96.27% | ₹3.55 L |
| Digital | 301 | 96.68% | ₹2.23 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,100 | 29.3% | 95.83% | ₹57.98 L |
| North | 3,599 | 25.7% | 96.03% | ₹39.90 L |
| West | 3,366 | 24.1% | 95.90% | ₹39.87 L |
| East | 1,699 | 12.1% | 96.65% | ₹19.38 L |
| Central | 1,229 | 8.8% | 95.04% | ₹10.11 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 83 | 92.77% | ₹1.86 L |
| Girnar Connect | Key Account | Bills | 267 | 96.25% | ₹1.29 L |
| Rapid Bazaar | Key Account | Retail | 380 | 96.32% | ₹1.26 L |
| Hampi Styles | Key Account | Retail | 36 | 97.22% | ₹1.25 L |
| Vasant Wardrobe | Key Account | Retail | 49 | 95.92% | ₹1.10 L |
| Vega Electronics | Large | Retail | 21 | 85.71% | ₹1.04 L |
| Dhruva Supermart | Large | Retail | 67 | 95.52% | ₹97,232 |
| Urban Boutique | Key Account | Retail | 104 | 98.08% | ₹84,817 |

## Failure analysis

Of 560 declined attempts, 435 were business declines (3.109% of attempts — balances, PINs and limits), 53 technical (0.379%), 53 timeouts (0.379%) and 19 risk declines (0.136%).

154 attempts were re-presentations of an earlier failure (1.10% of the day); 62.3% of them succeeded.

- Decline code YA (PSP not available) fired 14 times — 0.100% of attempts against a trailing 0.048%. Owner: PSP.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 175 | 1.251% | 1.468% |
| ZM | Invalid UPI PIN | business | Customer | 152 | 1.086% | 1.143% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.400% | 0.416% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.222% | 0.248% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.186% | 0.159% |
| U30 | Debit failed at remitter bank | technical | Issuer | 22 | 0.157% | 0.153% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.114% | 0.095% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.114% | 0.103% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 80 | 68 |
| Auto-reversals | 13 | 20 |
| Disputes / chargebacks | 11 | 8 |
| Value returned | ₹48,164 | ₹91,753 |

## Customer behaviour

11,437 distinct customers transacted (+27.8% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,567 | 4,088 | 1.15 | 95.79% | ₹1,174 |
| power | 2,353 | 3,307 | 1.41 | 95.83% | ₹1,709 |
| merchant_heavy | 2,552 | 3,104 | 1.22 | 96.49% | ₹1,039 |
| small_ticket | 1,774 | 2,234 | 1.26 | 95.79% | ₹467 |
| occasional | 939 | 991 | 1.06 | 95.36% | ₹1,822 |
| new | 221 | 236 | 1.07 | 96.19% | ₹754 |
| dormant_returning | 31 | 33 | 1.06 | 93.94% | ₹717 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ADOPT-0075** (Sev-3) — Upi Credit Line onboarding push, scoped to UPI_CREDIT_LINE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **CMP-0058** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code YA (PSP not available) fired 14 times — 0.100% of attempts against a trailing 0.048%. Owner: PSP.

### Opportunities

- Product UPI Circle is compounding — attempts up 71% across the trailing window to 250 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Person to Person is compounding — attempts up 50% across the trailing window to 4,779 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

07 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.93% success against a 95.56% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,993, successes=13,423, failed=560, pending=10, settled_value_inr=16,724,719.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,436; own_median=665.5; z=9.2
- products: product_name=UPI Circle; attempts=250; window_growth_pct=70.9; success_rate=99.2
- headline: attempts=13,993; trailing_median=10,531.5; z=3.17
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- psps: payer_psp=PhonePe; attempts=6,524; own_median=4,951; z=2.91
- products: product_name=UPI Person to Person; attempts=4,779; window_growth_pct=50; success_rate=95.02
- psps: payer_psp=Google Pay; attempts=4,657; own_median=3,502; z=3.23
- geography: region=North; attempts=3,599; own_median=2,676; z=3.08
- geography: region=South; attempts=4,100; own_median=3,126.5; z=2.53
- categories: mcc_category=Mobility; attempts=1,070; own_median=719; z=4.01

Refs: enterprise_data/warehouse/transactions, RPT-D61-DAILY, enterprise_data/warehouse/reference/incidents.parquet
