---
id: RPT-D84-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-13T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 13 Sep 2026)

**Report ID:** RPT-D84-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 13 Sep 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 84 of 180)

## Transaction summary
The rail processed 715.5M UPI transactions on Sunday — a quiet Sunday — up 7.1M on the same day last week. Success held at 98.78% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 715.5  (▼90.5 d/d, ▲7.1 w/w, ▼29.4 m/m)
- **Success Rate:** 98.78%  (▼1.03 d/d, ▼0.41 w/w, ▼0.82 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.33%  (▼0.12 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,307  (▼26 d/d, ▼51 w/w, ▼635 m/m)
- **Merchant Complaints:** 137  (▼1 d/d, ▼4 w/w, ▼74 m/m)
- **Fraud Alerts:** 848  (▼2 d/d, ▼22 w/w, ▼203 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 633 ms  (▲2 d/d, ▼5 w/w, ▼109 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.1 | 99.5% |
| HDFC Bank | 78.9 | 99.55% |
| Bank of Baroda | 56.7 | 99.64% |
| Union Bank of India | 49.3 | 99.43% |
| ICICI Bank | 44.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 341.4 | 99.14% | 231 ms |
| Google Pay | 233.7 | 99.17% | 316 ms |
| Paytm | 57.7 | 99.06% | 192 ms |
| Navi | 26.4 | 99.17% | 225 ms |
| SuperMoney | 13.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 268.3 |
| Person to Person | 254.0 |
| QR Payments | 68.0 |
| UPI Lite | 34.3 |
| UPI Autopay | 23.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D84-MON) and any meetings/emails on 13 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D84-MON, RPT-D83-DAILY
