fill_db:
	python3 manage.py import_data

start: migrate
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

test:
	python3 manage.py test

console:
	django-admin shell
