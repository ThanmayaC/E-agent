from app.domain.entities import ColumnProfile
from app.domain.enums import BusinessConcept, SemanticType
from app.intelligence.semantics.meaning import MeaningDetector


def _col(name: str, sem: SemanticType = SemanticType.TEXT) -> ColumnProfile:
    from app.intelligence.profiling.profiler import normalize_name
    return ColumnProfile(name=name, normalized_name=normalize_name(name),
                         dtype="object", semantic_type=sem)


def test_customer_aliases_all_map_to_customer():
    detector = MeaningDetector()
    for alias in ["cust_id", "customer", "customer_no", "cid", "consumer"]:
        concept, conf = detector.detect(_col(alias, SemanticType.IDENTIFIER))
        assert concept == BusinessConcept.CUSTOMER, alias
        assert conf > 0.5


def test_userid_maps_to_user():
    concept, _ = MeaningDetector().detect(_col("userid", SemanticType.IDENTIFIER))
    assert concept == BusinessConcept.USER


def test_revenue_detection():
    concept, _ = MeaningDetector().detect(_col("Txn_Value", SemanticType.CURRENCY))
    assert concept == BusinessConcept.REVENUE


def test_token_containment():
    concept, _ = MeaningDetector().detect(_col("merchant_growth_txn_value", SemanticType.MEASURE))
    assert concept in (BusinessConcept.REVENUE, BusinessConcept.MERCHANT, BusinessConcept.GROWTH)
