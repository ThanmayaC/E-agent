---
id: RPT-D21-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-12T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 12 Jul 2026)

**Report ID:** RPT-D21-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 12 Jul 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 21 of 180)

## Transaction summary
The rail processed 634.9M UPI transactions on Sunday — a quiet Sunday — up 14.2M on the same day last week. Success held at 98.94% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 634.9  (▼70.9 d/d, ▲14.2 w/w, ▼110.0 m/m)
- **Success Rate:** 98.94%  (▲0.31 w/w, ▼0.66 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.41%  (▼0.01 d/d, ▼0.04 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,791  (▲20 d/d, ▼121 w/w, ▼151 m/m)
- **Merchant Complaints:** 189  (▼9 w/w, ▼22 m/m)
- **Fraud Alerts:** 991  (▼1 d/d, ▼27 w/w, ▼60 m/m)
- **Risk Score:** 29  (▼1 w/w, ▼2 m/m)
- **Response Time:** 714 ms  (▲1 d/d, ▼20 w/w, ▼28 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 204.1 | 99.5% |
| HDFC Bank | 70.0 | 99.55% |
| Bank of Baroda | 50.4 | 99.64% |
| Union Bank of India | 43.7 | 99.43% |
| ICICI Bank | 39.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 302.9 | 99.14% | 231 ms |
| Google Pay | 207.4 | 99.17% | 316 ms |
| Paytm | 51.2 | 99.06% | 192 ms |
| Navi | 23.4 | 99.17% | 225 ms |
| SuperMoney | 12.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 238.1 |
| Person to Person | 225.4 |
| QR Payments | 60.3 |
| UPI Lite | 30.5 |
| UPI Autopay | 21.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D21-MON) and any meetings/emails on 12 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D21-MON, RPT-D20-DAILY
