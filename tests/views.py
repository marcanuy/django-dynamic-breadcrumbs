from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from tests.models import Continent, Country, City


class ContinentListView(ListView):
    model = Continent
    slug_field = "cotinent_slug"


class ContinentDetailView(DetailView):
    model = Continent
    slug_field = "cotinent_slug"


class CountryListView(ListView):
    def setup(self, request, *args, **kwargs):
        """Initialize attributes shared by all view methods."""
        super().setup(request, *args, **kwargs)
        continent_slug = self.kwargs.get("continent_slug")
        self.continent = get_object_or_404(Continent, slug=continent_slug)

    def get_queryset(self):
        """
        Return the list of items for this view.
        """
        qs = self.continent.country_set.all()
        return qs


class CountryDetailView(DetailView):
    model = Country
    slug_field = "country_slug"


class CityListView(ListView):
    pass


class CityDetailView(DetailView):
    model = City
    slug_field = "city_slug"
