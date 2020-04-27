PIP="venv/bin/pip"
PYTHON="venv/bin/python"

REQUIREMENTS:=requirements.txt

virtualenv:
	test -d venv || virtualenv -p python3.7 venv
	$(PIP) install -U "pip"
	$(PIP) install -r $(REQUIREMENTS)

test: virtualenv
	$(PYTHON) -m pytest wallapopy/tests
