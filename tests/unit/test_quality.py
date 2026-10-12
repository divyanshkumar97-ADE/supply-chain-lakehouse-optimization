from supply_chain.quality import (
    classify_inventory_record,
    classify_shipment_event,
    is_iso_timestamp,
    is_non_negative_integer,
    is_positive_number,
)


def test_positive_number():
    assert is_positive_number(1)
    assert is_positive_number("4.25")
    assert not is_positive_number(0)
    assert not is_positive_number(-2)
    assert not is_positive_number("bad")


def test_non_negative_integer():
    assert is_non_negative_integer(0)
    assert is_non_negative_integer("12")
    assert not is_non_negative_integer(-1)
    assert not is_non_negative_integer("1.5")


def test_iso_timestamp():
    assert is_iso_timestamp("2026-01-01T08:00:00Z")
    assert not is_iso_timestamp("not-a-timestamp")


def test_shipment_event_contract():
    valid = {
        "event_id": "EVT-1",
        "shipment_id": "SHP-1",
        "event_type": "SHIPPED",
        "event_timestamp": "2026-01-01T08:00:00Z",
        "warehouse_id": "WH-001",
    }
    assert classify_shipment_event(valid) == []
    invalid = {**valid, "event_timestamp": "bad", "event_type": "ALIEN"}
    assert set(classify_shipment_event(invalid)) == {
        "invalid_event_timestamp",
        "unknown_event_type",
    }


def test_inventory_negative_quantity_is_rejected():
    record = {
        "inventory_id": "INV-1",
        "product_id": "SKU-1",
        "warehouse_id": "WH-1",
        "on_hand_quantity": -3,
        "reorder_threshold": 10,
        "snapshot_timestamp": "2026-01-01T08:00:00Z",
    }
    assert classify_inventory_record(record) == ["negative_on_hand_quantity"]
