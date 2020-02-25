VENV_NAME?=venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	@test -d $(VENV_NAME) || python3 -m virtualenv --clear $(VENV_NAME)

linter:
	. $(VENV_NAME)/bin/activate; flake8 ./apidaze

linter-fix:
	. $(VENV_NAME)/bin/activate; autopep8 --in-place --aggressive --aggressive -r apidaze/

test:
	. $(VENV_NAME)/bin/activate; tox

test-current:
	. $(VENV_NAME)/bin/activate; tox -e python

docs-install:
	. $(VENV_NAME)/bin/activate; pip install -r tests/requirements.txt

docs:
	@rm -rf docs/source/_rst
	@rm -rf docs/build
	. $(VENV_NAME)/bin/activate; sphinx-apidoc -M -f apidaze -o docs/source/_rst --implicit-namespaces
	. $(VENV_NAME)/bin/activate; sphinx-build -b html -c ./docs -d docs/build/doctrees . docs/build/html

clean:
	@rm -rf $(VENV_NAME) build/ dist/

.PHONY: venv clean docs
