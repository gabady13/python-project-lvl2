install:
	@poetry install

build:
	@poetry build

publish:
	poetry publish --dry-run

lint:
	@poetry run flake8 gendiff
	@poetry run flake8 tests

package-install:
	pip install dist/*.whl

package-uninstall:
	pip uninstall hexlet-code

test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests

run-test:
	poetry run gendiff --format stylish tests/fixtures/nested_json/original.json tests/fixtures/nested_json/modified.json

test-stylish:
	poetry run gendiff --format stylish tests/fixtures/plain_json/original.json tests/fixtures/plain_json/modified.json
