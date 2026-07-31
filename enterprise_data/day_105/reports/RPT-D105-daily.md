---
id: RPT-D105-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-19T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Sunday, 19 Apr 2026)

**Report ID:** RPT-D105-DAILY · **Day 105 of 206** · **Derived from:** 13,937 transaction rows queried live from the warehouse

## Summary

The rail took **13,937 payment attempts** on Sunday 19 April 2026 (Akshaya Tritiya (build-up)) and settled **₹1.54 Cr** across 13,328 successful payments. Volume was −13.9% on yesterday and +22.9% on the same weekday last week. Success closed at **95.63%**, below the trailing 28-day median of 95.92%.

86 auto-reversals were raised, 5.7 sigma above the trailing median of 22. Category Retail carried 4,608 attempts, 43% up its trailing median and 49.5% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,937 | −13.9% | +22.9% | 12,818 |
| Successful payments | 13,328 | −14.3% | +23.2% | 12,208 |
| Success rate | 95.63% | −0.48pp | +0.27pp | 95.21% |
| Settled value | ₹1.54 Cr | −19.6% | +25.9% | ₹1.63 Cr |
| Average ticket | ₹1,159 | −6.2% | +2.2% | ₹1,337 |
| Technical declines | 0.416% | +0.10pp | −0.02pp | 0.601% |
| Business declines | 3.394% | +0.44pp | −0.19pp | 3.158% |
| Risk declines | 0.129% | +0.04pp | +0.01pp | 0.146% |
| Timeout declines | 0.301% | −0.15pp | −0.10pp | 0.767% |
| Retry share | 1.18% | −1.51pp | −0.23pp | 1.77% |
| Latency p95 | 1,225 ms | −1.8% | −2.0% | 1,361 ms |
| Active customers | 11,478 | −11.6% | +19.8% | 10,616 |
| Active merchants | 1,416 | −3.6% | +5.0% | 1,384 |

## What moved

- Category Retail carried 4,608 attempts, 43% up its trailing median and 49.5% of the day's volume.
- Product UPI Circle is compounding — attempts up 53% across the trailing window to 377 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 34% across the trailing window to 1,333 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,619 | 33.1% | 94.85% | ₹48.32 L | +9.5% |
| UPI Person to Merchant | 3,795 | 27.2% | 95.57% | ₹37.97 L | +13.5% |
| UPI QR Payments | 2,704 | 19.4% | 96.71% | ₹11.43 L | +27.1% |
| UPI Lite | 1,333 | 9.6% | 98.42% | ₹1.21 L | +26.8% |
| UPI Circle | 377 | 2.7% | 97.35% | ₹3.05 L | +43.6% |
| UPI AutoPay | 351 | 2.5% | 88.03% | ₹5.76 L | +9.0% |
| RuPay Credit on UPI | 212 | 1.5% | 97.64% | ₹10.60 L | −26.5% |
| Credit on UPI | 171 | 1.2% | 96.49% | ₹9.37 L | −12.8% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,375 | 95.43% | 95.92% | ₹47.37 L | normal |
| HDFC Bank | 1,519 | 94.73% | 96.04% | ₹19.77 L | normal |
| Bank of Baroda | 1,076 | 96.28% | 95.67% | ₹9.70 L | normal |
| Union Bank of India | 945 | 94.92% | 95.89% | ₹10.29 L | normal |
| ICICI Bank | 900 | 95.89% | 95.82% | ₹9.74 L | normal |
| Punjab National Bank | 881 | 95.57% | 95.64% | ₹8.13 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,701 | 95.97% | 95.78% | ₹66.79 L | normal |
| Google Pay | 4,546 | 95.29% | 95.63% | ₹52.87 L | normal |
| Paytm | 1,154 | 94.71% | 95.85% | ₹12.45 L | normal |
| Navi | 497 | 95.37% | 95.88% | ₹5.72 L | normal |
| SuperMoney | 260 | 94.62% | 94.55% | ₹7.10 L | normal |
| YONO SBI | 131 | 93.89% | 95.68% | ₹1.52 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,608 | 95.90% | ₹44.02 L |
| Food & Beverage | 2,023 | 97.13% | ₹9.63 L |
| Mobility | 947 | 97.36% | ₹4.49 L |
| Bills | 742 | 95.96% | ₹8.27 L |
| Healthcare | 408 | 97.79% | ₹3.29 L |
| Digital | 190 | 92.63% | ₹88,580 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,113 | 29.5% | 95.14% | ₹45.16 L |
| North | 3,478 | 25.0% | 96.41% | ₹39.06 L |
| West | 3,453 | 24.8% | 95.83% | ₹38.61 L |
| East | 1,635 | 11.7% | 95.35% | ₹20.50 L |
| Central | 1,258 | 9.0% | 94.91% | ₹11.14 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 29 | 96.55% | ₹1.98 L |
| Vasant Wardrobe | Key Account | Retail | 89 | 93.26% | ₹1.95 L |
| Rapid Bazaar | Key Account | Retail | 440 | 96.59% | ₹1.89 L |
| Ujjwal Water Board | Key Account | Bills | 33 | 93.94% | ₹1.40 L |
| Urban Boutique | Key Account | Retail | 144 | 96.53% | ₹1.06 L |
| Hampi Stores 2298 | Key Account | Retail | 159 | 95.60% | ₹88,563 |
| Zenith Diner | Large | Food & Beverage | 25 | 92.00% | ₹69,976 |
| Girnar Connect | Key Account | Bills | 135 | 95.56% | ₹65,076 |

