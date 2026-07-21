#!/usr/bin/env python
"""Synthetic Enterprise Generator — NPCI UPI Products (V3.0).

Generates ONE coherent fictional organization — "NPCI (Synthetic
Demonstration)", the UPI Products department — and exactly one business week
of its activity. The point is not volume but *connectedness*: every email,
Teams thread, meeting, RCA, SOP, decision, task, report and Excel workbook
belongs to the same company and references other artifacts the way real ones
do. A single narrative spine — a UPI Autopay mandate-failure spike caused by a
bank outage and a PSP callback timeout — runs Monday→Sunday through the whole
corpus, so the Enterprise Brain can answer a question by combining sources
rather than returning one file.

Design guarantees
-----------------
* **One source of truth for numbers.** Every KPI value lives once in
  ``KPICatalog``; Excel workbooks, reports, meetings and emails all read from
  it, so a figure quoted in an email equals the cell in the workbook equals
  the line in the executive report.
* **One roster.** Every person is drawn once from ``Org`` and referenced by
  lookup, so names, teams and titles never drift.
* **Forward time.** Every artifact carries a timestamp; within the week
  emails precede meetings, meetings precede RCAs, RCAs precede SOP updates,
  SOP updates precede reports, reports precede recommendations.
* **No orphans.** Every artifact declares ``Refs:`` to at least three others;
  a validation pass fails the build if any reference is dangling or any
  artifact has fewer than three links.
* **Deterministic.** ``--seed`` fully determines the organization; the same
  seed always produces the same company, a different seed a different but
  internally consistent one.

Usage
-----
    python generate_enterprise.py --days 7 --seed 2026

Produces ``enterprise_data/`` (master/, day_01..day_07/, scenarios/) written
as parser-supported files (.md, .xlsx, .csv) whose folders map onto the
platform's document source kinds, so ``backend/scripts/bootstrap_enterprise_
demo.py`` can register them and the ordinary sync → document-intelligence →
Brain pipeline ingests the whole organization unchanged.
"""
from __future__ import annotations

import argparse
import random
import shutil
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill
    _XLSX = True
except ImportError:  # pragma: no cover - openpyxl ships with the platform
    _XLSX = False


# ===========================================================================
# Organization definition — the fictional NPCI UPI Products department.
# ===========================================================================
ORG_NAME = "NPCI (Synthetic Demonstration)"
DEPARTMENT = "UPI Products"

TEAMS = [
    "UPI Core", "UPI Autopay", "UPI Lite", "UPI Lite X", "UPI Credit",
    "UPI International", "Merchant Products", "QR Payments",
    "Product Strategy", "Product Analytics", "Product Operations",
    "Risk & Compliance", "Customer Experience", "PSP Integration",
    "AI & Innovation",
]

OFFICES = [
    ("Mumbai HQ", "Mumbai", "West"),
    ("Hyderabad Tech Centre", "Hyderabad", "South"),
    ("Bengaluru Innovation Hub", "Bengaluru", "South"),
    ("Delhi NCR Office", "Gurugram", "North"),
    ("Chennai Office", "Chennai", "South"),
    ("Kolkata Office", "Kolkata", "East"),
]

REGIONS = ["North", "South", "East", "West", "Central"]

# Name pools — the RNG draws the roster from these, so a different seed yields
# a different (still realistic) set of colleagues.
FIRST_NAMES = [
    "Aarav", "Aditi", "Ananya", "Arjun", "Divya", "Farhan", "Gaurav",
    "Ishaan", "Kavya", "Lakshmi", "Manish", "Meera", "Naveen", "Neha",
    "Nikhil", "Pooja", "Pranav", "Priya", "Rahul", "Rajesh", "Rekha",
    "Rohan", "Sanjay", "Shreya", "Sneha", "Sunil", "Tanvi", "Varun",
    "Vikram", "Yash", "Zoya", "Deepak", "Anjali", "Karthik", "Swati",
    "Harsh", "Ritu", "Amit", "Nandini", "Suresh",
]
LAST_NAMES = [
    "Agarwal", "Bhat", "Chandra", "Desai", "Gupta", "Iyer", "Joshi",
    "Kapoor", "Krishnan", "Kulkarni", "Malhotra", "Menon", "Nair", "Pillai",
    "Rao", "Reddy", "Sharma", "Shetty", "Singh", "Subramanian", "Verma",
    "Bose", "Chopra", "Dutta", "Ghosh", "Mahajan", "Nanda", "Patel",
]

# Executive team — stable titles; the RNG fills the names.
EXEC_TITLES = [
    ("Chief Product Officer", "UPI Products"),
    ("Senior Vice President, UPI Products", "UPI Products"),
    ("Vice President, Product Strategy", "Product Strategy"),
    ("Vice President, Risk & Compliance", "Risk & Compliance"),
    ("Head of Product Operations", "Product Operations"),
]

# The products of the department, each owned by a team.
PRODUCTS = [
    ("UPI Core", "UPI Core", "Core real-time person-to-person and "
     "person-to-merchant payments rail across all UPI apps."),
    ("UPI Autopay", "UPI Autopay", "Recurring e-mandates for subscriptions, "
     "SIPs, bill payments and EMIs."),
    ("UPI Lite", "UPI Lite", "On-device low-value payments without a PIN for "
     "small-ticket transactions."),
    ("UPI Lite X", "UPI Lite X", "Offline UPI Lite payments over NFC without "
     "an active internet connection."),
    ("UPI Credit", "UPI Credit", "Credit-line-on-UPI and RuPay credit card "
     "linkage for pay-later flows."),
    ("UPI International", "UPI International", "Cross-border UPI acceptance for "
     "Indian travellers and NRIs."),
    ("Merchant Products", "Merchant Products", "Merchant onboarding, "
     "soundbox, and settlement products."),
    ("QR Payments", "QR Payments", "Interoperable UPI QR (static and dynamic) "
     "for merchant acceptance."),
]

# Merchant, bank and PSP pools — the RNG samples and assigns attributes.
MERCHANT_POOL = [
    ("BharatKart", "E-commerce"), ("FreshBasket", "Grocery"),
    ("MetroRide", "Mobility"), ("FlixStream", "OTT / Subscriptions"),
    ("EduPrime", "EdTech"), ("HealthFirst", "Pharmacy"),
    ("TravelGo", "Travel"), ("StyleHub", "Fashion"),
    ("QuickBite", "Food Delivery"), ("PowerPay Utilities", "Utilities"),
    ("InsureWell", "Insurance"), ("GadgetZone", "Electronics"),
    ("DailyMart", "Retail"), ("WealthGrow", "Wealth / SIP"),
    ("CityFuel", "Fuel"),
]
BANK_POOL = [
    "HDFC Bank", "ICICI Bank", "State Bank of India", "Axis Bank",
    "Kotak Mahindra Bank", "Punjab National Bank", "Bank of Baroda",
    "Canara Bank", "Yes Bank", "IDFC First Bank", "Union Bank of India",
    "IndusInd Bank",
]
PSP_POOL = [
    "PhonePe", "Google Pay", "Paytm", "BHIM", "Amazon Pay", "CRED",
    "Navi", "Slice", "Fampay", "WhatsApp Pay",
]

# Distribution lists / email groups and Teams channels — stable handles.
DISTRIBUTION_LISTS = [
    ("upi-leadership@npci-demo.in", "UPI Products leadership"),
    ("upi-core-team@npci-demo.in", "UPI Core engineering and product"),
    ("upi-autopay@npci-demo.in", "UPI Autopay product and ops"),
    ("upi-incident-bridge@npci-demo.in", "Live incident bridge distribution"),
    ("upi-risk-compliance@npci-demo.in", "Risk & Compliance"),
    ("upi-merchant-success@npci-demo.in", "Merchant Products & Success"),
    ("upi-psp-integration@npci-demo.in", "PSP Integration partners"),
    ("upi-analytics@npci-demo.in", "Product Analytics"),
    ("upi-all@npci-demo.in", "All UPI Products staff"),
]
TEAMS_CHANNELS = [
    ("UPI Products", "General", "Department-wide announcements"),
    ("UPI Products", "Incident Bridge", "Live incident coordination"),
    ("UPI Products", "Autopay", "UPI Autopay squad"),
    ("UPI Products", "Core Engineering", "UPI Core engineering"),
    ("UPI Products", "PSP Integration", "PSP partner integration"),
    ("UPI Products", "Risk and Compliance", "Risk, fraud and compliance"),
    ("UPI Products", "Merchant Success", "Merchant onboarding and support"),
    ("UPI Products", "Customer Experience", "Support and complaints"),
    ("UPI Products", "Leadership", "Leadership discussion"),
    ("UPI Products", "Analytics", "Product analytics and dashboards"),
]
MEETING_ROOMS = [
    ("Ganga", "Mumbai HQ", 12), ("Yamuna", "Mumbai HQ", 8),
    ("Kaveri", "Hyderabad Tech Centre", 10), ("Godavari", "Bengaluru Innovation Hub", 14),
    ("Narmada", "Delhi NCR Office", 6), ("Virtual Bridge A", "Online", 200),
]

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]


