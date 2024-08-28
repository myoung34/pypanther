test:
	poetry run tox
	poetry run pypanther test --verbose

fmt:
	poetry run ruff check --select I --fix .
	poetry run ruff format .

lint: fmt
	poetry run ruff check --fix .
	poetry run ruff format --check .
	poetry run mypy .

upload:
	poetry run pypanther upload

install:
	poetry install --no-root

update:
	poetry update
