---
id: RPT-D202-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-25T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 25 Jul 2026)

**Report ID:** RPT-D202-DAILY · **Day 202 of 206** · **Derived from:** 16,300 transaction rows queried live from the warehouse

## Summary

The rail took **16,300 payment attempts** on Saturday 25 July 2026 (Weekend) and settled **₹2.02 Cr** across 15,662 successful payments. Volume was +5.4% on yesterday and −1.6% on the same weekday last week. Success closed at **96.09%**, in line with the trailing 28-day median of 96.23%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,300 | +5.4% | −1.6% | 15,845 |
| Successful payments | 15,662 | +5.5% | −2.1% | 15,229 |
| Success rate | 96.09% | +0.02pp | −0.48pp | 96.14% |
| Settled value | ₹2.02 Cr | −5.8% | −10.3% | ₹2.08 Cr |
| Average ticket | ₹1,290 | −10.7% | −8.4% | ₹1,365 |
| Technical declines | 0.405% | −0.05pp | +0.07pp | 0.451% |
| Business declines | 2.957% | +0.08pp | +0.26pp | 2.834% |
| Risk declines | 0.086% | −0.03pp | −0.01pp | 0.111% |
| Timeout declines | 0.313% | −0.08pp | +0.12pp | 0.374% |
| Retry share | 1.18% | +0.18pp | +0.17pp | 1.28% |
| Latency p95 | 1,194 ms | −8.8% | −5.5% | 1,296 ms |
| Active customers | 13,383 | +4.5% | −0.5% | 12,959 |
| Active merchants | 1,592 | +0.1% | −2.6% | 1,604 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,603 | 28.2% | 95.05% | ₹46.40 L | +1.7% |
| UPI Person to Merchant | 4,141 | 25.4% | 95.97% | ₹39.74 L | +10.6% |
| UPI QR Payments | 2,759 | 16.9% | 96.77% | ₹10.64 L | +6.6% |
| UPI Lite | 2,459 | 15.1% | 98.94% | ₹2.26 L | −3.7% |
| UPI Circle | 967 | 5.9% | 97.41% | ₹7.61 L | +18.5% |
| UPI AutoPay | 381 | 2.3% | 86.88% | ₹6.26 L | +0.8% |
| Credit on UPI | 304 | 1.9% | 94.41% | ₹31.34 L | −41.7% |
| RuPay Credit on UPI | 218 | 1.3% | 96.79% | ₹14.46 L | −41.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,184 | 96.32% | 96.32% | ₹58.30 L | normal |
| HDFC Bank | 1,777 | 96.40% | 96.41% | ₹28.69 L | normal |
| Bank of Baroda | 1,331 | 94.74% | 96.45% | ₹11.96 L | normal |
| Union Bank of India | 1,055 | 96.11% | 96.20% | ₹11.68 L | normal |
| Axis Bank | 1,020 | 95.29% | 96.42% | ₹13.09 L | normal |
| Punjab National Bank | 977 | 96.42% | 95.68% | ₹12.11 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,856 | 95.68% | 96.22% | ₹96.65 L | normal |
| Google Pay | 5,281 | 96.55% | 96.22% | ₹64.23 L | normal |
| Paytm | 1,343 | 96.35% | 96.17% | ₹16.80 L | normal |
| Navi | 569 | 95.61% | 96.51% | ₹6.02 L | normal |
| SuperMoney | 340 | 95.88% | 96.54% | ₹3.08 L | normal |
| BHIM | 150 | 96.67% | 95.71% | ₹3.32 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,843 | 96.84% | ₹55.47 L |
| Food & Beverage | 3,085 | 97.18% | ₹13.60 L |
| Mobility | 1,454 | 97.32% | ₹6.28 L |
| Bills | 966 | 95.34% | ₹9.76 L |
| Healthcare | 623 | 96.63% | ₹6.40 L |
| Digital | 231 | 90.04% | ₹97,799 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,905 | 30.1% | 96.51% | ₹62.18 L |
| North | 4,132 | 25.3% | 95.69% | ₹45.35 L |
| West | 4,045 | 24.8% | 95.87% | ₹53.59 L |
| East | 1,764 | 10.8% | 96.37% | ₹23.86 L |
| Central | 1,454 | 8.9% | 96.01% | ₹17.13 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 25 | 96.00% | ₹3.05 L |
| Rapid Bazaar | Key Account | Retail | 482 | 98.76% | ₹1.85 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 89.06% | ₹1.19 L |
| Girnar Connect | Key Account | Bills | 176 | 93.75% | ₹90,625 |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 95.59% | ₹82,253 |
| Dhruva Supermart | Large | Retail | 88 | 95.45% | ₹75,051 |
| Urban Boutique | Key Account | Retail | 131 | 95.42% | ₹73,513 |
| Tejas Bites | Key Account | Food & Beverage | 217 | 96.77% | ₹69,083 |

