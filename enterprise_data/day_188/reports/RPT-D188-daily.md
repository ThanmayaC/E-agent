---
id: RPT-D188-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-11T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 11 Jul 2026)

**Report ID:** RPT-D188-DAILY · **Day 188 of 206** · **Derived from:** 16,402 transaction rows queried live from the warehouse

## Summary

The rail took **16,402 payment attempts** on Saturday 11 July 2026 (Weekend) and settled **₹1.85 Cr** across 15,746 successful payments. Volume was −5.8% on yesterday and −17.3% on the same weekday last week. Success closed at **96.00%**, in line with the trailing 28-day median of 96.16%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,402 | −5.8% | −17.3% | 17,179 |
| Successful payments | 15,746 | −5.7% | −14.5% | 16,500 |
| Success rate | 96.00% | +0.12pp | +3.16pp | 96.09% |
| Settled value | ₹1.85 Cr | −14.3% | −21.1% | ₹2.17 Cr |
| Average ticket | ₹1,177 | −9.1% | −7.7% | ₹1,314 |
| Technical declines | 0.439% | −0.14pp | −0.92pp | 0.498% |
| Business declines | 3.122% | +0.12pp | +0.42pp | 2.700% |
| Risk declines | 0.085% | −0.06pp | −0.06pp | 0.111% |
| Timeout declines | 0.244% | −0.07pp | −2.61pp | 0.515% |
| Retry share | 1.45% | +0.01pp | −1.92pp | 1.47% |
| Latency p95 | 1,198 ms | −10.3% | −35.0% | 1,311 ms |
| Active customers | 13,357 | −4.1% | −12.6% | 13,811 |
| Active merchants | 1,602 | −2.0% | −5.2% | 1,639 |

## What moved

- Product UPI Person to Merchant ran at 95.32% success on 3,998 attempts (24.4% of the day), 0.82pp down its own 28-day median.
- Product UPI Lite is compounding — attempts up 37% across the trailing window to 2,844 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 29% across the trailing window to 1,084 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,447 | 27.1% | 95.26% | ₹46.23 L | +0.4% |
| UPI Person to Merchant | 3,998 | 24.4% | 95.32% | ₹39.99 L | +10.4% |
| UPI Lite | 2,844 | 17.3% | 98.95% | ₹2.57 L | +15.1% |
| UPI QR Payments | 2,633 | 16.1% | 96.43% | ₹11.57 L | +3.4% |
| UPI Circle | 1,084 | 6.6% | 97.23% | ₹9.23 L | +34.2% |
| UPI AutoPay | 398 | 2.4% | 88.94% | ₹6.98 L | +5.7% |
| Credit on UPI | 283 | 1.7% | 95.76% | ₹23.56 L | −40.4% |
| RuPay Credit on UPI | 244 | 1.5% | 94.26% | ₹11.72 L | −34.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,113 | 96.40% | 96.16% | ₹66.71 L | normal |
| HDFC Bank | 1,854 | 95.63% | 96.39% | ₹17.50 L | normal |
| Bank of Baroda | 1,299 | 96.84% | 96.22% | ₹12.89 L | normal |
| Union Bank of India | 1,105 | 94.75% | 96.12% | ₹13.52 L | normal |
| ICICI Bank | 1,022 | 97.36% | 96.34% | ₹11.75 L | normal |
| Axis Bank | 966 | 94.93% | 96.17% | ₹8.70 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,697 | 95.97% | 96.20% | ₹82.72 L | normal |
| Google Pay | 5,395 | 96.07% | 96.18% | ₹62.20 L | normal |
| Paytm | 1,392 | 95.40% | 96.16% | ₹20.86 L | normal |
| Navi | 639 | 95.93% | 96.55% | ₹6.87 L | normal |
| SuperMoney | 323 | 97.52% | 95.64% | ₹3.75 L | normal |
| BHIM | 144 | 93.75% | 95.69% | ₹80,995 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,881 | 96.70% | ₹47.57 L |
| Food & Beverage | 3,127 | 96.61% | ₹14.31 L |
| Mobility | 1,578 | 97.47% | ₹7.68 L |
| Bills | 998 | 96.09% | ₹9.16 L |
| Healthcare | 633 | 96.68% | ₹7.42 L |
| Digital | 250 | 91.60% | ₹1.29 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,742 | 28.9% | 95.63% | ₹57.63 L |
| North | 4,260 | 26.0% | 95.85% | ₹49.63 L |
| West | 4,048 | 24.7% | 96.22% | ₹43.40 L |
| East | 1,893 | 11.5% | 96.62% | ₹21.11 L |
| Central | 1,459 | 8.9% | 96.23% | ₹13.52 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 81 | 95.06% | ₹2.20 L |
| Vega Electronics | Large | Retail | 36 | 97.22% | ₹2.17 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 74 | 94.59% | ₹2.11 L |
| Rapid Bazaar | Key Account | Retail | 529 | 98.11% | ₹1.88 L |
| Hampi Styles | Key Account | Retail | 39 | 94.87% | ₹1.10 L |
| Tejas Bites | Key Account | Food & Beverage | 233 | 97.85% | ₹82,300 |
| Hampi Stores 2298 | Key Account | Retail | 113 | 97.35% | ₹82,146 |
| Ujjwal Water Board | Key Account | Bills | 31 | 96.77% | ₹80,462 |

