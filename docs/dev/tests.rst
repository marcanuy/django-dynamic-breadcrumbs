======================
Running the Test Suite
======================

To run the `django-dynamic-breadcrumbs` tests checkout the source
code and create a virtualenv where you can install the test dependencies.

.. note::

    The following assumes you have `virtualenv`__ and `git`__ installed.

__ https://virtualenv.pypa.io/en/stable/
__ https://git-scm.com

Clone the repository
--------------------

Get the source code using the following command:

.. code-block:: bash

    $ git clone https://github.com/marcanuy/django-dynamic-breadcrumbs.git

Switch to the django-dynamic-breadcrumbs directory:

.. code-block:: bash

    $ cd django-dynamic-breadcrumbs

Set up the virtualenv
---------------------

Create a new virtualenv to run the test suite in:

.. code-block:: bash

    $ python3 -m venv ~/.virtualenvs/django-dynamic-breadcrumbs

Then activate the virtualenv and install the test requirements:

.. code-block:: bash

    $ source ~/.virtualenvs/django-dynamic-breadcrumbs/bin/activate
    $ pip install -r requirements/test.txt

Execute the test runner
-----------------------

Run the tests with the runner script:

.. code-block:: bash

    $ make tests-run


Test all supported versions
---------------------------

To run the tests against all supported versions of Python and Django
use `tox`__, then:

__ https://tox.readthedocs.io/en/latest/index.html

.. code-block:: bash

    $ tox


Formatting
----------

Python code is formatted with `black`__

__ https://github.com/psf/black

.. code-block:: bash

    $ black .


