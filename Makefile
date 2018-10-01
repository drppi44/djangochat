RUN_WEB=docker-compose run --rm web
MANAGE=python manage.py
DOCKER_PYTHON=$(RUN_WEB) $(MANAGE)

migrate:
	$(DOCKER_PYTHON) migrate

makemigrations:
	$(DOCKER_PYTHON) makemigrations

shell:
	$(DOCKER_PYTHON) shell_plus

createsuperuser:
	$(DOCKER_PYTHON) createsuperuser

test:
	$(DOCKER_PYTHON) test

pip:
	$(RUN_WEB) pip install -r requirements.txt

build:
	docker-compose build

loaddata:
	$(DOCKER_PYTHON) loaddata

