test:
	# disabling warnings because we're on an old version of django
	poetry run pytest lists --disable-warnings

functional_test:
	poetry run pytest functional_tests --disable-warnings

run:
	poetry run manage.py runserver
