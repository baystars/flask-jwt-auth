export SECRET_KEY="\xd7\xbdQ\xcb'32\xde\x8f2\x10\xc8\xea\x86,\xda\xd0}Q@\xc9'\xaf\xdc"
export FLASK_ENV=development

test:
	python manage.py test

run:
	python manage.py runserver

create-db:
	python manage.py create_db

init-db:
	python manage.py db init

migrate-db:
	python manage.py db migrate

add:
	git add .

commit:
	git commit -m 'modify'

push:
	git push -u origin master

add-commit-push: add commit push
