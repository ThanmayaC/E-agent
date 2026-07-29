#!/usr/bin/env python
"""Synthetic Enterprise Generator — NPCI UPI Products (V5.1, procedural).

Generates ONE coherent fictional organization — "NPCI (Synthetic
Demonstration)", the UPI Products department — and 35 continuous days of its
*day-to-day operations*. Unlike the earlier scripted version, V5.1 is fully
**procedural and transaction-driven**: nothing is hand-written per week.

How it works
------------
1. ``TransactionEngine`` simulates 35 days of UPI transaction behaviour. Volume
   follows a growth trend modulated by day-of-week, month-end and seeded
   high-volume campaign days. Every bank, PSP and UPI feature carries a health
   profile, and a seeded set of operational *issues* (bank timeout spikes, PSP
   latency, settlement delays, fraud-risk spikes, merchant decline spikes,
   feature degradations) perturbs the relevant entities over multi-day windows.
   Every headline KPI is *derived* from this behaviour, so a dip in Success Rate
   is always explainable by an underlying bank/PSP/feature event — the corpus's
   whole point.

2. ``IssueRegistry`` gives the organization memory. Each issue opens with
   canonical IDs and runs its natural lifecycle across days — detect → incident
   record → bridge → investigate → RCA → decision → SOP update → recovery →
   validation — and is referenced again in later weekly/monthly reviews, so
   "has this happened before" and "how did we fix it last time" have real
   answers.

3. Every day also emits routine operations regardless of incidents: a daily
   operations report (transaction summary, success rate, technical vs business
   declines, top banks/PSPs/merchants, peak hours, failure analysis,
   today/yesterday/last-week/monthly comparisons) and a transaction-monitoring
   note. Non-incident *operational reviews* (adoption reviews, capacity
   planning ahead of high-volume days, SLA reviews) appear on quieter days.
   Weekly reviews land every 7th day; the month closes with an executive/board
   review. No product is ever "launched" — only operated.

Design guarantees (unchanged from before)
------------------------------------------
* **One source of truth for numbers.** Every KPI value lives once in
  ``TransactionEngine``; the workbook, reports, meetings and emails read from
  it, so a figure quoted in an email equals the workbook cell.
* **One roster.** Every person is drawn once from ``Org``.
* **Forward time & continuity.** Every artifact carries a timestamp; issues are
  followed up on subsequent days and referenced by later reviews.
* **No orphans.** Every narrative artifact declares ``Refs:`` to >= 3 others; a
  validation pass fails the build on any dangling reference or under-linked
  artifact.
* **Deterministic.** ``--seed`` fully determines the month; the same seed always
  produces the same organization and the same sequence of operational events.

Usage
-----
    python generate_enterprise.py --days 35 --seed 2026

Produces ``enterprise_data/`` (master/, day_01..day_35/, scenarios/) written as
parser-supported files (.md, .xlsx, .csv) whose folders map onto the platform's
document source kinds, so ``backend/scripts/bootstrap_enterprise_demo.py`` can
register them and the ordinary sync -> document-intelligence -> Brain pipeline
ingests the whole organization unchanged.
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

# Product squads (own products) plus the broader operating functions the spec
# asks the simulation to involve.
TEAMS = [
    # product squads
    "UPI Core", "UPI Autopay", "UPI Lite", "UPI Lite X", "UPI Credit",
    "UPI International", "Merchant Products", "QR Payments",
    # functions
    "Product Management", "Product Strategy", "Product Analytics",
    "Product Operations", "Operations", "Technology", "Engineering",
    "Business", "Merchant Success", "Customer Experience", "Risk & Compliance",
    "Compliance", "PSP Integration", "AI & Innovation",
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

EXEC_TITLES = [
    ("Chief Product Officer", "UPI Products"),
    ("Senior Vice President, UPI Products", "UPI Products"),
    ("Vice President, Product Strategy", "Product Strategy"),
    ("Vice President, Risk & Compliance", "Risk & Compliance"),
    ("Head of Product Operations", "Product Operations"),
]

# Real, in-production UPI capabilities. NOTHING here is ever "launched" — the
# simulation only operates these.
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

# Transaction-carrying UPI features, each tied to the squad that owns it. These
# drive per-feature volume and are what incidents are scoped to.
# Feature volume shares. Calibrated to NPCI's P2P/P2M split (Jun-2026: P2M ~63.5%
# of volume, P2P ~36.5%). Person-to-Person carries the single largest slice;
# merchant-facing features (P2M + QR + Intent + Collect + Lite + Autopay +
# Credit) make up the ~63% remainder.
FEATURES = [
    ("Person to Merchant", "UPI Core", 0.375),
    ("Person to Person", "UPI Core", 0.355),
    ("QR Payments", "QR Payments", 0.095),
    ("Collect Requests", "UPI Core", 0.018),
    ("Intent Payments", "UPI Core", 0.028),
    ("UPI Lite", "UPI Lite", 0.048),
    ("UPI Lite X", "UPI Lite X", 0.010),
    ("UPI Autopay", "UPI Autopay", 0.033),
    ("UPI Credit Line", "UPI Credit", 0.013),
    ("RuPay Credit on UPI", "UPI Credit", 0.011),
    ("UPI International", "UPI International", 0.008),
]

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

# 15 banks spanning tiers and regions (spec coverage).
BANK_POOL = [
    "State Bank of India", "HDFC Bank", "ICICI Bank", "Axis Bank",
    "Punjab National Bank", "Canara Bank", "Union Bank of India",
    "Bank of Baroda", "Indian Bank", "IDFC First Bank", "Kotak Mahindra Bank",
    "Yes Bank", "IndusInd Bank", "AU Small Finance Bank", "Federal Bank",
]

# Third-party apps and bank apps that participate as PSPs.
PSP_POOL = [
    "PhonePe", "Google Pay", "Paytm", "BHIM", "Amazon Pay", "CRED",
    "WhatsApp Pay", "Navi", "FamApp", "SuperMoney",
    "Axis Mobile", "YONO SBI", "iMobile Pay", "HDFC MobileBanking",
]

# ---------------------------------------------------------------------------
# Real relative market share (source: NPCI UPI Ecosystem Statistics, Jun-2026).
# These are *relative volume weights* — the transaction engine normalises them,
# so only their proportions matter. They replace the earlier random-uniform
# weights so that rankings and market_share_pct match the real UPI ecosystem
# (PhonePe/Google Pay/Paytm dominance among apps; SBI-led remitter banks). Any
# entity absent from a table falls back to a small default, so the generator
# still works unchanged if the pools are swapped for a different dataset.
# UPI APPS by "Payer App" volume, Jun-2026 (share of 22,716 Mn monthly txns).
REAL_PSP_SHARE = {
    "PhonePe": 0.462, "Google Pay": 0.326, "Paytm": 0.079, "Navi": 0.037,
    "SuperMoney": 0.019, "BHIM": 0.010, "FamApp": 0.0086, "WhatsApp Pay": 0.0066,
    "CRED": 0.0062, "Axis Mobile": 0.006, "YONO SBI": 0.008, "iMobile Pay": 0.005,
    "HDFC MobileBanking": 0.005, "Amazon Pay": 0.004,
}
# Remitter/beneficiary banks by UPI volume, Jun-2026 (real banks only; the
# PhonePe/Paytm sponsor-bank routing pseudo-entries on NPCI's table are excluded
# so weights reflect the customer's own bank). SBI leads by a wide margin.
REAL_BANK_SHARE = {
    "State Bank of India": 0.26, "HDFC Bank": 0.090, "Bank of Baroda": 0.065,
    "Union Bank of India": 0.055, "ICICI Bank": 0.050, "Axis Bank": 0.050,
    "Punjab National Bank": 0.048, "Canara Bank": 0.042, "Yes Bank": 0.030,
    "Kotak Mahindra Bank": 0.028, "Indian Bank": 0.026, "IDFC First Bank": 0.022,
    "Federal Bank": 0.020, "IndusInd Bank": 0.018, "AU Small Finance Bank": 0.012,
}

# ---------------------------------------------------------------------------
# V7.0 ecosystem: geography, devices, channels, payment types, tickets and the
# failure taxonomy the sampled transaction ledger draws from.
# ---------------------------------------------------------------------------
# (city, state, relative weight). Weights are synthetic, not production shares.
CITIES = [
    ("Mumbai", "Maharashtra", 3.1), ("Delhi", "Delhi", 3.0),
    ("Bengaluru", "Karnataka", 2.8), ("Hyderabad", "Telangana", 2.2),
    ("Chennai", "Tamil Nadu", 2.0), ("Pune", "Maharashtra", 1.7),
    ("Kolkata", "West Bengal", 1.7), ("Ahmedabad", "Gujarat", 1.5),
    ("Surat", "Gujarat", 1.1), ("Jaipur", "Rajasthan", 1.1),
    ("Lucknow", "Uttar Pradesh", 1.0), ("Kanpur", "Uttar Pradesh", 0.8),
    ("Nagpur", "Maharashtra", 0.8), ("Indore", "Madhya Pradesh", 0.9),
    ("Bhopal", "Madhya Pradesh", 0.7), ("Patna", "Bihar", 0.8),
    ("Chandigarh", "Chandigarh", 0.7), ("Kochi", "Kerala", 0.9),
    ("Coimbatore", "Tamil Nadu", 0.8), ("Visakhapatnam", "Andhra Pradesh", 0.8),
    ("Guwahati", "Assam", 0.6), ("Bhubaneswar", "Odisha", 0.6),
    ("Ludhiana", "Punjab", 0.7), ("Vadodara", "Gujarat", 0.7),
    ("Gurugram", "Haryana", 1.0),
]

DEVICE_TYPES = [("Android", 0.78), ("iOS", 0.20), ("KaiOS/Feature", 0.02)]
CHANNELS = [("Mobile App", 0.86), ("Web/Collect", 0.07), ("USSD/*99#", 0.02),
            ("PoS/Soundbox", 0.05)]

# payment type each feature carries
PAYMENT_TYPE_BY_FEATURE = {
    "Person to Merchant": "P2M", "Person to Person": "P2P",
    "QR Payments": "P2M-QR", "Collect Requests": "Collect",
    "Intent Payments": "Intent", "UPI Lite": "P2M-Lite",
    "UPI Lite X": "P2M-LiteX-Offline", "UPI Autopay": "Mandate-Execution",
    "UPI Credit Line": "CreditLine", "RuPay Credit on UPI": "RuPayCredit",
    "UPI International": "Cross-Border",
}
# Average ticket size (INR) per feature. Anchored to NPCI Jun-2026 averages:
# P2P ~ Rs 2,450, all-P2M ~ Rs 600, blended ~ Rs 1,270 across the mix above.
FEATURE_TICKET = {
    "Person to Merchant": 600, "Person to Person": 2450, "QR Payments": 400,
    "Collect Requests": 2200, "Intent Payments": 700, "UPI Lite": 95,
    "UPI Lite X": 120, "UPI Autopay": 1450, "UPI Credit Line": 3100,
    "RuPay Credit on UPI": 2650, "UPI International": 5400,
}
# technical declines (rail/bank/PSP faults) and business declines (customer/limit)
TECH_FAIL_REASONS = [
    ("Beneficiary bank timeout", "U30"), ("Remitter bank unavailable", "U16"),
    ("PSP callback timeout", "U69"), ("NPCI switch 5xx", "U88"),
    ("Response not received", "RB"), ("Deemed approved reversal", "U67"),
]
BIZ_FAIL_REASONS = [
    ("Insufficient funds", "U51"), ("Per-txn limit exceeded", "U66"),
    ("Invalid MPIN", "ZM"), ("Risk hold / suspected fraud", "U28"),
    ("Mandate not registered", "UM"), ("Account frozen", "U54"),
]
PENDING_REASON = ("Awaiting beneficiary confirmation", "BT")

DISTRIBUTION_LISTS = [
    ("upi-leadership@npci-demo.in", "UPI Products leadership"),
    ("upi-core-team@npci-demo.in", "UPI Core engineering and product"),
    ("upi-autopay@npci-demo.in", "UPI Autopay product and ops"),
    ("upi-incident-bridge@npci-demo.in", "Live incident bridge distribution"),
    ("upi-risk-compliance@npci-demo.in", "Risk & Compliance"),
    ("upi-merchant-success@npci-demo.in", "Merchant Products & Success"),
    ("upi-psp-integration@npci-demo.in", "PSP Integration partners"),
    ("upi-analytics@npci-demo.in", "Product Analytics"),
    ("upi-operations@npci-demo.in", "Product Operations & Operations"),
    ("upi-all@npci-demo.in", "All UPI Products staff"),
]
TEAMS_CHANNELS = [
    ("UPI Products", "General", "Department-wide announcements"),
    ("UPI Products", "Ops Monitoring", "Daily transaction monitoring"),
    ("UPI Products", "Incident Bridge", "Live incident coordination"),
    ("UPI Products", "Autopay", "UPI Autopay squad"),
    ("UPI Products", "Core Engineering", "UPI Core engineering"),
    ("UPI Products", "PSP Integration", "PSP partner integration"),
    ("UPI Products", "Bank Coordination", "Bank coordination and reviews"),
    ("UPI Products", "Risk and Compliance", "Risk, fraud and compliance"),
    ("UPI Products", "Merchant Success", "Merchant onboarding and support"),
    ("UPI Products", "Customer Experience", "Support and complaints"),
    ("UPI Products", "Leadership", "Leadership discussion"),
    ("UPI Products", "Analytics", "Product analytics and dashboards"),
]
MEETING_ROOMS = [
    ("Ganga", "Mumbai HQ", 12), ("Yamuna", "Mumbai HQ", 8),
    ("Kaveri", "Hyderabad Tech Centre", 10),
    ("Godavari", "Bengaluru Innovation Hub", 14),
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
    customers: list[dict] = field(default_factory=list)
    exec_team: list[Person] = field(default_factory=list)
    product_team: dict[str, str] = field(default_factory=dict)  # product -> team

    def build(self) -> None:
        used_names: set[str] = set()

        def fresh_name() -> str:
            for _ in range(400):
                nm = (f"{self.rng.choice(FIRST_NAMES)} "
                      f"{self.rng.choice(LAST_NAMES)}")
                if nm not in used_names:
                    used_names.add(nm)
                    return nm
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

        for title, team in EXEC_TITLES:
            self.exec_team.append(add(title, team))
        cpo = self.exec_team[0]

        team_lead: dict[str, Person] = {}
        for team in TEAMS:
            lead = add(f"{team} Lead", team)
            lead.manager = cpo.emp_id
            team_lead[team] = lead
            for role in ("Senior Product Manager", "Product Manager",
                         "Engineering Manager", "Analyst"):
                if self.rng.random() < 0.55:
                    m = add(f"{role}, {team}", team)
                    m.manager = lead.emp_id

        for name, team, desc in PRODUCTS:
            owner = team_lead.get(team, cpo)
            self.product_team[name] = team
            self.products.append({
                "product_id": f"PRD-{name.replace(' ', '').upper()[:8]}",
                "name": name, "team": team, "owner": owner.emp_id,
                "owner_name": owner.name, "description": desc,
            })

        for i, bank in enumerate(BANK_POOL, start=1):
            # First eight are the large public/private banks (Tier 1).
            tier = "Tier 1" if i <= 8 else self.rng.choice(["Tier 2", "Tier 2",
                                                            "Tier 3"])
            self.banks.append({
                "bank_id": f"BANK-{i:03d}", "name": bank,
                "ifsc_prefix": bank.split()[0][:4].upper(),
                "region": self.rng.choice(REGIONS), "tier": tier,
                # Real relative share of total UPI volume this bank carries
                # (NPCI Jun-2026). Scaled x100 for readable weights; a small
                # jitter keeps ties apart without disturbing the ranking. Unknown
                # banks fall back to a modest long-tail weight.
                "weight": round(REAL_BANK_SHARE.get(bank, 0.008) * 100
                                * (1 + self.rng.uniform(-0.03, 0.03)), 2),
            })

        for i, psp in enumerate(PSP_POOL, start=1):
            self.psps.append({
                "psp_id": f"PSP-{i:03d}", "name": psp,
                "sponsor_bank": self.rng.choice(BANK_POOL),
                # Real relative "Payer App" share (NPCI Jun-2026), same scaling.
                "weight": round(REAL_PSP_SHARE.get(psp, 0.003) * 100
                                * (1 + self.rng.uniform(-0.03, 0.03)), 2),
            })

        sizes = ["Large", "Large", "Mid", "Mid", "Small"]
        for i, (name, cat) in enumerate(MERCHANT_POOL, start=1):
            size = self.rng.choice(sizes)
            self.merchants.append({
                "merchant_id": f"MID-{2000 + i}", "name": name,
                "category": cat, "region": self.rng.choice(REGIONS),
                "psp": self.rng.choice(PSP_POOL),
                "settlement_bank": self.rng.choice(BANK_POOL),
                "monthly_gmv_cr": round(self.rng.uniform(8.0, 240.0), 1),
                # V7.0 behaviour
                "size": size,
                "weight": round({"Large": self.rng.uniform(2.0, 4.0),
                                 "Mid": self.rng.uniform(0.8, 1.8),
                                 "Small": self.rng.uniform(0.2, 0.7)}[size], 2),
                "avg_ticket": FEATURE_TICKET.get(
                    "QR Payments" if cat in ("Grocery", "Retail", "Fuel", "Food Delivery")
                    else "Person to Merchant", 500) * round(self.rng.uniform(0.6, 2.2), 2),
                "repeat_rate": round(self.rng.uniform(0.35, 0.72), 2),
                "refund_rate": round(self.rng.uniform(0.004, 0.03), 3),
                "peak_hours": self.rng.choice([(11, 14), (12, 15), (18, 22),
                                               (19, 23), (9, 12)]),
                "seasonality": round(self.rng.uniform(0.9, 1.15), 2),
            })

    def build_customers(self, n: int) -> None:
        """A synthetic customer population, each with a behaviour profile that
        the transaction ledger samples from."""
        rng = self.rng
        cats = sorted({c for _n, c in MERCHANT_POOL})
        feat_names = [f[0] for f in FEATURES]
        for i in range(1, n + 1):
            city, state, _w = rng.choice(CITIES)
            profile = rng.choices(
                ["saver", "regular", "power", "merchant-heavy", "new-adopter"],
                weights=[0.22, 0.4, 0.13, 0.15, 0.10])[0]
            freq = {"saver": rng.uniform(0.2, 0.8), "regular": rng.uniform(0.8, 2.2),
                    "power": rng.uniform(3.0, 7.0), "merchant-heavy": rng.uniform(1.5, 4.0),
                    "new-adopter": rng.uniform(0.5, 1.8)}[profile]
            self.customers.append({
                "customer_id": f"CUST-{100000 + i}",
                "profile": profile,
                "city": city, "state": state,
                "region": rng.choice(REGIONS),
                "pref_psp": rng.choices(
                    PSP_POOL, weights=[REAL_PSP_SHARE.get(p, 0.003)
                                       for p in PSP_POOL])[0],
                "pref_bank": rng.choices(
                    BANK_POOL, weights=[REAL_BANK_SHARE.get(b, 0.008)
                                        for b in BANK_POOL])[0],
                "pref_feature": rng.choices(
                    feat_names, weights=[f[2] for f in FEATURES])[0],
                "pref_categories": rng.sample(cats, k=rng.randint(2, 4)),
                "pref_hours": rng.choice([(8, 11), (12, 15), (18, 22), (20, 23)]),
                "txn_freq": round(freq, 2),
                "avg_ticket": round(rng.uniform(120, 2600), 0),
                "weekend_mult": round(rng.uniform(0.7, 1.3), 2),
                "salary_week_mult": round(rng.uniform(1.1, 1.8), 2),
                "festival_mult": round(rng.uniform(1.2, 2.2), 2),
                "device": rng.choices([d for d, _w in DEVICE_TYPES],
                                      weights=[w for _d, w in DEVICE_TYPES])[0],
                # lifecycle: dormancy start day (or None), adoption day (or None)
                "dormant_from": (rng.randint(12, 30)
                                 if profile == "saver" and rng.random() < 0.35
                                 else None),
                "adopts_on": (rng.randint(6, 24)
                              if profile == "new-adopter" else None),
                "adopts_feature": rng.choice(["UPI Lite", "UPI Lite X",
                                              "UPI Autopay", "UPI Credit Line"]),
            })

    def lead(self, team: str) -> Person:
        return self.by_team[team][0]

    def anyone(self, team: str) -> Person:
        return self.rng.choice(self.by_team[team])

    def person(self, emp_id: str) -> Person:
        return self.by_id[emp_id]

    def named(self, p: Person) -> str:
        return f"{p.name} ({p.title})"

    def bank(self, name: str) -> dict:
        return next(b for b in self.banks if b["name"] == name)

    def owner_of(self, product: str) -> Person:
        team = self.product_team.get(product)
        return self.lead(team) if team and team in self.by_team else self.exec_team[0]


# ===========================================================================
# KPI metadata — the 15 canonical names the executive layer keys on. Values are
# DERIVED by TransactionEngine, not stored here.
# ===========================================================================
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

KPI_HIGHER_BETTER = {
    "UPI Transactions (M/day)": True, "Success Rate (%)": True,
    "Settlement Success (%)": True, "Technical Declines (%)": False,
    "Business Declines (%)": False, "Merchant Adoption (M)": True,
    "Active Banks": True, "Active PSPs": True, "UPI Lite Adoption (M)": True,
    "Autopay Registrations (K/day)": True, "Fraud Alerts": False,
    "Customer Complaints": False, "Merchant Complaints": False,
    "Response Time (ms)": False, "Risk Score": False,
}

# Baseline day-0 level of each KPI (kept within intelligence.py's KPI_SPEC
# ranges so health scoring stays meaningful).
BASELINE = {
    "UPI Transactions (M/day)": 750, "Success Rate (%)": 99.35,
    "Settlement Success (%)": 99.55, "Technical Declines (%)": 0.45,
    "Business Declines (%)": 0.20, "Merchant Adoption (M)": 61.5,
    "Active Banks": 731, "Active PSPs": 58, "UPI Lite Adoption (M)": 41.5,
    "Autopay Registrations (K/day)": 505, "Fraud Alerts": 1050,
    "Customer Complaints": 1950, "Merchant Complaints": 210,
    "Response Time (ms)": 735, "Risk Score": 31,
}
# Linear drift across the whole month (fixes land, adoption grows).
MONTH_GROWTH = {
    "UPI Transactions (M/day)": 0.10, "Merchant Adoption (M)": 0.045,
    "Active Banks": 0.008, "Active PSPs": 0.05, "UPI Lite Adoption (M)": 0.09,
    "Autopay Registrations (K/day)": 0.08, "Success Rate (%)": 0.002,
    "Settlement Success (%)": 0.0015, "Technical Declines (%)": -0.18,
    "Business Declines (%)": -0.12, "Customer Complaints": -0.22,
    "Merchant Complaints": -0.24, "Response Time (ms)": -0.09,
    "Risk Score": -0.15, "Fraud Alerts": -0.12,
}
# V8.0 long-horizon growth. The old model spread MONTH_GROWTH linearly over the
# whole window, so 35 and 180 days drifted by the SAME total — unrealistic over
# six months. We now treat these as *monthly* rates and compound them: a KPI at
# day d is BASELINE * (1 + rate) ** (d / 30). Rates are damped 0.6x so six months
# of compounding lands in a sane range (e.g. transactions ~ +40% over 180 days,
# technical declines roughly halve). 35-day output stays close to the old curve.
MONTHLY_GROWTH = {kpi: round(v * 0.6, 4) for kpi, v in MONTH_GROWTH.items()}


def growth_mult(kpi: str, day_index: int) -> float:
    """Compounding multiplier for a KPI at a given 0-based day index."""
    rate = MONTHLY_GROWTH.get(kpi, 0.0)
    return (1.0 + rate) ** (day_index / 30.0)


# ===========================================================================
# Operational issues — seeded, multi-day, transaction-driven events.
# ===========================================================================
# Each issue type says which KPIs it perturbs and by how much (fraction of the
# baseline), plus a human template. Signs are applied via KPI_HIGHER_BETTER.
ISSUE_TYPES = {
    "bank_timeout": {
        "label": "bank timeout / 5xx spike",
        "channel": "Bank Coordination",
        "impact": {"Success Rate (%)": 0.012, "Technical Declines (%)": 1.05,
                   "Response Time (ms)": 0.16, "Customer Complaints": 0.7,
                   "Merchant Complaints": 1.1, "Settlement Success (%)": 0.004},
        "needs": ("bank", "feature"),
    },
    "psp_latency": {
        "label": "PSP callback latency increase",
        "channel": "PSP Integration",
        "impact": {"Response Time (ms)": 0.22, "Technical Declines (%)": 0.55,
                   "Success Rate (%)": 0.006, "Customer Complaints": 0.45},
        "needs": ("psp", "feature"),
    },
    "settlement_delay": {
        "label": "merchant settlement delay",
        "channel": "Merchant Success",
        "impact": {"Settlement Success (%)": 0.011, "Merchant Complaints": 1.3,
                   "Business Declines (%)": 0.5, "Customer Complaints": 0.2},
        "needs": ("bank", "merchants"),
    },
    "fraud_spike": {
        "label": "fraud / risk spike",
        "channel": "Risk and Compliance",
        "impact": {"Fraud Alerts": 0.34, "Risk Score": 0.85,
                   "Business Declines (%)": 0.75, "Success Rate (%)": 0.004,
                   "Customer Complaints": 0.35},
        "needs": ("psp", "feature"),
    },
    "merchant_decline": {
        "label": "merchant decline-rate spike",
        "channel": "Merchant Success",
        "impact": {"Business Declines (%)": 0.7, "Merchant Complaints": 1.0,
                   "Success Rate (%)": 0.005},
        "needs": ("merchants", "feature"),
    },
    "feature_degradation": {
        "label": "feature-level degradation",
        "channel": "Core Engineering",
        "impact": {"Success Rate (%)": 0.009, "Technical Declines (%)": 0.8,
                   "Response Time (ms)": 0.12, "Customer Complaints": 0.5},
        "needs": ("feature",),
    },
}

# Decay shape of an issue over its active days (day 0 = worst).
DIP_SHAPE = [1.0, 0.62, 0.34, 0.16, 0.07, 0.02, 0.0]


@dataclass
class Issue:
    seq: int
    itype: str
    start: int              # 0-based global day
    duration: int           # active days
    severity: str
    bank: dict | None
    psp: dict | None
    feature: tuple | None   # (name, team, share)
    merchants: list[dict]
    year: int
    # canonical ids, filled on creation
    inc_id: str = ""
    rca_id: str = ""
    dec_id: str = ""

    @property
    def end(self) -> int:
        return self.start + self.duration - 1

    @property
    def product(self) -> str:
        if self.feature:
            team = self.feature[1]
            # map feature's owning squad back to a product name
            return team if team in {p[0] for p in PRODUCTS} else self.feature[0]
        if self.itype == "settlement_delay":
            return "Merchant Products"
        return "UPI Core"

    def active(self, di: int) -> bool:
        return self.start <= di <= self.end

    def intensity(self, di: int) -> float:
        if not self.active(di):
            return 0.0
        sev = 1.0 if self.severity == "Sev-2" else 0.6
        off = di - self.start
        shape = DIP_SHAPE[off] if off < len(DIP_SHAPE) else 0.0
        return sev * shape

    def entity_label(self) -> str:
        if self.bank:
            return self.bank["name"]
        if self.psp:
            return self.psp["name"]
        if self.merchants:
            return ", ".join(m["name"] for m in self.merchants[:2])
        return self.feature[0] if self.feature else "UPI"


class TransactionEngine:
    """Simulates 35 days of transaction behaviour and derives every KPI, plus
    per-bank / per-PSP / per-feature breakdowns, from it. Deterministic."""

    def __init__(self, org: Org, rng: random.Random, week_start: date,
                 days: int = 35):
        self.org = org
        self.rng = rng
        self.week_start = week_start
        self.days = days
        self.year = week_start.year
        self.dates = [week_start + timedelta(days=i) for i in range(days)]
        self.issues: list[Issue] = []
        self.archetype: list[str] = []
        self._vol_mult: list[float] = []
        self.series: dict[str, list[float]] = {}
        self.bank_success: dict[str, list[float]] = {}
        self.bank_txns: dict[str, list[float]] = {}
        self.psp_success: dict[str, list[float]] = {}
        self.psp_p95: dict[str, list[int]] = {}
        self.psp_txns: dict[str, list[float]] = {}
        self.feature_vol: dict[str, list[float]] = {}
        self._build()

    # ---------------------------------------------------------------- issues
    def _seed_issues(self) -> None:
        rng, days = self.rng, self.days
        tier1 = [b for b in self.org.banks if b["tier"] == "Tier 1"]
        seq = 0

        def make(itype: str, start: int, dur: int, sev: str) -> Issue:
            nonlocal seq
            seq += 1
            spec = ISSUE_TYPES[itype]
            needs = spec["needs"]
            bank = rng.choice(tier1 if itype != "settlement_delay"
                              else self.org.banks) if "bank" in needs else None
            psp = rng.choice(self.org.psps) if "psp" in needs else None
            feature = rng.choice(FEATURES) if "feature" in needs else None
            if itype == "bank_timeout" and feature is None:
                feature = rng.choice([f for f in FEATURES
                                      if f[0] in ("UPI Autopay", "Person to Merchant",
                                                  "QR Payments")])
            merchants = (rng.sample(self.org.merchants, k=rng.randint(2, 4))
                         if "merchants" in needs else [])
            iss = Issue(seq=seq, itype=itype, start=start, duration=dur,
                        severity=sev, bank=bank, psp=psp, feature=feature,
                        merchants=merchants, year=self.year)
            iss.inc_id = f"INC-{self.year}-{seq:02d}"
            if dur >= 3:
                iss.rca_id = f"RCA-{self.year}-{seq:02d}"
                iss.dec_id = f"DEC-{self.year}-{seq:02d}"
            return iss

        # Anchor incident: a Sev-2 bank timeout early in the month on a Tier-1
        # bank and a high-value feature. Guarantees a rich, recoverable incident
        # for the executive layer regardless of seed.
        anchor_feature = rng.choice([f for f in FEATURES
                                     if f[0] in ("UPI Autopay", "Person to Merchant")])
        anchor = make("bank_timeout", start=rng.randint(2, 4), dur=4, sev="Sev-2")
        anchor.feature = anchor_feature
        self.issues.append(anchor)
        used_starts: list[int] = [anchor.start]
        # A "repeat-offender" Tier-1 bank that recurs across the six months, so
        # banks_at_risk / weeks-flagged has a real multi-month signal.
        repeat_bank = anchor.bank or (rng.choice(tier1) if tier1 else None)

        # One Sev-2 major incident roughly per 30-day month after the first, so
        # every month of the six-month history has a headline incident to
        # investigate. Some reuse the repeat-offender bank.
        months = max(1, days // 30)
        major_types = ["bank_timeout", "fraud_spike", "settlement_delay"]
        for m in range(1, months):
            start = m * 30 + rng.randint(-4, 6)
            start = max(1, min(start, days - 4))
            if any(abs(start - u) < 3 for u in used_starts):
                continue
            used_starts.append(start)
            itype = rng.choice(major_types)
            iss = make(itype, start=start, dur=rng.randint(3, 5), sev="Sev-2")
            if itype == "bank_timeout" and repeat_bank and rng.random() < 0.6:
                iss.bank = repeat_bank
            self.issues.append(iss)

        # A spread of further Sev-3 issues, ~1 per week across the whole horizon.
        n_more = max(4, round(days / 7))
        weighted_types = (["psp_latency"] * 3 + ["settlement_delay"] * 3 +
                          ["fraud_spike"] * 2 + ["merchant_decline"] * 2 +
                          ["feature_degradation"] * 2 + ["bank_timeout"] * 1)
        # candidate start days, spread out, avoiding the anchor window
        pool = [d for d in range(1, days - 2) if not anchor.active(d)]
        rng.shuffle(pool)
        for _ in range(n_more):
            if not pool:
                break
            start = pool.pop()
            if any(abs(start - u) < 2 for u in used_starts):
                continue
            used_starts.append(start)
            itype = rng.choice(weighted_types)
            dur = rng.randint(2, 5)
            dur = min(dur, days - start)
            sev = "Sev-2" if (itype in ("bank_timeout", "fraud_spike")
                              and dur >= 3 and rng.random() < 0.5) else "Sev-3"
            self.issues.append(make(itype, start, dur, sev))

        self.issues.sort(key=lambda i: i.start)

    # -------------------------------------------------------------- archetype
    def _day_profile(self) -> None:
        rng = self.rng
        months = max(1, self.days // 30)
        # ~2 seeded high-volume campaign/festival days per month on weekdays.
        weekdays = [d for d in range(self.days)
                    if self.dates[d].weekday() < 5]
        n_campaign = min(len(weekdays), max(2, months * 2))
        campaigns = set(rng.sample(weekdays, k=n_campaign))
        # a maintenance window on ~one Sunday per month.
        sundays = [d for d in range(self.days) if self.dates[d].weekday() == 6]
        maint_days = set(rng.sample(sundays, k=min(len(sundays), months)) or
                         [self.days - 1])
        self.maint_days = maint_days
        maint_day = min(maint_days) if maint_days else self.days - 1
        for d in range(self.days):
            dt = self.dates[d]
            wd = dt.weekday()
            if d in campaigns:
                self.archetype.append("High-volume campaign day")
                mult = 1.22
            elif dt.day >= 28:
                self.archetype.append("Month-end peak")
                mult = 1.12
            elif wd == 6:
                self.archetype.append("Sunday (quiet)"
                                      + (" · maintenance window" if d in maint_days
                                         else ""))
                mult = 0.82
            elif wd == 5:
                self.archetype.append("Saturday (lighter)")
                mult = 0.9
            elif wd == 0:
                self.archetype.append("Monday (ramp-up)")
                mult = 0.97
            else:
                self.archetype.append("Weekday (steady)")
                mult = 1.0
            self._vol_mult.append(mult * (1 + rng.uniform(-0.02, 0.02)))
        self.maint_day = maint_day
        self.campaign_days = campaigns

    # ------------------------------------------------------------------ build
    def _build(self) -> None:
        self._seed_issues()
        self._day_profile()
        rng = self.rng
        j = lambda s: 1.0 + rng.uniform(-s, s)  # noqa: E731

        # Aggregate stress per day, split into the dimensions issues perturb.
        for kpi, base in BASELINE.items():
            hb = KPI_HIGHER_BETTER[kpi]
            vals: list[float] = []
            for d in range(self.days):
                trend = base * growth_mult(kpi, d)
                v = trend
                if kpi == "UPI Transactions (M/day)":
                    v = trend * self._vol_mult[d]
                else:
                    perturb = 0.0
                    for iss in self.issues:
                        mag = ISSUE_TYPES[iss.itype]["impact"].get(kpi)
                        if mag:
                            perturb += trend * mag * iss.intensity(d)
                    if perturb:
                        v += perturb if not hb else -perturb
                vj = v * j(0.01)
                if "%" in kpi:  # percentages stay physical
                    vj = max(0.0, min(vj, 99.98 if hb else 100.0))
                vals.append(vj)
            vals = self._round(kpi, vals)
            self.series[kpi] = vals

        self._build_entities()

    def _build_entities(self) -> None:
        rng = self.rng
        total = self.series["UPI Transactions (M/day)"]
        # per-bank
        wsum = sum(b["weight"] for b in self.org.banks)
        for b in self.org.banks:
            base_sr = rng.uniform(99.25, 99.68) if b["tier"] == "Tier 1" \
                else rng.uniform(98.9, 99.5)
            succ, txns = [], []
            for d in range(self.days):
                s = base_sr
                for iss in self.issues:
                    if iss.bank and iss.bank["name"] == b["name"]:
                        s -= (2.2 if iss.severity == "Sev-2" else 1.2) * iss.intensity(d)
                succ.append(round(max(95.5, s), 2))
                txns.append(round(total[d] * b["weight"] / wsum, 1))
            self.bank_success[b["name"]] = succ
            self.bank_txns[b["name"]] = txns
        # per-PSP. Volume follows the real "Payer App" share (PhonePe/Google
        # Pay/Paytm dominate); success/latency carry the per-app health profile.
        psp_wsum = sum(p["weight"] for p in self.org.psps)
        for p in self.org.psps:
            base_p95 = rng.randint(190, 340)
            base_sr = rng.uniform(99.0, 99.6)
            p95s, succ, txns = [], [], []
            for d in range(self.days):
                lat, s = base_p95, base_sr
                for iss in self.issues:
                    if iss.psp and iss.psp["name"] == p["name"]:
                        lat += int(base_p95 * (1.6 if iss.severity == "Sev-2" else 0.9)
                                   * iss.intensity(d))
                        s -= 1.0 * iss.intensity(d)
                p95s.append(int(lat))
                succ.append(round(max(96.0, s), 2))
                txns.append(round(total[d] * p["weight"] / psp_wsum, 1))
            self.psp_p95[p["name"]] = p95s
            self.psp_success[p["name"]] = succ
            self.psp_txns[p["name"]] = txns
        # per-feature volume (share of the day's total)
        for name, _team, share in FEATURES:
            self.feature_vol[name] = [round(total[d] * share, 1)
                                      for d in range(self.days)]

    @staticmethod
    def _round(kpi: str, vals: list[float]) -> list:
        if kpi in ("Active Banks", "Active PSPs", "Autopay Registrations (K/day)",
                   "Fraud Alerts", "Customer Complaints", "Merchant Complaints",
                   "Response Time (ms)", "Risk Score"):
            return [int(round(v)) for v in vals]
        if "%" in kpi:
            return [round(v, 2) for v in vals]
        return [round(v, 1) for v in vals]

    # ----------------------------------------------------------- KPI accessors
    def names(self) -> list[str]:
        return list(self.series.keys())

    def value(self, kpi: str, di: int):
        return self.series[kpi][di]

    def fmt(self, kpi: str, di: int) -> str:
        v = self.value(kpi, di)
        if "%" in kpi:
            return f"{v}%"
        if kpi == "Response Time (ms)":
            return f"{v} ms"
        if isinstance(v, float):
            return f"{v}"
        return f"{v:,}"

    def delta(self, kpi: str, di: int):
        if di == 0:
            return None
        return round(self.value(kpi, di) - self.value(kpi, di - 1), 2)

    def week_of(self, di: int) -> int:
        return di // 7

    def delta_week_over_week(self, kpi: str, di: int):
        prev = di - 7
        if prev < 0:
            return None
        return round(self.value(kpi, di) - self.value(kpi, prev), 2)

    def delta_month(self, kpi: str, di: int):
        if di == 0:
            return None
        return round(self.value(kpi, di) - self.value(kpi, 0), 2)

    # ----------------------------------------------------- event lookups
    def issues_opening(self, di: int) -> list[Issue]:
        return [i for i in self.issues if i.start == di]

    def issues_active(self, di: int) -> list[Issue]:
        return [i for i in self.issues if i.active(di)]

    def issues_recovering(self, di: int) -> list[Issue]:
        return [i for i in self.issues if i.end == di]

    def top_banks(self, di: int, n: int = 5) -> list[tuple[str, float, float]]:
        rows = [(b["name"], self.bank_txns[b["name"]][di],
                 self.bank_success[b["name"]][di]) for b in self.org.banks]
        rows.sort(key=lambda r: r[1], reverse=True)
        return rows[:n]

    def top_psps(self, di: int, n: int = 5) -> list[tuple[str, float, float, int]]:
        """Top UPI apps by *volume* (matching how NPCI reports app share),
        carrying each app's success rate and callback p95."""
        rows = [(p["name"], self.psp_txns[p["name"]][di],
                 self.psp_success[p["name"]][di], self.psp_p95[p["name"]][di])
                for p in self.org.psps]
        rows.sort(key=lambda r: r[1], reverse=True)
        return rows[:n]

    def top_features(self, di: int, n: int = 5) -> list[tuple[str, float]]:
        rows = [(name, self.feature_vol[name][di]) for name, _t, _s in FEATURES]
        rows.sort(key=lambda r: r[1], reverse=True)
        return rows[:n]

    def worst_bank(self, di: int) -> tuple[str, float]:
        rows = [(b["name"], self.bank_success[b["name"]][di]) for b in self.org.banks]
        rows.sort(key=lambda r: r[1])
        return rows[0]

    def weekly_flags(self) -> dict[int, dict[str, set]]:
        """{week_index: {"banks": set, "psps": set, "merchants": set}}.

        Each incident flags only the week it *opened* in — which is also where
        its KPI dip is worst (DIP_SHAPE peaks on day 0). This keeps the workbook
        flag aligned with the week that holds the incident's record/RCA, so the
        executive layer's "latest flagged week" always resolves to a real
        incident artifact from that same week."""
        out: dict[int, dict[str, set]] = {
            w: {"banks": set(), "psps": set(), "merchants": set()}
            for w in range(-(-self.days // 7))
        }
        for iss in self.issues:
            w = iss.start // 7
            if w not in out:
                continue
            if iss.bank:
                out[w]["banks"].add(iss.bank["name"])
            if iss.psp:
                out[w]["psps"].add(iss.psp["name"])
            for m in iss.merchants:
                out[w]["merchants"].add(m["name"])
        return out


# ===========================================================================
# Operations driver — dates, id helpers, task/email sequencing.
# ===========================================================================
class Ops:
    # stable ids that always exist (safe padding targets)
    WB = "upi_kpis_month.xlsx"
    OVERVIEW = "ORG-OVERVIEW"
    STORYLINE = "STORYLINE"
    MONTHLY = "RPT-MONTHLY-EXEC"

    SOP_BY_TYPE = {
        "bank_timeout": ("SOP-UPI-BANK-FAILOVER-014", "Bank failover & retry SOP"),
        "psp_latency": ("SOP-UPI-PSP-LATENCY-018", "PSP latency handling SOP"),
        "settlement_delay": ("SOP-UPI-SETTLEMENT-022", "Settlement recovery SOP"),
        "fraud_spike": ("SOP-UPI-RISK-030", "Fraud & risk response SOP"),
        "merchant_decline": ("SOP-UPI-MERCHANT-025", "Merchant decline triage SOP"),
        "feature_degradation": ("SOP-UPI-FEATURE-011", "Feature degradation SOP"),
    }

    def __init__(self, k: TransactionEngine):
        self.k = k
        self.dates = k.dates
        self.days = k.days
        self.year = k.year
        self._task_seq = 0
        self._email_seq: dict[int, int] = {}
        self._sops_emitted: set[str] = set()

    def when(self, di: int, hh: int, mm: int = 0) -> datetime:
        return datetime.combine(self.dates[di], time(hh, mm))

    def next_task_id(self) -> str:
        self._task_seq += 1
        return f"TASK-{self._task_seq:04d}"

    def email_id(self, di: int) -> str:
        n = self._email_seq.get(di, 0) + 1
        self._email_seq[di] = n
        return f"EMAIL-D{di+1:02d}-{n:03d}"

    def report_id(self, di: int) -> str:
        return f"RPT-D{di+1:02d}-DAILY"

    def monitor_id(self, di: int) -> str:
        return f"TEAMS-D{di+1:02d}-MON"

    def weekly_id(self, w: int) -> str:
        return f"RPT-W{w+1}-REVIEW"

    def weekly_mtg_id(self, w: int) -> str:
        return f"MTG-W{w+1}-REVIEW"

    def sop_for(self, itype: str) -> str:
        return self.SOP_BY_TYPE.get(itype, self.SOP_BY_TYPE["feature_degradation"])[0]


# ===========================================================================
# Artifact writer — records every file plus its declared cross-references.
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
        return "Refs: " + ", ".join(r for r in refs if r)

    def _base(self, day: int | None, top: str) -> Path:
        if top:
            return self.out / top
        return self.out / (f"day_{day:02d}" if day else "master")

    def doc(self, day: int | None, sub: str, filename: str, art_id: str,
            kind: str, when: datetime, title: str, body: str,
            refs: list[str], top: str = "") -> str:
        base = self._base(day, top)
        folder = base / sub if sub else base
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
        folder = (self.out / (f"day_{day:02d}" if day else "master") / sub
                  if sub else self.out / (f"day_{day:02d}" if day else "master"))
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / filename
        self.artifacts.append(Artifact(art_id, kind, path, when, _dedupe(refs)))
        self._ids.add(art_id)
        return path

    _DATA_KINDS = {"workbook", "master"}

    def validate(self) -> list[str]:
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


def _pad(refs: list[str], ops: Ops) -> list[str]:
    """Guarantee >= 3 references using always-existing anchors."""
    out = _dedupe(refs)
    for anchor in (ops.WB, ops.OVERVIEW, ops.STORYLINE):
        if len(out) >= 3:
            break
        if anchor not in out:
            out.append(anchor)
    return out


# ===========================================================================
# Prose helpers.
# ===========================================================================
def kline(k: TransactionEngine, kpi: str, di: int, with_delta: bool = True) -> str:
    base = f"{kpi.split(' (')[0]} at {k.fmt(kpi, di)}"
    if with_delta and di > 0:
        d = k.delta(kpi, di)
        if d is not None and d != 0:
            arrow = "up" if d > 0 else "down"
            base += f" ({arrow} {abs(d)} vs {k.dates[di-1].strftime('%a %d %b')})"
    return base


def sign_off(p: Person) -> str:
    first = p.name.split()[0]
    return f"{first}\n{p.name}\n{p.title}\n{DEPARTMENT}, {ORG_NAME}"


# ---------------------------------------------------------------------------
# Natural-language prose builders. Every sentence is composed from the day's
# *actual* engine state (volume, week-on-week delta, success, active incidents,
# softest bank/metric) so it reads like an experienced analyst wrote it rather
# than a fixed template. Phrasing variety is indexed by the day, so repeated
# days never read identically — without consuming the RNG stream, which would
# break the corpus's determinism guarantee.
# ---------------------------------------------------------------------------
_ARCHETYPE_CLAUSE = {
    "High-volume campaign day": "a campaign-driven high-volume day",
    "Month-end peak": "the month-end surge as salary and bill-pay flows land",
    "Saturday (lighter)": "a lighter Saturday",
    "Monday (ramp-up)": "the Monday ramp-up after the weekend",
    "Weekday (steady)": "a steady mid-week day",
}


def _archetype_clause(arch: str) -> str:
    if arch.startswith("Sunday"):
        return ("a quiet Sunday with a scheduled maintenance window"
                if "maintenance" in arch else "a quiet Sunday")
    return _ARCHETYPE_CLAUSE.get(arch, "a normal operating day")


def _wow_clause(k: "TransactionEngine", di: int) -> str:
    dw = k.delta_week_over_week("UPI Transactions (M/day)", di)
    if dw is None:
        return "the first day in the window"
    if abs(dw) < 0.1:
        return "broadly flat against the same day last week"
    return (f"{'up' if dw > 0 else 'down'} {abs(dw):.1f}M "
            "on the same day last week")


def transaction_summary(k: "TransactionEngine", di: int) -> str:
    """One or two natural sentences describing the day's throughput and health."""
    weekday = k.dates[di].strftime("%A")
    vol = k.fmt("UPI Transactions (M/day)", di)
    sr = k.fmt("Success Rate (%)", di)   # already includes the % sign
    ss = k.fmt("Settlement Success (%)", di)
    lead = (f"The rail processed {vol}M UPI transactions on {weekday} — "
            f"{_archetype_clause(k.archetype[di])} — {_wow_clause(k, di)}.")
    active = k.issues_active(di)
    if active:
        worst = ", ".join(sorted({i.entity_label() for i in active}))
        return (f"{lead} Success landed at {sr} and settlement at {ss}, held "
                f"back by live issues on {worst} (detailed below).")
    wb, wf = k.worst_bank(di)
    return (f"{lead} Success held at {sr} and settlement at {ss}; the softest "
            f"bank was {wb} at {wf}%, still comfortably inside the normal band.")


_STEADY_FOCUS = [
    "keep the standard monitoring cadence and let the adoption programmes run",
    "use the quieter window to progress capacity planning before the next peak",
    "hold the monitoring line and work down the merchant-onboarding backlog",
    "no action beyond routine watch; pick up the SLA trend at the next sync",
]


def _softest_kpi(k: "TransactionEngine", di: int) -> str:
    """Name the headline metric that has drifted most adversely this month."""
    candidates = ["Success Rate (%)", "Technical Declines (%)",
                  "Response Time (ms)", "Customer Complaints",
                  "Merchant Complaints"]
    worst_kpi, worst_score = "", 0.0
    for kpi in candidates:
        dm = k.delta_month(kpi, di)
        if dm is None:
            continue
        adverse = dm if not KPI_HIGHER_BETTER[kpi] else -dm
        score = adverse / (abs(BASELINE.get(kpi, 1)) or 1)
        if score > worst_score:
            worst_kpi, worst_score = kpi, score
    if worst_kpi and worst_score > 0.02:
        return (f"{worst_kpi.split(' (')[0]} at {k.fmt(worst_kpi, di)}, "
                "drifting the wrong way this month")
    return ""


def recommendation(k: "TransactionEngine", di: int) -> str:
    """State-driven recommendation prose (never a fixed template)."""
    active = k.issues_active(di)
    if active:
        worst = ", ".join(sorted({i.entity_label() for i in active}))
        plural = "s" if len(active) > 1 else ""
        return (f"Stay on the open incident{plural}: keep recovery monitoring on "
                f"{worst} and hold the bank/PSP bridge until success clears the "
                "99.2% floor and stays there through two clean hours.")
    base = _STEADY_FOCUS[di % len(_STEADY_FOCUS)]
    watch = _softest_kpi(k, di)
    return (f"Steady state — {base}." if not watch
            else f"Steady state — {base}. Worth a glance: {watch}.")


# ===========================================================================
# Daily routine emitters (run every day, incident or not).
# ===========================================================================
def emit_monitoring(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                    di: int) -> str:
    """A transaction-monitoring Teams note — cheap, always present, referenced
    by the day's report."""
    gd = di + 1
    mid = ops.monitor_id(di)
    ana = org.lead("Product Analytics")
    opslead = org.lead("Product Operations")
    active = k.issues_active(di)
    tps_peak = int(k.value("UPI Transactions (M/day)", di) * 1_000_000 / 86400 * 3.1)
    wb, wf = k.worst_bank(di)
    open_line = ("No open incidents — steady-state monitoring."
                 if not active else
                 "Open items: " + "; ".join(
                     f"{i.inc_id} ({ISSUE_TYPES[i.itype]['label']} · {i.entity_label()})"
                     for i in active))
    refs = _pad([ops.WB, ops.report_id(di)] + [i.inc_id for i in active], ops)
    body = f"""**Channel:** UPI Products / Ops Monitoring
**Date:** {k.dates[di].strftime('%A %d %b %Y')} · **Day archetype:** {k.archetype[di]}

**{opslead.name}** · 09:15
Morning sweep for {k.dates[di].strftime('%d %b')}. {kline(k, 'UPI Transactions (M/day)', di)};
{kline(k, 'Success Rate (%)', di)}; {kline(k, 'Technical Declines (%)', di)};
{kline(k, 'Business Declines (%)', di)}. Estimated peak ~{tps_peak:,} TPS.

**{ana.name}** · 09:22
Lowest bank success today: {wb} at {wf}%. Settlement Success
{k.fmt('Settlement Success (%)', di)}. Complaints: customer {k.fmt('Customer Complaints', di)},
merchant {k.fmt('Merchant Complaints', di)}. Full numbers in {ops.report_id(di)} and {ops.WB}.

**{opslead.name}** · 09:30
{open_line}"""
    return c.doc(gd, "teams", f"TEAMS-D{gd:02d}-monitoring.md", mid, "teams",
                 ops.when(di, 9, 30), f"Ops Monitoring — {k.dates[di].strftime('%d %b %Y')}",
                 body, refs)


def emit_daily_report(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                      di: int, monitor_ref: str) -> str:
    gd = di + 1
    rid = ops.report_id(di)
    ana = org.lead("Product Analytics")
    active = k.issues_active(di)

    def cmp_line(kpi: str) -> str:
        parts = [k.fmt(kpi, di)]
        dd, dw, dm = k.delta(kpi, di), k.delta_week_over_week(kpi, di), k.delta_month(kpi, di)
        extra = []
        if dd is not None and dd != 0:
            extra.append(f"{'▲' if dd > 0 else '▼'}{abs(dd)} d/d")
        if dw is not None and dw != 0:
            extra.append(f"{'▲' if dw > 0 else '▼'}{abs(dw)} w/w")
        if dm is not None and dm != 0:
            extra.append(f"{'▲' if dm > 0 else '▼'}{abs(dm)} m/m")
        tail = f"  ({', '.join(extra)})" if extra else ""
        return f"- **{kpi.split(' (')[0]}:** {parts[0]}{tail}"

    headline_kpis = ["UPI Transactions (M/day)", "Success Rate (%)",
                     "Settlement Success (%)", "Technical Declines (%)",
                     "Business Declines (%)", "Customer Complaints",
                     "Merchant Complaints", "Fraud Alerts", "Risk Score",
                     "Response Time (ms)"]
    kpi_lines = "\n".join(cmp_line(kpi) for kpi in headline_kpis)

    banks = "\n".join(f"| {n} | {tx} | {sr}% |" for n, tx, sr in k.top_banks(di))
    psps = "\n".join(f"| {n} | {tx} | {sr}% | {p95} ms |"
                     for n, tx, sr, p95 in k.top_psps(di))
    feats = "\n".join(f"| {n} | {v} |" for n, v in k.top_features(di))

    if active:
        fa = "\n".join(
            f"- {i.inc_id} — {ISSUE_TYPES[i.itype]['label']} on {i.entity_label()}"
            f" (day {di - i.start + 1} of {i.duration}); see {i.rca_id or i.inc_id}."
            for i in active)
    else:
        fa = ("- No incidents open. Technical declines are within the "
              f"{k.fmt('Technical Declines (%)', di)} steady-state band; "
              "residual failures are routine bank/network timeouts.")
    rec = recommendation(k, di)

    prev = [ops.report_id(di - 1)] if di > 0 else []
    rca_refs = [i.rca_id for i in active if i.rca_id]
    inc_refs = [i.inc_id for i in active]
    refs = _pad([ops.WB, monitor_ref, *prev, *inc_refs, *rca_refs], ops)

    body = f"""**Report ID:** {rid}  ·  **Prepared by:** {ana.name}
**Date:** {k.dates[di].strftime('%A %d %b %Y')}  ·  **Day archetype:** {k.archetype[di]}
**Source:** {ops.WB} ("Monthly KPIs", day {gd} of {ops.days})

## Transaction summary
{transaction_summary(k, di)}

## KPIs (today · vs yesterday / last week / month start)
{kpi_lines}

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
{banks}

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
{psps}

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
{feats}

## Failure analysis
{fa}

## Recommendations
{rec}

## Notes
All figures read from {ops.WB}; they match the day's monitoring note
({monitor_ref}) and any meetings/emails on {k.dates[di].strftime('%d %b')}."""
    return c.doc(gd, "reports", f"RPT-D{gd:02d}-daily.md", rid, "report",
                 ops.when(di, 17, 30),
                 f"UPI Products — Daily Operations Report "
                 f"({k.dates[di].strftime('%A, %d %b %Y')})", body, refs)


# ===========================================================================
# Issue lifecycle emitters.
# ===========================================================================
def _task(c: Corpus, org: Org, ops: Ops, di: int, title: str, owner: Person,
          created_by: Person, priority: int, status: str, due: datetime,
          refs: list[str]) -> str:
    gd = di + 1
    tid = ops.next_task_id()
    links = "\n".join("- " + r for r in _dedupe(refs) if r)
    body = f"""**Task ID:** {tid}  ·  **Status:** {status}  ·  **Priority:** P{priority}
**Owner:** {org.named(owner)}  ·  **Created by:** {org.named(created_by)}
**Created:** {ops.when(di, 9, 45).strftime('%d %b %Y %H:%M IST')}  ·  **Due:** {due.strftime('%d %b %Y %H:%M IST')}
**Team:** {owner.team}

## Description
{title}.

## Links
{links}"""
    return c.doc(gd, "tasks", f"{tid}.md", tid, "task", ops.when(di, 9, 45),
                 f"Task {tid} — {title}", body, _pad(refs, ops))


def emit_issue_open(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                    iss: Issue) -> None:
    """Day-0 of an issue: incident record, anomaly email, bridge note + bridge
    meeting, and opening tasks."""
    di = iss.start
    gd = di + 1
    spec = ISSUE_TYPES[iss.itype]
    ana = org.lead("Product Analytics")
    opslead = org.lead("Product Operations")
    prod_owner = org.owner_of(iss.product)
    psp_lead = org.lead("PSP Integration")
    risk = org.lead("Risk & Compliance")
    cx = org.lead("Customer Experience")
    merch = org.lead("Merchant Success")
    entity = iss.entity_label()
    rep = ops.report_id(di)

    # Incident record ------------------------------------------------------
    c.doc(gd, "incidents", f"{iss.inc_id}-record.md", iss.inc_id, "incident",
          ops.when(di, 9, 0),
          f"Incident Record — {iss.inc_id} {iss.product} {spec['label']}",
          f"""**Incident ID:** {iss.inc_id}  ·  **Severity:** {iss.severity}  ·  **Status:** Investigating
**Product:** {iss.product}  ·  **Commander:** {opslead.name}
**Detected:** {ops.when(di, 8, 30).strftime('%d %b %Y %H:%M IST')} (morning KPI sweep)

## Summary
A {spec['label']} on {entity} degraded {iss.product}. Success Rate at
{k.fmt('Success Rate (%)', di)}, Technical Declines {k.fmt('Technical Declines (%)', di)},
Response Time p95 {k.fmt('Response Time (ms)', di)}. Customer Complaints
{k.fmt('Customer Complaints', di)}, Merchant Complaints {k.fmt('Merchant Complaints', di)}.

## Impact
{('Affected merchants: ' + ', '.join(m['name'] for m in iss.merchants) + '.') if iss.merchants else 'Impact concentrated on the ' + iss.product + ' path.'}
Expected active window: {k.dates[di].strftime('%d %b')} - {k.dates[iss.end].strftime('%d %b')}.

## Timeline (day 1)
- 06:25 — first elevated failures on {iss.product}.
- 08:30 — anomaly flagged by KPI sweep ({rep}).
- 09:30 — incident bridge convened; {iss.severity} confirmed.

Root cause {'under investigation — see ' + iss.rca_id if iss.rca_id else 'being triaged as a short operational issue'}.
{('Permanent fix tracked as ' + iss.dec_id + '.') if iss.dec_id else ''}""",
          _pad([ops.WB, rep, iss.rca_id, iss.dec_id, ops.monitor_id(di)], ops))

    # Anomaly email --------------------------------------------------------
    eid = ops.email_id(di)
    c.doc(gd, "outlook", f"{eid}-anomaly.md", eid, "email", ops.when(di, 8, 40),
          f"[Action] {iss.product} — {spec['label']} on {entity}",
          f"""**From:** {ana.name} <{ana.email}>
**To:** upi-operations@npci-demo.in; upi-leadership@npci-demo.in
**Cc:** {opslead.name}, {prod_owner.name}
**Sent:** {ops.when(di, 8, 40).strftime('%a %d %b %Y, %H:%M IST')}
**Subject:** [Action] {iss.product} {spec['label']} flagged by the morning sweep

Team,

The KPI sweep this morning flagged {iss.product}. {kline(k, 'Success Rate (%)', di)},
{kline(k, 'Technical Declines (%)', di)}. Early cut points at {entity}.

I have opened incident {iss.inc_id} ({iss.severity}). Proposing the incident
bridge at 09:30. Day workbook and dashboards are in {rep} / {ops.WB}.

{sign_off(ana)}""",
          _pad([iss.inc_id, rep, ops.WB], ops))

    # Bridge note + meeting -----------------------------------------------
    mtg = f"MTG-D{gd:02d}-BRIDGE-{iss.seq:02d}"
    tnote = f"TEAMS-D{gd:02d}-BRIDGE-{iss.seq:02d}"
    c.doc(gd, "teams", f"{tnote}.md", tnote, "teams", ops.when(di, 9, 5),
          f"Teams — Incident Bridge {iss.inc_id}",
          f"""**Channel:** UPI Products / {spec['channel']}
**Date:** {k.dates[di].strftime('%A %d %b %Y')}

**{opslead.name}** · 09:05
Opening the bridge for {iss.inc_id} ({iss.severity}, {iss.product}). Bridge {mtg} at 09:30.

**{ana.name}** · 09:10
{kline(k, 'Success Rate (%)', di, False)}; {kline(k, 'Technical Declines (%)', di, False)};
Customer Complaints {k.fmt('Customer Complaints', di)} and climbing.

**{prod_owner.name}** · 09:18
Confirmed on our side — {spec['label']} on {entity}. Moving detail to {mtg}.
{('RCA will be ' + iss.rca_id + '.') if iss.rca_id else ''}""",
          _pad([iss.inc_id, mtg, iss.rca_id, rep], ops))

    attendees = [opslead, ana, prod_owner, psp_lead, risk, cx, merch]
    c.doc(gd, "meetings", f"{mtg}.md", mtg, "meeting", ops.when(di, 9, 30),
          f"Incident Bridge — {iss.product} {spec['label']} ({iss.severity})",
          f"""**Meeting ID:** {mtg}  ·  **Type:** Incident Bridge ({iss.severity})
**Room:** Virtual Bridge A  ·  **Start:** {ops.when(di, 9, 30).strftime('%d %b %Y %H:%M IST')}
**Incident:** {iss.inc_id}

## Attendees
{chr(10).join('- ' + org.named(p) for p in attendees)}

## Agenda
1. Confirm scope and severity of {iss.inc_id}.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- {ana.name.split()[0]} presented the sweep: {kline(k, 'Success Rate (%)', di)},
  {kline(k, 'Technical Declines (%)', di)}. Regression is confined to {iss.product} on {entity}.
- {prod_owner.name.split()[0]} confirmed the {spec['label']}; unrelated flows are green.
- {cx.name.split()[0]} noted Customer Complaints {k.fmt('Customer Complaints', di)},
  Merchant Complaints {k.fmt('Merchant Complaints', di)}.

## Decisions
- Treat {iss.inc_id} as {iss.severity}.
{('- RCA ' + iss.rca_id + ' to be drafted by EOD next day; permanent fix under ' + iss.dec_id + '.') if iss.rca_id else '- Handle as a short operational issue; recovery monitoring only.'}

## Action items
- [ ] {prod_owner.name}: lead investigation for {iss.inc_id}.
- [ ] {ana.name}: complaint + KPI breakdown into {rep}.""",
          _pad([iss.inc_id, iss.rca_id, iss.dec_id, rep, tnote], ops))

    # Opening tasks --------------------------------------------------------
    _task(c, org, ops, di, f"Investigate {iss.inc_id} ({spec['label']} on {entity})",
          prod_owner, opslead, 1, "in_progress", ops.when(min(iss.end, ops.days - 1), 18, 0),
          [iss.inc_id, mtg, iss.rca_id or ops.WB])
    _task(c, org, ops, di, f"Complaint & KPI breakdown for {iss.inc_id}",
          ana, opslead, 2, "done", ops.when(di, 17, 0),
          [iss.inc_id, rep, ops.WB])


def emit_issue_midlife(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                       iss: Issue) -> None:
    """Investigation + RCA + decision + SOP, one day after the issue opened
    (only for issues that run long enough to warrant an RCA)."""
    if not iss.rca_id:
        return
    di = min(iss.start + 1, iss.end)
    gd = di + 1
    spec = ISSUE_TYPES[iss.itype]
    prod_owner = org.owner_of(iss.product)
    eng = org.lead("Engineering")
    risk = org.lead("Risk & Compliance")
    svp = org.exec_team[1]
    entity = iss.entity_label()
    rep = ops.report_id(di)
    sop_id, sop_title = Ops.SOP_BY_TYPE.get(iss.itype, Ops.SOP_BY_TYPE["feature_degradation"])

    # Investigation meeting
    invmtg = f"MTG-D{gd:02d}-INVEST-{iss.seq:02d}"
    c.doc(gd, "meetings", f"{invmtg}.md", invmtg, "meeting", ops.when(di, 11, 0),
          f"Investigation — {iss.inc_id} {iss.product}",
          f"""**Meeting ID:** {invmtg}  ·  **Incident:** {iss.inc_id}
**Start:** {ops.when(di, 11, 0).strftime('%d %b %Y %H:%M IST')}

## Discussion
- {eng.name.split()[0]} walked the logs for {entity}: the {spec['label']} pattern
  matches. Success Rate is {k.fmt('Success Rate (%)', di)} today ({kline(k, 'Success Rate (%)', di)}).
- Mitigation in place; drafting RCA {iss.rca_id} and decision {iss.dec_id}.

## Action items
- [ ] {prod_owner.name}: finalise {iss.rca_id}.
- [ ] {eng.name}: prepare the fix for {iss.dec_id} and update {sop_id}.""",
          _pad([iss.inc_id, iss.rca_id, iss.dec_id, sop_id, rep], ops))

    # RCA (lives in incidents/, filename RCA-* so the reader tags it 'rca')
    recovery_day = iss.end
    c.doc(gd, "incidents", f"{iss.rca_id}.md", iss.rca_id, "rca", ops.when(di, 15, 0),
          f"RCA — {iss.rca_id} {iss.product} {spec['label']}",
          f"""**RCA ID:** {iss.rca_id}  ·  **Incident:** {iss.inc_id}  ·  **Author:** {prod_owner.name}
**Product:** {iss.product}  ·  **Severity:** {iss.severity}

## Root cause
A {spec['label']} on {entity} propagated into {iss.product}, driving Technical
Declines to a peak of {k.fmt('Technical Declines (%)', iss.start)} on day 1 and
Success Rate to a low of {k.fmt('Success Rate (%)', iss.start)}.

## Contributing factors
- {entity} degraded during peak hours.
- Retry/failover thresholds were not tuned for this failure mode.

## Corrective actions
- Immediate: mitigation applied (documented in {sop_id}).
- Permanent: {iss.dec_id} — tune failover/retry and add alerting.

## Recovery
KPIs return to trend by {k.dates[recovery_day].strftime('%d %b')}; validated in
{ops.report_id(recovery_day)}.""",
          _pad([iss.inc_id, iss.dec_id, sop_id, rep, ops.report_id(recovery_day)], ops))

    # Decision
    c.doc(gd, "decisions", f"{iss.dec_id}.md", iss.dec_id, "decision",
          ops.when(di, 16, 0),
          f"Decision — {iss.dec_id} {iss.product} resilience",
          f"""**Decision ID:** {iss.dec_id}  ·  **Owner:** {svp.name}  ·  **Status:** Approved
**Incident:** {iss.inc_id}  ·  **RCA:** {iss.rca_id}

## Decision
Approve the corrective actions from {iss.rca_id}: tune {iss.product} failover/retry
for the {spec['label']} failure mode on {entity}, and codify the runbook in {sop_id}.

## Rationale
Success Rate dipped to {k.fmt('Success Rate (%)', iss.start)} during {iss.inc_id};
the fix restores the >= 99.2% floor and prevents recurrence.

## Follow-up
Effectiveness reviewed at the next weekly review.""",
          _pad([iss.inc_id, iss.rca_id, sop_id, rep], ops))

    # SOP (emit once per id)
    if sop_id not in ops._sops_emitted:
        ops._sops_emitted.add(sop_id)
        c.doc(gd, "docs", f"{sop_id}.md", sop_id, "sop", ops.when(di, 16, 30),
              f"{sop_id} — {sop_title}",
              f"""**SOP ID:** {sop_id}  ·  **Owner:** {org.lead('Product Operations').name}
**Applies to:** {iss.product} and related flows

## Purpose
Standard operating procedure for handling a {spec['label']}, first codified after
{iss.inc_id}.

## Procedure
1. Confirm the failure signature on the affected entity ({entity}-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from {iss.rca_id} and decision {iss.dec_id}.""",
              _pad([iss.inc_id, iss.rca_id, iss.dec_id], ops))

    _task(c, org, ops, di, f"Implement {iss.dec_id} fix and update {sop_id}",
          eng, svp, 1, "in_progress", ops.when(min(iss.end + 3, ops.days - 1), 18, 0),
          [iss.dec_id, iss.rca_id, sop_id])


def emit_issue_recovery(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                        iss: Issue) -> None:
    di = iss.end
    gd = di + 1
    spec = ISSUE_TYPES[iss.itype]
    prod_owner = org.owner_of(iss.product)
    opslead = org.lead("Product Operations")
    rep = ops.report_id(di)
    eid = ops.email_id(di)
    c.doc(gd, "outlook", f"{eid}-recovery.md", eid, "email", ops.when(di, 16, 30),
          f"[Resolved] {iss.inc_id} {iss.product} recovered",
          f"""**From:** {prod_owner.name} <{prod_owner.email}>
**To:** upi-leadership@npci-demo.in; upi-operations@npci-demo.in
**Sent:** {ops.when(di, 16, 30).strftime('%a %d %b %Y, %H:%M IST')}
**Subject:** [Resolved] {iss.inc_id} — {iss.product} back to trend

{iss.inc_id} ({spec['label']} on {iss.entity_label()}) is resolved. Success Rate
recovered to {k.fmt('Success Rate (%)', di)} and Technical Declines to
{k.fmt('Technical Declines (%)', di)}. Validated in {rep}.
{('Fix and runbook tracked under ' + iss.dec_id + '.') if iss.dec_id else ''}

{sign_off(prod_owner)}""",
          _pad([iss.inc_id, iss.dec_id, iss.rca_id, rep], ops))


# ===========================================================================
# Operational reviews (non-incident) + weekly / monthly rollups.
# ===========================================================================
def emit_operational_review(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                            di: int, kind: str) -> None:
    """Adoption / capacity / SLA reviews of EXISTING features — no launches."""
    gd = di + 1
    rep = ops.report_id(di)
    strat = org.lead("Product Strategy")
    ana = org.lead("Product Analytics")
    if kind == "adoption":
        title = "UPI Lite & Autopay adoption review"
        owner, chan = strat, "Analytics"
        body_focus = (f"UPI Lite Adoption at {k.fmt('UPI Lite Adoption (M)', di)}M; "
                      f"Autopay Registrations {k.fmt('Autopay Registrations (K/day)', di)}K/day. "
                      "Reviewed growth by PSP and category; no product changes — "
                      "operating the existing features.")
    elif kind == "capacity":
        title = "Capacity planning ahead of high-volume day"
        owner, chan = org.lead("Technology"), "Ops Monitoring"
        body_focus = (f"Projected peak volume near {k.fmt('UPI Transactions (M/day)', di)}M/day. "
                      "Confirmed headroom on core and settlement; pre-scaled and "
                      "briefed bank/PSP partners.")
    else:  # sla
        title = "Weekly SLA & success-rate review"
        owner, chan = org.lead("Operations"), "Bank Coordination"
        body_focus = (f"Success Rate {k.fmt('Success Rate (%)', di)}, Response Time "
                      f"{k.fmt('Response Time (ms)', di)}. Reviewed banks/PSPs below "
                      "the 99.2% floor and agreed follow-ups.")
    mid = f"MTG-D{gd:02d}-REVIEW"
    c.doc(gd, "meetings", f"{mid}.md", mid, "meeting", ops.when(di, 15, 0),
          f"Operational Review — {title}",
          f"""**Meeting ID:** {mid}  ·  **Chair:** {owner.name}  ·  **Channel:** {chan}
**Date:** {k.dates[di].strftime('%A %d %b %Y')}

## Focus
{body_focus}

## KPIs referenced
{kline(k, 'UPI Transactions (M/day)', di)}; {kline(k, 'Success Rate (%)', di)};
{kline(k, 'Merchant Adoption (M)', di)}.

## Action items
- [ ] {ana.name}: circulate the review pack alongside {rep}.
- [ ] {owner.name}: track follow-ups to the next weekly review.""",
          _pad([ops.WB, rep, ops.monitor_id(di)], ops))


def emit_weekly_review(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                       w: int, last_day: int) -> None:
    gd = last_day + 1
    rid = ops.weekly_id(w)
    mid = ops.weekly_mtg_id(w)
    cpo = org.exec_team[0]
    ana = org.lead("Product Analytics")
    wdays = list(range(w * 7, min(w * 7 + 7, ops.days)))
    week_issues = [i for i in k.issues if any(i.active(d) for d in wdays)]
    daily_refs = [ops.report_id(d) for d in wdays]
    inc_refs = [i.inc_id for i in week_issues]

    def wavg(kpi: str) -> str:
        vals = [k.value(kpi, d) for d in wdays]
        return f"{round(sum(vals)/len(vals), 2)}"

    issues_md = ("\n".join(
        f"- {i.inc_id} — {ISSUE_TYPES[i.itype]['label']} on {i.entity_label()} "
        f"({i.severity}); {'RCA ' + i.rca_id if i.rca_id else 'no RCA (short)'}."
        for i in week_issues) or "- No incidents this week — steady state.")

    c.doc(gd, "reports", f"RPT-W{w+1}-review.md", rid, "report", ops.when(last_day, 18, 0),
          f"UPI Products — Week {w+1} Operations Review",
          f"""**Report ID:** {rid}  ·  **Prepared by:** {ana.name}
**Week:** {k.dates[wdays[0]].strftime('%d %b')} - {k.dates[wdays[-1]].strftime('%d %b %Y')}
**Source:** {ops.WB}

## Week in brief
{("A clean week — no incidents, volumes and success tracked in line with the "
  "month's trend.") if not week_issues else
 (f"The week carried {len(week_issues)} incident"
  f"{'s' if len(week_issues) != 1 else ''}"
  f" ({', '.join(sorted({i.entity_label() for i in week_issues}))}); success "
  f"averaged {wavg('Success Rate (%)')}% across the seven days, with the dips "
  "concentrated on the incident days rather than a broad decline.")}

## Week averages
- UPI Transactions: {wavg('UPI Transactions (M/day)')} M/day
- Success Rate: {wavg('Success Rate (%)')}%
- Technical Declines: {wavg('Technical Declines (%)')}%  ·  Business Declines: {wavg('Business Declines (%)')}%
- Customer Complaints: {wavg('Customer Complaints')}/day  ·  Merchant Complaints: {wavg('Merchant Complaints')}/day

## Incidents this week
{issues_md}

## Daily reports
{', '.join(daily_refs)}

## Recommendations
Carry open decisions to the next week; keep coordinating with banks/PSPs below
the success floor.""",
          _pad([ops.WB, *daily_refs[:4], *inc_refs], ops))

    c.doc(gd, "meetings", f"{mid}.md", mid, "meeting", ops.when(last_day, 16, 30),
          f"Weekly Operations Review — Week {w+1}",
          f"""**Meeting ID:** {mid}  ·  **Chair:** {cpo.name}
**Week:** {k.dates[wdays[0]].strftime('%d %b')} - {k.dates[wdays[-1]].strftime('%d %b %Y')}

## Discussion
Reviewed {rid}: {len(week_issues)} incident(s), week averages above. Success Rate
ended the week at {k.fmt('Success Rate (%)', last_day)}.

## Action items
- [ ] Owners to close out open RCAs/decisions from the week.
- [ ] {ana.name}: roll figures into the monthly close ({ops.MONTHLY}).""",
          _pad([rid, ops.WB, ops.MONTHLY, *inc_refs], ops))


def emit_monthly_close(c: Corpus, org: Org, k: TransactionEngine, ops: Ops) -> None:
    last = ops.days - 1
    gd = last + 1
    cpo = org.exec_team[0]
    svp = org.exec_team[1]
    ana = org.lead("Product Analytics")
    weeks = -(-ops.days // 7)
    weekly_refs = [ops.weekly_id(w) for w in range(weeks)]
    inc_refs = [i.inc_id for i in k.issues]
    rca_refs = [i.rca_id for i in k.issues if i.rca_id]

    def mline(kpi: str) -> str:
        dm = k.delta_month(kpi, last)
        arrow = "" if dm in (None, 0) else f" ({'▲' if dm > 0 else '▼'}{abs(dm)} m/m)"
        return f"- **{kpi.split(' (')[0]}:** {k.fmt(kpi, last)}{arrow}"

    kpi_lines = "\n".join(mline(kpi) for kpi in k.names())
    inc_md = "\n".join(
        f"- {i.inc_id} (day {i.start+1}) — {ISSUE_TYPES[i.itype]['label']} on "
        f"{i.entity_label()}; {'resolved, RCA ' + i.rca_id if i.rca_id else 'resolved (short)'}."
        for i in k.issues)

    # Monthly executive report
    c.doc(gd, "reports", "RPT-MONTHLY-exec.md", ops.MONTHLY, "report",
          ops.when(last, 18, 30),
          f"UPI Products — Monthly Executive Report ({k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')})",
          f"""**Report ID:** {ops.MONTHLY}  ·  **Prepared by:** {ana.name}  ·  **For:** {cpo.name}
**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')} ({ops.days} days)
**Source:** {ops.WB}

## Month in one line
UPI Transactions grew to {k.fmt('UPI Transactions (M/day)', last)} M/day while
Success Rate held at {k.fmt('Success Rate (%)', last)}; {len(k.issues)} operational
incidents were detected and resolved.

## KPIs (month close · vs month start)
{kpi_lines}

## Incidents this month
{inc_md}

## Weekly reviews
{', '.join(weekly_refs)}

## Outlook
Continue the resilience, capacity and decline-reduction programmes; no product
launches planned — the focus is operating the existing UPI stack reliably.""",
          _pad([ops.WB, *weekly_refs, *rca_refs[:3], *inc_refs[:2]], ops))

    # Executive review meeting
    c.doc(gd, "meetings", "MTG-MONTHLY-EXEC.md", "MTG-MONTHLY-EXEC", "meeting",
          ops.when(last, 17, 0), "Monthly Executive Review",
          f"""**Meeting ID:** MTG-MONTHLY-EXEC  ·  **Chair:** {cpo.name}
**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}

## Discussion
Reviewed {ops.MONTHLY}. {len(k.issues)} incidents, all resolved; Success Rate
closed at {k.fmt('Success Rate (%)', last)}, Risk Score {k.fmt('Risk Score', last)}.

## Decisions
- Approve continuation of the resilience programme informed by this month's RCAs.

## Action items
- [ ] {svp.name}: brief the board using {ops.MONTHLY}.""",
          _pad([ops.MONTHLY, ops.WB, *weekly_refs[-1:], *rca_refs[:2]], ops))

    # Board review + a monthly decision
    c.doc(gd, "meetings", "MTG-MONTHLY-BOARD.md", "MTG-MONTHLY-BOARD", "meeting",
          ops.when(last, 19, 0), "Board Review — UPI Products Monthly",
          f"""**Meeting ID:** MTG-MONTHLY-BOARD  ·  **Chair:** {cpo.name}
**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}

## Summary presented
{ops.MONTHLY}: volume {k.fmt('UPI Transactions (M/day)', last)} M/day, Success Rate
{k.fmt('Success Rate (%)', last)}, Merchant Adoption {k.fmt('Merchant Adoption (M)', last)}M.

## Board asks
- Maintain reliability posture; continue coordinated bank/PSP resilience work.""",
          _pad([ops.MONTHLY, "MTG-MONTHLY-EXEC", ops.WB], ops))

    c.doc(gd, "decisions", "DEC-MONTHLY-01.md", "DEC-MONTHLY-01", "decision",
          ops.when(last, 19, 30), "Decision — Continue resilience & capacity programmes",
          f"""**Decision ID:** DEC-MONTHLY-01  ·  **Owner:** {cpo.name}  ·  **Status:** Approved

## Decision
Continue the resilience, capacity-planning and decline-reduction programmes into
next month, prioritising the failure modes seen in this month's incidents.

## Rationale
Informed by {ops.MONTHLY} and the month's RCAs. No new products; operate the
existing UPI stack more reliably.""",
          _pad([ops.MONTHLY, "MTG-MONTHLY-EXEC", *rca_refs[:2]], ops))


# ===========================================================================
# Day driver.
# ===========================================================================
def build_days(c: Corpus, org: Org, k: TransactionEngine, ops: Ops) -> None:
    review_days = _pick_review_days(k, ops)
    for di in range(ops.days):
        # incident lifecycle
        for iss in k.issues_opening(di):
            emit_issue_open(c, org, k, ops, iss)
        for iss in k.issues:
            if iss.start + 1 == di:
                emit_issue_midlife(c, org, k, ops, iss)
        for iss in k.issues_recovering(di):
            if iss.duration >= 2:
                emit_issue_recovery(c, org, k, ops, iss)
        # non-incident operational reviews on quiet days
        if di in review_days:
            emit_operational_review(c, org, k, ops, di, review_days[di])
        # routine daily
        mon = emit_monitoring(c, org, k, ops, di)
        emit_daily_report(c, org, k, ops, di, mon)
        build_daily_workbook(c, org, k, ops, di)
        # weekly review on the last day of each 7-day block
        if (di + 1) % 7 == 0 or di == ops.days - 1:
            w = di // 7
            if di == w * 7 + 6 or di == ops.days - 1:
                emit_weekly_review(c, org, k, ops, w, di)
    emit_monthly_close(c, org, k, ops)


def _pick_review_days(k: TransactionEngine, ops: Ops) -> dict[int, str]:
    """Choose a few quiet, incident-free days for operational reviews."""
    out: dict[int, str] = {}
    quiet = [d for d in range(ops.days) if not k.issues_active(d)
             and (d + 1) % 7 != 0]
    kinds = ["adoption", "capacity", "sla"]
    # capacity review the day before a campaign day if it is quiet
    for d in sorted(k.campaign_days):
        if d - 1 in quiet and d - 1 not in out:
            out[d - 1] = "capacity"
    for i, d in enumerate(quiet):
        if d in out:
            continue
        if len(out) >= 5:
            break
        if k.dates[d].weekday() < 5 and i % 3 == 0:
            out[d] = kinds[len(out) % len(kinds)]
    return out


# ===========================================================================
# V7.0 — transaction ledger, aggregate cubes, trend & BI engines.
# ===========================================================================
import csv as _csvmod  # noqa: E402
import math as _math   # noqa: E402

HOURS = list(range(24))
# intraday shape: quiet overnight, morning ramp, midday + evening peaks.
HOURLY_WEIGHTS = [0.6, 0.4, 0.3, 0.2, 0.2, 0.3, 0.7, 1.2, 2.0, 3.0, 4.2, 5.0,
                  5.4, 4.8, 3.9, 3.6, 3.8, 4.4, 5.6, 6.2, 5.4, 4.0, 2.4, 1.3]
# per-feature month-long growth (end vs start) — makes "fastest growing" real.
FEATURE_GROWTH = {
    "Person to Merchant": 0.08, "Person to Person": -0.05, "QR Payments": 0.15,
    "Collect Requests": -0.10, "Intent Payments": 0.05, "UPI Lite": 0.35,
    "UPI Lite X": 0.90, "UPI Autopay": 0.40, "UPI Credit Line": 0.70,
    "RuPay Credit on UPI": 0.60, "UPI International": 0.50,
}

LEDGER_FIELDS = [
    "txn_id", "timestamp", "date", "hour", "day", "week", "month",
    "feature", "payment_type", "amount_inr", "status", "failure_reason",
    "response_code", "issuer_bank", "beneficiary_bank", "payer_psp",
    "payee_psp", "merchant_id", "merchant", "merchant_category",
    "customer_id", "customer_profile", "device", "channel", "city", "state",
    "latency_ms", "processing_ms",
]

# Features whose payee is a merchant (vs person-to-person style flows).
_MERCHANT_FEATURES = {"Person to Merchant", "QR Payments", "UPI Lite",
                      "UPI Lite X", "UPI Autopay", "UPI Credit Line",
                      "RuPay Credit on UPI"}


class Ledger:
    """Samples ~size transactions/day from the behaviour models, reconciled to
    the engine's daily success/decline rates, and rolls the sample up into the
    aggregate cubes that make the corpus analysable. Deterministic."""

    def __init__(self, org: Org, k: TransactionEngine, ops: Ops,
                 rng: random.Random, size: int = 10000):
        self.org = org
        self.k = k
        self.ops = ops
        self.rng = rng
        self.size = size
        self.cubes: dict[str, list] = {}

    def build(self, out: Path) -> dict[str, list]:
        rng, org, k = self.rng, self.org, self.k
        days = k.days
        bank_names = [b["name"] for b in org.banks]
        bank_w = [b["weight"] for b in org.banks]
        psp_names = [p["name"] for p in org.psps]
        psp_w = [p["weight"] for p in org.psps]
        feat_names = [f[0] for f in FEATURES]
        base_share = [f[2] for f in FEATURES]
        merch_by_psp: dict[str, list] = {}
        for m in org.merchants:
            merch_by_psp.setdefault(m["psp"], []).append(m)
        merch_names = [m["name"] for m in org.merchants]
        merch_w = [m["weight"] for m in org.merchants]
        merch_by_name = {m["name"]: m for m in org.merchants}
        dev_names = [d for d, _w in DEVICE_TYPES]
        dev_w = [w for _d, w in DEVICE_TYPES]
        chan_names = [c for c, _w in CHANNELS]
        chan_w = [w for _c, w in CHANNELS]

        # cube accumulators
        daily_metrics: list[dict] = []
        feature_daily: dict[tuple, dict] = {}
        bank_daily: dict[tuple, dict] = {}
        psp_daily: dict[tuple, dict] = {}
        merchant_daily: dict[tuple, dict] = {}
        city_daily: dict[tuple, dict] = {}
        hourly_month: dict[int, int] = {h: 0 for h in HOURS}
        mix_month: dict[str, dict] = {}
        customer_activity: list[dict] = []
        seen_customers: set[str] = set()

        for d in range(days):
            # feature share drifts across the horizon, compounding month over
            # month (damped) so six months of mix-shift accumulates naturally.
            share = [base_share[i] * ((1 + FEATURE_GROWTH.get(feat_names[i], 0.0)
                                       * 0.6) ** (d / 30.0))
                     for i in range(len(feat_names))]

            # Scale the daily sample by the engine's volume series (month
            # growth + archetype) so per-bank/PSP/city volumes grow month over
            # month, not just the feature mix.
            vol_ratio = (k.value("UPI Transactions (M/day)", d)
                         / k.value("UPI Transactions (M/day)", 0))
            N = max(1200, int(self.size * vol_ratio))
            # Reconcile to the engine: n_success is driven directly by the
            # engine Success Rate, and the failures are split into technical /
            # business / pending in proportion to the engine's decline mix — so
            # the ledger's success rate equals the workbook's (± rounding).
            sr = k.value("Success Rate (%)", d)
            td = k.value("Technical Declines (%)", d)
            bd = k.value("Business Declines (%)", d)
            n_success = int(round(N * sr / 100))
            fails = max(0, N - n_success)
            wsum = td + bd + 0.03
            n_tech = int(round(fails * td / wsum)) if wsum else 0
            n_biz = int(round(fails * bd / wsum)) if wsum else 0
            n_pending = max(0, fails - n_tech - n_biz)

            feats = rng.choices(feat_names, weights=share, k=N)
            custs = rng.choices(org.customers, k=N)
            issuers = rng.choices(bank_names, weights=bank_w, k=N)
            benefs = rng.choices(bank_names, weights=bank_w, k=N)
            payer_batch = rng.choices(psp_names, weights=psp_w, k=N)
            hours = rng.choices(HOURS, weights=HOURLY_WEIGHTS, k=N)
            devs = rng.choices(dev_names, weights=dev_w, k=N)
            chans = rng.choices(chan_names, weights=chan_w, k=N)

            # which entities are impaired today (from the active issues)
            active = k.issues_active(d)
            issue_banks = {i.bank["name"] for i in active if i.bank}
            issue_psps = {i.psp["name"] for i in active if i.psp}
            issue_feats = {i.feature[0] for i in active if i.feature}
            fraud_feats = {i.feature[0] for i in active
                           if i.itype == "fraud_spike" and i.feature}
            base_lat = k.value("Response Time (ms)", d)

            # failure propensities
            tech_key = [0.0] * N
            biz_key = [0.0] * N
            for i in range(N):
                tw = 1.0
                if issuers[i] in issue_banks or benefs[i] in issue_banks:
                    tw += 6.0
                if payer_batch[i] in issue_psps:
                    tw += 4.0
                if feats[i] in issue_feats:
                    tw += 3.0
                tw += max(0.0, 99.5 - k.bank_success[issuers[i]][d])
                tech_key[i] = rng.random() ** (1.0 / tw)
                bw = 1.0 + (3.0 if feats[i] in fraud_feats else 0.0)
                biz_key[i] = rng.random() ** (1.0 / bw)

            order_tech = sorted(range(N), key=lambda i: tech_key[i], reverse=True)
            tech_set = set(order_tech[:n_tech])
            rem = [i for i in order_tech[n_tech:]]
            rem.sort(key=lambda i: biz_key[i], reverse=True)
            biz_set = set(rem[:n_biz])
            pending_set = set(rem[n_biz:n_biz + n_pending])

            date = k.dates[d]
            week = d // 7 + 1
            rows: list[list] = []
            dm = {"txns": 0, "value": 0.0}
            for i in range(N):
                feat = feats[i]
                cust = custs[i]
                payer = cust["pref_psp"] if rng.random() < 0.55 else payer_batch[i]
                is_merch = feat in _MERCHANT_FEATURES
                if is_merch:
                    pool = merch_by_psp.get(payer) or org.merchants
                    m = rng.choice(pool)
                    payee = m["psp"]
                    # ticket is driven by the FEATURE (so Lite stays low-value,
                    # Credit high-value), scaled by merchant size.
                    size_factor = {"Large": 1.3, "Mid": 1.0,
                                   "Small": 0.75}.get(m.get("size"), 1.0)
                    base_amt = FEATURE_TICKET.get(feat, 500) * size_factor
                    mid, mname, mcat = m["merchant_id"], m["name"], m["category"]
                else:
                    m = None
                    payee = rng.choice([p for p in psp_names if p != payer] or psp_names)
                    base_amt = FEATURE_TICKET.get(feat, 500)
                    mid = mname = mcat = ""
                amount = max(1, int(base_amt * rng.lognormvariate(0.0, 0.55)))
                if i in tech_set:
                    status = "FAILED"
                    reason, code = rng.choice(TECH_FAIL_REASONS)
                    kind = "TECHNICAL"
                elif i in biz_set:
                    status = "FAILED"
                    reason, code = rng.choice(BIZ_FAIL_REASONS)
                    kind = "BUSINESS"
                elif i in pending_set:
                    status, kind = "PENDING", "PENDING"
                    reason, code = PENDING_REASON
                else:
                    status, kind = "SUCCESS", "SUCCESS"
                    reason, code = "", "00"
                lat = int(base_lat * rng.uniform(0.45, 1.5)
                          * (2.4 if kind == "TECHNICAL" else 1.0))
                proc = int(lat * rng.uniform(0.4, 0.8))
                hh = hours[i]
                ts = datetime.combine(date, time(hh, rng.randint(0, 59),
                                                 rng.randint(0, 59)))
                city, state = cust["city"], cust["state"]
                rows.append([
                    f"UPI{k.year}{d+1:02d}{i:05d}", ts.isoformat(),
                    date.isoformat(), hh, d + 1, week, date.strftime("%b"),
                    feat, PAYMENT_TYPE_BY_FEATURE.get(feat, "P2M"), amount,
                    status, reason, code, issuers[i], benefs[i], payer, payee,
                    mid, mname, mcat, cust["customer_id"], cust["profile"],
                    devs[i], chans[i], city, state, lat, proc,
                ])
                # cube rollups
                dm["txns"] += 1
                dm["value"] += amount
                succ = 1 if status == "SUCCESS" else 0
                dnum = d + 1  # cubes use 1-based day, matching daily_metrics
                fk = (feat, dnum)
                fc = feature_daily.setdefault(fk, {"txns": 0, "value": 0.0, "succ": 0})
                fc["txns"] += 1; fc["value"] += amount; fc["succ"] += succ
                bk = (issuers[i], dnum)
                bc = bank_daily.setdefault(bk, {"txns": 0, "value": 0.0, "succ": 0})
                bc["txns"] += 1; bc["value"] += amount; bc["succ"] += succ
                pk = (payer, dnum)
                pc = psp_daily.setdefault(pk, {"txns": 0, "value": 0.0, "succ": 0})
                pc["txns"] += 1; pc["value"] += amount; pc["succ"] += succ
                if mname:
                    mk = (mname, dnum)
                    mc = merchant_daily.setdefault(
                        mk, {"txns": 0, "value": 0.0, "succ": 0, "category": mcat})
                    mc["txns"] += 1; mc["value"] += amount; mc["succ"] += succ
                ck = (city, dnum)
                cc = city_daily.setdefault(ck, {"txns": 0, "value": 0.0, "state": state})
                cc["txns"] += 1; cc["value"] += amount
                hourly_month[hh] += 1
                pt = PAYMENT_TYPE_BY_FEATURE.get(feat, "P2M")
                mm = mix_month.setdefault(pt, {"txns": 0, "value": 0.0})
                mm["txns"] += 1; mm["value"] += amount
                seen_customers.add(cust["customer_id"])

            # write the per-day ledger CSV (data — not ingested/embedded)
            lpath = out / f"day_{d+1:02d}" / "ledger" / f"txns_day_{d+1:02d}.csv"
            lpath.parent.mkdir(parents=True, exist_ok=True)
            with lpath.open("w", newline="", encoding="utf-8") as f:
                w = _csvmod.writer(f)
                w.writerow(LEDGER_FIELDS)
                w.writerows(rows)

            # per-day active customers
            day_customers = {r[20] for r in rows}
            peak_hour = max(HOURS, key=lambda h: sum(1 for r in rows if r[3] == h))
            daily_metrics.append({
                "day": d + 1, "date": date.isoformat(),
                "archetype": k.archetype[d],
                "sample_txns": dm["txns"],
                "sample_value_inr": round(dm["value"], 0),
                "avg_ticket_inr": round(dm["value"] / max(1, dm["txns"]), 1),
                "success_rate": round(100 * sum(1 for r in rows if r[10] == "SUCCESS")
                                      / max(1, len(rows)), 3),
                "technical_decline_pct": round(100 * n_tech / max(1, N), 3),
                "business_decline_pct": round(100 * n_biz / max(1, N), 3),
                "pending_pct": round(100 * len(pending_set) / max(1, N), 3),
                "peak_hour": peak_hour,
                # the true (engine) scale, for reference / dashboards
                "volume_millions": k.value("UPI Transactions (M/day)", d),
                "active_customers_sample": len(day_customers),
            })
            customer_activity.append({
                "day": d + 1, "date": date.isoformat(),
                "active_customers_sample": len(day_customers),
                "cumulative_customers_seen": len(seen_customers),
                "avg_txns_per_active": round(dm["txns"] / max(1, len(day_customers)), 2),
            })

        self.cubes = {
            "daily_metrics": daily_metrics,
            "feature_daily": self._flatten(feature_daily, ["feature", "day"]),
            "bank_daily": self._flatten(bank_daily, ["bank", "day"]),
            "psp_daily": self._flatten(psp_daily, ["psp", "day"]),
            "merchant_daily": self._flatten(merchant_daily, ["merchant", "day"]),
            "city_daily": self._flatten(city_daily, ["city", "day"]),
            "hourly_distribution": [{"hour": h, "sample_txns": hourly_month[h]}
                                    for h in HOURS],
            "transaction_mix": [{"payment_type": pt, "sample_txns": v["txns"],
                                 "sample_value_inr": round(v["value"], 0)}
                                for pt, v in sorted(mix_month.items(),
                                                    key=lambda kv: -kv[1]["txns"])],
            "customer_activity": customer_activity,
        }
        return self.cubes

    @staticmethod
    def _flatten(cube: dict[tuple, dict], keys: list[str]) -> list[dict]:
        rows = []
        for kt, vals in cube.items():
            row = dict(zip(keys, kt))
            for kk, vv in vals.items():
                row[kk] = round(vv, 1) if isinstance(vv, float) else vv
            if "succ" in row and "txns" in row:
                row["success_rate"] = round(100 * row["succ"] / max(1, row["txns"]), 2)
                del row["succ"]
            rows.append(row)
        return rows


# ---------------------------------------------------------------------------
# Trend engine + business-intelligence layer (computed from the cubes).
# ---------------------------------------------------------------------------
def _series_from(cube: list[dict], key: str, entity: str, value: str,
                 days: int) -> list[float]:
    s = [0.0] * days
    for r in cube:
        if str(r.get(key)) == str(entity):
            di = int(r["day"]) - 1
            if 0 <= di < days:
                s[di] = float(r.get(value, 0) or 0)
    return s


def _trend_row(name: str, series: list[float]) -> dict:
    n = len(series)
    today = series[-1] if n else 0.0
    yest = series[-2] if n > 1 else None
    last7 = series[-8] if n > 7 else (series[0] if n else None)
    last30 = series[0] if n else None
    ma7 = round(sum(series[-7:]) / min(7, n), 2) if n else 0.0
    ma_all = round(sum(series) / n, 2) if n else 0.0
    wow = None
    if n >= 14:
        wow = round((sum(series[-7:]) / 7) - (sum(series[-14:-7]) / 7), 2)
    mtd = round(sum(series), 2)
    # growth: first-week vs last-week average (smooths day-of-week/archetype
    # noise); falls back to today-vs-start for short series.
    growth = None
    if n >= 14:
        first_avg = sum(series[:7]) / 7
        last_avg = sum(series[-7:]) / 7
        if first_avg:
            growth = round(100 * (last_avg - first_avg) / abs(first_avg), 1)
    elif last30 not in (None, 0):
        growth = round(100 * (today - last30) / abs(last30), 1)
    # forecast: last value + average daily delta over the last 7 days
    if n >= 8:
        deltas = [series[i] - series[i - 1] for i in range(n - 7, n)]
        step = sum(deltas) / len(deltas)
    elif n >= 2:
        step = series[-1] - series[-2]
    else:
        step = 0.0
    fc_next = round(today + step, 2)
    fc_7d = round(today + step * 7, 2)
    return {"series": name, "today": round(today, 2),
            "yesterday": None if yest is None else round(yest, 2),
            "last_7d": None if last7 is None else round(last7, 2),
            "last_30d": None if last30 is None else round(last30, 2),
            "wow_change": wow, "mtd": mtd, "ma_7d": ma7, "ma_all": ma_all,
            "growth_pct": growth, "forecast_next": fc_next, "forecast_7d": fc_7d}


def build_trends(cubes: dict[str, list], k: TransactionEngine) -> list[dict]:
    days = k.days
    rows: list[dict] = []
    dm = cubes["daily_metrics"]
    for metric in ("sample_txns", "sample_value_inr", "success_rate",
                   "avg_ticket_inr"):
        rows.append(_trend_row(f"total::{metric}",
                               [float(r[metric]) for r in dm]))
    for feat, _t, _s in FEATURES:
        rows.append(_trend_row(
            f"feature::{feat}",
            _series_from(cubes["feature_daily"], "feature", feat, "txns", days)))
    for b in sorted({r["bank"] for r in cubes["bank_daily"]}):
        rows.append(_trend_row(
            f"bank::{b}",
            _series_from(cubes["bank_daily"], "bank", b, "txns", days)))
    for p in sorted({r["psp"] for r in cubes["psp_daily"]}):
        rows.append(_trend_row(
            f"psp::{p}",
            _series_from(cubes["psp_daily"], "psp", p, "txns", days)))
    for cty in sorted({r["city"] for r in cubes["city_daily"]}):
        rows.append(_trend_row(
            f"city::{cty}",
            _series_from(cubes["city_daily"], "city", cty, "txns", days)))
    return rows


def build_bi(cubes: dict[str, list], trends: list[dict],
             k: TransactionEngine) -> list[dict]:
    findings: list[dict] = []
    by_series = {t["series"]: t for t in trends}

    def growth_of(prefix: str) -> list[tuple[str, float]]:
        out = [(t["series"].split("::", 1)[1], t["growth_pct"])
               for t in trends if t["series"].startswith(prefix)
               and t["growth_pct"] is not None]
        out.sort(key=lambda x: x[1], reverse=True)
        return out

    feats = growth_of("feature::")
    if feats:
        findings.append({"category": "growing_features", "severity": "info",
                         "finding": f"Fastest-growing feature: {feats[0][0]} "
                         f"({feats[0][1]:+}% m/m).",
                         "entity": feats[0][0], "metric": "txns",
                         "value": feats[0][1]})
        findings.append({"category": "declining_features", "severity": "watch",
                         "finding": f"Weakest feature: {feats[-1][0]} "
                         f"({feats[-1][1]}% m/m).",
                         "entity": feats[-1][0], "metric": "txns",
                         "value": feats[-1][1]})
    banks = growth_of("bank::")
    if banks:
        findings.append({"category": "fastest_growing_bank", "severity": "info",
                         "finding": f"Fastest-growing bank by volume: {banks[0][0]} "
                         f"({banks[0][1]:+}%).", "entity": banks[0][0],
                         "metric": "txns", "value": banks[0][1]})
    psps = growth_of("psp::")
    if psps:
        findings.append({"category": "psp_share_loss", "severity": "watch",
                         "finding": f"PSP losing share: {psps[-1][0]} "
                         f"({psps[-1][1]}% m/m).", "entity": psps[-1][0],
                         "metric": "txns", "value": psps[-1][1]})
    # high-risk banks: lowest average success rate
    bank_sr: dict[str, list] = {}
    for r in cubes["bank_daily"]:
        bank_sr.setdefault(r["bank"], []).append(r.get("success_rate", 100))
    risk = sorted(((b, round(sum(v) / len(v), 2)) for b, v in bank_sr.items()),
                  key=lambda x: x[1])[:3]
    for b, srv in risk:
        findings.append({"category": "high_risk_bank", "severity": "high"
                         if srv < 98.8 else "watch",
                         "finding": f"{b} lowest avg success ({srv}%).",
                         "entity": b, "metric": "success_rate", "value": srv})
    # transaction/usage anomalies: z-score of daily success rate
    dm = [float(r["success_rate"]) for r in cubes["daily_metrics"]]
    if len(dm) >= 7:
        mean = sum(dm) / len(dm)
        var = sum((x - mean) ** 2 for x in dm) / len(dm)
        sd = _math.sqrt(var) or 1.0
        for i, x in enumerate(dm):
            z = (x - mean) / sd
            if z < -2.0:
                findings.append({"category": "anomaly", "severity": "high",
                                 "finding": f"Success-rate anomaly on day {i+1} "
                                 f"({x}%, z={round(z,1)}).",
                                 "entity": f"day {i+1}", "metric": "success_rate",
                                 "value": x})
    # regional/city growth leader
    cities = {}
    for r in cubes["city_daily"]:
        cities.setdefault(r["city"], [0.0] * k.days)
        cities[r["city"]][int(r["day"]) - 1] = float(r["txns"])
    cg = sorted(((c, round(100 * (s[-1] - s[0]) / max(1, s[0]), 1))
                 for c, s in cities.items()), key=lambda x: x[1], reverse=True)
    if cg:
        findings.append({"category": "regional_growth", "severity": "info",
                         "finding": f"Fastest-growing city: {cg[0][0]} ({cg[0][1]:+}%).",
                         "entity": cg[0][0], "metric": "txns", "value": cg[0][1]})
    return findings


# ===========================================================================
# Excel workbooks.
# ===========================================================================
def _style_header(ws) -> None:
    fill = PatternFill("solid", fgColor="1F4E79")
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = fill


def build_master_workbook(c: Corpus, org: Org, k: TransactionEngine, ops: Ops) -> None:
    """The monthly KPI workbook — every report and email reads from this."""
    if not _XLSX:
        return
    refs = [i.inc_id for i in k.issues[:4]]
    path = c.raw(None, "", ops.WB, ops.WB, "workbook", ops.when(ops.days - 1, 9, 0),
                 [*refs, ops.MONTHLY])
    wb = openpyxl.Workbook()

    ws = wb.active
    ws.title = "Monthly KPIs"
    day_labels = [k.dates[i].strftime('%d-%b') for i in range(ops.days)]
    ws.append(["KPI", "Unit", *day_labels])
    for kpi in k.names():
        ws.append([kpi, KPI_UNITS[kpi], *[k.value(kpi, d) for d in range(ops.days)]])
    _style_header(ws)
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 26

    flags = k.weekly_flags()
    weeks = -(-ops.days // 7)

    wsb = wb.create_sheet("Bank Performance")
    wsb.append(["Week", "Bank", "Tier", "Region", "Success %", "Txns (M/day)",
                "Incident bank"])
    for w in range(weeks):
        wd = min(w * 7 + 6, ops.days - 1)
        fset = flags.get(w, {}).get("banks", set())
        for b in org.banks:
            wsb.append([f"Week {w+1}", b["name"], b["tier"], b["region"],
                        k.bank_success[b["name"]][wd], k.bank_txns[b["name"]][wd],
                        "YES" if b["name"] in fset else ""])
    _style_header(wsb)
    wsb.column_dimensions["B"].width = 24

    wsp = wb.create_sheet("PSP Performance")
    wsp.append(["Week", "PSP", "Sponsor bank", "Success %", "Callback p95 (ms)",
                "Incident PSP"])
    for w in range(weeks):
        wd = min(w * 7 + 6, ops.days - 1)
        fset = flags.get(w, {}).get("psps", set())
        for p in org.psps:
            wsp.append([f"Week {w+1}", p["name"], p["sponsor_bank"],
                        k.psp_success[p["name"]][wd], k.psp_p95[p["name"]][wd],
                        "YES" if p["name"] in fset else ""])
    _style_header(wsp)
    wsp.column_dimensions["B"].width = 18

    wsm = wb.create_sheet("Merchant KPIs")
    wsm.append(["Week", "Merchant", "Category", "Region", "PSP", "Settlement bank",
                "Monthly GMV (Cr)", "Affected this week"])
    for w in range(weeks):
        fset = flags.get(w, {}).get("merchants", set())
        for m in org.merchants:
            wsm.append([f"Week {w+1}", m["name"], m["category"], m["region"],
                        m["psp"], m["settlement_bank"], m["monthly_gmv_cr"],
                        "YES" if m["name"] in fset else ""])
    _style_header(wsm)
    wsm.column_dimensions["B"].width = 20

    # Feature volume sheet (extra, for richer analysis)
    wsf = wb.create_sheet("Feature Volume")
    wsf.append(["Feature", "Owning squad", *day_labels])
    for name, team, _share in FEATURES:
        wsf.append([name, team, *k.feature_vol[name]])
    _style_header(wsf)
    wsf.column_dimensions["A"].width = 22

    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def build_daily_workbook(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                         di: int) -> None:
    if not _XLSX:
        return
    gd = di + 1
    art_id = f"KPI-D{gd:02d}"
    path = c.raw(gd, "excel", f"upi_kpis_day_{gd:02d}.xlsx", art_id, "workbook",
                 ops.when(di, 17, 0), [ops.WB, ops.report_id(di)])
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Daily KPIs"
    ws.append(["KPI", "Unit", k.dates[di].strftime('%d %b %Y'),
               "Delta vs prev day", "Delta vs last week"])
    for kpi in k.names():
        d = k.delta(kpi, di)
        dw = k.delta_week_over_week(kpi, di)
        ws.append([kpi, KPI_UNITS[kpi], k.value(kpi, di),
                   "" if d is None else d, "" if dw is None else dw])
    _style_header(ws)
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 26

    mtd = wb.create_sheet("Month to Date")
    mtd.append(["KPI", *[k.dates[i].strftime('%d-%b') for i in range(di + 1)]])
    for kpi in k.names():
        mtd.append([kpi, *[k.value(kpi, d) for d in range(di + 1)]])
    _style_header(mtd)
    mtd.column_dimensions["A"].width = 30
    wb.save(path)


# ===========================================================================
# Master data — CSV reference tables + an org overview document.
# ===========================================================================
def _csv(path: Path, header: list[str], rows: list[list]) -> None:
    import csv
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(header)
        wr.writerows(rows)


def build_master(c: Corpus, org: Org, k: TransactionEngine, ops: Ops) -> None:
    m = c.out / "master"
    m.mkdir(parents=True, exist_ok=True)

    _csv(m / "employees.csv",
         ["emp_id", "name", "title", "team", "email", "office", "region",
          "manager_id"],
         [[p.emp_id, p.name, p.title, p.team, p.email, p.office, p.region,
           p.manager] for p in org.people])
    _csv(m / "teams.csv", ["team", "lead_emp_id", "lead_name", "headcount"],
         [[t, org.lead(t).emp_id, org.lead(t).name, len(org.by_team[t])]
          for t in TEAMS])
    _csv(m / "products.csv",
         ["product_id", "name", "team", "owner_emp_id", "owner_name",
          "description"],
         [[p["product_id"], p["name"], p["team"], p["owner"], p["owner_name"],
           p["description"]] for p in org.products])
    _csv(m / "features.csv", ["feature", "owning_team", "volume_share"],
         [[name, team, share] for name, team, share in FEATURES])
    _csv(m / "merchants.csv",
         ["merchant_id", "name", "category", "region", "psp",
          "settlement_bank", "monthly_gmv_cr"],
         [[x["merchant_id"], x["name"], x["category"], x["region"], x["psp"],
           x["settlement_bank"], x["monthly_gmv_cr"]] for x in org.merchants])
    _csv(m / "banks.csv", ["bank_id", "name", "ifsc_prefix", "region", "tier"],
         [[b["bank_id"], b["name"], b["ifsc_prefix"], b["region"], b["tier"]]
          for b in org.banks])
    _csv(m / "psps.csv", ["psp_id", "name", "sponsor_bank"],
         [[p["psp_id"], p["name"], p["sponsor_bank"]] for p in org.psps])
    _csv(m / "customers.csv",
         ["customer_id", "profile", "city", "state", "region", "pref_psp",
          "pref_bank", "pref_feature", "txn_freq", "avg_ticket", "device"],
         [[x["customer_id"], x["profile"], x["city"], x["state"], x["region"],
           x["pref_psp"], x["pref_bank"], x["pref_feature"], x["txn_freq"],
           x["avg_ticket"], x["device"]] for x in org.customers])
    _csv(m / "cities.csv", ["city", "state", "weight"],
         [[c, s, w] for c, s, w in CITIES])
    _csv(m / "regions.csv", ["region"], [[r] for r in REGIONS])
    _csv(m / "offices.csv", ["office", "city", "region"],
         [[o[0], o[1], o[2]] for o in OFFICES])
    _csv(m / "distribution_lists.csv", ["address", "description"],
         [[d[0], d[1]] for d in DISTRIBUTION_LISTS])
    _csv(m / "teams_channels.csv", ["team", "channel", "purpose"],
         [[t[0], t[1], t[2]] for t in TEAMS_CHANNELS])
    _csv(m / "meeting_rooms.csv", ["room", "location", "capacity"],
         [[r[0], r[1], r[2]] for r in MEETING_ROOMS])
    _csv(m / "projects.csv", ["project_id", "name", "product", "status"],
         [["PROG-UPI-101", "Autopay & Core Resilience", "UPI Autopay", "active"],
          ["PROG-UPI-102", "Settlement Reliability", "Merchant Products", "active"],
          ["PROG-UPI-103", "Decline Reduction", "UPI Core", "active"],
          ["PROG-UPI-104", "Capacity & Peak Readiness", "UPI Core", "active"],
          ["PROG-UPI-105", "Fraud & Risk Hardening", "UPI Credit", "active"]])
    # Reference festival/holiday calendar (broader than the 35-day window).
    _csv(m / "holiday_calendar.csv", ["date", "holiday", "region"],
         [["2026-08-15", "Independence Day", "All"],
          ["2026-08-27", "Ganesh Chaturthi", "West"],
          ["2026-10-02", "Gandhi Jayanti", "All"],
          ["2026-10-20", "Dussehra", "All"],
          ["2026-11-08", "Diwali", "All"]])

    exec_rows = "\n".join(f"- {org.named(p)}" for p in org.exec_team)
    team_rows = "\n".join(
        f"| {t} | {org.lead(t).name} | {len(org.by_team[t])} |" for t in TEAMS)
    inc_rows = "\n".join(
        f"| {i.inc_id} | day {i.start+1} | {ISSUE_TYPES[i.itype]['label']} | "
        f"{i.entity_label()} | {i.severity} |" for i in k.issues)

    c.doc(None, "", "ORG-OVERVIEW.md", ops.OVERVIEW, "product_document",
          ops.when(0, 8, 0), f"{ORG_NAME} — {DEPARTMENT} Organization Overview",
          f"""**Organization:** {ORG_NAME}  ·  **Department:** {DEPARTMENT}
**Headcount:** {len(org.people)}  ·  **Products:** {len(org.products)}  ·  **Teams:** {len(TEAMS)}
**Banks:** {len(org.banks)}  ·  **PSPs:** {len(org.psps)}  ·  **Merchants:** {len(org.merchants)}

## Executive team
{exec_rows}

## Teams
| Team | Lead | Headcount |
|------|------|-----------|
{team_rows}

## This month's operations
{ops.days} continuous days of UPI operations. Enterprise activity is driven by
transaction behaviour; {len(k.issues)} operational incidents were detected and
resolved:

| Incident | Opened | Type | Entity | Severity |
|----------|--------|------|--------|----------|
{inc_rows}

All KPIs are maintained in {ops.WB}; the month is summarised in {ops.MONTHLY}.

## Master data
Employees, teams, products, features, merchants, banks, PSPs, regions, offices,
distribution lists, Teams channels, meeting rooms, programmes and the holiday
calendar are in this folder as CSVs.""",
          _pad([ops.WB, ops.MONTHLY, ops.STORYLINE] +
               [i.inc_id for i in k.issues[:2]], ops))


# ===========================================================================
# V7.0 — write aggregate cubes and emit ingestible analytics/BI/forecast docs.
# ===========================================================================
def write_cubes(out: Path, cubes: dict[str, list], trends: list[dict],
                bi: list[dict], forecasts: list[dict]) -> None:
    a = out / "master" / "analytics"
    a.mkdir(parents=True, exist_ok=True)

    def dump(name: str, rows: list[dict]) -> None:
        if not rows:
            return
        header = list(rows[0].keys())
        _csv(a / f"{name}.csv", header, [[r.get(h, "") for h in header]
                                         for r in rows])

    for name, rows in cubes.items():
        dump(name, rows)
    dump("trends", trends)
    dump("bi_findings", bi)
    dump("forecasts", forecasts)


def _month_totals(cube: list[dict], key: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in cube:
        e = str(r.get(key))
        agg = out.setdefault(e, {"txns": 0.0, "value": 0.0, "sr": [], "cat": r.get("category", "")})
        agg["txns"] += float(r.get("txns", 0) or 0)
        agg["value"] += float(r.get("value", 0) or 0)
        if r.get("success_rate") is not None:
            agg["sr"].append(float(r["success_rate"]))
    return out


def _growth_map(trends: list[dict], prefix: str) -> dict[str, float]:
    return {t["series"].split("::", 1)[1]: (t["growth_pct"] or 0.0)
            for t in trends if t["series"].startswith(prefix)}


def build_forecasts(trends: list[dict]) -> list[dict]:
    keep = {"total::sample_txns", "total::sample_value_inr",
            "total::success_rate", "total::avg_ticket_inr"}
    keep |= {f"feature::{f[0]}" for f in FEATURES}
    return [{"series": t["series"], "today": t["today"],
             "forecast_next": t["forecast_next"], "forecast_7d": t["forecast_7d"],
             "ma_7d": t["ma_7d"], "growth_pct": t["growth_pct"]}
            for t in trends if t["series"] in keep]


# ===========================================================================
# V8.0 — six-month evolution. Entity lifecycle, multi-granularity trends,
# rolling windows, forecast validation (predicted vs realised), executive
# decision tracking (expected vs actual impact), cross-entity relationships and
# weekly storylines. Everything below is DERIVED from the same ledger/KPI ground
# truth the V7.0 cubes use — nothing random-walks on its own — and is emitted as
# flat cubes the executive/ecosystem layer reads exactly like the V7.0 cubes.
# ===========================================================================
def _month_label(d: date) -> str:
    return d.strftime("%b %Y")


def _quarter_label(d: date) -> str:
    return f"{d.year}-Q{(d.month - 1) // 3 + 1}"


def _clampf(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def _lifecycle_stage(growth_pct: float | None, share_pct: float) -> str:
    g = growth_pct if growth_pct is not None else 0.0
    if share_pct < 2.5 and g > 12:
        return "Introduction"
    if g > 8:
        return "Growth"
    if g > 1:
        return "Maturity"
    if g >= -2.5:
        return "Saturation"
    return "Decline"


def _health_grade(score: float) -> str:
    return ("Healthy" if score >= 80 else "Stable" if score >= 65
            else "Watch" if score >= 50 else "At risk")


def _pct_change(a: float, b: float) -> float | None:
    """Percent change from a to b."""
    if a in (0, None):
        return None
    return round(100 * (b - a) / abs(a), 1)


def _forecast_linear(series: list[float], horizon: int,
                     window: int = 14) -> list[float]:
    """Least-squares linear extrapolation over the last `window` points."""
    n = len(series)
    if n == 0:
        return [0.0] * horizon
    w = series[-min(window, n):]
    m = len(w)
    xs = list(range(m))
    mean_x = sum(xs) / m
    mean_y = sum(w) / m
    denom = sum((x - mean_x) ** 2 for x in xs) or 1.0
    slope = sum((xs[i] - mean_x) * (w[i] - mean_y) for i in range(m)) / denom
    intercept = mean_y - slope * mean_x
    return [intercept + slope * (m - 1 + step) for step in range(1, horizon + 1)]


def _stdev(xs: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mean = sum(xs) / n
    return (sum((x - mean) ** 2 for x in xs) / n) ** 0.5


def _mape(actual: list[float], pred: list[float]) -> float:
    pairs = [(a, p) for a, p in zip(actual, pred) if a not in (0, None)]
    if not pairs:
        return 0.0
    return 100 * sum(abs(a - p) / abs(a) for a, p in pairs) / len(pairs)


def _period_day_counts(k: TransactionEngine, label_fn) -> dict[str, int]:
    """Number of days each period label spans within the horizon — so growth is
    compared on a per-day basis and unequal calendar months (a 9-day first month
    vs a 31-day month) don't create phantom swings."""
    out: dict[str, int] = {}
    for d in range(k.days):
        lbl = label_fn(k.dates[d])
        out[lbl] = out.get(lbl, 0) + 1
    return out


def _period_rows(cube: list[dict], entity_key: str, k: TransactionEngine,
                 label_fn) -> dict:
    """Group a *_daily cube by (entity, period-label) → aggregated txns/value/sr,
    preserving period order."""
    per: dict[tuple, dict] = {}
    order: list[str] = []
    for r in cube:
        di = int(r["day"]) - 1
        if not (0 <= di < k.days):
            continue
        lbl = label_fn(k.dates[di])
        if lbl not in order:
            order.append(lbl)
        ent = str(r.get(entity_key))
        agg = per.setdefault((ent, lbl), {"txns": 0.0, "value": 0.0, "sr": [],
                                          "category": r.get("category")})
        agg["txns"] += float(r.get("txns") or 0)
        agg["value"] += float(r.get("value") or 0)
        if r.get("success_rate") is not None:
            agg["sr"].append(float(r["success_rate"]))
    return {"per": per, "order": order}


# ---------------------------------------------------------------- customers
def build_customer_evolution(k: TransactionEngine) -> list[dict]:
    """Daily user-base lifecycle anchored to transaction volume + KPI growth:
    DAU/WAU/MAU, joins/churn/returns, retention, power vs dormant, stickiness."""
    days = k.days
    rows: list[dict] = []
    prev_base = None
    for d in range(days):
        dt = k.dates[d]
        # Registered base follows the SMOOTH compounding growth trend (not the
        # weekend/campaign-modulated daily volume), so it grows monotonically.
        volr = growth_mult("UPI Transactions (M/day)", d)
        prog = d / max(1, days - 1)
        base = 342.0 * (1 + 0.75 * (volr - 1))          # registered base (M)
        engage = 0.60 + 0.06 * prog                     # MAU / base
        dau_mau = 0.34 + 0.045 * prog
        wau_mau = 0.70 + 0.02 * prog
        mau = base * engage
        arch = k._vol_mult[d]                            # weekend / campaign shape
        dau = mau * dau_mau * arch
        wau = mau * wau_mau
        churn_m = 0.11 - 0.04 * prog                     # improves 11% -> 7%
        churned = mau * churn_m / 30.0
        returned = churned * (0.32 + 0.10 * prog)
        d_base = 0.0 if prev_base is None else (base - prev_base)
        new = max(0.0, d_base + churned)
        prev_base = base
        power = mau * (0.13 + 0.02 * prog)
        dormant = max(0.0, base - mau)
        adopters = (k.value("UPI Lite Adoption (M)", d)
                    + k.value("Autopay Registrations (K/day)", d) / 1000.0 * 30)
        rows.append({
            "day": d + 1, "date": dt.isoformat(), "week": d // 7 + 1,
            "month": _month_label(dt),
            "dau_m": round(dau, 2), "wau_m": round(wau, 2), "mau_m": round(mau, 2),
            "registered_base_m": round(base, 2),
            "new_users_k": round(new * 1000, 1),
            "churned_users_k": round(churned * 1000, 1),
            "returned_users_k": round(returned * 1000, 1),
            "retention_pct": round(100 * (1 - churn_m), 2),
            "churn_pct": round(100 * churn_m, 2),
            "power_users_m": round(power, 2),
            "dormant_users_m": round(dormant, 2),
            "stickiness_pct": round(100 * dau / mau, 1) if mau else 0.0,
            "feature_adopters_m": round(adopters, 2),
        })
    return rows


def _base_by_month(cust_evo: list[dict]) -> dict[str, float]:
    """End-of-month registered base per month label (for adoption sizing)."""
    out: dict[str, float] = {}
    for r in cust_evo:
        out[r["month"]] = r["registered_base_m"]
    return out


# ----------------------------------------------------------------- features
def build_feature_adoption(k: TransactionEngine, cubes: dict,
                           base_by_month: dict[str, float]) -> list[dict]:
    grp = _period_rows(cubes["feature_daily"], "feature", k, _month_label)
    per, order = grp["per"], grp["order"]
    pdays = _period_day_counts(k, _month_label)
    month_grand = {m: sum(v["txns"] for (e, mm), v in per.items() if mm == m)
                   for m in order}
    prev: dict[str, float] = {}
    rows: list[dict] = []
    for (feat, m), v in sorted(per.items(), key=lambda kv: (kv[0][0],
                                                            order.index(kv[0][1]))):
        idx = order.index(m)
        share = 100 * v["txns"] / (month_grand[m] or 1)
        avg_daily = v["txns"] / max(1, pdays.get(m, 1))
        mom = _pct_change(prev.get(feat), avg_daily) if feat in prev else None
        prev[feat] = avg_daily
        adopters = base_by_month.get(m, 340.0) * share / 100
        rows.append({
            "feature": feat, "month": m, "month_index": idx + 1,
            "txns": int(v["txns"]), "value_inr": int(v["value"]),
            "avg_ticket_inr": round(v["value"] / (v["txns"] or 1), 0),
            "avg_success_rate": round(sum(v["sr"]) / len(v["sr"]), 2)
            if v["sr"] else None,
            "share_pct": round(share, 2),
            "mom_growth_pct": mom,
            "adopters_m": round(adopters, 2),
            "stage": _lifecycle_stage(mom, share),
        })
    return rows


# ---------------------------------------------------------------- merchants
def build_merchant_evolution(k: TransactionEngine, org: Org,
                             cubes: dict) -> list[dict]:
    by_name = {m["name"]: m for m in org.merchants}
    grp = _period_rows(cubes["merchant_daily"], "merchant", k, _month_label)
    per, order = grp["per"], grp["order"]
    pdays = _period_day_counts(k, _month_label)
    prev: dict[str, float] = {}
    rows: list[dict] = []
    for (name, m), v in sorted(per.items(), key=lambda kv: (kv[0][0],
                                                           order.index(kv[0][1]))):
        idx = order.index(m)
        meta = by_name.get(name, {})
        sr = sum(v["sr"]) / len(v["sr"]) if v["sr"] else 99.0
        avg_daily = v["txns"] / max(1, pdays.get(m, 1))
        mom = _pct_change(prev.get(name), avg_daily) if name in prev else None
        prev[name] = avg_daily
        sr_score = _clampf((sr - 96) / (99.8 - 96) * 100, 0, 100)
        g = mom if mom is not None else 0.0
        growth_score = _clampf(50 + g * 2.5, 0, 100)
        health = round(0.55 * sr_score + 0.30 * growth_score
                       + 0.15 * min(100, v["txns"] / 40), 1)
        refund = float(meta.get("refund_rate", 0.01))
        satisfaction = round(_clampf(sr - refund * 400 + 3, 40, 99), 1)
        if idx == 0:
            stage = "Onboarding"
        elif g > 12:
            stage = "Growing"
        elif g < -12:
            stage = "Declining"
        elif health < 55:
            stage = "At risk"
        else:
            stage = "Mature"
        status = ("Churned" if (mom is not None and mom < -55)
                  else "Declining" if g < -8 else "Active")
        rows.append({
            "merchant": name, "category": meta.get("category", ""),
            "size": meta.get("size", ""), "month": m, "month_index": idx + 1,
            "txns": int(v["txns"]), "value_inr": int(v["value"]),
            "avg_ticket_inr": round(v["value"] / (v["txns"] or 1), 0),
            "avg_success_rate": round(sr, 2),
            "mom_growth_pct": mom,
            "health_score": health, "health_grade": _health_grade(health),
            "lifecycle_stage": stage, "satisfaction": satisfaction,
            "status": status,
        })
    return rows


# ------------------------------------------------------------------- banks
def build_bank_evolution(k: TransactionEngine, org: Org,
                         cubes: dict) -> list[dict]:
    def wk(d: date) -> str:
        return f"W{(d - k.week_start).days // 7 + 1}"
    grp = _period_rows(cubes["bank_daily"], "bank", k, wk)
    per, order = grp["per"], grp["order"]
    pdays = _period_day_counts(k, wk)
    week_grand = {w: sum(v["txns"] for (e, ww), v in per.items() if ww == w)
                  for w in order}
    # incidents per (bank, week)
    inc: dict[tuple, int] = {}
    for iss in k.issues:
        if not iss.bank:
            continue
        for d in range(iss.start, min(iss.end + 1, k.days)):
            key = (iss.bank["name"], wk(k.dates[d]))
            inc[key] = inc.get(key, 0) + 1
    prev: dict[str, float] = {}
    rows: list[dict] = []
    for (name, w), v in sorted(per.items(), key=lambda kv: (kv[0][0],
                                                           order.index(kv[0][1]))):
        idx = order.index(w)
        d_mid = min(idx * 7 + 3, k.days - 1)
        sr = sum(v["sr"]) / len(v["sr"]) if v["sr"] else 99.0
        share = 100 * v["txns"] / (week_grand[w] or 1)
        avg_daily = v["txns"] / max(1, pdays.get(w, 1))
        mom = _pct_change(prev.get(name), avg_daily) if name in prev else None
        prev[name] = avg_daily
        meta = next((b for b in org.banks if b["name"] == name), {})
        p95 = round(k.value("Response Time (ms)", d_mid)
                    * (1 + max(0.0, 99.4 - sr) / 40), 0)
        health = round(_clampf((sr - 96.5) / (99.8 - 96.5) * 100, 0, 100)
                       - inc.get((name, w), 0) * 4, 1)
        rows.append({
            "bank": name, "tier": meta.get("tier", ""), "week": w,
            "week_index": idx + 1,
            "date": k.dates[d_mid].isoformat(),
            "txns": int(v["txns"]), "value_inr": int(v["value"]),
            "market_share_pct": round(share, 2),
            "success_rate": round(sr, 2),
            "p95_latency_ms": int(p95),
            "wow_growth_pct": mom,
            "incidents": inc.get((name, w), 0),
            "health_score": max(0.0, health),
            "health_grade": _health_grade(max(0.0, health)),
        })
    return rows


# -------------------------------------------------------------------- psps
def build_psp_evolution(k: TransactionEngine, org: Org,
                        cubes: dict) -> list[dict]:
    def wk(d: date) -> str:
        return f"W{(d - k.week_start).days // 7 + 1}"
    grp = _period_rows(cubes["psp_daily"], "psp", k, wk)
    per, order = grp["per"], grp["order"]
    pdays = _period_day_counts(k, wk)
    week_grand = {w: sum(v["txns"] for (e, ww), v in per.items() if ww == w)
                  for w in order}
    # weekly share-leader per week
    leader: dict[str, str] = {}
    for w in order:
        rowsw = [(e, v["txns"]) for (e, ww), v in per.items() if ww == w]
        if rowsw:
            leader[w] = max(rowsw, key=lambda x: x[1])[0]
    prev: dict[str, float] = {}
    rows: list[dict] = []
    for (name, w), v in sorted(per.items(), key=lambda kv: (kv[0][0],
                                                           order.index(kv[0][1]))):
        idx = order.index(w)
        sr = sum(v["sr"]) / len(v["sr"]) if v["sr"] else 99.0
        share = 100 * v["txns"] / (week_grand[w] or 1)
        avg_daily = v["txns"] / max(1, pdays.get(w, 1))
        mom = _pct_change(prev.get(name), avg_daily) if name in prev else None
        prev[name] = avg_daily
        meta = next((p for p in org.psps if p["name"] == name), {})
        rows.append({
            "psp": name, "sponsor_bank": meta.get("sponsor_bank", ""),
            "week": w, "week_index": idx + 1,
            "txns": int(v["txns"]), "value_inr": int(v["value"]),
            "market_share_pct": round(share, 2),
            "success_rate": round(sr, 2),
            "wow_growth_pct": mom,
            "new_users_k": round(max(0.0, (mom or 0)) * share * 1.5, 1),
            "satisfaction": round(_clampf(sr - 1.5, 40, 99), 1),
            "is_market_leader": leader.get(w) == name,
        })
    return rows


# ---------------------------------------------------------------- products
_PRODUCT_FEATURES = {
    "UPI Core": ["Person to Merchant", "Person to Person", "Collect Requests",
                 "Intent Payments"],
    "UPI Autopay": ["UPI Autopay"],
    "UPI Lite": ["UPI Lite"],
    "UPI Lite X": ["UPI Lite X"],
    "UPI Credit": ["UPI Credit Line", "RuPay Credit on UPI"],
    "UPI International": ["UPI International"],
    "QR Payments": ["QR Payments"],
    "Merchant Products": ["QR Payments", "Person to Merchant"],
}


def build_product_lifecycle(k: TransactionEngine, org: Org,
                            cubes: dict, base_by_month: dict) -> list[dict]:
    grp = _period_rows(cubes["feature_daily"], "feature", k, _month_label)
    per, order = grp["per"], grp["order"]
    pdays = _period_day_counts(k, _month_label)
    month_grand = {m: sum(v["txns"] for (e, mm), v in per.items() if mm == m)
                   for m in order}
    month_grand_val = {m: sum(v["value"] for (e, mm), v in per.items() if mm == m)
                       for m in order}
    prod_meta = {p["name"]: p for p in org.products}
    prev: dict[str, float] = {}
    rows: list[dict] = []
    for prod, feats in _PRODUCT_FEATURES.items():
        for m in order:
            idx = order.index(m)
            txns = sum(per.get((f, m), {}).get("txns", 0.0) for f in feats)
            value = sum(per.get((f, m), {}).get("value", 0.0) for f in feats)
            merch_txns = sum(per.get((f, m), {}).get("txns", 0.0)
                             for f in feats if f in _MERCHANT_FEATURES)
            if txns == 0:
                continue
            share = 100 * txns / (month_grand[m] or 1)
            rev_share = 100 * value / (month_grand_val[m] or 1)
            avg_daily = txns / max(1, pdays.get(m, 1))
            mom = _pct_change(prev.get(prod), avg_daily) if prod in prev else None
            prev[prod] = avg_daily
            adoption = base_by_month.get(m, 340.0) * share / 100
            rows.append({
                "product": prod, "team": prod_meta.get(prod, {}).get("team", ""),
                "owner": prod_meta.get(prod, {}).get("owner_name", ""),
                "month": m, "month_index": idx + 1,
                "txns": int(txns), "value_inr": int(value),
                "avg_ticket_inr": round(value / (txns or 1), 0),
                "market_share_pct": round(share, 2),
                "revenue_contribution_pct": round(rev_share, 2),
                "merchant_mix_pct": round(100 * merch_txns / (txns or 1), 1),
                "customer_mix_pct": round(100 * (txns - merch_txns) / (txns or 1), 1),
                "adoption_m": round(adoption, 2),
                "mom_growth_pct": mom,
                "lifecycle_stage": _lifecycle_stage(mom, share),
            })
    return rows


# ------------------------------------------------ multi-granularity KPI trends
def build_kpi_rollups(k: TransactionEngine) -> list[dict]:
    """Every KPI aggregated to weekly / monthly / quarterly period means with
    period-over-period deltas — the long-term trend surface."""
    rows: list[dict] = []
    grains = [("weekly", lambda d: f"W{(d - k.week_start).days // 7 + 1}"),
              ("monthly", _month_label), ("quarterly", _quarter_label)]
    for kpi in k.names():
        series = k.series[kpi]
        for grain, label_fn in grains:
            buckets: dict[str, list[float]] = {}
            order: list[str] = []
            for d in range(k.days):
                lbl = label_fn(k.dates[d])
                if lbl not in buckets:
                    buckets[lbl] = []
                    order.append(lbl)
                buckets[lbl].append(series[d])
            prev_val = None
            for i, lbl in enumerate(order):
                vals = buckets[lbl]
                val = round(sum(vals) / len(vals), 3)
                delta = _pct_change(prev_val, val) if prev_val is not None else None
                direction = ("up" if (prev_val is not None and val > prev_val)
                             else "down" if (prev_val is not None and val < prev_val)
                             else "flat")
                prev_val = val
                rows.append({
                    "kpi": kpi, "grain": grain, "period": lbl,
                    "period_index": i + 1, "value": val,
                    "delta_pct": delta, "direction": direction})
    return rows


def build_kpi_rolling(k: TransactionEngine) -> list[dict]:
    """Rolling 30- and 90-day means per KPI per day."""
    rows: list[dict] = []
    for kpi in k.names():
        s = k.series[kpi]
        for d in range(k.days):
            w30 = s[max(0, d - 29):d + 1]
            w90 = s[max(0, d - 89):d + 1]
            rows.append({
                "kpi": kpi, "day": d + 1, "date": k.dates[d].isoformat(),
                "value": round(s[d], 3),
                "rolling_30": round(sum(w30) / len(w30), 3),
                "rolling_90": round(sum(w90) / len(w90), 3)})
    return rows


# --------------------------------------------------------- forecast validation
def build_forecast_validation(k: TransactionEngine) -> list[dict]:
    """Backtest: forecast the last `horizon` days from the earlier history and
    compare to what actually happened — accuracy, error, direction, confidence."""
    horizon = min(30, max(5, k.days // 6))
    rows: list[dict] = []
    for kpi in k.names():
        s = k.series[kpi]
        if len(s) < horizon + 8:
            continue
        train = s[:-horizon]
        actual = s[-horizon:]
        pred = _forecast_linear(train, horizon)
        mape = _mape(actual, pred)
        acc = round(_clampf(100 - mape, 0, 100), 1)
        mae = round(sum(abs(a - p) for a, p in zip(actual, pred)) / horizon, 3)
        # direction hit: sign of realised vs predicted change over the window
        act_dir = actual[-1] - train[-1]
        pred_dir = pred[-1] - train[-1]
        dir_ok = (act_dir >= 0) == (pred_dir >= 0)
        vol = _stdev([train[i] - train[i - 1] for i in range(1, len(train))])
        mean = sum(train) / len(train) or 1.0
        conf = round(_clampf(100 - abs(vol / mean) * 100 * 4, 45, 97), 1)
        rows.append({
            "kpi": kpi, "train_end_day": len(train),
            "horizon_days": horizon,
            "predicted_end": round(pred[-1], 3),
            "actual_end": round(actual[-1], 3),
            "mape_pct": round(mape, 2), "accuracy_pct": acc,
            "mean_abs_error": mae,
            "direction_correct": dir_ok,
            "confidence_pct": conf,
            "method": "least-squares linear (14d window)"})
    return rows


def build_forecast_forward(k: TransactionEngine) -> list[dict]:
    """Forward 30-day forecast per KPI with a confidence band, starting the day
    after the history ends."""
    horizon = 30
    rows: list[dict] = []
    for kpi in k.names():
        s = k.series[kpi]
        pred = _forecast_linear(s, horizon)
        diffs = [s[i] - s[i - 1] for i in range(1, len(s))]
        vol = _stdev(diffs[-30:] if len(diffs) >= 30 else diffs)
        mean = sum(s) / len(s) or 1.0
        conf = round(_clampf(100 - abs(vol / mean) * 100 * 4, 45, 97), 1)
        for step in range(horizon):
            dt = k.dates[-1] + timedelta(days=step + 1)
            band = vol * 1.96 * ((step + 1) ** 0.5)
            rows.append({
                "kpi": kpi, "horizon_day": step + 1, "date": dt.isoformat(),
                "forecast": round(pred[step], 3),
                "lower": round(pred[step] - band, 3),
                "upper": round(pred[step] + band, 3),
                "confidence_pct": conf})
    return rows


# ----------------------------------------------------------- decision tracking
def build_decision_tracking(k: TransactionEngine, org: Org) -> list[dict]:
    """Every incident-driven executive decision, with the KPI it targeted, the
    expected impact, the *actual* measured recovery, a success score and an
    estimated business value protected."""
    rows: list[dict] = []
    for iss in k.issues:
        if not getattr(iss, "dec_id", None):
            continue
        impacts = ISSUE_TYPES[iss.itype]["impact"]
        # Prefer Success Rate as the headline KPI when the incident touches it,
        # otherwise the largest-magnitude impacted KPI.
        kpi = ("Success Rate (%)" if "Success Rate (%)" in impacts
               else max(impacts, key=lambda kk: impacts[kk]) if impacts
               else "Success Rate (%)")
        s = k.series.get(kpi) or []
        active = list(range(iss.start, min(iss.end + 1, k.days)))
        if not s or not active:
            continue
        hb = KPI_HIGHER_BETTER.get(kpi, True)
        pre_i = max(0, iss.start - 1)
        post_i = min(iss.end + 3, k.days - 1)
        pre = s[pre_i]
        trough = min(s[i] for i in active) if hb else max(s[i] for i in active)
        post = s[post_i]
        drop = abs(pre - trough)
        recovered = abs(post - trough)
        recovery_pct = round(100 * recovered / drop, 1) if drop else 100.0
        success = round(_clampf(recovery_pct - abs(_pct_change(pre, post) or 0) * 2,
                                0, 100), 1)
        # Business value protected: transactions kept successful by restoring the
        # Success Rate from its trough, priced at the ~average ticket over the
        # remediation window (in crore).
        srs = k.series.get("Success Rate (%)") or [99.0]
        sr_trough = min(srs[i] for i in active)
        sr_post = srs[post_i]
        sr_recovered = max(0.0, sr_post - sr_trough)
        vol_m = k.value("UPI Transactions (M/day)", post_i)
        biz_cr = round(vol_m * 1e6 * (sr_recovered / 100) * 640 * len(active) / 1e7, 1)
        refs = [x for x in (iss.inc_id, iss.rca_id, iss.dec_id) if x]
        rows.append({
            "decision_id": iss.dec_id, "incident_id": iss.inc_id,
            "date": k.dates[iss.start].isoformat(),
            "title": f"{ISSUE_TYPES[iss.itype]['label']} response",
            "severity": iss.severity,
            "bank": iss.bank["name"] if iss.bank else "",
            "psp": iss.psp["name"] if iss.psp else "",
            "feature": iss.feature[0] if iss.feature else "",
            "target_kpi": kpi,
            "expected_impact": f"Restore {kpi} toward pre-incident {round(pre,2)}",
            "pre_value": round(pre, 3), "trough_value": round(trough, 3),
            "post_value": round(post, 3),
            "actual_impact": f"Recovered {recovery_pct}% of the dip "
                             f"({round(trough,2)} -> {round(post,2)})",
            "recovery_pct": recovery_pct,
            "success_score": success,
            "business_value_cr": biz_cr,
            "status": "Resolved" if recovery_pct >= 80 else "Monitoring",
            "evidence_refs": " ".join(refs)})
    return rows


# ------------------------------------------------------------- cross-entity
def build_cross_entity(k: TransactionEngine, org: Org,
                       cubes: dict) -> list[dict]:
    """Interconnections across the ecosystem: merchant->PSP, PSP->sponsor bank,
    feature->product, entity->region and feature->business-growth."""
    rows: list[dict] = []
    m_tot: dict[str, float] = {}
    for r in cubes["merchant_daily"]:
        m_tot[str(r.get("merchant"))] = m_tot.get(str(r.get("merchant")), 0.0) \
            + float(r.get("txns") or 0)
    for m in org.merchants:
        rows.append({"source_type": "merchant", "source": m["name"],
                     "relation": "settles_via", "target_type": "psp",
                     "target": m["psp"], "weight": int(m_tot.get(m["name"], 0)),
                     "note": f"{m['category']} / {m.get('size','')}"})
        rows.append({"source_type": "merchant", "source": m["name"],
                     "relation": "in_region", "target_type": "region",
                     "target": m.get("region", ""), "weight": int(m_tot.get(m["name"], 0)),
                     "note": ""})
    for p in org.psps:
        rows.append({"source_type": "psp", "source": p["name"],
                     "relation": "sponsored_by", "target_type": "bank",
                     "target": p["sponsor_bank"], "weight": 0, "note": ""})
    for prod, feats in _PRODUCT_FEATURES.items():
        for f in feats:
            rows.append({"source_type": "feature", "source": f,
                         "relation": "part_of", "target_type": "product",
                         "target": prod, "weight": 0, "note": ""})
    # feature -> business growth (its month-over-month volume growth)
    fgrowth: dict[str, list[float]] = {}
    for r in cubes["feature_daily"]:
        fgrowth.setdefault(str(r["feature"]), [0.0] * k.days)
        fgrowth[str(r["feature"])][int(r["day"]) - 1] = float(r.get("txns") or 0)
    for f, s in fgrowth.items():
        g = _pct_change(sum(s[:7]) / 7, sum(s[-7:]) / 7) if k.days >= 14 else None
        rows.append({"source_type": "feature", "source": f,
                     "relation": "drives_growth", "target_type": "business",
                     "target": "UPI volume", "weight": int(sum(s)),
                     "note": f"{g:+}% over the period" if g is not None else ""})
    return rows


# --------------------------------------------------------------- storylines
def build_storylines(k: TransactionEngine, org: Org) -> list[dict]:
    """A connected weekly narrative: a signal from transaction behaviour ->
    entity impact -> team discussion -> executive action -> next-week outcome."""
    rows: list[dict] = []
    weeks = -(-k.days // 7)
    flags = k.weekly_flags()
    for w in range(weeks):
        d0 = w * 7
        d1 = min(w * 7 + 6, k.days - 1)
        wk_issues = [i for i in k.issues if d0 <= i.start <= d1]
        wstart = k.dates[d0].isoformat()
        top_bank, worst_sr = k.worst_bank(d1)
        feats = k.top_features(d1, n=1)
        top_feat = feats[0][0] if feats else "Person to Merchant"
        sr_end = k.value("Success Rate (%)", d1)
        sr_start = k.value("Success Rate (%)", d0)
        steps: list[tuple[str, str, str, str, str]] = []
        if wk_issues:
            iss = wk_issues[0]
            ent = iss.entity_label()
            steps = [
                ("Signal", "Product Analytics",
                 f"Transaction monitoring flags {ISSUE_TYPES[iss.itype]['label']} "
                 f"on {ent}", ent, "Success Rate (%)"),
                ("Impact", "Operations",
                 f"{iss.severity} incident {iss.inc_id} opened; "
                 f"complaints and declines rise", ent, "Customer Complaints"),
                ("Discussion", "Engineering",
                 "Incident bridge convenes; root cause isolated and mitigation "
                 "deployed", ent, "Response Time (ms)"),
                ("Action", "UPI Products leadership",
                 f"Executive approves the {ISSUE_TYPES[iss.itype]['channel']} "
                 f"remediation ({iss.dec_id or iss.inc_id})", ent, "Risk Score"),
                ("Outcome", "Product Operations",
                 f"Success Rate recovers to {round(sr_end,2)}% by week end",
                 ent, "Success Rate (%)"),
            ]
        else:
            steps = [
                ("Signal", "Product Analytics",
                 f"{top_feat} leads volume; adoption and merchant growth continue",
                 top_feat, "UPI Transactions (M/day)"),
                ("Impact", "Merchant Success",
                 "Merchant onboarding and QR acceptance expand",
                 "QR Payments", "Merchant Adoption (M)"),
                ("Discussion", "Product Strategy",
                 "Capacity and adoption reviewed against forecast",
                 top_feat, "UPI Lite Adoption (M)"),
                ("Action", "UPI Products leadership",
                 "Executive endorses continued scaling; no incident this week",
                 top_feat, "Autopay Registrations (K/day)"),
                ("Outcome", "Product Operations",
                 f"Steady week; success rate {round(sr_end,2)}%, "
                 f"lowest bank {top_bank} at {round(worst_sr,2)}%",
                 top_bank, "Success Rate (%)"),
            ]
        for n, (stage, actor, event, entity, kpi) in enumerate(steps, start=1):
            rows.append({
                "week": w + 1, "week_start": wstart, "step_no": n,
                "stage": stage, "actor_team": actor, "event": event,
                "entity": entity, "linked_kpi": kpi,
                "sr_start": round(sr_start, 2), "sr_end": round(sr_end, 2),
                "has_incident": bool(wk_issues)})
    return rows


def build_evolution(org: Org, k: TransactionEngine, ops: Ops,
                    cubes: dict) -> dict[str, list]:
    """Assemble every V8.0 evolution cube from the ledger/KPI ground truth."""
    cust = build_customer_evolution(k)
    bbm = _base_by_month(cust)
    return {
        "customer_evolution": cust,
        "feature_adoption": build_feature_adoption(k, cubes, bbm),
        "merchant_evolution": build_merchant_evolution(k, org, cubes),
        "bank_evolution": build_bank_evolution(k, org, cubes),
        "psp_evolution": build_psp_evolution(k, org, cubes),
        "product_lifecycle": build_product_lifecycle(k, org, cubes, bbm),
        "kpi_rollups": build_kpi_rollups(k),
        "kpi_rolling": build_kpi_rolling(k),
        "forecast_validation": build_forecast_validation(k),
        "forecast_forward": build_forecast_forward(k),
        "decision_tracking": build_decision_tracking(k, org),
        "cross_entity": build_cross_entity(k, org, cubes),
        "storylines": build_storylines(k, org),
    }


def emit_analytics_docs(c: Corpus, org: Org, k: TransactionEngine, ops: Ops,
                        cubes: dict[str, list], trends: list[dict],
                        bi: list[dict], forecasts: list[dict]) -> None:
    """Ingestible markdown so the Brain can answer the V7.0 question set. Weekly
    BI notes plus a month-close analytics pack."""
    days = k.days
    last = days - 1
    fgrowth = _growth_map(trends, "feature::")
    feat_tot = _month_totals(cubes["feature_daily"], "feature")
    bank_tot = _month_totals(cubes["bank_daily"], "bank")
    psp_tot = _month_totals(cubes["psp_daily"], "psp")
    merch_tot = _month_totals(cubes["merchant_daily"], "merchant")
    city_tot = _month_totals(cubes["city_daily"], "city")
    total_txns = sum(v["txns"] for v in feat_tot.values()) or 1.0

    # ---- weekly BI notes ------------------------------------------------
    weeks = -(-days // 7)
    for w in range(weeks):
        wd_last = min(w * 7 + 6, last)
        gd = wd_last + 1
        wk_bi = [f for f in bi if f["category"] in
                 ("anomaly", "high_risk_bank", "growing_features", "regional_growth")]
        lines = "\n".join(f"- **{f['category']}** ({f['severity']}): {f['finding']}"
                          for f in wk_bi[:8]) or "- No material signals this week."
        c.doc(gd, "analytics", f"BI-W{w+1}-findings.md", f"BI-W{w+1}", "report",
              ops.when(wd_last, 18, 45),
              f"Business Intelligence — Week {w+1} Signals",
              f"""**Period:** {k.dates[w*7].strftime('%d %b')} - {k.dates[wd_last].strftime('%d %b %Y')}
**Source:** analytics cubes ({ops.WB} for KPIs)

## Detected signals
{lines}

## Note
Signals are derived from the transaction ledger and aggregate cubes; incidents
this month are the operational response to the adverse ones.""",
              _pad([ops.WB, ops.weekly_id(w), ops.MONTHLY], ops))

    # ---- feature comparison & analytics --------------------------------
    frows = sorted(feat_tot.items(), key=lambda kv: kv[1]["txns"], reverse=True)
    ftable = "\n".join(
        f"| {name} | {int(v['txns']):,} | {int(v['value']):,} | "
        f"{round(v['value']/max(1,v['txns']),0):,.0f} | "
        f"{round(sum(v['sr'])/len(v['sr']),2) if v['sr'] else '—'} | "
        f"{'+' if fgrowth.get(name,0)>=0 else ''}{fgrowth.get(name,0)}% |"
        for name, v in frows)
    fastest = max(fgrowth.items(), key=lambda kv: kv[1]) if fgrowth else ("—", 0)
    high_ticket = max(feat_tot.items(),
                      key=lambda kv: kv[1]["value"]/max(1, kv[1]["txns"]))
    c.doc(days, "analytics", "ANALYTICS-features.md",
          "ANALYTICS-FEATURES", "report", ops.when(last, 19, 0),
          "UPI Feature Comparison & Analytics",
          f"""**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}
**Source:** analytics/feature_daily.csv, analytics/trends.csv

## All features (sample month totals)
| Feature | Txns | Value (INR) | Avg ticket | Success % | Growth m/m |
|---------|------|-------------|-----------|-----------|-----------|
{ftable}

## Highlights
- **Fastest-growing feature:** {fastest[0]} ({'+' if fastest[1]>=0 else ''}{fastest[1]}% m/m).
- **Highest average ticket size:** {high_ticket[0]}
  (~INR {round(high_ticket[1]['value']/max(1,high_ticket[1]['txns']),0):,.0f}).
- Compare P2P vs P2M, QR vs Intent, and Lite vs Autopay directly from the table.""",
          _pad([ops.WB, ops.MONTHLY, ops.OVERVIEW], ops))

    # ---- bank & PSP scorecards -----------------------------------------
    bgrowth = _growth_map(trends, "bank::")
    pgrowth = _growth_map(trends, "psp::")
    brows = sorted(bank_tot.items(), key=lambda kv: kv[1]["txns"], reverse=True)
    btable = "\n".join(
        f"| {n} | {int(v['txns']):,} | {round(v['txns']/total_txns*100,1)}% | "
        f"{round(sum(v['sr'])/len(v['sr']),2) if v['sr'] else '—'} | "
        f"{'+' if bgrowth.get(n,0)>=0 else ''}{bgrowth.get(n,0)}% |"
        for n, v in brows)
    prows = sorted(psp_tot.items(), key=lambda kv: kv[1]["txns"], reverse=True)
    ptable = "\n".join(
        f"| {n} | {int(v['txns']):,} | {round(v['txns']/total_txns*100,1)}% | "
        f"{round(sum(v['sr'])/len(v['sr']),2) if v['sr'] else '—'} | "
        f"{'+' if pgrowth.get(n,0)>=0 else ''}{pgrowth.get(n,0)}% |"
        for n, v in prows)
    psp_loser = min(pgrowth.items(), key=lambda kv: kv[1]) if pgrowth else ("—", 0)
    c.doc(days, "analytics", "ANALYTICS-banks-psps.md", "ANALYTICS-BANKS-PSPS",
          "report", ops.when(last, 19, 10), "Bank & PSP Scorecards",
          f"""**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}
**Source:** analytics/bank_daily.csv, analytics/psp_daily.csv, analytics/trends.csv

## Banks (by sampled volume)
| Bank | Txns | Share | Avg success % | Growth m/m |
|------|------|-------|---------------|-----------|
{btable}

## PSPs (by sampled volume)
| PSP | Txns | Share | Avg success % | Growth m/m |
|-----|------|-------|---------------|-----------|
{ptable}

## Highlights
- **PSP losing the most share:** {psp_loser[0]} ({psp_loser[1]}% m/m).
- Banks that improved this month are those with positive growth and rising success.""",
          _pad([ops.WB, ops.MONTHLY, ops.OVERVIEW], ops))

    # ---- market share, cities, mix, hourly -----------------------------
    crows = sorted(city_tot.items(), key=lambda kv: kv[1]["txns"], reverse=True)[:10]
    ctable = "\n".join(f"| {n} | {int(v['txns']):,} | {int(v['value']):,} |"
                       for n, v in crows)
    mix = cubes["transaction_mix"]
    mixtable = "\n".join(f"| {r['payment_type']} | {int(r['sample_txns']):,} | "
                         f"{round(100*r['sample_txns']/total_txns,1)}% |" for r in mix)
    hourly = cubes["hourly_distribution"]
    peak = max(hourly, key=lambda r: r["sample_txns"])
    c.doc(days, "analytics", "ANALYTICS-market-mix.md", "ANALYTICS-MARKET-MIX",
          "report", ops.when(last, 19, 20),
          "Market Share, Cities, Transaction Mix & Hourly Distribution",
          f"""**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}
**Source:** analytics/city_daily.csv, transaction_mix.csv, hourly_distribution.csv

## Top cities (by sampled volume)
| City | Txns | Value (INR) |
|------|------|-------------|
{ctable}

## Transaction mix
| Payment type | Txns | Share |
|--------------|------|-------|
{mixtable}

## Hourly distribution
Peak hour is ~{peak['hour']}:00. Volume concentrates in the 10:00-13:00 and
19:00-22:00 windows; overnight is quiet — the basis for capacity planning.""",
          _pad([ops.WB, ops.MONTHLY, ops.OVERVIEW], ops))

    # ---- forecasts & recommendations -----------------------------------
    def fc(series: str) -> dict:
        return next((f for f in forecasts if f["series"] == series), {})
    ftx, fval = fc("total::sample_txns"), fc("total::sample_value_inr")
    fsr = fc("total::success_rate")
    rec_lines = []
    for f in bi:
        if f["severity"] in ("high", "watch"):
            rec_lines.append(f"- {f['finding']}")
    rec_md = "\n".join(rec_lines[:6]) or "- Maintain current operating posture."
    c.doc(days, "analytics", "ANALYTICS-forecasts.md", "ANALYTICS-FORECASTS",
          "report", ops.when(last, 19, 30), "Forecasts & Executive Recommendations",
          f"""**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}
**Method:** deterministic trend projection (7-day average daily delta) over the
analytics cubes. Directional, not a statistical model.

## Next-period forecast (sampled scale)
- Transactions: today {ftx.get('today','—')} → next day {ftx.get('forecast_next','—')},
  +7d {ftx.get('forecast_7d','—')} (growth {ftx.get('growth_pct','—')}% m/m).
- Value (INR): +7d {fval.get('forecast_7d','—')}.
- Success rate: +7d {fsr.get('forecast_7d','—')}%.
- Fastest-growing features are projected to keep gaining share
  ({', '.join(f[0] for f in sorted(fgrowth.items(), key=lambda kv: kv[1], reverse=True)[:3])}).

## Recommendations (from BI signals)
{rec_md}""",
          _pad([ops.WB, ops.MONTHLY, ops.OVERVIEW], ops))

    # ---- executive KPI dashboard doc -----------------------------------
    kpi_lines = "\n".join(
        f"- **{kpi.split(' (')[0]}:** {k.fmt(kpi, last)}" for kpi in k.names())
    c.doc(days, "analytics", "ANALYTICS-exec-kpis.md", "ANALYTICS-EXEC-KPIS",
          "report", ops.when(last, 19, 40), "Executive KPI Dashboard (Month Close)",
          f"""**Period:** {k.dates[0].strftime('%d %b')} - {k.dates[last].strftime('%d %b %Y')}
**Source:** {ops.WB} + analytics cubes

## Headline KPIs (month close)
{kpi_lines}

## Ecosystem
- Active banks in the ledger: {len(bank_tot)}; PSPs: {len(psp_tot)};
  merchants: {len(merch_tot)}; cities: {len(city_tot)}.
- Top feature by volume: {frows[0][0]}; top bank: {brows[0][0]}; top PSP: {prows[0][0]}.""",
          _pad([ops.WB, ops.MONTHLY, ops.OVERVIEW], ops))


# ===========================================================================
# Scenario spine — the human-readable storyline and cross-reference index.
# ===========================================================================
def build_scenarios(c: Corpus, org: Org, k: TransactionEngine, ops: Ops) -> None:
    scen = c.out / "scenarios"
    scen.mkdir(parents=True, exist_ok=True)

    timeline = "\n".join(
        f"- **Day {i.start+1} ({k.dates[i.start].strftime('%a %d %b')})** — "
        f"{i.inc_id}: {ISSUE_TYPES[i.itype]['label']} on {i.entity_label()} "
        f"({i.severity}, {i.duration} days). "
        f"{'RCA ' + i.rca_id + ', decision ' + i.dec_id + '.' if i.rca_id else 'Short operational issue.'}"
        for i in k.issues)

    c.doc(None, "", "STORYLINE.md", ops.STORYLINE, "product_document",
          ops.when(ops.days - 1, 20, 0), "Operational Month — Transaction-Driven Timeline",
          f"""This corpus is one continuous month of NPCI UPI Products operations.
There are no scripted weekly themes and no product launches — every artifact is
routine operations or the natural consequence of transaction behaviour.

Volume follows a growth trend modulated by weekday, month-end and high-volume
campaign days. Bank/PSP/feature health degradations surface as incidents, each
running its lifecycle (detect -> bridge -> investigate -> RCA -> decision -> SOP
-> recovery -> validation) and referenced again in weekly and monthly reviews.

## Incident timeline
{timeline}

The numeric spine is {ops.WB}; the monthly close is {ops.MONTHLY}. Every day also
has a daily operations report (RPT-Dxx-DAILY) and a monitoring note.""",
          _pad([ops.WB, ops.MONTHLY, ops.OVERVIEW] +
               [i.inc_id for i in k.issues[:2]], ops), top="scenarios")

    lines = ["| Artifact | Type | When | References |",
             "|----------|------|------|------------|"]
    for a in sorted(c.artifacts, key=lambda x: x.when):
        refs = ", ".join(a.refs[:6])
        lines.append(f"| {a.art_id} | {a.kind} | {a.when.strftime('%d-%b %H:%M')} "
                     f"| {refs} |")
    (scen / "CROSS_REFERENCE_INDEX.md").write_text(
        f"# Cross-Reference Index — {ORG_NAME}\n\n"
        f"{len(c.artifacts)} artifacts across {ops.days} days; every narrative "
        f"artifact links to at least three others.\n\n" + "\n".join(lines) + "\n",
        encoding="utf-8")


# ===========================================================================
# Ingestion manifest + cross-reference export.
# ===========================================================================
INGEST_KINDS: dict[str, tuple[str, str]] = {
    "outlook": ("meeting_notes", "Outlook email threads"),
    "teams": ("meeting_notes", "Microsoft Teams conversations"),
    "meetings": ("meeting_notes", "Meetings: agendas, notes, decisions"),
    "decisions": ("meeting_notes", "Decision records"),
    "incidents": ("rca_repository", "Incident records and RCAs"),
    "docs": ("product_documents", "SOPs, BRDs, PRDs, product docs"),
    "reports": ("document_folder", "Daily, weekly, executive, risk reports"),
    "excel": ("document_folder", "KPI workbooks"),
    "tasks": ("document_folder", "Enterprise tasks"),
    "analytics": ("document_folder", "Ecosystem analytics, BI, comparisons, forecasts"),
}

CATEGORY_BY_KIND = {
    "meeting_notes": "meeting", "rca_repository": "rca",
    "product_documents": "product_document", "document_folder": "document",
    "sop_repository": "sop", "policy_repository": "policy",
}


def write_crossref(c: Corpus, out: Path) -> None:
    import json
    cat_by_sub = {sub: CATEGORY_BY_KIND[kind]
                  for sub, (kind, _d) in INGEST_KINDS.items()}
    cat_by_sub["master"] = "document"
    entries: dict[str, dict] = {}
    for a in c.artifacts:
        sub = a.path.parent.name
        category = cat_by_sub.get(sub)
        if category is None:
            continue
        entries[a.art_id] = {"stem": a.path.stem, "category": category,
                             "refs": a.refs}
    (out / "CROSSREF.json").write_text(json.dumps(entries, indent=2),
                                       encoding="utf-8")


def write_manifest(out: Path, org: Org, ops: Ops, days: int) -> None:
    import json
    ingest = []
    for d in range(1, days + 1):
        day_dir = out / f"day_{d:02d}"
        for sub, (kind, desc) in INGEST_KINDS.items():
            folder = day_dir / sub
            if folder.exists() and any(folder.iterdir()):
                ingest.append({
                    "name": f"npci-day{d:02d}-{sub}",
                    "kind": kind,
                    "location": str(folder.resolve()),
                    "description": f"Day {d} — {desc}",
                })
    manifest = {
        "organization": ORG_NAME,
        "department": DEPARTMENT,
        "week_start": ops.dates[0].isoformat(),
        "week_end": ops.dates[-1].isoformat(),
        "weeks": -(-days // 7),
        "days": days,
        "master": str((out / "master").resolve()),
        "ingest_sources": ingest,
    }
    (out / "INGEST_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")


# ===========================================================================
# Main.
# ===========================================================================
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the synthetic NPCI UPI Products enterprise (V5.1).")
    parser.add_argument("--days", type=int, default=180,
                        help="business days to generate (1-180, default 180 = "
                             "a continuous six-month operating history)")
    parser.add_argument("--seed", type=int, default=2026,
                        help="deterministic seed (default 2026)")
    parser.add_argument("--out", default="enterprise_data",
                        help="output directory (default enterprise_data)")
    parser.add_argument("--week-start", default="2026-06-22",
                        help="Monday of day 1 (default 2026-06-22)")
    parser.add_argument("--no-clean", action="store_true",
                        help="do not delete an existing output directory first")
    parser.add_argument("--ledger-size", type=int, default=10000,
                        help="sampled transactions per day for the ledger "
                             "(default 10000)")
    args = parser.parse_args()

    days = max(1, min(180, args.days))
    out = Path(args.out).resolve()
    week_start = date.fromisoformat(args.week_start)
    if week_start.weekday() != 0:
        week_start -= timedelta(days=week_start.weekday())  # snap to Monday

    print(f"Synthetic Enterprise Generator V8.0 — {ORG_NAME} / {DEPARTMENT}")
    print(f"  seed={args.seed}  days={days}  day1={week_start} -> "
          f"{week_start + timedelta(days=days-1)}  ledger={args.ledger_size}/day")

    if out.exists() and not args.no_clean:
        shutil.rmtree(out)
        print(f"  removed existing {out}")
    out.mkdir(parents=True, exist_ok=True)

    rng = random.Random(args.seed)
    org = Org(rng=rng)
    org.build()
    org.build_customers(4000)
    k = TransactionEngine(org, rng, week_start, days)
    ops = Ops(k)
    c = Corpus(out)

    build_master(c, org, k, ops)
    build_master_workbook(c, org, k, ops)
    build_days(c, org, k, ops)

    # V7.0 ecosystem: sampled ledger -> aggregate cubes -> trends -> BI ->
    # forecasts -> ingestible analytics docs. The ledger is the ground truth;
    # the cubes and every analytics document roll up from it.
    print("  simulating transaction ledger + analytics ...")
    ledger = Ledger(org, k, ops, rng, size=args.ledger_size)
    cubes = ledger.build(out)
    trends = build_trends(cubes, k)
    bi = build_bi(cubes, trends, k)
    forecasts = build_forecasts(trends)
    # V8.0 six-month evolution cubes (lifecycle, rollups, rolling windows,
    # forecast validation, decision tracking, cross-entity, storylines).
    print("  deriving six-month evolution + forecast validation ...")
    evolution = build_evolution(org, k, ops, cubes)
    cubes.update(evolution)
    write_cubes(out, cubes, trends, bi, forecasts)
    emit_analytics_docs(c, org, k, ops, cubes, trends, bi, forecasts)

    build_scenarios(c, org, k, ops)
    write_manifest(out, org, ops, days)
    write_crossref(c, out)

    problems = c.validate()
    files = sorted(p for p in out.rglob("*") if p.is_file())
    by_day: dict[str, int] = {}
    for p in files:
        top = p.relative_to(out).parts[0]
        by_day[top] = by_day.get(top, 0) + 1

    ledger_rows = sum(len(rows) for rows in cubes.values())
    total_txns = sum(int(r["sample_txns"]) for r in cubes["daily_metrics"])
    print(f"\n  {len(c.artifacts)} linked artifacts, {len(files)} files, "
          f"{len(k.issues)} incidents")
    for top in sorted(by_day):
        print(f"    {top:<12} {by_day[top]}")
    print(f"  people={len(org.people)} products={len(org.products)} "
          f"merchants={len(org.merchants)} banks={len(org.banks)} "
          f"psps={len(org.psps)} features={len(FEATURES)} "
          f"customers={len(org.customers)}")
    print(f"  ledger: {total_txns:,} sampled transactions; "
          f"{len(cubes)} cubes, {len(trends)} trend series, {len(bi)} BI findings")
    evo_counts = {name: len(evolution[name]) for name in evolution}
    print(f"  evolution: " + ", ".join(f"{n}={c}" for n, c in evo_counts.items()))

    if problems:
        print(f"\n  INTEGRITY PROBLEMS ({len(problems)}):")
        for p in problems[:25]:
            print(f"    - {p}")
        raise SystemExit(1)
    print("\n  integrity: OK — every artifact links to >= 3 others, "
          "no dangling references.")
    print(f"\nDone. Enterprise written to {out}")
    print("Ingest with:  cd backend && python scripts/bootstrap_enterprise_demo.py")


if __name__ == "__main__":
    main()
