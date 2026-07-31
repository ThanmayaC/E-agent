---
id: RPT-D195-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-18T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 18 Jul 2026)

**Report ID:** RPT-D195-DAILY · **Day 195 of 206** · **Derived from:** 16,561 transaction rows queried live from the warehouse

## Summary

The rail took **16,561 payment attempts** on Saturday 18 July 2026 (Weekend) and settled **₹2.25 Cr** across 15,992 successful payments. Volume was +6.3% on yesterday and +1.0% on the same weekday last week. Success closed at **96.56%**, above the trailing 28-day median of 96.13%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,561 | +6.3% | +1.0% | 16,400 |
| Successful payments | 15,992 | +6.6% | +1.6% | 15,764 |
| Success rate | 96.56% | +0.30pp | +0.56pp | 96.15% |
| Settled value | ₹2.25 Cr | +3.8% | +21.5% | ₹2.14 Cr |
| Average ticket | ₹1,408 | −2.6% | +19.7% | ₹1,358 |
| Technical declines | 0.332% | −0.08pp | −0.11pp | 0.454% |
| Business declines | 2.693% | −0.24pp | −0.43pp | 2.801% |
| Risk declines | 0.097% | +0.01pp | +0.01pp | 0.104% |
| Timeout declines | 0.193% | −0.01pp | −0.05pp | 0.399% |
| Retry share | 1.01% | −0.19pp | −0.44pp | 1.33% |
| Latency p95 | 1,264 ms | −3.3% | +5.5% | 1,303 ms |
| Active customers | 13,455 | +5.0% | +0.7% | 13,316 |
| Active merchants | 1,635 | +1.1% | +2.1% | 1,618 |

## What moved

- Product Credit on UPI is compounding — attempts up 30% across the trailing window to 482 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle carried 1,137 attempts, 41% up its trailing median and 6.9% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,492 | 27.1% | 95.24% | ₹46.74 L | −2.3% |
| UPI Person to Merchant | 4,011 | 24.2% | 96.68% | ₹42.38 L | +9.8% |
| UPI QR Payments | 2,672 | 16.1% | 96.78% | ₹11.15 L | +4.7% |
| UPI Lite | 2,561 | 15.5% | 99.41% | ₹2.33 L | −0.2% |
| UPI Circle | 1,137 | 6.9% | 97.27% | ₹9.75 L | +40.8% |
| Credit on UPI | 482 | 2.9% | 96.68% | ₹38.36 L | +0.6% |
| UPI AutoPay | 380 | 2.3% | 91.58% | ₹7.03 L | +0.5% |
| RuPay Credit on UPI | 306 | 1.8% | 96.08% | ₹19.91 L | −20.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,226 | 96.71% | 96.19% | ₹65.42 L | normal |
| HDFC Bank | 1,730 | 96.65% | 96.39% | ₹25.20 L | normal |
| Bank of Baroda | 1,313 | 96.57% | 96.35% | ₹16.53 L | normal |
| Union Bank of India | 1,141 | 96.84% | 96.25% | ₹13.43 L | normal |
| Axis Bank | 1,003 | 96.31% | 96.17% | ₹15.26 L | normal |
| ICICI Bank | 1,002 | 96.81% | 96.34% | ₹16.18 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,883 | 96.69% | 96.21% | ₹1.02 Cr | normal |
| Google Pay | 5,438 | 96.56% | 96.09% | ₹83.62 L | normal |
| Paytm | 1,314 | 96.19% | 96.18% | ₹15.22 L | normal |
| Navi | 593 | 96.63% | 96.33% | ₹11.47 L | normal |
| SuperMoney | 324 | 97.84% | 96.22% | ₹3.43 L | normal |
| FamApp | 148 | 95.27% | 96.75% | ₹1.23 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,105 | 97.10% | ₹62.74 L |
| Food & Beverage | 3,106 | 97.33% | ₹14.61 L |
| Mobility | 1,511 | 98.48% | ₹7.82 L |
| Bills | 986 | 96.35% | ₹10.95 L |
| Healthcare | 610 | 97.87% | ₹12.10 L |
| Digital | 217 | 95.39% | ₹1.04 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,850 | 29.3% | 96.52% | ₹65.70 L |
| North | 4,309 | 26.0% | 96.43% | ₹51.35 L |
| West | 4,007 | 24.2% | 96.81% | ₹62.78 L |
| East | 1,869 | 11.3% | 96.20% | ₹30.71 L |
| Central | 1,526 | 9.2% | 96.92% | ₹14.65 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 512 | 97.46% | ₹2.41 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 94.59% | ₹2.19 L |
| Vega Electronics | Large | Retail | 34 | 97.06% | ₹2.10 L |
| Ujjwal Water Board | Key Account | Bills | 30 | 96.67% | ₹1.83 L |
| Hampi Styles | Key Account | Retail | 48 | 93.75% | ₹1.71 L |
| Hampi Stores 2298 | Key Account | Retail | 122 | 97.54% | ₹1.20 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 80 | 98.75% | ₹90,520 |
| Urban Boutique | Key Account | Retail | 131 | 96.18% | ₹89,692 |

