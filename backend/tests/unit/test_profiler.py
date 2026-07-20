from app.domain.enums import ColumnRole, SemanticType
from app.intelligence.profiling.profiler import ColumnProfiler, normalize_name


def test_normalize_name():
    assert normalize_name("Cust ID") == "cust_id"
    assert normalize_name("TxnValue") == "txn_value"
    assert normalize_name("MAU (%)") == "mau"


def test_profile_detects_types(txn_table):
    profile = ColumnProfiler().profile_table(txn_table, "ds1")
    by_name = {c.name: c for c in profile.columns}

    assert by_name["Txn_ID"].semantic_type == SemanticType.IDENTIFIER
    assert by_name["Txn_ID"].is_pk_candidate
    assert by_name["Txn_ID"].role == ColumnRole.PRIMARY_KEY
    assert by_name["Txn_Date"].semantic_type in (SemanticType.DATE, SemanticType.DATETIME)
    assert by_name["Txn_Value"].role == ColumnRole.MEASURE
    assert by_name["Status"].semantic_type == SemanticType.STATUS
    assert profile.row_count == 400


def test_currency_strings_coerced():
    import pandas as pd
    from app.intelligence.connectors.excel import ExtractedTable

    df = pd.DataFrame({"Amount": ["$1,200.50", "$980.00", "$1,405.75", "$2,001.00"]})
    t = ExtractedTable(name="x", source_file="f", source_sheet="s", header_row=0, df=df)
    profile = ColumnProfiler().profile_table(t, "ds")
    assert profile.columns[0].semantic_type == SemanticType.CURRENCY
