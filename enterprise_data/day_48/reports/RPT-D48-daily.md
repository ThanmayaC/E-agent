---
id: RPT-D48-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-08T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 08 Aug 2026)

**Report ID:** RPT-D48-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 08 Aug 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 48 of 180)

## Transaction summary
The rail processed 754.6M UPI transactions on Saturday — a lighter Saturday — up 41.0M on the same day last week. Success held at 99.98% and settlement at 99.91%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 754.6  (▼52.3 d/d, ▲41.0 w/w, ▲9.7 m/m)
- **Success Rate:** 99.98%  (▲1.3 d/d, ▲1.37 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.91%  (▲0.01 d/d, ▲0.3 w/w, ▲0.48 m/m)
- **Technical Declines:** 0.37%  (▼0.02 w/w, ▼0.08 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,562  (▼16 d/d, ▼65 w/w, ▼380 m/m)
- **Merchant Complaints:** 165  (▼1 d/d, ▼7 w/w, ▼46 m/m)
- **Fraud Alerts:** 929  (▼10 d/d, ▼24 w/w, ▼122 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼4 m/m)
- **Response Time:** 678 ms  (▲4 d/d, ▼4 w/w, ▼64 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.6 | 99.5% |
| HDFC Bank | 83.2 | 99.55% |
| Bank of Baroda | 59.8 | 99.64% |
| Union Bank of India | 52.0 | 99.43% |
| ICICI Bank | 46.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 360.0 | 99.14% | 231 ms |
| Google Pay | 246.5 | 99.17% | 316 ms |
| Paytm | 60.9 | 99.06% | 192 ms |
| Navi | 27.8 | 99.17% | 225 ms |
| SuperMoney | 14.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 283.0 |
| Person to Person | 267.9 |
| QR Payments | 71.7 |
| UPI Lite | 36.2 |
| UPI Autopay | 24.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D48-MON) and any meetings/emails on 08 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D48-MON, RPT-D47-DAILY
