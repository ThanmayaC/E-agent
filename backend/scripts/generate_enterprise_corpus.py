"""Generate a synthetic enterprise corpus for the Enterprise Brain demo (V2.3).

This is the organizational activity the Brain ingests: SOPs, RCAs, policies,
meeting notes, decision logs, action items, product docs, BRDs, roadmaps,
executive / weekly / monthly / merchant / risk reports, email threads, Teams
conversations, and Excel KPI workbooks — roughly six months (Jan–Jun 2026) of a
fintech payments company.

The point is not volume but *connectedness*: every document names other
entities the way real ones do. A single narrative spine — a March settlement
success-rate dip — runs through an RCA, the incident bridge meeting, a decision
log, a policy, an SOP, the KPI workbook, a weekly report, an email thread, and a
Teams channel. That is what lets the Brain answer a question by combining
sources ("Why did settlement success dip in March and what did we do about
it?") rather than returning a single file.

Everything is written as parser-supported files (.md, .xlsx) into a folder tree
whose sub-folders map onto the platform's document source kinds, so
``bootstrap_enterprise_demo.py`` can register them and the ordinary sync →
document-intelligence → Brain pipeline does the rest. Deterministic (seed=42).

    python scripts/generate_enterprise_corpus.py [OUTPUT_DIR]
"""
from __future__ import annotations

import random
import sys
from datetime import date
from pathlib import Path

import pandas as pd

random.seed(42)

OUT = (Path(sys.argv[1]) if len(sys.argv) > 1
       else Path(__file__).resolve().parents[1] / "sample_data" / "enterprise")

# --------------------------------------------------------------- the company
COMPANY = "SkyPay"

PEOPLE = {
    "Priya Nair": "VP Product",
    "Arjun Mehta": "Head of Payments",
    "Sara Khan": "Settlement Lead",
    "David Chen": "Engineering Manager, Payments",
    "Meera Iyer": "Risk & Fraud Lead",
    "Tom Fischer": "SRE Lead",
    "Ananya Rao": "Merchant Success Lead",
    "Rahul Verma": "Analytics Lead",
    "Lisa Wong": "Compliance Officer",
    "Karan Singh": "Product Manager, Checkout",
    "Nisha Patel": "Product Manager, Settlement",
    "James O'Brien": "CFO",
}
# f-string expressions cannot contain a backslash (Py 3.11), so the one name
# with an apostrophe is referenced through a constant key.
JAMES = "James O'Brien"

PRODUCTS = {
    "Payments": "Core transaction processing across UPI, Card, NetBanking, Wallet.",
    "Settlement": "Merchant payouts and bank reconciliation.",
    "Checkout": "Hosted checkout and payment pages.",
    "Merchant Onboarding": "KYC, activation, and merchant go-live.",
    "Fraud Shield": "Real-time risk scoring and fraud rules.",
    "Refunds": "Refund initiation, tracking, and reconciliation.",
}

PRODUCT_OWNER = {
    "Payments": "Arjun Mehta", "Settlement": "Nisha Patel",
    "Checkout": "Karan Singh", "Merchant Onboarding": "Ananya Rao",
    "Fraud Shield": "Meera Iyer", "Refunds": "Sara Khan",
}

KPIS = [
    "Settlement Success Rate", "Payment Success Rate", "Transaction Volume",
    "Gross Revenue", "Fraud Rate (bps)", "Refund Rate", "MAU",
    "Merchant Churn",
]

BANKS = ["HDFC", "ICICI", "SBI", "Axis", "Kotak"]
REGIONS = ["North", "South", "East", "West"]
MERCHANTS = ["ZapMart", "FreshKart", "UrbanEats", "NovaBazaar", "MetroMart",
             "BlueWave", "SunCart", "AlphaMart", "CityFoods", "PrimeGoods"]
MONTHS = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06"]
MONTH_NAME = {"2026-01": "January", "2026-02": "February", "2026-03": "March",
              "2026-04": "April", "2026-05": "May", "2026-06": "June"}

