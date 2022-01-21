from rest_framework import mixins, viewsets

from apps.cocktails.filters import CocktailsFilter
from apps.cocktails.models import Cocktail, Ingredient
from apps.cocktails.serializers import CocktailSerializer, IngredientSerializer


class CocktailViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()
    filterset_class = CocktailsFilter


class IngredientsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
