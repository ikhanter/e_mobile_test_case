start:
	poetry run python main.py

lint:
	poetry run ruff check

install:
	poetry install
