# Runbook

## Local CI failure
1. Activate the virtual environment.
2. Run `ruff check .` and resolve lint issues.
3. Run `pytest -q` to isolate failures.
4. Commit the fix and push the branch.

## Bad source batch
1. Preserve raw source data in Bronze.
2. Inspect quarantine records and issue codes.
3. Fix upstream data or the transformation rule.
4. Reprocess the same batch using the idempotent path.
5. Verify accepted + rejected + duplicate counts reconcile.

## Failed incremental run
1. Identify the run ID and last successfully committed batch/checkpoint.
2. Confirm whether target writes committed before retrying.
3. Retry from the last committed checkpoint.
4. Confirm business-key uniqueness and row-count reconciliation.

## Cost and safety guardrails
- Use Databricks Free Edition only for cloud execution.
- Do not enable paid cloud resources for this project.
- Do not place secrets in notebooks, Git, logs, or screenshots.
- Use small test datasets before scaling workloads.