# Canonical cross-reference ids — the spine the whole corpus points at.
REF = {
    "sop_settlement": "SOP-SET-001 Settlement Reconciliation",
    "sop_incident": "SOP-OPS-002 Incident Response",
    "sop_release": "SOP-ENG-003 Release Management",
    "sop_onboarding": "SOP-MER-004 Merchant Onboarding",
    "sop_refund": "SOP-FIN-005 Refund Processing",
    "sop_fraud": "SOP-RSK-006 Fraud Review",
    "rca_settlement": "RCA-2026-03-014 Settlement Success Dip",
    "rca_checkout": "RCA-2026-02-009 Checkout Latency Spike",
    "rca_fraud": "RCA-2026-04-021 Fraud Rate Uptick",
    "rca_refund": "RCA-2026-05-030 Refund Backlog",
    "meeting_bridge": "Settlement Incident Bridge — 2026-03-12",
    "meeting_steering": "Product Steering Committee — 2026-03",
    "dec_monitoring": "DEC-2026-03-05 Settlement Monitoring & Auto-Retry",
    "dec_fraud_rule": "DEC-2026-04-08 Tighten Fraud Rule FS-17",
    "policy_retention": "POL-DATA-01 Data Retention Policy",
    "policy_refund": "POL-FIN-02 Refund Policy",
    "policy_risk": "POL-RSK-03 Merchant Risk Policy",
    "policy_incident": "POL-OPS-04 Incident Severity Policy",
    "policy_access": "POL-SEC-05 Access Control Policy",
    "roadmap_settlement": "Settlement Reliability (H1 2026 roadmap)",
    "brd_autoretry": "BRD-2026-11 Settlement Auto-Retry & Monitoring",
}


# ---------------------------------------------------------------- utilities
def w(folder: str, name: str, text: str) -> None:
    path = OUT / folder / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def owner(product: str) -> str:
    person = PRODUCT_OWNER[product]
    return f"{person} ({PEOPLE[person]})"


# ------------------------------------------------------------------- KPI data
# The KPI numbers every narrative references. Settlement success dips in March
# and recovers by May; fraud rate rises in April; refund rate rises in May.
KPI_SERIES = {
    "Settlement Success Rate": [98.6, 98.7, 94.2, 96.8, 98.4, 98.9],
    "Payment Success Rate": [97.9, 97.6, 96.4, 97.2, 97.8, 98.1],
    "Transaction Volume": [1_180_000, 1_240_000, 1_205_000, 1_310_000,
                           1_395_000, 1_460_000],
    "Gross Revenue": [42.1, 44.8, 43.0, 47.9, 51.2, 54.6],  # ₹ crore
    "Fraud Rate (bps)": [7.2, 7.0, 7.4, 11.8, 9.1, 8.3],
    "Refund Rate": [1.8, 1.9, 2.1, 2.4, 3.1, 2.6],
    "MAU": [512_000, 528_000, 531_000, 559_000, 587_000, 612_000],
    "Merchant Churn": [1.1, 1.2, 1.4, 1.6, 2.2, 1.7],
}


def build_kpi_workbook() -> None:
    """The monthly KPI workbook — the numbers the reports and RCAs cite."""
    rows = []
    for i, month in enumerate(MONTHS):
        row = {"Month": month}
        for kpi in KPIS:
            row[kpi] = KPI_SERIES[kpi][i]
        rows.append(row)
    df = pd.DataFrame(rows)
    path = OUT / "kpis" / "monthly_kpis_2026.xlsx"
    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        df.to_excel(xl, sheet_name="Monthly KPIs", index=False)


def build_merchant_workbook() -> None:
    """Per-merchant performance — the merchant report's underlying numbers."""
    rows = []
    for m in MERCHANTS:
        region = random.choice(REGIONS)
        rows.append({
            "Merchant": m,
            "Region": region,
            "Monthly_GMV_Cr": round(random.uniform(1.5, 12.0), 2),
            "Settlement_Success_Pct": round(random.uniform(93.5, 99.2), 2),
            "Refund_Rate_Pct": round(random.uniform(1.2, 3.8), 2),
            "Chargeback_bps": round(random.uniform(4, 18), 1),
            "Churn_Risk": random.choice(["Low", "Low", "Medium", "High"]),
        })
    df = pd.DataFrame(rows)
    path = OUT / "kpis" / "merchant_performance_2026H1.xlsx"
    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        df.to_excel(xl, sheet_name="Merchants", index=False)


