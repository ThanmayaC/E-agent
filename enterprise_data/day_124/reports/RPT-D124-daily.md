---
id: RPT-D124-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-23T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 23 Oct 2026)

**Report ID:** RPT-D124-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 23 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 124 of 180)

## Transaction summary
The rail processed 952.6M UPI transactions on Friday — a steady mid-week day — up 16.5M on the same day last week. Success held at 99.98% and settlement at 99.51%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 952.6  (▲9.1 d/d, ▲16.5 w/w, ▲207.7 m/m)
- **Success Rate:** 99.98%  (▲0.73 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.51%  (▼0.31 d/d, ▼0.32 w/w, ▲0.08 m/m)
- **Technical Declines:** 0.28%  (▼0.11 w/w, ▼0.17 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,087  (▼7 d/d, ▼372 w/w, ▼855 m/m)
- **Merchant Complaints:** 110  (▼2 d/d, ▼4 w/w, ▼101 m/m)
- **Fraud Alerts:** 770  (▼12 d/d, ▼20 w/w, ▼281 m/m)
- **Risk Score:** 21  (▼2 w/w, ▼10 m/m)
- **Response Time:** 585 ms  (▼90 w/w, ▼157 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 306.3 | 99.5% |
| HDFC Bank | 105.1 | 99.55% |
| Bank of Baroda | 75.5 | 99.64% |
| Union Bank of India | 65.6 | 99.43% |
| ICICI Bank | 58.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 454.5 | 99.14% | 231 ms |
| Google Pay | 311.2 | 99.17% | 316 ms |
| Paytm | 76.9 | 99.06% | 192 ms |
| Navi | 35.1 | 99.17% | 225 ms |
| SuperMoney | 18.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 357.2 |
| Person to Person | 338.2 |
| QR Payments | 90.5 |
| UPI Lite | 45.7 |
| UPI Autopay | 31.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D124-MON) and any meetings/emails on 23 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D124-MON, RPT-D123-DAILY
