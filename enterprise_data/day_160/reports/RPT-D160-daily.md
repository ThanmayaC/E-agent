---
id: RPT-D160-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-28T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 28 Nov 2026)

**Report ID:** RPT-D160-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 28 Nov 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 160 of 180)

## Transaction summary
The rail processed 1117.9M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 212.6M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1117.9  (▲116.9 d/d, ▲212.6 w/w, ▲373.0 m/m)
- **Success Rate:** 99.98%  (▲0.7 d/d, ▲0.68 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.25%  (▲0.01 d/d, ▼0.2 m/m)
- **Business Declines:** 0.13%  (▼0.01 d/d, ▼0.04 w/w, ▼0.07 m/m)
- **Customer Complaints:** 923  (▼3 d/d, ▼143 w/w, ▼1019 m/m)
- **Merchant Complaints:** 92  (▼1 d/d, ▼4 w/w, ▼119 m/m)
- **Fraud Alerts:** 711  (▼1 d/d, ▼87 w/w, ▼340 m/m)
- **Risk Score:** 19  (▼6 w/w, ▼12 m/m)
- **Response Time:** 544 ms  (▲1 d/d, ▼14 w/w, ▼198 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 359.4 | 99.5% |
| HDFC Bank | 123.3 | 99.55% |
| Bank of Baroda | 88.7 | 99.64% |
| Union Bank of India | 77.0 | 99.43% |
| ICICI Bank | 68.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 533.3 | 99.14% | 231 ms |
| Google Pay | 365.1 | 99.17% | 316 ms |
| Paytm | 90.2 | 99.06% | 192 ms |
| Navi | 41.2 | 99.17% | 225 ms |
| SuperMoney | 21.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 419.2 |
| Person to Person | 396.9 |
| QR Payments | 106.2 |
| UPI Lite | 53.7 |
| UPI Autopay | 36.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D160-MON) and any meetings/emails on 28 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D160-MON, RPT-D159-DAILY
