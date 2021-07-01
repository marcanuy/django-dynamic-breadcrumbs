.. django-dynamic-breadcrumbs documentation master file, created by
   sphinx-quickstart on Thu Jul  1 10:14:43 2021.

django-dynamic-breadcrumbs's documentation
======================================================

`django-dynamic-breadcrumbs` is a Django app to generate HTML breadcrumbs
dynamically from URL paths.

How does it work
----------------

1. A request is handled by Django at a specific URL:
   
   https://example.com/reference/instrument/guitar/
   
2. A *context processor* analyze the URL, and extracts the path:

   /reference/instrument/guitar/
   
3. For each part separated by `/` tries to `resolve`__ it and get the
   specific *View* that handles that URL.
4. Adds to the request context a list of names and urls

.. code-block:: python

    home       -> https://example.com
    reference  -> https://example.com/reference
    instrument -> https://example.com/reference/instrument
    guitar
   
5. The template shows the above list with links for each level

   Home > Reference > Instrument > Guitar
   
__ https://docs.djangoproject.com/en/3.2/ref/urlresolvers/#resolve

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. toctree::
    :maxdepth: 2
    :caption: User Guide

    guide/install
    guide/usage

.. toctree::
    :maxdepth: 1
    :caption: Reference

    ref/settings

.. toctree::
    :maxdepth: 1
    :caption: Developers

    dev/tests
