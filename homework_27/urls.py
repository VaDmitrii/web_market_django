from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from homework_27 import settings
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    # path('cat/', include('category.urls')),
    path('', include('ads.urls')),
    path('user/', include('users.urls')),
    # path('selection/', include('selection.urls')),
    # path('', views.index),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
