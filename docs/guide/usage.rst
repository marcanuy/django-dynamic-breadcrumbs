===============
Getting Started
===============

Add to settings
---------------

Add `dynamic_breadcrumbs.context_processors.breadcrumbs` to **context_processors**:

.. code-block:: python

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


Add template
------------

Include the `dynamic_breadcrumbs/breadcrumbs.html` in your base template.

.. code-block:: jinja

    {% if breadcrumbs %}
    <div class="container">
	{% include "dynamic_breadcrumbs/breadcrumbs.html" with breadcrumbs=breadcrumbs%}
    </div>
    {% endif %}



