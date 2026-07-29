---
id: STORYLINE
type: product_document
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-29T20:00:00
---

# Operational Month — Transaction-Driven Timeline

This corpus is one continuous month of NPCI UPI Products operations.
There are no scripted weekly themes and no product launches — every artifact is
routine operations or the natural consequence of transaction behaviour.

Volume follows a growth trend modulated by weekday, month-end and high-volume
campaign days. Bank/PSP/feature health degradations surface as incidents, each
running its lifecycle (detect -> bridge -> investigate -> RCA -> decision -> SOP
-> recovery -> validation) and referenced again in weekly and monthly reviews.

## Incident timeline
- **Day 5 (Fri 09 Jan)** — INC-2026-01: bank timeout / 5xx spike on Punjab National Bank (Sev-2, 4 days). RCA RCA-2026-01, decision DEC-2026-01.
- **Day 18 (Thu 22 Jan)** — INC-2026-24: feature-level degradation on UPI Lite (Sev-3, 3 days). RCA RCA-2026-24, decision DEC-2026-24.
- **Day 22 (Mon 26 Jan)** — INC-2026-15: fraud / risk spike on FamApp (Sev-2, 3 days). RCA RCA-2026-15, decision DEC-2026-15.
- **Day 31 (Wed 04 Feb)** — INC-2026-02: fraud / risk spike on HDFC MobileBanking (Sev-2, 5 days). RCA RCA-2026-02, decision DEC-2026-02.
- **Day 34 (Sat 07 Feb)** — INC-2026-08: fraud / risk spike on WhatsApp Pay (Sev-3, 5 days). RCA RCA-2026-08, decision DEC-2026-08.
- **Day 50 (Mon 23 Feb)** — INC-2026-19: fraud / risk spike on Google Pay (Sev-2, 3 days). RCA RCA-2026-19, decision DEC-2026-19.
- **Day 52 (Wed 25 Feb)** — INC-2026-22: PSP callback latency increase on Navi (Sev-3, 4 days). RCA RCA-2026-22, decision DEC-2026-22.
- **Day 55 (Sat 28 Feb)** — INC-2026-16: fraud / risk spike on Navi (Sev-3, 2 days). Short operational issue.
- **Day 59 (Wed 04 Mar)** — INC-2026-03: fraud / risk spike on Navi (Sev-2, 3 days). RCA RCA-2026-03, decision DEC-2026-03.
- **Day 61 (Fri 06 Mar)** — INC-2026-09: merchant settlement delay on Bank of Baroda (Sev-3, 2 days). Short operational issue.
- **Day 76 (Sat 21 Mar)** — INC-2026-17: PSP callback latency increase on YONO SBI (Sev-3, 3 days). RCA RCA-2026-17, decision DEC-2026-17.
- **Day 78 (Mon 23 Mar)** — INC-2026-12: PSP callback latency increase on BHIM (Sev-3, 2 days). Short operational issue.
- **Day 80 (Wed 25 Mar)** — INC-2026-21: feature-level degradation on RuPay Credit on UPI (Sev-3, 4 days). RCA RCA-2026-21, decision DEC-2026-21.
- **Day 92 (Mon 06 Apr)** — INC-2026-04: bank timeout / 5xx spike on State Bank of India (Sev-2, 4 days). RCA RCA-2026-04, decision DEC-2026-04.
- **Day 101 (Wed 15 Apr)** — INC-2026-20: merchant settlement delay on Kotak Mahindra Bank (Sev-3, 3 days). RCA RCA-2026-20, decision DEC-2026-20.
- **Day 109 (Thu 23 Apr)** — INC-2026-23: merchant decline-rate spike on PowerPay Utilities, MetroRide (Sev-3, 4 days). RCA RCA-2026-23, decision DEC-2026-23.
- **Day 114 (Tue 28 Apr)** — INC-2026-11: bank timeout / 5xx spike on Bank of Baroda (Sev-3, 2 days). Short operational issue.
- **Day 117 (Fri 01 May)** — INC-2026-05: merchant settlement delay on Union Bank of India (Sev-2, 3 days). RCA RCA-2026-05, decision DEC-2026-05.
- **Day 124 (Fri 08 May)** — INC-2026-26: merchant settlement delay on AU Small Finance Bank (Sev-3, 4 days). RCA RCA-2026-26, decision DEC-2026-26.
- **Day 128 (Tue 12 May)** — INC-2026-13: merchant decline-rate spike on TravelGo, InsureWell (Sev-3, 5 days). RCA RCA-2026-13, decision DEC-2026-13.
- **Day 138 (Fri 22 May)** — INC-2026-25: merchant settlement delay on ICICI Bank (Sev-3, 2 days). Short operational issue.
- **Day 140 (Sun 24 May)** — INC-2026-18: fraud / risk spike on BHIM (Sev-2, 4 days). RCA RCA-2026-18, decision DEC-2026-18.
- **Day 144 (Thu 28 May)** — INC-2026-14: PSP callback latency increase on BHIM (Sev-3, 5 days). RCA RCA-2026-14, decision DEC-2026-14.
- **Day 147 (Sun 31 May)** — INC-2026-07: merchant decline-rate spike on MetroRide, QuickBite (Sev-3, 2 days). Short operational issue.
- **Day 151 (Thu 04 Jun)** — INC-2026-06: bank timeout / 5xx spike on Punjab National Bank (Sev-2, 3 days). RCA RCA-2026-06, decision DEC-2026-06.
- **Day 184 (Tue 07 Jul)** — INC-2026-10: feature-level degradation on UPI 123Pay (Sev-3, 5 days). RCA RCA-2026-10, decision DEC-2026-10.

The numeric spine is upi_kpis_month.xlsx; the monthly close is RPT-MONTHLY-EXEC. Every day also
has a daily operations report (RPT-Dxx-DAILY) and a monitoring note.

Refs: upi_kpis_month.xlsx, RPT-MONTHLY-EXEC, ORG-OVERVIEW, INC-2026-01, INC-2026-24
