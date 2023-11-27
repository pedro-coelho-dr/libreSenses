.PHONY: migrations-init superuser migrations migrate run requirements collectstatic freeze diagram cloud-sql-proxy gcloud-build gcloud-deploy gcloud-update

migrations-init:
	python manage.py makemigrations libresenses

superuser:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver 8080

requirements:
	pip install -r requirements.txt

collectstatic:
	python manage.py collectstatic

freeze:
	pip freeze > requirements. txt  

diagram: 
	python manage.py graph_models libresenses  -e -S --arrow-shape normal  -n  --dot -g -o libresenses_models.dot
	dot -Tpng libresenses_models.dot -o libresenses_models.png

#GOOGLE CLOUD COMMANDS
cloud-sql-proxy:
	./cloud-sql-proxy libresenses:southamerica-east1:libresenses-postgresql-instance --port 1234

gcloud-build:
	gcloud builds submit --config cloudmigrate.yaml

gcloud-deploy:
	gcloud run deploy libresenses-service \
    --platform managed \
    --region southamerica-east1 \
    --image gcr.io/libresenses/libresenses-service \
    --add-cloudsql-instances libresenses:southamerica-east1:libresenses-postgresql-instance \
    --allow-unauthenticated

gcloud-update:
	$(eval SERVICE_URL := $(shell gcloud run services describe libresenses-service --platform managed --region southamerica-east1 --format "value(status.url)"))
	@gcloud run services update libresenses-service \
		--platform managed \
		--region southamerica-east1 \
		--set-env-vars CLOUDRUN_SERVICE_URL=$(SERVICE_URL)