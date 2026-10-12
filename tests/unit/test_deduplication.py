from supply_chain.deduplication import deduplicate_by_latest


def test_deduplicates_by_latest_timestamp():
    records = [
        {"event_id": "E1", "updated_at": "2026-01-01T08:00:00Z", "value": 1},
        {"event_id": "E1", "updated_at": "2026-01-02T08:00:00Z", "value": 2},
        {"event_id": "E2", "updated_at": "2026-01-01T09:00:00Z", "value": 3},
    ]
    result = deduplicate_by_latest(records, "event_id", "updated_at")
    assert {row["event_id"]: row["value"] for row in result} == {"E1": 2, "E2": 3}


def test_skips_records_without_dedup_key():
    assert deduplicate_by_latest([{"updated_at": "2026-01-01"}], "event_id", "updated_at") == []
