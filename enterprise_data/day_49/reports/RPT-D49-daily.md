---
id: RPT-D49-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-09T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 09 Aug 2026)

**Report ID:** RPT-D49-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 09 Aug 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 49 of 180)

## Transaction summary
The rail processed 664.1M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — down 7.9M on the same day last week. Success held at 99.98% and settlement at 99.67%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 664.1  (▼90.5 d/d, ▼7.9 w/w, ▼80.8 m/m)
- **Success Rate:** 99.98%  (▲0.28 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.67%  (▼0.24 d/d, ▼0.31 w/w, ▲0.24 m/m)
- **Technical Declines:** 0.38%  (▲0.01 d/d, ▼0.07 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,557  (▼5 d/d, ▼36 w/w, ▼385 m/m)
- **Merchant Complaints:** 163  (▼2 d/d, ▼8 w/w, ▼48 m/m)
- **Fraud Alerts:** 929  (▼28 w/w, ▼122 m/m)
- **Risk Score:** 27  (▼4 m/m)
- **Response Time:** 668 ms  (▼10 d/d, ▼11 w/w, ▼74 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 213.5 | 99.5% |
| HDFC Bank | 73.3 | 99.55% |
| Bank of Baroda | 52.7 | 99.64% |
| Union Bank of India | 45.7 | 99.43% |
| ICICI Bank | 40.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 316.8 | 99.14% | 231 ms |
| Google Pay | 216.9 | 99.17% | 316 ms |
| Paytm | 53.6 | 99.06% | 192 ms |
| Navi | 24.5 | 99.17% | 225 ms |
| SuperMoney | 12.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 249.0 |
| Person to Person | 235.8 |
| QR Payments | 63.1 |
| UPI Lite | 31.9 |
| UPI Autopay | 21.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D49-MON) and any meetings/emails on 09 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D49-MON, RPT-D48-DAILY
