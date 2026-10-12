import pytest

from supply_chain.metrics import create_run_metrics


def test_run_metrics_reconcile_counts():
    metrics = create_run_metrics("run-1", "silver_events", 10, 8, 2, "SUCCESS")
    assert metrics.accounted_for
    assert metrics.to_dict()["input_count"] == 10


def test_run_metrics_reject_impossible_counts():
    with pytest.raises(ValueError):
        create_run_metrics("run-1", "silver_events", 10, 9, 2, "SUCCESS")
