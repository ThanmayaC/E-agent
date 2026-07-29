---
id: RPT-D56-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-16T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 16 Aug 2026)

**Report ID:** RPT-D56-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 16 Aug 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 56 of 180)

## Transaction summary
The rail processed 682.1M UPI transactions on Sunday — a quiet Sunday — up 18.0M on the same day last week. Success held at 99.25% and settlement at 98.91%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 682.1  (▼63.5 d/d, ▲18.0 w/w, ▼62.8 m/m)
- **Success Rate:** 99.25%  (▼0.44 d/d, ▼0.73 w/w, ▼0.35 m/m)
- **Settlement Success:** 98.91%  (▼1.07 d/d, ▼0.76 w/w, ▼0.52 m/m)
- **Technical Declines:** 0.36%  (▼0.01 d/d, ▼0.02 w/w, ▼0.09 m/m)
- **Business Declines:** 0.17%  (▼0.01 d/d, ▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,513  (▼44 w/w, ▼429 m/m)
- **Merchant Complaints:** 158  (▼1 d/d, ▼5 w/w, ▼53 m/m)
- **Fraud Alerts:** 906  (▼11 d/d, ▼23 w/w, ▼145 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼5 m/m)
- **Response Time:** 660 ms  (▼7 d/d, ▼8 w/w, ▼82 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 219.3 | 99.5% |
| HDFC Bank | 75.3 | 99.55% |
| Bank of Baroda | 54.1 | 99.64% |
| Union Bank of India | 47.0 | 99.43% |
| ICICI Bank | 42.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 325.4 | 99.14% | 231 ms |
| Google Pay | 222.8 | 99.17% | 316 ms |
| Paytm | 55.0 | 99.06% | 192 ms |
| Navi | 25.1 | 99.17% | 225 ms |
| SuperMoney | 13.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 255.8 |
| Person to Person | 242.1 |
| QR Payments | 64.8 |
| UPI Lite | 32.7 |
| UPI Autopay | 22.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.36% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D56-MON) and any meetings/emails on 16 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D56-MON, RPT-D55-DAILY