# ===========================================================================
# People & organization roster (drawn once, referenced everywhere).
# ===========================================================================
@dataclass
class Person:
    emp_id: str
    name: str
    title: str
    team: str
    email: str
    office: str
    region: str
    manager: str = ""       # emp_id of manager


@dataclass
class Org:
    """The whole organization: people, products, merchants, banks, PSPs."""
    rng: random.Random
    people: list[Person] = field(default_factory=list)
    by_id: dict[str, Person] = field(default_factory=dict)
    by_team: dict[str, list[Person]] = field(default_factory=dict)
    products: list[dict] = field(default_factory=list)
    merchants: list[dict] = field(default_factory=list)
    banks: list[dict] = field(default_factory=list)
    psps: list[dict] = field(default_factory=list)
    exec_team: list[Person] = field(default_factory=list)

    def build(self) -> None:
        used_names: set[str] = set()

        def fresh_name() -> str:
            for _ in range(200):
                nm = (f"{self.rng.choice(FIRST_NAMES)} "
                      f"{self.rng.choice(LAST_NAMES)}")
                if nm not in used_names:
                    used_names.add(nm)
                    return nm
            # Exhausted the unique combinations — disambiguate with a suffix.
            nm = f"{self.rng.choice(FIRST_NAMES)} {self.rng.choice(LAST_NAMES)}"
            used_names.add(nm)
            return nm

        def email_for(name: str) -> str:
            handle = name.lower().replace(" ", ".").replace("'", "")
            return f"{handle}@npci-demo.in"

        seq = 1001

        def add(title: str, team: str) -> Person:
            nonlocal seq
            name = fresh_name()
            office, _city, region = self.rng.choice(OFFICES)
            p = Person(emp_id=f"EMP-{seq}", name=name, title=title, team=team,
                       email=email_for(name), office=office, region=region)
            seq += 1
            self.people.append(p)
            self.by_id[p.emp_id] = p
            self.by_team.setdefault(team, []).append(p)
            return p

        # Executive team first.
        for title, team in EXEC_TITLES:
            self.exec_team.append(add(title, team))
        cpo = self.exec_team[0]

        # Each team: a lead and one or two members.
        team_lead: dict[str, Person] = {}
        for team in TEAMS:
            lead = add(f"{team} Lead", team)
            lead.manager = cpo.emp_id
            team_lead[team] = lead
            for role in ("Senior Product Manager", "Product Manager",
                         "Engineering Manager"):
                if self.rng.random() < 0.6:
                    m = add(f"{role}, {team}", team)
                    m.manager = lead.emp_id

        # Products, each owned by the lead of its team.
        for name, team, desc in PRODUCTS:
            owner = team_lead.get(team, cpo)
            self.products.append({
                "product_id": f"PRD-{name.replace(' ', '').upper()[:8]}",
                "name": name, "team": team, "owner": owner.emp_id,
                "owner_name": owner.name, "description": desc,
            })

        # Banks — a live UPI member set with health attributes.
        for i, bank in enumerate(BANK_POOL, start=1):
            self.banks.append({
                "bank_id": f"BANK-{i:03d}", "name": bank,
                "ifsc_prefix": bank.split()[0][:4].upper(),
                "region": self.rng.choice(REGIONS),
                "tier": self.rng.choice(["Tier 1", "Tier 1", "Tier 2"]),
            })

        # PSP apps.
        for i, psp in enumerate(PSP_POOL, start=1):
            self.psps.append({
                "psp_id": f"PSP-{i:03d}", "name": psp,
                "sponsor_bank": self.rng.choice(BANK_POOL),
            })

        # Merchants — sampled and attributed.
        for i, (name, cat) in enumerate(MERCHANT_POOL, start=1):
            self.merchants.append({
                "merchant_id": f"MID-{2000 + i}", "name": name,
                "category": cat, "region": self.rng.choice(REGIONS),
                "psp": self.rng.choice(PSP_POOL),
                "settlement_bank": self.rng.choice(BANK_POOL),
                "monthly_gmv_cr": round(self.rng.uniform(8.0, 240.0), 1),
            })

    # -- convenience lookups -------------------------------------------------
    def lead(self, team: str) -> Person:
        return self.by_team[team][0]

    def anyone(self, team: str) -> Person:
        return self.rng.choice(self.by_team[team])

    def person(self, emp_id: str) -> Person:
        return self.by_id[emp_id]

    def named(self, p: Person) -> str:
        return f"{p.name} ({p.title})"


# ===========================================================================
# KPI catalog — the single source of truth for every number in the corpus.
# ===========================================================================
# The story arc is fixed: a UPI Autopay mandate-failure spike detected Monday,
# bottoming Tuesday, root-caused Wednesday, fixed Thursday, recovering Friday,
# monitored across the weekend. Baselines take a small seed-driven jitter so a
# different seed is a different-but-plausible company; the shape never changes.
KPI_UNITS = {
    "UPI Transactions (M/day)": "million transactions/day",
    "Success Rate (%)": "percent",
    "Settlement Success (%)": "percent",
    "Technical Declines (%)": "percent",
    "Business Declines (%)": "percent",
    "Merchant Adoption (M)": "million live merchants",
    "Active Banks": "count",
    "Active PSPs": "count",
    "UPI Lite Adoption (M)": "million users",
    "Autopay Registrations (K/day)": "thousand new mandates/day",
    "Fraud Alerts": "alerts/day",
    "Customer Complaints": "complaints/day",
    "Merchant Complaints": "complaints/day",
    "Response Time (ms)": "p95 milliseconds",
    "Risk Score": "0-100 (higher = worse)",
}

# Direction of "good": whether a higher value is better, for report narration.
KPI_HIGHER_BETTER = {
    "UPI Transactions (M/day)": True, "Success Rate (%)": True,
    "Settlement Success (%)": True, "Technical Declines (%)": False,
    "Business Declines (%)": False, "Merchant Adoption (M)": True,
    "Active Banks": True, "Active PSPs": True, "UPI Lite Adoption (M)": True,
    "Autopay Registrations (K/day)": True, "Fraud Alerts": False,
    "Customer Complaints": False, "Merchant Complaints": False,
    "Response Time (ms)": False, "Risk Score": False,
}


class KPICatalog:
    """Seven days (Mon-Sun) of every KPI, one value per day. The dip/recovery
    shape is fixed; the seed nudges the baselines."""

    def __init__(self, rng: random.Random):
        j = lambda scale: 1.0 + rng.uniform(-scale, scale)  # noqa: E731
        # Each series is [Mon, Tue, Wed, Thu, Fri, Sat, Sun].
        self.series: dict[str, list[float]] = {
            "UPI Transactions (M/day)": [round(v * j(0.03), 1) for v in
                [546, 551, 549, 558, 564, 579, 571]],
            "Success Rate (%)": [round(v, 2) for v in
                [98.74, 98.29, 98.52, 99.02, 99.31, 99.36, 99.38]],
            "Settlement Success (%)": [round(v, 2) for v in
                [98.90, 98.55, 98.71, 99.28, 99.55, 99.60, 99.63]],
            "Technical Declines (%)": [round(v, 2) for v in
                [0.92, 1.31, 1.18, 0.74, 0.49, 0.44, 0.42]],
            "Business Declines (%)": [round(v, 2) for v in
                [0.34, 0.40, 0.30, 0.24, 0.20, 0.20, 0.20]],
            "Merchant Adoption (M)": [round(v * j(0.02), 2) for v in
                [61.2, 61.4, 61.6, 61.9, 62.2, 62.5, 62.7]],
            "Active Banks": [int(round(v)) for v in
                [641, 640, 641, 643, 645, 646, 646]],
            "Active PSPs": [int(round(v)) for v in
                [58, 57, 58, 59, 60, 60, 60]],
            "UPI Lite Adoption (M)": [round(v * j(0.02), 1) for v in
                [41.2, 41.6, 42.0, 42.5, 43.0, 43.6, 44.1]],
            "Autopay Registrations (K/day)": [int(round(v * j(0.04))) for v in
                [512, 468, 455, 523, 561, 548, 502]],
            "Fraud Alerts": [int(round(v * j(0.05))) for v in
                [1240, 1418, 1372, 1195, 1088, 1042, 1015]],
            "Customer Complaints": [int(round(v * j(0.04))) for v in
                [3120, 4870, 4210, 2980, 2210, 1980, 1875]],
            "Merchant Complaints": [int(round(v * j(0.04))) for v in
                [412, 690, 588, 360, 240, 205, 190]],
            "Response Time (ms)": [int(round(v * j(0.03))) for v in
                [842, 968, 915, 812, 742, 730, 728]],
            "Risk Score": [int(round(v)) for v in
                [38, 57, 52, 41, 33, 30, 29]],
        }

    def names(self) -> list[str]:
        return list(self.series.keys())

    def value(self, kpi: str, day_index: int):
        return self.series[kpi][day_index]

    def fmt(self, kpi: str, day_index: int) -> str:
        v = self.value(kpi, day_index)
        if "%" in kpi:
            return f"{v}%"
        if kpi == "Response Time (ms)":
            return f"{v} ms"
        if isinstance(v, float):
            return f"{v}"
        return f"{v:,}"

    def delta(self, kpi: str, day_index: int):
        """Change versus the previous day (None on Monday)."""
        if day_index == 0:
            return None
        return round(self.value(kpi, day_index)
                     - self.value(kpi, day_index - 1), 2)


