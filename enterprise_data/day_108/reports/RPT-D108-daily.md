---
id: RPT-D108-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-07T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 07 Oct 2026)

**Report ID:** RPT-D108-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 07 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 108 of 180)

## Transaction summary
The rail processed 929.4M UPI transactions on Wednesday — a steady mid-week day — down 76.0M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 929.4  (▼5.9 d/d, ▼76.0 w/w, ▲184.5 m/m)
- **Success Rate:** 99.98%  (▲1.17 d/d, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.07 d/d, ▲1.14 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.04 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,181  (▲9 d/d, ▼124 w/w, ▼761 m/m)
- **Merchant Complaints:** 121  (▼66 w/w, ▼90 m/m)
- **Fraud Alerts:** 801  (▲2 d/d, ▼23 w/w, ▼250 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼9 m/m)
- **Response Time:** 603 ms  (▼1 d/d, ▼13 w/w, ▼139 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 298.8 | 99.5% |
| HDFC Bank | 102.5 | 99.55% |
| Bank of Baroda | 73.7 | 99.64% |
| Union Bank of India | 64.0 | 99.43% |
| ICICI Bank | 57.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 443.4 | 99.14% | 231 ms |
| Google Pay | 303.6 | 99.17% | 316 ms |
| Paytm | 75.0 | 99.06% | 192 ms |
| Navi | 34.3 | 99.17% | 225 ms |
| SuperMoney | 18.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 348.5 |
| Person to Person | 329.9 |
| QR Payments | 88.3 |
| UPI Lite | 44.6 |
| UPI Autopay | 30.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D108-MON) and any meetings/emails on 07 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D108-MON, RPT-D107-DAILY
