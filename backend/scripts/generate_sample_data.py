"""Generate realistic sample Excel workbooks for demos and tests.

Creates a fintech-style portfolio with deliberately messy characteristics:
different column naming conventions per file, monthly partitions, merged
header cells, a hidden sheet, missing values, and outliers — so every stage
of the automatic-understanding pipeline is exercised.
"""
from __future__ import annotations

import random
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

random.seed(42)
np.random.seed(42)

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "sample_data"

MERCHANT_NAMES = ["ZapMart", "FreshKart", "UrbanEats", "SkyPay Retail", "NovaBazaar",
                  "PixelStore", "GreenGrocer", "MetroMart", "BlueWave", "QuickShip",
                  "SunCart", "AlphaMart", "OmegaStores", "CityFoods", "PrimeGoods"]
BANKS = ["HDFC", "ICICI", "SBI", "Axis", "Kotak"]
REGIONS = ["North", "South", "East", "West"]
CHANNELS = ["UPI", "Card", "NetBanking", "Wallet"]
STATUSES = ["SUCCESS"] * 88 + ["FAILED"] * 9 + ["TIMEOUT"] * 3


def month_range(start: date, months: int):
    d = start
    for _ in range(months):
        yield d
        d = (d.replace(day=28) + timedelta(days=4)).replace(day=1)


def build_transactions(months: int = 24) -> pd.DataFrame:
    rows = []
    txn_id = 100000
    for i, month in enumerate(month_range(date(2024, 1, 1), months)):
        # growth trend + seasonality (festive Q4 peak) + noise
        base = 900 + i * 40
        seasonal = 1.35 if month.month in (10, 11) else (0.85 if month.month == 2 else 1.0)
        count = int(base * seasonal * np.random.uniform(0.92, 1.08))
        for _ in range(count):
            txn_id += 1
            m_idx = np.random.zipf(1.6) % len(MERCHANT_NAMES)  # concentration: few big merchants
            day = min(month.day + random.randint(0, 27), 28)
            rows.append({
                "Txn_ID": f"T{txn_id}",
                "Txn_Date": month.replace(day=day),
                "Cust_ID": f"C{random.randint(1, 4000):05d}",
                "MID": f"M{m_idx + 1:03d}",
                "Bank_Name": random.choice(BANKS),
                "Pay_Mode": random.choices(CHANNELS, weights=[55, 25, 10, 10])[0],
                "Txn_Value": round(abs(np.random.lognormal(6.2, 0.9)), 2),
                "Status": random.choice(STATUSES),
            })
    df = pd.DataFrame(rows)
    # inject quality issues: missing values + one wild outlier
    df.loc[df.sample(frac=0.02, random_state=1).index, "Bank_Name"] = None
    df.loc[df.index[100], "Txn_Value"] = 9_500_000.0
    return df


def build_merchants() -> pd.DataFrame:
    return pd.DataFrame([{
        "merchant_id": f"M{i + 1:03d}",
        "merchant_name": name,
        "Category": random.choice(["Grocery", "Food", "Electronics", "Fashion", "Travel"]),
        "Region": random.choice(REGIONS),
        "onboard_date": date(2023, random.randint(1, 12), random.randint(1, 28)),
        "mdr_pct": round(random.uniform(0.8, 2.4), 2),
    } for i, name in enumerate(MERCHANT_NAMES)])


def build_customers() -> pd.DataFrame:
    return pd.DataFrame([{
        "customer_no": f"C{i:05d}",
        "region": random.choice(REGIONS),
        "signup_month": random.choice(list(month_range(date(2023, 6, 1), 18))),
        "segment": random.choices(["Mass", "Affluent", "Premium"], weights=[70, 22, 8])[0],
    } for i in range(1, 4001)])


def build_active_users(months: int = 24) -> pd.DataFrame:
    rows = []
    mau = 52000
    for i, month in enumerate(month_range(date(2024, 1, 1), months)):
        mau = int(mau * np.random.uniform(1.005, 1.03))
        dip = 0.93 if i == months - 2 else 1.0  # recent dip -> anomaly insight
        rows.append({
            "Month": month,
            "MAU": int(mau * dip),
            "DAU": int(mau * dip * np.random.uniform(0.28, 0.33)),
            "New_Registrations": int(2600 + i * 55 * np.random.uniform(0.8, 1.2)),
            "Retention_Rate_Pct": round(np.random.uniform(61, 68) * dip, 1),
        })
    return rows and pd.DataFrame(rows)


def write_plain(df: pd.DataFrame, path: Path, sheet: str) -> None:
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        df.to_excel(xl, sheet_name=sheet, index=False)


def write_messy_workbook(df_q1: pd.DataFrame, df_q2: pd.DataFrame, path: Path) -> None:
    """Workbook with a merged title cell, two partition sheets, and a hidden sheet."""
    wb = Workbook()
    for sheet_name, frame in [("Jan-Jun Txns", df_q1), ("Jul-Dec Txns", df_q2)]:
        ws = wb.create_sheet(sheet_name)
        ws.merge_cells("A1:D1")
        ws["A1"] = "SkyPay Payments — Transaction Extract (confidential)"
        ws.append([])
        for row in dataframe_to_rows(frame, index=False, header=True):
            ws.append(row)
    hidden = wb.create_sheet("Reconciliation_WIP")
    hidden.append(["note", "internal draft — ignore"])
    hidden.sheet_state = "hidden"
    del wb["Sheet"]
    wb.save(path)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    txns = build_transactions()
    txns["Txn_Date"] = pd.to_datetime(txns["Txn_Date"])
    mid = txns["Txn_Date"] < pd.Timestamp(2025, 1, 1)

    # transactions split across two files with a messy layout in one
    write_messy_workbook(
        txns[mid & (txns["Txn_Date"].dt.month <= 6)],
        txns[mid & (txns["Txn_Date"].dt.month > 6)],
        OUT / "transactions_2024.xlsx",
    )
    write_plain(txns[~mid], OUT / "transactions_2025.xlsx", "txn_data")

    write_plain(build_merchants(), OUT / "merchant_master.xlsx", "Merchants")
    write_plain(build_customers(), OUT / "customer_master.xlsx", "Customers")
    write_plain(build_active_users(), OUT / "growth_metrics.xlsx", "Monthly KPIs")
    print(f"Sample data written to {OUT.resolve()}  ({len(txns):,} transactions)")


if __name__ == "__main__":
    main()
