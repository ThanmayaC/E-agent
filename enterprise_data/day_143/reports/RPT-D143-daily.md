---
id: RPT-D143-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Wednesday, 27 May 2026)

**Report ID:** RPT-D143-DAILY · **Day 143 of 206** · **Derived from:** 15,372 transaction rows queried live from the warehouse

## Summary

The rail took **15,372 payment attempts** on Wednesday 27 May 2026 (Bakrid / Eid al-Adha) and settled **₹1.96 Cr** across 14,770 successful payments. Volume was +4.9% on yesterday and +9.2% on the same weekday last week. Success closed at **96.08%**, in line with the trailing 28-day median of 96.07%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 15,372 | +4.9% | +9.2% | 14,818 |
| Successful payments | 14,770 | +4.9% | +9.1% | 14,216 |
| Success rate | 96.08% | +0.00pp | −0.09pp | 95.93% |
| Settled value | ₹1.96 Cr | +9.5% | +4.2% | ₹1.97 Cr |
| Average ticket | ₹1,327 | +4.3% | −4.5% | ₹1,386 |
| Technical declines | 0.520% | +0.03pp | +0.16pp | 0.509% |
| Business declines | 2.914% | +0.04pp | −0.03pp | 2.931% |
| Risk declines | 0.104% | −0.03pp | −0.05pp | 0.128% |
| Timeout declines | 0.332% | +0.05pp | +0.08pp | 0.396% |
| Retry share | 1.30% | +0.11pp | +0.23pp | 1.35% |
| Latency p95 | 1,262 ms | +1.4% | −1.6% | 1,285 ms |
| Active customers | 12,530 | +4.5% | +7.8% | 12,092 |
| Active merchants | 1,540 | +1.2% | +5.6% | 1,501 |

## What moved

- Product UPI International is compounding — attempts up 35% across the trailing window to 163 today, with success holding, so the growth is healthy and worth funding.
- Issuer HDFC Bank ran at 97.04% success on 1,725 attempts (11.2% of the day), 0.85pp up its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,792 | 31.2% | 95.20% | ₹52.77 L | +6.7% |
| UPI Person to Merchant | 4,047 | 26.3% | 95.90% | ₹44.09 L | +3.3% |
| UPI QR Payments | 2,646 | 17.2% | 96.83% | ₹11.54 L | +10.0% |
| UPI Lite | 1,791 | 11.7% | 99.61% | ₹1.76 L | +4.4% |
| UPI Circle | 718 | 4.7% | 97.21% | ₹6.70 L | +29.4% |
| UPI AutoPay | 342 | 2.2% | 85.09% | ₹6.35 L | +3.8% |
| Credit on UPI | 299 | 1.9% | 95.32% | ₹22.09 L | −17.3% |
| RuPay Credit on UPI | 270 | 1.8% | 97.41% | ₹17.75 L | −26.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,814 | 95.53% | 96.05% | ₹60.02 L | normal |
| HDFC Bank | 1,725 | 97.04% | 96.20% | ₹26.03 L | ⚠ outlier |
| Bank of Baroda | 1,155 | 96.80% | 95.88% | ₹15.52 L | normal |
| Union Bank of India | 1,082 | 96.40% | 95.64% | ₹13.20 L | normal |
| ICICI Bank | 931 | 96.46% | 96.42% | ₹10.94 L | normal |
| Axis Bank | 929 | 96.56% | 96.62% | ₹10.83 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,216 | 96.29% | 96.00% | ₹91.69 L | normal |
| Google Pay | 5,059 | 95.99% | 95.99% | ₹60.56 L | normal |
| Paytm | 1,305 | 96.09% | 96.14% | ₹19.96 L | normal |
| Navi | 587 | 94.72% | 95.71% | ₹6.59 L | normal |
| SuperMoney | 304 | 96.05% | 96.38% | ₹3.94 L | normal |
| BHIM | 137 | 94.89% | 95.87% | ₹1.83 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,786 | 96.55% | ₹50.16 L |
| Food & Beverage | 2,273 | 96.74% | ₹11.08 L |
| Bills | 1,196 | 96.49% | ₹14.11 L |
| Mobility | 1,086 | 98.71% | ₹6.21 L |
| Healthcare | 504 | 97.02% | ₹7.05 L |
| Digital | 257 | 91.05% | ₹1.38 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,481 | 29.2% | 95.96% | ₹59.76 L |
| North | 3,916 | 25.5% | 96.30% | ₹43.60 L |
| West | 3,732 | 24.3% | 96.06% | ₹50.14 L |
| East | 1,855 | 12.1% | 96.01% | ₹28.24 L |
| Central | 1,388 | 9.0% | 96.04% | ₹14.22 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Ujjwal Water Board | Key Account | Bills | 78 | 94.87% | ₹3.55 L |
| Vega Electronics | Large | Retail | 40 | 90.00% | ₹2.79 L |
| Rapid Bazaar | Key Account | Retail | 489 | 97.75% | ₹1.71 L |
| Vasant Wardrobe | Key Account | Retail | 97 | 96.91% | ₹1.71 L |
| Girnar Connect | Key Account | Bills | 218 | 98.62% | ₹87,094 |
| Urban Boutique | Key Account | Retail | 120 | 97.50% | ₹87,088 |
| Hampi Stores 2298 | Key Account | Retail | 115 | 97.39% | ₹83,647 |
| Hampi Styles | Key Account | Retail | 40 | 95.00% | ₹81,708 |

