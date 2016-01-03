"""
Definition of urls for CloudSite.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from CloudApi.api import CloudStateViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clouds', CloudStateViewset)
urlpatterns = router.urls


