---
id: RPT-D68-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-28T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 28 Aug 2026)

**Report ID:** RPT-D68-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 28 Aug 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 68 of 180)

## Transaction summary
The rail processed 953.2M UPI transactions on Friday — the month-end surge as salary and bill-pay flows land — down 80.1M on the same day last week. Success held at 99.6% and settlement at 99.9%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 953.2  (▲86.5 d/d, ▼80.1 w/w, ▲208.3 m/m)
- **Success Rate:** 99.6%  (▼0.36 d/d, ▲0.67 w/w)
- **Settlement Success:** 99.9%  (▼0.08 d/d, ▼0.08 w/w, ▲0.47 m/m)
- **Technical Declines:** 0.35%  (▼0.18 w/w, ▼0.1 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,425  (▲1 d/d, ▼473 w/w, ▼517 m/m)
- **Merchant Complaints:** 149  (▼1 d/d, ▼6 w/w, ▼62 m/m)
- **Fraud Alerts:** 886  (▼13 d/d, ▼14 w/w, ▼165 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼6 m/m)
- **Response Time:** 650 ms  (▼1 d/d, ▼48 w/w, ▼92 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 306.5 | 99.5% |
| HDFC Bank | 105.2 | 99.55% |
| Bank of Baroda | 75.6 | 99.64% |
| Union Bank of India | 65.7 | 99.43% |
| ICICI Bank | 58.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 454.8 | 99.14% | 231 ms |
| Google Pay | 311.3 | 99.17% | 316 ms |
| Paytm | 76.9 | 99.06% | 192 ms |
| Navi | 35.1 | 99.17% | 225 ms |
| SuperMoney | 18.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 357.5 |
| Person to Person | 338.4 |
| QR Payments | 90.6 |
| UPI Lite | 45.8 |
| UPI Autopay | 31.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D68-MON) and any meetings/emails on 28 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D68-MON, RPT-D67-DAILY
