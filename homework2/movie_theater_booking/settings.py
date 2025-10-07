"""
Django settings for movie_theater_booking project.
Production-ready for Render, Django 5.x.
"""

from pathlib import Path
import os
import dj_database_url

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core security toggles from environment ---
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "INSECURE-DEV-ONLY-CHANGE-ME")

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
    "editor-cs4300advancedswe-19.devedu.io",
    "app-cs4300advancedswe-19.devedu.io",
]

# Add your Render URL via env once you know it:
# e.g. CSRF_TRUSTED_ORIGIN=https://cs4300-y9l7.onrender.com
CSRF_TRUSTED_ORIGINS = [
    "https://app-cs4300advancedswe-19.devedu.io",
    "https://editor-cs4300advancedswe-19.devedu.io",
    "https://cs4300-y9l7.onrender.com/"
]

# --- Installed apps ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "bookings",
]

# --- Middleware (WhiteNoise right after SecurityMiddleware) ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # must be here
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "movie_theater_booking.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # app templates are used (bookings/templates/...)
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "movie_theater_booking.wsgi.application"

# --- Database ---
# Use Postgres on Render when DATABASE_URL is present; otherwise SQLite.
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    db_cfg = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    # Enforce SSL only for Postgres
    if db_cfg.get("ENGINE", "").endswith("postgresql"):
        db_cfg.setdefault("OPTIONS", {})
        db_cfg["OPTIONS"]["sslmode"] = "require"
    DATABASES = {"default": db_cfg}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Internationalization ---
LANGUAGE_CODE = "en-us"
# Use UTC in prod; Django uses tz-aware datetimes when USE_TZ=True
TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
USE_I18N = True
USE_TZ = True

# --- Static files ---
# Django 5 uses STORAGES instead of STATICFILES_STORAGE
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# --- Default PK type ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Render / proxy security ---
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
