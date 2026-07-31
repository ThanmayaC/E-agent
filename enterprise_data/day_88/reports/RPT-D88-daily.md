---
id: RPT-D88-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-02T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 02 Apr 2026)

**Report ID:** RPT-D88-DAILY · **Day 88 of 206** · **Derived from:** 11,949 transaction rows queried live from the warehouse

## Summary

The rail took **11,949 payment attempts** on Thursday 02 April 2026 (Working day) and settled **₹1.62 Cr** across 11,475 successful payments. Volume was −9.6% on yesterday and +16.2% on the same weekday last week. Success closed at **96.03%**, in line with the trailing 28-day median of 95.83%.

Category Bills carried 1,328 attempts, 91% up its trailing median and 16.7% of the day's volume. Product Credit on UPI is compounding — attempts up 48% across the trailing window to 177 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,949 | −9.6% | +16.2% | 12,582 |
| Successful payments | 11,475 | −9.5% | +23.9% | 12,080 |
| Success rate | 96.03% | +0.03pp | +5.92pp | 96.02% |
| Settled value | ₹1.62 Cr | −7.7% | +26.2% | ₹1.69 Cr |
| Average ticket | ₹1,411 | +2.0% | +1.9% | ₹1,397 |
| Technical declines | 0.435% | +0.00pp | −1.23pp | 0.433% |
| Business declines | 3.046% | +0.08pp | −1.06pp | 3.006% |
| Risk declines | 0.126% | −0.00pp | −0.04pp | 0.127% |
| Timeout declines | 0.268% | −0.09pp | −3.51pp | 0.312% |
| Retry share | 1.14% | −0.21pp | −3.74pp | 1.24% |
| Latency p95 | 1,290 ms | +0.7% | −44.1% | 1,285 ms |
| Active customers | 10,036 | −8.3% | +18.3% | 10,492 |
| Active merchants | 1,349 | −3.2% | +6.2% | 1,372 |

## What moved

- Category Bills carried 1,328 attempts, 91% up its trailing median and 16.7% of the day's volume.
- Product Credit on UPI is compounding — attempts up 48% across the trailing window to 177 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 30% across the trailing window to 271 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,995 | 33.4% | 95.42% | ₹44.05 L | −8.9% |
| UPI Person to Merchant | 3,381 | 28.3% | 96.18% | ₹38.16 L | −2.3% |
| UPI QR Payments | 2,037 | 17.0% | 96.42% | ₹10.30 L | −4.3% |
| UPI Lite | 1,126 | 9.4% | 99.20% | ₹99,137 | +21.9% |
| UPI AutoPay | 325 | 2.7% | 91.69% | ₹6.14 L | +2.7% |
| RuPay Credit on UPI | 289 | 2.4% | 94.81% | ₹20.31 L | +17.0% |
| UPI Circle | 271 | 2.3% | 96.31% | ₹2.45 L | +35.2% |
| Credit on UPI | 177 | 1.5% | 94.92% | ₹11.74 L | +7.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,748 | 96.61% | 95.82% | ₹51.50 L | normal |
| HDFC Bank | 1,320 | 95.45% | 95.59% | ₹16.84 L | normal |
| Bank of Baroda | 947 | 97.04% | 95.94% | ₹10.01 L | normal |
| Union Bank of India | 864 | 95.49% | 95.79% | ₹11.82 L | normal |
| Punjab National Bank | 738 | 94.44% | 95.23% | ₹9.22 L | normal |
| ICICI Bank | 704 | 97.02% | 95.86% | ₹11.23 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,567 | 95.99% | 95.88% | ₹68.47 L | normal |
| Google Pay | 3,990 | 96.12% | 95.76% | ₹57.76 L | normal |
| Paytm | 1,035 | 96.43% | 95.97% | ₹17.21 L | normal |
| Navi | 450 | 94.22% | 95.74% | ₹6.68 L | normal |
| SuperMoney | 237 | 94.94% | 95.09% | ₹3.34 L | normal |
| BHIM | 116 | 98.28% | 95.72% | ₹1.35 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,902 | 96.80% | ₹33.44 L |
| Food & Beverage | 1,798 | 96.44% | ₹9.54 L |
| Bills | 1,328 | 95.56% | ₹15.90 L |
| Mobility | 882 | 96.49% | ₹6.59 L |
| Healthcare | 381 | 97.38% | ₹2.86 L |
| Digital | 266 | 95.86% | ₹1.64 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,542 | 29.6% | 96.30% | ₹49.95 L |
| North | 2,966 | 24.8% | 95.82% | ₹37.43 L |
| West | 2,966 | 24.8% | 96.16% | ₹40.72 L |
| East | 1,431 | 12.0% | 95.39% | ₹21.19 L |
| Central | 1,044 | 8.7% | 96.26% | ₹12.64 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 28 | 92.86% | ₹3.01 L |
| Rapid Bazaar | Key Account | Retail | 313 | 98.08% | ₹1.73 L |
| Vasant Wardrobe | Key Account | Retail | 64 | 92.19% | ₹1.72 L |
| Ujjwal Water Board | Key Account | Bills | 61 | 93.44% | ₹1.60 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 51 | 96.08% | ₹1.14 L |
| Girnar Connect | Key Account | Bills | 227 | 97.36% | ₹99,260 |
| Tejas Restaurant | Large | Food & Beverage | 27 | 100.00% | ₹51,630 |
| Hampi Stores 2298 | Key Account | Retail | 76 | 96.05% | ₹50,975 |

