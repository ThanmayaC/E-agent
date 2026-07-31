---
id: RPT-D67-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-12T18:30:00
source: enterprise_data/warehouse (raw transactions)
---

# UPI Products — Daily Operations Report (Thursday, 12 Mar 2026)

**Report ID:** RPT-D67-DAILY · **Day 67 of 206** · **Derived from:** 10,793 transaction rows queried live from the warehouse

## Summary

The rail took **10,793 payment attempts** on Thursday 12 March 2026 (Working day) and settled **₹1.26 Cr** across 10,278 successful payments. Volume was −3.1% on yesterday and −17.8% on the same weekday last week. Success closed at **95.23%**, below the trailing 28-day median of 95.62%.

Retries reached 215 attempts (1.99% of the day, 4.3 sigma above normal). 63.7% of re-presented payments recovered, so the retry path was doing its job. Category Retail ran at 94.56% success on 2,795 attempts (41.9% of the day), 1.57pp down its own 28-day median.

## Key measures

| Measure | Today | vs yesterday | vs last week | Month to date |
|---|---|---|---|---|
| Attempts | 10,793 | −3.1% | −17.8% | 13,106 |
| Successful payments | 10,278 | −2.4% | −18.4% | 12,555 |
| Success rate | 95.23% | +0.68pp | −0.64pp | 95.77% |
| Settled value | ₹1.26 Cr | −0.7% | −22.5% | ₹1.50 Cr |
| Average ticket | ₹1,230 | +1.8% | −5.0% | ₹1,200 |
| Technical declines | 0.510% | −0.24pp | +0.15pp | 0.455% |
| Business declines | 3.613% | +0.02pp | +0.31pp | 3.205% |
| Risk declines | 0.176% | +0.06pp | +0.05pp | 0.120% |
| Timeout declines | 0.352% | −0.54pp | +0.15pp | 0.353% |
| Retry share | 1.99% | −0.09pp | +0.79pp | 1.32% |
| Latency p95 | 1,306 ms | −9.2% | +9.2% | 1,255 ms |
| Active customers | 9,176 | −1.9% | −14.8% | 10,768 |
| Active merchants | 1,290 | −1.2% | −2.1% | 1,333 |

## What moved

- Category Retail ran at 94.56% success on 2,795 attempts (41.9% of the day), 1.57pp down its own 28-day median.
- Product UPI Circle is compounding — attempts up 69% across the trailing window to 173 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Person to Merchant ran at 95.03% success on 2,838 attempts (26.3% of the day), 0.94pp down its own 28-day median.
- Product UPI International is compounding — attempts up 45% across the trailing window to 113 today, with success holding, so the growth is healthy and worth funding.

## Product performance

| Product | Attempts | Share | Success | Settled value | vs 28d median |
|---|---|---|---|---|---|
| UPI Person to Person | 4,121 | 38.2% | 95.03% | ₹43.36 L | +1.7% |
| UPI Person to Merchant | 2,838 | 26.3% | 95.03% | ₹26.74 L | −11.3% |
| UPI QR Payments | 1,804 | 16.7% | 95.68% | ₹7.47 L | −8.9% |
| UPI Lite | 724 | 6.7% | 98.76% | ₹62,649 | −4.7% |
| UPI AutoPay | 330 | 3.1% | 90.00% | ₹5.73 L | +9.6% |
| RuPay Credit on UPI | 269 | 2.5% | 96.65% | ₹10.35 L | +25.1% |
| Credit on UPI | 174 | 1.6% | 95.98% | ₹12.38 L | +17.2% |
| UPI Circle | 173 | 1.6% | 95.38% | ₹1.32 L | +30.1% |

## Rail performance

### Issuer performance

| Bank | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| State Bank of India | 3,495 | 95.71% | 95.52% | ₹39.86 L | normal |
| HDFC Bank | 1,169 | 95.04% | 96.23% | ₹14.14 L | ⚠ outlier |
| Union Bank of India | 785 | 93.38% | 95.26% | ₹9.94 L | ⚠ outlier |
| Bank of Baroda | 782 | 96.68% | 95.47% | ₹7.93 L | normal |
| Punjab National Bank | 650 | 94.62% | 95.09% | ₹6.73 L | normal |
| Axis Bank | 638 | 94.36% | 95.88% | ₹7.97 L | normal |

### App / PSP performance

| Psp | Attempts | Success | Own 28d median | Settled value | Status |
|---|---|---|---|---|---|
| PhonePe | 5,017 | 95.61% | 95.66% | ₹57.95 L | normal |
| Google Pay | 3,600 | 95.14% | 95.67% | ₹43.18 L | normal |
| Paytm | 865 | 93.99% | 95.41% | ₹9.51 L | normal |
| Navi | 417 | 95.20% | 95.49% | ₹5.37 L | normal |
| SuperMoney | 195 | 94.36% | 95.88% | ₹1.98 L | normal |
| BHIM | 122 | 96.72% | 95.18% | ₹1.76 L | normal |

