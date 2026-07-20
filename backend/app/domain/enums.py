"""Domain enumerations shared across the platform."""
from enum import Enum


class SemanticType(str, Enum):
    IDENTIFIER = "identifier"
    DATE = "date"
    DATETIME = "datetime"
    MEASURE = "measure"
    CURRENCY = "currency"
    PERCENTAGE = "percentage"
    CATEGORY = "category"
    STATUS = "status"
    BOOLEAN = "boolean"
    TEXT = "text"
    GEO = "geo"
    CODE = "code"
    UNKNOWN = "unknown"


class ColumnRole(str, Enum):
    PRIMARY_KEY = "primary_key"
    FOREIGN_KEY = "foreign_key"
    TIME_DIMENSION = "time_dimension"
    DIMENSION = "dimension"
    MEASURE = "measure"
    ATTRIBUTE = "attribute"


class BusinessConcept(str, Enum):
    CUSTOMER = "Customer"
    MERCHANT = "Merchant"
    USER = "User"
    EMPLOYEE = "Employee"
    BANK = "Bank"
    PSP = "PSP"
    REGION = "Region"
    PRODUCT = "Product"
    CAMPAIGN = "Campaign"
    TRANSACTION = "Transaction"
    ORDER = "Order"
    PAYMENT = "Payment"
    SETTLEMENT = "Settlement"
    REVENUE = "Revenue"
    VOLUME = "Volume"
    VALUE = "Value"
    GROWTH = "Growth"
    RETENTION = "Retention"
    CONVERSION = "Conversion"
    ACTIVE_USERS = "Active Users"
    REGISTERED_USERS = "Registered Users"
    MARKET_SHARE = "Market Share"
    STATUS = "Status"
    DATE = "Date"
    CHANNEL = "Channel"
    CATEGORY = "Category"
    PRICE = "Price"
    QUANTITY = "Quantity"
    FEE = "Fee"
    UNKNOWN = "Unknown"


class TimeGrain(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"
    IRREGULAR = "irregular"


class RelationshipType(str, Enum):
    FOREIGN_KEY = "foreign_key"
    SHARED_DIMENSION = "shared_dimension"
    DATE_ALIGNMENT = "date_alignment"
    PARTITION_OF = "partition_of"
    HIERARCHY = "hierarchy"


class Cardinality(str, Enum):
    ONE_TO_ONE = "1:1"
    ONE_TO_MANY = "1:N"
    MANY_TO_MANY = "N:M"


class SignalKind(str, Enum):
    """Deterministic statistical signals — facts, never narrative."""
    TREND = "trend"
    SEASONALITY = "seasonality"
    ANOMALY = "anomaly"
    CONCENTRATION = "concentration"
    CORRELATION = "correlation"
    INVERSE_CORRELATION = "inverse_correlation"  # cannibalization candidate


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class PipelineStage(str, Enum):
    FILE_DISCOVERY = "file_discovery"
    WORKSHEET_DISCOVERY = "worksheet_discovery"
    SCHEMA_DISCOVERY = "schema_discovery"
    COLUMN_PROFILING = "column_profiling"
    BUSINESS_MEANING = "business_meaning"
    DEDUPLICATION = "deduplication"
    RELATIONSHIP_DETECTION = "relationship_detection"
    TIME_SERIES_DETECTION = "time_series_detection"
    KPI_DISCOVERY = "kpi_discovery"
    DATA_QUALITY = "data_quality"
    SEMANTIC_LAYER = "semantic_layer"
    KNOWLEDGE_GRAPH = "knowledge_graph"
    EMBEDDINGS = "embeddings"
    ANALYTICS = "analytics"
    SIGNALS = "signals"
    PREDICTIONS = "predictions"
    CONFIDENCE_ASSESSMENT = "confidence_assessment"
    BUSINESS_CONTEXT = "business_context"
    AI_REASONING = "ai_reasoning"
    REPORT = "report"


class StageStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
