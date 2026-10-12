.PHONY: install test lint check data

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

check: lint test

data:
	python scripts/generate_data.py --output-dir data/generated --rows 1000
