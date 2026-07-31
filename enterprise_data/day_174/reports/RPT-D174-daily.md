---
id: RPT-D174-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-27T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 27 Jun 2026)

**Report ID:** RPT-D174-DAILY · **Day 174 of 206** · **Derived from:** 16,137 transaction rows queried live from the warehouse

## Summary

The rail took **16,137 payment attempts** on Saturday 27 June 2026 (Weekend) and settled **₹1.97 Cr** across 15,532 successful payments. Volume was +16.7% on yesterday and −16.4% on the same weekday last week. Success closed at **96.25%**, in line with the trailing 28-day median of 96.28%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 16,137 | +16.7% | −16.4% | 14,836 |
| Successful payments | 15,532 | +17.3% | −16.8% | 14,279 |
| Success rate | 96.25% | +0.42pp | −0.35pp | 96.22% |
| Settled value | ₹1.97 Cr | +35.4% | −23.7% | ₹1.93 Cr |
| Average ticket | ₹1,267 | +15.4% | −8.3% | ₹1,347 |
| Technical declines | 0.465% | +0.07pp | +0.00pp | 0.423% |
| Business declines | 2.832% | −0.47pp | +0.35pp | 2.876% |
| Risk declines | 0.118% | −0.06pp | +0.01pp | 0.125% |
| Timeout declines | 0.235% | +0.00pp | −0.01pp | 0.266% |
| Retry share | 1.11% | −0.14pp | +0.15pp | 1.09% |
| Latency p95 | 1,277 ms | −0.5% | +0.4% | 1,278 ms |
| Active customers | 13,121 | +13.6% | −13.7% | 12,199 |
| Active merchants | 1,597 | +6.0% | −4.2% | 1,544 |

## What moved

- Product UPI Lite carried 2,994 attempts, 42% up its trailing median and 18.6% of the day's volume.
- Category Bills carried 1,380 attempts, 62% up its trailing median and 11.9% of the day's volume.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,548 | 28.2% | 95.01% | ₹46.12 L | +8.9% |
| UPI Person to Merchant | 3,596 | 22.3% | 96.47% | ₹33.75 L | +1.1% |
| UPI Lite | 2,994 | 18.6% | 98.73% | ₹2.64 L | +41.8% |
| UPI QR Payments | 2,605 | 16.1% | 96.55% | ₹10.41 L | +11.4% |
| UPI Circle | 949 | 5.9% | 98.21% | ₹9.73 L | +32.2% |
| UPI AutoPay | 395 | 2.4% | 87.09% | ₹7.19 L | +11.1% |
| Credit on UPI | 315 | 2.0% | 94.29% | ₹37.87 L | −30.3% |
| RuPay Credit on UPI | 228 | 1.4% | 98.68% | ₹14.69 L | −39.2% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,057 | 96.18% | 96.28% | ₹59.24 L | normal |
| HDFC Bank | 1,741 | 97.07% | 96.46% | ₹20.98 L | normal |
| Bank of Baroda | 1,268 | 95.58% | 96.26% | ₹16.12 L | normal |
| Union Bank of India | 1,060 | 97.08% | 96.21% | ₹12.39 L | normal |
| Axis Bank | 1,034 | 96.81% | 96.23% | ₹12.70 L | normal |
| Punjab National Bank | 1,030 | 95.24% | 96.27% | ₹13.78 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,677 | 96.43% | 96.11% | ₹93.76 L | normal |
| Google Pay | 5,232 | 96.20% | 96.36% | ₹64.86 L | normal |
| Paytm | 1,313 | 96.04% | 96.28% | ₹18.74 L | normal |
| Navi | 589 | 94.91% | 96.61% | ₹5.78 L | ⚠ outlier |
| SuperMoney | 334 | 96.71% | 95.64% | ₹3.62 L | normal |
| BHIM | 169 | 95.86% | 95.86% | ₹2.52 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 4,370 | 96.89% | ₹42.74 L |
| Food & Beverage | 2,972 | 97.44% | ₹11.22 L |
| Mobility | 1,532 | 97.91% | ₹7.28 L |
| Bills | 1,380 | 95.87% | ₹14.39 L |
| Healthcare | 564 | 97.34% | ₹9.35 L |
| Digital | 258 | 94.19% | ₹1.33 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,672 | 29.0% | 96.43% | ₹61.20 L |
| North | 4,256 | 26.4% | 96.31% | ₹45.54 L |
| West | 3,933 | 24.4% | 96.01% | ₹52.57 L |
| East | 1,849 | 11.5% | 96.38% | ₹23.66 L |
| Central | 1,427 | 8.8% | 96.01% | ₹13.89 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 455 | 97.36% | ₹2.28 L |
| Ujjwal Water Board | Key Account | Bills | 51 | 96.08% | ₹1.83 L |
| Hampi Styles | Key Account | Retail | 28 | 96.43% | ₹1.31 L |
| Vega Electronics | Large | Retail | 27 | 96.30% | ₹1.20 L |
| Vasant Wardrobe | Key Account | Retail | 55 | 94.55% | ₹1.09 L |
| Girnar Connect | Key Account | Bills | 237 | 95.36% | ₹95,490 |
| Yamuna Restaurant | Key Account | Food & Beverage | 68 | 97.06% | ₹76,422 |
| Hampi Stores 2298 | Key Account | Retail | 121 | 98.35% | ₹67,611 |

