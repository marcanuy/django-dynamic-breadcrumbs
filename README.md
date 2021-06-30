django-breadcrumbing
=====

django-breadcrumbing is a Django app to generate HTML breadcrumbs from
URL paths. 

At `https://themusicsecret.com/reference/instrument/`, it shows:
`Home > Reference > Instrument`.

# Quick start

## 1. Add to settings

Add "breadcrumbing" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'breadcrumbing',
    ]

## 2. Add context processor

Add `"reference.context_processors.breadcrumbs"` the breadcrumbing context processor to your settings like this::

~~~ python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
				#...
                "reference.context_processors.breadcrumbs",
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
	    {% include "breadcrumbing/breadcrumbs.html" with breadcrumbs=breadcrumbs%}
	</div>
	{% endif %}
	{% endblock %}
~~~

Now each time you visit a page which makes use of the above template,
it will have the breadcrumbs generated from the URL path.


## References

- https://www.w3.org/TR/html53/common-idioms-without-dedicated-elements.html#bread-crumb-navigation
