---
id: RPT-D139-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-23T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Saturday, 23 May 2026)

**Report ID:** RPT-D139-DAILY · **Day 139 of 206** · **Derived from:** 14,778 transaction rows queried live from the warehouse

## Summary

The rail took **14,778 payment attempts** on Saturday 23 May 2026 (Weekend) and settled **₹1.91 Cr** across 14,188 successful payments. Volume was +6.6% on yesterday and −14.2% on the same weekday last week. Success closed at **96.01%**, in line with the trailing 28-day median of 96.03%.

Product UPI International is compounding — attempts up 77% across the trailing window to 186 today, but success is slipping as it scales, so the growth is outrunning its reliability. Product UPI Circle is compounding — attempts up 53% across the trailing window to 759 today, with success holding, so the growth is healthy and worth funding.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 14,778 | +6.6% | −14.2% | 14,878 |
| Successful payments | 14,188 | +6.8% | −13.8% | 14,273 |
| Success rate | 96.01% | +0.11pp | +0.41pp | 95.93% |
| Settled value | ₹1.91 Cr | −14.2% | −16.4% | ₹1.99 Cr |
| Average ticket | ₹1,349 | −19.6% | −3.0% | ₹1,398 |
| Technical declines | 0.562% | +0.12pp | −0.07pp | 0.511% |
| Business declines | 2.856% | −0.30pp | −0.25pp | 2.917% |
| Risk declines | 0.169% | +0.05pp | +0.03pp | 0.127% |
| Timeout declines | 0.298% | +0.02pp | −0.12pp | 0.405% |
| Retry share | 1.18% | +0.08pp | −1.08pp | 1.37% |
| Latency p95 | 1,262 ms | −3.2% | −2.3% | 1,290 ms |
| Active customers | 12,065 | +5.1% | −11.8% | 12,119 |
| Active merchants | 1,481 | +1.0% | −7.4% | 1,499 |

## What moved

- Product UPI International is compounding — attempts up 77% across the trailing window to 186 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Circle is compounding — attempts up 53% across the trailing window to 759 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,997 | 33.8% | 94.90% | ₹50.69 L | +13.2% |
| UPI Person to Merchant | 3,543 | 24.0% | 96.08% | ₹28.74 L | −8.8% |
| UPI QR Payments | 2,314 | 15.7% | 97.19% | ₹10.64 L | −1.6% |
| UPI Lite | 1,884 | 12.7% | 98.62% | ₹1.67 L | +12.7% |
| UPI Circle | 759 | 5.1% | 96.57% | ₹5.77 L | +43.9% |
| UPI AutoPay | 339 | 2.3% | 92.04% | ₹6.38 L | +3.0% |
| RuPay Credit on UPI | 244 | 1.7% | 95.49% | ₹16.42 L | −33.7% |
| Credit on UPI | 243 | 1.6% | 95.06% | ₹29.32 L | −31.6% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 4,655 | 95.94% | 96.05% | ₹63.80 L | normal |
| HDFC Bank | 1,553 | 96.07% | 96.18% | ₹24.13 L | normal |
| Union Bank of India | 1,086 | 96.41% | 95.35% | ₹12.33 L | normal |
| Bank of Baroda | 1,082 | 95.01% | 95.81% | ₹10.76 L | normal |
| Punjab National Bank | 931 | 96.24% | 95.61% | ₹12.99 L | normal |
| ICICI Bank | 930 | 96.67% | 96.43% | ₹12.95 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 7,002 | 95.99% | 95.95% | ₹81.60 L | normal |
| Google Pay | 4,849 | 96.10% | 95.85% | ₹68.53 L | normal |
| Paytm | 1,166 | 96.14% | 96.05% | ₹17.14 L | normal |
| Navi | 537 | 95.53% | 95.80% | ₹4.73 L | normal |
| SuperMoney | 282 | 96.45% | 96.11% | ₹3.48 L | normal |
| BHIM | 169 | 97.04% | 95.87% | ₹4.57 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 3,948 | 96.63% | ₹40.52 L |
| Food & Beverage | 2,515 | 97.18% | ₹9.68 L |
| Mobility | 1,252 | 97.44% | ₹7.21 L |
| Bills | 878 | 95.90% | ₹8.03 L |
| Healthcare | 502 | 97.81% | ₹5.75 L |
| Digital | 181 | 97.24% | ₹90,529 |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 4,345 | 29.4% | 96.18% | ₹67.54 L |
| North | 3,878 | 26.2% | 96.08% | ₹45.28 L |
| West | 3,583 | 24.2% | 95.87% | ₹46.08 L |
| East | 1,765 | 11.9% | 95.41% | ₹19.44 L |
| Central | 1,207 | 8.2% | 96.44% | ₹13.03 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Rapid Bazaar | Key Account | Retail | 417 | 97.36% | ₹1.62 L |
| Vega Electronics | Large | Retail | 26 | 92.31% | ₹1.38 L |
| Vasant Wardrobe | Key Account | Retail | 59 | 93.22% | ₹1.01 L |
| Hampi Stores 2298 | Key Account | Retail | 118 | 94.92% | ₹81,539 |
| Yamuna Restaurant | Key Account | Food & Beverage | 76 | 96.05% | ₹75,243 |
| Swift Mart 1738 | Key Account | Retail | 132 | 97.73% | ₹73,147 |
| Urban Boutique | Key Account | Retail | 103 | 98.06% | ₹71,279 |
| Girnar Connect | Key Account | Bills | 139 | 97.84% | ₹68,345 |

