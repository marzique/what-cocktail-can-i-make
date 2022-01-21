
from rest_framework.routers import DefaultRouter

from apps.cocktails import views as cocktail_views


router = DefaultRouter()

router.register('cocktails', cocktail_views.CocktailViewSet, basename='cocktails')
