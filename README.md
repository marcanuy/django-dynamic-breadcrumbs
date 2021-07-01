django-dynamic-breadcrumbs
=====

[![Django CI](https://github.com/marcanuy/django-dynamic-breadcrumbs/actions/workflows/django.yml/badge.svg)](https://github.com/marcanuy/django-dynamic-breadcrumbs/actions/workflows/django.yml)
[![PyPI version](https://badge.fury.io/py/django-dynamic-breadcrumbs.svg)](https://badge.fury.io/py/django-dynamic-breadcrumbs)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/django-dynamic-breadcrumbs)](https://pepy.tech/project/django-dynamic-breadcrumbs)

django-dynamic-breadcrumbs is a Django app to generate HTML breadcrumbs
dynamically from URL paths. 

At `https://themusicsecret.com/reference/instrument/`, it shows:
`Home > Reference > Instrument`.

# Quick start

## 1. Add to settings

Add "dynamic_breadcrumbs" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dynamic_breadcrumbs',
    ]

## 2. Add context processor

Add `"dynamic_breadcrumbs.context_processors.breadcrumbs"` the **dynamic-breadcrumbs** context processor to your settings like this::

~~~ python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
				#...
                "dynamic_breadcrumbs.context_processors.breadcrumbs",
            ],
        },
    },
]
~~~

## 3. Add template

Include the `breadcrumbs.html` template code.

~~~
	{% block breadcrumbs %}
	{% if breadcrumbs %}
	<div class="container">
	    {% include "dynamic_breadcrumbs/breadcrumbs.html" with breadcrumbs=breadcrumbs%}
	</div>
	{% endif %}
	{% endblock %}
~~~

Now each time you visit a page which makes use of the above template,
it will have the breadcrumbs generated from the URL path.


## References

- https://www.w3.org/TR/html53/common-idioms-without-dedicated-elements.html#bread-crumb-navigation
