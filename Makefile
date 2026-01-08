.PHONY: setup data train serve help

help:
	@echo "Available commands:"
	@echo "  make setup   → install dependencies & hooks"
	@echo "  make data    → download Kaggle dataset"
	@echo "  make train   → train model + save artifacts"
	@echo "  make serve   → start inference API"

setup:
	poetry install
	poetry run pre-commit install || true

data:
	poetry run download-data
	poetry run prepare-data

train:
	poetry run train

serve:
	poetry run serve

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

test:
	poetry run pytest -q