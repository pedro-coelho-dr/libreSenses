.PHONY: install migrate migrations runserver superuser update

install:
	poetry install

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

runserver:
	poetry run python manage.py runserver

superuser:
	poetry run python manage.py createsuperuser

update: install migrate ;
