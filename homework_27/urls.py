from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads import views
from homework_27 import settings

urlpatterns = [
    path('cat/', include('category.urls')),
    path('ad/', include('ads.urls')),
    path('user/', include('users.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
