---
id: RPT-D96-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 10 Apr 2026)

**Report ID:** RPT-D96-DAILY · **Day 96 of 206** · **Derived from:** 12,938 transaction rows queried live from the warehouse

## Summary

The rail took **12,938 payment attempts** on Friday 10 April 2026 (Working day) and settled **₹1.80 Cr** across 12,451 successful payments. Volume was +5.6% on yesterday and +0.4% on the same weekday last week. Success closed at **96.24%**, above the trailing 28-day median of 95.94%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 12,938 | +5.6% | +0.4% | 13,053 |
| Successful payments | 12,451 | +5.8% | +0.5% | 12,467 |
| Success rate | 96.24% | +0.17pp | +0.06pp | 95.49% |
| Settled value | ₹1.80 Cr | +13.4% | −2.0% | ₹1.70 Cr |
| Average ticket | ₹1,443 | +7.2% | −2.5% | ₹1,361 |
| Technical declines | 0.332% | −0.08pp | −0.03pp | 0.557% |
| Business declines | 3.007% | +0.12pp | +0.21pp | 2.981% |
| Risk declines | 0.085% | −0.04pp | −0.07pp | 0.141% |
| Timeout declines | 0.255% | −0.14pp | −0.10pp | 0.703% |
| Retry share | 1.08% | −0.06pp | +0.07pp | 1.66% |
| Latency p95 | 1,296 ms | +1.6% | +4.2% | 1,360 ms |
| Active customers | 10,728 | +4.8% | +0.5% | 10,777 |
| Active merchants | 1,377 | +1.3% | −1.4% | 1,392 |

## What moved

- Product UPI International is compounding — attempts up 39% across the trailing window to 146 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 36% across the trailing window to 1,101 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,713 | 36.4% | 95.52% | ₹52.39 L | +7.3% |
| UPI Person to Merchant | 3,286 | 25.4% | 96.38% | ₹32.75 L | −5.8% |
| UPI QR Payments | 2,240 | 17.3% | 96.43% | ₹11.39 L | +4.1% |
| UPI Lite | 1,101 | 8.5% | 99.18% | ₹1.09 L | +7.6% |
| RuPay Credit on UPI | 349 | 2.7% | 95.42% | ₹21.58 L | +37.9% |
| UPI AutoPay | 333 | 2.6% | 93.99% | ₹6.16 L | +4.2% |
| UPI Circle | 266 | 2.1% | 96.99% | ₹1.50 L | +13.2% |
| Credit on UPI | 248 | 1.9% | 96.37% | ₹22.44 L | +42.9% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,133 | 96.47% | 95.96% | ₹57.57 L | normal |
| HDFC Bank | 1,430 | 96.78% | 95.53% | ₹19.78 L | normal |
| Bank of Baroda | 966 | 95.24% | 95.94% | ₹15.59 L | normal |
| Union Bank of India | 903 | 95.90% | 95.82% | ₹13.34 L | normal |
| Punjab National Bank | 795 | 95.60% | 95.48% | ₹7.65 L | normal |
| ICICI Bank | 781 | 96.93% | 95.85% | ₹10.98 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 6,070 | 96.41% | 95.93% | ₹88.35 L | normal |
| Google Pay | 4,289 | 96.11% | 95.75% | ₹56.67 L | normal |
| Paytm | 1,087 | 95.95% | 96.03% | ₹14.25 L | normal |
| Navi | 484 | 96.69% | 95.77% | ₹7.39 L | normal |
| SuperMoney | 256 | 97.27% | 95.26% | ₹4.19 L | normal |
| BHIM | 139 | 98.56% | 96.28% | ₹1.80 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,427 | 96.59% | ₹49.53 L |
| Food & Beverage | 2,053 | 97.03% | ₹9.41 L |
| Mobility | 929 | 96.99% | ₹5.41 L |
| Bills | 741 | 96.49% | ₹8.01 L |
| Healthcare | 449 | 98.00% | ₹4.77 L |
| Digital | 209 | 93.78% | ₹97,358 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,850 | 29.8% | 96.36% | ₹50.87 L |
| North | 3,238 | 25.0% | 96.23% | ₹44.82 L |
| West | 3,170 | 24.5% | 96.09% | ₹48.40 L |
| East | 1,558 | 12.0% | 96.08% | ₹20.59 L |
| Central | 1,122 | 8.7% | 96.43% | ₹14.96 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 96.88% | ₹3.04 L |
| Vasant Wardrobe | Key Account | Retail | 80 | 95.00% | ₹1.75 L |
| Rapid Bazaar | Key Account | Retail | 327 | 96.94% | ₹1.64 L |
| Urban Boutique | Key Account | Retail | 106 | 96.23% | ₹1.27 L |
| Hampi Styles | Key Account | Retail | 30 | 96.67% | ₹85,450 |
| Ujjwal Water Board | Key Account | Bills | 42 | 95.24% | ₹79,145 |
| Yamuna Restaurant | Key Account | Food & Beverage | 74 | 95.95% | ₹73,704 |
| Hampi Stores 2298 | Key Account | Retail | 113 | 92.92% | ₹66,401 |

