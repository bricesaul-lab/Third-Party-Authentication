setup:
	pip3 install virtualenv
	virtualenv .venv
	
	.venv/bin/pip3 install -r requirements.txt


source:
	@echo .venv/bin/activate
debug:
	python3 wsgi.py

run:
	gunicorn --bind 0.0.0.0:5000 wsgi:app
