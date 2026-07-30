"""Customer and merchant populations.

Analytics that matter — retention, cohorts, adoption, dormancy, merchant
concentration — only exist if the *same* customers and merchants recur across
days with stable characteristics. So the population is built once, up front,
with per-entity attributes (segment, home city, primary bank/PSP, onboarding
day, activity weight) and every transaction indexes into it.

Activity follows a heavy-tailed distribution: a small share of customers and a
small share of merchants carry most of the volume, which is what makes
concentration metrics and Pareto analysis meaningful.
"""
from __future__ import annotations

import numpy as np

from app.warehouse.generator.catalog import (
    BANKS, CITIES, MCCS, PSPS, SEGMENTS,
)

_MERCHANT_PREFIXES = [
    "Bharat", "Shakti", "Metro", "Prime", "Swift", "Urban", "Nova", "Kaveri",
    "Sundar", "Vega", "Anand", "Rapid", "Sahyadri", "Trinetra", "Konark",
    "Aravalli", "Deccan", "Malabar", "Nilgiri", "Chola", "Vindhya", "Zenith",
    "Kalinga", "Rohini", "Sarita", "Tejas", "Ujjwal", "Vasant", "Yamuna",
    "Ashoka", "Bharati", "Chandra", "Dhruva", "Girnar", "Hampi", "Indus",
]
_MERCHANT_SUFFIX = {
    "Grocery": ["Mart", "Bazaar", "Fresh", "Stores", "Supermart"],
    "Food Delivery": ["Kitchen", "Bites", "Express", "Foods", "Tiffin"],
    "Dining": ["Diner", "Kitchen", "Restaurant", "Cafe", "Grill"],
    "Fuel": ["Fuels", "Petro", "Energy", "Filling Station"],
    "Ride Hailing": ["Rides", "Cabs", "Mobility", "Go"],
    "General Retail": ["Retail", "Stores", "Trading", "Emporium"],
    "Fashion": ["Styles", "Wardrobe", "Apparel", "Threads", "Couture"],
    "Electronics": ["Electronics", "Gadgets", "Digital", "Tech"],
    "Pharmacy": ["Pharmacy", "Medicos", "Health", "Chemists"],
    "Hospitals": ["Hospital", "Healthcare", "Medical Centre", "Clinic"],
    "Utilities": ["Power", "Utilities", "Energy", "Water Board"],
    "Mobile & DTH Recharge": ["Telecom", "Mobile", "Connect", "Broadband"],
    "Insurance": ["Insurance", "Assurance", "Life", "General Insurance"],
    "Wealth & SIP": ["Capital", "Wealth", "Mutual", "Investments"],
    "Loan & EMI": ["Finance", "Credit", "Lending", "Capital"],
    "Travel Booking": ["Travels", "Holidays", "Journeys", "Tours"],
    "Airlines": ["Airways", "Air", "Aviation"],
    "Hotels": ["Hotels", "Residency", "Inn", "Suites"],
    "Speciality": ["Specials", "Boutique", "Collection", "House"],
    "Gaming": ["Games", "Play", "Arena", "Interactive"],
    "OTT & Subscriptions": ["Stream", "Play", "Originals", "Studios"],
    "Education Fees": ["Institute", "College", "Academy", "University"],
    "EdTech": ["Learn", "Academy", "Tutorials", "Classes"],
    "Salon & Spa": ["Salon", "Spa", "Studio", "Wellness"],
    "Parking & Tolls": ["Parking", "Tollway", "Plaza"],
    "Footwear": ["Footwear", "Shoes", "Steps"],
}