## Failure analysis

Of 463 declined attempts, 364 were business declines (3.046% of attempts — balances, PINs and limits), 52 technical (0.435%), 32 timeouts (0.268%) and 15 risk declines (0.126%).

136 attempts were re-presentations of an earlier failure (1.14% of the day); 69.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 145 | 1.213% | 1.341% |
| ZM | Invalid UPI PIN | business | Customer | 121 | 1.013% | 1.081% |
| ZA | Transaction declined by customer | business | Customer | 47 | 0.393% | 0.364% |
| XH | Account does not exist / frozen | business | Issuer | 31 | 0.259% | 0.224% |
| U30 | Debit failed at remitter bank | technical | Issuer | 29 | 0.243% | 0.189% |
| ZX | Mandate not found or revoked | business | PSP | 14 | 0.117% | 0.083% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 14 | 0.117% | 0.107% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 13 | 0.109% | 0.101% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 75 | 78 |
| Auto-reversals | 20 | 24 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹1.92 L | ₹1.32 L |

## Customer behaviour

10,036 distinct customers transacted (+0.9% on the 28-day median) at 1.19 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,073 | 3,499 | 1.14 | 96.63% | ₹1,477 |
| power | 2,135 | 2,824 | 1.32 | 95.82% | ₹1,770 |
| merchant_heavy | 2,280 | 2,713 | 1.19 | 95.76% | ₹1,119 |
| small_ticket | 1,529 | 1,846 | 1.21 | 95.83% | ₹631 |
| occasional | 802 | 839 | 1.05 | 95.35% | ₹1,879 |
| new | 192 | 203 | 1.06 | 97.54% | ₹1,141 |
| dormant_returning | 25 | 25 | 1.00 | 92.00% | ₹739 |

## Operational events

- **INC-PSP-0028** (Sev-3) — Axis Mobile app release regression, scoped to Axis Mobile between 19:00 and 23:00. A Axis Mobile client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **DORM-0073** (Sev-3) — South region customer dormancy wave, scoped to South. A cohort of South-region customers went inactive after a competing wallet promotion. Per-customer transaction frequency fell without any success-rate degradation — a demand problem, not a reliability one.
- **ADOPT-0076** (Sev-3) — Upi Autopay onboarding push, scoped to UPI_AUTOPAY. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.
- **MKT-0078** (Sev-3) — Discretionary spend correction, scoped to UPI_CREDIT_LINE,RUPAY_CREDIT,UPI_P2M,UPI_INTL. A broad pull-back in discretionary spending compressed credit-funded and high-ticket merchant volume while essential categories held flat.
- **REG-0068** (Sev-3) — UPI Lite per-transaction cap raised to ₹1,000, scoped to UPI_LITE. The Lite per-transaction cap was raised, moving a band of small-ticket payments off the full UPI rail onto Lite. Lite volume steps up permanently and average ticket rises.

## Risks and opportunities

### Risks

- Issuer Indian Bank ran at 92.47% success on 372 attempts (3.1% of the day), 2.90pp down its own 28-day median.

### Opportunities

- Product Credit on UPI is compounding — attempts up 48% across the trailing window to 177 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 30% across the trailing window to 271 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

02 April ran on trend at 96.03% success and ₹1.62 Cr settled. The movement worth carrying forward is in merchant categories: category Bills carried 1,328 attempts, 91% up its trailing median and 16.7% of the day's volume. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-02` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,949, successes=11,475, failed=463, pending=11, settled_value_inr=16,193,009.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- categories: mcc_category=Bills; attempts=1,328; own_median=694.5; z=7.12
- products: product_name=Credit on UPI; attempts=177; window_growth_pct=48.5; success_rate=94.92
- products: product_name=UPI Circle; attempts=271; window_growth_pct=30.4; success_rate=96.31
- incidents: event_id=INC-PSP-0028; kind=psp_degradation; severity=Sev-3; window=2026-04-02 to 2026-04-05; success_impact_pp=-3.75; volume_impact_pct=-5.87
- banks: payer_bank=Indian Bank; attempts=372; success_rate=92.47; own_median=95.38; z=-2.21
- incidents: event_id=DORM-0073; kind=dormancy_wave; severity=Sev-3; window=2026-03-16 to 2026-04-04; success_impact_pp=0.05; volume_impact_pct=-18.31
- incidents: event_id=ADOPT-0076; kind=adoption_surge; severity=Sev-3; window=2026-03-30 to 2026-04-12; success_impact_pp=-0.35; volume_impact_pct=37.98
- incidents: event_id=MKT-0078; kind=market_correction; severity=Sev-3; window=2026-03-31 to 2026-04-10; success_impact_pp=-0.15; volume_impact_pct=-10.41
- incidents: event_id=REG-0068; kind=regulatory_change; severity=Sev-3; window=2026-04-01 to 2026-07-29; success_impact_pp=0.18; volume_impact_pct=26
- categories: mcc_category=Travel; attempts=111; own_median=67.5; z=2.93

Refs: enterprise_data/warehouse/transactions, RPT-D87-DAILY, enterprise_data/warehouse/reference/incidents.parquet
