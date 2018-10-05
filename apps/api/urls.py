from rest_framework import routers

from django.conf.urls import url
from django.contrib import admin

import views as V

urlpatterns = [
    url(r'^test/', V.test),
    url(r'^login/', V.login),
]
