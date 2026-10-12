# Databricks notebooks (next milestone)

Create workspace-compatible notebooks for:
1. `01_bronze_ingestion`: read generated source batches, attach metadata, write Bronze Delta tables.
2. `02_silver_quality`: apply schema contracts, write valid records and quarantine with issue codes.
3. `03_gold_products`: create shipment SLA and inventory-risk datasets.
4. `04_optimization_lab`: compare query plans, joins, file sizes, and supported table-layout optimizations.

Keep notebooks thin: reusable business logic should live in `src/` where practical. Do not assume UC Volumes, external locations, Auto Loader, or deployment capabilities until verified in the Free Edition workspace.
