---
id: RPT-D94-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-08T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 08 Apr 2026)

**Report ID:** RPT-D94-DAILY · **Day 94 of 206** · **Derived from:** 13,485 transaction rows queried live from the warehouse

## Summary

The rail took **13,485 payment attempts** on Wednesday 08 April 2026 (Working day) and settled **₹1.76 Cr** across 12,942 successful payments. Volume was +4.2% on yesterday and +2.1% on the same weekday last week. Success closed at **95.97%**, in line with the trailing 28-day median of 95.84%.

Product UPI Lite is compounding — attempts up 52% across the trailing window to 1,160 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 13,485 | +4.2% | +2.1% | 13,168 |
| Successful payments | 12,942 | +4.3% | +2.0% | 12,557 |
| Success rate | 95.97% | +0.04pp | −0.03pp | 95.33% |
| Settled value | ₹1.76 Cr | +3.8% | +0.5% | ₹1.70 Cr |
| Average ticket | ₹1,362 | −0.5% | −1.5% | ₹1,353 |
| Technical declines | 0.556% | +0.18pp | +0.12pp | 0.603% |
| Business declines | 2.877% | −0.11pp | −0.09pp | 2.990% |
| Risk declines | 0.104% | −0.03pp | −0.02pp | 0.151% |
| Timeout declines | 0.378% | −0.06pp | +0.02pp | 0.797% |
| Retry share | 1.23% | +0.01pp | −0.12pp | 1.80% |
| Latency p95 | 1,256 ms | −1.6% | −2.0% | 1,379 ms |
| Active customers | 11,128 | +3.7% | +1.6% | 10,851 |
| Active merchants | 1,392 | −1.6% | −0.1% | 1,398 |

## What moved

- Product UPI Lite is compounding — attempts up 52% across the trailing window to 1,160 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Circle is compounding — attempts up 39% across the trailing window to 256 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,809 | 35.7% | 95.57% | ₹51.50 L | +10.0% |
| UPI Person to Merchant | 3,549 | 26.3% | 96.03% | ₹36.77 L | +2.0% |
| UPI QR Payments | 2,470 | 18.3% | 96.72% | ₹10.49 L | +18.7% |
| UPI Lite | 1,160 | 8.6% | 97.93% | ₹1.08 L | +16.9% |
| RuPay Credit on UPI | 317 | 2.4% | 95.58% | ₹21.73 L | +25.3% |
| UPI AutoPay | 307 | 2.3% | 91.86% | ₹6.05 L | −4.1% |
| UPI Circle | 256 | 1.9% | 95.70% | ₹2.15 L | +12.5% |
| Credit on UPI | 217 | 1.6% | 94.01% | ₹19.31 L | +27.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,257 | 95.94% | 95.92% | ₹48.41 L | normal |
| HDFC Bank | 1,440 | 96.25% | 95.46% | ₹18.85 L | normal |
| Bank of Baroda | 1,052 | 95.82% | 96.02% | ₹13.38 L | normal |
| Union Bank of India | 973 | 94.45% | 95.69% | ₹11.44 L | normal |
| Punjab National Bank | 849 | 95.88% | 95.41% | ₹16.16 L | normal |
| Axis Bank | 836 | 96.17% | 95.78% | ₹12.71 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,290 | 96.10% | 95.82% | ₹84.13 L | normal |
| Google Pay | 4,566 | 95.55% | 95.68% | ₹57.47 L | normal |
| Paytm | 1,105 | 95.84% | 95.97% | ₹15.52 L | normal |
| Navi | 471 | 97.03% | 95.67% | ₹8.42 L | normal |
| SuperMoney | 267 | 98.50% | 94.95% | ₹2.51 L | normal |
| BHIM | 144 | 97.22% | 96.28% | ₹1.32 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,563 | 96.38% | ₹45.45 L |
| Food & Beverage | 2,333 | 96.40% | ₹11.98 L |
| Mobility | 985 | 97.46% | ₹5.39 L |
| Bills | 788 | 94.67% | ₹7.28 L |
| Healthcare | 433 | 95.15% | ₹3.22 L |
| Digital | 186 | 95.16% | ₹1.07 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,938 | 29.2% | 96.47% | ₹46.29 L |
| North | 3,383 | 25.1% | 95.63% | ₹51.82 L |
| West | 3,335 | 24.7% | 95.77% | ₹45.21 L |
| East | 1,616 | 12.0% | 95.67% | ₹20.60 L |
| Central | 1,213 | 9.0% | 96.29% | ₹12.42 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹1.99 L |
| Vasant Wardrobe | Key Account | Retail | 74 | 98.65% | ₹1.85 L |
| Rapid Bazaar | Key Account | Retail | 362 | 97.51% | ₹1.42 L |
| Hampi Stores 2298 | Key Account | Retail | 109 | 97.25% | ₹1.20 L |
| Urban Boutique | Key Account | Retail | 96 | 94.79% | ₹1.18 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 78 | 94.87% | ₹1.05 L |
| Tejas Restaurant | Large | Food & Beverage | 32 | 100.00% | ₹66,002 |
| Aravalli Pharmacy | Large | Healthcare | 77 | 98.70% | ₹63,700 |

