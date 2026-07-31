---
id: RPT-D26-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-30T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 30 Jan 2026)

**Report ID:** RPT-D26-DAILY · **Day 26 of 206** · **Derived from:** 10,452 transaction rows queried live from the warehouse

## Summary

The rail took **10,452 payment attempts** on Friday 30 January 2026 (Working day) and settled **₹1.28 Cr** across 10,029 successful payments. Volume was +22.1% on yesterday and −17.5% on the same weekday last week. Success closed at **95.95%**, above the trailing 28-day median of 95.15%.

Success rate closed at 95.95%, 0.80pp up the trailing median — a 1.7-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,452 | +22.1% | −17.5% | 10,256 |
| Successful payments | 10,029 | +22.9% | −17.1% | 9,761 |
| Success rate | 95.95% | +0.68pp | +0.48pp | 95.14% |
| Settled value | ₹1.28 Cr | +34.5% | −15.1% | ₹1.16 Cr |
| Average ticket | ₹1,281 | +9.4% | +2.4% | ₹1,185 |
| Technical declines | 0.431% | −0.04pp | −0.33pp | 0.604% |
| Business declines | 3.148% | −0.55pp | −0.02pp | 3.606% |
| Risk declines | 0.105% | +0.00pp | −0.03pp | 0.131% |
| Timeout declines | 0.258% | −0.08pp | −0.09pp | 0.383% |
| Retry share | 1.22% | −0.44pp | −0.07pp | 1.50% |
| Latency p95 | 1,203 ms | −8.6% | −2.6% | 1,246 ms |
| Active customers | 8,867 | +19.6% | −15.1% | 8,694 |
| Active merchants | 1,210 | +5.2% | −6.5% | 1,199 |

## What moved

- Success rate closed at 95.95%, 0.80pp up the trailing median — a 1.7-sigma move.
- Category Bills carried 910 attempts, 44% up its trailing median and 14.0% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,967 | 38.0% | 95.56% | ₹43.68 L | −0.5% |
| UPI Person to Merchant | 2,915 | 27.9% | 96.36% | ₹26.66 L | −0.3% |
| UPI QR Payments | 1,802 | 17.2% | 96.45% | ₹7.65 L | +9.3% |
| UPI Lite | 727 | 7.0% | 99.17% | ₹65,064 | +12.7% |
| UPI AutoPay | 301 | 2.9% | 90.37% | ₹5.26 L | −1.0% |
| RuPay Credit on UPI | 190 | 1.8% | 94.21% | ₹15.94 L | −1.0% |
| Credit on UPI | 175 | 1.7% | 94.29% | ₹12.51 L | +33.6% |
| UPI Lite Auto Top-Up | 89 | 0.9% | 98.88% | ₹97,957 | +6.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,269 | 95.50% | 94.91% | ₹35.25 L | normal |
| HDFC Bank | 1,158 | 96.46% | 95.89% | ₹15.44 L | normal |
| Bank of Baroda | 778 | 96.02% | 94.46% | ₹11.28 L | normal |
| Union Bank of India | 735 | 95.10% | 94.72% | ₹10.00 L | normal |
| Axis Bank | 654 | 96.48% | 95.28% | ₹9.12 L | normal |
| ICICI Bank | 634 | 96.53% | 95.92% | ₹12.08 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,896 | 95.75% | 95.08% | ₹61.55 L | normal |
| Google Pay | 3,415 | 96.46% | 95.26% | ₹41.24 L | normal |
| Paytm | 916 | 95.85% | 94.59% | ₹10.55 L | normal |
| Navi | 369 | 95.93% | 95.79% | ₹6.32 L | normal |
| SuperMoney | 202 | 94.55% | 95.49% | ₹2.77 L | normal |
| BHIM | 129 | 94.57% | 95.33% | ₹1.37 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,512 | 96.42% | ₹27.61 L |
| Food & Beverage | 1,506 | 97.01% | ₹6.64 L |
| Bills | 910 | 97.03% | ₹9.45 L |
| Mobility | 736 | 96.47% | ₹4.48 L |
| Healthcare | 325 | 95.38% | ₹4.69 L |
| Digital | 223 | 93.27% | ₹1.15 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,055 | 29.2% | 95.94% | ₹40.51 L |
| North | 2,704 | 25.9% | 95.86% | ₹35.17 L |
| West | 2,566 | 24.6% | 95.56% | ₹28.90 L |
| East | 1,214 | 11.6% | 96.29% | ₹14.85 L |
| Central | 913 | 8.7% | 96.93% | ₹9.02 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 26 | 96.15% | ₹2.64 L |
| Vasant Wardrobe | Key Account | Retail | 72 | 90.28% | ₹1.45 L |
| Rapid Bazaar | Key Account | Retail | 250 | 98.80% | ₹1.03 L |
| Girnar Connect | Key Account | Bills | 168 | 99.40% | ₹82,196 |
| Ujjwal Water Board | Key Account | Bills | 47 | 100.00% | ₹80,947 |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 94.12% | ₹72,260 |
| Urban Boutique | Key Account | Retail | 89 | 96.63% | ₹70,502 |
| Shakti Stores 1531 | Key Account | Retail | 60 | 96.67% | ₹54,585 |

