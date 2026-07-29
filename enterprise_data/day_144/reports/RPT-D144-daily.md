---
id: RPT-D144-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-12T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 12 Nov 2026)

**Report ID:** RPT-D144-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 12 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 144 of 180)

## Transaction summary
The rail processed 989.3M UPI transactions on Thursday — a steady mid-week day — up 2.4M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 989.3  (▼11.6 d/d, ▲2.4 w/w, ▲244.4 m/m)
- **Success Rate:** 99.98%  (▲0.24 d/d, ▲0.93 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.35 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.26%  (▼0.01 d/d, ▼0.01 w/w, ▼0.19 m/m)
- **Business Declines:** 0.14%  (▼0.06 m/m)
- **Customer Complaints:** 1,001  (▼6 d/d, ▼20 w/w, ▼941 m/m)
- **Merchant Complaints:** 100  (▼1 d/d, ▼4 w/w, ▼111 m/m)
- **Fraud Alerts:** 738  (▲6 d/d, ▼7 w/w, ▼313 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 566 ms  (▼8 d/d, ▼7 w/w, ▼176 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 318.1 | 99.5% |
| HDFC Bank | 109.1 | 99.55% |
| Bank of Baroda | 78.5 | 99.64% |
| Union Bank of India | 68.2 | 99.43% |
| ICICI Bank | 61.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 472.0 | 99.14% | 231 ms |
| Google Pay | 323.1 | 99.17% | 316 ms |
| Paytm | 79.8 | 99.06% | 192 ms |
| Navi | 36.5 | 99.17% | 225 ms |
| SuperMoney | 19.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 371.0 |
| Person to Person | 351.2 |
| QR Payments | 94.0 |
| UPI Lite | 47.5 |
| UPI Autopay | 32.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D144-MON) and any meetings/emails on 12 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D144-MON, RPT-D143-DAILY
