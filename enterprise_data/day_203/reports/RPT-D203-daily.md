---
id: RPT-D203-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 26 Jul 2026)

**Report ID:** RPT-D203-DAILY · **Day 203 of 206** · **Derived from:** 13,825 transaction rows queried live from the warehouse

## Summary

The rail took **13,825 payment attempts** on Sunday 26 July 2026 (Weekend) and settled **₹1.57 Cr** across 13,247 successful payments. Volume was −15.2% on yesterday and −0.2% on the same weekday last week. Success closed at **95.82%**, below the trailing 28-day median of 96.17%.

Decline code Z9 (Insufficient funds) fired 228 times — 1.649% of attempts against a trailing 1.191%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,825 | −15.2% | −0.2% | 15,767 |
| Successful payments | 13,247 | −15.4% | −0.3% | 15,153 |
| Success rate | 95.82% | −0.27pp | −0.09pp | 96.12% |
| Settled value | ₹1.57 Cr | −22.1% | +5.1% | ₹2.06 Cr |
| Average ticket | ₹1,188 | −7.9% | +5.4% | ₹1,359 |
| Technical declines | 0.369% | −0.04pp | −0.01pp | 0.448% |
| Business declines | 3.284% | +0.33pp | +0.06pp | 2.851% |
| Risk declines | 0.065% | −0.02pp | −0.06pp | 0.110% |
| Timeout declines | 0.362% | +0.05pp | +0.09pp | 0.374% |
| Retry share | 1.37% | +0.19pp | +0.19pp | 1.29% |
| Latency p95 | 1,241 ms | +3.9% | −0.5% | 1,294 ms |
| Active customers | 11,629 | −13.1% | +0.3% | 12,908 |
| Active merchants | 1,548 | −2.8% | +0.7% | 1,602 |

## What moved

- Issuer Union Bank of India ran at 94.84% success on 949 attempts (6.9% of the day), 1.32pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,964 | 28.7% | 94.85% | ₹41.63 L | −13.0% |
| UPI Person to Merchant | 3,360 | 24.3% | 96.46% | ₹29.81 L | −11.1% |
| UPI QR Payments | 2,316 | 16.8% | 96.68% | ₹9.87 L | −11.0% |
| UPI Lite | 2,175 | 15.7% | 98.90% | ₹1.91 L | −13.1% |
| UPI Circle | 723 | 5.2% | 98.20% | ₹5.93 L | −11.4% |
| UPI AutoPay | 383 | 2.8% | 80.16% | ₹5.99 L | +1.3% |
| Credit on UPI | 257 | 1.9% | 92.61% | ₹16.30 L | −50.7% |
| RuPay Credit on UPI | 205 | 1.5% | 93.66% | ₹17.56 L | −45.3% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,423 | 96.11% | 96.33% | ₹48.03 L | normal |
| HDFC Bank | 1,500 | 95.80% | 96.40% | ₹18.14 L | normal |
| Bank of Baroda | 1,014 | 95.56% | 96.45% | ₹12.02 L | normal |
| Union Bank of India | 949 | 94.84% | 96.16% | ₹9.97 L | ⚠ outlier |
| Axis Bank | 838 | 95.82% | 96.34% | ₹10.08 L | normal |
| ICICI Bank | 835 | 96.65% | 96.50% | ₹9.67 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,437 | 95.57% | 96.21% | ₹68.03 L | normal |
| Google Pay | 4,557 | 95.70% | 96.30% | ₹53.65 L | normal |
| Paytm | 1,172 | 96.67% | 96.23% | ₹16.53 L | normal |
| Navi | 512 | 97.85% | 96.51% | ₹5.34 L | normal |
| SuperMoney | 292 | 96.58% | 96.34% | ₹2.21 L | normal |
| FamApp | 132 | 96.21% | 96.54% | ₹3.76 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,758 | 96.91% | ₹32.41 L |
| Food & Beverage | 2,404 | 97.09% | ₹10.48 L |
| Bills | 1,255 | 95.30% | ₹10.45 L |
| Mobility | 1,223 | 97.47% | ₹5.63 L |
| Healthcare | 507 | 97.63% | ₹3.51 L |
| Digital | 270 | 90.37% | ₹1.15 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,061 | 29.4% | 96.16% | ₹55.28 L |
| North | 3,604 | 26.1% | 95.31% | ₹31.98 L |
| West | 3,365 | 24.3% | 95.60% | ₹37.47 L |
| East | 1,578 | 11.4% | 96.39% | ₹18.92 L |
| Central | 1,217 | 8.8% | 96.06% | ₹13.76 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 390 | 97.95% | ₹1.71 L |
| Vega Electronics | Large | Retail | 29 | 96.55% | ₹1.61 L |
| Vasant Wardrobe | Key Account | Retail | 51 | 92.16% | ₹92,867 |
| Girnar Connect | Key Account | Bills | 207 | 94.69% | ₹74,797 |
| Ujjwal Water Board | Key Account | Bills | 39 | 97.44% | ₹58,818 |
| Hampi Stores 2298 | Key Account | Retail | 79 | 93.67% | ₹55,124 |
| Malabar Supermart 1818 | Large | Retail | 49 | 97.96% | ₹53,962 |
| Swift Grill | Large | Food & Beverage | 24 | 91.67% | ₹50,195 |

