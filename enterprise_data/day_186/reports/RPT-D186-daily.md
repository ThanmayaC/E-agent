---
id: RPT-D186-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-09T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 09 Jul 2026)

**Report ID:** RPT-D186-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 09 Jul 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 186 of 206)

## Transaction summary
The rail processed 903.8M UPI transactions on Thursday — a campaign-driven high-volume day — up 173.9M on the same day last week. Success landed at 99.98% and settlement at 99.34%, held back by live issues on UPI 123Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 903.8  (▲161.0 d/d, ▲173.9 w/w, ▲107.9 m/m)
- **Success Rate:** 99.98%  (▲0.97 d/d, ▲0.54 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.34%  (▼0.33 d/d, ▼0.64 w/w, ▼0.61 m/m)
- **Technical Declines:** 0.31%  (▼0.04 d/d, ▲0.03 w/w, ▼0.24 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 999  (▼70 d/d, ▲66 w/w, ▼1143 m/m)
- **Merchant Complaints:** 90  (▼1 d/d, ▼4 w/w, ▼144 m/m)
- **Fraud Alerts:** 722  (▼7 d/d, ▼12 w/w, ▼438 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 551 ms  (▼8 d/d, ▲7 w/w, ▼202 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 294.2 | 99.67% |
| HDFC Bank | 96.6 | 99.42% |
| Bank of Baroda | 69.6 | 99.26% |
| Union Bank of India | 61.0 | 99.63% |
| Axis Bank | 55.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 431.7 | 99.51% | 198 ms |
| Google Pay | 295.6 | 99.35% | 241 ms |
| Paytm | 71.7 | 99.53% | 201 ms |
| Navi | 33.2 | 99.53% | 304 ms |
| SuperMoney | 17.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 334.4 |
| Person to Person | 320.8 |
| QR Payments | 85.9 |
| UPI Lite | 43.4 |
| UPI Autopay | 29.8 |

## Failure analysis
- INC-2026-10 — feature-level degradation on UPI 123Pay (day 3 of 5); see RCA-2026-10.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI 123Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D186-MON) and any meetings/emails on 09 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D186-MON, RPT-D185-DAILY, INC-2026-10, RCA-2026-10
