install:
	python3 -m venv .venv
	pip install -r requirements.txt
	chmod u+x run/*.command