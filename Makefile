migrate:
	poetry run python manage.py migrate

migration:
	poetry run python manage.py makemigrations

start: migrate
	poetry run python manage.py runserver

black:
	poetry run black --line-length 120 .

test:
	poetry run pytest