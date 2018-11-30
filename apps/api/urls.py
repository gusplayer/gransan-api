from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin


import views as V


urlpatterns = [
    url(r'^muro/$', V.PostList.as_view(), name='muro-listado'),
    url(r'^muro/(?P<pk>[0-9]+)/$', V.PostDetail.as_view(), name='muro-listado-d'),
    #path('songs/', V.listarMuro.as_view(), name="muro-listado"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



