"""Business ontology: concepts, their aliases, and classification metadata.

This is the vocabulary the platform uses to map raw column names
(cust_id, userid, cid ...) onto business concepts (Customer).
Extend it via configuration — nothing else in the codebase references raw names.
"""
from app.domain.enums import BusinessConcept

# concept -> list of alias fragments (normalized snake_case, matched fuzzily too)
CONCEPT_ALIASES: dict[BusinessConcept, list[str]] = {
    # In payments schemas the paying party IS the customer — `payer`,
    # `payeraddress` (a VPA) and `prdmobile` identify a person just as surely
    # as `customer_id` does. Without these aliases the platform reports
    # "no customer-level data" while holding 34k distinct payer identities.
    BusinessConcept.CUSTOMER: [
        "customer", "cust", "cust_id", "customer_id", "customer_no", "consumer",
        "cid", "client", "buyer", "shopper", "account_holder", "userid_customer",
        "payer", "payer_address", "payeraddress", "payer_vpa", "vpa", "remitter",
        "sender", "prdmobile", "msisdn", "mobile", "payer_mobile", "payer_bank",
    ],
    BusinessConcept.USER: ["user", "user_id", "userid", "uid", "member", "subscriber"],
    BusinessConcept.MERCHANT: [
        "merchant", "mid", "merchant_id", "seller", "vendor", "store", "shop",
        "retailer", "supplier", "partner",
        # NB: MCC is a merchant *category*, not a merchant identity — it stays
        # under CATEGORY so it is never counted as "active merchants".
        "payee", "payee_name", "payeename", "payee_address", "payeeaddress",
        "payee_merchant", "beneficiary",
    ],
    BusinessConcept.EMPLOYEE: ["employee", "emp", "emp_id", "staff", "agent", "worker"],
    BusinessConcept.BANK: ["bank", "bank_name", "issuer", "acquirer", "ifsc", "branch",
                           "payer_bank", "payerbank", "payee_bank", "payeebank",
                           "remitter_org", "remitterorgid", "beneficiary_bank"],
    BusinessConcept.PSP: ["psp", "gateway", "payment_gateway", "aggregator", "processor",
                          "payer_psp", "payerpsp", "payee_psp", "payeepsp",
                          "psp_org", "psporgid", "initiator_psp"],
    BusinessConcept.REGION: [
        "region", "zone", "state", "country", "city", "territory", "geo",
        "location", "area", "district", "market",
    ],
    BusinessConcept.PRODUCT: ["product", "sku", "item", "prod", "product_id", "product_name", "plan", "package"],
    BusinessConcept.CAMPAIGN: ["campaign", "promo", "promotion", "offer", "coupon", "ad", "creative"],
    BusinessConcept.TRANSACTION: [
        "transaction", "txn", "trans", "txn_id", "transaction_id", "payment_id",
        "order_txn", "trace", "rrn", "utr",
    ],
    BusinessConcept.ORDER: ["order", "order_id", "order_no", "purchase", "booking", "invoice"],
    BusinessConcept.PAYMENT: ["payment", "pay", "pay_mode", "payment_mode", "method", "instrument", "upi", "card", "wallet", "netbanking"],
    BusinessConcept.SETTLEMENT: ["settlement", "settle", "payout", "disbursement", "remittance"],
    BusinessConcept.REVENUE: [
        "revenue", "rev", "income", "earnings", "gmv", "sales", "sales_amount",
        "amount", "amt", "txn_value", "txn_amount", "transaction_value", "total_value", "net_amount", "gross_amount", "turnover",
    ],
    BusinessConcept.VOLUME: ["volume", "vol", "count", "txn_count", "transactions", "num_txn", "no_of_txn", "orders_count", "units", "quantity_sold"],
    BusinessConcept.VALUE: ["value", "ticket_size", "avg_ticket", "aov", "average_order_value"],
    BusinessConcept.GROWTH: ["growth", "growth_rate", "yoy", "mom", "qoq", "cagr", "increase"],
    BusinessConcept.RETENTION: ["retention", "retained", "churn", "repeat", "repeat_rate", "returning"],
    BusinessConcept.CONVERSION: ["conversion", "convert", "cvr", "funnel", "success_rate", "activation"],
    BusinessConcept.ACTIVE_USERS: ["active_users", "dau", "mau", "wau", "active", "monthly_active", "daily_active", "mtu"],
    BusinessConcept.REGISTERED_USERS: ["registered", "registrations", "signups", "sign_ups", "onboarded", "new_users", "enrolled"],
    BusinessConcept.MARKET_SHARE: ["market_share", "share", "share_pct", "penetration"],
    BusinessConcept.STATUS: ["status", "state", "result", "outcome", "success", "failure", "failed", "declined", "response_code"],
    BusinessConcept.DATE: ["date", "day", "month", "year", "week", "period", "time", "timestamp", "created_at", "txn_date", "order_date"],
    BusinessConcept.CHANNEL: ["channel", "source", "medium", "platform", "device", "app", "web"],
    BusinessConcept.CATEGORY: ["category", "cat", "segment", "type", "class", "group", "tier", "mcc"],
    BusinessConcept.PRICE: ["price", "unit_price", "rate_card", "mrp", "list_price"],
    BusinessConcept.QUANTITY: ["quantity", "qty", "units", "count_of_items"],
    BusinessConcept.FEE: ["fee", "mdr", "commission", "charge", "surcharge", "tax", "gst"],
}

# concepts that represent business entities (graph nodes / dimension tables)
ENTITY_CONCEPTS = {
    BusinessConcept.CUSTOMER, BusinessConcept.USER, BusinessConcept.MERCHANT,
    BusinessConcept.EMPLOYEE, BusinessConcept.BANK, BusinessConcept.PSP,
    BusinessConcept.REGION, BusinessConcept.PRODUCT, BusinessConcept.CAMPAIGN,
    BusinessConcept.TRANSACTION, BusinessConcept.ORDER, BusinessConcept.PAYMENT,
    BusinessConcept.SETTLEMENT, BusinessConcept.CHANNEL, BusinessConcept.CATEGORY,
}

# concepts that are financial / KPI-bearing metrics
METRIC_CONCEPTS = {
    BusinessConcept.REVENUE, BusinessConcept.VOLUME, BusinessConcept.VALUE,
    BusinessConcept.GROWTH, BusinessConcept.RETENTION, BusinessConcept.CONVERSION,
    BusinessConcept.ACTIVE_USERS, BusinessConcept.REGISTERED_USERS,
    BusinessConcept.MARKET_SHARE, BusinessConcept.PRICE, BusinessConcept.QUANTITY,
    BusinessConcept.FEE,
}
