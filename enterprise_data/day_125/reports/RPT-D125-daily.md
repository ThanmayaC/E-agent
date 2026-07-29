---
id: RPT-D125-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-24T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 24 Oct 2026)

**Report ID:** RPT-D125-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 24 Oct 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 125 of 180)

## Transaction summary
The rail processed 871.1M UPI transactions on Saturday — a lighter Saturday — up 20.7M on the same day last week. Success held at 99.78% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 871.1  (▼81.5 d/d, ▲20.7 w/w, ▲126.2 m/m)
- **Success Rate:** 99.78%  (▼0.2 d/d, ▼0.2 w/w, ▲0.18 m/m)
- **Settlement Success:** 99.98%  (▲0.47 d/d, ▲0.99 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.28%  (▼0.07 w/w, ▼0.17 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,093  (▲6 d/d, ▼224 w/w, ▼849 m/m)
- **Merchant Complaints:** 111  (▲1 d/d, ▼4 w/w, ▼100 m/m)
- **Fraud Alerts:** 768  (▼2 d/d, ▼11 w/w, ▼283 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 588 ms  (▲3 d/d, ▼49 w/w, ▼154 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 280.1 | 99.5% |
| HDFC Bank | 96.1 | 99.55% |
| Bank of Baroda | 69.1 | 99.64% |
| Union Bank of India | 60.0 | 99.43% |
| ICICI Bank | 53.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 415.6 | 99.14% | 231 ms |
| Google Pay | 284.5 | 99.17% | 316 ms |
| Paytm | 70.3 | 99.06% | 192 ms |
| Navi | 32.1 | 99.17% | 225 ms |
| SuperMoney | 17.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 326.7 |
| Person to Person | 309.2 |
| QR Payments | 82.8 |
| UPI Lite | 41.8 |
| UPI Autopay | 28.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D125-MON) and any meetings/emails on 24 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D125-MON, RPT-D124-DAILY
