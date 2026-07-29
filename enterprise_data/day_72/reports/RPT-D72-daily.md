---
id: RPT-D72-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-01T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 01 Sep 2026)

**Report ID:** RPT-D72-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 01 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 72 of 180)

## Transaction summary
The rail processed 861.8M UPI transactions on Tuesday — a steady mid-week day — up 5.8M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 861.8  (▼95.0 d/d, ▲5.8 w/w, ▲116.9 m/m)
- **Success Rate:** 99.98%  (▲1.03 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.62 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.35%  (▼0.07 d/d, ▼0.01 w/w, ▼0.1 m/m)
- **Business Declines:** 0.17%  (▼0.07 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,397  (▼236 d/d, ▼40 w/w, ▼545 m/m)
- **Merchant Complaints:** 146  (▲1 d/d, ▼96 w/w, ▼65 m/m)
- **Fraud Alerts:** 887  (▲4 d/d, ▼11 w/w, ▼164 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼6 m/m)
- **Response Time:** 649 ms  (▼49 d/d, ▼3 w/w, ▼93 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 277.1 | 99.5% |
| HDFC Bank | 95.1 | 99.55% |
| Bank of Baroda | 68.3 | 99.64% |
| Union Bank of India | 59.4 | 99.43% |
| ICICI Bank | 53.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 411.1 | 99.14% | 231 ms |
| Google Pay | 281.5 | 99.17% | 316 ms |
| Paytm | 69.5 | 99.06% | 192 ms |
| Navi | 31.8 | 99.17% | 225 ms |
| SuperMoney | 16.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 323.2 |
| Person to Person | 305.9 |
| QR Payments | 81.9 |
| UPI Lite | 41.4 |
| UPI Autopay | 28.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D72-MON) and any meetings/emails on 01 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D72-MON, RPT-D71-DAILY
