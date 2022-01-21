from rest_framework import viewsets

from apps.cocktails.filters import CocktailsFilter
from apps.cocktails.models import Cocktail
from apps.cocktails.serializers import CocktailSerializer


class CocktailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()
    filterset_class = CocktailsFilter
