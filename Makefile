VENV_NAME?=venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	@test -d $(VENV_NAME) || python3 -m virtualenv --clear $(VENV_NAME)

clean:
	@rm -rf $(VENV_NAME) build/ dist/

.PHONY: venv clean
