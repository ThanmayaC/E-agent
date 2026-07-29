---
id: RPT-D24-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-15T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 15 Jul 2026)

**Report ID:** RPT-D24-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 15 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 24 of 180)

## Transaction summary
The rail processed 780.3M UPI transactions on Wednesday — a steady mid-week day — up 13.6M on the same day last week. Success held at 99.42% and settlement at 99.84%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 780.3  (▲3.7 d/d, ▲13.6 w/w, ▲35.4 m/m)
- **Success Rate:** 99.42%  (▼0.56 d/d, ▼0.56 w/w, ▼0.18 m/m)
- **Settlement Success:** 99.84%  (▼0.14 d/d, ▼0.14 w/w, ▲0.41 m/m)
- **Technical Declines:** 0.41%  (▼0.02 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.05 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,755  (▼19 d/d, ▼287 w/w, ▼187 m/m)
- **Merchant Complaints:** 186  (▼2 d/d, ▼8 w/w, ▼25 m/m)
- **Fraud Alerts:** 990  (▲2 d/d, ▼146 w/w, ▼61 m/m)
- **Risk Score:** 29  (▼9 w/w, ▼2 m/m)
- **Response Time:** 709 ms  (▲3 d/d, ▼10 w/w, ▼33 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 250.9 | 99.5% |
| HDFC Bank | 86.1 | 99.55% |
| Bank of Baroda | 61.9 | 99.64% |
| Union Bank of India | 53.8 | 99.43% |
| ICICI Bank | 48.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 372.3 | 99.14% | 231 ms |
| Google Pay | 254.9 | 99.17% | 316 ms |
| Paytm | 63.0 | 99.06% | 192 ms |
| Navi | 28.8 | 99.17% | 225 ms |
| SuperMoney | 15.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 292.6 |
| Person to Person | 277.0 |
| QR Payments | 74.1 |
| UPI Lite | 37.5 |
| UPI Autopay | 25.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D24-MON) and any meetings/emails on 15 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D24-MON, RPT-D23-DAILY
