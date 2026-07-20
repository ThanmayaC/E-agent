import pandas as pd

from app.domain.enums import RelationshipType
from app.intelligence.connectors.excel import ExtractedTable
from app.intelligence.profiling.profiler import ColumnProfiler
from app.intelligence.relationships.detector import RelationshipDetector
from app.intelligence.semantics.meaning import MeaningDetector


def test_fk_detected_despite_different_names():
    txns = pd.DataFrame({
        "Txn_ID": [f"T{i}" for i in range(200)],
        "MID": [f"M{i % 10:03d}" for i in range(200)],
        "Txn_Value": [float(i) for i in range(200)],
    })
    merchants = pd.DataFrame({
        "merchant_id": [f"M{i:03d}" for i in range(10)],
        "merchant_name": [f"Shop {i}" for i in range(10)],
    })
    profiler = ColumnProfiler()
    p1 = profiler.profile_table(ExtractedTable("txns", "a.xlsx", "s", 0, txns), "ds_txn")
    p2 = profiler.profile_table(ExtractedTable("merchants", "b.xlsx", "s", 0, merchants), "ds_mer")
    MeaningDetector().annotate([p1, p2])

    rels = RelationshipDetector().detect([p1, p2], {"ds_txn": txns, "ds_mer": merchants})
    fks = [r for r in rels if r.rel_type == RelationshipType.FOREIGN_KEY]
    assert fks, "expected an FK between MID and merchant_id"
    fk = fks[0]
    assert {fk.from_column, fk.to_column} == {"MID", "merchant_id"}
    assert fk.overlap >= 0.9