# ===========================================================================
# Narrative spine — canonical artifact IDs and the week's story.
# ===========================================================================
class Story:
    """The connective tissue: canonical IDs every artifact points at, plus
    the incident specifics (which bank and PSP failed) chosen by the seed."""

    def __init__(self, org: Org, rng: random.Random, week_start: date):
        self.org = org
        self.rng = rng
        self.week_start = week_start
        self.dates = [week_start + timedelta(days=i) for i in range(7)]

        # The bank and PSP at the centre of the incident.
        self.bank = rng.choice([b for b in org.banks
                                if b["tier"] == "Tier 1"])
        self.psp = rng.choice(org.psps)
        # The most-affected merchants (Autopay-heavy categories).
        autopay_cats = {"OTT / Subscriptions", "Utilities", "Insurance",
                        "Wealth / SIP", "EdTech"}
        affected = [m for m in org.merchants
                    if m["category"] in autopay_cats] or org.merchants[:4]
        self.affected_merchants = affected[:4]

        # Canonical IDs — allocated up front so every artifact can cite them.
        wk = week_start.strftime("%Y%m%d")
        self.ID = {
            "incident": f"INC-{wk}-01",
            "rca": f"RCA-{week_start.year}-{week_start.strftime('%m%d')}-01",
            "decision": f"DEC-{week_start.year}-{week_start.strftime('%m%d')}-01",
            "sop": "SOP-UPI-AUTOPAY-014",
            "brd": f"BRD-{week_start.year}-071 Autopay Bank Failover",
            "prd": f"PRD-{week_start.year}-071 Autopay Resilient Mandate Execution",
            "mtg_bridge": "MTG-D01-INCIDENT-BRIDGE",
            "mtg_invest": "MTG-D02-INVESTIGATION",
            "mtg_rca": "MTG-D03-RCA-REVIEW",
            "mtg_cab": "MTG-D04-CHANGE-ADVISORY",
            "mtg_weekly": "MTG-D06-WEEKLY-REVIEW",
            "mtg_exec": "MTG-D07-EXEC-REVIEW",
            "kpi_workbook": "upi_kpis_week.xlsx",
        }
        # Per-day daily report IDs.
        for i in range(7):
            self.ID[f"report_d{i+1}"] = f"RPT-D{i+1:02d}-DAILY"
        self.ID["report_exec"] = "RPT-EXEC-WEEKLY"
        self.ID["report_risk"] = "RPT-RISK-WEEKLY"
        self.ID["report_merchant"] = "RPT-MERCHANT-WEEKLY"

    def when(self, day_index: int, hh: int, mm: int = 0) -> datetime:
        return datetime.combine(self.dates[day_index], time(hh, mm))


# ===========================================================================
# Artifact writer — records every file plus its declared cross-references, so
# a validation pass can prove the graph is fully connected.
# ===========================================================================
@dataclass
class Artifact:
    art_id: str
    kind: str
    path: Path
    when: datetime
    refs: list[str]


class Corpus:
    def __init__(self, out: Path):
        self.out = out
        self.artifacts: list[Artifact] = []
        self._ids: set[str] = set()

    def _ref_block(self, refs: list[str]) -> str:
        clean = [r for r in refs if r]
        return "Refs: " + ", ".join(clean)

    def doc(self, day: int | None, sub: str, filename: str, art_id: str,
            kind: str, when: datetime, title: str, body: str,
            refs: list[str]) -> str:
        """Write a Markdown artifact with a consistent metadata header and a
        Refs line, and register it (with its refs) for validation."""
        folder = (self.out / (f"day_{day:02d}" if day else "master") / sub
                  if sub else self.out / (f"day_{day:02d}" if day else "master"))
        folder.mkdir(parents=True, exist_ok=True)
        header = (f"---\n"
                  f"id: {art_id}\n"
                  f"type: {kind}\n"
                  f"organization: {ORG_NAME}\n"
                  f"department: {DEPARTMENT}\n"
                  f"timestamp: {when.isoformat()}\n"
                  f"---\n\n")
        clean_refs = _dedupe(refs)
        text = f"{header}# {title}\n\n{body.strip()}\n\n{self._ref_block(clean_refs)}\n"
        (folder / filename).write_text(text, encoding="utf-8")
        self.artifacts.append(Artifact(art_id, kind, folder / filename, when,
                                       clean_refs))
        self._ids.add(art_id)
        return art_id

    def raw(self, day: int | None, sub: str, filename: str, art_id: str,
            kind: str, when: datetime, refs: list[str]) -> Path:
        """Register a non-Markdown artifact (e.g. an Excel workbook written
        separately) and return the path to write into."""
        folder = (self.out / (f"day_{day:02d}" if day else "master") / sub
                  if sub else self.out / (f"day_{day:02d}" if day else "master"))
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / filename
        self.artifacts.append(Artifact(art_id, kind, path, when,
                                        _dedupe(refs)))
        self._ids.add(art_id)
        return path

    # Reference data (workbooks, master tables) are valid link *targets* but
    # are not required to declare three references of their own.
    _DATA_KINDS = {"workbook", "master"}

    def validate(self) -> list[str]:
        """Return a list of integrity problems (empty = fully connected)."""
        problems: list[str] = []
        known = self._ids
        for a in self.artifacts:
            if a.kind not in self._DATA_KINDS and len(a.refs) < 3:
                problems.append(
                    f"{a.art_id}: only {len(a.refs)} references (need >= 3)")
            for r in a.refs:
                if r not in known:
                    problems.append(f"{a.art_id}: dangling reference '{r}'")
        return problems


def _dedupe(refs: list[str]) -> list[str]:
    seen: list[str] = []
    for r in refs:
        if r and r not in seen:
            seen.append(r)
    return seen


# ===========================================================================
# Prose helpers — small utilities so narration reads naturally and reuses the
# one KPI source of truth. Writing style is varied per author below.
# ===========================================================================
def kline(kpis: "KPICatalog", kpi: str, di: int, with_delta: bool = True) -> str:
    """A KPI stated with its value and (optionally) day-over-day change."""
    base = f"{kpi.split(' (')[0]} at {kpis.fmt(kpi, di)}"
    if with_delta and di > 0:
        d = kpis.delta(kpi, di)
        if d is not None and d != 0:
            arrow = "up" if d > 0 else "down"
            base += f" ({arrow} {abs(d)} vs {WEEKDAYS[di-1]})"
    return base


def sign_off(p: Person) -> str:
    first = p.name.split()[0]
    return f"{first}\n{p.name}\n{p.title}\n{DEPARTMENT}, {ORG_NAME}"