## Failure analysis

Of 549 declined attempts, 446 were business declines (2.693% of attempts — balances, PINs and limits), 55 technical (0.332%), 32 timeouts (0.193%) and 16 risk declines (0.097%).

167 attempts were re-presentations of an earlier failure (1.01% of the day); 62.3% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 188 | 1.135% | 1.218% |
| ZM | Invalid UPI PIN | business | Customer | 151 | 0.912% | 0.995% |
| ZA | Transaction declined by customer | business | Customer | 43 | 0.260% | 0.325% |
| XH | Account does not exist / frozen | business | Issuer | 37 | 0.223% | 0.185% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.133% | 0.127% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.121% | 0.174% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.097% | 0.092% |
| U28 | Remitter bank unavailable | technical | Issuer | 14 | 0.085% | 0.115% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 112 | 113 |
| Auto-reversals | 23 | 23 |
| Disputes / chargebacks | 8 | 16 |
| Value returned | ₹5.97 L | ₹1.80 L |

## Customer behaviour

13,455 distinct customers transacted (+3.1% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,149 | 4,835 | 1.17 | 96.55% | ₹1,396 |
| merchant_heavy | 3,183 | 3,925 | 1.23 | 96.46% | ₹1,147 |
| power | 2,818 | 3,921 | 1.39 | 97.02% | ₹1,918 |
| small_ticket | 2,019 | 2,509 | 1.24 | 96.49% | ₹590 |
| occasional | 1,044 | 1,113 | 1.07 | 95.60% | ₹1,869 |
| new | 217 | 232 | 1.07 | 96.12% | ₹676 |
| dormant_returning | 25 | 26 | 1.04 | 100.00% | ₹1,042 |

## Operational events

- **INC-BANK-0020** (Sev-2) — Federal Bank issuer decline spike, scoped to Federal Bank between 20:00 and 24:00. Federal Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product Credit on UPI is compounding — attempts up 30% across the trailing window to 482 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

18 July was an incident day: INC-BANK-0020 was live and the rail closed at 96.56% success against a 96.13% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-18` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,561, successes=15,992, failed=549, pending=20, settled_value_inr=22,518,175.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0020; kind=bank_outage; severity=Sev-2; window=2026-07-17 to 2026-07-19; success_impact_pp=-11.07; volume_impact_pct=-9.82
- products: product_name=Credit on UPI; attempts=482; window_growth_pct=30.1; success_rate=96.68
- products: product_name=UPI Circle; attempts=1,137; own_median=807.5; z=4

Refs: enterprise_data/warehouse/transactions, RPT-D194-DAILY, enterprise_data/warehouse/reference/incidents.parquet
