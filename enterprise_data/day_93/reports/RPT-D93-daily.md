---
id: RPT-D93-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-07T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 07 Apr 2026)

**Report ID:** RPT-D93-DAILY · **Day 93 of 206** · **Derived from:** 12,939 transaction rows queried live from the warehouse

## Summary

The rail took **12,939 payment attempts** on Tuesday 07 April 2026 (Working day) and settled **₹1.70 Cr** across 12,413 successful payments. Volume was −5.3% on yesterday and −5.6% on the same weekday last week. Success closed at **95.93%**, in line with the trailing 28-day median of 95.84%.

72 auto-reversals were raised, 5.9 sigma above the trailing median of 24. Category Bills carried 1,382 attempts, 96% up its trailing median and 16.2% of the day's volume.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,939 | −5.3% | −5.6% | 13,123 |
| Successful payments | 12,413 | −5.6% | −5.9% | 12,502 |
| Success rate | 95.93% | −0.25pp | −0.39pp | 95.24% |
| Settled value | ₹1.70 Cr | −2.1% | −18.1% | ₹1.69 Cr |
| Average ticket | ₹1,369 | +3.7% | −13.0% | ₹1,351 |
| Technical declines | 0.379% | −0.07pp | −0.08pp | 0.610% |
| Business declines | 2.983% | +0.20pp | +0.31pp | 3.006% |
| Risk declines | 0.131% | −0.01pp | +0.02pp | 0.157% |
| Timeout declines | 0.441% | +0.06pp | +0.10pp | 0.857% |
| Retry share | 1.22% | −1.57pp | −0.04pp | 1.88% |
| Latency p95 | 1,276 ms | +0.5% | +0.0% | 1,397 ms |
| Active customers | 10,729 | −4.4% | −4.6% | 10,811 |
| Active merchants | 1,415 | −0.8% | +0.4% | 1,399 |

## What moved

- Category Bills carried 1,382 attempts, 96% up its trailing median and 16.2% of the day's volume.
- Product UPI Lite is compounding — attempts up 54% across the trailing window to 1,066 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 45% across the trailing window to 240 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,395 | 34.0% | 95.31% | ₹47.17 L | +1.5% |
| UPI Person to Merchant | 3,482 | 26.9% | 96.07% | ₹39.81 L | +0.2% |
| UPI QR Payments | 2,566 | 19.8% | 97.08% | ₹10.60 L | +23.3% |
| UPI Lite | 1,066 | 8.2% | 99.06% | ₹98,987 | +10.2% |
| UPI AutoPay | 335 | 2.6% | 88.36% | ₹5.72 L | +4.7% |
| RuPay Credit on UPI | 275 | 2.1% | 95.64% | ₹18.53 L | +9.8% |
| UPI Circle | 240 | 1.9% | 95.00% | ₹2.20 L | +6.4% |
| Credit on UPI | 206 | 1.6% | 94.17% | ₹19.81 L | +21.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,104 | 96.13% | 95.86% | ₹53.12 L | normal |
| HDFC Bank | 1,412 | 95.40% | 95.53% | ₹20.34 L | normal |
| Bank of Baroda | 963 | 96.47% | 96.02% | ₹9.28 L | normal |
| Union Bank of India | 876 | 96.35% | 95.69% | ₹9.46 L | normal |
| ICICI Bank | 790 | 95.44% | 95.73% | ₹9.66 L | normal |
| Punjab National Bank | 782 | 96.55% | 95.21% | ₹10.20 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,214 | 95.80% | 95.88% | ₹84.82 L | normal |
| Google Pay | 4,226 | 95.74% | 95.68% | ₹54.38 L | normal |
| Paytm | 1,033 | 96.22% | 95.97% | ₹16.50 L | normal |
| Navi | 457 | 97.59% | 95.67% | ₹4.34 L | normal |
| SuperMoney | 288 | 96.18% | 94.87% | ₹2.26 L | normal |
| YONO SBI | 119 | 95.80% | 96.05% | ₹1.19 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,138 | 96.05% | ₹36.60 L |
| Food & Beverage | 2,044 | 97.02% | ₹9.99 L |
| Bills | 1,382 | 96.45% | ₹19.08 L |
| Mobility | 917 | 96.51% | ₹5.24 L |
| Healthcare | 387 | 98.19% | ₹3.39 L |
| Digital | 295 | 94.24% | ₹1.66 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,809 | 29.4% | 95.77% | ₹48.86 L |
| North | 3,281 | 25.4% | 95.70% | ₹42.98 L |
| West | 3,171 | 24.5% | 95.62% | ₹42.00 L |
| East | 1,599 | 12.4% | 96.69% | ₹23.16 L |
| Central | 1,079 | 8.3% | 97.03% | ₹12.90 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 84 | 100.00% | ₹2.26 L |
| Vega Electronics | Large | Retail | 30 | 90.00% | ₹1.63 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 83 | 96.39% | ₹1.41 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 96.88% | ₹1.38 L |
| Girnar Connect | Key Account | Bills | 269 | 97.40% | ₹1.31 L |
| Rapid Bazaar | Key Account | Retail | 313 | 96.81% | ₹1.17 L |
| Hampi Styles | Key Account | Retail | 39 | 100.00% | ₹88,066 |
| Swift Grill | Large | Food & Beverage | 55 | 94.55% | ₹65,918 |

