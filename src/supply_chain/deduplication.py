"""Pure-Python reference helpers for deterministic deduplication tests."""

from __future__ import annotations

from typing import Any


def deduplicate_by_latest(
    records: list[dict[str, Any]],
    key: str,
    order_by: str,
) -> list[dict[str, Any]]:
    """Keep the latest record per key; ties are resolved by later input order."""
    latest: dict[object, dict[str, Any]] = {}
    for record in records:
        record_key = record.get(key)
        if record_key is None:
            continue
        current = latest.get(record_key)
        if current is None or str(record.get(order_by, "")) >= str(current.get(order_by, "")):
            latest[record_key] = record
    return list(latest.values())
