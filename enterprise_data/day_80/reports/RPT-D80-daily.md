---
id: RPT-D80-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-09T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 09 Sep 2026)

**Report ID:** RPT-D80-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 09 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 80 of 180)

## Transaction summary
The rail processed 867.2M UPI transactions on Wednesday — a steady mid-week day — up 12.5M on the same day last week. Success held at 98.92% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 867.2  (▼15.0 d/d, ▲12.5 w/w, ▲122.3 m/m)
- **Success Rate:** 98.92%  (▼1.06 d/d, ▼1.06 w/w, ▼0.68 m/m)
- **Settlement Success:** 99.98%  (▲1.06 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.33%  (▼0.01 d/d, ▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,330  (▼20 d/d, ▼72 w/w, ▼612 m/m)
- **Merchant Complaints:** 139  (▼1 d/d, ▼4 w/w, ▼72 m/m)
- **Fraud Alerts:** 865  (▲3 d/d, ▼13 w/w, ▼186 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼7 m/m)
- **Response Time:** 632 ms  (▲1 d/d, ▼6 w/w, ▼110 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 278.8 | 99.5% |
| HDFC Bank | 95.7 | 99.55% |
| Bank of Baroda | 68.8 | 99.64% |
| Union Bank of India | 59.7 | 99.43% |
| ICICI Bank | 53.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 413.7 | 99.14% | 231 ms |
| Google Pay | 283.3 | 99.17% | 316 ms |
| Paytm | 70.0 | 99.06% | 192 ms |
| Navi | 32.0 | 99.17% | 225 ms |
| SuperMoney | 16.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 325.2 |
| Person to Person | 307.9 |
| QR Payments | 82.4 |
| UPI Lite | 41.6 |
| UPI Autopay | 28.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D80-MON) and any meetings/emails on 09 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D80-MON, RPT-D79-DAILY
