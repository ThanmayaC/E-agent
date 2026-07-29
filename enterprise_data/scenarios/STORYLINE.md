---
id: STORYLINE
type: product_document
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-18T20:00:00
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
- **Day 3 (Wed 24 Jun)** — INC-2026-01: bank timeout / 5xx spike on Union Bank of India (Sev-2, 4 days). RCA RCA-2026-01, decision DEC-2026-01.
- **Day 9 (Tue 30 Jun)** — INC-2026-13: PSP callback latency increase on YONO SBI (Sev-3, 4 days). RCA RCA-2026-13, decision DEC-2026-13.
- **Day 11 (Thu 02 Jul)** — INC-2026-16: PSP callback latency increase on Paytm (Sev-3, 4 days). RCA RCA-2026-16, decision DEC-2026-16.
- **Day 15 (Mon 06 Jul)** — INC-2026-09: fraud / risk spike on YONO SBI (Sev-2, 3 days). RCA RCA-2026-09, decision DEC-2026-09.
- **Day 28 (Sun 19 Jul)** — INC-2026-11: PSP callback latency increase on CRED (Sev-3, 2 days). Short operational issue.
- **Day 34 (Sat 25 Jul)** — INC-2026-27: PSP callback latency increase on Amazon Pay (Sev-3, 5 days). RCA RCA-2026-27, decision DEC-2026-27.
- **Day 36 (Mon 27 Jul)** — INC-2026-02: merchant settlement delay on Axis Bank (Sev-2, 3 days). RCA RCA-2026-02, decision DEC-2026-02.
- **Day 43 (Mon 03 Aug)** — INC-2026-07: merchant settlement delay on Yes Bank (Sev-3, 2 days). Short operational issue.
- **Day 57 (Mon 17 Aug)** — INC-2026-03: merchant settlement delay on ICICI Bank (Sev-2, 4 days). RCA RCA-2026-03, decision DEC-2026-03.
- **Day 61 (Fri 21 Aug)** — INC-2026-28: feature-level degradation on Collect Requests (Sev-3, 3 days). RCA RCA-2026-28, decision DEC-2026-28.
- **Day 65 (Tue 25 Aug)** — INC-2026-18: merchant decline-rate spike on MetroRide, QuickBite (Sev-3, 2 days). Short operational issue.
- **Day 70 (Sun 30 Aug)** — INC-2026-23: PSP callback latency increase on BHIM (Sev-3, 2 days). Short operational issue.
- **Day 85 (Mon 14 Sep)** — INC-2026-14: PSP callback latency increase on Axis Mobile (Sev-3, 5 days). RCA RCA-2026-14, decision DEC-2026-14.
- **Day 95 (Thu 24 Sep)** — INC-2026-04: fraud / risk spike on iMobile Pay (Sev-2, 5 days). RCA RCA-2026-04, decision DEC-2026-04.
- **Day 100 (Tue 29 Sep)** — INC-2026-12: merchant settlement delay on State Bank of India (Sev-3, 5 days). RCA RCA-2026-12, decision DEC-2026-12.
- **Day 113 (Mon 12 Oct)** — INC-2026-19: fraud / risk spike on WhatsApp Pay (Sev-3, 5 days). RCA RCA-2026-19, decision DEC-2026-19.
- **Day 117 (Fri 16 Oct)** — INC-2026-08: PSP callback latency increase on CRED (Sev-3, 4 days). RCA RCA-2026-08, decision DEC-2026-08.
- **Day 126 (Sun 25 Oct)** — INC-2026-05: bank timeout / 5xx spike on Union Bank of India (Sev-2, 5 days). RCA RCA-2026-05, decision DEC-2026-05.
- **Day 129 (Wed 28 Oct)** — INC-2026-24: merchant decline-rate spike on TravelGo, InsureWell (Sev-3, 5 days). RCA RCA-2026-24, decision DEC-2026-24.
- **Day 131 (Fri 30 Oct)** — INC-2026-10: bank timeout / 5xx spike on Union Bank of India (Sev-3, 2 days). Short operational issue.
- **Day 135 (Tue 03 Nov)** — INC-2026-20: merchant settlement delay on Bank of Baroda (Sev-3, 2 days). Short operational issue.
- **Day 139 (Sat 07 Nov)** — INC-2026-25: PSP callback latency increase on BHIM (Sev-3, 5 days). RCA RCA-2026-25, decision DEC-2026-25.
- **Day 145 (Fri 13 Nov)** — INC-2026-17: merchant settlement delay on IndusInd Bank (Sev-3, 4 days). RCA RCA-2026-17, decision DEC-2026-17.
- **Day 147 (Sun 15 Nov)** — INC-2026-26: fraud / risk spike on FamApp (Sev-2, 3 days). RCA RCA-2026-26, decision DEC-2026-26.
- **Day 151 (Thu 19 Nov)** — INC-2026-06: fraud / risk spike on HDFC MobileBanking (Sev-2, 5 days). RCA RCA-2026-06, decision DEC-2026-06.
- **Day 161 (Sun 29 Nov)** — INC-2026-22: bank timeout / 5xx spike on Bank of Baroda (Sev-3, 2 days). Short operational issue.
- **Day 166 (Fri 04 Dec)** — INC-2026-21: feature-level degradation on QR Payments (Sev-3, 5 days). RCA RCA-2026-21, decision DEC-2026-21.
- **Day 171 (Wed 09 Dec)** — INC-2026-15: merchant settlement delay on Bank of Baroda (Sev-3, 4 days). RCA RCA-2026-15, decision DEC-2026-15.

The numeric spine is upi_kpis_month.xlsx; the monthly close is RPT-MONTHLY-EXEC. Every day also
has a daily operations report (RPT-Dxx-DAILY) and a monitoring note.

Refs: upi_kpis_month.xlsx, RPT-MONTHLY-EXEC, ORG-OVERVIEW, INC-2026-01, INC-2026-13
