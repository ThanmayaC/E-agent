---
id: RPT-D187-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-10T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Friday, 10 Jul 2026)

**Report ID:** RPT-D187-DAILY · **Day 187 of 206** · **Derived from:** 17,419 transaction rows queried live from the warehouse

## Summary

The rail took **17,419 payment attempts** on Friday 10 July 2026 (Working day) and settled **₹2.16 Cr** across 16,702 successful payments. Volume was +14.5% on yesterday and +0.3% on the same weekday last week. Success closed at **95.88%**, below the trailing 28-day median of 96.21%.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 17,419 | +14.5% | +0.3% | 17,256 |
| Successful payments | 16,702 | +13.8% | −0.5% | 16,575 |
| Success rate | 95.88% | −0.59pp | −0.79pp | 96.10% |
| Settled value | ₹2.16 Cr | +14.8% | −4.0% | ₹2.20 Cr |
| Average ticket | ₹1,295 | +0.9% | −3.5% | ₹1,328 |
| Technical declines | 0.574% | +0.19pp | +0.23pp | 0.504% |
| Business declines | 2.997% | +0.32pp | +0.45pp | 2.658% |
| Risk declines | 0.149% | +0.06pp | +0.02pp | 0.113% |
| Timeout declines | 0.310% | +0.04pp | +0.07pp | 0.543% |
| Retry share | 1.44% | +0.45pp | +0.49pp | 1.47% |
| Latency p95 | 1,335 ms | +5.1% | +6.2% | 1,322 ms |
| Active customers | 13,931 | +11.0% | −0.8% | 13,857 |
| Active merchants | 1,635 | +3.5% | −1.3% | 1,643 |

## What moved

- Product UPI Lite is compounding — attempts up 33% across the trailing window to 2,796 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 31% across the trailing window to 892 today, with success holding, so the growth is healthy and worth funding.
- Product UPI QR Payments ran at 95.77% success on 2,764 attempts (15.9% of the day), 0.79pp down its own 28-day median.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,849 | 27.8% | 95.17% | ₹50.77 L | +10.4% |
| UPI Person to Merchant | 4,284 | 24.6% | 96.10% | ₹43.27 L | +19.2% |
| UPI Lite | 2,796 | 16.1% | 98.64% | ₹2.59 L | +13.2% |
| UPI QR Payments | 2,764 | 15.9% | 95.77% | ₹12.48 L | +9.8% |
| UPI Circle | 892 | 5.1% | 96.97% | ₹7.31 L | +11.8% |
| Credit on UPI | 540 | 3.1% | 95.37% | ₹37.40 L | +14.8% |
| UPI AutoPay | 370 | 2.1% | 87.57% | ₹6.05 L | −1.7% |
| RuPay Credit on UPI | 360 | 2.1% | 96.39% | ₹16.38 L | −4.0% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 5,423 | 95.85% | 96.16% | ₹64.29 L | normal |
| HDFC Bank | 1,914 | 95.30% | 96.39% | ₹22.94 L | normal |
| Bank of Baroda | 1,298 | 95.76% | 96.22% | ₹15.62 L | normal |
| Union Bank of India | 1,256 | 96.34% | 96.12% | ₹17.30 L | normal |
| ICICI Bank | 1,086 | 95.67% | 96.34% | ₹17.04 L | normal |
| Axis Bank | 1,070 | 96.54% | 96.13% | ₹14.72 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 8,154 | 95.93% | 96.22% | ₹98.52 L | normal |
| Google Pay | 5,837 | 95.99% | 96.21% | ₹73.15 L | normal |
| Paytm | 1,421 | 96.13% | 96.12% | ₹17.34 L | normal |
| Navi | 651 | 94.47% | 96.55% | ₹8.21 L | ⚠ outlier |
| SuperMoney | 359 | 96.38% | 95.51% | ₹4.80 L | normal |
| BHIM | 179 | 93.30% | 95.85% | ₹1.46 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 5,285 | 96.78% | ₹68.19 L |
| Food & Beverage | 3,167 | 96.46% | ₹17.35 L |
| Mobility | 1,611 | 97.27% | ₹8.10 L |
| Bills | 1,117 | 94.00% | ₹11.87 L |
| Healthcare | 682 | 97.07% | ₹8.85 L |
| Digital | 249 | 93.17% | ₹1.24 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 5,045 | 29.0% | 95.66% | ₹64.40 L |
| North | 4,588 | 26.3% | 95.64% | ₹60.03 L |
| West | 4,274 | 24.5% | 96.09% | ₹50.76 L |
| East | 1,994 | 11.4% | 96.59% | ₹25.64 L |
| Central | 1,518 | 8.7% | 95.85% | ₹15.39 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 33 | 93.94% | ₹3.92 L |
| Rapid Bazaar | Key Account | Retail | 522 | 98.28% | ₹2.73 L |
| Vasant Wardrobe | Key Account | Retail | 92 | 96.74% | ₹1.56 L |
| Yamuna Restaurant | Key Account | Food & Beverage | 86 | 98.84% | ₹1.41 L |
| Urban Boutique | Key Account | Retail | 139 | 94.24% | ₹1.19 L |
| Hampi Stores 2298 | Key Account | Retail | 153 | 96.08% | ₹1.12 L |
| Girnar Connect | Key Account | Bills | 198 | 92.42% | ₹1.02 L |
| Trinetra Restaurant | Large | Food & Beverage | 50 | 100.00% | ₹97,692 |

## Failure analysis

