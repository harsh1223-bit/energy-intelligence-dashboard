install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	./run.sh

test:
	. .venv/bin/activate && pytest -q

down:
	docker compose down
