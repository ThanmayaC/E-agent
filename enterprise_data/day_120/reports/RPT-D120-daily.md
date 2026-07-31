---
id: RPT-D120-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-04T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 04 May 2026)

**Report ID:** RPT-D120-DAILY · **Day 120 of 206** · **Derived from:** 15,408 transaction rows queried live from the warehouse

## Summary

The rail took **15,408 payment attempts** on Monday 04 May 2026 (Working day) and settled **₹2.13 Cr** across 14,802 successful payments. Volume was +6.1% on yesterday and +24.5% on the same weekday last week. Success closed at **96.07%**, above the trailing 28-day median of 95.53%.

Product UPI Circle is compounding — attempts up 69% across the trailing window to 472 today, with success holding, so the growth is healthy and worth funding. Product Credit on UPI is compounding — attempts up 60% across the trailing window to 373 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,408 | +6.1% | +24.5% | 15,536 |
| Successful payments | 14,802 | +6.0% | +25.4% | 14,935 |
| Success rate | 96.07% | −0.06pp | +0.68pp | 96.12% |
| Settled value | ₹2.13 Cr | +29.7% | +33.3% | ₹1.99 Cr |
| Average ticket | ₹1,442 | +22.3% | +6.3% | ₹1,322 |
| Technical declines | 0.545% | +0.08pp | −0.08pp | 0.446% |
| Business declines | 2.921% | +0.13pp | −0.55pp | 2.874% |
| Risk declines | 0.058% | −0.04pp | −0.05pp | 0.113% |
| Timeout declines | 0.260% | −0.13pp | −0.08pp | 0.319% |
| Retry share | 1.13% | −0.28pp | −0.32pp | 1.32% |
| Latency p95 | 1,232 ms | +1.9% | −4.3% | 1,224 ms |
| Active customers | 12,556 | +5.6% | +21.4% | 12,553 |
| Active merchants | 1,475 | +0.8% | +5.8% | 1,498 |

## What moved

- Product UPI Circle is compounding — attempts up 69% across the trailing window to 472 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 60% across the trailing window to 373 today, with success holding, so the growth is healthy and worth funding.
- Category Bills carried 1,519 attempts, 90% up its trailing median and 15.0% of the day's volume.
- Category Healthcare carried 598 attempts, 42% up its trailing median and 5.9% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 5,309 | 34.5% | 95.05% | ₹57.31 L | +21.1% |
| UPI Person to Merchant | 3,945 | 25.6% | 96.40% | ₹41.64 L | +19.2% |
| UPI QR Payments | 2,677 | 17.4% | 96.56% | ₹11.83 L | +16.8% |
| UPI Lite | 1,513 | 9.8% | 98.81% | ₹1.48 L | +30.5% |
| UPI Circle | 472 | 3.1% | 97.25% | ₹4.09 L | +42.0% |
| RuPay Credit on UPI | 390 | 2.5% | 95.90% | ₹30.19 L | +16.6% |
| Credit on UPI | 373 | 2.4% | 95.44% | ₹32.11 L | +48.6% |
| UPI AutoPay | 327 | 2.1% | 93.58% | ₹6.32 L | +0.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,910 | 96.42% | 95.67% | ₹79.99 L | normal |
| HDFC Bank | 1,718 | 95.29% | 95.95% | ₹18.77 L | normal |
| Bank of Baroda | 1,117 | 95.61% | 95.76% | ₹14.42 L | normal |
| Union Bank of India | 1,043 | 96.55% | 94.99% | ₹13.09 L | normal |
| Axis Bank | 996 | 96.59% | 95.94% | ₹11.59 L | normal |
| ICICI Bank | 965 | 97.31% | 96.37% | ₹12.09 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,229 | 96.21% | 95.76% | ₹1.05 Cr | normal |
| Google Pay | 5,061 | 95.99% | 95.56% | ₹64.36 L | normal |
| Paytm | 1,278 | 95.46% | 95.36% | ₹21.18 L | normal |
| Navi | 552 | 94.93% | 96.18% | ₹6.22 L | normal |
| SuperMoney | 314 | 96.50% | 95.63% | ₹4.28 L | normal |
| BHIM | 151 | 95.36% | 95.70% | ₹1.46 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,772 | 96.13% | ₹41.42 L |
| Food & Beverage | 2,227 | 97.13% | ₹11.41 L |
| Bills | 1,519 | 97.24% | ₹18.46 L |
| Mobility | 1,188 | 97.64% | ₹7.62 L |
| Healthcare | 598 | 97.99% | ₹7.23 L |
| Digital | 334 | 91.92% | ₹2.09 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,571 | 29.7% | 96.37% | ₹53.57 L |
| North | 3,854 | 25.0% | 96.06% | ₹56.37 L |
| West | 3,768 | 24.5% | 95.89% | ₹59.59 L |
| East | 1,907 | 12.4% | 95.54% | ₹29.23 L |
| Central | 1,308 | 8.5% | 96.33% | ₹14.65 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 68 | 97.06% | ₹2.19 L |
| Vasant Wardrobe | Key Account | Retail | 83 | 95.18% | ₹2.12 L |
| Rapid Bazaar | Key Account | Retail | 388 | 95.88% | ₹1.80 L |
| Girnar Connect | Key Account | Bills | 276 | 97.83% | ₹1.19 L |
| Trinetra Restaurant | Large | Food & Beverage | 42 | 95.24% | ₹81,823 |
| Hampi Styles | Key Account | Retail | 36 | 100.00% | ₹79,634 |
| Yamuna Restaurant | Key Account | Food & Beverage | 69 | 100.00% | ₹74,668 |
| Urban Boutique | Key Account | Retail | 105 | 97.14% | ₹69,397 |

