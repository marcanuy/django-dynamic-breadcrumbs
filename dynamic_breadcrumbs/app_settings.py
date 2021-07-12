from django.conf import settings


DYNAMIC_BREADCRUMBS_HOME_LABEL = getattr(
    settings, "DYNAMIC_BREADCRUMBS_HOME_LABEL", "Home"
)
DYNAMIC_BREADCRUMBS_SHOW_AT_BASE_PATH = getattr(
    settings, "DYNAMIC_BREADCRUMBS_SHOW_AT_BASE_PATH", False
)
