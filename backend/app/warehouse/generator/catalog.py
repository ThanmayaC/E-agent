"""Reference catalog for the simulation — NPCI products, MCCs, and the
ecosystem entities every transaction joins to.

The product table is the important part. Each NPCI product is a genuinely
different payment instrument: UPI Lite is an on-device wallet with a ₹1,000 cap
and no PIN, AutoPay is a debit against a pre-registered mandate, Credit on UPI
draws on a sanctioned line, UPI International settles cross-border with an FX
leg. Those differences show up in ticket size, success rate, failure taxonomy,
latency and time-of-day — so they are modelled per product rather than as one
transaction table with a `feature` column.
"""
from __future__ import annotations

from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Products
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Product:
    code: str
    name: str
    family: str                 # UPI | Credit | Mandates
    owning_team: str
    payment_types: tuple[str, ...]
    share: float                # share of ecosystem volume at window start
    # Adoption curve: 'mature' (slow linear), 'growth' (S-curve), 'hyper'
    # (steep S-curve off a small base), 'declining'.
    lifecycle: str
    adoption_target: float      # end-of-window multiple of the start share
    ticket_median: float        # ₹ — median ticket
    ticket_sigma: float         # lognormal sigma; higher = fatter tail
    ticket_cap: float | None    # regulatory / product cap in ₹
    base_success: float         # % at window start, before incidents
    success_drift: float        # percentage points added across the window
    latency_p50: int            # ms
    latency_p95: int
    merchant_facing: bool
    settlement_sensitive: bool  # suppressed on bank holidays
    weekend_bias: float         # >1 = skews to weekends (consumer/discretionary)
    description: str
    # Baseline decline *hazards* in percent, one per failure bucket:
    # (technical, business, risk, timeout). These are independent competing
    # risks, not a mix that sums to one — each is the standalone probability
    # that this class of failure kills the attempt, before any bank, ticket,
    # calendar or incident modifier. A bucket is therefore always caused by
    # something rather than drawn from a fixed distribution after the fact.
    #
    # Calibrated to published UPI behaviour: technical declines run well under
    # 1%, business declines (insufficient funds, wrong PIN, limits) dominate,
    # and mandate products fail several times more often than consumer ones
    # because a scheduled debit cannot wait for the payer to top up.
    decline_hazards: tuple[float, float, float, float] = (
        0.50, 2.80, 0.11, 0.34)