## Failure analysis

Of 638 declined attempts, 512 were business declines (3.122% of attempts — balances, PINs and limits), 72 technical (0.439%), 40 timeouts (0.244%) and 14 risk declines (0.085%).

238 attempts were re-presentations of an earlier failure (1.45% of the day); 55.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 191 | 1.164% | 1.224% |
| ZM | Invalid UPI PIN | business | Customer | 183 | 1.116% | 0.956% |
| ZA | Transaction declined by customer | business | Customer | 65 | 0.396% | 0.325% |
| XH | Account does not exist / frozen | business | Issuer | 38 | 0.232% | 0.187% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.171% | 0.176% |
| UX | Mandate execution outside permitted window | business | PSP | 18 | 0.110% | 0.079% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.110% | 0.122% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 17 | 0.104% | 0.092% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 113 | 110 |
| Auto-reversals | 23 | 24 |
| Disputes / chargebacks | 9 | 14 |
| Value returned | ₹3.23 L | ₹1.68 L |

## Customer behaviour

13,357 distinct customers transacted (+4.1% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,193 | 4,869 | 1.16 | 95.54% | ₹1,184 |
| power | 2,875 | 4,031 | 1.40 | 96.08% | ₹1,515 |
| merchant_heavy | 3,107 | 3,798 | 1.22 | 96.37% | ₹939 |
| small_ticket | 1,933 | 2,377 | 1.23 | 96.51% | ₹614 |
| occasional | 995 | 1,046 | 1.05 | 95.60% | ₹1,375 |
| new | 220 | 246 | 1.12 | 94.31% | ₹707 |
| dormant_returning | 34 | 35 | 1.03 | 100.00% | ₹559 |

## Operational events

- **INC-SETL-0082** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **INC-BANK-0003** (Sev-2) — Axis Bank issuer decline spike, scoped to Axis Bank between 09:00 and 14:00. Axis Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- Product UPI Person to Merchant ran at 95.32% success on 3,998 attempts (24.4% of the day), 0.82pp down its own 28-day median.

### Opportunities

- Product UPI Lite is compounding — attempts up 37% across the trailing window to 2,844 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 29% across the trailing window to 1,084 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

11 July was an incident day: INC-SETL-0082, INC-BANK-0003 were live and the rail closed at 96.00% success against a 96.16% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-11` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,402, successes=15,746, failed=638, pending=18, settled_value_inr=18,529,468.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-SETL-0082; kind=settlement_delay; severity=Sev-2; window=2026-07-10 to 2026-07-12; success_impact_pp=-6.29; volume_impact_pct=-22.54
- incidents: event_id=INC-BANK-0003; kind=bank_outage; severity=Sev-2; window=2026-07-11 to 2026-07-11; success_impact_pp=-18.99; volume_impact_pct=-16.85
- products: product_name=UPI Person to Merchant; attempts=3,998; success_rate=95.32; own_median=96.14; z=-2.36
- products: product_name=UPI Lite; attempts=2,844; window_growth_pct=37.3; success_rate=98.95
- products: product_name=UPI Circle; attempts=1,084; window_growth_pct=29; success_rate=97.23
- products: product_name=UPI Circle; attempts=1,084; own_median=807.5; z=3.36

Refs: enterprise_data/warehouse/transactions, RPT-D187-DAILY, enterprise_data/warehouse/reference/incidents.parquet
