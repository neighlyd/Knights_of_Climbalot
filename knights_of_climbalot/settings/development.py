# Import all settings from _base.py and build upon them.
from ._base import *

# Debug for testing
DEBUG = True

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
