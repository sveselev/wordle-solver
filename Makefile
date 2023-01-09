# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com


ERROR_COLOR = \033[1;31m
INFO_COLOR = \033[1;32m
WARN_COLOR = \033[1;33m
NO_COLOR = \033[0m

PYTHON_VERSION_SUPPORTED := 3.8 3.9 3.10
PYTHON_VERSION_SHELL := $(shell python --version | cut -f2 -d' ' | cut -f1,2 -d'.')
check-python-version:
ifeq ($(findstring $(PYTHON_VERSION_SHELL),$(PYTHON_VERSION_SUPPORTED)),)
	@printf "$(WARN_COLOR)You have python $(ERROR_COLOR)$(PYTHON_VERSION_SHELL)$(WARN_COLOR); you need python one of $(INFO_COLOR)($(PYTHON_VERSION_SUPPORTED))$(NO_COLOR).\n"
	@exit 1
else
	@printf "$(INFO_COLOR)OK!$(NO_COLOR) Shell version $(PYTHON_VERSION_SHELL) in ($(PYTHON_VERSION_SUPPORTED)).\n"
endif

VIRTUALENV := venv
$(VIRTUALENV): check-python-version
	@python -m venv $(VIRTUALENV)

PYTHON_ARGS := . $(VIRTUALENV)/bin/activate && PYTHONPATH=.
LIBS := $(VIRTUALENV)/lib/python$(PYTHON_VERSION_SHELL)/site-packages
REQUIREMENTS := requirements.txt
.PHONY: init
init: $(LIBS)
$(LIBS): $(VIRTUALENV) $(REQUIREMENTS)
	@$(PYTHON_ARGS) pip install -r $(REQUIREMENTS)
	@touch $(LIBS)

.PHONY: run
run: $(LIBS)
	@$(PYTHON_ARGS) python src/functions/handler.py --goal $(goal)

.PHONY: evaluate
evaluate: count ?= 100
evaluate: $(LIBS)
	@$(PYTHON_ARGS) python src/functions/handler.py --evaluate $(count)

.PHONY: test
test:
	@$(PYTHON_ARGS) pytest tests

.PHONY: lint
lint:
	@$(PYTHON_ARGS) flake8 src tests
	@$(PYTHON_ARGS) mypy src tests

.PHONY: check
check: lint test
