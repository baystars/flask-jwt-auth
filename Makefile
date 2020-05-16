MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := test

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

export SECRET_KEY="\xd7\xbdQ\xcb'32\xde\x8f2\x10\xc8\xea\x86,\xda\xd0}Q@\xc9'\xaf\xdc"
export FLASK_ENV=development

# .env
ifneq ("$(wildcard ./.env)","")
  include ./.env
endif

run: ## Run server
	@python manage.py runserver

create-db: ## Create database
	@python manage.py create_db

init-db: ## Initialize database
	@python manage.py db init

migrate-db: ## Migrate database
	@python manage.py db migrate

test: ## Unit test
	@python manage.py test
