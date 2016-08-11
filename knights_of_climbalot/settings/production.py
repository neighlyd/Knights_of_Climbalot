# Import all settings from _base.py and build upon them.
from ._base import *

# Turn off Debug for production
DEBUG = False

# Set allowed hosts to url.
ALLOWED_HOSTS = ['.knightsofclimbalot.com', '.knightsofclimbalot.com.']

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 3
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Prevents a frame from serving content from another frame. Suggested to set as false for production, but may change with content generation. We will see.
X_FRAME_OPTIONS = 'DENY'

# Location of static files. This path must be an absolute path.
STATIC_ROOT = "/home/dusnei/knightsofclimbalot.com/public/static"
