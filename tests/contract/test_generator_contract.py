from supply_chain.contracts import (
    INVENTORY_REQUIRED_FIELDS,
    ORDER_REQUIRED_FIELDS,
    SHIPMENT_EVENT_REQUIRED_FIELDS,
)
from supply_chain.generator import generate_datasets


def test_generator_emits_required_columns():
    datasets = generate_datasets(20, seed=7)
    assert set(ORDER_REQUIRED_FIELDS).issubset(datasets["orders"][0])
    assert set(SHIPMENT_EVENT_REQUIRED_FIELDS).issubset(datasets["shipment_events"][1])
    assert set(INVENTORY_REQUIRED_FIELDS).issubset(datasets["inventory"][0])


def test_generator_is_deterministic():
    assert generate_datasets(5, seed=7) == generate_datasets(5, seed=7)