## Failure analysis

Of 613 declined attempts, 482 were business declines (2.957% of attempts — balances, PINs and limits), 66 technical (0.405%), 51 timeouts (0.313%) and 14 risk declines (0.086%).

192 attempts were re-presentations of an earlier failure (1.18% of the day); 68.2% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 211 | 1.294% | 1.191% |
| ZM | Invalid UPI PIN | business | Customer | 151 | 0.926% | 0.933% |
| ZA | Transaction declined by customer | business | Customer | 61 | 0.374% | 0.326% |
| U30 | Debit failed at remitter bank | technical | Issuer | 31 | 0.190% | 0.171% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 25 | 0.153% | 0.133% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.147% | 0.188% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 20 | 0.123% | 0.087% |
| U28 | Remitter bank unavailable | technical | Issuer | 19 | 0.117% | 0.118% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 98 | 113 |
| Auto-reversals | 33 | 23 |
| Disputes / chargebacks | 18 | 16 |
| Value returned | ₹3.44 L | ₹1.68 L |

## Customer behaviour

13,383 distinct customers transacted (+2.5% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,183 | 4,833 | 1.16 | 96.48% | ₹1,473 |
| power | 2,889 | 3,944 | 1.37 | 95.49% | ₹1,620 |
| merchant_heavy | 3,109 | 3,812 | 1.23 | 95.96% | ₹1,032 |
| small_ticket | 2,003 | 2,453 | 1.22 | 96.25% | ₹570 |
| occasional | 942 | 980 | 1.04 | 96.02% | ₹1,151 |
| new | 226 | 245 | 1.08 | 97.96% | ₹918 |
| dormant_returning | 31 | 33 | 1.06 | 100.00% | ₹583 |

## Operational events

- **INC-BANK-0019** (Sev-2) — Yes Bank issuer decline spike, scoped to Yes Bank between 17:00 and 20:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0064** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Category Digital ran at 90.04% success on 231 attempts (2.0% of the day), 3.98pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

25 July was an incident day: INC-BANK-0019 was live and the rail closed at 96.09% success against a 96.23% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-25` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,300, successes=15,662, failed=613, pending=25, settled_value_inr=20,209,701.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0019; kind=bank_outage; severity=Sev-2; window=2026-07-25 to 2026-07-27; success_impact_pp=-14.88; volume_impact_pct=-13.2
- incidents: event_id=CMP-0064; kind=merchant_campaign; severity=Sev-3; window=2026-07-22 to 2026-07-27; success_impact_pp=-0.11; volume_impact_pct=44.38
- categories: mcc_category=Digital; attempts=231; success_rate=90.04; own_median=94.02; z=-2.41
- products: product_name=RuPay Credit on UPI; attempts=218; own_median=375; z=-2.61

Refs: enterprise_data/warehouse/transactions, RPT-D201-DAILY, enterprise_data/warehouse/reference/incidents.parquet
