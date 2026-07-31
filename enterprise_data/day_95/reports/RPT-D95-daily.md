---
id: RPT-D95-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-09T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 09 Apr 2026)

**Report ID:** RPT-D95-DAILY · **Day 95 of 206** · **Derived from:** 12,248 transaction rows queried live from the warehouse

## Summary

The rail took **12,248 payment attempts** on Thursday 09 April 2026 (Working day) and settled **₹1.58 Cr** across 11,766 successful payments. Volume was −9.2% on yesterday and +2.5% on the same weekday last week. Success closed at **96.06%**, in line with the trailing 28-day median of 95.91%.

92 refunds were raised, 2.4 sigma above the trailing median of 74.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,248 | −9.2% | +2.5% | 13,066 |
| Successful payments | 11,766 | −9.1% | +2.5% | 12,469 |
| Success rate | 96.06% | +0.09pp | +0.03pp | 95.41% |
| Settled value | ₹1.58 Cr | −10.2% | −2.2% | ₹1.69 Cr |
| Average ticket | ₹1,346 | −1.2% | −4.6% | ₹1,352 |
| Technical declines | 0.408% | −0.15pp | −0.03pp | 0.582% |
| Business declines | 2.890% | +0.01pp | −0.16pp | 2.979% |
| Risk declines | 0.122% | +0.02pp | −0.00pp | 0.148% |
| Timeout declines | 0.392% | +0.01pp | +0.12pp | 0.752% |
| Retry share | 1.14% | −0.09pp | +0.00pp | 1.73% |
| Latency p95 | 1,276 ms | +1.6% | −1.1% | 1,368 ms |
| Active customers | 10,238 | −8.0% | +2.0% | 10,783 |
| Active merchants | 1,359 | −2.4% | +0.7% | 1,394 |

## What moved

- Product UPI Lite is compounding — attempts up 47% across the trailing window to 997 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 246 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,447 | 36.3% | 95.64% | ₹49.22 L | +1.4% |
| UPI Person to Merchant | 3,174 | 25.9% | 96.16% | ₹31.90 L | −9.0% |
| UPI QR Payments | 2,183 | 17.8% | 96.52% | ₹8.73 L | +2.2% |
| UPI Lite | 997 | 8.1% | 99.00% | ₹91,643 | −2.6% |
| RuPay Credit on UPI | 337 | 2.8% | 94.66% | ₹19.67 L | +33.2% |
| UPI AutoPay | 319 | 2.6% | 89.34% | ₹5.58 L | −0.3% |
| UPI Circle | 246 | 2.0% | 98.37% | ₹2.41 L | +7.0% |
| Credit on UPI | 197 | 1.6% | 95.94% | ₹16.87 L | +14.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,905 | 96.21% | 95.94% | ₹50.87 L | normal |
| HDFC Bank | 1,339 | 95.74% | 95.46% | ₹17.51 L | normal |
| Bank of Baroda | 916 | 95.52% | 96.02% | ₹10.06 L | normal |
| Union Bank of India | 859 | 96.51% | 95.69% | ₹11.71 L | normal |
| ICICI Bank | 785 | 97.71% | 95.73% | ₹11.75 L | normal |
| Punjab National Bank | 734 | 95.37% | 95.41% | ₹11.85 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,790 | 96.06% | 95.88% | ₹72.63 L | normal |
| Google Pay | 4,058 | 95.76% | 95.68% | ₹51.18 L | normal |
| Paytm | 1,005 | 96.82% | 95.97% | ₹12.51 L | normal |
| Navi | 425 | 96.71% | 95.74% | ₹6.97 L | normal |
| SuperMoney | 245 | 97.96% | 95.09% | ₹2.61 L | normal |
| BHIM | 114 | 94.74% | 96.46% | ₹1.52 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,286 | 96.41% | ₹37.57 L |
| Food & Beverage | 1,886 | 96.87% | ₹8.79 L |
| Mobility | 899 | 96.89% | ₹4.98 L |
| Bills | 730 | 96.71% | ₹8.26 L |
| Healthcare | 425 | 97.65% | ₹6.35 L |
| Digital | 195 | 90.26% | ₹95,494 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,565 | 29.1% | 95.88% | ₹40.95 L |
| North | 3,095 | 25.3% | 95.80% | ₹42.19 L |
| West | 3,036 | 24.8% | 95.98% | ₹38.89 L |
| East | 1,495 | 12.2% | 96.86% | ₹21.85 L |
| Central | 1,057 | 8.6% | 96.59% | ₹14.54 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 27 | 92.59% | ₹1.92 L |
| Vasant Wardrobe | Key Account | Retail | 63 | 92.06% | ₹1.56 L |
| Rapid Bazaar | Key Account | Retail | 300 | 97.67% | ₹1.42 L |
| Hampi Stores 2298 | Key Account | Retail | 120 | 96.67% | ₹1.04 L |
| Hampi Styles | Key Account | Retail | 36 | 97.22% | ₹1.01 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 61 | 95.08% | ₹88,824 |
| Ujjwal Water Board | Key Account | Bills | 44 | 93.18% | ₹88,715 |
| Urban Boutique | Key Account | Retail | 103 | 97.09% | ₹78,833 |

