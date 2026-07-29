---
id: RPT-D32-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-05T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 05 Feb 2026)

**Report ID:** RPT-D32-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 05 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 32 of 206)

## Transaction summary
The rail processed 685.5M UPI transactions on Thursday — a steady mid-week day — down 58.9M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 685.5  (▲20.1 d/d, ▼58.9 w/w, ▼110.4 m/m)
- **Success Rate:** 99.98%  (▲1.37 d/d, ▲0.05 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.12 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.49%  (▼0.01 w/w, ▼0.06 m/m)
- **Business Declines:** 0.33%  (▼0.06 d/d, ▲0.1 w/w, ▲0.09 m/m)
- **Customer Complaints:** 2,252  (▼273 d/d, ▲348 w/w, ▲110 m/m)
- **Merchant Complaints:** 198  (▼5 d/d, ▼11 w/w, ▼36 m/m)
- **Fraud Alerts:** 1,297  (▼122 d/d, ▲224 w/w, ▲137 m/m)
- **Risk Score:** 47  (▼10 d/d, ▲15 w/w, ▲13 m/m)
- **Response Time:** 720 ms  (▲4 d/d, ▼1 w/w, ▼33 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 223.1 | 99.67% |
| HDFC Bank | 73.3 | 99.42% |
| Bank of Baroda | 52.8 | 99.26% |
| Union Bank of India | 46.2 | 99.63% |
| Axis Bank | 42.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 327.4 | 99.51% | 198 ms |
| Google Pay | 224.2 | 99.35% | 241 ms |
| Paytm | 54.4 | 99.53% | 201 ms |
| Navi | 25.2 | 99.53% | 304 ms |
| SuperMoney | 13.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 253.6 |
| Person to Person | 243.4 |
| QR Payments | 65.1 |
| UPI Lite | 32.9 |
| UPI Autopay | 22.6 |

## Failure analysis
- INC-2026-02 — fraud / risk spike on HDFC MobileBanking (day 2 of 5); see RCA-2026-02.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D32-MON) and any meetings/emails on 05 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D32-MON, RPT-D31-DAILY, INC-2026-02, RCA-2026-02
