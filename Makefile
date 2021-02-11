install:
	@poetry install

build:
	poetry build

publish:
	poetry publish -r tatoxer_gendiff

lint:
	poetry run flake8 brain_games