PRODUCTS: list[Product] = [
    Product(
        "UPI_P2P", "UPI Person to Person", "UPI", "UPI Core",
        ("P2P", "P2P-Collect"), 0.3350, "mature", 1.14,
        520.0, 1.25, 100_000, 98.72, 0.55, 340, 1180, False, False, 1.06,
        "Core account-to-account real-time transfers between individuals.",
        (0.55, 3.10, 0.10, 0.38)),
    Product(
        "UPI_P2M", "UPI Person to Merchant", "UPI", "UPI Core",
        ("P2M", "P2M-Intent", "P2M-Collect"), 0.2620, "mature", 1.21,
        286.0, 1.42, 200_000, 99.02, 0.42, 295, 940, True, False, 1.10,
        "Merchant payments over UPI intent, collect and deep-link flows.",
        (0.48, 2.55, 0.12, 0.32)),
    Product(
        "UPI_QR", "UPI QR Payments", "UPI", "QR Payments",
        ("P2M-QR-Static", "P2M-QR-Dynamic"), 0.1480, "growth", 1.46,
        174.0, 1.30, 200_000, 99.15, 0.38, 268, 860, True, False, 1.14,
        "Interoperable static and dynamic QR acceptance at physical merchants.",
        (0.42, 2.30, 0.10, 0.30)),
    Product(
        "UPI_LITE", "UPI Lite", "UPI", "UPI Lite",
        ("P2M-Lite", "P2P-Lite"), 0.0610, "hyper", 2.95,
        64.0, 0.82, 1_000, 99.62, 0.22, 118, 340, True, False, 1.18,
        "On-device low-value payments with no PIN and no core-banking hop.",
        (0.16, 0.86, 0.03, 0.12)),
    Product(
        "UPI_LITE_ATU", "UPI Lite Auto Top-Up", "UPI", "UPI Lite",
        ("Lite-AutoTopUp",), 0.0125, "hyper", 4.20,
        1_000.0, 0.34, 2_000, 99.28, 0.48, 402, 1240, False, True, 0.82,
        "Automatic replenishment of the on-device Lite balance via a mandate.",
        (0.52, 2.10, 0.05, 0.30)),
    Product(
        "UPI_AUTOPAY", "UPI AutoPay", "Mandates", "UPI Autopay",
        ("Mandate-Execution", "Mandate-Retry"), 0.0415, "growth", 1.92,
        1_240.0, 1.05, 1_500_000, 96.84, 1.35, 610, 2350, True, True, 0.58,
        "Recurring e-mandate debits for subscriptions, SIPs, EMIs and bills.",
        (0.90, 6.80, 0.12, 0.55)),
    Product(
        "UPI_CIRCLE", "UPI Circle", "UPI", "UPI Core",
        ("Circle-Delegated", "Circle-Full"), 0.0085, "hyper", 6.40,
        410.0, 1.18, 15_000, 98.34, 1.80, 388, 1320, True, False, 1.22,
        "Delegated payments where a primary user authorises secondary users.",
        (0.70, 2.60, 0.30, 0.35)),
    Product(
        "UPI_INTL", "UPI International", "UPI", "UPI International",
        ("Cross-Border-P2M", "Cross-Border-Remit"), 0.0072, "growth", 2.35,
        3_450.0, 1.34, 200_000, 96.10, 1.95, 1_180, 3_900, True, True, 1.28,
        "Cross-border UPI acceptance for Indian travellers and inbound NRIs.",
        (1.60, 2.20, 0.45, 0.90)),
    Product(
        "UPI_CREDIT_LINE", "Credit on UPI", "Credit", "UPI Credit",
        ("CreditLine-P2M",), 0.0128, "hyper", 3.60,
        2_180.0, 1.16, 500_000, 97.42, 1.62, 520, 1_780, True, True, 0.94,
        "Pre-sanctioned bank credit lines drawn down through a UPI handle.",
        (0.60, 3.40, 0.22, 0.28)),
    Product(
        "RUPAY_CREDIT", "RuPay Credit on UPI", "Credit", "UPI Credit",
        ("RuPayCredit-P2M", "RuPayCredit-QR"), 0.0176, "growth", 2.28,
        1_640.0, 1.22, 500_000, 98.16, 0.92, 465, 1_540, True, True, 1.02,
        "RuPay credit cards tokenised onto UPI for QR and merchant payments.",
        (0.55, 2.80, 0.26, 0.26)),
    Product(
        "UPI_RECURRING", "Recurring Payments", "Mandates", "UPI Autopay",
        ("Recurring-SIP", "Recurring-Bill", "Recurring-EMI"), 0.0089,
        "growth", 1.74,
        4_600.0, 1.02, 1_500_000, 97.55, 1.10, 690, 2_580, True, True, 0.44,
        "Scheduled SIP, insurance premium, EMI and utility bill collections.",
        (0.85, 7.40, 0.10, 0.60)),
    Product(
        "UPI_123PAY", "UPI 123Pay", "UPI", "UPI 123Pay",
        ("IVR", "MissedCall", "SoundBox-123"), 0.0050, "growth", 1.38,
        238.0, 1.05, 10_000, 95.90, 1.40, 2_450, 7_800, True, False, 0.90,
        "Feature-phone UPI over IVR, missed call and sound-based flows.",
        (2.10, 1.90, 0.10, 1.10)),
]

PRODUCT_BY_CODE = {p.code: p for p in PRODUCTS}

# ---------------------------------------------------------------------------
# Merchant Category Codes — the ISO 18245 codes actually seen on UPI acquiring.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class MCC:
    code: str
    name: str
    category: str
    subcategory: str
    ticket_mult: float          # relative to the product's median ticket
    share: float                # share of merchant-facing volume
    seasonality: str            # steady | festive | monthly | travel | daily
    risk: float                 # 0-1 chargeback / fraud propensity
    success_delta: float        # pp added to the product's base success rate


