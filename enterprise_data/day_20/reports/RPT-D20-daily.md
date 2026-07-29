---
id: RPT-D20-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-11T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 11 Jul 2026)

**Report ID:** RPT-D20-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 11 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 20 of 180)

## Transaction summary
The rail processed 705.8M UPI transactions on Saturday — a lighter Saturday — up 9.4M on the same day last week. Success held at 98.94% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 705.8  (▼66.7 d/d, ▲9.4 w/w, ▼39.1 m/m)
- **Success Rate:** 98.94%  (▼0.37 d/d, ▲0.21 w/w, ▼0.66 m/m)
- **Settlement Success:** 99.98%  (▲0.35 d/d, ▲0.57 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.42%  (▼0.06 w/w, ▼0.03 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,771  (▼28 d/d, ▼250 w/w, ▼171 m/m)
- **Merchant Complaints:** 189  (▼1 d/d, ▼10 w/w, ▼22 m/m)
- **Fraud Alerts:** 992  (▼21 d/d, ▼22 w/w, ▼59 m/m)
- **Risk Score:** 29  (▼1 w/w, ▼2 m/m)
- **Response Time:** 713 ms  (▲6 d/d, ▼46 w/w, ▼29 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 226.9 | 99.5% |
| HDFC Bank | 77.9 | 99.55% |
| Bank of Baroda | 56.0 | 99.64% |
| Union Bank of India | 48.6 | 99.43% |
| ICICI Bank | 43.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 336.7 | 99.14% | 231 ms |
| Google Pay | 230.5 | 99.17% | 316 ms |
| Paytm | 56.9 | 99.06% | 192 ms |
| Navi | 26.0 | 99.17% | 225 ms |
| SuperMoney | 13.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 264.7 |
| Person to Person | 250.6 |
| QR Payments | 67.1 |
| UPI Lite | 33.9 |
| UPI Autopay | 23.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D20-MON) and any meetings/emails on 11 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D20-MON, RPT-D19-DAILY
