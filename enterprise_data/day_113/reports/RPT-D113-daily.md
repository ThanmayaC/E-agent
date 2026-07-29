---
id: RPT-D113-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-12T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 12 Oct 2026)

**Report ID:** RPT-D113-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 12 Oct 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 113 of 180)

## Transaction summary
The rail processed 894.7M UPI transactions on Monday — the Monday ramp-up after the weekend — down 222.3M on the same day last week. Success landed at 99.91% and settlement at 99.96%, held back by live issues on WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 894.7  (▲144.2 d/d, ▼222.3 w/w, ▲149.8 m/m)
- **Success Rate:** 99.91%  (▼0.07 d/d, ▲0.7 w/w, ▲0.31 m/m)
- **Settlement Success:** 99.96%  (▼0.02 d/d, ▼0.02 w/w, ▲0.53 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.22%  (▲0.07 d/d, ▲0.07 w/w, ▲0.02 m/m)
- **Customer Complaints:** 1,397  (▲251 d/d, ▲219 w/w, ▼545 m/m)
- **Merchant Complaints:** 118  (▼3 w/w, ▼93 m/m)
- **Fraud Alerts:** 955  (▲165 d/d, ▲145 w/w, ▼96 m/m)
- **Risk Score:** 33  (▲11 d/d, ▲11 w/w, ▲2 m/m)
- **Response Time:** 594 ms  (▼6 d/d, ▼11 w/w, ▼148 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 287.7 | 99.5% |
| HDFC Bank | 98.7 | 99.55% |
| Bank of Baroda | 71.0 | 99.64% |
| Union Bank of India | 61.6 | 99.43% |
| ICICI Bank | 55.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 426.8 | 99.14% | 231 ms |
| Google Pay | 292.2 | 99.17% | 316 ms |
| Paytm | 72.2 | 99.06% | 192 ms |
| Navi | 33.0 | 99.17% | 225 ms |
| SuperMoney | 17.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 335.5 |
| Person to Person | 317.6 |
| QR Payments | 85.0 |
| UPI Lite | 42.9 |
| UPI Autopay | 29.5 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on WhatsApp Pay (day 1 of 5); see RCA-2026-19.

## Recommendations
Stay on the open incident: keep recovery monitoring on WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D113-MON) and any meetings/emails on 12 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D113-MON, RPT-D112-DAILY, INC-2026-19, RCA-2026-19