MCCS: list[MCC] = [
    MCC("5411", "Grocery Stores & Supermarkets", "Retail", "Grocery",
        0.72, 0.148, "daily", 0.06, 0.22),
    MCC("5814", "Fast Food Restaurants", "Food & Beverage", "Food Delivery",
        0.54, 0.112, "daily", 0.08, 0.18),
    MCC("5812", "Eating Places & Restaurants", "Food & Beverage", "Dining",
        1.35, 0.058, "festive", 0.09, 0.10),
    MCC("5541", "Service Stations (Fuel)", "Mobility", "Fuel",
        2.10, 0.084, "steady", 0.04, 0.26),
    MCC("4121", "Taxicabs & Ride Hailing", "Mobility", "Ride Hailing",
        0.88, 0.071, "daily", 0.07, 0.05),
    MCC("5399", "General Merchandise", "Retail", "General Retail",
        0.96, 0.066, "festive", 0.10, 0.12),
    MCC("5691", "Clothing & Accessory Stores", "Retail", "Fashion",
        2.35, 0.052, "festive", 0.16, -0.06),
    MCC("5732", "Electronics Stores", "Retail", "Electronics",
        7.80, 0.038, "festive", 0.24, -0.22),
    MCC("5912", "Drug Stores & Pharmacies", "Healthcare", "Pharmacy",
        1.12, 0.045, "steady", 0.05, 0.20),
    MCC("8062", "Hospitals", "Healthcare", "Hospitals",
        14.50, 0.016, "steady", 0.11, -0.30),
    MCC("4900", "Utilities — Electric, Gas, Water", "Bills", "Utilities",
        3.40, 0.061, "monthly", 0.03, 0.24),
    MCC("4814", "Telecom Services", "Bills", "Mobile & DTH Recharge",
        0.62, 0.058, "monthly", 0.04, 0.28),
    MCC("6300", "Insurance Premiums", "Financial Services", "Insurance",
        18.20, 0.021, "monthly", 0.06, -0.18),
    MCC("6211", "Securities & Investments", "Financial Services",
        "Wealth & SIP", 22.40, 0.019, "monthly", 0.05, -0.24),
    MCC("6012", "Financial Institutions — Loan Repayment", "Financial Services",
        "Loan & EMI", 26.80, 0.024, "monthly", 0.07, -0.34),
    MCC("4722", "Travel Agencies & Tour Operators", "Travel", "Travel Booking",
        16.40, 0.018, "travel", 0.19, -0.28),
    MCC("4511", "Airlines", "Travel", "Airlines",
        24.60, 0.011, "travel", 0.21, -0.34),
    MCC("7011", "Hotels & Lodging", "Travel", "Hotels",
        11.80, 0.013, "travel", 0.17, -0.20),
    MCC("5999", "Speciality Retail", "Retail", "Speciality",
        1.28, 0.034, "festive", 0.13, 0.02),
    MCC("7994", "Gaming & Digital Goods", "Digital", "Gaming",
        0.78, 0.026, "steady", 0.28, -0.10),
    MCC("5815", "Digital Media & OTT", "Digital", "OTT & Subscriptions",
        1.02, 0.031, "monthly", 0.09, 0.14),
    MCC("8220", "Colleges & Universities", "Education", "Education Fees",
        32.50, 0.014, "monthly", 0.04, -0.40),
    MCC("8299", "Educational Services", "Education", "EdTech",
        6.20, 0.017, "monthly", 0.12, -0.12),
    MCC("7230", "Beauty & Personal Care", "Services", "Salon & Spa",
        1.85, 0.022, "festive", 0.11, 0.06),
    MCC("7523", "Parking & Tolls", "Mobility", "Parking & Tolls",
        0.34, 0.019, "daily", 0.03, 0.30),
    MCC("5661", "Footwear Stores", "Retail", "Footwear",
        2.05, 0.012, "festive", 0.15, -0.04),
]

MCC_BY_CODE = {m.code: m for m in MCCS}

