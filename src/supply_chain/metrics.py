"""Run-level audit and reconciliation helpers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class RunMetrics:
    run_id: str
    pipeline_name: str
    started_at_utc: str
    input_count: int
    output_count: int
    rejected_count: int
    status: str

    @property
    def accounted_for(self) -> bool:
        return self.output_count + self.rejected_count <= self.input_count

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def create_run_metrics(
    run_id: str,
    pipeline_name: str,
    input_count: int,
    output_count: int,
    rejected_count: int,
    status: str,
) -> RunMetrics:
    if min(input_count, output_count, rejected_count) < 0:
        raise ValueError("Run counts cannot be negative")
    if output_count + rejected_count > input_count:
        raise ValueError("Output + rejected counts cannot exceed input count")
    return RunMetrics(
        run_id=run_id,
        pipeline_name=pipeline_name,
        started_at_utc=datetime.now(UTC).isoformat(),
        input_count=input_count,
        output_count=output_count,
        rejected_count=rejected_count,
        status=status,
    )