## Where the demand came from

### Merchant categories

| Category | Attempts | Success | Settled value |
|---|---|---|---|
| Retail | 2,795 | 94.56% | ₹30.16 L |
| Food & Beverage | 1,660 | 95.90% | ₹7.58 L |
| Mobility | 696 | 97.27% | ₹4.50 L |
| Bills | 654 | 96.48% | ₹7.05 L |
| Healthcare | 319 | 99.06% | ₹2.26 L |
| Digital | 202 | 91.58% | ₹1.08 L |

### Geography

| Region | Attempts | Share | Success | Settled value |
|---|---|---|---|---|
| South | 3,163 | 29.3% | 95.64% | ₹40.44 L |
| North | 2,780 | 25.8% | 95.32% | ₹36.15 L |
| West | 2,609 | 24.2% | 94.52% | ₹27.04 L |
| East | 1,252 | 11.6% | 95.93% | ₹15.02 L |
| Central | 989 | 9.2% | 94.64% | ₹7.74 L |

### Largest merchants by settled value

| Merchant | Tier | Category | Attempts | Success | Settled value |
|---|---|---|---|---|---|
| Vega Electronics | Large | Retail | 31 | 93.55% | ₹4.30 L |
| Rapid Bazaar | Key Account | Retail | 315 | 92.06% | ₹1.40 L |
| Vasant Wardrobe | Key Account | Retail | 48 | 91.67% | ₹1.10 L |
| Hampi Styles | Key Account | Retail | 37 | 83.78% | ₹70,436 |
| Shakti Stores 1531 | Key Account | Retail | 72 | 95.83% | ₹65,804 |
| Yamuna Restaurant | Key Account | Food & Beverage | 67 | 97.01% | ₹64,267 |
| Ujjwal Water Board | Key Account | Bills | 32 | 90.62% | ₹62,115 |
| Hampi Stores 2298 | Key Account | Retail | 83 | 97.59% | ₹58,830 |

## Failure analysis

Of 502 declined attempts, 390 were business declines (3.613% of attempts — balances, PINs and limits), 55 technical (0.510%), 38 timeouts (0.352%) and 19 risk declines (0.176%).

215 attempts were re-presentations of an earlier failure (1.99% of the day); 63.7% of them succeeded.

- Retries reached 215 attempts (1.99% of the day, 4.3 sigma above normal). 63.7% of re-presented payments recovered, so the retry path was doing its job.
- Decline code ZM (Invalid UPI PIN) fired 150 times — 1.390% of attempts against a trailing 1.101%. Owner: Customer.
- Decline code YA (PSP not available) fired 13 times — 0.120% of attempts against a trailing 0.053%. Owner: PSP.
- Decline code U16 (Risk threshold exceeded at remitter) fired 17 times — 0.158% of attempts against a trailing 0.095%. Owner: Issuer.

| Code | Reason | Bucket | Owner | Count | Rate today | 28d median rate |
|---|---|---|---|---|---|---|
| ZM | Invalid UPI PIN | business | Customer | 150 | 1.390% | 1.101% |
| Z9 | Insufficient funds | business | Customer | 147 | 1.362% | 1.420% |
| ZA | Transaction declined by customer | business | Customer | 39 | 0.361% | 0.410% |
| XH | Account does not exist / frozen | business | Issuer | 28 | 0.259% | 0.240% |
| U30 | Debit failed at remitter bank | technical | Issuer | 20 | 0.185% | 0.165% |
| U54 | Transaction timed out at beneficiary | timeout | Issuer | 19 | 0.176% | 0.164% |
| U16 | Risk threshold exceeded at remitter | risk | Issuer | 17 | 0.158% | 0.095% |
| ZX | Mandate not found or revoked | business | PSP | 14 | 0.130% | 0.091% |

## Refunds, reversals and disputes

| Flow | Today | 28d median |
|---|---|---|
| Refunds | 80 | 68 |
| Auto-reversals | 29 | 20 |
| Disputes / chargebacks | 12 | 9 |
| Value returned | ₹2.80 L | ₹89,740 |

## Customer behaviour

9,176 distinct customers transacted (−1.4% on the 28-day median) at 1.18 attempts each.

