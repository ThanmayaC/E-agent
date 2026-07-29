---
id: RPT-D121-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-20T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 20 Oct 2026)

**Report ID:** RPT-D121-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 20 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 121 of 180)

## Transaction summary
The rail processed 932.0M UPI transactions on Tuesday — a steady mid-week day — down 22.8M on the same day last week. Success held at 99.76% and settlement at 99.61%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 932.0  (▲5.1 d/d, ▼22.8 w/w, ▲187.1 m/m)
- **Success Rate:** 99.76%  (▲0.47 d/d, ▲1.03 w/w, ▲0.16 m/m)
- **Settlement Success:** 99.61%  (▼0.37 d/d, ▼0.37 w/w, ▲0.18 m/m)
- **Technical Declines:** 0.29%  (▼0.01 d/d, ▼0.16 m/m)
- **Business Declines:** 0.15%  (▼0.04 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,105  (▼49 d/d, ▼192 w/w, ▼837 m/m)
- **Merchant Complaints:** 113  (▼1 d/d, ▼5 w/w, ▼98 m/m)
- **Fraud Alerts:** 775  (▼2 d/d, ▼125 w/w, ▼276 m/m)
- **Risk Score:** 21  (▼8 w/w, ▼10 m/m)
- **Response Time:** 593 ms  (▼10 d/d, ▼2 w/w, ▼149 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 299.7 | 99.5% |
| HDFC Bank | 102.8 | 99.55% |
| Bank of Baroda | 73.9 | 99.64% |
| Union Bank of India | 64.2 | 99.43% |
| ICICI Bank | 57.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 444.6 | 99.14% | 231 ms |
| Google Pay | 304.4 | 99.17% | 316 ms |
| Paytm | 75.2 | 99.06% | 192 ms |
| Navi | 34.3 | 99.17% | 225 ms |
| SuperMoney | 18.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 349.5 |
| Person to Person | 330.9 |
| QR Payments | 88.5 |
| UPI Lite | 44.7 |
| UPI Autopay | 30.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D121-MON) and any meetings/emails on 20 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D121-MON, RPT-D120-DAILY
