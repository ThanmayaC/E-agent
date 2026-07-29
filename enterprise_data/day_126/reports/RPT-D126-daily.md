---
id: RPT-D126-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-25T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 25 Oct 2026)

**Report ID:** RPT-D126-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 25 Oct 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 126 of 180)

## Transaction summary
The rail processed 781.4M UPI transactions on Sunday — a quiet Sunday — up 16.9M on the same day last week. Success landed at 98.22% and settlement at 99.08%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 781.4  (▼89.7 d/d, ▲16.9 w/w, ▲36.5 m/m)
- **Success Rate:** 98.22%  (▼1.56 d/d, ▼1.76 w/w, ▼1.38 m/m)
- **Settlement Success:** 99.08%  (▼0.9 d/d, ▼0.38 w/w, ▼0.35 m/m)
- **Technical Declines:** 0.58%  (▲0.3 d/d, ▲0.26 w/w, ▲0.13 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,831  (▲738 d/d, ▲621 w/w, ▼111 m/m)
- **Merchant Complaints:** 229  (▲118 d/d, ▲115 w/w, ▲18 m/m)
- **Fraud Alerts:** 774  (▲6 d/d, ▼8 w/w, ▼277 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 682 ms  (▲94 d/d, ▲69 w/w, ▼60 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 251.2 | 99.5% |
| HDFC Bank | 86.2 | 99.55% |
| Bank of Baroda | 62.0 | 99.64% |
| Union Bank of India | 53.8 | 97.23% |
| ICICI Bank | 48.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 372.8 | 99.14% | 231 ms |
| Google Pay | 255.2 | 99.17% | 316 ms |
| Paytm | 63.0 | 99.06% | 192 ms |
| Navi | 28.8 | 99.17% | 225 ms |
| SuperMoney | 15.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 293.0 |
| Person to Person | 277.4 |
| QR Payments | 74.2 |
| UPI Lite | 37.5 |
| UPI Autopay | 25.8 |

## Failure analysis
- INC-2026-05 — bank timeout / 5xx spike on Union Bank of India (day 1 of 5); see RCA-2026-05.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D126-MON) and any meetings/emails on 25 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D126-MON, RPT-D125-DAILY, INC-2026-05, RCA-2026-05