## Failure analysis

Of 583 declined attempts, 450 were business declines (2.921% of attempts — balances, PINs and limits), 84 technical (0.545%), 40 timeouts (0.260%) and 9 risk declines (0.058%).

174 attempts were re-presentations of an earlier failure (1.13% of the day); 64.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 187 | 1.214% | 1.303% |
| ZM | Invalid UPI PIN | business | Customer | 159 | 1.032% | 1.050% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.318% | 0.378% |
| U30 | Debit failed at remitter bank | technical | Issuer | 40 | 0.260% | 0.209% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.175% | 0.220% |
| U28 | Remitter bank unavailable | technical | Issuer | 23 | 0.149% | 0.120% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.143% | 0.201% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.084% | 0.112% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 92 | 88 |
| Auto-reversals | 21 | 29 |
| Disputes / chargebacks | 15 | 11 |
| Value returned | ₹3.20 L | ₹1.46 L |

## Customer behaviour

12,556 distinct customers transacted (+17.0% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,842 | 4,479 | 1.17 | 96.09% | ₹1,639 |
| power | 2,604 | 3,607 | 1.39 | 95.68% | ₹1,902 |
| merchant_heavy | 2,941 | 3,596 | 1.22 | 96.38% | ₹1,056 |
| small_ticket | 1,882 | 2,355 | 1.25 | 96.18% | ₹640 |
| occasional | 1,010 | 1,065 | 1.05 | 96.34% | ₹1,459 |
| new | 245 | 274 | 1.12 | 94.53% | ₹956 |
| dormant_returning | 32 | 32 | 1.00 | 96.88% | ₹473 |

## Operational events

- **INC-BANK-0013** (Sev-1) — Yes Bank issuer decline spike, scoped to Yes Bank between 19:00 and 24:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **INC-PSP-0029** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 17:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CMP-0055** (Sev-3) — Pharmacy cashback campaign, scoped to 5912. A cashback campaign across Pharmacy merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI Circle is compounding — attempts up 69% across the trailing window to 472 today, with success holding, so the growth is healthy and worth funding.
- Product Credit on UPI is compounding — attempts up 60% across the trailing window to 373 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

04 May was an incident day: INC-BANK-0013, INC-PSP-0029 were live and the rail closed at 96.07% success against a 95.53% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-04` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,408, successes=14,802, failed=583, pending=23, settled_value_inr=21,340,284.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0013; kind=bank_outage; severity=Sev-1; window=2026-05-04 to 2026-05-04; success_impact_pp=-37.09; volume_impact_pct=-32.91
- products: product_name=UPI Circle; attempts=472; window_growth_pct=69.4; success_rate=97.25
- incidents: event_id=INC-PSP-0029; kind=psp_degradation; severity=Sev-2; window=2026-05-02 to 2026-05-04; success_impact_pp=-10.68; volume_impact_pct=-16.71
- products: product_name=Credit on UPI; attempts=373; window_growth_pct=59.7; success_rate=95.44
- categories: mcc_category=Bills; attempts=1,519; own_median=798.5; z=4.81
- categories: mcc_category=Healthcare; attempts=598; own_median=421; z=4.34
- categories: mcc_category=Mobility; attempts=1,188; own_median=921.5; z=2.79
- banks: payer_bank=Axis Bank; attempts=996; own_median=767.5; z=2.47
- banks: payer_bank=Kotak Mahindra Bank; attempts=530; success_rate=97.74; own_median=95.81; z=2.41
- incidents: event_id=CMP-0055; kind=merchant_campaign; severity=Sev-3; window=2026-04-30 to 2026-05-08; success_impact_pp=-0.17; volume_impact_pct=67.55

Refs: enterprise_data/warehouse/transactions, RPT-D119-DAILY, enterprise_data/warehouse/reference/incidents.parquet
