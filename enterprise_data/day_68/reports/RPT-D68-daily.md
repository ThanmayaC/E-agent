---
id: RPT-D68-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-13T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 13 Mar 2026)

**Report ID:** RPT-D68-DAILY · **Day 68 of 206** · **Derived from:** 11,911 transaction rows queried live from the warehouse

## Summary

The rail took **11,911 payment attempts** on Friday 13 March 2026 (Working day) and settled **₹1.41 Cr** across 11,396 successful payments. Volume was +10.4% on yesterday and −10.5% on the same weekday last week. Success closed at **95.68%**, in line with the trailing 28-day median of 95.62%.

Product UPI Circle is compounding — attempts up 71% across the trailing window to 239 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,911 | +10.4% | −10.5% | 13,015 |
| Successful payments | 11,396 | +10.9% | −10.9% | 12,466 |
| Success rate | 95.68% | +0.45pp | −0.45pp | 95.76% |
| Settled value | ₹1.41 Cr | +11.7% | −15.8% | ₹1.49 Cr |
| Average ticket | ₹1,239 | +0.8% | −5.6% | ₹1,203 |
| Technical declines | 0.487% | −0.02pp | +0.07pp | 0.458% |
| Business declines | 3.283% | −0.33pp | +0.26pp | 3.211% |
| Risk declines | 0.143% | −0.03pp | +0.05pp | 0.121% |
| Timeout declines | 0.369% | +0.02pp | +0.15pp | 0.355% |
| Retry share | 1.06% | −0.93pp | +0.10pp | 1.30% |
| Latency p95 | 1,234 ms | −5.6% | −1.5% | 1,253 ms |
| Active customers | 9,963 | +8.6% | −8.9% | 10,706 |
| Active merchants | 1,329 | +3.0% | −3.6% | 1,333 |

## What moved

- Product UPI Circle is compounding — attempts up 71% across the trailing window to 239 today, with success holding, so the growth is healthy and worth funding.
- Product UPI International is compounding — attempts up 48% across the trailing window to 101 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Category Mobility ran at 98.01% success on 755 attempts (10.0% of the day), 1.20pp up its own 28-day median.
- Product UPI QR Payments ran at 97.56% success on 2,010 attempts (16.9% of the day), 1.12pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,389 | 36.8% | 94.71% | ₹48.58 L | +6.9% |
| UPI Person to Merchant | 3,384 | 28.4% | 95.74% | ₹29.57 L | +5.8% |
| UPI QR Payments | 2,010 | 16.9% | 97.56% | ₹8.63 L | +1.5% |
| UPI Lite | 792 | 6.6% | 98.61% | ₹73,654 | +4.2% |
| UPI AutoPay | 320 | 2.7% | 89.38% | ₹5.15 L | +5.6% |
| RuPay Credit on UPI | 251 | 2.1% | 96.41% | ₹13.15 L | +14.6% |
| UPI Circle | 239 | 2.0% | 96.23% | ₹2.34 L | +70.1% |
| Credit on UPI | 168 | 1.4% | 94.64% | ₹10.49 L | +11.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,665 | 96.26% | 95.56% | ₹40.04 L | normal |
| HDFC Bank | 1,378 | 94.99% | 96.23% | ₹16.23 L | ⚠ outlier |
| Bank of Baroda | 948 | 96.52% | 95.53% | ₹11.37 L | normal |
| Union Bank of India | 858 | 95.80% | 95.26% | ₹13.23 L | normal |
| Punjab National Bank | 795 | 94.47% | 95.03% | ₹8.32 L | normal |
| ICICI Bank | 723 | 96.54% | 95.85% | ₹10.03 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,623 | 96.32% | 95.66% | ₹66.67 L | normal |
| Google Pay | 3,891 | 95.07% | 95.67% | ₹45.91 L | normal |
| Paytm | 977 | 96.01% | 95.36% | ₹9.88 L | normal |
| Navi | 439 | 93.85% | 95.49% | ₹6.28 L | normal |
| SuperMoney | 239 | 96.23% | 95.88% | ₹4.21 L | normal |
| BHIM | 126 | 92.86% | 95.53% | ₹2.01 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,297 | 96.42% | ₹32.79 L |
| Food & Beverage | 1,786 | 96.75% | ₹8.96 L |
| Mobility | 755 | 98.01% | ₹5.84 L |
| Bills | 706 | 96.60% | ₹8.12 L |
| Healthcare | 378 | 96.30% | ₹6.51 L |
| Digital | 246 | 91.87% | ₹1.09 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,588 | 30.1% | 96.01% | ₹42.21 L |
| North | 3,014 | 25.3% | 96.08% | ₹38.81 L |
| West | 2,913 | 24.5% | 95.40% | ₹34.33 L |
| East | 1,353 | 11.4% | 94.53% | ₹15.53 L |
| Central | 1,043 | 8.8% | 95.59% | ₹10.34 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 32 | 90.62% | ₹1.85 L |
| Rapid Bazaar | Key Account | Retail | 362 | 97.24% | ₹1.23 L |
| Vasant Wardrobe | Key Account | Retail | 68 | 97.06% | ₹1.03 L |
| Aravalli Pharmacy | Large | Healthcare | 71 | 91.55% | ₹92,661 |
| Ujjwal Water Board | Key Account | Bills | 40 | 100.00% | ₹75,883 |
| Yamuna Restaurant | Key Account | Food & Beverage | 62 | 96.77% | ₹74,665 |
| Urban Boutique | Key Account | Retail | 109 | 98.17% | ₹70,128 |
| Hampi Stores 2298 | Key Account | Retail | 97 | 98.97% | ₹64,964 |

