---
id: RPT-D105-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-04T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 04 Oct 2026)

**Report ID:** RPT-D105-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 04 Oct 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 105 of 180)

## Transaction summary
The rail processed 747.8M UPI transactions on Sunday — a quiet Sunday — up 19.6M on the same day last week. Success held at 99.44% and settlement at 99.21%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 747.8  (▼73.7 d/d, ▲19.6 w/w, ▲2.9 m/m)
- **Success Rate:** 99.44%  (▼0.4 d/d, ▼0.4 w/w, ▼0.16 m/m)
- **Settlement Success:** 99.21%  (▲0.27 d/d, ▲0.33 w/w, ▼0.22 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,191  (▼23 d/d, ▼118 w/w, ▼751 m/m)
- **Merchant Complaints:** 123  (▼8 d/d, ▼3 w/w, ▼88 m/m)
- **Fraud Alerts:** 814  (▲4 d/d, ▼61 w/w, ▼237 m/m)
- **Risk Score:** 22  (▼4 w/w, ▼9 m/m)
- **Response Time:** 602 ms  (▼11 d/d, ▼11 w/w, ▼140 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 240.4 | 99.5% |
| HDFC Bank | 82.5 | 99.55% |
| Bank of Baroda | 59.3 | 99.64% |
| Union Bank of India | 51.5 | 99.43% |
| ICICI Bank | 46.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 356.8 | 99.14% | 231 ms |
| Google Pay | 244.3 | 99.17% | 316 ms |
| Paytm | 60.3 | 99.06% | 192 ms |
| Navi | 27.6 | 99.17% | 225 ms |
| SuperMoney | 14.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 280.4 |
| Person to Person | 265.5 |
| QR Payments | 71.0 |
| UPI Lite | 35.9 |
| UPI Autopay | 24.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D105-MON) and any meetings/emails on 04 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D105-MON, RPT-D104-DAILY
