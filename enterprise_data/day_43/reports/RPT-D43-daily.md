---
id: RPT-D43-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-16T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Monday, 16 Feb 2026)

**Report ID:** RPT-D43-DAILY · **Day 43 of 206** · **Derived from:** 10,897 transaction rows queried live from the warehouse

## Summary

The rail took **10,897 payment attempts** on Monday 16 February 2026 (Working day) and settled **₹1.33 Cr** across 10,445 successful payments. Volume was +2.4% on yesterday and +4.9% on the same weekday last week. Success closed at **95.85%**, above the trailing 28-day median of 95.41%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,897 | +2.4% | +4.9% | 10,946 |
| Successful payments | 10,445 | +2.6% | +4.7% | 10,444 |
| Success rate | 95.85% | +0.18pp | −0.20pp | 95.37% |
| Settled value | ₹1.33 Cr | +7.2% | +25.8% | ₹1.24 Cr |
| Average ticket | ₹1,276 | +4.5% | +20.2% | ₹1,187 |
| Technical declines | 0.431% | +0.10pp | +0.09pp | 0.431% |
| Business declines | 3.294% | −0.22pp | +0.15pp | 3.523% |
| Risk declines | 0.138% | +0.04pp | +0.04pp | 0.142% |
| Timeout declines | 0.202% | −0.02pp | −0.04pp | 0.419% |
| Retry share | 1.16% | +0.04pp | −0.10pp | 1.48% |
| Latency p95 | 1,263 ms | +1.3% | −1.4% | 1,291 ms |
| Active customers | 9,210 | +1.7% | +4.1% | 9,220 |
| Active merchants | 1,255 | +0.1% | +0.0% | 1,259 |

## What moved

Nothing crossed the materiality threshold today: every dimension tracked inside its own 28-day band, so the day is a clean baseline rather than an event to explain.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,951 | 36.3% | 95.34% | ₹41.07 L | +1.3% |
| UPI Person to Merchant | 3,159 | 29.0% | 96.45% | ₹33.00 L | +1.5% |
| UPI QR Payments | 2,115 | 19.4% | 96.78% | ₹9.51 L | +24.2% |
| UPI Lite | 619 | 5.7% | 98.38% | ₹53,072 | −14.9% |
| UPI AutoPay | 288 | 2.6% | 89.93% | ₹5.18 L | −3.5% |
| RuPay Credit on UPI | 210 | 1.9% | 94.76% | ₹10.57 L | +4.5% |
| Credit on UPI | 148 | 1.4% | 90.54% | ₹9.68 L | +2.1% |
| Recurring Payments | 115 | 1.1% | 88.70% | ₹5.30 L | +39.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,484 | 95.64% | 95.49% | ₹40.67 L | normal |
| HDFC Bank | 1,167 | 96.57% | 95.88% | ₹14.25 L | normal |
| Bank of Baroda | 848 | 97.64% | 95.28% | ₹7.79 L | ⚠ outlier |
| Union Bank of India | 790 | 95.06% | 95.20% | ₹9.17 L | normal |
| Punjab National Bank | 668 | 92.66% | 94.84% | ₹8.97 L | ⚠ outlier |
| ICICI Bank | 639 | 95.93% | 96.31% | ₹9.89 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,153 | 95.81% | 95.29% | ₹61.15 L | normal |
| Google Pay | 3,606 | 95.73% | 95.61% | ₹42.80 L | normal |
| Paytm | 885 | 96.16% | 94.87% | ₹12.02 L | normal |
| Navi | 379 | 95.78% | 95.58% | ₹6.43 L | normal |
| SuperMoney | 217 | 95.85% | 96.27% | ₹1.78 L | normal |
| BHIM | 97 | 98.97% | 94.59% | ₹1.19 L | ⚠ outlier |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,927 | 96.41% | ₹34.84 L |
| Food & Beverage | 1,673 | 96.83% | ₹7.77 L |
| Mobility | 807 | 96.53% | ₹5.08 L |
| Bills | 650 | 96.77% | ₹8.02 L |
| Healthcare | 383 | 95.56% | ₹5.57 L |
| Digital | 168 | 92.86% | ₹95,476 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,136 | 28.8% | 96.08% | ₹39.16 L |
| North | 2,810 | 25.8% | 95.30% | ₹30.74 L |
| West | 2,691 | 24.7% | 96.17% | ₹38.52 L |
| East | 1,290 | 11.8% | 95.89% | ₹15.25 L |
| Central | 970 | 8.9% | 95.77% | ₹9.59 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vasant Wardrobe | Key Account | Retail | 61 | 100.00% | ₹2.00 L |
| Vega Electronics | Large | Retail | 38 | 97.37% | ₹1.93 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 82 | 98.78% | ₹1.25 L |
| Rapid Bazaar | Key Account | Retail | 327 | 96.02% | ₹1.23 L |
| Aravalli Pharmacy | Large | Healthcare | 67 | 97.01% | ₹94,188 |
| Swift Mart 1738 | Key Account | Retail | 94 | 96.81% | ₹93,331 |
| Ujjwal Water Board | Key Account | Bills | 37 | 91.89% | ₹64,213 |
| Hampi Stores 2298 | Key Account | Retail | 107 | 96.26% | ₹62,109 |

