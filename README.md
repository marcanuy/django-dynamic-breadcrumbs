Polls
=====

django-breadcrumbing is a Django app to generate HTML breadcrumbs from
apps URL paths. For `https://example.com/a/b/c/`, generates a markup
bread-crumb navigation as a list:

~~~
<ul>
<li>a</li>
<li>b</li>
<li>c</li>
</ul>
~~~

# Quick start

1. Add "breadcrumbing" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'breadcrumbing',
    ]

2. Add  the breadcrumbing context processor to your ... like this::

    path('polls/', include('polls.urls')),

## References

- https://www.w3.org/TR/html53/common-idioms-without-dedicated-elements.html#bread-crumb-navigation
