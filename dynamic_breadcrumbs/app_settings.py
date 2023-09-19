from django.conf import settings

HOME_LABEL = getattr(
    settings, "DYNAMIC_BREADCRUMBS_HOME_LABEL", "Home"
)
SHOW_AT_BASE_PATH = getattr(
    settings, "DYNAMIC_BREADCRUMBS_SHOW_AT_BASE_PATH", False
)
SHOW_VERBOSE_NAME = getattr(
    settings, "DYNAMIC_BREADCRUMBS_SHOW_VERBOSE_NAME", True
)

PATH_ALPHANUMERIC = getattr(
    settings, "DYNAMIC_BREADCRUMBS_PATH_ONLY_ALPHANUMERIC", True
)
