import pandas as pd

from app.intelligence.dedup.merger import DatasetMerger
from app.intelligence.connectors.excel import ExtractedTable


def _table(name: str, offset: int) -> ExtractedTable:
    df = pd.DataFrame({
        "Order_ID": [f"O{offset + i}" for i in range(50)],
        "Amount": [float(i) for i in range(50)],
        "Order Date": pd.date_range("2024-01-01", periods=50),
    })
    return ExtractedTable(name=name, source_file=f"{name}.xlsx", source_sheet="s", header_row=0, df=df)


def test_monthly_partitions_are_merged():
    tables = [_table("jan_sales", 0), _table("feb_sales", 100), _table("mar_sales", 200)]
    merged, lineage = DatasetMerger().merge(tables)
    assert len(merged) == 1
    assert merged[0].name == "sales"
    assert len(merged[0].df) == 150
    assert set(lineage["sales"]) == {"jan_sales", "feb_sales", "mar_sales"}


def test_different_schemas_not_merged():
    a = _table("jan_sales", 0)
    b = ExtractedTable("users", "u.xlsx", "s", 0,
                       pd.DataFrame({"user_id": [1, 2], "email": ["a@x.com", "b@x.com"]}))
    merged, _ = DatasetMerger().merge([a, b])
    assert len(merged) == 2