## Failure analysis

Of 476 declined attempts, 389 were business declines (3.007% of attempts — balances, PINs and limits), 43 technical (0.332%), 33 timeouts (0.255%) and 11 risk declines (0.085%).

140 attempts were re-presentations of an earlier failure (1.08% of the day); 65.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 168 | 1.299% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 128 | 0.989% | 1.022% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.271% | 0.220% |
| ZA | Transaction declined by customer | business | Customer | 32 | 0.247% | 0.358% |
| UX | Mandate execution outside permitted window | business | PSP | 19 | 0.147% | 0.075% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 18 | 0.139% | 0.166% |
| U30 | Debit failed at remitter bank | technical | Issuer | 16 | 0.124% | 0.191% |
| U28 | Remitter bank unavailable | technical | Issuer | 13 | 0.100% | 0.111% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 77 | 74 |
| Auto-reversals | 19 | 24 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹1.18 L | ₹1.47 L |

## Customer behaviour

10,728 distinct customers transacted (+4.7% on the 28-day median) at 1.21 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,196 | 3,673 | 1.15 | 95.94% | ₹1,574 |
| power | 2,362 | 3,203 | 1.36 | 96.32% | ₹1,951 |
| merchant_heavy | 2,411 | 2,893 | 1.20 | 96.75% | ₹1,096 |
| small_ticket | 1,670 | 2,030 | 1.22 | 96.45% | ₹677 |
| occasional | 868 | 906 | 1.04 | 95.47% | ₹1,290 |
| new | 201 | 213 | 1.06 | 93.90% | ₹936 |
| dormant_returning | 20 | 20 | 1.00 | 100.00% | ₹1,063 |

## Operational events

- **INC-FRAUD-0044** (Sev-1) — Fraud pattern on UPI QR Payments — Electronics, scoped to UPI_QR. Coordinated fraud attempts concentrated on UPI QR Payments at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **CMP-0051** (Sev-3) — Dining cashback campaign, scoped to 5812. A cashback campaign across Dining merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- None material today. No entity, code or flow breached its own 28-day band.

### Opportunities

- Product UPI International is compounding — attempts up 39% across the trailing window to 146 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Lite is compounding — attempts up 36% across the trailing window to 1,101 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

10 April was an incident day: INC-FRAUD-0044 was live and the rail closed at 96.24% success against a 95.94% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=12,938, successes=12,451, failed=476, pending=11, settled_value_inr=17,963,799.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0044; kind=fraud_spike; severity=Sev-1; window=2026-04-03 to 2026-04-10; success_impact_pp=-1.95; volume_impact_pct=16.79
- products: product_name=UPI International; attempts=146; window_growth_pct=38.7; success_rate=99.32
- products: product_name=UPI Lite; attempts=1,101; window_growth_pct=36.3; success_rate=99.18
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41
- incidents: event_id=CMP-0051; kind=merchant_campaign; severity=Sev-3; window=2026-04-04 to 2026-04-10; success_impact_pp=-0.14; volume_impact_pct=56.15
- categories: mcc_category=Travel; attempts=135; own_median=71; z=2.21

Refs: enterprise_data/warehouse/transactions, RPT-D95-DAILY, enterprise_data/warehouse/reference/incidents.parquet
