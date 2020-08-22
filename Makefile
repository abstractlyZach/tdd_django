test:
	# disabling warnings because we're on an old version of django
	pytest lists --disable-warnings

functional_test:
	python functional_tests.py