# Which MCCs each product realistically acquires, with affinity weights.
PRODUCT_MCC_AFFINITY: dict[str, dict[str, float]] = {
    "UPI_P2M":  {"5411": 1.3, "5814": 1.2, "5399": 1.2, "5912": 1.1,
                 "4900": 1.1, "4814": 1.2, "5691": 1.0, "5732": 0.9,
                 "5812": 1.1, "5999": 1.0, "7230": 1.0, "5815": 0.9},
    "UPI_QR":   {"5411": 1.6, "5814": 1.7, "4121": 1.5, "5541": 1.4,
                 "7523": 1.8, "5812": 1.3, "5912": 1.2, "5399": 1.2,
                 "5999": 1.1, "5661": 0.9},
    "UPI_LITE": {"5814": 2.4, "7523": 2.6, "4121": 1.8, "5411": 1.5,
                 "5912": 1.1, "4814": 1.2, "5999": 0.8},
    "UPI_AUTOPAY": {"5815": 2.8, "4900": 2.2, "4814": 2.0, "6300": 1.9,
                    "6211": 2.1, "6012": 1.8, "8299": 1.4, "8220": 0.9},
    "UPI_RECURRING": {"6211": 3.0, "6300": 2.6, "6012": 2.4, "4900": 1.6,
                      "8220": 1.5, "8299": 1.2},
    "UPI_CREDIT_LINE": {"5732": 2.2, "5691": 1.8, "8062": 1.6, "4722": 1.5,
                        "5411": 1.2, "5399": 1.3, "8220": 1.4, "5812": 1.1},
    "RUPAY_CREDIT": {"5732": 2.0, "5691": 1.9, "4722": 1.7, "4511": 1.8,
                     "7011": 1.6, "5812": 1.4, "5541": 1.3, "5399": 1.2},
    "UPI_INTL": {"4511": 3.0, "7011": 2.8, "4722": 2.4, "5812": 1.6,
                 "5691": 1.4, "5399": 1.1},
    "UPI_CIRCLE": {"5411": 1.8, "5814": 1.6, "4814": 1.5, "8299": 1.4,
                   "5912": 1.3, "4121": 1.2, "5999": 1.0},
    "UPI_123PAY": {"4814": 3.2, "4900": 2.4, "5411": 1.6, "7523": 1.2},
    "UPI_LITE_ATU": {},          # account-funded, no merchant leg
    "UPI_P2P": {},               # no merchant leg
}

# ---------------------------------------------------------------------------
# Ecosystem entities. Shares are the real Jun-2026 NPCI relative volumes so
# rankings match the published ecosystem statistics.
# ---------------------------------------------------------------------------
BANKS: list[dict] = [
    {"bank_id": "BANK-001", "name": "State Bank of India", "tier": "Tier 1",
     "region": "West", "share": 0.260, "base_success": 98.42, "p95": 1180},
    {"bank_id": "BANK-002", "name": "HDFC Bank", "tier": "Tier 1",
     "region": "North", "share": 0.090, "base_success": 99.28, "p95": 720},
    {"bank_id": "BANK-003", "name": "ICICI Bank", "tier": "Tier 1",
     "region": "North", "share": 0.050, "base_success": 99.34, "p95": 690},
    {"bank_id": "BANK-004", "name": "Axis Bank", "tier": "Tier 1",
     "region": "West", "share": 0.050, "base_success": 99.11, "p95": 810},
    {"bank_id": "BANK-005", "name": "Punjab National Bank", "tier": "Tier 2",
     "region": "North", "share": 0.048, "base_success": 97.85, "p95": 1520},
    {"bank_id": "BANK-006", "name": "Canara Bank", "tier": "Tier 2",
     "region": "South", "share": 0.042, "base_success": 98.05, "p95": 1390},
    {"bank_id": "BANK-007", "name": "Union Bank of India", "tier": "Tier 2",
     "region": "West", "share": 0.055, "base_success": 97.92, "p95": 1450},
    {"bank_id": "BANK-008", "name": "Bank of Baroda", "tier": "Tier 1",
     "region": "West", "share": 0.065, "base_success": 98.26, "p95": 1240},
    {"bank_id": "BANK-009", "name": "Indian Bank", "tier": "Tier 2",
     "region": "South", "share": 0.026, "base_success": 97.68, "p95": 1610},
    {"bank_id": "BANK-010", "name": "IDFC First Bank", "tier": "Tier 2",
     "region": "South", "share": 0.022, "base_success": 99.05, "p95": 760},
    {"bank_id": "BANK-011", "name": "Kotak Mahindra Bank", "tier": "Tier 1",
     "region": "West", "share": 0.028, "base_success": 99.18, "p95": 700},
    {"bank_id": "BANK-012", "name": "Yes Bank", "tier": "Tier 2",
     "region": "West", "share": 0.030, "base_success": 98.74, "p95": 900},
    {"bank_id": "BANK-013", "name": "IndusInd Bank", "tier": "Tier 2",
     "region": "West", "share": 0.018, "base_success": 98.60, "p95": 950},
    {"bank_id": "BANK-014", "name": "AU Small Finance Bank", "tier": "Tier 3",
     "region": "North", "share": 0.012, "base_success": 97.40, "p95": 1720},
    {"bank_id": "BANK-015", "name": "Federal Bank", "tier": "Tier 2",
     "region": "South", "share": 0.020, "base_success": 98.88, "p95": 840},
]

