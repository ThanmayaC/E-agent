---
id: RPT-D79-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-24T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 24 Mar 2026)

**Report ID:** RPT-D79-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 24 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 79 of 206)

## Transaction summary
The rail processed 693.7M UPI transactions on Tuesday — a steady mid-week day — up 2.3M on the same day last week. Success landed at 99.18% and settlement at 99.41%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 693.7  (▲17.8 d/d, ▲2.3 w/w, ▼102.2 m/m)
- **Success Rate:** 99.18%  (▲0.47 d/d, ▲0.15 w/w, ▲0.05 m/m)
- **Settlement Success:** 99.41%  (▼0.25 d/d, ▲0.03 w/w, ▼0.54 m/m)
- **Technical Declines:** 0.49%  (▼0.1 d/d, ▲0.07 w/w, ▼0.06 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,725  (▼324 d/d, ▲184 w/w, ▼417 m/m)
- **Merchant Complaints:** 157  (▼1 d/d, ▼7 w/w, ▼77 m/m)
- **Fraud Alerts:** 949  (▼4 d/d, ▼5 w/w, ▼211 m/m)
- **Risk Score:** 27  (▲1 d/d, ▼7 m/m)
- **Response Time:** 710 ms  (▼58 d/d, ▲49 w/w, ▼43 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 225.8 | 99.67% |
| HDFC Bank | 74.2 | 99.42% |
| Bank of Baroda | 53.4 | 99.26% |
| Union Bank of India | 46.8 | 99.63% |
| Axis Bank | 42.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 331.3 | 99.51% | 198 ms |
| Google Pay | 226.9 | 99.35% | 241 ms |
| Paytm | 55.0 | 99.53% | 201 ms |
| Navi | 25.5 | 99.53% | 304 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 256.7 |
| Person to Person | 246.3 |
| QR Payments | 65.9 |
| UPI Lite | 33.3 |
| UPI Autopay | 22.9 |

## Failure analysis
- INC-2026-12 — PSP callback latency increase on BHIM (day 2 of 2); see INC-2026-12.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D79-MON) and any meetings/emails on 24 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D79-MON, RPT-D78-DAILY, INC-2026-12
