---
id: RPT-D180-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-18T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 18 Dec 2026)

**Report ID:** RPT-D180-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 18 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 180 of 180)

## Transaction summary
The rail processed 1055.4M UPI transactions on Friday — a steady mid-week day — down 247.5M on the same day last week. Success held at 99.57% and settlement at 99.33%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1055.4  (▼234.7 d/d, ▼247.5 w/w, ▲310.5 m/m)
- **Success Rate:** 99.57%  (▲0.07 d/d, ▲0.39 w/w, ▼0.03 m/m)
- **Settlement Success:** 99.33%  (▼0.65 d/d, ▼0.55 w/w, ▼0.1 m/m)
- **Technical Declines:** 0.23%  (▼0.22 m/m)
- **Business Declines:** 0.13%  (▼0.01 w/w, ▼0.07 m/m)
- **Customer Complaints:** 839  (▼11 d/d, ▼54 w/w, ▼1103 m/m)
- **Merchant Complaints:** 84  (▼26 w/w, ▼127 m/m)
- **Fraud Alerts:** 670  (▼2 d/d, ▼17 w/w, ▼381 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 531 ms  (▼1 d/d, ▼9 w/w, ▼211 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 339.3 | 99.5% |
| HDFC Bank | 116.4 | 99.55% |
| Bank of Baroda | 83.7 | 99.64% |
| Union Bank of India | 72.7 | 99.43% |
| ICICI Bank | 65.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 503.5 | 99.14% | 231 ms |
| Google Pay | 344.7 | 99.17% | 316 ms |
| Paytm | 85.1 | 99.06% | 192 ms |
| Navi | 38.9 | 99.17% | 225 ms |
| SuperMoney | 20.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 395.8 |
| Person to Person | 374.7 |
| QR Payments | 100.3 |
| UPI Lite | 50.7 |
| UPI Autopay | 34.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.23% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D180-MON) and any meetings/emails on 18 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D180-MON, RPT-D179-DAILY
