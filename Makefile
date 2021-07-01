dev-deps:
	pip install -r requirements/dev.txt

dist-build-package: dev-deps
	python3.8 setup.py sdist

dist-check:  dist-build-package
	twine check dist/*

dist-upload-test:
	twine upload --repository testpypi dist/*

dist-upload: dist-build-package
	twine upload dist/*

tests-deps:
	pip install -r requirements/test.txt

clean:
	rm -fr build dist
	find . -name "*~" -exec rm {} -v \;
	find . -name "*#" -exec rm {} -v \;
	find . -name "__pycache__" -exec rm -rf {} -v \;

format:
	black .
	flake8 .
