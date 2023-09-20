from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from geography.models import Continent, Country, City


class ContinentListView(ListView):
    model = Continent
    

class ContinentDetailView(DetailView):
    model = Continent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["continent_slug"] = self.kwargs.get("slug")
        return context

class CountryDetailView(DetailView):
    model = Country
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["continent_slug"] = self.kwargs.get("continent_slug")
        context["country_slug"] = self.kwargs.get("slug")
        return context

class CityDetailView(DetailView):
    model = City

