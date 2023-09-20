from django.urls import path

from geography.views import (
    ContinentListView,
    ContinentDetailView,
    CountryDetailView,
    CityDetailView,
)

urlpatterns = [
    path("", ContinentListView.as_view(), name="continent-list"),
    path(
        "<slug:slug>/",
        ContinentDetailView.as_view(),
        name="continent-detail",
    ),
    path(
        "<slug:continent_slug>/<slug:slug>/",
        CountryDetailView.as_view(),
        name="country-detail",
    ),
    path(
        "<slug:continent_slug>/<slug:country_slug>/<slug:slug>/",  # noqa
        CityDetailView.as_view(),
        name="city-detail",
    ),
]
