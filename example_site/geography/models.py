from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="", editable=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Continent(BaseModel):
    def get_absolute_url(self):
        kwargs = {"continent_slug": self.slug}
        return reverse("continent-detail", kwargs=kwargs)


class Country(BaseModel):
    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
    )


class City(BaseModel):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )

