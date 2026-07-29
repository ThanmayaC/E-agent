---
id: RPT-D134-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-02T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 02 Nov 2026)

**Report ID:** RPT-D134-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 02 Nov 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 134 of 180)

## Transaction summary
The rail processed 946.7M UPI transactions on Monday — the Monday ramp-up after the weekend — up 21.4M on the same day last week. Success held at 99.01% and settlement at 99.87%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 946.7  (▲161.7 d/d, ▲21.4 w/w, ▲201.8 m/m)
- **Success Rate:** 99.01%  (▼0.17 d/d, ▲0.23 w/w, ▼0.59 m/m)
- **Settlement Success:** 99.87%  (▲0.61 d/d, ▲0.98 w/w, ▲0.44 m/m)
- **Technical Declines:** 0.27%  (▼0.19 w/w, ▼0.18 m/m)
- **Business Declines:** 0.14%  (▼0.01 d/d, ▼0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,036  (▼1 d/d, ▼511 w/w, ▼906 m/m)
- **Merchant Complaints:** 105  (▼6 d/d, ▼78 w/w, ▼106 m/m)
- **Fraud Alerts:** 758  (▼4 d/d, ▼7 w/w, ▼293 m/m)
- **Risk Score:** 20  (▼1 d/d, ▼1 w/w, ▼11 m/m)
- **Response Time:** 578 ms  (▼58 w/w, ▼164 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 304.4 | 99.5% |
| HDFC Bank | 104.4 | 99.55% |
| Bank of Baroda | 75.1 | 99.64% |
| Union Bank of India | 65.2 | 99.43% |
| ICICI Bank | 58.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 451.7 | 99.14% | 231 ms |
| Google Pay | 309.2 | 99.17% | 316 ms |
| Paytm | 76.4 | 99.06% | 192 ms |
| Navi | 34.9 | 99.17% | 225 ms |
| SuperMoney | 18.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 355.0 |
| Person to Person | 336.1 |
| QR Payments | 89.9 |
| UPI Lite | 45.4 |
| UPI Autopay | 31.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D134-MON) and any meetings/emails on 02 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D134-MON, RPT-D133-DAILY
