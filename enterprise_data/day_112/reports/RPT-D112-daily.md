---
id: RPT-D112-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-11T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 11 Oct 2026)

**Report ID:** RPT-D112-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 11 Oct 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 112 of 180)

## Transaction summary
The rail processed 750.5M UPI transactions on Sunday — a quiet Sunday — up 2.7M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 750.5  (▼98.2 d/d, ▲2.7 w/w, ▲5.6 m/m)
- **Success Rate:** 99.98%  (▲0.77 d/d, ▲0.54 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.68 d/d, ▲0.77 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.29%  (▼0.01 d/d, ▼0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,146  (▼9 d/d, ▼45 w/w, ▼796 m/m)
- **Merchant Complaints:** 118  (▼1 d/d, ▼5 w/w, ▼93 m/m)
- **Fraud Alerts:** 790  (▼5 d/d, ▼24 w/w, ▼261 m/m)
- **Risk Score:** 22  (▼9 m/m)
- **Response Time:** 600 ms  (▼2 w/w, ▼142 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 241.3 | 99.5% |
| HDFC Bank | 82.8 | 99.55% |
| Bank of Baroda | 59.5 | 99.64% |
| Union Bank of India | 51.7 | 99.43% |
| ICICI Bank | 46.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 358.0 | 99.14% | 231 ms |
| Google Pay | 245.1 | 99.17% | 316 ms |
| Paytm | 60.5 | 99.06% | 192 ms |
| Navi | 27.7 | 99.17% | 225 ms |
| SuperMoney | 14.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 281.4 |
| Person to Person | 266.4 |
| QR Payments | 71.3 |
| UPI Lite | 36.0 |
| UPI Autopay | 24.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D112-MON) and any meetings/emails on 11 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D112-MON, RPT-D111-DAILY