# ------------------------------------------------------------------- SOPs
def build_sops() -> None:
    w("sops", "SOP-SET-001-settlement-reconciliation.md", f"""
# {REF['sop_settlement']}

**Owner:** {owner('Settlement')}  ·  **Product:** Settlement  ·  **Version:** 3.1

## Purpose
Standard procedure for reconciling merchant settlements against bank payout
files for the **Settlement** product. Governed by {REF['policy_incident']} when a
reconciliation break becomes an incident.

## Procedure
1. Pull the daily bank payout file from each partner bank ({', '.join(BANKS)}).
2. Match payout references against the settlement ledger within the T+1 window.
3. Any unmatched entry older than 4 hours is escalated to the Settlement Lead
   ({PRODUCT_OWNER['Settlement']}) and logged.
4. If a bank API times out, retry per the backoff table; after 3 failures raise
   a Sev-2 incident and follow {REF['sop_incident']}.

## Known gaps
Prior to March 2026 this SOP had **no automated monitoring** for bank API
timeouts — a gap identified in {REF['rca_settlement']} and closed by
{REF['dec_monitoring']}.
""")

    w("sops", "SOP-OPS-002-incident-response.md", f"""
# {REF['sop_incident']}

**Owner:** {owner('Payments')} / {PEOPLE['Tom Fischer']} (SRE)  ·  **Version:** 2.4

## Severity
Severity is assigned per {REF['policy_incident']}. Sev-1/Sev-2 open an incident
bridge (see {REF['meeting_bridge']} for a worked example).

## Steps
1. Declare, assign an Incident Commander, open the bridge.
2. Post updates to the **#payments-incidents** Teams channel every 15 minutes.
3. On resolution, the owning team files an RCA within 48 hours.
4. Decisions taken on the bridge are recorded in the decision log.
""")

    w("sops", "SOP-ENG-003-release-management.md", f"""
# {REF['sop_release']}

**Owner:** {PEOPLE['David Chen']}  ·  **Product:** Payments / Checkout  ·  **Version:** 1.9

## Procedure
Releases ship behind feature flags with staged rollout. A load test is
mandatory for any change touching the Checkout hot path — the step skipped in
{REF['rca_checkout']}, after which this SOP made load testing a hard gate.
""")

    w("sops", "SOP-MER-004-merchant-onboarding.md", f"""
# {REF['sop_onboarding']}

**Owner:** {owner('Merchant Onboarding')}  ·  **Version:** 2.0

KYC, risk scoring, and activation for new merchants. Risk scoring follows
{REF['policy_risk']}; high-risk merchants route to {PEOPLE['Meera Iyer']} for
manual review before go-live.
""")

    w("sops", "SOP-FIN-005-refund-processing.md", f"""
# {REF['sop_refund']}

**Owner:** {owner('Refunds')}  ·  **Version:** 1.5

Governs refund initiation and reconciliation under {REF['policy_refund']}.
Refund SLA is T+5. The May 2026 refund backlog ({REF['rca_refund']}) breached
this SLA and prompted a review of the batch job schedule.
""")

    w("sops", "SOP-RSK-006-fraud-review.md", f"""
# {REF['sop_fraud']}

**Owner:** {owner('Fraud Shield')}  ·  **Version:** 2.2

Manual review queue for transactions scored above the Fraud Shield threshold.
Rule changes require sign-off from {PEOPLE['Meera Iyer']} and {PEOPLE['Lisa Wong']}
(Compliance). See {REF['dec_fraud_rule']} for the April 2026 rule tightening.
""")