## Failure analysis

Of 509 declined attempts, 386 were business declines (2.983% of attempts — balances, PINs and limits), 49 technical (0.379%), 57 timeouts (0.441%) and 17 risk declines (0.131%).

158 attempts were re-presentations of an earlier failure (1.22% of the day); 64.6% of them succeeded.

- Decline code BT (Acquirer / NPCI switch timeout) fired 22 times — 0.170% of attempts against a trailing 0.102%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 155 | 1.198% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 133 | 1.028% | 1.056% |
| ZA | Transaction declined by customer | business | Customer | 45 | 0.348% | 0.360% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 26 | 0.201% | 0.159% |
| XH | Account does not exist / frozen | business | Issuer | 25 | 0.193% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 24 | 0.185% | 0.191% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 22 | 0.170% | 0.102% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 15 | 0.116% | 0.116% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 83 | 76 |
| Auto-reversals | 72 | 24 |
| Disputes / chargebacks | 8 | 10 |
| Value returned | ₹2.09 L | ₹1.53 L |

## Customer behaviour

10,729 distinct customers transacted (+6.2% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,292 | 3,735 | 1.13 | 95.74% | ₹1,378 |
| power | 2,263 | 3,058 | 1.35 | 96.14% | ₹1,910 |
| merchant_heavy | 2,471 | 3,004 | 1.22 | 95.91% | ₹951 |
| small_ticket | 1,632 | 2,014 | 1.23 | 95.83% | ₹605 |
| occasional | 837 | 881 | 1.05 | 96.37% | ₹1,882 |
| new | 199 | 212 | 1.07 | 95.28% | ₹1,138 |
| dormant_returning | 35 | 35 | 1.00 | 100.00% | ₹830 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- 72 auto-reversals were raised, 5.9 sigma above the trailing median of 24.
- Product UPI Circle is compounding — attempts up 45% across the trailing window to 240 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code BT (Acquirer / NPCI switch timeout) fired 22 times — 0.170% of attempts against a trailing 0.102%. Owner: NPCI.

### Opportunities

- Product UPI Lite is compounding — attempts up 54% across the trailing window to 1,066 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

07 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 95.93% success against a 95.84% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-07` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,939, successes=12,413, failed=509, pending=17, settled_value_inr=16,990,396.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: reversals=72; trailing_median=23.5; z=5.95
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- categories: mcc_category=Bills; attempts=1,382; own_median=706; z=5.81
- products: product_name=UPI Lite; attempts=1,066; window_growth_pct=54.3; success_rate=99.06
- products: product_name=UPI Circle; attempts=240; window_growth_pct=45.5; success_rate=95
- failures: failure_code=BT; count=22; rate_pct=0.17; trailing_rate_pct=0.1; owner=NPCI; z=3.21
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41
- incidents: event_id=CMP-0051; kind=merchant_campaign; severity=Sev-3; window=2026-04-04 to 2026-04-10; success_impact_pp=-0.14; volume_impact_pct=56.15

Refs: enterprise_data/warehouse/transactions, RPT-D92-DAILY, enterprise_data/warehouse/reference/incidents.parquet
