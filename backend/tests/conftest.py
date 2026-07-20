import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.intelligence.connectors.excel import ExtractedTable  # noqa: E402


@pytest.fixture()
def txn_frame() -> pd.DataFrame:
    dates = pd.date_range("2024-01-01", periods=400, freq="D")
    return pd.DataFrame({
        "Txn_ID": [f"T{i:06d}" for i in range(400)],
        "Txn_Date": dates,
        "Cust_ID": [f"C{i % 60:04d}" for i in range(400)],
        "Txn_Value": [100 + (i % 50) * 10.5 for i in range(400)],
        "Status": ["SUCCESS" if i % 10 else "FAILED" for i in range(400)],
        "Region": ["North", "South", "East", "West"][0:1] * 400,
    })


@pytest.fixture()
def txn_table(txn_frame) -> ExtractedTable:
    return ExtractedTable(name="txns", source_file="t.xlsx", source_sheet="s1",
                          header_row=0, df=txn_frame)
