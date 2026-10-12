"""Generate synthetic source feeds for local development and Databricks ingestion."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from supply_chain.generator import generate_datasets


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="data/generated")
    parser.add_argument("--rows", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    try:
        datasets = generate_datasets(args.rows, args.seed)
    except ValueError as exc:
        parser.error(str(exc))

    output_dir = Path(args.output_dir)
    for name, records in datasets.items():
        destination = output_dir / f"{name}.csv"
        write_csv(destination, records)
        print(f"{name}: wrote {len(records):,} records to {destination}")


if __name__ == "__main__":
    main()
