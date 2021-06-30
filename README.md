Polls
=====

django-breadcrumbing is a Django app to generate HTML breadcrumbs from
URL paths. 

e.g. for `https://themusicsecret.com/reference/instrument/`, generates a markup
bread-crumb navigation as a list:

~~~ html
<nav aria-label="breadcrumb">
    <ol class="breadcrumb alert alert-success" itemprop="breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
		 <li class="breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
			 <a itemprop="item" href="https://themusicsecret.com">
			 <span itemprop="name">Home</span>
			 <meta itemprop="position" content="1" />
			 </a>
		 </li>
		 <li class="breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">

			 <a itemprop="item" href="https://themusicsecret.com/reference/">
			 <span itemprop="name">Reference</span>
			 <meta itemprop="position" content="2" />
			 </a>

		 </li>
		 <li class="breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">

			 <a itemprop="item" href="https://themusicsecret.com/reference/instrument/">
			 <span itemprop="name">Instrument</span>
			 <meta itemprop="position" content="3" />
			 </a>

		 </li>
	</ol>
</nav>
~~~

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
	    {% include "partials/breadcrumbs.html" with breadcrumbs=breadcrumbs%}
	</div>
	{% endif %}
	{% endblock %}
~~~

Now each time you visit a page which makes use of the above template,
it will have the breadcrumbs generated from the URL path.


## References

- https://www.w3.org/TR/html53/common-idioms-without-dedicated-elements.html#bread-crumb-navigation