## Failure analysis

Of 467 declined attempts, 354 were business declines (2.890% of attempts — balances, PINs and limits), 50 technical (0.408%), 48 timeouts (0.392%) and 15 risk declines (0.122%).

140 attempts were re-presentations of an earlier failure (1.14% of the day); 65.0% of them succeeded.

- Decline code U54 (Transaction timed out at beneficiary) fired 32 times — 0.261% of attempts against a trailing 0.166%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 156 | 1.274% | 1.322% |
| ZM | Invalid UPI PIN | business | Customer | 119 | 0.972% | 1.039% |
| ZA | Transaction declined by customer | business | Customer | 44 | 0.359% | 0.358% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 32 | 0.261% | 0.166% |
| U30 | Debit failed at remitter bank | technical | Issuer | 26 | 0.212% | 0.190% |
| XH | Account does not exist / frozen | business | Issuer | 24 | 0.196% | 0.221% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.106% | 0.113% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 12 | 0.098% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 92 | 74 |
| Auto-reversals | 36 | 24 |
| Disputes / chargebacks | 12 | 10 |
| Value returned | ₹1.61 L | ₹1.47 L |

## Customer behaviour

10,238 distinct customers transacted (−0.0% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,147 | 3,583 | 1.14 | 95.95% | ₹1,461 |
| power | 2,187 | 2,909 | 1.33 | 96.15% | ₹1,662 |
| merchant_heavy | 2,360 | 2,818 | 1.19 | 96.31% | ₹1,173 |
| small_ticket | 1,523 | 1,861 | 1.22 | 95.86% | ₹582 |
| occasional | 790 | 837 | 1.06 | 95.82% | ₹1,446 |
| new | 205 | 214 | 1.04 | 95.79% | ₹691 |
| dormant_returning | 26 | 26 | 1.00 | 100.00% | ₹1,030 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 92 refunds were raised, 2.4 sigma above the trailing median of 74.
- Decline code U54 (Transaction timed out at beneficiary) fired 32 times — 0.261% of attempts against a trailing 0.166%. Owner: Issuer.

### Opportunities

- Product UPI Lite is compounding — attempts up 47% across the trailing window to 997 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 34% across the trailing window to 246 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

09 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 96.06% success against a 95.91% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-09` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,248, successes=11,766, failed=467, pending=15, settled_value_inr=15,841,902.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- adjustments: refunds=92; trailing_median=74.5; z=2.36
- products: product_name=UPI Lite; attempts=997; window_growth_pct=46.9; success_rate=99
- failures: failure_code=U54; count=32; rate_pct=0.26; trailing_rate_pct=0.17; owner=Issuer; z=2.15
- products: product_name=UPI Circle; attempts=246; window_growth_pct=33.8; success_rate=98.37
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41
- incidents: event_id=CMP-0051; kind=merchant_campaign; severity=Sev-3; window=2026-04-04 to 2026-04-10; success_impact_pp=-0.14; volume_impact_pct=56.15

Refs: enterprise_data/warehouse/transactions, RPT-D94-DAILY, enterprise_data/warehouse/reference/incidents.parquet
