.PHONY: install test lint clean run

install:
	pip install -e . pytest

test:
	pytest -q

lint:
	python -m compileall -q src

run:
	python -m fl_studio_2026_producer_edition_premium_tools

clean:
	rm -rf build dist *.egg-info __pycache__
