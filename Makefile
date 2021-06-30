build-package:
	python3.8 setup.py sdist

clean:
	rm -fr build dist django_breadcrumbing.egg-info *~
