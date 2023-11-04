.PHONY: install migrate migrations migrations-init run superuser update


install:
	poetry install

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

migrations-init:
	poetry run python manage.py makemigrations libresenses

run:
	poetry run python manage.py runserver

superuser:
	poetry run python manage.py createsuperuser

update: install migrate ;