# ------------------------------------------------------------------- RCAs
def build_rcas() -> None:
    w("rcas", "RCA-2026-03-014-settlement-success-dip.md", f"""
# {REF['rca_settlement']}

**Product:** Settlement  ·  **Owner:** {owner('Settlement')}  ·  **Severity:** Sev-2
**Incident window:** 2026-03-10 to 2026-03-12  ·  **Related meeting:** {REF['meeting_bridge']}

## Summary
The **Settlement Success Rate** KPI fell from **98.7% (February) to 94.2% in
March 2026** — see `monthly_kpis_2026.xlsx`. Root cause: intermittent HDFC bank
payout API timeouts coincided with a gap in {REF['sop_settlement']}, which had no
automated monitoring for stalled reconciliations, so breaks accumulated for
hours before detection.

## Impact
~₹1.2 crore in delayed merchant payouts across {', '.join(MERCHANTS[:4])}; a spike
in Merchant Success tickets handled by {PEOPLE['Ananya Rao']}.

## Root cause
1. HDFC payout API latency exceeded the retry budget in {REF['sop_settlement']}.
2. No alerting on unmatched settlements older than the T+1 window.

## Corrective actions
- {REF['dec_monitoring']}: add settlement reconciliation monitoring and
  auto-retry (tracked in {REF['brd_autoretry']} and the {REF['roadmap_settlement']}).
- Update {REF['sop_settlement']} to v3.1 with an explicit monitoring step.

Decided on {REF['meeting_bridge']}; owner {PEOPLE['Nisha Patel']}, target April 2026.
""")

    w("rcas", "RCA-2026-02-009-checkout-latency-spike.md", f"""
# {REF['rca_checkout']}

**Product:** Checkout  ·  **Owner:** {owner('Checkout')}  ·  **Severity:** Sev-3
**Incident window:** 2026-02-18

## Summary
Checkout p95 latency spiked to 2.4s after a release that skipped the mandatory
load test in {REF['sop_release']}. Payment Success Rate dipped to 97.6% for the
day. Rolled back within 40 minutes.

## Corrective actions
- Make load testing a hard gate in {REF['sop_release']} (done, v1.9).
- Owner {PEOPLE['Karan Singh']}; reviewed at {REF['meeting_steering']}.
""")

    w("rcas", "RCA-2026-04-021-fraud-rate-uptick.md", f"""
# {REF['rca_fraud']}

**Product:** Fraud Shield  ·  **Owner:** {owner('Fraud Shield')}  ·  **Severity:** Sev-2

## Summary
**Fraud Rate rose from 7.0 to 11.8 bps in April 2026** (`monthly_kpis_2026.xlsx`)
driven by a card-testing attack against several West-region merchants. Existing
rule FS-17 under-scored velocity anomalies.

## Corrective actions
- {REF['dec_fraud_rule']}: tighten rule FS-17 velocity thresholds, per
  {REF['sop_fraud']}. Signed off by {PEOPLE['Meera Iyer']} and {PEOPLE['Lisa Wong']}.
- Fraud rate fell to 9.1 bps in May and 8.3 bps in June.
""")

    w("rcas", "RCA-2026-05-030-refund-backlog.md", f"""
# {REF['rca_refund']}

**Product:** Refunds  ·  **Owner:** {owner('Refunds')}  ·  **Severity:** Sev-3

## Summary
**Refund Rate climbed to 3.1% in May 2026** and the T+5 SLA in {REF['sop_refund']}
was breached for ~4% of refunds when the nightly batch job fell behind after the
May volume surge (Transaction Volume 1.395M). Backlog cleared by early June
(Refund Rate 2.6%).

## Corrective actions
- Re-scheduled the refund batch to run twice daily; owner {PEOPLE['Sara Khan']}.
- Flagged in the May weekly report and the {REF['policy_refund']} review.
""")


