.DEFAULT_GOAL := init-dev

# test managing
test:
	docker-compose run --rm server pytest -v tests/

test-coverage:
	docker-compose run --rm server pytest -v --cov --cov-report term --cov-report html --html=pytest_report.html --self-contained-html --junitxml=pytest_junit_report.xml tests/

# database managing
db-upgrade:
	docker-compose run --rm server flask db upgrade;

db-downgrade:
	docker-compose run --rm server flask db downgrade;

db-migrate:
	docker-compose run --rm server flask db migrate;
	$(MAKE) chown

db-init:
	docker-compose run --rm server flask db init;
	$(MAKE) chown

# server managing
init:
	docker network create workssingleview || true

build:
	docker-compose build server

start:
	docker-compose up server

startd:
	docker-compose up -d server

start-db:
	docker-compose up -d postgres

stop-db:
	docker-compose stop postgres

stop:
	docker-compose stop

down:
	docker-compose down

# utils
requirements:
	docker-compose run --rm server pip-compile -U -o requirements.txt requirements.in
	$(MAKE) chown

chown:
	$(SUDO) chown -hR $(UID):$(GID) .
