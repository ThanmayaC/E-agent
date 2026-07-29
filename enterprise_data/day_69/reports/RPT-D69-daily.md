---
id: RPT-D69-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-29T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 29 Aug 2026)

**Report ID:** RPT-D69-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 29 Aug 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 69 of 180)

## Transaction summary
The rail processed 952.1M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 197.6M on the same day last week. Success held at 99.5% and settlement at 99.1%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 952.1  (▼1.1 d/d, ▲197.6 w/w, ▲207.2 m/m)
- **Success Rate:** 99.5%  (▼0.1 d/d, ▼0.48 w/w, ▼0.1 m/m)
- **Settlement Success:** 99.1%  (▼0.8 d/d, ▼0.88 w/w, ▼0.33 m/m)
- **Technical Declines:** 0.35%  (▼0.11 w/w, ▼0.1 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,411  (▼14 d/d, ▼335 w/w, ▼531 m/m)
- **Merchant Complaints:** 148  (▼1 d/d, ▼5 w/w, ▼63 m/m)
- **Fraud Alerts:** 879  (▼7 d/d, ▼31 w/w, ▼172 m/m)
- **Risk Score:** 25  (▼6 m/m)
- **Response Time:** 645 ms  (▼5 d/d, ▼41 w/w, ▼97 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 306.1 | 99.5% |
| HDFC Bank | 105.0 | 99.55% |
| Bank of Baroda | 75.5 | 99.64% |
| Union Bank of India | 65.6 | 99.43% |
| ICICI Bank | 58.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 454.2 | 99.14% | 231 ms |
| Google Pay | 311.0 | 99.17% | 316 ms |
| Paytm | 76.8 | 99.06% | 192 ms |
| Navi | 35.1 | 99.17% | 225 ms |
| SuperMoney | 18.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 357.0 |
| Person to Person | 338.0 |
| QR Payments | 90.4 |
| UPI Lite | 45.7 |
| UPI Autopay | 31.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D69-MON) and any meetings/emails on 29 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D69-MON, RPT-D68-DAILY