## Failure analysis

Of 564 declined attempts, 454 were business declines (3.284% of attempts — balances, PINs and limits), 51 technical (0.369%), 50 timeouts (0.362%) and 9 risk declines (0.065%).

189 attempts were re-presentations of an earlier failure (1.37% of the day); 66.1% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 228 times — 1.649% of attempts against a trailing 1.191%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 30 times — 0.217% of attempts against a trailing 0.133%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 228 | 1.649% | 1.191% |
| ZM | Invalid UPI PIN | business | Customer | 134 | 0.969% | 0.941% |
| ZA | Transaction declined by customer | business | Customer | 41 | 0.297% | 0.326% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 30 | 0.217% | 0.133% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.210% | 0.171% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.203% | 0.185% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.116% | 0.087% |
| UX | Mandate execution outside permitted window | business | PSP | 14 | 0.101% | 0.082% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 115 | 113 |
| Auto-reversals | 33 | 23 |
| Disputes / chargebacks | 14 | 16 |
| Value returned | ₹1.98 L | ₹1.68 L |

## Customer behaviour

11,629 distinct customers transacted (−11.0% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,518 | 3,971 | 1.13 | 95.59% | ₹1,393 |
| power | 2,567 | 3,385 | 1.32 | 95.98% | ₹1,671 |
| merchant_heavy | 2,703 | 3,198 | 1.18 | 95.72% | ₹803 |
| small_ticket | 1,753 | 2,125 | 1.21 | 96.19% | ₹416 |
| occasional | 882 | 926 | 1.05 | 95.57% | ₹975 |
| new | 188 | 201 | 1.07 | 96.02% | ₹898 |
| dormant_returning | 18 | 19 | 1.06 | 100.00% | ₹933 |

## Operational events

- **INC-BANK-0019** (Sev-2) — Yes Bank issuer decline spike, scoped to Yes Bank between 17:00 and 20:00. Yes Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CMP-0064** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 228 times — 1.649% of attempts against a trailing 1.191%. Owner: Customer.
- Decline code U54 (Transaction timed out at beneficiary) fired 30 times — 0.217% of attempts against a trailing 0.133%. Owner: Issuer.
- Issuer Union Bank of India ran at 94.84% success on 949 attempts (6.9% of the day), 1.32pp down its own 28-day median.
- Product UPI AutoPay ran at 80.16% success on 383 attempts (2.8% of the day), 8.86pp down its own 28-day median.
- Product Credit on UPI ran at 92.61% success on 257 attempts (1.9% of the day), 3.01pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

26 July was an incident day: INC-BANK-0019 was live and the rail closed at 95.82% success against a 96.17% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,825, successes=13,247, failed=564, pending=14, settled_value_inr=15,740,965.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=228; rate_pct=1.65; trailing_rate_pct=1.19; owner=Customer; z=4.56
- incidents: event_id=INC-BANK-0019; kind=bank_outage; severity=Sev-2; window=2026-07-25 to 2026-07-27; success_impact_pp=-14.88; volume_impact_pct=-13.2
- failures: failure_code=U54; count=30; rate_pct=0.22; trailing_rate_pct=0.13; owner=Issuer; z=2.93
- banks: payer_bank=Union Bank of India; attempts=949; success_rate=94.84; own_median=96.16; z=-3.44
- products: product_name=UPI AutoPay; attempts=383; success_rate=80.16; own_median=89.02; z=-3.33
- products: product_name=Credit on UPI; attempts=257; success_rate=92.61; own_median=95.61; z=-3.77
- categories: mcc_category=Financial Services; attempts=182; success_rate=78.02; own_median=86.05; z=-2.72
- incidents: event_id=CMP-0064; kind=merchant_campaign; severity=Sev-3; window=2026-07-22 to 2026-07-27; success_impact_pp=-0.11; volume_impact_pct=44.38
- products: product_name=RuPay Credit on UPI; attempts=205; own_median=375; z=-2.83

Refs: enterprise_data/warehouse/transactions, RPT-D202-DAILY, enterprise_data/warehouse/reference/incidents.parquet
