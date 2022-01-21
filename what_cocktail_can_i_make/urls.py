from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from apps.cocktails.views import HealthCheckView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('apps.api.urls', namespace='api')),
    path('health/', HealthCheckView.as_view(), name='health'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
