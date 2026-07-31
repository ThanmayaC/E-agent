---
id: RPT-D80-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 25 Mar 2026)

**Report ID:** RPT-D80-DAILY · **Day 80 of 206** · **Derived from:** 9,967 transaction rows queried live from the warehouse

## Summary

The rail took **9,967 payment attempts** on Wednesday 25 March 2026 (Working day) and settled **₹1.19 Cr** across 9,490 successful payments. Volume was −1.9% on yesterday and −23.1% on the same weekday last week. Success closed at **95.21%**, below the trailing 28-day median of 95.79%.

Decline code Z9 (Insufficient funds) fired 187 times — 1.876% of attempts against a trailing 1.332%. Owner: Customer. Region North ran at 94.67% success on 2,533 attempts (25.4% of the day), 1.25pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 9,967 | −1.9% | −23.1% | 12,523 |
| Successful payments | 9,490 | −2.1% | −23.6% | 11,994 |
| Success rate | 95.21% | −0.20pp | −0.58pp | 95.74% |
| Settled value | ₹1.19 Cr | −2.6% | −20.4% | ₹1.41 Cr |
| Average ticket | ₹1,254 | −0.6% | +4.1% | ₹1,181 |
| Technical declines | 0.311% | −0.11pp | −0.18pp | 0.442% |
| Business declines | 3.953% | +0.31pp | +0.78pp | 3.274% |
| Risk declines | 0.120% | −0.06pp | −0.01pp | 0.124% |
| Timeout declines | 0.251% | +0.00pp | −0.05pp | 0.320% |
| Retry share | 1.24% | +0.06pp | +0.06pp | 1.26% |
| Latency p95 | 1,324 ms | +3.5% | +6.2% | 1,245 ms |
| Active customers | 8,587 | −1.5% | −19.7% | 10,372 |
| Active merchants | 1,274 | +0.4% | −3.2% | 1,320 |

## What moved

- Region North ran at 94.67% success on 2,533 attempts (25.4% of the day), 1.25pp down its own 28-day median.
- Success rate closed at 95.21%, 0.58pp down the trailing median — a 2.2-sigma move.
- Product UPI Circle is compounding — attempts up 51% across the trailing window to 170 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI AutoPay ran at 83.53% success on 340 attempts (3.4% of the day), 7.28pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 27% across the trailing window to 731 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,280 | 32.9% | 94.60% | ₹33.27 L | −26.5% |
| UPI Person to Merchant | 2,911 | 29.2% | 95.98% | ₹25.71 L | −16.6% |
| UPI QR Payments | 1,751 | 17.6% | 96.86% | ₹6.80 L | −19.0% |
| UPI Lite | 731 | 7.3% | 98.36% | ₹66,461 | −20.2% |
| UPI AutoPay | 340 | 3.4% | 83.53% | ₹5.61 L | +8.1% |
| RuPay Credit on UPI | 250 | 2.5% | 96.40% | ₹12.37 L | +12.4% |
| UPI Circle | 170 | 1.7% | 94.71% | ₹1.27 L | −6.1% |
| Credit on UPI | 170 | 1.7% | 94.12% | ₹8.85 L | +11.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,163 | 95.10% | 95.72% | ₹34.45 L | normal |
| HDFC Bank | 1,114 | 94.70% | 95.71% | ₹14.35 L | normal |
| Bank of Baroda | 753 | 96.55% | 95.58% | ₹8.76 L | normal |
| Union Bank of India | 675 | 95.26% | 95.43% | ₹8.67 L | normal |
| ICICI Bank | 604 | 95.20% | 95.86% | ₹5.80 L | normal |
| Punjab National Bank | 604 | 95.70% | 95.23% | ₹7.26 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,639 | 95.32% | 95.95% | ₹59.94 L | normal |
| Google Pay | 3,321 | 95.45% | 95.71% | ₹38.29 L | normal |
| Paytm | 840 | 96.07% | 95.65% | ₹9.73 L | normal |
| Navi | 356 | 92.98% | 95.75% | ₹4.29 L | ⚠ outlier |
| SuperMoney | 199 | 93.97% | 95.73% | ₹1.57 L | normal |
| BHIM | 117 | 96.58% | 95.53% | ₹89,872 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,790 | 96.45% | ₹30.98 L |
| Food & Beverage | 1,646 | 96.23% | ₹7.85 L |
| Mobility | 692 | 96.97% | ₹3.94 L |
| Bills | 667 | 94.00% | ₹7.61 L |
| Healthcare | 364 | 96.70% | ₹2.98 L |
| Digital | 186 | 88.71% | ₹81,830 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,898 | 29.1% | 95.38% | ₹35.94 L |
| North | 2,533 | 25.4% | 94.67% | ₹26.81 L |
| West | 2,482 | 24.9% | 95.00% | ₹33.24 L |
| East | 1,160 | 11.6% | 95.43% | ₹13.88 L |
| Central | 894 | 9.0% | 96.53% | ₹9.14 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 50 | 98.00% | ₹1.83 L |
| Rapid Bazaar | Key Account | Retail | 285 | 96.84% | ₹1.17 L |
| Hampi Styles | Key Account | Retail | 37 | 100.00% | ₹1.07 L |
| Vega Electronics | Large | Retail | 22 | 100.00% | ₹79,019 |
| Aravalli Pharmacy | Large | Healthcare | 60 | 96.67% | ₹74,078 |
| Ujjwal Water Board | Key Account | Bills | 23 | 91.30% | ₹63,351 |
| Konark Boutique | Large | Retail | 29 | 100.00% | ₹53,248 |
| Girnar Connect | Key Account | Bills | 103 | 97.09% | ₹53,163 |