# ------------------------------------------------------------------- policies
def build_policies() -> None:
    w("policies", "POL-DATA-01-data-retention.md", f"""
# {REF['policy_retention']}

**Owner:** {PEOPLE['Lisa Wong']} (Compliance)  ·  **Version:** 4.0

Transaction records are retained for 7 years; PII is minimized and access is
governed by {REF['policy_access']}. Applies to all products including Payments,
Settlement, and Refunds.
""")
    w("policies", "POL-FIN-02-refund-policy.md", f"""
# {REF['policy_refund']}

**Owner:** {owner('Refunds')}  ·  **Version:** 2.3

Standard refund SLA is T+5, executed via {REF['sop_refund']}. Reviewed after
{REF['rca_refund']}; batch scheduling tightened in May 2026.
""")
    w("policies", "POL-RSK-03-merchant-risk.md", f"""
# {REF['policy_risk']}

**Owner:** {PEOPLE['Meera Iyer']}  ·  **Version:** 3.2

Merchant risk tiers and thresholds. High-risk onboarding routes through manual
review per {REF['sop_onboarding']}. Fraud rule changes (e.g. {REF['dec_fraud_rule']})
must align with this policy.
""")
    w("policies", "POL-OPS-04-incident-severity.md", f"""
# {REF['policy_incident']}

**Owner:** {PEOPLE['Tom Fischer']}  ·  **Version:** 1.8

Defines Sev-1 to Sev-4. Sev-1/Sev-2 require an incident bridge and a 48-hour RCA
per {REF['sop_incident']}. {REF['rca_settlement']} was handled as Sev-2.
""")
    w("policies", "POL-SEC-05-access-control.md", f"""
# {REF['policy_access']}

**Owner:** {PEOPLE['Lisa Wong']}  ·  **Version:** 2.1

Least-privilege access to production settlement and payout systems. Referenced
by {REF['policy_retention']}.
""")


