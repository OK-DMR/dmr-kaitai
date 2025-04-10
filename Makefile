.PHONY: test test-only build package upload

test-only:
	PYTHONPATH=. pytest -rP --cov-report=term-missing --cov=okdmr.kaitai

build:
	sh rebuild-all.sh

test: build test-only

package:
	python3 -m build . --sdist --wheel

upload-only:
	python3 -m twine upload dist/* --repository pypi --verbose

upload: build package upload-only