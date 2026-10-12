"""Deterministic synthetic supply-chain dataset generator."""

from __future__ import annotations

import random
from datetime import UTC, datetime, timedelta
from typing import Any


def generate_datasets(rows: int, seed: int = 42) -> dict[str, list[dict[str, Any]]]:
    if rows < 1:
        raise ValueError("rows must be at least 1")

    rng = random.Random(seed)
    start = datetime(2026, 1, 1, 8, 0, tzinfo=UTC)
    orders: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    inventory: list[dict[str, Any]] = []
    event_types = ["CREATED", "PICKED", "SHIPPED", "IN_TRANSIT", "DELIVERED"]

    for i in range(1, rows + 1):
        order_id = f"ORD-{i:08d}"
        shipment_id = f"SHP-{i:08d}"
        product_id = f"SKU-{rng.randint(1, max(20, rows // 5)):05d}"
        warehouse_id = f"WH-{rng.randint(1, 12):03d}"
        order_time = start + timedelta(minutes=rng.randint(0, 60 * 24 * 90))

        orders.append({
            "order_id": order_id,
            "product_id": product_id,
            "warehouse_id": warehouse_id,
            "quantity": rng.randint(1, 25),
            "unit_cost": round(rng.uniform(4.0, 500.0), 2),
            "order_timestamp": order_time.isoformat(),
        })

        for seq, event_type in enumerate(event_types[: rng.randint(2, 5)]):
            event_time = order_time + timedelta(hours=seq * rng.randint(1, 8))
            events.append({
                "event_id": f"EVT-{i:08d}-{seq + 1}",
                "shipment_id": shipment_id,
                "order_id": order_id,
                "event_type": event_type,
                "event_timestamp": event_time.isoformat(),
                "warehouse_id": warehouse_id,
                "source_system": rng.choice(["WMS_A", "TMS_B", "CARRIER_API"]),
                "source_batch_id": f"BATCH-{(i - 1) // 250 + 1:05d}",
            })

        inventory.append({
            "inventory_id": f"INV-{i:08d}",
            "product_id": product_id,
            "warehouse_id": warehouse_id,
            "on_hand_quantity": rng.randint(0, 1000),
            "reorder_threshold": rng.randint(20, 150),
            "snapshot_timestamp": order_time.isoformat(),
        })

    # Intentional data issues are deterministic and easy to test.
    if events:
        events[0]["event_timestamp"] = "not-a-timestamp"
        if len(events) > 1:
            duplicate = events[1].copy()
            duplicate["source_batch_id"] = "BATCH-REPLAY"
            events.append(duplicate)
    if inventory and rows >= 3:
        inventory[2]["on_hand_quantity"] = -5

    return {"orders": orders, "shipment_events": events, "inventory": inventory}
