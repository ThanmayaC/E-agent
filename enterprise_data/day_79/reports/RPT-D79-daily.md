---
id: RPT-D79-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-24T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 24 Mar 2026)

**Report ID:** RPT-D79-DAILY · **Day 79 of 206** · **Derived from:** 10,157 transaction rows queried live from the warehouse

## Summary

The rail took **10,157 payment attempts** on Tuesday 24 March 2026 (Working day) and settled **₹1.22 Cr** across 9,691 successful payments. Volume was −6.5% on yesterday and −13.9% on the same weekday last week. Success closed at **95.41%**, below the trailing 28-day median of 95.79%.

Decline code Z9 (Insufficient funds) fired 176 times — 1.733% of attempts against a trailing 1.332%. Owner: Customer. Product UPI Circle is compounding — attempts up 69% across the trailing window to 170 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,157 | −6.5% | −13.9% | 12,630 |
| Successful payments | 9,691 | −6.8% | −14.4% | 12,098 |
| Success rate | 95.41% | −0.27pp | −0.56pp | 95.76% |
| Settled value | ₹1.22 Cr | −4.7% | −12.4% | ₹1.42 Cr |
| Average ticket | ₹1,261 | +2.3% | +2.4% | ₹1,178 |
| Technical declines | 0.423% | +0.08pp | −0.06pp | 0.447% |
| Business declines | 3.643% | +0.07pp | +0.52pp | 3.246% |
| Risk declines | 0.177% | +0.05pp | +0.08pp | 0.124% |
| Timeout declines | 0.246% | +0.03pp | +0.00pp | 0.323% |
| Retry share | 1.18% | −0.21pp | +0.13pp | 1.26% |
| Latency p95 | 1,279 ms | +3.6% | +4.3% | 1,242 ms |
| Active customers | 8,722 | −5.9% | −11.8% | 10,446 |
| Active merchants | 1,269 | −2.6% | −1.2% | 1,322 |

## What moved

- Product UPI Circle is compounding — attempts up 69% across the trailing window to 170 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 38% across the trailing window to 761 today, with success holding, so the growth is healthy and worth funding.
- Product UPI AutoPay ran at 82.19% success on 320 attempts (3.2% of the day), 8.63pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,545 | 34.9% | 95.32% | ₹36.00 L | −20.6% |
| UPI Person to Merchant | 2,816 | 27.7% | 95.70% | ₹24.10 L | −19.3% |
| UPI QR Payments | 1,699 | 16.7% | 96.00% | ₹6.78 L | −21.4% |
| UPI Lite | 761 | 7.5% | 99.08% | ₹66,796 | −16.9% |
| UPI AutoPay | 320 | 3.2% | 82.19% | ₹5.21 L | +2.4% |
| RuPay Credit on UPI | 295 | 2.9% | 95.25% | ₹17.11 L | +33.2% |
| Credit on UPI | 193 | 1.9% | 97.93% | ₹15.22 L | +30.0% |
| UPI Circle | 170 | 1.7% | 98.24% | ₹1.39 L | −6.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,193 | 95.55% | 95.72% | ₹35.60 L | normal |
| HDFC Bank | 1,151 | 96.26% | 95.67% | ₹15.73 L | normal |
| Bank of Baroda | 742 | 95.42% | 95.58% | ₹7.59 L | normal |
| Union Bank of India | 716 | 95.39% | 95.30% | ₹8.85 L | normal |
| Punjab National Bank | 654 | 94.34% | 95.23% | ₹11.01 L | normal |
| ICICI Bank | 623 | 94.54% | 95.94% | ₹7.39 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,887 | 95.56% | 95.95% | ₹61.59 L | normal |
| Google Pay | 3,341 | 95.09% | 95.71% | ₹39.56 L | normal |
| Paytm | 800 | 95.50% | 95.65% | ₹7.51 L | normal |
| Navi | 373 | 95.98% | 95.68% | ₹4.36 L | normal |
| SuperMoney | 185 | 92.97% | 95.73% | ₹1.86 L | normal |
| BHIM | 97 | 96.91% | 95.45% | ₹2.62 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,833 | 96.05% | ₹32.00 L |
| Food & Beverage | 1,590 | 96.04% | ₹8.74 L |
| Mobility | 710 | 97.04% | ₹3.89 L |
| Bills | 641 | 95.32% | ₹6.31 L |
| Healthcare | 310 | 97.74% | ₹4.47 L |
| Digital | 184 | 86.96% | ₹70,660 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 2,955 | 29.1% | 95.63% | ₹42.02 L |
| North | 2,596 | 25.6% | 95.88% | ₹28.87 L |
| West | 2,557 | 25.2% | 95.07% | ₹31.92 L |
| East | 1,177 | 11.6% | 95.41% | ₹11.60 L |
| Central | 872 | 8.6% | 94.27% | ₹7.82 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 23 | 91.30% | ₹2.42 L |
| Vasant Wardrobe | Key Account | Retail | 61 | 88.52% | ₹1.42 L |
| Rapid Bazaar | Key Account | Retail | 283 | 95.41% | ₹95,600 |
| Hampi Stores 2298 | Key Account | Retail | 102 | 99.02% | ₹83,978 |
| Urban Boutique | Key Account | Retail | 97 | 96.91% | ₹75,997 |
| Ujjwal Water Board | Key Account | Bills | 36 | 94.44% | ₹69,674 |
| Girnar Connect | Key Account | Bills | 107 | 94.39% | ₹56,315 |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 96.77% | ₹53,312 |

