test:
	# disabling warnings because we're on an old version of django
	pytest lists --disable-warnings

functional_test:
	pytest functional_tests.py

run:
	python manage.py runserver
