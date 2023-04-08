# Dev Configurations for the project
from .base import *

AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_REDIRECT_URL = "accounts:dashboard_view"
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


# Get the current machine IP Address
def get_ipaddress():
    import socket

    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address


ALLOWED_HOSTS = [get_ipaddress(), "localhost", "127.0.0.1"]
