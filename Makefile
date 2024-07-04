install:
	poetry install

start:
	poetry run python manage.py runserver 127.0.0.1:8000

migrate:
    poetry run python manage.py migrate

lint:
	poetry run flake8 hexlet_django_blog
