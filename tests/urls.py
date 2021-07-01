from django.urls import path

from tests.views import (
    ContinentListView,
    ContinentDetailView,
    CountryListView,
    CountryDetailView,
    CityListView,
    CityDetailView,
)

urlpatterns = [
    path("", ContinentListView.as_view(), name="homepage"),
    path("continent/", ContinentListView.as_view(), name="continent-list"),
    path(
        "continent/<slug:continent_slug>/",
        ContinentDetailView.as_view(),
        name="continent-detail",
    ),
    path(
        "continent/<slug:continent_slug>/country",
        CountryListView.as_view(),
        name="country-list",
    ),
    path(
        "continent/<slug:continent_slug>/country/<slug:country_slug>/",
        CountryDetailView.as_view(),
        name="country-detail",
    ),
    path(
        "continent/<slug:continent_slug>/country/<slug:country_slug>/city/",
        CityListView.as_view(),
        name="city-list",
    ),
    path(
        "continent/<slug:continent_slug>/country/<slug:country_slug>/city/<slug:city_slug>/",  # noqa
        CityDetailView.as_view(),
        name="city-detail",
    ),
]