# ------------------------------------------------------------------- meetings
def build_meetings() -> None:
    w("meetings", "2026-03-12-settlement-incident-bridge.md", f"""
# {REF['meeting_bridge']}

**Type:** Incident Bridge (Sev-2)  ·  **Product:** Settlement
**Attendees:** {PEOPLE['Nisha Patel']}, {PEOPLE['Sara Khan']}, {PEOPLE['Tom Fischer']},
{PEOPLE['David Chen']}, {PEOPLE['Arjun Mehta']}, {PEOPLE['Ananya Rao']}

## Notes
- Settlement Success Rate down to 94.2% for March; root cause traced to HDFC
  payout API timeouts and missing monitoring in {REF['sop_settlement']}.
- {PEOPLE['Ananya Rao']}: merchants {', '.join(MERCHANTS[:3])} raised payout delays.
- Full write-up in {REF['rca_settlement']}.

## Decisions
- **{REF['dec_monitoring']}** — build settlement monitoring + auto-retry.
  Owner {PEOPLE['Nisha Patel']}; captured as {REF['brd_autoretry']}.

## Action items
- [ ] {PEOPLE['David Chen']}: implement timeout alerting (due 2026-03-20)
- [ ] {PEOPLE['Sara Khan']}: update {REF['sop_settlement']} to v3.1 (due 2026-03-18)
- [ ] {PEOPLE['Nisha Patel']}: add auto-retry to {REF['roadmap_settlement']}
""")

    w("meetings", "2026-03-25-product-steering-committee.md", f"""
# {REF['meeting_steering']}

**Type:** Steering Committee (monthly)
**Attendees:** {PEOPLE['Priya Nair']}, {PEOPLE['Arjun Mehta']}, {PEOPLE['Meera Iyer']},
{PEOPLE[JAMES]}, {PEOPLE['Karan Singh']}, {PEOPLE['Nisha Patel']}

## Agenda & notes
- March incident review: {REF['rca_settlement']} and {REF['rca_checkout']}.
- {PEOPLE[JAMES]}: revenue held at ₹43.0 Cr despite the settlement dip.
- Prioritized {REF['roadmap_settlement']} for H1; {REF['brd_autoretry']} approved.

## Decisions
- Fund Settlement Reliability workstream; owner {PEOPLE['Nisha Patel']}.

## Action items
- [ ] {PEOPLE['Rahul Verma']}: add settlement monitoring dashboard (due 2026-04-05)
""")

    # Email thread (as a document so its body reaches the Brain).
    w("meetings", "2026-03-13-email-thread-settlement-escalation.md", f"""
# Email Thread — Settlement payout delays (escalation)

**Channel:** Email  ·  **Subject:** Settlement payout delays — March 2026

---
**From:** {PEOPLE['Ananya Rao']}  **To:** {PEOPLE['Nisha Patel']}, {PEOPLE['Arjun Mehta']}
**Date:** 2026-03-11

Nisha — three of our top merchants ({', '.join(MERCHANTS[:3])}) are flagging
delayed payouts today. Settlement dashboard shows success at ~94%. Can we get an
ETA? This is hurting merchant trust.

---
**From:** {PEOPLE['Nisha Patel']}  **To:** {PEOPLE['Ananya Rao']}, {PEOPLE['Arjun Mehta']}
**Date:** 2026-03-11

We've opened a Sev-2 and scheduled {REF['meeting_bridge']}. Early signal points
to HDFC API timeouts plus a monitoring gap in {REF['sop_settlement']}. Fix plan
will be recorded as {REF['dec_monitoring']}.

---
**From:** {PEOPLE['Arjun Mehta']}  **To:** all
**Date:** 2026-03-12

Thanks both. Approving the auto-retry work ({REF['brd_autoretry']}) into the
{REF['roadmap_settlement']}. Let's close the loop in {REF['meeting_steering']}.
""")

    # Teams conversation (as a document — this is what makes Teams answerable).
    w("meetings", "2026-03-12-teams-payments-incidents.md", f"""
# Teams Conversation — #payments-incidents

**Channel:** Microsoft Teams / #payments-incidents  ·  **Date:** 2026-03-12

**{PEOPLE['Tom Fischer']}:** Declaring Sev-2 on settlement. Success rate 94.2%,
unmatched payouts climbing. Bridge starting — {REF['meeting_bridge']}.

**{PEOPLE['David Chen']}:** Confirmed HDFC payout API timing out ~30% of calls.
Retry budget in {REF['sop_settlement']} exhausted, no alert fired. That's the gap.

**{PEOPLE['Nisha Patel']}:** Logging {REF['dec_monitoring']}. David to add timeout
alerting by 2026-03-20, I'll get auto-retry into {REF['roadmap_settlement']}.

**{PEOPLE['Ananya Rao']}:** Merchant comms sent to {MERCHANTS[0]} and {MERCHANTS[1]}.

**{PEOPLE['Arjun Mehta']}:** 👍 RCA within 48h please — {REF['rca_settlement']}.
""")

    w("meetings", "2026-04-02-teams-fraud-review.md", f"""
# Teams Conversation — #risk-fraud

**Channel:** Microsoft Teams / #risk-fraud  ·  **Date:** 2026-04-02

**{PEOPLE['Meera Iyer']}:** Fraud rate jumped to ~11.8 bps — card-testing on West
region merchants. Rule FS-17 is under-scoring velocity. See {REF['rca_fraud']}.

**{PEOPLE['Lisa Wong']}:** Compliance is fine with tightening FS-17 provided we
log it. Approving {REF['dec_fraud_rule']} under {REF['policy_risk']}.

**{PEOPLE['Meera Iyer']}:** Deploying tonight per {REF['sop_fraud']}. Expect the
rate back toward 9 bps in May.
""")

    w("meetings", "2026-05-20-weekly-product-sync.md", f"""
# Weekly Product Sync — 2026-05-20

**Attendees:** {PEOPLE['Priya Nair']}, {PEOPLE['Karan Singh']}, {PEOPLE['Nisha Patel']},
{PEOPLE['Sara Khan']}, {PEOPLE['Rahul Verma']}

## Notes
- Settlement recovered to 98.4% in May; auto-retry ({REF['brd_autoretry']}) live.
- Refund Rate up to 3.1% — batch backlog, tracked in {REF['rca_refund']}.
- Merchant Churn ticked to 2.2% in South region; {PEOPLE['Ananya Rao']} to dig in.

## Action items
- [ ] {PEOPLE['Sara Khan']}: re-schedule refund batch twice daily (due 2026-05-24)
- [ ] {PEOPLE['Rahul Verma']}: South churn deep-dive for the monthly report
""")

    # A consolidated decision log.
    w("meetings", "2026-H1-decision-log.md", f"""
# Decision Log — H1 2026

| ID | Decision | Owner | Context |
|----|----------|-------|---------|
| {REF['dec_monitoring']} | Build settlement monitoring & auto-retry | {PEOPLE['Nisha Patel']} | {REF['rca_settlement']} / {REF['meeting_bridge']} |
| {REF['dec_fraud_rule']} | Tighten fraud rule FS-17 | {PEOPLE['Meera Iyer']} | {REF['rca_fraud']} |
| DEC-2026-02-03 | Make load testing a release gate | {PEOPLE['David Chen']} | {REF['rca_checkout']} |
| DEC-2026-05-11 | Refund batch twice daily | {PEOPLE['Sara Khan']} | {REF['rca_refund']} |
""")

    # A consolidated action-item tracker.
    w("meetings", "2026-H1-action-items.md", f"""
# Action Item Tracker — H1 2026

- [x] Add settlement timeout alerting — {PEOPLE['David Chen']} — from {REF['meeting_bridge']}
- [x] Update {REF['sop_settlement']} to v3.1 — {PEOPLE['Sara Khan']}
- [x] Auto-retry into {REF['roadmap_settlement']} — {PEOPLE['Nisha Patel']} ({REF['brd_autoretry']})
- [x] Deploy FS-17 tightening — {PEOPLE['Meera Iyer']} — from {REF['dec_fraud_rule']}
- [ ] South-region churn deep-dive — {PEOPLE['Ananya Rao']}
""")


