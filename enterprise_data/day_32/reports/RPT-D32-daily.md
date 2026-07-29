---
id: RPT-D32-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-23T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 23 Jul 2026)

**Report ID:** RPT-D32-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 23 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 32 of 180)

## Transaction summary
The rail processed 781.6M UPI transactions on Thursday — a steady mid-week day — up 2.5M on the same day last week. Success held at 99.48% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 781.6  (▼27.1 d/d, ▲2.5 w/w, ▲36.7 m/m)
- **Success Rate:** 99.48%  (▼0.14 d/d, ▼0.5 w/w, ▼0.12 m/m)
- **Settlement Success:** 99.98%  (▲0.78 d/d, ▲0.93 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.4%  (▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,682  (▼24 d/d, ▼53 w/w, ▼260 m/m)
- **Merchant Complaints:** 179  (▼1 d/d, ▼8 w/w, ▼32 m/m)
- **Fraud Alerts:** 980  (▲11 d/d, ▼14 w/w, ▼71 m/m)
- **Risk Score:** 28  (▼1 w/w, ▼3 m/m)
- **Response Time:** 687 ms  (▼3 d/d, ▼13 w/w, ▼55 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 251.3 | 99.5% |
| HDFC Bank | 86.2 | 99.55% |
| Bank of Baroda | 62.0 | 99.64% |
| Union Bank of India | 53.8 | 99.43% |
| ICICI Bank | 48.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 372.9 | 99.14% | 231 ms |
| Google Pay | 255.3 | 99.17% | 316 ms |
| Paytm | 63.1 | 99.06% | 192 ms |
| Navi | 28.8 | 99.17% | 225 ms |
| SuperMoney | 15.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 293.1 |
| Person to Person | 277.5 |
| QR Payments | 74.3 |
| UPI Lite | 37.5 |
| UPI Autopay | 25.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D32-MON) and any meetings/emails on 23 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D32-MON, RPT-D31-DAILY
