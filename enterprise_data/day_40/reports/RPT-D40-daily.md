---
id: RPT-D40-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-13T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 13 Feb 2026)

**Report ID:** RPT-D40-DAILY · **Day 40 of 206** · **Derived from:** 10,152 transaction rows queried live from the warehouse

## Summary

The rail took **10,152 payment attempts** on Friday 13 February 2026 (Working day) and settled **₹1.14 Cr** across 9,681 successful payments. Volume was +2.3% on yesterday and −16.7% on the same weekday last week. Success closed at **95.36%**, in line with the trailing 28-day median of 95.35%.

16 disputes were raised, 8.1 sigma above the trailing median of 4.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,152 | +2.3% | −16.7% | 10,911 |
| Successful payments | 9,681 | +2.4% | −17.2% | 10,402 |
| Success rate | 95.36% | +0.01pp | −0.57pp | 95.27% |
| Settled value | ₹1.14 Cr | +6.9% | −19.3% | ₹1.24 Cr |
| Average ticket | ₹1,177 | +4.4% | −2.5% | ₹1,189 |
| Technical declines | 0.374% | −0.02pp | +0.04pp | 0.439% |
| Business declines | 3.753% | −0.03pp | +0.53pp | 3.563% |
| Risk declines | 0.118% | −0.01pp | −0.05pp | 0.144% |
| Timeout declines | 0.296% | +0.05pp | +0.03pp | 0.458% |
| Retry share | 1.39% | +0.08pp | +0.20pp | 1.56% |
| Latency p95 | 1,252 ms | +3.2% | −0.6% | 1,301 ms |
| Active customers | 8,667 | +1.9% | −14.6% | 9,188 |
| Active merchants | 1,227 | −0.4% | −6.6% | 1,258 |

## What moved

- Product UPI Lite is compounding — attempts up 32% across the trailing window to 649 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 3,864 | 38.1% | 94.75% | ₹42.12 L | −0.5% |
| UPI Person to Merchant | 2,890 | 28.5% | 95.78% | ₹25.70 L | −6.8% |
| UPI QR Payments | 1,662 | 16.4% | 95.97% | ₹7.96 L | −0.0% |
| UPI Lite | 649 | 6.4% | 98.92% | ₹56,734 | −10.5% |
| UPI AutoPay | 295 | 2.9% | 87.12% | ₹5.51 L | −2.3% |
| RuPay Credit on UPI | 235 | 2.3% | 95.74% | ₹12.14 L | +16.9% |
| Credit on UPI | 152 | 1.5% | 98.03% | ₹6.86 L | +4.8% |
| UPI Circle | 100 | 1.0% | 98.00% | ₹1.21 L | −2.4% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,258 | 94.48% | 95.39% | ₹35.22 L | normal |
| HDFC Bank | 1,089 | 96.24% | 95.80% | ₹12.55 L | normal |
| Bank of Baroda | 761 | 95.53% | 94.99% | ₹8.14 L | normal |
| Union Bank of India | 737 | 96.61% | 94.67% | ₹7.24 L | normal |
| ICICI Bank | 632 | 96.99% | 96.29% | ₹7.08 L | normal |
| Axis Bank | 604 | 94.04% | 95.13% | ₹7.00 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 4,761 | 95.15% | 95.22% | ₹51.56 L | normal |
| Google Pay | 3,372 | 95.58% | 95.45% | ₹39.07 L | normal |
| Paytm | 842 | 94.77% | 94.89% | ₹10.08 L | normal |
| Navi | 375 | 94.13% | 95.59% | ₹4.30 L | normal |
| SuperMoney | 193 | 96.89% | 95.88% | ₹2.03 L | normal |
| YONO SBI | 101 | 95.05% | 95.62% | ₹97,551 | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,696 | 95.99% | ₹25.35 L |
| Food & Beverage | 1,466 | 96.73% | ₹7.81 L |
| Mobility | 682 | 97.07% | ₹4.54 L |
| Bills | 604 | 95.70% | ₹6.97 L |
| Healthcare | 329 | 95.14% | ₹1.99 L |
| Digital | 185 | 92.97% | ₹1.46 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,008 | 29.6% | 95.48% | ₹35.35 L |
| North | 2,555 | 25.2% | 95.46% | ₹27.00 L |
| West | 2,483 | 24.5% | 94.97% | ₹29.12 L |
| East | 1,225 | 12.1% | 95.43% | ₹14.19 L |
| Central | 881 | 8.7% | 95.69% | ₹8.30 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 301 | 95.68% | ₹1.40 L |
| Ujjwal Water Board | Key Account | Bills | 32 | 84.38% | ₹1.32 L |
| Vasant Wardrobe | Key Account | Retail | 60 | 95.00% | ₹1.21 L |
| Hampi Stores 2298 | Key Account | Retail | 88 | 98.86% | ₹93,511 |
| Yamuna Restaurant | Key Account | Food & Beverage | 57 | 98.25% | ₹64,398 |
| Urban Boutique | Key Account | Retail | 88 | 95.45% | ₹56,305 |
| Girnar Connect | Key Account | Bills | 106 | 97.17% | ₹53,417 |
| Vega Electronics | Large | Retail | 24 | 91.67% | ₹50,705 |