# --------------------------------------------------------------- product docs
def build_product_docs() -> None:
    for product, desc in PRODUCTS.items():
        slug = product.lower().replace(" ", "-")
        w("product", f"product-{slug}.md", f"""
# Product One-Pager — {product}

**Owner:** {owner(product)}

## What it is
{desc}

## Key KPIs
{('Settlement Success Rate, Transaction Volume' if product == 'Settlement' else 'Payment Success Rate, Transaction Volume, Gross Revenue')}.

## Notable H1 2026 events
{('Settlement success dipped in March (' + REF['rca_settlement'] + ') and recovered via ' + REF['brd_autoretry'] + '.') if product == 'Settlement' else ('See the monthly executive reports for ' + product + ' performance.')}
""")

    w("product", "BRD-2026-11-settlement-auto-retry.md", f"""
# {REF['brd_autoretry']}

**Product:** Settlement  ·  **Author:** {PEOPLE['Nisha Patel']}  ·  **Status:** Approved

## Background
{REF['rca_settlement']} exposed a monitoring and retry gap in
{REF['sop_settlement']}. Approved at {REF['meeting_steering']} as
{REF['dec_monitoring']}.

## Requirements
1. Alert when a settlement is unmatched beyond the T+1 window.
2. Auto-retry failed bank payout calls with exponential backoff.
3. A live settlement reliability dashboard for {PEOPLE['Rahul Verma']}'s team.

## Success metric
Settlement Success Rate sustained ≥ 98.5%. (Achieved: 98.4% May, 98.9% June.)
""")

    w("product", "roadmap-H1-2026.md", f"""
# Product Roadmap — H1 2026

## Settlement
- **{REF['roadmap_settlement']}** — monitoring + auto-retry ({REF['brd_autoretry']}).
  Driven by {REF['rca_settlement']}. Delivered April 2026.

## Fraud Shield
- Rule engine v2 and FS-17 tightening ({REF['dec_fraud_rule']}).

## Checkout
- Load-testing gate hardening after {REF['rca_checkout']}.

## Refunds
- Batch scheduling improvements after {REF['rca_refund']}.
""")


