from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

ALLOWED_HOSTS = ["www.example.com"]

SECRET_KEY = "foobar"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
