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

help:
	poetry run python -m gendiff.scripts.gendiff_script --h

test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests
