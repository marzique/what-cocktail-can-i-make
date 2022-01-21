from django.urls import path, include

from apps.api.routers import router

app_name = 'api'

urlpatterns = [
    # path('health/', core_views.HealthView.as_view(), name='health'),

    path('', include(router.urls)),
]