---
id: RPT-D52-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-12T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 12 Aug 2026)

**Report ID:** RPT-D52-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 12 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 52 of 180)

## Transaction summary
The rail processed 830.8M UPI transactions on Wednesday — a steady mid-week day — up 13.3M on the same day last week. Success held at 99.98% and settlement at 99.82%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 830.8  (▲23.3 d/d, ▲13.3 w/w, ▲85.9 m/m)
- **Success Rate:** 99.98%  (▲0.29 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.82%  (▲0.92 d/d, ▼0.16 w/w, ▲0.39 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,533  (▼20 d/d, ▼57 w/w, ▼409 m/m)
- **Merchant Complaints:** 162  (▼1 d/d, ▼7 w/w, ▼49 m/m)
- **Fraud Alerts:** 930  (▲5 d/d, ▼19 w/w, ▼121 m/m)
- **Risk Score:** 26  (▼1 d/d, ▼1 w/w, ▼5 m/m)
- **Response Time:** 667 ms  (▲3 d/d, ▼13 w/w, ▼75 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 267.1 | 99.5% |
| HDFC Bank | 91.7 | 99.55% |
| Bank of Baroda | 65.9 | 99.64% |
| Union Bank of India | 57.2 | 99.43% |
| ICICI Bank | 51.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 396.4 | 99.14% | 231 ms |
| Google Pay | 271.4 | 99.17% | 316 ms |
| Paytm | 67.0 | 99.06% | 192 ms |
| Navi | 30.6 | 99.17% | 225 ms |
| SuperMoney | 16.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 311.5 |
| Person to Person | 294.9 |
| QR Payments | 78.9 |
| UPI Lite | 39.9 |
| UPI Autopay | 27.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D52-MON) and any meetings/emails on 12 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D52-MON, RPT-D51-DAILY