## Failure analysis

Of 528 declined attempts, 388 were business declines (2.877% of attempts — balances, PINs and limits), 75 technical (0.556%), 51 timeouts (0.378%) and 14 risk declines (0.104%).

166 attempts were re-presentations of an earlier failure (1.23% of the day); 71.7% of them succeeded.

- Decline code U69 (Beneficiary bank offline) fired 22 times — 0.163% of attempts against a trailing 0.072%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 22 times — 0.163% of attempts against a trailing 0.103%. Owner: NPCI.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 178 | 1.320% | 1.332% |
| ZM | Invalid UPI PIN | business | Customer | 126 | 0.934% | 1.056% |
| ZA | Transaction declined by customer | business | Customer | 42 | 0.311% | 0.360% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.185% | 0.191% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.171% | 0.169% |
| XH | Account does not exist / frozen | business | Issuer | 22 | 0.163% | 0.221% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 22 | 0.163% | 0.103% |
| U69 | Beneficiary bank offline | technical | Issuer | 22 | 0.163% | 0.072% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 70 | 76 |
| Auto-reversals | 30 | 24 |
| Disputes / chargebacks | 7 | 10 |
| Value returned | ₹1.48 L | ₹1.53 L |

## Customer behaviour

11,128 distinct customers transacted (+9.1% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,420 | 3,933 | 1.15 | 96.34% | ₹1,541 |
| power | 2,374 | 3,221 | 1.36 | 96.18% | ₹1,596 |
| merchant_heavy | 2,454 | 2,955 | 1.20 | 96.14% | ₹1,260 |
| small_ticket | 1,699 | 2,117 | 1.25 | 95.37% | ₹509 |
| occasional | 904 | 962 | 1.06 | 94.70% | ₹1,465 |
| new | 247 | 266 | 1.08 | 95.49% | ₹776 |
| dormant_returning | 30 | 31 | 1.03 | 96.77% | ₹601 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI Lite is compounding — attempts up 52% across the trailing window to 1,160 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code U69 (Beneficiary bank offline) fired 22 times — 0.163% of attempts against a trailing 0.072%. Owner: Issuer.
- Product UPI Circle is compounding — attempts up 39% across the trailing window to 256 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code BT (Acquirer / NPCI switch timeout) fired 22 times — 0.163% of attempts against a trailing 0.103%. Owner: NPCI.
- Product UPI Lite ran at 97.93% success on 1,160 attempts (8.6% of the day), 0.89pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

08 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 95.97% success against a 95.84% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-08` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=13,485, successes=12,942, failed=528, pending=15, settled_value_inr=17,633,326.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- products: product_name=UPI Lite; attempts=1,160; window_growth_pct=52.4; success_rate=97.93
- failures: failure_code=U69; count=22; rate_pct=0.16; trailing_rate_pct=0.07; owner=Issuer; z=3.75
- products: product_name=UPI Circle; attempts=256; window_growth_pct=38.9; success_rate=95.7
- failures: failure_code=BT; count=22; rate_pct=0.16; trailing_rate_pct=0.1; owner=NPCI; z=2.85
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- products: product_name=UPI Lite; attempts=1,160; success_rate=97.93; own_median=98.82; z=-2.37
- banks: payer_bank=Kotak Mahindra Bank; attempts=490; success_rate=98.16; own_median=95.75; z=2.26
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41

Refs: enterprise_data/warehouse/transactions, RPT-D93-DAILY, enterprise_data/warehouse/reference/incidents.parquet
