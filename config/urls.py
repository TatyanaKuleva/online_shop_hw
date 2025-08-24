from django.conf import settings
from django.conf.global_settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = ([
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
])
               # +static(settings.MEDIA.URL, document_root=MEDIA_ROOT))
