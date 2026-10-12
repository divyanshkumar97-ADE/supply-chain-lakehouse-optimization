"""Deterministic, testable data-quality rules."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from supply_chain.contracts import ALLOWED_SHIPMENT_EVENT_TYPES, SHIPMENT_EVENT_REQUIRED_FIELDS


def is_non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_positive_number(value: object) -> bool:
    try:
        return float(value) > 0
    except (TypeError, ValueError):
        return False


def is_non_negative_integer(value: object) -> bool:
    try:
        numeric = int(value)
        return numeric >= 0 and str(value).strip() in {str(numeric), f"{numeric}.0"}
    except (TypeError, ValueError):
        return False


def is_iso_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def classify_shipment_event(record: dict[str, Any]) -> list[str]:
    """Return all rejection reasons for a shipment event."""
    issues: list[str] = []
    for field in SHIPMENT_EVENT_REQUIRED_FIELDS:
        if record.get(field) is None or (
            isinstance(record.get(field), str) and not record[field].strip()
        ):
            issues.append(f"missing_{field}")

    if record.get("event_timestamp") is not None and not is_iso_timestamp(
        record["event_timestamp"]
    ):
        issues.append("invalid_event_timestamp")

    event_type = record.get("event_type")
    if event_type and event_type not in ALLOWED_SHIPMENT_EVENT_TYPES:
        issues.append("unknown_event_type")

    return issues


def classify_inventory_record(record: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if not is_non_empty_string(record.get("inventory_id")):
        issues.append("missing_inventory_id")
    if not is_non_empty_string(record.get("product_id")):
        issues.append("missing_product_id")
    if not is_non_empty_string(record.get("warehouse_id")):
        issues.append("missing_warehouse_id")
    try:
        if int(record.get("on_hand_quantity")) < 0:
            issues.append("negative_on_hand_quantity")
    except (TypeError, ValueError):
        issues.append("invalid_on_hand_quantity")
    try:
        if int(record.get("reorder_threshold")) < 0:
            issues.append("negative_reorder_threshold")
    except (TypeError, ValueError):
        issues.append("invalid_reorder_threshold")
    if not is_iso_timestamp(record.get("snapshot_timestamp")):
        issues.append("invalid_snapshot_timestamp")
    return issues