# ===========================================================================
# Day 1 (Monday) — anomaly detected: emails, Teams, incident bridge.
# ===========================================================================
def build_day1(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 0
    analytics = org.lead("Product Analytics")
    autopay = org.lead("UPI Autopay")
    core = org.lead("UPI Core")
    ops = org.lead("Product Operations")
    psp_lead = org.lead("PSP Integration")
    risk = org.lead("Risk & Compliance")
    cx = org.lead("Customer Experience")
    cpo = org.exec_team[0]
    svp = org.exec_team[1]
    ID = s.ID
    bank, psp = s.bank, s.psp

    # 08:40 — Analytics detects the anomaly and emails leadership + squads.
    c.doc(1, "outlook", "EMAIL-D01-001-anomaly-detected.md", "EMAIL-D01-001",
          "email", s.when(di, 8, 40),
          "Autopay success dip flagged by the morning KPI sweep",
          f"""**From:** {analytics.name} <{analytics.email}>
**To:** upi-autopay@npci-demo.in; upi-leadership@npci-demo.in
**Cc:** {ops.name}, {psp_lead.name}
**Sent:** {s.when(di, 8, 40).strftime('%a %d %b %Y, %H:%M IST')}
**Subject:** [Action] UPI Autopay mandate success dipping since ~06:30

Team,

The automated KPI sweep this morning flagged UPI Autopay. Overall
{kline(k, 'Success Rate (%)', di)} and {kline(k, 'Settlement Success (%)', di)},
both below our 99.2% floor. {kline(k, 'Technical Declines (%)', di)} — the jump
is almost entirely on Autopay mandate *execution* calls, not collends or P2P.

Early cut of the data points at {bank['name']} handles and callbacks routed via
{psp['name']}. Autopay Registrations are also soft this morning
({k.fmt('Autopay Registrations (K/day)', di)}K vs a ~510K weekday norm).

I have opened incident {ID['incident']}. Proposing we convene the incident
bridge at 09:30. Dashboards and the day-1 workbook are attached to
{ID['report_d1']}.

{sign_off(analytics)}""",
          [ID["incident"], ID["report_d1"], ID["kpi_workbook"],
           ID["mtg_bridge"]])

    # 08:55 — Autopay lead replies, escalates.
    c.doc(1, "outlook", "EMAIL-D01-002-autopay-reply.md", "EMAIL-D01-002",
          "email", s.when(di, 8, 55),
          "RE: UPI Autopay mandate success dipping since ~06:30",
          f"""**From:** {autopay.name} <{autopay.email}>
**To:** {analytics.name}; upi-leadership@npci-demo.in
**Cc:** upi-incident-bridge@npci-demo.in
**Sent:** {s.when(di, 8, 55).strftime('%a %d %b %Y, %H:%M IST')}
**Subject:** RE: UPI Autopay mandate success dipping since ~06:30

Confirmed from our side. Mandate execution failures started around 06:25 and are
concentrated on subscription and SIP debits for {', '.join(m['name'] for m in s.affected_merchants[:3])}.
This lines up with {analytics.name.split()[0]}'s read on {bank['name']} / {psp['name']}.

Declaring this a Sev-2 under {ID['incident']}. {psp_lead.name.split()[0]} — can
PSP Integration pull the {psp['name']} callback latency for the last 4 hours
before the 09:30 bridge ({ID['mtg_bridge']})? I want the RCA clock started.

{sign_off(autopay)}""",
          [ID["incident"], ID["mtg_bridge"], "EMAIL-D01-001"])

    # Teams — incident bridge channel spins up.
    c.doc(1, "teams", "TEAMS-D01-incident-bridge.md", "TEAMS-D01-INCIDENT",
          "teams", s.when(di, 9, 5),
          "Teams — UPI Products / Incident Bridge",
          f"""**Channel:** UPI Products / Incident Bridge
**Date:** {s.dates[di].strftime('%A %d %b %Y')}

**{ops.name}** · 09:05
Opening the bridge for {ID['incident']} (Sev-2, UPI Autopay). Bridge invite for
09:30 is out — {ID['mtg_bridge']}. Please keep updates here every 15 minutes.

**{analytics.name}** · 09:07
Numbers so far: {kline(k, 'Success Rate (%)', di, False)}, {kline(k, 'Technical Declines (%)', di, False)},
Customer Complaints running at {k.fmt('Customer Complaints', di)} for the day and
climbing. Risk Score is up to {k.fmt('Risk Score', di)}.

**{psp_lead.name}** · 09:16
{psp['name']} callback p95 is elevated — timeouts on mandate execution
acknowledgements. {bank['name']} core is returning intermittent 5xx on the debit
leg. Looks like a bank-side maintenance window bleeding into peak.

**{core.name}** · 09:22
UPI Core rail itself is healthy — P2P and collect are green. This is isolated to
the Autopay execution path when it hits {bank['name']} via {psp['name']}.

**{autopay.name}** · 09:27
Agreed. Moving detail to the bridge now — {ID['mtg_bridge']}. RCA will be
{ID['rca']}.""",
          [ID["incident"], ID["mtg_bridge"], ID["rca"], "EMAIL-D01-001"])

    # 09:30 — incident bridge meeting.
    attendees = [ops, autopay, analytics, psp_lead, core, risk, cx]
    c.doc(1, "meetings", "MTG-D01-incident-bridge.md", ID["mtg_bridge"],
          "meeting", s.when(di, 9, 30),
          "Incident Bridge — UPI Autopay mandate failures (Sev-2)",
          f"""**Meeting ID:** {ID['mtg_bridge']}  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** {s.when(di, 9, 30).strftime('%d %b %Y %H:%M IST')}
**Incident:** {ID['incident']}  ·  **Recording:** rec/{ID['mtg_bridge'].lower()}.mp4 (00:41:12)

## Attendees
{chr(10).join('- ' + org.named(p) for p in attendees)}

## Agenda
1. Confirm scope and severity of {ID['incident']}.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- {analytics.name.split()[0]} presented the morning sweep: {kline(k, 'Success Rate (%)', di)},
  {kline(k, 'Settlement Success (%)', di)}, {kline(k, 'Technical Declines (%)', di)}. The
  regression is confined to UPI Autopay mandate execution.
- {psp_lead.name.split()[0]} reported {psp['name']} callback timeouts coinciding with
  intermittent 5xx from {bank['name']} on the debit leg during a bank maintenance
  window that overran into the 06:00-09:00 peak.
- {core.name.split()[0]} confirmed UPI Core P2P/collect unaffected.
- {cx.name.split()[0]} noted Customer Complaints at {k.fmt('Customer Complaints', di)} and
  Merchant Complaints at {k.fmt('Merchant Complaints', di)}, mostly failed SIP/subscription debits.

## Decisions
- Treat {ID['incident']} as Sev-2; RCA {ID['rca']} to be drafted by EOD Tuesday.
- Immediate mitigation: {psp['name']} to raise callback timeout and NPCI to shift
  Autopay retries away from {bank['name']} during the window (manual, pending a
  permanent fix considered under {ID['decision']}).

## Action items
- [ ] {psp_lead.name}: quantify {psp['name']}/{bank['name']} failure correlation — due Tue 12:00 (TASK-0001)
- [ ] {autopay.name}: draft {ID['rca']} — due Tue 18:00 (TASK-0002)
- [ ] {analytics.name}: complaint + KPI breakdown for {ID['report_d1']} — due Mon 17:00 (TASK-0003)""",
          [ID["incident"], ID["rca"], ID["decision"], ID["report_d1"],
           "TEAMS-D01-INCIDENT"])

    # 17:00 — Day-1 daily report.
    _daily_report(c, org, k, s, di, extra_refs=[ID["mtg_bridge"], ID["incident"]],
                  headline=f"UPI Autopay Sev-2 declared ({ID['incident']}); mandate "
                           f"execution failures on {bank['name']}/{psp['name']}.")

    # Tasks opened today.
    _task(c, org, s, di, "TASK-0001", "Quantify PSP/bank failure correlation",
          org.lead("PSP Integration"), org.lead("UPI Autopay"), 1, "in_progress",
          s.when(1, 12, 0), [ID["mtg_bridge"], ID["incident"], ID["rca"]])
    _task(c, org, s, di, "TASK-0002", f"Draft {ID['rca']}",
          org.lead("UPI Autopay"), org.exec_team[1], 1, "in_progress",
          s.when(1, 18, 0), [ID["mtg_bridge"], ID["rca"], ID["incident"]])
    _task(c, org, s, di, "TASK-0003", "Complaint & KPI breakdown for day-1 report",
          org.lead("Product Analytics"), org.lead("Product Operations"), 2,
          "done", s.when(0, 17, 0),
          [ID["mtg_bridge"], ID["report_d1"], ID["kpi_workbook"]])

    # Incident record.
    c.doc(1, "incidents", "INC-incident-record.md", ID["incident"],
          "incident", s.when(di, 9, 0),
          f"Incident Record — {ID['incident']} UPI Autopay mandate failures",
          f"""**Incident ID:** {ID['incident']}  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Autopay  ·  **Commander:** {ops.name}
**Detected:** {s.when(di, 8, 30).strftime('%d %b %Y %H:%M IST')} (morning KPI sweep)
**Declared:** {s.when(di, 8, 55).strftime('%d %b %Y %H:%M IST')}

## Summary
UPI Autopay mandate execution success degraded from ~99.3% to
{k.fmt('Success Rate (%)', di)} beginning ~06:25, driven by intermittent 5xx from
{bank['name']} and callback timeouts via {psp['name']}. Customer Complaints
{k.fmt('Customer Complaints', di)}, Merchant Complaints {k.fmt('Merchant Complaints', di)}.

## Impact
Failed subscription/SIP debits for {', '.join(m['name'] for m in s.affected_merchants)}.
Technical Declines {k.fmt('Technical Declines (%)', di)}; Response Time p95
{k.fmt('Response Time (ms)', di)}.

## Timeline (day 1)
- 06:25 — first elevated failures on Autopay execution.
- 08:30 — anomaly flagged by KPI sweep ({ID['report_d1']}).
- 09:30 — incident bridge {ID['mtg_bridge']}; Sev-2 confirmed.

Root cause under investigation — see {ID['rca']}. Permanent fix tracked as
{ID['decision']}.""",
          [ID["rca"], ID["mtg_bridge"], ID["decision"], ID["report_d1"]])


# ===========================================================================
# Day 2 (Tuesday) — investigation, complaints, RCA draft.
# ===========================================================================
def build_day2(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 1
    ID = s.ID
    bank, psp = s.bank, s.psp
    analytics = org.lead("Product Analytics")
    autopay = org.lead("UPI Autopay")
    psp_lead = org.lead("PSP Integration")
    cx = org.lead("Customer Experience")
    merch = org.lead("Merchant Products")
    risk = org.lead("Risk & Compliance")

    # Merchant complaint escalation email thread.
    c.doc(2, "outlook", "EMAIL-D02-003-merchant-escalation.md", "EMAIL-D02-003",
          "email", s.when(di, 10, 15),
          "Merchant escalations — failed subscription debits",
          f"""**From:** {merch.name} <{merch.email}>
**To:** upi-autopay@npci-demo.in; upi-leadership@npci-demo.in
**Cc:** {cx.name}, {analytics.name}
**Sent:** {s.when(di, 10, 15).strftime('%a %d %b %Y, %H:%M IST')}
**Subject:** [Escalation] {ID['incident']} — merchants reporting mandate failures

Merchant Success has taken formal escalations from
{', '.join(m['name'] for m in s.affected_merchants)}. Their SIP and subscription
collections that route through {psp['name']} are failing on the {bank['name']}
debit leg. Merchant Complaints for the day are {k.fmt('Merchant Complaints', di)},
up sharply from Monday.

We told them the incident bridge ({ID['mtg_bridge']}) is active and the RCA
({ID['rca']}) lands today. Please keep the fix ETA visible — WealthGrow's SIP run
is tomorrow morning.

{sign_off(merch)}""",
          [ID["incident"], ID["mtg_bridge"], ID["rca"]])

    # Customer Experience Teams thread.
    c.doc(2, "teams", "TEAMS-D02-customer-experience.md", "TEAMS-D02-CX",
          "teams", s.when(di, 11, 0),
          "Teams — UPI Products / Customer Experience",
          f"""**Channel:** UPI Products / Customer Experience
**Date:** {s.dates[di].strftime('%A %d %b %Y')}

**{cx.name}** · 11:00
Complaint queue for {ID['incident']} is heavy — Customer Complaints at
{k.fmt('Customer Complaints', di)} today, mostly "autopay failed / double
attempt". Canned response drafted and linked in {ID['report_d2']}.

**{analytics.name}** · 11:12
Confirmed the complaints correlate 1:1 with the {bank['name']} 5xx windows.
Technical Declines {k.fmt('Technical Declines (%)', di)} — the worst point of
the week so far. Feeding this into {ID['rca']}.

**{psp_lead.name}** · 11:26
{psp['name']} raised their callback timeout at 10:40; early signal is the failure
rate is stabilising, not yet recovering. Full correlation pack for {ID['mtg_invest']}
this afternoon.""",
          [ID["incident"], ID["rca"], ID["report_d2"], ID["mtg_invest"]])

    # Investigation meeting.
    c.doc(2, "meetings", "MTG-D02-investigation.md", ID["mtg_invest"],
          "meeting", s.when(di, 15, 0),
          "Investigation Review — UPI Autopay failures",
          f"""**Meeting ID:** {ID['mtg_invest']}  ·  **Type:** Investigation Review
**Room:** Kaveri  ·  **Start:** {s.when(di, 15, 0).strftime('%d %b %Y %H:%M IST')}
**Incident:** {ID['incident']}  ·  **Recording:** rec/{ID['mtg_invest'].lower()}.mp4 (00:33:50)

## Attendees
{chr(10).join('- ' + org.named(p) for p in (autopay, psp_lead, analytics, cx, risk))}

## Discussion
- {psp_lead.name.split()[0]}: {psp['name']}/{bank['name']} failure correlation is 0.94
  over the incident window (TASK-0001 complete). Every failure cluster maps to a
  {bank['name']} 5xx burst; {psp['name']} callback timeouts were a secondary
  amplifier now mitigated.
- {analytics.name.split()[0]}: today's KPIs — {kline(k, 'Success Rate (%)', di)},
  {kline(k, 'Technical Declines (%)', di)}, {kline(k, 'Customer Complaints', di)}.
  This is the bottom of the dip.
- {risk.name.split()[0]}: Risk Score {k.fmt('Risk Score', di)}; no fraud signal —
  Fraud Alerts {k.fmt('Fraud Alerts', di)} are within noise. This is availability,
  not abuse.

## Decisions
- Confirm the working root cause for {ID['rca']}: absent bank-failover in the
  Autopay retry path defined by {ID['sop']}.
- Bring a permanent fix proposal ({ID['decision']}) to the RCA review tomorrow.

## Action items
- [ ] {autopay.name}: finalise {ID['rca']} draft tonight — due Tue 18:00 (TASK-0002)
- [ ] {psp_lead.name}: propose failover design for {ID['brd']} — due Wed 10:00 (TASK-0004)""",
          [ID["incident"], ID["rca"], ID["decision"], ID["sop"], ID["brd"]])

    # RCA draft (v0.9).
    c.doc(2, "incidents", "RCA-draft.md", ID["rca"], "rca", s.when(di, 18, 0),
          f"Root Cause Analysis (DRAFT v0.9) — {ID['rca']}",
          f"""**RCA ID:** {ID['rca']}  ·  **Status:** Draft v0.9  ·  **Incident:** {ID['incident']}
**Product:** UPI Autopay  ·  **Author:** {autopay.name}  ·  **Severity:** Sev-2
**Incident window:** {s.dates[0].strftime('%d %b')} 06:25 — {s.dates[1].strftime('%d %b')} (recovering)

## Detection
Flagged by the automated morning KPI sweep on {s.dates[0].strftime('%d %b')}
(see {ID['report_d1']}); Success Rate had fallen to {k.fmt('Success Rate (%)', 0)}.

## Timeline
- {s.dates[0].strftime('%d %b')} 06:25 — Autopay execution failures begin.
- {s.dates[0].strftime('%d %b')} 09:30 — incident bridge {ID['mtg_bridge']}, Sev-2.
- {s.dates[1].strftime('%d %b')} 10:40 — {psp['name']} callback timeout raised (mitigation).
- {s.dates[1].strftime('%d %b')} 15:00 — investigation review {ID['mtg_invest']}, root cause confirmed.

## Impact
- Success Rate low of {k.fmt('Success Rate (%)', 1)}; Technical Declines peak
  {k.fmt('Technical Declines (%)', 1)}; Settlement Success {k.fmt('Settlement Success (%)', 1)}.
- Customer Complaints {k.fmt('Customer Complaints', 1)}, Merchant Complaints
  {k.fmt('Merchant Complaints', 1)} at peak.
- Affected merchants: {', '.join(m['name'] for m in s.affected_merchants)}.

## Root cause (preliminary)
A {bank['name']} maintenance window produced intermittent 5xx on the debit leg
during peak. The Autopay retry logic in {ID['sop']} retried against the *same*
bank endpoint with no failover to an alternate rail, so transient bank
unavailability converted directly into mandate failures. {psp['name']} callback
timeouts amplified the effect until raised.

## Corrective actions (proposed)
- {ID['decision']}: introduce bank-failover + circuit-breaker in the Autopay
  retry path; specified in {ID['brd']} / {ID['prd']}.
- Update {ID['sop']} to v3.1 with the failover procedure.

Final RCA to be signed off at {ID['mtg_rca']}.""",
          [ID["incident"], ID["mtg_bridge"], ID["mtg_invest"], ID["decision"],
           ID["sop"], ID["brd"], ID["report_d1"]])

    _daily_report(c, org, k, s, di, extra_refs=[ID["mtg_invest"], ID["rca"]],
                  headline=f"Dip bottoms out ({kline(k, 'Success Rate (%)', di, False)}); "
                           f"root cause confirmed as missing bank-failover in {ID['sop']}.")

    _task(c, org, s, di, "TASK-0004", f"Propose Autopay failover design for {ID['brd']}",
          org.lead("PSP Integration"), org.lead("UPI Autopay"), 1, "in_progress",
          s.when(2, 10, 0), [ID["mtg_invest"], ID["brd"], ID["decision"]])


# ===========================================================================
# Day 3 (Wednesday) — root cause confirmed, decision proposed.
# ===========================================================================
def build_day3(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 2
    ID = s.ID
    bank, psp = s.bank, s.psp
    autopay = org.lead("UPI Autopay")
    psp_lead = org.lead("PSP Integration")
    strategy = org.lead("Product Strategy")
    analytics = org.lead("Product Analytics")
    ops = org.lead("Product Operations")
    risk = org.lead("Risk & Compliance")
    cpo = org.exec_team[0]
    svp = org.exec_team[1]

    # RCA review meeting — sign-off.
    c.doc(3, "meetings", "MTG-D03-rca-review.md", ID["mtg_rca"], "meeting",
          s.when(di, 11, 0), "RCA Review & Sign-off — UPI Autopay",
          f"""**Meeting ID:** {ID['mtg_rca']}  ·  **Type:** RCA Review
**Room:** Godavari  ·  **Start:** {s.when(di, 11, 0).strftime('%d %b %Y %H:%M IST')}
**Incident:** {ID['incident']}  ·  **Recording:** rec/{ID['mtg_rca'].lower()}.mp4 (00:38:20)

## Attendees
{chr(10).join('- ' + org.named(p) for p in (svp, autopay, psp_lead, analytics, ops, risk))}

## Discussion
- {autopay.name.split()[0]} walked through {ID['rca']}: confirmed root cause is the
  missing bank-failover in the Autopay retry path of {ID['sop']}, triggered by the
  {bank['name']} maintenance-window 5xx and amplified by {psp['name']} callback
  timeouts.
- Today's KPIs show early stabilisation: {kline(k, 'Success Rate (%)', di)},
  {kline(k, 'Technical Declines (%)', di)}, {kline(k, 'Customer Complaints', di)}.
- {svp.name.split()[0]} signed off {ID['rca']} as final.

## Decisions
- **{ID['decision']} proposed:** implement Autopay bank-failover + circuit-breaker,
  per {ID['brd']} and {ID['prd']}, and revise {ID['sop']} to v3.1. Owner:
  {autopay.name}. Target rollout: Thursday, with executed verification Friday.
- {ID['decision']} to be tabled for approval at the Change Advisory review
  {ID['mtg_cab']} tomorrow morning.

## Action items
- [ ] {autopay.name}: raise {ID['decision']} for CAB approval — due Thu 09:00 (TASK-0005)
- [ ] {psp_lead.name}: prepare rollout runbook referencing {ID['sop']} v3.1 — due Thu 09:00 (TASK-0006)""",
          [ID["incident"], ID["rca"], ID["decision"], ID["brd"], ID["prd"],
           ID["sop"], ID["mtg_cab"]])

    # BRD.
    c.doc(3, "docs", "BRD-autopay-failover.md", ID["brd"], "product_document",
          s.when(di, 13, 0), f"Business Requirements Document — {ID['brd']}",
          f"""**Document:** {ID['brd']}  ·  **Status:** Approved for build
**Product:** UPI Autopay  ·  **Author:** {strategy.name}  ·  **Sponsor:** {org.exec_team[1].name}

## Background
{ID['rca']} identified that Autopay mandate execution has no failover when a
sponsor bank ({bank['name']} in {ID['incident']}) returns transient 5xx. The
retry logic in {ID['sop']} loops on the same endpoint, converting a bank blip
into customer-visible mandate failures.

## Business objective
Sustain Autopay Success Rate at or above 99.2% through single-bank
unavailability, protecting subscription/SIP collections for merchants such as
{', '.join(m['name'] for m in s.affected_merchants[:3])}.

## Requirements
1. Detect repeated 5xx / timeout from a sponsor bank within a rolling window and
   open a circuit-breaker for that endpoint.
2. Fail Autopay execution over to an alternate available rail rather than
   re-hitting the impaired bank.
3. Cap PSP callback wait and treat a timeout as a retriable, not terminal, state.
4. Emit failover events to Product Analytics for the daily KPI workbook
   ({ID['kpi_workbook']}).

## Success metric
Autopay Success Rate >= 99.2% sustained; Technical Declines back under 0.6%.
Detailed design in {ID['prd']}; procedure change in {ID['sop']} v3.1.""",
          [ID["rca"], ID["decision"], ID["prd"], ID["sop"], ID["kpi_workbook"]])

    # PRD.
    c.doc(3, "docs", "PRD-resilient-mandate-execution.md", ID["prd"],
          "product_document", s.when(di, 14, 30),
          f"Product Requirements Document — {ID['prd']}",
          f"""**Document:** {ID['prd']}  ·  **Status:** In build
**Product:** UPI Autopay  ·  **Author:** {autopay.name}  ·  **Linked BRD:** {ID['brd']}

## Overview
Resilient mandate execution for UPI Autopay: a circuit-breaker per sponsor-bank
endpoint plus failover to an alternate rail, addressing {ID['rca']} /
{ID['incident']}.

## Functional design
- **Health tracking:** per-bank rolling error-rate and latency, sourced from the
  same telemetry that feeds {ID['kpi_workbook']}.
- **Circuit-breaker:** open at >5% 5xx or p95 > 1500 ms over 2 minutes; half-open
  probe every 60 s.
- **Failover:** when open, route the mandate execution to an alternate rail; if
  none is available, defer and auto-reattempt within the mandate window.
- **PSP callbacks:** bounded wait (per {ID['sop']} v3.1); timeout is retriable.

## Rollout
Feature-flagged, staged 10% → 50% → 100% on Thursday under {ID['decision']},
following the runbook in {ID['sop']} v3.1. Verification of recovery on Friday via
{ID['report_d5']}.

## Non-goals
No change to P2P / collect on UPI Core; scope is Autopay execution only.""",
          [ID["rca"], ID["incident"], ID["decision"], ID["sop"], ID["brd"],
           ID["kpi_workbook"], ID["report_d5"]])

    # Decision record — proposed.
    c.doc(3, "decisions", "DEC-autopay-failover.md", ID["decision"], "decision",
          s.when(di, 16, 0),
          f"Decision Record — {ID['decision']} Autopay Bank-Failover",
          f"""**Decision ID:** {ID['decision']}  ·  **Status:** Proposed
**Product:** UPI Autopay  ·  **Owner:** {autopay.name}  ·  **Sponsor:** {org.exec_team[1].name}
**Proposed:** {s.when(di, 16, 0).strftime('%d %b %Y %H:%M IST')}

## Context
Arising from {ID['incident']} and confirmed by {ID['rca']}: Autopay lacks
bank-failover, so a {bank['name']} maintenance blip caused mandate failures and a
Success Rate low of {k.fmt('Success Rate (%)', 1)} on Tuesday.

## Decision
Build and roll out Autopay bank-failover + circuit-breaker per {ID['brd']} /
{ID['prd']}, and adopt {ID['sop']} v3.1. Staged rollout Thursday; executed
verification Friday.

## Lifecycle
- Proposed — {s.dates[2].strftime('%d %b %Y')} (this record, at {ID['mtg_rca']}).
- Approval sought at {ID['mtg_cab']} (Thursday).

## Expected impact
Autopay Success Rate restored to >= 99.2%; Technical Declines < 0.6%; complaint
volumes normalised. Tracked in {ID['kpi_workbook']} and the {ID['report_exec']}.""",
          [ID["incident"], ID["rca"], ID["brd"], ID["prd"], ID["sop"],
           ID["mtg_cab"], ID["kpi_workbook"]])

    _daily_report(c, org, k, s, di, extra_refs=[ID["mtg_rca"], ID["decision"]],
                  headline=f"RCA signed off; {ID['decision']} proposed — Autopay "
                           f"bank-failover, rollout targeted for Thursday.")

    _task(c, org, s, di, "TASK-0005", f"Raise {ID['decision']} for CAB approval",
          org.lead("UPI Autopay"), org.exec_team[1], 1, "in_progress",
          s.when(3, 9, 0), [ID["mtg_rca"], ID["decision"], ID["mtg_cab"]])
    _task(c, org, s, di, "TASK-0006", "Prepare rollout runbook for SOP v3.1",
          org.lead("PSP Integration"), org.lead("UPI Autopay"), 2, "in_progress",
          s.when(3, 9, 0), [ID["mtg_rca"], ID["sop"], ID["decision"]])


# ===========================================================================
# Day 4 (Thursday) — SOP updated, rollout.
# ===========================================================================
def build_day4(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 3
    ID = s.ID
    autopay = org.lead("UPI Autopay")
    psp_lead = org.lead("PSP Integration")
    ops = org.lead("Product Operations")
    core = org.lead("UPI Core")
    risk = org.lead("Risk & Compliance")
    svp = org.exec_team[1]

    # Change Advisory Board meeting — approval.
    c.doc(4, "meetings", "MTG-D04-change-advisory.md", ID["mtg_cab"], "meeting",
          s.when(di, 9, 30), "Change Advisory Board — Autopay failover rollout",
          f"""**Meeting ID:** {ID['mtg_cab']}  ·  **Type:** Change Advisory Board
**Room:** Ganga  ·  **Start:** {s.when(di, 9, 30).strftime('%d %b %Y %H:%M IST')}
**Change:** {ID['decision']}  ·  **Recording:** rec/{ID['mtg_cab'].lower()}.mp4 (00:27:05)

## Attendees
{chr(10).join('- ' + org.named(p) for p in (svp, ops, autopay, psp_lead, core, risk))}

## Discussion
- {autopay.name.split()[0]} presented {ID['decision']} with {ID['prd']} and the runbook
  under {ID['sop']} v3.1. Rollback is a single flag flip.
- {risk.name.split()[0]} confirmed no compliance blockers; the change is availability
  hardening, logged under {ID['incident']}.
- KPIs already recovering: {kline(k, 'Success Rate (%)', di)},
  {kline(k, 'Technical Declines (%)', di)}.

## Decisions
- **{ID['decision']} APPROVED** for staged rollout today (10% → 50% → 100%). Owner
  {autopay.name}. Verification of full recovery Friday via {ID['report_d5']}.
- {ID['sop']} v3.1 adopted as the operative procedure on approval.

## Action items
- [ ] {autopay.name}: execute staged rollout of {ID['decision']} — due Thu 18:00 (TASK-0007)
- [ ] {ops.name}: monitor KPIs post-rollout for {ID['report_d4']} — due Thu 20:00 (TASK-0008)""",
          [ID["decision"], ID["prd"], ID["sop"], ID["incident"], ID["report_d5"],
           ID["report_d4"]])

    # SOP v3.1 (updated) and a v3.0 (prior) so version history exists.
    c.doc(4, "docs", "SOP-UPI-AUTOPAY-014-v3.1.md", ID["sop"], "sop",
          s.when(di, 10, 30),
          f"{ID['sop']} — UPI Autopay Mandate Execution (v3.1)",
          f"""**SOP ID:** {ID['sop']}  ·  **Version:** 3.1  ·  **Status:** Active
**Product:** UPI Autopay  ·  **Owner:** {autopay.name}
**Approved:** {s.when(di, 10, 0).strftime('%d %b %Y')} at {ID['mtg_cab']}
**Supersedes:** v3.0 ({s.dates[0].strftime('%B %Y')})

## Purpose
Standard procedure for executing UPI Autopay e-mandate debits, including the
bank-failover behaviour added after {ID['rca']} / {ID['incident']}.

## Procedure
1. Resolve the mandate and select the sponsor bank rail.
2. **(New in v3.1)** Check the sponsor-bank circuit-breaker. If open, fail over
   to an alternate available rail; if none, defer and reattempt within the
   mandate window. Per {ID['prd']}.
3. Execute the debit; bound the PSP callback wait and treat a timeout as
   retriable (not a terminal failure).
4. On repeated 5xx/timeout from a bank, open the circuit-breaker and emit a
   failover event to Product Analytics for {ID['kpi_workbook']}.
5. Reconcile executed mandates against the settlement file (unchanged from v3.0).

## Version history
| Version | Date | Change | Approved at |
|---------|------|--------|-------------|
| 3.0 | {s.dates[0].strftime('%d %b %Y')} | Baseline mandate execution (no failover) | prior CAB |
| 3.1 | {s.dates[3].strftime('%d %b %Y')} | Add bank-failover + circuit-breaker | {ID['mtg_cab']} |

## Linked
Decision {ID['decision']}; RCA {ID['rca']}; design {ID['prd']}; training deck
"Autopay Failover — {s.dates[3].strftime('%b %Y')}" to be issued to on-call.""",
          [ID["rca"], ID["incident"], ID["decision"], ID["prd"],
           ID["mtg_cab"], ID["kpi_workbook"]])

    _daily_report(c, org, k, s, di, extra_refs=[ID["mtg_cab"], ID["sop"]],
                  headline=f"{ID['decision']} approved and rolled out; {ID['sop']} "
                           f"v3.1 active; Success Rate recovering to {k.fmt('Success Rate (%)', di)}.")

    _task(c, org, s, di, "TASK-0007", f"Execute staged rollout of {ID['decision']}",
          org.lead("UPI Autopay"), org.exec_team[1], 1, "done",
          s.when(3, 18, 0), [ID["mtg_cab"], ID["decision"], ID["sop"]])
    _task(c, org, s, di, "TASK-0008", "Monitor KPIs post-rollout",
          org.lead("Product Operations"), org.lead("UPI Autopay"), 2, "done",
          s.when(3, 20, 0), [ID["mtg_cab"], ID["report_d4"], ID["kpi_workbook"]])


# ===========================================================================
# Day 5 (Friday) — KPI recovery, decision executed.
# ===========================================================================
def build_day5(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 4
    ID = s.ID
    autopay = org.lead("UPI Autopay")
    analytics = org.lead("Product Analytics")
    ops = org.lead("Product Operations")
    cpo = org.exec_team[0]

    # Recovery confirmation email.
    c.doc(5, "outlook", "EMAIL-D05-004-recovery-confirmed.md", "EMAIL-D05-004",
          "email", s.when(di, 12, 0),
          "Autopay recovered — closing the loop on the incident",
          f"""**From:** {analytics.name} <{analytics.email}>
**To:** upi-leadership@npci-demo.in; upi-autopay@npci-demo.in
**Cc:** upi-incident-bridge@npci-demo.in
**Sent:** {s.when(di, 12, 0).strftime('%a %d %b %Y, %H:%M IST')}
**Subject:** RE: {ID['incident']} — Autopay recovered, {ID['decision']} executed

Good news. With {ID['decision']} at 100% and {ID['sop']} v3.1 live, Autopay has
recovered: {kline(k, 'Success Rate (%)', di)}, {kline(k, 'Technical Declines (%)', di)},
and {kline(k, 'Settlement Success (%)', di)}. Customer Complaints down to
{k.fmt('Customer Complaints', di)} and Merchant Complaints to
{k.fmt('Merchant Complaints', di)}. Autopay Registrations back to
{k.fmt('Autopay Registrations (K/day)', di)}K.

Proposing we mark {ID['incident']} resolved and move to monitoring over the
weekend. Full numbers in {ID['report_d5']} and the weekend review {ID['mtg_weekly']}.

{sign_off(analytics)}""",
          [ID["incident"], ID["decision"], ID["sop"], ID["report_d5"],
           ID["mtg_weekly"]])

    # Decision executed — update the decision-lifecycle by a linked record.
    c.doc(5, "decisions", "DEC-autopay-failover-executed.md",
          "DEC-EXEC-CONFIRM", "decision", s.when(di, 15, 0),
          f"Decision Execution Confirmation — {ID['decision']}",
          f"""**Confirms:** {ID['decision']}  ·  **Status:** Executed / Closed
**Product:** UPI Autopay  ·  **Owner:** {autopay.name}
**Executed:** {s.when(di, 15, 0).strftime('%d %b %Y %H:%M IST')}

## Outcome
{ID['decision']} (Autopay bank-failover + circuit-breaker) reached 100% rollout on
Thursday under {ID['sop']} v3.1 and is confirmed effective:
- Success Rate {k.fmt('Success Rate (%)', di)} (target >= 99.2% met).
- Technical Declines {k.fmt('Technical Declines (%)', di)} (target < 0.6% met).
- Settlement Success {k.fmt('Settlement Success (%)', di)}.

## Verification
KPIs sourced from {ID['kpi_workbook']} and reported in {ID['report_d5']}.
{ID['incident']} moved to Resolved. Post-incident monitoring continues over the
weekend ({ID['mtg_weekly']}); durability confirmed in the {ID['report_exec']}.

## Lifecycle
Proposed ({s.dates[2].strftime('%d %b')}) → Approved ({s.dates[3].strftime('%d %b')}, {ID['mtg_cab']})
→ Executed ({s.dates[4].strftime('%d %b')}) → Closed.""",
          [ID["decision"], ID["sop"], ID["incident"], ID["kpi_workbook"],
           ID["report_d5"], ID["mtg_weekly"], ID["report_exec"]])

    _daily_report(c, org, k, s, di, extra_refs=[ID["decision"], "EMAIL-D05-004"],
                  headline=f"Recovery confirmed: {kline(k, 'Success Rate (%)', di, False)}; "
                           f"{ID['decision']} executed and {ID['incident']} resolved.")

    _task(c, org, s, di, "TASK-0009", f"Confirm {ID['incident']} resolution & close",
          org.lead("Product Operations"), org.lead("UPI Autopay"), 2, "done",
          s.when(4, 16, 0), [ID["incident"], ID["decision"], ID["report_d5"]])


# ===========================================================================
# Day 6 (Saturday) — monitoring and weekly review.
# ===========================================================================
def build_day6(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 5
    ID = s.ID
    ops = org.lead("Product Operations")
    analytics = org.lead("Product Analytics")
    autopay = org.lead("UPI Autopay")
    risk = org.lead("Risk & Compliance")
    merch = org.lead("Merchant Products")
    svp = org.exec_team[1]

    # Weekend monitoring Teams thread.
    c.doc(6, "teams", "TEAMS-D06-monitoring.md", "TEAMS-D06-MON", "teams",
          s.when(di, 10, 0), "Teams — UPI Products / Incident Bridge (monitoring)",
          f"""**Channel:** UPI Products / Incident Bridge
**Date:** {s.dates[di].strftime('%A %d %b %Y')}

**{ops.name}** · 10:00
Weekend monitoring on {ID['incident']} (now Resolved). Autopay holding:
{kline(k, 'Success Rate (%)', di, False)}, {kline(k, 'Technical Declines (%)', di, False)}.
No failover storms overnight.

**{analytics.name}** · 10:12
Confirmed — {ID['sop']} v3.1 failover fired cleanly twice overnight on brief bank
blips and self-healed. Exactly the {ID['decision']} design intent. Numbers in
{ID['report_d6']}.

**{risk.name}** · 10:20
Risk Score down to {k.fmt('Risk Score', di)}, Fraud Alerts {k.fmt('Fraud Alerts', di)} —
all nominal. Nothing for compliance to action.""",
          [ID["incident"], ID["sop"], ID["decision"], ID["report_d6"]])

    # Weekly review meeting.
    c.doc(6, "meetings", "MTG-D06-weekly-review.md", ID["mtg_weekly"], "meeting",
          s.when(di, 15, 0), "Weekly Operations & Product Review",
          f"""**Meeting ID:** {ID['mtg_weekly']}  ·  **Type:** Weekly Review
**Room:** Virtual Bridge A  ·  **Start:** {s.when(di, 15, 0).strftime('%d %b %Y %H:%M IST')}
**Recording:** rec/{ID['mtg_weekly'].lower()}.mp4 (00:44:30)

## Attendees
{chr(10).join('- ' + org.named(p) for p in (svp, ops, autopay, analytics, risk, merch))}

## Agenda
1. {ID['incident']} closure and week-in-review.
2. KPI trajectory Monday → Saturday.
3. Inputs to the executive summary {ID['report_exec']}.

## Discussion
- Week arc: Success Rate {k.fmt('Success Rate (%)', 0)} (Mon) → low
  {k.fmt('Success Rate (%)', 1)} (Tue) → {k.fmt('Success Rate (%)', di)} (Sat),
  fully recovered after {ID['decision']} / {ID['sop']} v3.1.
- Complaints normalised: Customer {k.fmt('Customer Complaints', di)}, Merchant
  {k.fmt('Merchant Complaints', di)}.
- {merch.name.split()[0]}: affected merchants ({', '.join(m['name'] for m in s.affected_merchants[:3])})
  informed of resolution; feeds the {ID['report_merchant']}.

## Decisions
- Endorse the recommendation to make bank-failover the standard for all recurring
  rails (UPI Credit next), for {ID['report_exec']} sign-off on Sunday.

## Action items
- [ ] {analytics.name}: assemble {ID['report_exec']} and {ID['report_risk']} — due Sun 10:00 (TASK-0010)""",
          [ID["incident"], ID["decision"], ID["sop"], ID["report_exec"],
           ID["report_merchant"], ID["report_risk"]])

    _daily_report(c, org, k, s, di, extra_refs=[ID["mtg_weekly"], ID["decision"]],
                  headline=f"Stable over the weekend; failover self-healing; "
                           f"week-in-review completed at {ID['mtg_weekly']}.")

    _task(c, org, s, di, "TASK-0010", "Assemble weekly executive & risk reports",
          org.lead("Product Analytics"), org.exec_team[1], 1, "in_progress",
          s.when(6, 10, 0), [ID["mtg_weekly"], ID["report_exec"], ID["report_risk"]])

    # Merchant weekly report (Saturday).
    _merchant_report(c, org, k, s, di)


# ===========================================================================
# Day 7 (Sunday) — executive summary and recommendations.
# ===========================================================================
def build_day7(c: Corpus, org: Org, k: KPICatalog, s: Story) -> None:
    di = 6
    ID = s.ID
    cpo = org.exec_team[0]
    svp = org.exec_team[1]
    analytics = org.lead("Product Analytics")
    autopay = org.lead("UPI Autopay")
    risk = org.lead("Risk & Compliance")

    _daily_report(c, org, k, s, di, extra_refs=[ID["report_exec"], ID["decision"]],
                  headline=f"Week closed; Autopay resilient; recommendations issued "
                           f"in {ID['report_exec']}.")

    # Executive weekly report.
    def week_row(kpi: str) -> str:
        vals = " | ".join(k.fmt(kpi, d) for d in range(7))
        return f"| {kpi} | {vals} |"

    kpi_table = "\n".join(week_row(kpi) for kpi in k.names())
    c.doc(7, "reports", "RPT-exec-weekly.md", ID["report_exec"], "report",
          s.when(di, 11, 0),
          "UPI Products — Executive Weekly Summary",
          f"""**Report ID:** {ID['report_exec']}  ·  **Prepared by:** {analytics.name}
**For:** {cpo.name} ({cpo.title}), {svp.name}
**Week:** {s.dates[0].strftime('%d %b')} – {s.dates[6].strftime('%d %b %Y')}
**Source:** {ID['kpi_workbook']} (all figures)

## Executive summary
UPI Autopay experienced a Sev-2 mandate-failure incident ({ID['incident']}) on
Monday, caused by a {s.bank['name']} maintenance-window outage with no
bank-failover in the Autopay retry path ({ID['rca']}). Success Rate fell to a low
of {k.fmt('Success Rate (%)', 1)} on Tuesday. Decision {ID['decision']} (Autopay
bank-failover + circuit-breaker) was proposed Wednesday, approved and rolled out
Thursday under {ID['sop']} v3.1, and executed Friday. The rail fully recovered to
{k.fmt('Success Rate (%)', di)} and held stable across the weekend.

## KPI trajectory (Mon → Sun)
| KPI | {' | '.join(WEEKDAYS)} |
|-----|{'|'.join(['---'] * 7)}|
{kpi_table}

## What worked
- Detection to Sev-2 in under two hours via the automated KPI sweep.
- Root cause confirmed within 48 hours ({ID['rca']}, {ID['mtg_rca']}).
- Fix proposed, approved and executed within the same week ({ID['decision']}).

## Recommendations
1. Adopt bank-failover as the standard for all recurring-debit rails, starting
   with UPI Credit — extend {ID['sop']} family accordingly.
2. Add sponsor-bank maintenance-window awareness to the Autopay scheduler.
3. Institute a weekly resilience KPI in {ID['kpi_workbook']} (failover events,
   circuit-breaker trips).

Risk posture is covered in {ID['report_risk']}; merchant impact in
{ID['report_merchant']}.""",
          [ID["incident"], ID["rca"], ID["decision"], ID["sop"],
           ID["kpi_workbook"], ID["report_risk"], ID["report_merchant"],
           ID["mtg_rca"]])

    # Risk weekly report.
    c.doc(7, "reports", "RPT-risk-weekly.md", ID["report_risk"], "report",
          s.when(di, 11, 30), "UPI Products — Weekly Risk & Compliance Report",
          f"""**Report ID:** {ID['report_risk']}  ·  **Prepared by:** {risk.name}
**Week:** {s.dates[0].strftime('%d %b')} – {s.dates[6].strftime('%d %b %Y')}
**Source:** {ID['kpi_workbook']}

## Availability risk
{ID['incident']} was an availability event, not abuse. Risk Score peaked at
{k.fmt('Risk Score', 1)} on Tuesday and returned to {k.fmt('Risk Score', di)} by
Sunday. Fraud Alerts stayed within noise (peak {k.fmt('Fraud Alerts', 1)}), with
no correlated fraud pattern.

## Controls & compliance
{ID['decision']} was approved through the Change Advisory Board ({ID['mtg_cab']})
with a single-flag rollback; {ID['sop']} v3.1 is the operative procedure. No
regulatory reportable event; customer redress for failed debits handled by
Customer Experience.

## Recommendation
Endorse recommendation 1 of {ID['report_exec']} (failover as standard for
recurring rails) as a resilience control. Residual risk: concentration on
{s.bank['name']} as a sponsor bank — see {ID['rca']}.""",
          [ID["incident"], ID["decision"], ID["sop"], ID["mtg_cab"],
           ID["report_exec"], ID["rca"], ID["kpi_workbook"]])

    # Executive review meeting (Sunday sign-off).
    c.doc(7, "meetings", "MTG-D07-exec-review.md", ID["mtg_exec"], "meeting",
          s.when(di, 16, 0), "Executive Review — Weekly close & recommendations",
          f"""**Meeting ID:** {ID['mtg_exec']}  ·  **Type:** Executive Review
**Room:** Ganga  ·  **Start:** {s.when(di, 16, 0).strftime('%d %b %Y %H:%M IST')}
**Recording:** rec/{ID['mtg_exec'].lower()}.mp4 (00:29:40)

## Attendees
{chr(10).join('- ' + org.named(p) for p in (cpo, svp, analytics, autopay, risk))}

## Discussion
- {analytics.name.split()[0]} presented {ID['report_exec']}: Autopay incident
  ({ID['incident']}) resolved within the week; Success Rate recovered to
  {k.fmt('Success Rate (%)', di)}.
- {cpo.name.split()[0]} approved the three recommendations in {ID['report_exec']}.

## Decisions
- Approve extending bank-failover to UPI Credit next sprint (new BRD to follow).
- Adopt a weekly resilience KPI in {ID['kpi_workbook']} from next week.

## Action items
- [ ] {autopay.name}: open the UPI Credit failover BRD — due next Wed (TASK-0011)""",
          [ID["report_exec"], ID["incident"], ID["decision"],
           ID["kpi_workbook"], ID["report_risk"]])

    _task(c, org, s, di, "TASK-0011", "Open UPI Credit failover BRD (next sprint)",
          org.lead("UPI Autopay"), org.exec_team[0], 3, "todo",
          s.when(6, 18, 0), [ID["mtg_exec"], ID["report_exec"], ID["decision"]])

