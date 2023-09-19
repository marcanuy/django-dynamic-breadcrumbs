from unittest.mock import patch

from django.test import TestCase, override_settings

from dynamic_breadcrumbs.utils import (
    Breadcrumbs,
    validate_path,
    sanitize_url,
)
from dynamic_breadcrumbs import app_settings
from django.conf import settings


@override_settings(ALLOWED_HOSTS=["www.example.com"])
class SanitizeUrlTests(TestCase):
    def test_sanitize_base_urls_host_in_allowed_hosts_keeps_url(self):
        base_url = f"https://{settings.ALLOWED_HOSTS[0]}"

        result = sanitize_url(url=base_url)

        self.assertEqual(result, base_url)

    def test_sanitize_base_urls_host_not_in_allowed_hosts_returns_empty_string(self):
        base_url = "https://anothersite.com"

        result = sanitize_url(url=base_url)

        self.assertEqual(result, "")


class ValidatePathTests(TestCase):
    def test_validate_path_not_string_returns_empty_string(self):
        path = 3.1416

        result = validate_path(path=path)

        self.assertEqual(result, "")

    def test_validate_path_check_alphanumeric_returns_empty_string(self):
        app_settings.PATH_XSS_SAFE_MODE = True
        path = "*%#$@@#*(/%#%_)*"

        result = validate_path(path=path)

        self.assertEqual(result, "")

    def test_validate_path_non_check_alphanumeric_returns_path(self):
        app_settings.PATH_XSS_SAFE_MODE = False
        path = "*%#$@@#*(/%#%_)*"

        result = validate_path(path=path)

        self.assertEqual(result, path)


class BreadcrumbsTests(TestCase):
    def setUp(self):
        self.host = settings.ALLOWED_HOSTS[0]

        # response = self.client.get('/')
        # request = HttpRequest().build_absolute_uri(location="/")
        # print(request)

        # self.breadcrumbs = Breadcrumbs(base_url=self.base_url)

    def test_split_path_ending_in_slash(self):
        path = "/scale/minor-scale/"
        expected_result = ["scale", "minor-scale"]
        breadcrumbs = Breadcrumbs()

        paths = breadcrumbs._split_path(path=path)

        self.assertEqual(paths, expected_result)

    def test_split_path_ending_in_char(self):
        path = "/scale/minor-scale/c"
        expected_result = ["scale", "minor-scale", "c"]
        breadcrumbs = Breadcrumbs()

        paths = breadcrumbs._split_path(path=path)

        self.assertEqual(paths, expected_result)

    def test_split_path_returns_empty_list(self):
        path = "/"
        expected_result = []

        paths = Breadcrumbs()._split_path(path=path)

        self.assertEqual(paths, expected_result)

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_process_all_paths_including_home(self, mock_resolve):
        mock_resolve = True  # noqa
        base_url = "https://example.com"
        path = "/scale/minor-scale/c"
        breadcrumbs = Breadcrumbs(base_url=base_url, path=path)

        result = breadcrumbs.get_items()

        self.assertEqual(len(result), 4)

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_as_list(self, mock_resolve):
        mock_resolve = True  # noqa
        path = "/continent/some-continent/"
        breadcrumbs = Breadcrumbs(path=path)

        result = breadcrumbs.as_list()

        self.assertEqual(result[0]["name"], app_settings.HOME_LABEL)
        self.assertEqual(result[1]["name"], "continent")
        self.assertEqual(result[2]["name"], "some-continent")

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_as_list_only_home(self, mock_resolve):
        mock_resolve = True  # noqa
        app_settings.SHOW_AT_BASE_PATH = True
        path = "/"
        breadcrumbs = Breadcrumbs(path=path)

        result = breadcrumbs.as_list()

        self.assertEqual(len(result), 1)

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_as_list_not_showing_at_home(self, mock_resolve):
        mock_resolve = True  # noqa
        app_settings.SHOW_AT_BASE_PATH = False
        path = "/"
        breadcrumbs = Breadcrumbs(path=path)

        result = breadcrumbs.as_list()

        self.assertEqual(len(result), 0)

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_show_home_at_base_url(self, mock_resolve):
        mock_resolve = True  # noqa
        app_settings.SHOW_AT_BASE_PATH = True
        path = "/"
        breadcrumbs = Breadcrumbs(path=path)

        result = breadcrumbs.as_list()

        self.assertEqual(len(result), 1)

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_hide_home_at_base_url(self, mock_resolve):
        mock_resolve = True  # noqa
        app_settings.SHOW_AT_BASE_PATH = False
        path = "/"
        breadcrumbs = Breadcrumbs(path=path)

        result = breadcrumbs.as_list()

        self.assertEqual(len(result), 0)

    @patch("dynamic_breadcrumbs.utils.BreadcrumbsItem._get_resolved_url_metadata")
    def test_filter_xss_attacks(self, mock_resolve):
        mock_resolve = False  # noqa

        app_settings.SHOW_AT_BASE_PATH = False
        malicious_code = """
        jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
        """  # noqa
        path = f"/level/{malicious_code}/leaf/"
        breadcrumbs = Breadcrumbs(path=path)

        result = breadcrumbs.as_list()
        self.assertEqual(len(result), 0)


# class BreadcrumbsItemTests(TestCase):
#     def test_get_resolved_url_metadata_resolves_valid_path(self):
#         item = BreadcrumbsItem(
#             name_raw="some-continent", path="/continent/some-continent/", position=2
#         )

#         result = item._get_resolved_url_metadata()

#         self.assertTrue(result)

#     def test_get_resolved_url_metadata_not_resolves_invalid_path(self):
#         item = BreadcrumbsItem(
#             name_raw="some-continent", path="/conti/some-continent/", position=2
#         )

#         result = item._get_resolved_url_metadata()

#         self.assertFalse(result)
