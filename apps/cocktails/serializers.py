from rest_framework import serializers

from apps.cocktails.models import Cocktail


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'
        depth = 1
