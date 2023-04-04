# Dev Configurations for the project
from .base import *

AUTH_USER_MODEL = "accounts.CustomUser"
INSTALLED_APPS += [
    "django_extensions",
    "debug_toolbar"
] # Installed apps for dev environment
#  Handle debug toolbars internal ip address that link to localhost or 127.0.0.0.
if DEBUG:
    INTERNAL_IPS = (
        "127.0.0.1",
        "localhost",
    )
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
MIDDLEWARE += [] # Installed middleware for dev environment

# DEBUG Toolbar Settings
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": True,
}
