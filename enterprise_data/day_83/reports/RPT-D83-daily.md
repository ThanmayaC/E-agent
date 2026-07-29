---
id: RPT-D83-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-28T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 28 Mar 2026)

**Report ID:** RPT-D83-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 28 Mar 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 83 of 206)

## Transaction summary
The rail processed 788.2M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 176.6M on the same day last week. Success landed at 99.07% and settlement at 99.98%, held back by live issues on RuPay Credit on UPI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 788.2  (▲93.6 d/d, ▲176.6 w/w, ▼7.7 m/m)
- **Success Rate:** 99.07%  (▼0.91 d/d, ▲0.67 w/w, ▼0.06 m/m)
- **Settlement Success:** 99.98%  (▲0.34 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.44%  (▼0.03 d/d, ▼0.11 w/w, ▼0.11 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,534  (▼93 d/d, ▼397 w/w, ▼608 m/m)
- **Merchant Complaints:** 155  (▼3 w/w, ▼79 m/m)
- **Fraud Alerts:** 929  (▼14 d/d, ▼24 w/w, ▼231 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼8 m/m)
- **Response Time:** 661 ms  (▼4 d/d, ▼86 w/w, ▼92 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 256.6 | 99.67% |
| HDFC Bank | 84.3 | 99.42% |
| Bank of Baroda | 60.7 | 99.26% |
| Union Bank of India | 53.2 | 99.63% |
| Axis Bank | 48.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 376.5 | 99.51% | 198 ms |
| Google Pay | 257.8 | 99.35% | 241 ms |
| Paytm | 62.5 | 99.53% | 201 ms |
| Navi | 29.0 | 99.53% | 304 ms |
| SuperMoney | 15.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 291.6 |
| Person to Person | 279.8 |
| QR Payments | 74.9 |
| UPI Lite | 37.8 |
| UPI Autopay | 26.0 |

## Failure analysis
- INC-2026-21 — feature-level degradation on RuPay Credit on UPI (day 4 of 4); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on RuPay Credit on UPI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D83-MON) and any meetings/emails on 28 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D83-MON, RPT-D82-DAILY, INC-2026-21, RCA-2026-21
