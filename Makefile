migrate:
	poetry run python manage.py migrate

migration:
	poetry run python manage.py makemigrations

start:
	poetry run python manage.py runserver