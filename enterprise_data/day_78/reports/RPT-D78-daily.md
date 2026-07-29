---
id: RPT-D78-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-07T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 07 Sep 2026)

**Report ID:** RPT-D78-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 07 Sep 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 78 of 180)

## Transaction summary
The rail processed 855.2M UPI transactions on Monday — the Monday ramp-up after the weekend — down 101.6M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 855.2  (▲146.8 d/d, ▼101.6 w/w, ▲110.3 m/m)
- **Success Rate:** 99.98%  (▲0.79 d/d, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.34%  (▲0.01 d/d, ▼0.08 w/w, ▼0.11 m/m)
- **Business Declines:** 0.16%  (▼0.01 d/d, ▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,362  (▲4 d/d, ▼271 w/w, ▼580 m/m)
- **Merchant Complaints:** 140  (▼1 d/d, ▼5 w/w, ▼71 m/m)
- **Fraud Alerts:** 862  (▼8 d/d, ▼21 w/w, ▼189 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼7 m/m)
- **Response Time:** 638 ms  (▼60 w/w, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 275.0 | 99.5% |
| HDFC Bank | 94.3 | 99.55% |
| Bank of Baroda | 67.8 | 99.64% |
| Union Bank of India | 58.9 | 99.43% |
| ICICI Bank | 52.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 408.0 | 99.14% | 231 ms |
| Google Pay | 279.3 | 99.17% | 316 ms |
| Paytm | 69.0 | 99.06% | 192 ms |
| Navi | 31.5 | 99.17% | 225 ms |
| SuperMoney | 16.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 320.7 |
| Person to Person | 303.6 |
| QR Payments | 81.2 |
| UPI Lite | 41.0 |
| UPI Autopay | 28.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D78-MON) and any meetings/emails on 07 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D78-MON, RPT-D77-DAILY
