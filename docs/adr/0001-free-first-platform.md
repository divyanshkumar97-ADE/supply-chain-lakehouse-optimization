# ADR 0001: Free-first development platform

- **Status:** Accepted
- **Decision:** Use Databricks Free Edition for workspace-based Spark/Delta exercises, local Python for deterministic unit tests, and GitHub Actions for CI.
- **Constraints:** No Azure, no paid cloud storage/database, and no personal Spark cluster.
- **Consequences:** Local tests validate pure transformation rules; Spark/Delta integration tests run only in the Databricks workspace. Workspace-specific capabilities must be verified before enabling deployment.