## Failure analysis

Of 589 declined attempts, 457 were business declines (2.832% of attempts — balances, PINs and limits), 75 technical (0.465%), 38 timeouts (0.235%) and 19 risk declines (0.118%).

179 attempts were re-presentations of an earlier failure (1.11% of the day); 65.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 198 | 1.227% | 1.217% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 0.843% | 0.943% |
| ZA | Transaction declined by customer | business | Customer | 55 | 0.341% | 0.337% |
| XH | Account does not exist / frozen | business | Issuer | 40 | 0.248% | 0.200% |
| U30 | Debit failed at remitter bank | technical | Issuer | 33 | 0.204% | 0.173% |
| U28 | Remitter bank unavailable | technical | Issuer | 20 | 0.124% | 0.111% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 18 | 0.112% | 0.113% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 16 | 0.099% | 0.139% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 110 | 106 |
| Auto-reversals | 18 | 22 |
| Disputes / chargebacks | 18 | 14 |
| Value returned | ₹1.88 L | ₹1.70 L |

## Customer behaviour

13,121 distinct customers transacted (+8.5% on the 28-day median) at 1.23 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,087 | 4,763 | 1.17 | 95.88% | ₹1,281 |
| power | 2,833 | 3,908 | 1.38 | 96.08% | ₹1,766 |
| merchant_heavy | 3,009 | 3,708 | 1.23 | 96.41% | ₹882 |
| small_ticket | 1,952 | 2,434 | 1.25 | 96.92% | ₹612 |
| occasional | 1,003 | 1,064 | 1.06 | 96.62% | ₹1,353 |
| new | 198 | 219 | 1.11 | 95.43% | ₹1,785 |
| dormant_returning | 39 | 41 | 1.05 | 95.12% | ₹2,224 |

## Operational events

- **INC-BANK-0010** (Sev-2) — Kotak Mahindra Bank issuer decline spike, scoped to Kotak Mahindra Bank between 10:00 and 15:00. Kotak Mahindra Bank core banking reported elevated U30/U28 declines. Remitter-side debit failures rose sharply and PSPs began routing retries, lifting p95 latency.
- **CHURN-0092** (Sev-2) — Mobile & DTH Recharge merchant attrition to competing acquirer, scoped to 4814. A rival acquirer won a block of Mobile & DTH Recharge merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **ADOPT-0074** (Sev-3) — Upi Lite onboarding push, scoped to UPI_LITE. A coordinated PSP onboarding push drove a step-in of first-time users. New-user cohorts transact at lower ticket sizes and slightly lower success rates.

## Risks and opportunities

### Risks

- Product UPI Lite Auto Top-Up ran at 89.25% success on 93 attempts (0.6% of the day), 8.00pp down its own 28-day median.
- App Navi ran at 94.91% success on 589 attempts (3.6% of the day), 1.71pp down its own 28-day median.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

27 June was an incident day: INC-BANK-0010 was live and the rail closed at 96.25% success against a 96.28% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-06-27` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=16,137, successes=15,532, failed=589, pending=16, settled_value_inr=19,685,669.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-BANK-0010; kind=bank_outage; severity=Sev-2; window=2026-06-25 to 2026-06-27; success_impact_pp=-19.68; volume_impact_pct=-17.46
- products: product_name=UPI Lite; attempts=2,994; own_median=2,111.5; z=4.15
- categories: mcc_category=Bills; attempts=1,380; own_median=852; z=5.02
- incidents: event_id=CHURN-0092; kind=merchant_churn; severity=Sev-2; window=2026-05-25 to 2026-07-04; success_impact_pp=0.08; volume_impact_pct=-26.07
- categories: mcc_category=Mobility; attempts=1,532; own_median=1,254.5; z=2.42
- products: product_name=UPI Lite Auto Top-Up; attempts=93; success_rate=89.25; own_median=97.25; z=-6.3
- products: product_name=UPI Circle; attempts=949; own_median=718; z=2.4
- psps: payer_psp=Navi; attempts=589; success_rate=94.91; own_median=96.61; z=-2.22
- incidents: event_id=ADOPT-0074; kind=adoption_surge; severity=Sev-3; window=2026-06-22 to 2026-07-05; success_impact_pp=-0.45; volume_impact_pct=40.31

Refs: enterprise_data/warehouse/transactions, RPT-D173-DAILY, enterprise_data/warehouse/reference/incidents.parquet
