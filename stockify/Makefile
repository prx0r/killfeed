.PHONY: dev test seed ingest clean

dev:
	uvicorn stockify.api:app --reload --host 0.0.0.0 --port 8000

test:
	pytest -q

seed:
	python -m stockify.cli seed

ingest:
	python -m stockify.cli ingest

clean:
	rm -f stockify.db