## Failure analysis

Of 595 declined attempts, 448 were business declines (2.914% of attempts — balances, PINs and limits), 80 technical (0.520%), 51 timeouts (0.332%) and 16 risk declines (0.104%).

200 attempts were re-presentations of an earlier failure (1.30% of the day); 71.0% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 178 | 1.158% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 151 | 0.982% | 0.987% |
| ZA | Transaction declined by customer | business | Customer | 56 | 0.364% | 0.336% |
| XH | Account does not exist / frozen | business | Issuer | 35 | 0.228% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 34 | 0.221% | 0.202% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 23 | 0.150% | 0.110% |
| U28 | Remitter bank unavailable | technical | Issuer | 22 | 0.143% | 0.135% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 20 | 0.130% | 0.155% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 103 | 100 |
| Auto-reversals | 39 | 27 |
| Disputes / chargebacks | 15 | 13 |
| Value returned | ₹1.19 L | ₹1.98 L |

## Customer behaviour

12,530 distinct customers transacted (+4.7% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,889 | 4,537 | 1.17 | 95.83% | ₹1,256 |
| power | 2,582 | 3,627 | 1.40 | 96.20% | ₹1,806 |
| merchant_heavy | 2,924 | 3,538 | 1.21 | 96.35% | ₹1,164 |
| small_ticket | 1,822 | 2,278 | 1.25 | 96.49% | ₹525 |
| occasional | 1,070 | 1,129 | 1.06 | 95.66% | ₹1,575 |
| new | 213 | 233 | 1.09 | 93.13% | ₹958 |
| dormant_returning | 30 | 30 | 1.00 | 96.67% | ₹1,107 |

## Operational events

- **INC-FRAUD-0045** (Sev-2) — Fraud pattern on RuPay Credit on UPI — Electronics, scoped to RUPAY_CREDIT. Coordinated fraud attempts concentrated on RuPay Credit on UPI at Electronics merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0059** (Sev-3) — Salon & Spa cashback campaign, scoped to 7230. A cashback campaign across Salon & Spa merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Product UPI AutoPay ran at 85.09% success on 342 attempts (2.2% of the day), 5.31pp down its own 28-day median.

### Opportunities

- Product UPI International is compounding — attempts up 35% across the trailing window to 163 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

27 May was an incident day: INC-FRAUD-0045 was live and the rail closed at 96.08% success against a 96.07% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=15,372, successes=14,770, failed=595, pending=7, settled_value_inr=19,595,857.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-FRAUD-0045; kind=fraud_spike; severity=Sev-2; window=2026-05-24 to 2026-05-31; success_impact_pp=-2.39; volume_impact_pct=10.94
- products: product_name=UPI International; attempts=163; window_growth_pct=34.7; success_rate=96.32
- banks: payer_bank=HDFC Bank; attempts=1,725; success_rate=97.04; own_median=96.2; z=2.75
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- categories: mcc_category=Mobility; attempts=1,086; success_rate=98.71; own_median=97.39; z=2.23
- products: product_name=UPI Lite; attempts=1,791; success_rate=99.61; own_median=98.89; z=2.07
- incidents: event_id=CMP-0059; kind=merchant_campaign; severity=Sev-3; window=2026-05-25 to 2026-06-01; success_impact_pp=-0.15; volume_impact_pct=59.67
- products: product_name=UPI AutoPay; attempts=342; success_rate=85.09; own_median=90.4; z=-2.03
- products: product_name=RuPay Credit on UPI; attempts=270; own_median=368; z=-2.36

Refs: enterprise_data/warehouse/transactions, RPT-D142-DAILY, enterprise_data/warehouse/reference/incidents.parquet