## Failure analysis

Of 461 declined attempts, 381 were business declines (3.753% of attempts — balances, PINs and limits), 38 technical (0.374%), 30 timeouts (0.296%) and 12 risk declines (0.118%).

141 attempts were re-presentations of an earlier failure (1.39% of the day); 51.1% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 151 | 1.487% | 1.491% |
| ZM | Invalid UPI PIN | business | Customer | 145 | 1.428% | 1.194% |
| ZA | Transaction declined by customer | business | Customer | 42 | 0.414% | 0.428% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.276% | 0.233% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 17 | 0.167% | 0.159% |
| U30 | Debit failed at remitter bank | technical | Issuer | 15 | 0.148% | 0.224% |
| U28 | Remitter bank unavailable | technical | Issuer | 12 | 0.118% | 0.144% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 11 | 0.108% | 0.117% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 79 | 70 |
| Auto-reversals | 15 | 21 |
| Disputes / chargebacks | 16 | 4 |
| Value returned | ₹87,841 | ₹1.16 L |

## Customer behaviour

8,667 distinct customers transacted (−2.2% on the 28-day median) at 1.17 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,626 | 2,924 | 1.11 | 95.04% | ₹1,267 |
| power | 1,849 | 2,380 | 1.29 | 95.42% | ₹1,535 |
| merchant_heavy | 1,931 | 2,276 | 1.18 | 95.43% | ₹925 |
| small_ticket | 1,376 | 1,639 | 1.19 | 96.28% | ₹544 |
| occasional | 704 | 735 | 1.04 | 93.61% | ₹1,211 |
| new | 156 | 172 | 1.10 | 97.09% | ₹792 |
| dormant_returning | 25 | 26 | 1.04 | 100.00% | ₹614 |

## Operational events

- **INC-FRAUD-0048** (Sev-1) — Fraud pattern on Credit on UPI — Footwear, scoped to UPI_CREDIT_LINE. Coordinated fraud attempts concentrated on Credit on UPI at Footwear merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **INC-BANK-0004** (Sev-2) — State Bank of India issuer decline spike, scoped to State Bank of India between 01:00 and 08:00. State Bank of India core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **ONBRD-0090** (Sev-3) — Fuel acquirer onboarding drive, scoped to 5541. An acquiring push signed a cohort of new Fuel merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.

## Risks and opportunities

### Risks

- 16 disputes were raised, 8.1 sigma above the trailing median of 4.

### Opportunities

- Product UPI Lite is compounding — attempts up 32% across the trailing window to 649 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

13 February was an incident day: INC-FRAUD-0048, INC-BANK-0004 were live and the rail closed at 95.36% success against a 95.35% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-02-13` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,152, successes=9,681, failed=461, pending=10, settled_value_inr=11,396,927.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- adjustments: chargebacks=16; trailing_median=4; z=8.09
- incidents: event_id=INC-FRAUD-0048; kind=fraud_spike; severity=Sev-1; window=2026-02-13 to 2026-02-24; success_impact_pp=-1.76; volume_impact_pct=11.4
- incidents: event_id=INC-BANK-0004; kind=bank_outage; severity=Sev-2; window=2026-02-13 to 2026-02-13; success_impact_pp=-13.87; volume_impact_pct=-12.3
- products: product_name=UPI Lite; attempts=649; window_growth_pct=32.1; success_rate=98.92
- incidents: event_id=ONBRD-0090; kind=merchant_onboarding; severity=Sev-3; window=2026-01-25 to 2026-02-22; success_impact_pp=-0.98; volume_impact_pct=23.24
- categories: mcc_category=Financial Services; attempts=151; own_median=132.5; z=2.5

Refs: enterprise_data/warehouse/transactions, RPT-D39-DAILY, enterprise_data/warehouse/reference/incidents.parquet