## Failure analysis

Of 443 declined attempts, 359 were business declines (3.294% of attempts — balances, PINs and limits), 47 technical (0.431%), 22 timeouts (0.202%) and 15 risk declines (0.138%).

126 attempts were re-presentations of an earlier failure (1.16% of the day); 63.5% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 143 | 1.312% | 1.464% |
| ZM | Invalid UPI PIN | business | Customer | 110 | 1.009% | 1.196% |
| ZA | Transaction declined by customer | business | Customer | 54 | 0.496% | 0.423% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.294% | 0.231% |
| U30 | Debit failed at remitter bank | technical | Issuer | 21 | 0.193% | 0.213% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 14 | 0.128% | 0.105% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.119% | 0.136% |
| UX | Mandate execution outside permitted window | business | PSP | 12 | 0.110% | 0.105% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 60 | 70 |
| Auto-reversals | 17 | 20 |
| Disputes / chargebacks | 6 | 4 |
| Value returned | ₹71,023 | ₹1.14 L |

## Customer behaviour

9,210 distinct customers transacted (+3.8% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,778 | 3,113 | 1.12 | 96.15% | ₹1,127 |
| power | 1,947 | 2,550 | 1.31 | 95.69% | ₹1,964 |
| merchant_heavy | 2,080 | 2,466 | 1.19 | 95.54% | ₹1,069 |
| small_ticket | 1,454 | 1,755 | 1.21 | 96.35% | ₹505 |
| occasional | 750 | 794 | 1.06 | 94.71% | ₹1,357 |
| new | 173 | 189 | 1.09 | 97.35% | ₹986 |
| dormant_returning | 28 | 30 | 1.07 | 96.67% | ₹678 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- Issuer Punjab National Bank ran at 92.66% success on 668 attempts (6.1% of the day), 2.18pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

16 February was an incident day: INC-FRAUD-0048 was live and the rail closed at 95.85% success against a 95.41% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-16` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,897, successes=10,445, failed=443, pending=9, settled_value_inr=13,325,622.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- banks: payer_bank=Bank of Baroda; attempts=848; success_rate=97.64; own_median=95.28; z=2.53
- banks: payer_bank=Punjab National Bank; attempts=668; success_rate=92.66; own_median=94.84; z=-2.06
- products: product_name=Recurring Payments; attempts=115; own_median=82.5; z=4.87
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- categories: mcc_category=Financial Services; attempts=158; own_median=134; z=2.49

Refs: enterprise_data/warehouse/transactions, RPT-D42-DAILY, enterprise_data/warehouse/reference/incidents.parquet
