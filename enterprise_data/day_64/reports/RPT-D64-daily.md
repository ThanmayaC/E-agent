---
id: RPT-D64-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-24T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 24 Aug 2026)

**Report ID:** RPT-D64-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 24 Aug 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 64 of 180)

## Transaction summary
The rail processed 824.2M UPI transactions on Monday — the Monday ramp-up after the weekend — up 3.7M on the same day last week. Success held at 98.91% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 824.2  (▲130.2 d/d, ▲3.7 w/w, ▲79.3 m/m)
- **Success Rate:** 98.91%  (▼0.47 d/d, ▼0.66 w/w, ▼0.69 m/m)
- **Settlement Success:** 99.98%  (▲1.13 d/d, ▲2.04 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.35%  (▼0.06 d/d, ▼0.01 w/w, ▼0.1 m/m)
- **Business Declines:** 0.17%  (▼0.09 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,435  (▼182 d/d, ▼379 w/w, ▼507 m/m)
- **Merchant Complaints:** 150  (▼3 d/d, ▼213 w/w, ▼61 m/m)
- **Fraud Alerts:** 889  (▼19 d/d, ▼31 w/w, ▼162 m/m)
- **Risk Score:** 25  (▼1 d/d, ▼1 w/w, ▼6 m/m)
- **Response Time:** 655 ms  (▼18 d/d, ▼11 w/w, ▼87 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 265.0 | 99.5% |
| HDFC Bank | 90.9 | 99.55% |
| Bank of Baroda | 65.4 | 99.64% |
| Union Bank of India | 56.8 | 99.43% |
| ICICI Bank | 50.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 393.2 | 99.14% | 231 ms |
| Google Pay | 269.2 | 99.17% | 316 ms |
| Paytm | 66.5 | 99.06% | 192 ms |
| Navi | 30.4 | 99.17% | 225 ms |
| SuperMoney | 16.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 309.1 |
| Person to Person | 292.6 |
| QR Payments | 78.3 |
| UPI Lite | 39.6 |
| UPI Autopay | 27.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D64-MON) and any meetings/emails on 24 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D64-MON, RPT-D63-DAILY
