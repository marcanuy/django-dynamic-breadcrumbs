build-package:
	python3.8 setup.py sdist

clean:
	rm -fr build dist
	find . -name "*~" -exec rm {} -v \;
	find . -name "*#" -exec rm {} -v \;
	find . -name "__pycache__" -exec rm -rf {} -v \;