Of 702 declined attempts, 522 were business declines (2.997% of attempts — balances, PINs and limits), 100 technical (0.574%), 54 timeouts (0.310%) and 26 risk declines (0.149%).

251 attempts were re-presentations of an earlier failure (1.44% of the day); 44.6% of them succeeded.

- Decline code YA (PSP not available) fired 18 times — 0.103% of attempts against a trailing 0.046%. Owner: PSP.
- Decline code U28 (Remitter bank unavailable) fired 32 times — 0.184% of attempts against a trailing 0.122%. Owner: Issuer.
- Decline code BT (Acquirer / NPCI switch timeout) fired 27 times — 0.155% of attempts against a trailing 0.091%. Owner: NPCI.
- Decline code U69 (Beneficiary bank offline) fired 23 times — 0.132% of attempts against a trailing 0.089%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 208 | 1.194% | 0.956% |
| Z9 | Insufficient funds | business | Customer | 196 | 1.125% | 1.224% |
| ZA | Transaction declined by customer | business | Customer | 57 | 0.327% | 0.325% |
| U28 | Remitter bank unavailable | technical | Issuer | 32 | 0.184% | 0.122% |
| XH | Account does not exist / frozen | business | Issuer | 32 | 0.184% | 0.190% |
| BT | Acquirer / NPCI switch timeout | timeout | NPCI | 27 | 0.155% | 0.091% |
| U30 | Debit failed at remitter bank | technical | Issuer | 25 | 0.144% | 0.176% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 23 | 0.132% | 0.132% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 133 | 108 |
| Auto-reversals | 12 | 24 |
| Disputes / chargebacks | 18 | 14 |
| Value returned | ₹1.43 L | ₹1.71 L |

## Customer behaviour

13,931 distinct customers transacted (+11.7% on the 28-day median) at 1.25 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 4,318 | 5,119 | 1.19 | 95.55% | ₹1,308 |
| power | 3,014 | 4,295 | 1.43 | 95.55% | ₹1,794 |
| merchant_heavy | 3,202 | 3,957 | 1.24 | 96.29% | ₹1,010 |
| small_ticket | 2,077 | 2,642 | 1.27 | 96.10% | ₹483 |
| occasional | 1,053 | 1,113 | 1.06 | 96.32% | ₹1,363 |
| new | 241 | 266 | 1.10 | 97.37% | ₹907 |
| dormant_returning | 26 | 27 | 1.04 | 100.00% | ₹7,093 |

## Operational events

- **INC-SETL-0082** (Sev-2) — Mandate settlement batch delay, scoped to UPI_AUTOPAY,UPI_RECURRING,UPI_LITE_ATU. The overnight mandate execution batch ran late, pushing debits past the pre-debit notification window. Failed mandates were re-presented the following day, producing a retry spike.
- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **MAINT-0085** (Sev-3) — HDFC Bank scheduled CBS maintenance, scoped to HDFC Bank between 00:00 and 04:00. HDFC Bank runs its announced core-banking maintenance slot every 28 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.

## Risks and opportunities

### Risks

- Decline code YA (PSP not available) fired 18 times — 0.103% of attempts against a trailing 0.046%. Owner: PSP.
- Decline code U28 (Remitter bank unavailable) fired 32 times — 0.184% of attempts against a trailing 0.122%. Owner: Issuer.
- 133 refunds were raised, 2.2 sigma above the trailing median of 108.
- Product UPI QR Payments ran at 95.77% success on 2,764 attempts (15.9% of the day), 0.79pp down its own 28-day median.
- Decline code BT (Acquirer / NPCI switch timeout) fired 27 times — 0.155% of attempts against a trailing 0.091%. Owner: NPCI.

### Opportunities

- Product UPI Lite is compounding — attempts up 33% across the trailing window to 2,796 today, with success holding, so the growth is healthy and worth funding.
- Product UPI Circle is compounding — attempts up 31% across the trailing window to 892 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

10 July was an incident day: INC-SETL-0082 was live and the rail closed at 95.88% success against a 96.21% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-07-10` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=17,419, successes=16,702, failed=702, pending=15, settled_value_inr=21,623,476.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- incidents: event_id=INC-SETL-0082; kind=settlement_delay; severity=Sev-2; window=2026-07-10 to 2026-07-12; success_impact_pp=-6.29; volume_impact_pct=-22.54
- failures: failure_code=YA; count=18; rate_pct=0.1; trailing_rate_pct=0.05; owner=PSP; z=4.67
- failures: failure_code=U28; count=32; rate_pct=0.18; trailing_rate_pct=0.12; owner=Issuer; z=3.4
- adjustments: refunds=133; trailing_median=108.5; z=2.2
- products: product_name=UPI Lite; attempts=2,796; window_growth_pct=33.1; success_rate=98.64
- products: product_name=UPI Circle; attempts=892; window_growth_pct=31.3; success_rate=96.97
- products: product_name=UPI QR Payments; attempts=2,764; success_rate=95.77; own_median=96.56; z=-2.05
- failures: failure_code=BT; count=27; rate_pct=0.15; trailing_rate_pct=0.09; owner=NPCI; z=2.1
- banks: payer_bank=Canara Bank; attempts=949; success_rate=94.63; own_median=96.52; z=-2.96
- categories: mcc_category=Bills; attempts=1,117; success_rate=94; own_median=95.93; z=-2.29

Refs: enterprise_data/warehouse/transactions, RPT-D186-DAILY, enterprise_data/warehouse/reference/incidents.parquet
