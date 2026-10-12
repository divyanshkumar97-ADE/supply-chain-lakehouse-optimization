"""Lightweight source contracts; Spark schemas will be defined in Databricks notebooks."""

SHIPMENT_EVENT_REQUIRED_FIELDS = (
    "event_id",
    "shipment_id",
    "event_type",
    "event_timestamp",
    "warehouse_id",
)

ORDER_REQUIRED_FIELDS = (
    "order_id",
    "product_id",
    "warehouse_id",
    "quantity",
    "unit_cost",
    "order_timestamp",
)

INVENTORY_REQUIRED_FIELDS = (
    "inventory_id",
    "product_id",
    "warehouse_id",
    "on_hand_quantity",
    "reorder_threshold",
    "snapshot_timestamp",
)

ALLOWED_SHIPMENT_EVENT_TYPES = frozenset(
    {"CREATED", "PICKED", "SHIPPED", "IN_TRANSIT", "DELIVERED", "DELAYED"}
)