## Failure analysis

Of 456 declined attempts, 370 were business declines (3.643% of attempts — balances, PINs and limits), 43 technical (0.423%), 25 timeouts (0.246%) and 18 risk declines (0.177%).

120 attempts were re-presentations of an earlier failure (1.18% of the day); 60.8% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 176 times — 1.733% of attempts against a trailing 1.332%. Owner: Customer.
- Decline code XH (Account does not exist / frozen) fired 34 times — 0.335% of attempts against a trailing 0.228%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 176 | 1.733% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 108 | 1.063% | 1.084% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.364% | 0.393% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.335% | 0.228% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.226% | 0.187% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.148% | 0.101% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 9 | 0.089% | 0.107% |
| ZX | Mandate not found or revoked | business | PSP | 9 | 0.089% | 0.088% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 99 | 74 |
| Auto-reversals | 15 | 24 |
| Disputes / chargebacks | 7 | 10 |
| Value returned | ₹1.01 L | ₹1.16 L |

## Customer behaviour

8,722 distinct customers transacted (−13.6% on the 28-day median) at 1.16 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,653 | 2,977 | 1.12 | 95.40% | ₹1,333 |
| power | 1,860 | 2,368 | 1.27 | 95.44% | ₹1,648 |
| merchant_heavy | 2,026 | 2,367 | 1.17 | 95.52% | ₹1,004 |
| small_ticket | 1,316 | 1,547 | 1.18 | 95.28% | ₹560 |
| occasional | 693 | 721 | 1.04 | 95.56% | ₹1,369 |
| new | 154 | 157 | 1.02 | 94.27% | ₹705 |
| dormant_returning | 20 | 20 | 1.00 | 95.00% | ₹541 |

## Operational events

- **MAINT-0087** (Sev-3) — Union Bank of India scheduled CBS maintenance, scoped to Union Bank of India between 01:00 and 05:00. Union Bank of India runs its announced core-banking maintenance slot every 35 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 176 times — 1.733% of attempts against a trailing 1.332%. Owner: Customer.
- 99 refunds were raised, 2.6 sigma above the trailing median of 74.
- Decline code XH (Account does not exist / frozen) fired 34 times — 0.335% of attempts against a trailing 0.228%. Owner: Issuer.
- Product UPI AutoPay ran at 82.19% success on 320 attempts (3.2% of the day), 8.63pp down its own 28-day median.
- Issuer Kotak Mahindra Bank ran at 93.80% success on 371 attempts (3.7% of the day), 2.16pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 69% across the trailing window to 170 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 38% across the trailing window to 761 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

24 March ran on trend at 95.41% success and ₹1.22 Cr settled. The movement worth carrying forward is in the decline profile: decline code Z9 (Insufficient funds) fired 176 times — 1.733% of attempts against a trailing 1.332%. Owner: Customer. 4 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-24` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,157, successes=9,691, failed=456, pending=10, settled_value_inr=12,223,303.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=176; rate_pct=1.73; trailing_rate_pct=1.33; owner=Customer; z=3.26
- products: product_name=UPI Circle; attempts=170; window_growth_pct=69.5; success_rate=98.24
- adjustments: refunds=99; trailing_median=73.5; z=2.65
- failures: failure_code=XH; count=34; rate_pct=0.33; trailing_rate_pct=0.23; owner=Issuer; z=2.73
- products: product_name=UPI Lite; attempts=761; window_growth_pct=37.6; success_rate=99.08
- products: product_name=UPI AutoPay; attempts=320; success_rate=82.19; own_median=90.81; z=-5.35
- incidents: event_id=MAINT-0087; kind=maintenance_window; severity=Sev-3; window=2026-01-13 to 2026-07-29; success_impact_pp=-38; volume_impact_pct=-55
- banks: payer_bank=Kotak Mahindra Bank; attempts=371; success_rate=93.8; own_median=95.96; z=-2.01
- categories: mcc_category=Financial Services; attempts=150; success_rate=80.67; own_median=87.76; z=-2.44
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04

Refs: enterprise_data/warehouse/transactions, RPT-D78-DAILY, enterprise_data/warehouse/reference/incidents.parquet