## Failure analysis

Of 510 declined attempts, 391 were business declines (3.283% of attempts — balances, PINs and limits), 58 technical (0.487%), 44 timeouts (0.369%) and 17 risk declines (0.143%).

126 attempts were re-presentations of an earlier failure (1.06% of the day); 58.7% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 154 | 1.293% | 1.413% |
| ZM | Invalid UPI PIN | business | Customer | 148 | 1.243% | 1.101% |
| ZA | Transaction declined by customer | business | Customer | 38 | 0.319% | 0.406% |
| XH | Account does not exist / frozen | business | Issuer | 27 | 0.227% | 0.248% |
| U30 | Debit failed at remitter bank | technical | Issuer | 23 | 0.193% | 0.165% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 22 | 0.185% | 0.167% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 18 | 0.151% | 0.108% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.134% | 0.095% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 78 | 68 |
| Auto-reversals | 28 | 20 |
| Disputes / chargebacks | 11 | 10 |
| Value returned | ₹79,192 | ₹89,740 |

## Customer behaviour

9,963 distinct customers transacted (+7.1% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,048 | 3,501 | 1.15 | 95.92% | ₹1,368 |
| power | 2,094 | 2,799 | 1.34 | 95.21% | ₹1,560 |
| merchant_heavy | 2,243 | 2,668 | 1.19 | 95.80% | ₹961 |
| small_ticket | 1,523 | 1,826 | 1.20 | 96.11% | ₹556 |
| occasional | 811 | 855 | 1.05 | 94.97% | ₹1,290 |
| new | 218 | 235 | 1.08 | 95.74% | ₹764 |
| dormant_returning | 26 | 27 | 1.04 | 92.59% | ₹3,912 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0065** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI International is compounding — attempts up 48% across the trailing window to 101 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Issuer HDFC Bank ran at 94.99% success on 1,378 attempts (11.6% of the day), 1.24pp down its own 28-day median.
- Issuer IDFC First Bank ran at 93.48% success on 322 attempts (2.7% of the day), 2.22pp down its own 28-day median.
- Issuer Indian Bank ran at 92.93% success on 368 attempts (3.1% of the day), 2.54pp down its own 28-day median.

### Opportunities

- Product UPI Circle is compounding — attempts up 71% across the trailing window to 239 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

13 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.68% success against a 95.62% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-13` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,911, successes=11,396, failed=510, pending=5, settled_value_inr=14,121,840.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI Circle; attempts=239; window_growth_pct=71; success_rate=96.23
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI International; attempts=101; window_growth_pct=47.5; success_rate=92.08
- categories: mcc_category=Mobility; attempts=755; success_rate=98.01; own_median=96.81; z=3.3
- products: product_name=UPI QR Payments; attempts=2,010; success_rate=97.56; own_median=96.44; z=2.25
- banks: payer_bank=HDFC Bank; attempts=1,378; success_rate=94.99; own_median=96.23; z=-2.13
- banks: payer_bank=IDFC First Bank; attempts=322; success_rate=93.48; own_median=95.7; z=-3.27
- banks: payer_bank=Indian Bank; attempts=368; success_rate=92.93; own_median=95.48; z=-2.23
- incidents: event_id=ONBRD-0088; kind=merchant_onboarding; severity=Sev-3; window=2026-03-08 to 2026-03-25; success_impact_pp=-1.01; volume_impact_pct=29.04
- incidents: event_id=CMP-0065; kind=merchant_campaign; severity=Sev-3; window=2026-03-10 to 2026-03-15; success_impact_pp=-0.19; volume_impact_pct=76.56

Refs: enterprise_data/warehouse/transactions, RPT-D67-DAILY, enterprise_data/warehouse/reference/incidents.parquet