## Failure analysis

Of 591 declined attempts, 473 were business declines (3.394% of attempts — balances, PINs and limits), 58 technical (0.416%), 42 timeouts (0.301%) and 18 risk declines (0.129%).

164 attempts were re-presentations of an earlier failure (1.18% of the day); 62.2% of them succeeded.

- Decline code ZA (Transaction declined by customer) fired 65 times — 0.466% of attempts against a trailing 0.369%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 190 | 1.363% | 1.322% |
| ZM | Invalid UPI PIN | business | Customer | 151 | 1.083% | 1.022% |
| ZA | Transaction declined by customer | business | Customer | 65 | 0.466% | 0.369% |
| XH | Account does not exist / frozen | business | Issuer | 36 | 0.258% | 0.220% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.179% | 0.193% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.144% | 0.183% |
| ZX | Mandate not found or revoked | business | PSP | 17 | 0.122% | 0.075% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 16 | 0.115% | 0.103% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 88 | 78 |
| Auto-reversals | 86 | 22 |
| Disputes / chargebacks | 11 | 11 |
| Value returned | ₹1.19 L | ₹1.55 L |

## Customer behaviour

11,478 distinct customers transacted (+12.5% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,597 | 4,145 | 1.15 | 95.97% | ₹1,179 |
| power | 2,408 | 3,307 | 1.37 | 95.07% | ₹1,456 |
| merchant_heavy | 2,579 | 3,110 | 1.21 | 95.69% | ₹941 |
| small_ticket | 1,670 | 2,074 | 1.24 | 95.90% | ₹692 |
| occasional | 957 | 1,013 | 1.06 | 95.06% | ₹1,120 |
| new | 231 | 251 | 1.09 | 97.21% | ₹750 |
| dormant_returning | 36 | 37 | 1.03 | 91.89% | ₹1,595 |

## Operational events

- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.
- **CMP-0054** (Sev-3) — Mobile & DTH Recharge cashback campaign, scoped to 4814. A cashback campaign across Mobile & DTH Recharge merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 86 auto-reversals were raised, 5.7 sigma above the trailing median of 22.
- Decline code ZA (Transaction declined by customer) fired 65 times — 0.466% of attempts against a trailing 0.369%. Owner: Customer.
- Category Financial Services ran at 79.01% success on 162 attempts (1.7% of the day), 8.28pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 53% across the trailing window to 377 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 34% across the trailing window to 1,333 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

19 April ran on trend at 95.63% success and ₹1.54 Cr settled. The movement worth carrying forward is in money moving back: 86 auto-reversals were raised, 5.7 sigma above the trailing median of 22. 3 further movements cleared the materiality threshold and are listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-19` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,937, successes=13,328, failed=591, pending=18, settled_value_inr=15,446,574.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: reversals=86; trailing_median=22.5; z=5.71
- categories: mcc_category=Retail; attempts=4,608; own_median=3,224.5; z=5.71
- products: product_name=UPI Circle; attempts=377; window_growth_pct=53.3; success_rate=97.35
- failures: failure_code=ZA; count=65; rate_pct=0.47; trailing_rate_pct=0.37; owner=Customer; z=2.26
- products: product_name=UPI Lite; attempts=1,333; window_growth_pct=33.6; success_rate=98.42
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=CMP-0053; kind=merchant_campaign; severity=Sev-3; window=2026-04-14 to 2026-04-21; success_impact_pp=-0.2; volume_impact_pct=80.12
- incidents: event_id=CMP-0054; kind=merchant_campaign; severity=Sev-3; window=2026-04-15 to 2026-04-22; success_impact_pp=-0.17; volume_impact_pct=66.38
- products: product_name=UPI Circle; attempts=377; own_median=262.5; z=2.41
- categories: mcc_category=Financial Services; attempts=162; success_rate=79.01; own_median=87.3; z=-2.18

Refs: enterprise_data/warehouse/transactions, RPT-D104-DAILY, enterprise_data/warehouse/reference/incidents.parquet
