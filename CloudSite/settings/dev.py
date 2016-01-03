from CloudSite.settings.base import *   # pylint: disable=W0614,W0401
import dj_database_url

DATABASES['default'] =  dj_database_url.config()