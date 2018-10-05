from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

#from django.conf.urls.static import static
#from apps.api.urls import urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.api.urls', namespace='api-rest')),
]