## Failure analysis

Of 412 declined attempts, 329 were business declines (3.148% of attempts — balances, PINs and limits), 45 technical (0.431%), 27 timeouts (0.258%) and 11 risk declines (0.105%).

127 attempts were re-presentations of an earlier failure (1.22% of the day); 64.6% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 150 | 1.435% | 1.541% |
| ZM | Invalid UPI PIN | business | Customer | 100 | 0.957% | 1.130% |
| ZA | Transaction declined by customer | business | Customer | 32 | 0.306% | 0.411% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.239% | 0.238% |
| U30 | Debit failed at remitter bank | technical | Issuer | 18 | 0.172% | 0.262% |
| U28 | Remitter bank unavailable | technical | Issuer | 18 | 0.172% | 0.155% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 15 | 0.144% | 0.131% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 12 | 0.115% | 0.185% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 75 | 59 |
| Auto-reversals | 20 | 22 |
| Disputes / chargebacks | 4 | 2 |
| Value returned | ₹91,345 | ₹96,474 |

## Customer behaviour

8,867 distinct customers transacted (+1.0% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,738 | 3,037 | 1.11 | 96.15% | ₹1,294 |
| power | 1,888 | 2,493 | 1.32 | 95.99% | ₹1,662 |
| merchant_heavy | 1,996 | 2,374 | 1.19 | 95.62% | ₹1,063 |
| small_ticket | 1,279 | 1,525 | 1.19 | 96.07% | ₹516 |
| occasional | 744 | 785 | 1.06 | 95.54% | ₹1,646 |
| new | 195 | 211 | 1.08 | 97.16% | ₹760 |
| dormant_returning | 27 | 27 | 1.00 | 96.30% | ₹343 |

## Operational events

- **INC-PSP-0025** (Sev-2) — Navi app release regression, scoped to Navi between 18:00 and 23:00. A Navi client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **INC-BANK-0015** (Sev-3) — Union Bank of India issuer decline spike, scoped to Union Bank of India between 10:00 and 14:00. Union Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

30 January was an incident day: INC-PSP-0025 was live and the rail closed at 95.95% success against a 95.15% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-01-30` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,452, successes=10,029, failed=412, pending=11, settled_value_inr=12,844,292.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-PSP-0025; kind=psp_degradation; severity=Sev-2; window=2026-01-28 to 2026-01-30; success_impact_pp=-7.08; volume_impact_pct=-11.08
- headline: success_rate=95.95; trailing_median=95.15; z=1.71
- categories: mcc_category=Bills; attempts=910; own_median=632; z=3.68
- geography: region=Central; attempts=913; success_rate=96.93; own_median=95.32; z=2.34
- incidents: event_id=INC-BANK-0015; kind=bank_outage; severity=Sev-3; window=2026-01-29 to 2026-01-30; success_impact_pp=-4.58; volume_impact_pct=-4.06
- banks: payer_bank=Kotak Mahindra Bank; attempts=365; success_rate=96.99; own_median=95.25; z=2.3
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24

Refs: enterprise_data/warehouse/transactions, RPT-D25-DAILY, enterprise_data/warehouse/reference/incidents.parquet
