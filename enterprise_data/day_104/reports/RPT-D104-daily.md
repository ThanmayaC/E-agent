---
id: RPT-D104-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-03T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 03 Oct 2026)

**Report ID:** RPT-D104-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 03 Oct 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 104 of 180)

## Transaction summary
The rail processed 821.5M UPI transactions on Saturday — a lighter Saturday — up 4.5M on the same day last week. Success landed at 99.84% and settlement at 98.94%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 821.5  (▼309.2 d/d, ▲4.5 w/w, ▲76.6 m/m)
- **Success Rate:** 99.84%  (▼0.14 d/d, ▼0.14 w/w, ▲0.24 m/m)
- **Settlement Success:** 98.94%  (▼0.23 d/d, ▼0.01 w/w, ▼0.49 m/m)
- **Technical Declines:** 0.3%  (▼0.01 d/d, ▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.16%  (▼0.04 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,214  (▼13 d/d, ▼185 w/w, ▼728 m/m)
- **Merchant Complaints:** 131  (▼9 d/d, ▲3 w/w, ▼80 m/m)
- **Fraud Alerts:** 810  (▼4 d/d, ▼112 w/w, ▼241 m/m)
- **Risk Score:** 22  (▼7 w/w, ▼9 m/m)
- **Response Time:** 613 ms  (▲5 d/d, ▼129 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 264.1 | 99.45% |
| HDFC Bank | 90.6 | 99.55% |
| Bank of Baroda | 65.2 | 99.64% |
| Union Bank of India | 56.6 | 99.43% |
| ICICI Bank | 50.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 391.9 | 99.14% | 231 ms |
| Google Pay | 268.3 | 99.17% | 316 ms |
| Paytm | 66.3 | 99.06% | 192 ms |
| Navi | 30.3 | 99.17% | 225 ms |
| SuperMoney | 16.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 308.1 |
| Person to Person | 291.6 |
| QR Payments | 78.0 |
| UPI Lite | 39.4 |
| UPI Autopay | 27.1 |

## Failure analysis
- INC-2026-12 — merchant settlement delay on State Bank of India (day 5 of 5); see RCA-2026-12.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D104-MON) and any meetings/emails on 03 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D104-MON, RPT-D103-DAILY, INC-2026-12, RCA-2026-12
