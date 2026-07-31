---
id: RPT-D100-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-14T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Tuesday, 14 Apr 2026)

**Report ID:** RPT-D100-DAILY · **Day 100 of 206** · **Derived from:** 11,971 transaction rows queried live from the warehouse

## Summary

The rail took **11,971 payment attempts** on Tuesday 14 April 2026 (Ambedkar Jayanti) and settled **₹1.42 Cr** across 11,422 successful payments. Volume was +2.3% on yesterday and −7.5% on the same weekday last week. Success closed at **95.41%**, below the trailing 28-day median of 95.94%.

Retries reached 179 attempts (1.50% of the day, 2.3 sigma above normal). 58.1% of re-presented payments recovered, so the retry path was doing its job. Success rate closed at 95.41%, 0.53pp down the trailing median — a 1.8-sigma move.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 11,971 | +2.3% | −7.5% | 12,755 |
| Successful payments | 11,422 | +2.4% | −8.0% | 12,183 |
| Success rate | 95.41% | +0.10pp | −0.52pp | 95.49% |
| Settled value | ₹1.42 Cr | −17.1% | −16.7% | ₹1.64 Cr |
| Average ticket | ₹1,239 | −19.1% | −9.5% | ₹1,340 |
| Technical declines | 0.543% | −0.00pp | +0.16pp | 0.532% |
| Business declines | 3.458% | −0.05pp | +0.48pp | 3.105% |
| Risk declines | 0.142% | −0.01pp | +0.01pp | 0.143% |
| Timeout declines | 0.326% | −0.04pp | −0.11pp | 0.604% |
| Retry share | 1.50% | +0.34pp | +0.27pp | 1.56% |
| Latency p95 | 1,224 ms | −3.8% | −4.1% | 1,326 ms |
| Active customers | 9,982 | +0.3% | −7.0% | 10,580 |
| Active merchants | 1,359 | −0.9% | −4.0% | 1,384 |

## What moved

- Success rate closed at 95.41%, 0.53pp down the trailing median — a 1.8-sigma move.
- Product Credit on UPI is compounding — attempts up 45% across the trailing window to 157 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Person to Merchant carried 4,491 attempts, 29% up its trailing median and 37.5% of the day's volume.
- Product RuPay Credit on UPI is compounding — attempts up 38% across the trailing window to 176 today, but success is slipping as it scales, so the growth is outrunning its reliability.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Merchant | 4,491 | 37.5% | 95.79% | ₹41.67 L | +29.1% |
| UPI Person to Person | 3,758 | 31.4% | 94.70% | ₹40.40 L | −15.6% |
| UPI QR Payments | 1,529 | 12.8% | 96.34% | ₹6.66 L | −29.6% |
| UPI Lite | 948 | 7.9% | 98.63% | ₹90,962 | −10.9% |
| UPI AutoPay | 328 | 2.7% | 89.33% | ₹5.85 L | +2.5% |
| UPI Circle | 279 | 2.3% | 95.34% | ₹1.91 L | +12.3% |
| RuPay Credit on UPI | 176 | 1.5% | 93.75% | ₹13.83 L | −31.5% |
| Credit on UPI | 157 | 1.3% | 94.27% | ₹13.00 L | −11.5% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,860 | 95.08% | 95.99% | ₹44.94 L | normal |
| HDFC Bank | 1,273 | 96.39% | 95.82% | ₹14.73 L | normal |
| Bank of Baroda | 864 | 95.83% | 95.85% | ₹9.75 L | normal |
| Union Bank of India | 789 | 95.94% | 95.90% | ₹10.04 L | normal |
| Axis Bank | 752 | 95.35% | 95.72% | ₹9.76 L | normal |
| ICICI Bank | 741 | 96.36% | 96.30% | ₹10.25 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,706 | 95.76% | 95.88% | ₹65.40 L | normal |
| Google Pay | 3,927 | 95.24% | 95.76% | ₹49.35 L | normal |
| Paytm | 986 | 95.33% | 96.01% | ₹12.98 L | normal |
| Navi | 438 | 93.38% | 95.88% | ₹4.24 L | ⚠ outlier |
| SuperMoney | 220 | 95.45% | 95.09% | ₹3.13 L | normal |
| BHIM | 114 | 92.98% | 96.46% | ₹1.21 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,481 | 96.01% | ₹40.53 L |
| Food & Beverage | 2,076 | 95.86% | ₹10.26 L |
| Bills | 903 | 94.57% | ₹10.20 L |
| Mobility | 671 | 96.72% | ₹3.42 L |
| Healthcare | 486 | 97.74% | ₹3.90 L |
| Digital | 212 | 92.45% | ₹87,603 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,294 | 27.5% | 95.05% | ₹39.22 L |
| North | 3,162 | 26.4% | 95.32% | ₹35.52 L |
| West | 3,123 | 26.1% | 95.20% | ₹39.73 L |
| East | 1,287 | 10.8% | 95.88% | ₹15.95 L |
| Central | 1,105 | 9.2% | 96.83% | ₹11.13 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 40 | 92.50% | ₹2.43 L |
| Rapid Bazaar | Key Account | Retail | 340 | 95.59% | ₹1.55 L |
| Hampi Styles | Key Account | Retail | 40 | 90.00% | ₹1.36 L |
| Vasant Wardrobe | Key Account | Retail | 75 | 98.67% | ₹1.31 L |
| Girnar Connect | Key Account | Bills | 138 | 96.38% | ₹94,348 |
| Ujjwal Water Board | Key Account | Bills | 58 | 91.38% | ₹91,716 |
| Aravalli Pharmacy | Large | Healthcare | 90 | 97.78% | ₹73,441 |
| Urban Boutique | Key Account | Retail | 108 | 98.15% | ₹68,638 |

