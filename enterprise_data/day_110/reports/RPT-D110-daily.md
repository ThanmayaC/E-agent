---
id: RPT-D110-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-09T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 09 Oct 2026)

**Report ID:** RPT-D110-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 09 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 110 of 180)

## Transaction summary
The rail processed 901.9M UPI transactions on Friday — a steady mid-week day — down 228.8M on the same day last week. Success held at 99.41% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 901.9  (▼12.3 d/d, ▼228.8 w/w, ▲157.0 m/m)
- **Success Rate:** 99.41%  (▼0.03 d/d, ▼0.57 w/w, ▼0.19 m/m)
- **Settlement Success:** 99.98%  (▲0.8 d/d, ▲0.81 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,169  (▲5 d/d, ▼58 w/w, ▼773 m/m)
- **Merchant Complaints:** 119  (▼2 d/d, ▼21 w/w, ▼92 m/m)
- **Fraud Alerts:** 806  (▼3 d/d, ▼8 w/w, ▼245 m/m)
- **Risk Score:** 22  (▼9 m/m)
- **Response Time:** 601 ms  (▼3 d/d, ▼7 w/w, ▼141 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 290.0 | 99.5% |
| HDFC Bank | 99.5 | 99.55% |
| Bank of Baroda | 71.5 | 99.64% |
| Union Bank of India | 62.1 | 99.43% |
| ICICI Bank | 55.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 430.3 | 99.14% | 231 ms |
| Google Pay | 294.6 | 99.17% | 316 ms |
| Paytm | 72.8 | 99.06% | 192 ms |
| Navi | 33.2 | 99.17% | 225 ms |
| SuperMoney | 17.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 338.2 |
| Person to Person | 320.2 |
| QR Payments | 85.7 |
| UPI Lite | 43.3 |
| UPI Autopay | 29.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D110-MON) and any meetings/emails on 09 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D110-MON, RPT-D109-DAILY
