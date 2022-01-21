from rest_framework import serializers

from apps.cocktails.models import Cocktail, Ingredient


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'
        depth = 1


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        depth = 1
