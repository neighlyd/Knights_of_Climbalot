# Import all settings from _base.py and build upon them.
from ._base import *

# Turn off Debug for production
DEBUG = False

# Set allowed hosts to url.
ALLOWED_HOSTS = ['.knightsofclimbalot.com', '.knightsofclimbalot.com.']
