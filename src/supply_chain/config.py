"""Central project configuration with environment-overridable defaults."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectConfig:
    """Non-secret settings shared by local utilities and notebooks."""

    project_name: str = "supply_chain_lakehouse"
    environment: str = "dev"
    catalog: str = "workspace"
    schema: str = "supply_chain"
    data_quality_fail_threshold: float = 0.05

    @classmethod
    def from_environment(cls) -> "ProjectConfig":
        """Load configuration without storing credentials in source control."""
        threshold = float(os.getenv("DQ_FAIL_THRESHOLD", "0.05"))
        if not 0 <= threshold <= 1:
            raise ValueError("DQ_FAIL_THRESHOLD must be between 0 and 1")
        return cls(
            environment=os.getenv("PROJECT_ENV", "dev"),
            catalog=os.getenv("DATABRICKS_CATALOG", "workspace"),
            schema=os.getenv("DATABRICKS_SCHEMA", "supply_chain"),
            data_quality_fail_threshold=threshold,
        )
