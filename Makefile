.PHONY: docs test

help:
		@echo "  env         create a development environment using virtualenv"
		@echo "  deps        install dependencies using pip"
		@echo "  install	 install dependencies and update db schema"
		@echo "  run         run project locally"
		@echo "  updatedb	 updates database schema"
		#@echo "  clean       remove unwanted files like .pyc's"
		#@echo "  lint        check style with flake8"
		#@echo "  test        run all your tests using py.test"

env:
		virtualenv venv 

deps:
		sudo apt-get install libpq-dev python-dev && \
		pip install -r requirements.txt

install:
		make deps && make updatedb 

run:
		python manage.py runserver	

updatedb:
		python manage.py migrate

