install-pip:
	python -m pip install --upgrade pip
dev-deps: install-pip
	pip install -r requirements/dev.txt

dist-build-package:
	python setup.py sdist

dist-check:
	twine check dist/*

dist-upload-test:
	twine upload --repository testpypi dist/*

dist-upload: dist-build-package
	twine upload dist/*

tests-deps: install-pip
	pip install -r requirements/test.txt

tests-run:
	PYTHONPATH=$$PWD:$$PYTHONPATH DJANGO_SETTINGS_MODULE=tests.settings ~/.virtualenvs/django-dynamic-breadcrumbs/bin/django-admin test
clean:
	rm -fr build dist
	find . -name "*~" -exec rm {} -v \;
	find . -name "*#" -exec rm {} -v \;
	find . -name "__pycache__" -exec rm -rf {} -v \;

format:
	black .
	flake8 .
