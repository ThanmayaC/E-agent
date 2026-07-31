---
id: RPT-D142-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-26T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 26 May 2026)

**Report ID:** RPT-D142-DAILY · **Day 142 of 206** · **Derived from:** 14,652 transaction rows queried live from the warehouse

## Summary

The rail took **14,652 payment attempts** on Tuesday 26 May 2026 (Bakrid / Eid al-Adha (build-up)) and settled **₹1.79 Cr** across 14,078 successful payments. Volume was −1.6% on yesterday and +0.3% on the same weekday last week. Success closed at **96.08%**, in line with the trailing 28-day median of 96.05%.

Decline code Z9 (Insufficient funds) fired 201 times — 1.372% of attempts against a trailing 1.181%. Owner: Customer.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,652 | −1.6% | +0.3% | 14,797 |
| Successful payments | 14,078 | −1.7% | +0.2% | 14,194 |
| Success rate | 96.08% | −0.06pp | −0.08pp | 95.93% |
| Settled value | ₹1.79 Cr | −7.5% | −10.4% | ₹1.97 Cr |
| Average ticket | ₹1,272 | −5.9% | −10.6% | ₹1,389 |
| Technical declines | 0.491% | +0.04pp | +0.03pp | 0.508% |
| Business declines | 2.873% | −0.05pp | +0.07pp | 2.932% |
| Risk declines | 0.137% | +0.02pp | +0.01pp | 0.129% |
| Timeout declines | 0.280% | +0.00pp | −0.04pp | 0.398% |
| Retry share | 1.19% | −0.03pp | +0.01pp | 1.35% |
| Latency p95 | 1,244 ms | −2.1% | −2.2% | 1,286 ms |
| Active customers | 11,994 | −2.0% | −0.5% | 12,075 |
| Active merchants | 1,522 | +0.5% | +2.7% | 1,500 |

## What moved

- Product UPI International is compounding — attempts up 40% across the trailing window to 147 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,382 | 29.9% | 95.05% | ₹44.74 L | −2.4% |
| UPI Person to Merchant | 3,921 | 26.8% | 96.48% | ₹41.24 L | +0.4% |
| UPI QR Payments | 2,538 | 17.3% | 96.85% | ₹10.69 L | +7.1% |
| UPI Lite | 1,751 | 12.0% | 99.20% | ₹1.68 L | +3.3% |
| UPI Circle | 546 | 3.7% | 97.44% | ₹5.60 L | −1.6% |
| UPI AutoPay | 358 | 2.4% | 85.75% | ₹5.68 L | +8.6% |
| Credit on UPI | 351 | 2.4% | 96.30% | ₹24.94 L | −2.9% |
| RuPay Credit on UPI | 346 | 2.4% | 96.53% | ₹18.23 L | −6.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,624 | 95.61% | 96.05% | ₹53.52 L | normal |
| HDFC Bank | 1,562 | 96.22% | 96.20% | ₹19.15 L | normal |
| Bank of Baroda | 1,190 | 96.22% | 95.81% | ₹14.40 L | normal |
| Union Bank of India | 1,030 | 96.41% | 95.57% | ₹12.03 L | normal |
| Punjab National Bank | 932 | 95.71% | 95.68% | ₹11.60 L | normal |
| Axis Bank | 882 | 96.49% | 96.62% | ₹15.23 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,960 | 96.11% | 95.99% | ₹85.03 L | normal |
| Google Pay | 4,853 | 95.82% | 95.99% | ₹59.27 L | normal |
| Paytm | 1,194 | 96.57% | 96.05% | ₹16.64 L | normal |
| Navi | 542 | 96.68% | 95.45% | ₹4.72 L | normal |
| SuperMoney | 293 | 94.54% | 96.43% | ₹3.45 L | normal |
| FamApp | 130 | 96.92% | 94.98% | ₹2.03 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,462 | 96.80% | ₹51.44 L |
| Food & Beverage | 2,253 | 97.60% | ₹12.33 L |
| Bills | 1,123 | 95.46% | ₹11.32 L |
| Mobility | 1,115 | 97.58% | ₹5.67 L |
| Healthcare | 534 | 97.57% | ₹4.30 L |
| Digital | 279 | 94.27% | ₹1.97 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,319 | 29.5% | 96.04% | ₹54.84 L |
| North | 3,707 | 25.3% | 96.30% | ₹48.38 L |
| West | 3,542 | 24.2% | 95.79% | ₹46.07 L |
| East | 1,788 | 12.2% | 96.31% | ₹18.91 L |
| Central | 1,296 | 8.8% | 96.06% | ₹10.82 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 36 | 94.44% | ₹2.53 L |
| Vasant Wardrobe | Key Account | Retail | 95 | 96.84% | ₹2.30 L |
| Rapid Bazaar | Key Account | Retail | 465 | 97.20% | ₹1.73 L |
| Hampi Styles | Key Account | Retail | 36 | 100.00% | ₹1.04 L |
| Ujjwal Water Board | Key Account | Bills | 66 | 95.45% | ₹1.03 L |
| Hampi Stores 2298 | Key Account | Retail | 112 | 98.21% | ₹93,536 |
| Aravalli Pharmacy | Large | Healthcare | 78 | 98.72% | ₹84,986 |
| Girnar Connect | Key Account | Bills | 182 | 95.05% | ₹80,907 |

