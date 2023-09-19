import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "dynamic_breadcrumbs",
)

ALLOWED_HOSTS = ["www.example.com"]

MIDDLEWARE = []

SECRET_KEY = "foobar"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

