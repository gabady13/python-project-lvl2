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

run4:
	poetry run gendiff -f j tests/fixtures/step4/original.json tests/fixtures/step4/modified.json
	poetry run gendiff tests/fixtures/step4/original.json tests/fixtures/step4/modified.json

run5:
	poetry run gendiff -f j tests/fixtures/step5/original.yml tests/fixtures/step5/modified.yml
	poetry run gendiff tests/fixtures/step5/original.yml tests/fixtures/step5/modified.yml

run6json:
	poetry run gendiff tests/fixtures/step6/original.json tests/fixtures/step6/modified.json

run6yml:
	poetry run gendiff tests/fixtures/step6/original.yml tests/fixtures/step6/modified.yml

run7stylish:
	poetry run gendiff --format stylish tests/fixtures/step6/original.json tests/fixtures/step6/modified.json

run7plain:
	poetry run gendiff --format plain tests/fixtures/step6/original.json tests/fixtures/step6/modified.json
