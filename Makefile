.DEFAULT_GOAL := init-dev

# test managing
test:
	docker-compose run --rm $(SERVICE_NAME)-app pytest -v tests/

test-coverage:
	docker-compose run --rm $(SERVICE_NAME)-app pytest -v --cov --cov-report term --cov-report html --html=pytest_report.html --self-contained-html --junitxml=pytest_junit_report.xml tests/

# database managing
db-upgrade:
	docker-compose run --rm $(SERVICE_NAME)-app flask db upgrade;

db-downgrade:
	docker-compose run --rm $(SERVICE_NAME)-app flask db downgrade;

db-migrate:
	docker-compose run --rm $(SERVICE_NAME)-app flask db migrate;
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

# utils
stop:
	docker-compose stop

down:
	docker-compose down

requirements:
	docker-compose run --rm server pip-compile -U -o requirements.txt requirements.in
	$(MAKE) chown

chown:
	$(SUDO) chown -hR $(UID):$(GID) .
