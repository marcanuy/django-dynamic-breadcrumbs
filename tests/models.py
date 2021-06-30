from django.db import models
from django.urls import reverse

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="", editable=True, max_length=100)
    


class Continent(BaseModel):
    def get_absolute_url(self):
        return reverse('continent-detail', kwargs={'continent_slug': self.slug})

class Country(BaseModel):
    pass

class City(BaseModel):
    pass