## Failure analysis

Of 462 declined attempts, 394 were business declines (3.953% of attempts — balances, PINs and limits), 31 technical (0.311%), 25 timeouts (0.251%) and 12 risk declines (0.120%).

124 attempts were re-presentations of an earlier failure (1.24% of the day); 71.0% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 187 times — 1.876% of attempts against a trailing 1.332%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 187 | 1.876% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 115 | 1.154% | 1.082% |
| ZA | Transaction declined by customer | business | Customer | 42 | 0.421% | 0.391% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.221% | 0.228% |
| UX | Mandate execution outside permitted window | business | PSP | 14 | 0.140% | 0.089% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 13 | 0.130% | 0.162% |
| ZX | Mandate not found or revoked | business | PSP | 11 | 0.110% | 0.088% |
| U30 | Debit failed at remitter bank | technical | Issuer | 10 | 0.100% | 0.187% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 104 | 76 |
| Auto-reversals | 12 | 24 |
| Disputes / chargebacks | 12 | 10 |
| Value returned | ₹2.17 L | ₹1.16 L |

## Customer behaviour

8,587 distinct customers transacted (−15.0% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,555 | 2,826 | 1.11 | 95.26% | ₹1,261 |
| power | 1,864 | 2,408 | 1.29 | 95.18% | ₹1,609 |
| merchant_heavy | 1,986 | 2,295 | 1.16 | 94.99% | ₹959 |
| small_ticket | 1,302 | 1,518 | 1.17 | 95.19% | ₹578 |
| occasional | 711 | 741 | 1.04 | 95.55% | ₹1,559 |
| new | 146 | 156 | 1.07 | 96.15% | ₹1,411 |
| dormant_returning | 23 | 23 | 1.00 | 100.00% | ₹376 |

## Operational events

- **MAINT-0084** (Sev-3) — State Bank of India scheduled CBS maintenance, scoped to State Bank of India between 00:00 and 02:00. State Bank of India runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **CMP-0057** (Sev-3) — Grocery cashback campaign, scoped to 5411. A cashback campaign across Grocery merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 187 times — 1.876% of attempts against a trailing 1.332%. Owner: Customer.
- Region North ran at 94.67% success on 2,533 attempts (25.4% of the day), 1.25pp down its own 28-day median.
- Success rate closed at 95.21%, 0.58pp down the trailing median — a 2.2-sigma move.
- 104 refunds were raised, 3.1 sigma above the trailing median of 76.
- Product UPI Circle is compounding — attempts up 51% across the trailing window to 170 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

Reliability, not demand, is the story of 25 March: success came in 0.58pp below baseline at 95.21% on 9,967 attempts. The decline table below attributes it by code and owner; that attribution is where the next action sits.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=9,967, successes=9,490, failed=462, pending=15, settled_value_inr=11,900,205.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=187; rate_pct=1.88; trailing_rate_pct=1.33; owner=Customer; z=4.43
- geography: region=North; attempts=2,533; success_rate=94.67; own_median=95.92; z=-4.03
- headline: success_rate=95.21; trailing_median=95.79; z=-2.24
- adjustments: refunds=104; trailing_median=76; z=3.15
- products: product_name=UPI Circle; attempts=170; window_growth_pct=50.8; success_rate=94.71
- products: product_name=UPI AutoPay; attempts=340; success_rate=83.53; own_median=90.81; z=-4.52
- products: product_name=UPI Lite; attempts=731; window_growth_pct=26.9; success_rate=98.36
- incidents: event_id=MAINT-0084; kind=maintenance_window; severity=Sev-3; window=2026-01-24 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- psps: payer_psp=Navi; attempts=356; success_rate=92.98; own_median=95.75; z=-3.44
- categories: mcc_category=Financial Services; attempts=161; success_rate=76.4; own_median=87.76; z=-3.91

Refs: enterprise_data/warehouse/transactions, RPT-D79-DAILY, enterprise_data/warehouse/reference/incidents.parquet