PSPS: list[dict] = [
    {"psp_id": "PSP-001", "name": "PhonePe", "kind": "TPAP",
     "sponsor_bank": "IndusInd Bank", "share": 0.462, "p95": 640},
    {"psp_id": "PSP-002", "name": "Google Pay", "kind": "TPAP",
     "sponsor_bank": "HDFC Bank", "share": 0.326, "p95": 590},
    {"psp_id": "PSP-003", "name": "Paytm", "kind": "TPAP",
     "sponsor_bank": "Union Bank of India", "share": 0.079, "p95": 780},
    {"psp_id": "PSP-004", "name": "Navi", "kind": "TPAP",
     "sponsor_bank": "Yes Bank", "share": 0.037, "p95": 700},
    {"psp_id": "PSP-005", "name": "SuperMoney", "kind": "TPAP",
     "sponsor_bank": "Yes Bank", "share": 0.019, "p95": 820},
    {"psp_id": "PSP-006", "name": "BHIM", "kind": "TPAP",
     "sponsor_bank": "State Bank of India", "share": 0.010, "p95": 1150},
    {"psp_id": "PSP-007", "name": "FamApp", "kind": "TPAP",
     "sponsor_bank": "Federal Bank", "share": 0.0086, "p95": 760},
    {"psp_id": "PSP-008", "name": "WhatsApp Pay", "kind": "TPAP",
     "sponsor_bank": "ICICI Bank", "share": 0.0066, "p95": 690},
    {"psp_id": "PSP-009", "name": "CRED", "kind": "TPAP",
     "sponsor_bank": "Axis Bank", "share": 0.0062, "p95": 720},
    {"psp_id": "PSP-010", "name": "Axis Mobile", "kind": "Bank App",
     "sponsor_bank": "Axis Bank", "share": 0.006, "p95": 980},
    {"psp_id": "PSP-011", "name": "YONO SBI", "kind": "Bank App",
     "sponsor_bank": "State Bank of India", "share": 0.008, "p95": 1320},
    {"psp_id": "PSP-012", "name": "iMobile Pay", "kind": "Bank App",
     "sponsor_bank": "ICICI Bank", "share": 0.005, "p95": 860},
    {"psp_id": "PSP-013", "name": "HDFC MobileBanking", "kind": "Bank App",
     "sponsor_bank": "HDFC Bank", "share": 0.005, "p95": 880},
    {"psp_id": "PSP-014", "name": "Amazon Pay", "kind": "TPAP",
     "sponsor_bank": "Axis Bank", "share": 0.004, "p95": 740},
]

