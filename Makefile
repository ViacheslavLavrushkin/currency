SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

makemigrate:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate
