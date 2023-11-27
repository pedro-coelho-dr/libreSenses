.PHONY: install migrate migrations migrations-init run superuser update docker diagram

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

docker:
	docker build -t libresenses-app .

update: install migrate ;

diagram: 
	poetry run python manage.py graph_models libresenses  -e -S --arrow-shape normal  -n  --dot -g -o libresenses_models.dot
	dot -Tpng libresenses_models.dot -o libresenses_models.png