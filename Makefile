.PHONY: install virtualenv ipython test pflake8

install:
	@echo "Installing for dev enviroment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -s --forked

testci:
	@pytest -v --junitxml=test-result.xml

watch:
	@.venv/bin/ptw -- -vv -s

lint:
	@.venv/bin/pflake8 dundie

fmt:
	@.venv/bin/black dundie tests integration