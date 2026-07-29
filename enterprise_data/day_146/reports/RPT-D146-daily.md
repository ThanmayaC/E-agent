---
id: RPT-D146-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-14T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 14 Nov 2026)

**Report ID:** RPT-D146-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 14 Nov 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 146 of 180)

## Transaction summary
The rail processed 874.8M UPI transactions on Saturday — a lighter Saturday — down 15.4M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on IndusInd Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 874.8  (▼135.3 d/d, ▼15.4 w/w, ▲129.9 m/m)
- **Success Rate:** 99.98%  (▲0.19 d/d, ▲0.33 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.2 d/d, ▲0.36 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.26%  (▼0.09 w/w, ▼0.19 m/m)
- **Business Declines:** 0.16%  (▼0.02 d/d, ▲0.02 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,058  (▼47 d/d, ▼222 w/w, ▼884 m/m)
- **Merchant Complaints:** 146  (▼32 d/d, ▲43 w/w, ▼65 m/m)
- **Fraud Alerts:** 728  (▼17 w/w, ▼323 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 560 ms  (▲2 d/d, ▼82 w/w, ▼182 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 281.3 | 99.5% |
| HDFC Bank | 96.5 | 99.55% |
| Bank of Baroda | 69.4 | 99.64% |
| Union Bank of India | 60.3 | 99.43% |
| ICICI Bank | 53.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 417.3 | 99.14% | 231 ms |
| Google Pay | 285.7 | 99.17% | 316 ms |
| Paytm | 70.6 | 99.06% | 192 ms |
| Navi | 32.2 | 99.17% | 225 ms |
| SuperMoney | 17.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 328.0 |
| Person to Person | 310.6 |
| QR Payments | 83.1 |
| UPI Lite | 42.0 |
| UPI Autopay | 28.9 |

## Failure analysis
- INC-2026-17 — merchant settlement delay on IndusInd Bank (day 2 of 4); see RCA-2026-17.

## Recommendations
Stay on the open incident: keep recovery monitoring on IndusInd Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D146-MON) and any meetings/emails on 14 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D146-MON, RPT-D145-DAILY, INC-2026-17, RCA-2026-17
