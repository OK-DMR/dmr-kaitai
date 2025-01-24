.PHONY: test build

test: build test-only

test-only:
	PYTHONPATH=. pytest -rP --cov-report=term-missing --cov=okdmr.kaitai

build:
	sh rebuild-all.sh