## Failure analysis

Of 574 declined attempts, 422 were business declines (2.856% of attempts — balances, PINs and limits), 83 technical (0.562%), 44 timeouts (0.298%) and 25 risk declines (0.169%).

175 attempts were re-presentations of an earlier failure (1.18% of the day); 70.9% of them succeeded.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| Z9 | Insufficient funds | business | Customer | 182 | 1.232% | 1.181% |
| ZM | Invalid UPI PIN | business | Customer | 137 | 0.927% | 1.022% |
| ZA | Transaction declined by customer | business | Customer | 49 | 0.332% | 0.339% |
| U30 | Debit failed at remitter bank | technical | Issuer | 38 | 0.257% | 0.206% |
| XH | Account does not exist / frozen | business | Issuer | 33 | 0.223% | 0.219% |
| U28 | Remitter bank unavailable | technical | Issuer | 23 | 0.156% | 0.134% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 21 | 0.142% | 0.155% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 20 | 0.135% | 0.106% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 106 | 96 |
| Auto-reversals | 16 | 28 |
| Disputes / chargebacks | 19 | 13 |
| Value returned | ₹1.41 L | ₹1.88 L |

## Customer behaviour

12,065 distinct customers transacted (+4.1% on the 28-day median) at 1.22 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 3,712 | 4,283 | 1.15 | 96.43% | ₹1,332 |
| power | 2,567 | 3,539 | 1.38 | 95.73% | ₹1,895 |
| merchant_heavy | 2,715 | 3,315 | 1.22 | 95.87% | ₹984 |
| small_ticket | 1,854 | 2,332 | 1.26 | 95.71% | ₹626 |
| occasional | 957 | 1,020 | 1.07 | 96.57% | ₹1,804 |
| new | 227 | 255 | 1.12 | 94.90% | ₹564 |
| dormant_returning | 33 | 34 | 1.03 | 97.06% | ₹514 |

## Operational events

- **INC-PSP-0024** (Sev-3) — PhonePe app release regression, scoped to PhonePe between 19:00 and 23:00. A PhonePe client release degraded the collect and intent flows. Volume shifted to competing apps for the duration and returned only partially after rollback.

## Risks and opportunities

### Risks

- Product UPI International is compounding — attempts up 77% across the trailing window to 186 today, but success is slipping as it scales, so the growth is outrunning its reliability.

### Opportunities

- Product UPI Circle is compounding — attempts up 53% across the trailing window to 759 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

23 May ran on trend at 96.01% success and ₹1.91 Cr settled. The movement worth carrying forward is in the product mix: product UPI International is compounding — attempts up 77% across the trailing window to 186 today, but success is slipping as it scales, so the growth is outrunning its reliability. 1 further movement cleared the materiality threshold and is listed above.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-05-23` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=14,778, successes=14,188, failed=574, pending=16, settled_value_inr=19,136,598.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- products: product_name=UPI International; attempts=186; window_growth_pct=76.7; success_rate=93.01
- products: product_name=UPI Circle; attempts=759; window_growth_pct=53.1; success_rate=96.57
- incidents: event_id=INC-PSP-0024; kind=psp_degradation; severity=Sev-3; window=2026-05-21 to 2026-05-24; success_impact_pp=-4.06; volume_impact_pct=-6.35
- products: product_name=UPI Circle; attempts=759; own_median=527.5; z=2.67
- products: product_name=RuPay Credit on UPI; attempts=244; own_median=368; z=-2.88
- products: product_name=UPI Lite Auto Top-Up; attempts=92; success_rate=100; own_median=96.63; z=2.12

Refs: enterprise_data/warehouse/transactions, RPT-D138-DAILY, enterprise_data/warehouse/reference/incidents.parquet
