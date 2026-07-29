---
id: RPT-D76-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-05T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 05 Sep 2026)

**Report ID:** RPT-D76-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 05 Sep 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 76 of 180)

## Transaction summary
The rail processed 767.7M UPI transactions on Saturday — a lighter Saturday — down 184.4M on the same day last week. Success held at 99.95% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 767.7  (▼99.6 d/d, ▼184.4 w/w, ▲22.8 m/m)
- **Success Rate:** 99.95%  (▲0.6 d/d, ▲0.45 w/w, ▲0.35 m/m)
- **Settlement Success:** 99.98%  (▲0.59 d/d, ▲0.88 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,376  (▼7 d/d, ▼35 w/w, ▼566 m/m)
- **Merchant Complaints:** 143  (▼1 d/d, ▼5 w/w, ▼68 m/m)
- **Fraud Alerts:** 873  (▲5 d/d, ▼6 w/w, ▼178 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼7 m/m)
- **Response Time:** 636 ms  (▼4 d/d, ▼9 w/w, ▼106 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 246.8 | 99.5% |
| HDFC Bank | 84.7 | 99.55% |
| Bank of Baroda | 60.9 | 99.64% |
| Union Bank of India | 52.9 | 99.43% |
| ICICI Bank | 47.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 366.3 | 99.14% | 231 ms |
| Google Pay | 250.8 | 99.17% | 316 ms |
| Paytm | 61.9 | 99.06% | 192 ms |
| Navi | 28.3 | 99.17% | 225 ms |
| SuperMoney | 15.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 287.9 |
| Person to Person | 272.5 |
| QR Payments | 72.9 |
| UPI Lite | 36.8 |
| UPI Autopay | 25.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D76-MON) and any meetings/emails on 05 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D76-MON, RPT-D75-DAILY
