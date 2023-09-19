==================
Settings Reference
==================

List of all available settings of `django-dynamic-breadcrumbs` and their
default values.

All settings are prefixed with ``DYNAMIC_BREADCRUMBS_``.


DYNAMIC_BREADCRUMBS_HOME_LABEL
------------------------------

Default: ``'Home'``

Set the default base Url to be shown as the first item of the
breadcrumb list.


DYNAMIC_BREADCRUMBS_SHOW_AT_BASE_PATH
-------------------------------------

Default: ``False``

Wheter to show or hide breadcrumbs at site's root.


DYNAMIC_BREADCRUMBS_PATH_ONLY_ALPHANUMERIC
------------------------------------------

Default: ``True``

Only allows alphanumeric characters in breadcrumb item names. If
someone contains non-alphanumeric values it will show an empty string.


DYNAMIC_BREADCRUMBS_PATH_MAX_DEPTH
----------------------------------

Default: ``5``

The maximum number of breadcrumb items to show


DYNAMIC_BREADCRUMBS_PATH_MAX_COMPONENT_LENGTH
---------------------------------------------

Default: ``50``

Each path component's maximum length.
