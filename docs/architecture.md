# Architecture and engineering decisions

## Logical flow
1. **Landing**: source files are grouped into immutable batches. Each batch has a batch ID and ingestion timestamp.
2. **Bronze**: preserve source values with metadata (`_ingested_at`, `_source_file`, `_batch_id`, `_run_id`). Avoid destructive cleansing in this layer.
3. **Silver**: apply contracts, normalize types, deduplicate by business key and event timestamp, route invalid rows to quarantine with issue codes.
4. **Gold**: create business-facing datasets such as shipment SLA and inventory risk.
5. **Audit**: record run ID, pipeline name, batch ID, source count, accepted count, rejected count, duplicate count, status, and timestamps.

## Reliability patterns
- Reprocessing a batch must not duplicate business events.
- Use stable event IDs and deterministic deduplication ordering.
- Treat late-arriving events explicitly; do not discard them just because their event timestamp is old.
- Watermarks must represent successfully committed source progress, not merely the latest timestamp observed before a failed write.
- Reconcile input = accepted + rejected + duplicates according to the documented counting convention.

## Performance experiment protocol
- Fix the data, query, and output before comparing variants.
- Record row count, file count, total bytes, runtime, Spark physical plan, and available scan metrics.
- Run multiple trials and report median, not only the fastest run.
- Separate cold-start/serverless startup effects from query execution when possible.
- Only claim an improvement if the benchmark can be reproduced.
