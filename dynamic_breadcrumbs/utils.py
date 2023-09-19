import logging
import re
from urllib.parse import urljoin, urlparse

from django.apps import apps
from django.conf import settings
from django.utils.html import escape
from django.urls import Resolver404, resolve

from . import app_settings

logger = logging.getLogger(__name__)


def sanitize_url(url):
    """Sanitize the URL to prevent malicious content."""
    parsed_url = urlparse(url)

    # Ensure the URL is in the allowed list
    if parsed_url.hostname not in settings.ALLOWED_HOSTS:
        logger.warning("Invalid base URL provided: %s", url)
        return ""
    return url


def validate_path(path):
    """Validate the path to ensure it matches an expected pattern and is within allowed limits."""
    if not isinstance(path, str):
        logger.warning("Invalid path type provided: %s", type(path))
        return ""

    if app_settings.PATH_XSS_SAFE_MODE:
        # Ensure the path contains only alphanumeric characters, dashes, underscores, and slashes
        if not re.match(r"^[a-zA-Z0-9_\-/]*$", path):
            logger.warning("Invalid path provided: %s", path)
            return ""

    components = path.split("/")
    # Check path depth
    if len(components) > app_settings.PATH_MAX_DEPTH:
        logger.warning("Path depth exceeded for: %s", path)
        return ""

    # Check each path component's length
    for component in components:
        if len(component) > app_settings.PATH_MAX_COMPONENT_LENGTH:
            logger.warning("Path component length exceeded in: %s", path)
            return ""

    return path


class Breadcrumbs:
    def __init__(self, base_url="", path=None):
        self.base_url = sanitize_url(base_url)
        self.path = validate_path(path)
        self.items = []

    def get_items(self):
        if not self.items:
            self._fill_items()
        return self.items

    def as_list(self):
        return [item.as_dict() for item in self.get_items()]

    def _split_path(self, path=None):
        """Returns a list of the path components between slashes"""
        if not path:
            path = self.path
        if path.endswith("/"):
            path = path[:-1]
        if path.startswith("/"):
            path = path[1:]

        # avoid splitting and returning a list with an empty string
        if path == "":
            return list()

        result = path.split("/")
        return result

    def _add_home(self):
        b_item = BreadcrumbsItem(
            base_url=self.base_url,
            name_raw=app_settings.HOME_LABEL,
            path="/",
            position=1,
        )
        self.items.append(b_item)

    def _fill_items(self):
        path = "/"
        parts = self._split_path()

        # add home
        # if have to show home item, and location is home, shows it
        # or if location is not home, always shows home in breadcrumbs
        if (app_settings.SHOW_AT_BASE_PATH and not parts) or parts:
            self._add_home()

        if parts == []:
            return

        for i, item in enumerate(parts):
            path = urljoin(path, item + "/")
            b_item = BreadcrumbsItem(
                base_url=self.base_url, name_raw=item, path=path, position=i + 2
            )
            self.items.append(b_item)


class BreadcrumbsItem:
    def __init__(self, name_raw, path, position, base_url=None):
        self.name_raw = escape(name_raw)  # Escape the raw name
        self.path = escape(path)  # Escape the path
        self.position = position
        self.resolved_url = self._get_resolved_url_metadata()
        self.base_url = base_url

    def _get_resolved_url_metadata(self):
        try:
            func, args, kwargs = resolve(self.path)
            return True
        except Resolver404:
            return False

    def get_url(self):
        result = urljoin(self.base_url, self.path)
        return result

    def get_name(self):
        if self.position == 2 and app_settings.SHOW_VERBOSE_NAME:
            try:
                return apps.get_app_config(self.name_raw).verbose_name
            except Exception:
                pass
        return self.name_raw

    def as_dict(self):
        result = {
            "position": self.position,
            "name": self.get_name(),
            "path": self.path,
            "url": self.get_url(),
            "resolved": self.resolved_url,
        }
        return result

    def __str__(self):
        return "{}: {} {}".format(self.position, self.name_raw, self.path)