| Segment | Active customers | Attempts | Attempts / customer | Success | Avg ticket |
|---|---|---|---|---|---|
| regular | 2,821 | 3,167 | 1.12 | 95.17% | ₹1,143 |
| power | 1,992 | 2,597 | 1.30 | 94.53% | ₹1,628 |
| merchant_heavy | 2,037 | 2,384 | 1.17 | 95.72% | ₹1,040 |
| small_ticket | 1,349 | 1,622 | 1.20 | 96.05% | ₹505 |
| occasional | 760 | 798 | 1.05 | 94.36% | ₹1,417 |
| new | 184 | 192 | 1.04 | 95.31% | ₹1,777 |
| dormant_returning | 33 | 33 | 1.00 | 100.00% | ₹620 |

## Operational events

- **INC-FRAUD-0046** (Sev-2) — Fraud pattern on UPI Lite Auto Top-Up — Education Fees, scoped to UPI_LITE_ATU. Coordinated fraud attempts concentrated on UPI Lite Auto Top-Up at Education Fees merchants. Risk declines (U16/K1) climbed until rules were tightened and the ring was shut down.
- **MAINT-0086** (Sev-3) — Bank of Baroda scheduled CBS maintenance, scoped to Bank of Baroda between 02:00 and 06:00. Bank of Baroda runs its announced core-banking maintenance slot every 30 days in the overnight window. Remitter debits are rejected outright for the duration and PSPs suppress retries until it closes, so the dip is expected and should not be paged on.
- **ONBRD-0088** (Sev-3) — Grocery acquirer onboarding drive, scoped to 5411. An acquiring push signed a cohort of new Grocery merchants. Newly onboarded terminals carry configuration errors and unfamiliar staff, so volume rises while the category's success rate dips until the cohort settles.
- **CMP-0065** (Sev-3) — OTT & Subscriptions cashback campaign, scoped to 5815. A cashback campaign across OTT & Subscriptions merchants lifted volume sharply. Ticket sizes fell as customers split baskets to maximise the offer.

## Risks and opportunities

### Risks

- Category Retail ran at 94.56% success on 2,795 attempts (41.9% of the day), 1.57pp down its own 28-day median.
- Decline code ZM (Invalid UPI PIN) fired 150 times — 1.390% of attempts against a trailing 1.101%. Owner: Customer.
- Product UPI Circle is compounding — attempts up 69% across the trailing window to 173 today, but success is slipping as it scales, so the growth is outrunning its reliability.
- Product UPI Person to Merchant ran at 95.03% success on 2,838 attempts (26.3% of the day), 0.94pp down its own 28-day median.
- Decline code YA (PSP not available) fired 13 times — 0.120% of attempts against a trailing 0.053%. Owner: PSP.

### Opportunities

- Product UPI International is compounding — attempts up 45% across the trailing window to 113 today, with success holding, so the growth is healthy and worth funding.

## Executive observation

12 March was an incident day: INC-FRAUD-0046 was live and the rail closed at 95.23% success against a 95.62% baseline. Priority is confirming the fix held rather than reading the day's demand signal, which the incident contaminates.

## Evidence

Every figure in this report is a SQL aggregate over raw transaction rows; none of it is read from a precomputed summary.

- Corpus window queried: `2026-03-12` plus the 28 preceding days, over `enterprise_data/warehouse/transactions/`.
- Day totals: attempts=10,793, successes=10,278, failed=502, pending=13, settled_value_inr=12,638,754.00.
- Every rate is computed as a share of attempts on this date; every '28d median' is that entity's own median over the preceding 28 days, excluding today.
- failures: retries=215; retry_share_pct=1.99; recovery_pct=63.72; z=4.32
- categories: mcc_category=Retail; attempts=2,795; success_rate=94.56; own_median=96.14; z=-3.84
- failures: failure_code=ZM; count=150; rate_pct=1.39; trailing_rate_pct=1.1; owner=Customer; z=2.12
- products: product_name=UPI Circle; attempts=173; window_growth_pct=69; success_rate=95.38
- products: product_name=UPI Person to Merchant; attempts=2,838; success_rate=95.03; own_median=95.97; z=-3.34
- incidents: event_id=INC-FRAUD-0046; kind=fraud_spike; severity=Sev-2; window=2026-03-05 to 2026-03-16; success_impact_pp=-1.21; volume_impact_pct=6.66
- products: product_name=UPI International; attempts=113; window_growth_pct=44.6; success_rate=93.81
- failures: failure_code=YA; count=13; rate_pct=0.12; trailing_rate_pct=0.05; owner=PSP; z=3.28
- failures: failure_code=U16; count=17; rate_pct=0.16; trailing_rate_pct=0.09; owner=Issuer; z=2.62
- banks: payer_bank=HDFC Bank; attempts=1,169; success_rate=95.04; own_median=96.23; z=-2.05

Refs: enterprise_data/warehouse/transactions, RPT-D66-DAILY, enterprise_data/warehouse/reference/incidents.parquet