# (city, state, region, relative weight, tier)
CITIES: list[tuple[str, str, str, float, int]] = [
    ("Mumbai", "Maharashtra", "West", 3.10, 1),
    ("Delhi", "Delhi", "North", 3.00, 1),
    ("Bengaluru", "Karnataka", "South", 2.80, 1),
    ("Hyderabad", "Telangana", "South", 2.20, 1),
    ("Chennai", "Tamil Nadu", "South", 2.00, 1),
    ("Pune", "Maharashtra", "West", 1.70, 1),
    ("Kolkata", "West Bengal", "East", 1.70, 1),
    ("Ahmedabad", "Gujarat", "West", 1.50, 1),
    ("Gurugram", "Haryana", "North", 1.00, 1),
    ("Surat", "Gujarat", "West", 1.10, 2),
    ("Jaipur", "Rajasthan", "North", 1.10, 2),
    ("Lucknow", "Uttar Pradesh", "North", 1.00, 2),
    ("Indore", "Madhya Pradesh", "Central", 0.90, 2),
    ("Kochi", "Kerala", "South", 0.90, 2),
    ("Kanpur", "Uttar Pradesh", "North", 0.80, 2),
    ("Nagpur", "Maharashtra", "Central", 0.80, 2),
    ("Patna", "Bihar", "East", 0.80, 2),
    ("Coimbatore", "Tamil Nadu", "South", 0.80, 2),
    ("Visakhapatnam", "Andhra Pradesh", "South", 0.80, 2),
    ("Bhopal", "Madhya Pradesh", "Central", 0.70, 2),
    ("Chandigarh", "Chandigarh", "North", 0.70, 2),
    ("Ludhiana", "Punjab", "North", 0.70, 2),
    ("Vadodara", "Gujarat", "West", 0.70, 2),
    ("Guwahati", "Assam", "East", 0.60, 3),
    ("Bhubaneswar", "Odisha", "East", 0.60, 3),
]

DEVICES: list[tuple[str, float]] = [
    ("Android", 0.766), ("iOS", 0.202), ("KaiOS/Feature", 0.021),
    ("Wearable", 0.007), ("PoS Terminal", 0.004),
]

CHANNELS: list[tuple[str, float]] = [
    ("Mobile App", 0.842), ("QR Scan", 0.061), ("PoS/Soundbox", 0.048),
    ("Web/Collect", 0.031), ("USSD/*99#", 0.011), ("IVR", 0.007),
]

# Customer behavioural segments — the cohort dimension analytics and ML use.
SEGMENTS: list[dict] = [
    {"code": "power", "name": "Power User", "share": 0.104,
     "txn_rate": 6.8, "ticket_mult": 1.34, "churn": 0.004, "credit_pref": 1.7},
    {"code": "regular", "name": "Regular User", "share": 0.318,
     "txn_rate": 2.7, "ticket_mult": 1.00, "churn": 0.010, "credit_pref": 1.0},
    {"code": "merchant_heavy", "name": "Merchant-Heavy", "share": 0.176,
     "txn_rate": 3.9, "ticket_mult": 0.72, "churn": 0.008, "credit_pref": 0.8},
    {"code": "occasional", "name": "Occasional User", "share": 0.242,
     "txn_rate": 0.9, "ticket_mult": 1.12, "churn": 0.024, "credit_pref": 0.6},
    {"code": "small_ticket", "name": "Small-Ticket Daily", "share": 0.104,
     "txn_rate": 4.4, "ticket_mult": 0.38, "churn": 0.013, "credit_pref": 0.3},
    {"code": "new", "name": "Newly Onboarded", "share": 0.036,
     "txn_rate": 1.5, "ticket_mult": 0.64, "churn": 0.041, "credit_pref": 0.4},
    {"code": "dormant_returning", "name": "Dormant / Returning", "share": 0.020,
     "txn_rate": 0.4, "ticket_mult": 0.88, "churn": 0.062, "credit_pref": 0.5},
]

# ---------------------------------------------------------------------------
# Failure taxonomy — real UPI/NPCI response codes with their business meaning.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class FailureCode:
    code: str
    reason: str
    bucket: str                 # technical | business | risk | timeout
    weight: float
    retryable: bool
    owner: str                  # who owns the fix: Issuer | PSP | NPCI | Customer