# ------------------------------------------------------------------- reports
def build_reports() -> None:
    for i, month in enumerate(MONTHS):
        mname = MONTH_NAME[month]
        ssr = KPI_SERIES["Settlement Success Rate"][i]
        rev = KPI_SERIES["Gross Revenue"][i]
        vol = KPI_SERIES["Transaction Volume"][i]
        fraud = KPI_SERIES["Fraud Rate (bps)"][i]
        highlight = {
            "2026-02": f"Checkout latency incident ({REF['rca_checkout']}).",
            "2026-03": f"Settlement success dipped to {ssr}% "
                       f"({REF['rca_settlement']}); recovery funded via "
                       f"{REF['brd_autoretry']}.",
            "2026-04": f"Fraud rate rose to {fraud} bps ({REF['rca_fraud']}); "
                       f"rule FS-17 tightened ({REF['dec_fraud_rule']}).",
            "2026-05": f"Refund backlog ({REF['rca_refund']}); settlement "
                       f"recovered to {ssr}%.",
        }.get(month, "Steady operations; KPIs within target.")
        w("reports", f"executive-report-{month}.md", f"""
# Executive Monthly Report — {mname} 2026

**Prepared by:** {PEOPLE['Rahul Verma']} for {PEOPLE['Priya Nair']} and {PEOPLE[JAMES]}
**Source:** `monthly_kpis_2026.xlsx`

## Headline KPIs
- Settlement Success Rate: **{ssr}%**
- Gross Revenue: **₹{rev} Cr**
- Transaction Volume: **{vol:,}**
- Fraud Rate: **{fraud} bps**

## Highlight
{highlight}

## Outlook
{'Recovery on track; settlement reliability work delivering.' if i >= 3 else 'Monitoring incident follow-ups from the steering committee.'}
""")

    # Weekly report (representative).
    w("reports", "weekly-report-2026-03-15.md", f"""
# Weekly Report — Week of 2026-03-15

**Prepared by:** {PEOPLE['Rahul Verma']}

- **Settlement:** Sev-2 resolved; success rate stabilizing after the March dip
  ({REF['rca_settlement']}). Auto-retry work started ({REF['brd_autoretry']}).
- **Checkout:** stable following {REF['rca_checkout']} remediation.
- **Risk:** watching West-region velocity ahead of the April fraud uptick.
- Open action items tracked from {REF['meeting_bridge']}.
""")

    # Merchant report.
    w("reports", "merchant-report-2026H1.md", f"""
# Merchant Performance Report — H1 2026

**Prepared by:** {PEOPLE['Ananya Rao']}  ·  **Source:** `merchant_performance_2026H1.xlsx`

## Summary
Top merchants by GMV: {', '.join(MERCHANTS[:5])}. Payout reliability was affected
in March by {REF['rca_settlement']} — {', '.join(MERCHANTS[:3])} were most impacted
and received proactive comms. South-region churn rose to 2.2% in May and is
under review.

## Watch list
- {MERCHANTS[6]} and {MERCHANTS[8]}: elevated chargeback rates, per {REF['policy_risk']}.
""")

    # Risk report.
    w("reports", "risk-report-2026Q2.md", f"""
# Risk Report — Q2 2026

**Prepared by:** {PEOPLE['Meera Iyer']} and {PEOPLE['Lisa Wong']}

## Fraud
Fraud Rate peaked at 11.8 bps in April ({REF['rca_fraud']}) due to card-testing
on West-region merchants; mitigated by {REF['dec_fraud_rule']} (rule FS-17),
falling to 8.3 bps by June.

## Operational risk
Settlement reliability materially improved after {REF['brd_autoretry']} closed
the gap found in {REF['rca_settlement']}. Residual risk: partner-bank API
stability (HDFC).

## Compliance
All changes logged under {REF['policy_risk']} and {REF['policy_access']}.
""")


# ------------------------------------------------------------------------ run
def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    build_kpi_workbook()
    build_merchant_workbook()
    build_sops()
    build_rcas()
    build_policies()
    build_meetings()
    build_product_docs()
    build_reports()

    files = sorted(p for p in OUT.rglob("*") if p.is_file())
    by_folder: dict[str, int] = {}
    for p in files:
        by_folder[p.parent.name] = by_folder.get(p.parent.name, 0) + 1
    print(f"Enterprise corpus written to {OUT.resolve()}")
    print(f"  {len(files)} files across {len(by_folder)} folders:")
    for folder, count in sorted(by_folder.items()):
        print(f"    {folder:<10} {count}")


if __name__ == "__main__":
    main()
