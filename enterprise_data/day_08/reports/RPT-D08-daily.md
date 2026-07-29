---
id: RPT-D08-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-29T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 29 Jun 2026)

**Report ID:** RPT-D08-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 29 Jun 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 8 of 180)

## Transaction summary
The rail processed 861.8M UPI transactions on Monday — the month-end surge as salary and bill-pay flows land — up 116.9M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 861.8  (▲12.3 d/d, ▲116.9 w/w, ▲116.9 m/m)
- **Success Rate:** 99.98%  (▲0.38 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.44%  (▼0.01 w/w, ▼0.01 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 1,895  (▼10 d/d, ▼47 w/w, ▼47 m/m)
- **Merchant Complaints:** 204  (▼7 w/w, ▼7 m/m)
- **Fraud Alerts:** 1,025  (▼11 d/d, ▼26 w/w, ▼26 m/m)
- **Risk Score:** 30  (▼1 d/d, ▼1 w/w, ▼1 m/m)
- **Response Time:** 719 ms  (▼11 d/d, ▼23 w/w, ▼23 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 277.1 | 99.5% |
| HDFC Bank | 95.1 | 99.55% |
| Bank of Baroda | 68.3 | 99.64% |
| Union Bank of India | 59.4 | 99.43% |
| ICICI Bank | 53.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 411.1 | 99.14% | 231 ms |
| Google Pay | 281.5 | 99.17% | 316 ms |
| Paytm | 69.5 | 99.06% | 192 ms |
| Navi | 31.8 | 99.17% | 225 ms |
| SuperMoney | 16.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 323.2 |
| Person to Person | 305.9 |
| QR Payments | 81.9 |
| UPI Lite | 41.4 |
| UPI Autopay | 28.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.44% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D08-MON) and any meetings/emails on 29 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D08-MON, RPT-D07-DAILY
