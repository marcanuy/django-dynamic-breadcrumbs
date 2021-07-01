from django.urls import resolve, Resolver404
from urllib.parse import urljoin

from . import app_settings

class Breadcrumbs:
    def __init__(self, base_url="", path=None):
        self.base_url = base_url
        self.path = path
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
        result = path.split("/")
        return result

    def _fill_items(self):
        # add home
        b_item = BreadcrumbsItem(
            base_url=self.base_url,
            name_raw=app_settings.DYNAMIC_BREADCRUMBS_HOME_LABEL,
            path="/",
            position=1
        )
        self.items.append(b_item)

        # add paths
        path = "/"
        for i, item in enumerate(self._split_path()):
            path = urljoin(path, item + "/")
            b_item = BreadcrumbsItem(
                base_url=self.base_url, name_raw=item, path=path, position=i + 1
            )
            self.items.append(b_item)


class BreadcrumbsItem:
    def __init__(self, name_raw, path, position, base_url=None):
        self.name_raw = name_raw
        self.path = path
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
        # if self.resolved_url:
        #     # check view
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