class Population:
    """Immutable customer + merchant universe for the whole simulation."""

    def __init__(self, rng: np.random.Generator, days: int,
                 n_customers: int = 80_000, n_merchants: int = 2_400):
        self.rng = rng
        self.days = days
        self.n_customers = n_customers
        self.n_merchants = n_merchants
        self._build_customers()
        self._build_merchants()

    # ----------------------------------------------------------- customers
    def _build_customers(self) -> None:
        rng, n = self.rng, self.n_customers
        seg_share = np.array([s["share"] for s in SEGMENTS], dtype=float)
        seg_share /= seg_share.sum()
        self.cust_segment = rng.choice(len(SEGMENTS), size=n, p=seg_share)

        city_w = np.array([c[3] for c in CITIES], dtype=float)
        city_w /= city_w.sum()
        self.cust_city = rng.choice(len(CITIES), size=n, p=city_w)

        bank_w = np.array([b["share"] for b in BANKS], dtype=float)
        bank_w /= bank_w.sum()
        self.cust_bank = rng.choice(len(BANKS), size=n, p=bank_w)

        psp_w = np.array([p["share"] for p in PSPS], dtype=float)
        psp_w /= psp_w.sum()
        self.cust_psp = rng.choice(len(PSPS), size=n, p=psp_w)

        # 72% were already on the platform before the window opened; the rest
        # onboard across it, weighted to later days (adoption is accelerating).
        pre_existing = rng.random(n) < 0.72
        onboard = np.where(
            pre_existing, -rng.integers(1, 900, size=n),
            (rng.beta(1.35, 1.0, size=n) * self.days).astype(int))
        self.cust_onboard_day = onboard

        # Heavy-tailed activity: lognormal weight scaled by the segment rate.
        seg_rate = np.array([s["txn_rate"] for s in SEGMENTS])[self.cust_segment]
        self.cust_weight = seg_rate * rng.lognormal(0.0, 0.62, size=n)

        # Per-customer dormancy: a start day and length for a quiet spell.
        has_gap = rng.random(n) < 0.22
        gap_start = rng.integers(0, max(1, self.days - 10), size=n)
        gap_len = (rng.gamma(2.0, 7.0, size=n)).astype(int) + 3
        self.cust_gap_start = np.where(has_gap, gap_start, self.days + 1)
        self.cust_gap_end = self.cust_gap_start + gap_len

        # Churn: a fraction leave permanently partway through.
        churn_p = np.array([s["churn"] for s in SEGMENTS])[self.cust_segment]
        churned = rng.random(n) < churn_p * (self.days / 30.0)
        self.cust_churn_day = np.where(
            churned, rng.integers(int(self.days * 0.25), self.days, size=n),
            self.days + 1)

        self.cust_credit_pref = np.array(
            [s["credit_pref"] for s in SEGMENTS])[self.cust_segment]
        self.cust_ticket_mult = np.array(
            [s["ticket_mult"] for s in SEGMENTS])[self.cust_segment] * \
            rng.lognormal(0.0, 0.28, size=n)

    def active_weights(self, day: int) -> np.ndarray:
        """Per-customer sampling weight for one day — zero if not yet
        onboarded, churned, or inside a dormancy gap."""
        w = self.cust_weight.copy()
        w[self.cust_onboard_day > day] = 0.0
        w[self.cust_churn_day <= day] = 0.0
        in_gap = (self.cust_gap_start <= day) & (day < self.cust_gap_end)
        w[in_gap] *= 0.06          # not fully silent — dormant, not deleted
        return w

    # ----------------------------------------------------------- merchants
    def _build_merchants(self) -> None:
        rng, n = self.rng, self.n_merchants
        mcc_w = np.array([m.share for m in MCCS], dtype=float)
        mcc_w /= mcc_w.sum()
        self.merch_mcc = rng.choice(len(MCCS), size=n, p=mcc_w)

        city_w = np.array([c[3] for c in CITIES], dtype=float)
        city_w /= city_w.sum()
        self.merch_city = rng.choice(len(CITIES), size=n, p=city_w)

        psp_w = np.array([p["share"] for p in PSPS], dtype=float)
        psp_w /= psp_w.sum()
        self.merch_psp = rng.choice(len(PSPS), size=n, p=psp_w)

        bank_w = np.array([b["share"] for b in BANKS], dtype=float)
        bank_w /= bank_w.sum()
        self.merch_bank = rng.choice(len(BANKS), size=n, p=bank_w)

        # Merchant size follows a Pareto: the top ~2% carry ~35% of volume.
        self.merch_weight = rng.pareto(1.35, size=n) + 0.08
        tier_cut = np.quantile(self.merch_weight, [0.70, 0.93, 0.99])
        self.merch_tier = np.digitize(self.merch_weight, tier_cut)  # 0..3

        self.merch_onboard_day = np.where(
            rng.random(n) < 0.80, -rng.integers(1, 700, size=n),
            (rng.beta(1.2, 1.0, size=n) * self.days).astype(int))

        # A handful of merchants behave abnormally: sudden volume explosions
        # (possible laundering / mis-categorisation) or abrupt shutdowns.
        self.merch_anomaly = np.zeros(n, dtype=np.int8)
        self.merch_anomaly_day = np.full(n, self.days + 1)
        n_anom = max(6, n // 160)
        idx = rng.choice(n, size=n_anom, replace=False)
        kinds = rng.choice([1, 2, 3], size=n_anom, p=[0.42, 0.33, 0.25])
        self.merch_anomaly[idx] = kinds        # 1=surge 2=shutdown 3=churn-back
        self.merch_anomaly_day[idx] = rng.integers(
            int(self.days * 0.15), self.days - 3, size=n_anom)

        names, ids = [], []
        used: set[str] = set()
        for i in range(n):
            sub = MCCS[self.merch_mcc[i]].subcategory
            suf = _MERCHANT_SUFFIX.get(sub, ["Services"])
            for _ in range(24):
                nm = (f"{_MERCHANT_PREFIXES[rng.integers(len(_MERCHANT_PREFIXES))]}"
                      f" {suf[rng.integers(len(suf))]}")
                if nm not in used:
                    break
            if nm in used:
                nm = f"{nm} {i}"
            used.add(nm)
            names.append(nm)
            ids.append(f"MID-{100000 + i}")
        self.merch_name = np.array(names, dtype=object)
        self.merch_id = np.array(ids, dtype=object)

        # Per-MCC merchant index, for affinity-weighted merchant selection.
        self.merch_by_mcc: dict[int, np.ndarray] = {}
        self.merch_w_by_mcc: dict[int, np.ndarray] = {}
        for mi in range(len(MCCS)):
            sel = np.flatnonzero(self.merch_mcc == mi)
            if len(sel) == 0:                    # guarantee every MCC is live
                sel = rng.choice(n, size=3, replace=False)
                self.merch_mcc[sel] = mi
            self.merch_by_mcc[mi] = sel
            self.merch_w_by_mcc[mi] = self.merch_weight[sel]

    def merchant_day_weights(self, day: int) -> np.ndarray:
        w = self.merch_weight.copy()
        w[self.merch_onboard_day > day] = 0.0
        live = self.merch_anomaly_day <= day
        w[live & (self.merch_anomaly == 1)] *= 6.5      # abnormal surge
        w[live & (self.merch_anomaly == 2)] = 0.0       # abrupt shutdown
        w[live & (self.merch_anomaly == 3)] *= 0.12     # sharp decline
        return w

    # ------------------------------------------------------------- exports
    def customer_rows(self, start_date) -> list[dict]:
        from datetime import timedelta
        out = []
        for i in range(self.n_customers):
            ob = int(self.cust_onboard_day[i])
            out.append({
                "customer_id": f"CUST-{500000 + i}",
                "segment": SEGMENTS[self.cust_segment[i]]["code"],
                "segment_name": SEGMENTS[self.cust_segment[i]]["name"],
                "city": CITIES[self.cust_city[i]][0],
                "state": CITIES[self.cust_city[i]][1],
                "region": CITIES[self.cust_city[i]][2],
                "city_tier": CITIES[self.cust_city[i]][4],
                "primary_bank": BANKS[self.cust_bank[i]]["name"],
                "primary_psp": PSPS[self.cust_psp[i]]["name"],
                "onboarded_date": str(start_date + timedelta(days=ob)),
                "is_pre_window": ob < 0,
                "activity_weight": round(float(self.cust_weight[i]), 4),
                "churn_day": int(self.cust_churn_day[i])
                if self.cust_churn_day[i] <= self.days else None,
            })
        return out

    def merchant_rows(self, start_date) -> list[dict]:
        from datetime import timedelta
        tier_name = {0: "Long Tail", 1: "Mid Market", 2: "Large", 3: "Key Account"}
        anom_name = {0: None, 1: "volume_surge", 2: "abrupt_shutdown",
                     3: "sharp_decline"}
        out = []
        for i in range(self.n_merchants):
            m = MCCS[self.merch_mcc[i]]
            ob = int(self.merch_onboard_day[i])
            out.append({
                "merchant_id": self.merch_id[i],
                "merchant_name": self.merch_name[i],
                "mcc": m.code,
                "mcc_name": m.name,
                "category": m.category,
                "subcategory": m.subcategory,
                "city": CITIES[self.merch_city[i]][0],
                "state": CITIES[self.merch_city[i]][1],
                "region": CITIES[self.merch_city[i]][2],
                "acquiring_psp": PSPS[self.merch_psp[i]]["name"],
                "settlement_bank": BANKS[self.merch_bank[i]]["name"],
                "size_tier": tier_name[int(self.merch_tier[i])],
                "onboarded_date": str(start_date + timedelta(days=ob)),
                "risk_index": round(float(m.risk), 3),
                "behaviour_flag": anom_name[int(self.merch_anomaly[i])],
                "behaviour_change_day": int(self.merch_anomaly_day[i])
                if self.merch_anomaly[i] else None,
            })
        return out
