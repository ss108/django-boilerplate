from django.conf.urls import url
from django.contrib import admin

from .controllers.main import urlpatterns as main_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += main_urls
