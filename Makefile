install:
	@poetry install

build:
	@poetry build

publish:
	poetry publish --dry-run

lint:
	@poetry run flake8 gendiff

package-install:
	pip install dist/*.whl

package-uninstall:
	pip uninstall hexlet-code

help:
	poetry run python -m gendiff.scripts.gendiff --h