## Failure analysis

Of 554 declined attempts, 421 were business declines (2.873% of attempts — balances, PINs and limits), 72 technical (0.491%), 41 timeouts (0.280%) and 20 risk declines (0.137%).

174 attempts were re-presentations of an earlier failure (1.19% of the day); 72.4% of them succeeded.

- Decline code Z9 (Insufficient funds) fired 201 times — 1.372% of attempts against a trailing 1.181%. Owner: Customer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 201 | 1.372% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 0.860% | 1.002% |
| ZA | Transaction declined by customer | business | Customer | 37 | 0.253% | 0.336% |
| XH | Account does not exist / frozen | business | Issuer | 34 | 0.232% | 0.219% |
| U30 | Debit failed at remitter bank | technical | Issuer | 28 | 0.191% | 0.206% |
| U28 | Remitter bank unavailable | technical | Issuer | 25 | 0.171% | 0.134% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.137% | 0.155% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.116% | 0.106% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 106 | 100 |
| Auto-reversals | 25 | 27 |
| Disputes / chargebacks | 15 | 13 |
| Value returned | ₹1.20 L | ₹1.98 L |

## Customer behaviour

11,994 distinct customers transacted (+0.7% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,771 | 4,358 | 1.16 | 95.92% | ₹1,341 |
| power | 2,564 | 3,553 | 1.39 | 95.98% | ₹1,725 |
| merchant_heavy | 2,723 | 3,298 | 1.21 | 96.54% | ₹892 |
| small_ticket | 1,769 | 2,205 | 1.25 | 96.01% | ₹580 |
| occasional | 930 | 980 | 1.05 | 95.92% | ₹1,495 |
| new | 206 | 225 | 1.09 | 95.56% | ₹745 |
| dormant_returning | 31 | 33 | 1.06 | 96.97% | ₹2,286 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Decline code Z9 (Insufficient funds) fired 201 times — 1.372% of attempts against a trailing 1.181%. Owner: Customer.
- Product UPI Lite Auto Top-Up ran at 90.10% success on 101 attempts (0.7% of the day), 6.69pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 40% across the trailing window to 147 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 25% across the trailing window to 546 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

26 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 96.08% success against a 96.05% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-26` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,652, successes=14,078, failed=554, pending=20, settled_value_inr=17,902,363.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: failure_code=Z9; count=201; rate_pct=1.37; trailing_rate_pct=1.18; owner=Customer; z=2.27
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- products: product_name=UPI International; attempts=147; window_growth_pct=40.3; success_rate=96.6
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- products: product_name=UPI Circle; attempts=546; window_growth_pct=25.3; success_rate=97.44
- incidents: event_id=CMP-0059; kind=merchant_campaign; severity=Sev-3; window=2026-05-25 to 2026-06-01; success_impact_pp=-0.15; volume_impact_pct=59.67
- products: product_name=UPI Lite Auto Top-Up; attempts=101; success_rate=90.1; own_median=96.79; z=-3.8
- products: product_name=Recurring Payments; attempts=115; own_median=97; z=2.7

Refs: enterprise_data/warehouse/transactions, RPT-D141-DAILY, enterprise_data/warehouse/reference/incidents.parquet
