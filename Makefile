update: init update-deps install

update-deps:
		pip-compile --upgrade --generate-hashes
		pip-compile --upgrade --generate-hashes --output-file dev-requirements.txt dev-requirements.in
		pip install --upgrade -r requirements.txt  -r dev-requirements.txt

install:
		pip install --editable .

init:
		pip install pip-tools
		rm -rf .tox

# PHONY: targets (update-deps, install and init cant be confused with files)
.PHONY: update-deps init update install