## Failure analysis

Of 535 declined attempts, 414 were business declines (3.458% of attempts — balances, PINs and limits), 65 technical (0.543%), 39 timeouts (0.326%) and 17 risk declines (0.142%).

179 attempts were re-presentations of an earlier failure (1.50% of the day); 58.1% of them succeeded.

- Retries reached 179 attempts (1.50% of the day, 2.3 sigma above normal). 58.1% of re-presented payments recovered, so the retry path was doing its job.
- Decline code YA (PSP not available) fired 13 times — 0.109% of attempts against a trailing 0.059%. Owner: PSP.
- Decline code U69 (Beneficiary bank offline) fired 13 times — 0.109% of attempts against a trailing 0.063%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 173 | 1.445% | 1.315% |
| ZM | Invalid UPI PIN | business | Customer | 136 | 1.136% | 1.013% |
| ZA | Transaction declined by customer | business | Customer | 46 | 0.384% | 0.359% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.276% | 0.221% |
| U30 | Debit failed at remitter bank | technical | Issuer | 27 | 0.226% | 0.188% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.192% | 0.166% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 16 | 0.134% | 0.116% |
| ZX | Mandate not found or revoked | business | PSP | 14 | 0.117% | 0.072% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 90 | 74 |
| Auto-reversals | 21 | 22 |
| Disputes / chargebacks | 8 | 11 |
| Value returned | ₹2.08 L | ₹1.55 L |

## Customer behaviour

9,982 distinct customers transacted (−5.9% on the 28-day median) at 1.20 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,066 | 3,527 | 1.15 | 95.69% | ₹1,146 |
| power | 2,130 | 2,838 | 1.33 | 95.07% | ₹1,717 |
| merchant_heavy | 2,289 | 2,727 | 1.19 | 95.31% | ₹985 |
| small_ticket | 1,496 | 1,823 | 1.22 | 95.23% | ₹587 |
| occasional | 777 | 819 | 1.05 | 96.21% | ₹1,657 |
| new | 197 | 210 | 1.07 | 94.76% | ₹538 |
| dormant_returning | 27 | 27 | 1.00 | 100.00% | ₹543 |

## Operational events

- **INC-PSP-0030** (Sev-2) — PhonePe app release regression, scoped to PhonePe between 16:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.
- **CHURN-0091** (Sev-2) — Fuel merchant attrition to competing acquirer, scoped to 5541. A rival acquirer won a block of Fuel merchants on pricing. Category volume decays steadily with no reliability degradation — a commercial loss, not an operational one.
- **CMP-0053** (Sev-3) — Utilities cashback campaign, scoped to 4900. A cashback campaign across Utilities merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Success rate closed at 95.41%, 0.53pp down the trailing median — a 1.8-sigma move.
- 90 refunds were raised, 2.3 sigma above the trailing median of 74.
- Product Credit on UPI is compounding — attempts up 45% across the trailing window to 157 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product RuPay Credit on UPI is compounding — attempts up 38% across the trailing window to 176 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Decline code YA (PSP not available) fired 13 times — 0.109% of attempts against a trailing 0.059%. Owner: PSP.

### Opportunities

- No growth signal cleared the threshold today; the compounding products are tracking their existing curves.

## Executive observation

14 April was an incident day: INC-PSP-0030 was live and the rail closed at 95.41% success against a 95.94% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-04-14` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=11,971, successes=11,422, failed=535, pending=14, settled_value_inr=14,154,799.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=179; retry_share_pct=1.5; recovery_pct=58.1; z=2.32
- incidents: event_id=INC-PSP-0030; kind=psp_degradation; severity=Sev-2; window=2026-04-14 to 2026-04-16; success_impact_pp=-7.77; volume_impact_pct=-12.17
- headline: success_rate=95.41; trailing_median=95.94; z=-1.82
- adjustments: refunds=90; trailing_median=74.5; z=2.32
- products: product_name=Credit on UPI; attempts=157; window_growth_pct=45; success_rate=94.27
- products: product_name=UPI Person to Merchant; attempts=4,491; own_median=3,480; z=2.45
- products: product_name=RuPay Credit on UPI; attempts=176; window_growth_pct=38.1; success_rate=93.75
- incidents: event_id=CHURN-0091; kind=merchant_churn; severity=Sev-2; window=2026-04-06 to 2026-05-02; success_impact_pp=0.08; volume_impact_pct=-24.83
- failures: failure_code=YA; count=13; rate_pct=0.11; trailing_rate_pct=0.06; owner=PSP; z=2.66
- failures: failure_code=U69; count=13; rate_pct=0.11; trailing_rate_pct=0.06; owner=Issuer; z=2.1

Refs: enterprise_data/warehouse/transactions, RPT-D99-DAILY, enterprise_data/warehouse/reference/incidents.parquet