FAILURE_CODES: list[FailureCode] = [
    FailureCode("U30", "Debit failed at remitter bank", "technical", 0.146,
                True, "Issuer"),
    FailureCode("U16", "Risk threshold exceeded at remitter", "risk", 0.052,
                False, "Issuer"),
    FailureCode("U28", "Remitter bank unavailable", "technical", 0.088, True,
                "Issuer"),
    FailureCode("U54", "Transaction timed out at beneficiary", "timeout",
                0.074, True, "Issuer"),
    FailureCode("U69", "Beneficiary bank offline", "technical", 0.061, True,
                "Issuer"),
    FailureCode("Z9", "Insufficient funds", "business", 0.214, False,
                "Customer"),
    FailureCode("ZM", "Invalid UPI PIN", "business", 0.118, True, "Customer"),
    FailureCode("ZA", "Transaction declined by customer", "business", 0.062,
                False, "Customer"),
    FailureCode("XH", "Account does not exist / frozen", "business", 0.036,
                False, "Issuer"),
    FailureCode("YA", "PSP not available", "technical", 0.041, True, "PSP"),
    FailureCode("BT", "Acquirer / NPCI switch timeout", "timeout", 0.048, True,
                "NPCI"),
    FailureCode("U67", "Debit reversal timeout — credit not confirmed",
                "timeout", 0.021, True, "NPCI"),
    FailureCode("ZX", "Mandate not found or revoked", "business", 0.014, False,
                "PSP"),
    FailureCode("UX", "Mandate execution outside permitted window", "business",
                0.010, True, "PSP"),
    FailureCode("K1", "Suspected fraud — blocked by risk engine", "risk",
                0.009, False, "NPCI"),
    FailureCode("FX1", "FX rate quote expired", "technical", 0.003, True,
                "NPCI"),
    FailureCode("CL1", "Credit line limit exhausted", "business", 0.003, False,
                "Issuer"),
]

FAILURE_BY_BUCKET: dict[str, list[FailureCode]] = {}
for _f in FAILURE_CODES:
    FAILURE_BY_BUCKET.setdefault(_f.bucket, []).append(_f)

# AutoPay / mandate lifecycle event vocabulary.
MANDATE_EVENTS: tuple[str, ...] = (
    "MANDATE_CREATED", "MANDATE_MODIFIED", "MANDATE_PAUSED",
    "MANDATE_RESUMED", "MANDATE_REVOKED", "MANDATE_EXPIRED",
    "MANDATE_EXECUTED", "MANDATE_FAILED", "MANDATE_RETRY",
    "MANDATE_CANCELLED", "MERCHANT_INITIATED", "CUSTOMER_INITIATED",
    "PRE_DEBIT_NOTIFICATION",
)

MANDATE_FREQUENCIES: list[tuple[str, float, int]] = [
    # (frequency, share, days between executions)
    ("MONTHLY", 0.585, 30), ("WEEKLY", 0.088, 7), ("QUARTERLY", 0.072, 91),
    ("DAILY", 0.019, 1), ("HALF_YEARLY", 0.021, 182), ("YEARLY", 0.031, 365),
    ("AS_PRESENTED", 0.184, 0),
]

MANDATE_PURPOSES: list[tuple[str, str, float, float]] = [
    # (purpose, mcc, share, median amount)
    ("OTT Subscription", "5815", 0.212, 299.0),
    ("Mobile / DTH Recharge", "4814", 0.164, 399.0),
    ("Electricity Bill", "4900", 0.118, 1_840.0),
    ("Mutual Fund SIP", "6211", 0.156, 5_000.0),
    ("Insurance Premium", "6300", 0.086, 3_420.0),
    ("Loan EMI", "6012", 0.104, 8_650.0),
    ("EdTech Subscription", "8299", 0.048, 1_299.0),
    ("Gym & Wellness", "7230", 0.031, 1_499.0),
    ("Cloud / SaaS", "5815", 0.042, 749.0),
    ("Lite Auto Top-Up", "4814", 0.088, 1_000.0),
]


def entity_names(rows: list[dict]) -> list[str]:
    return [r["name"] for r in rows]
