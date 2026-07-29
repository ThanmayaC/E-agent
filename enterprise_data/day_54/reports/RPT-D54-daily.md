---
id: RPT-D54-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-14T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 14 Aug 2026)

**Report ID:** RPT-D54-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 14 Aug 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 54 of 180)

## Transaction summary
The rail processed 995.9M UPI transactions on Friday — a campaign-driven high-volume day — up 189.0M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 995.9  (▲164.4 d/d, ▲189.0 w/w, ▲251.0 m/m)
- **Success Rate:** 99.98%  (▲0.64 d/d, ▲1.3 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.97 d/d, ▲0.08 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.36%  (▼0.01 d/d, ▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.17%  (▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,525  (▲6 d/d, ▼53 w/w, ▼417 m/m)
- **Merchant Complaints:** 160  (▼6 w/w, ▼51 m/m)
- **Fraud Alerts:** 929  (▲14 d/d, ▼10 w/w, ▼122 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼5 m/m)
- **Response Time:** 666 ms  (▼6 d/d, ▼8 w/w, ▼76 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 320.2 | 99.5% |
| HDFC Bank | 109.9 | 99.55% |
| Bank of Baroda | 79.0 | 99.64% |
| Union Bank of India | 68.6 | 99.43% |
| ICICI Bank | 61.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 475.1 | 99.14% | 231 ms |
| Google Pay | 325.3 | 99.17% | 316 ms |
| Paytm | 80.3 | 99.06% | 192 ms |
| Navi | 36.7 | 99.17% | 225 ms |
| SuperMoney | 19.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 373.5 |
| Person to Person | 353.5 |
| QR Payments | 94.6 |
| UPI Lite | 47.8 |
| UPI Autopay | 32.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.36% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D54-MON) and any meetings/emails on 14 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D54-MON, RPT-D53-DAILY
