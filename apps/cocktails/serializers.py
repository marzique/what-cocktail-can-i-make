import requests

from rest_framework import serializers

from apps.cocktails.models import Cocktail, Ingredient


class BaseSerializer:
    hostname = serializers.SerializerMethodField()

    def get_hostname(self, instance):
        try:
            response = requests.get('http://169.254.169.254/latest/meta-data/hostname')
            return response.json()
        except requests.exceptions.ConnectionError:
            return 'not aws environment'


class CocktailSerializer(serializers.ModelSerializer, BaseSerializer):
    hostname = serializers.SerializerMethodField()

    class Meta:
        model = Cocktail
        fields = '__all__'
        depth = 1


class IngredientSerializer(serializers.ModelSerializer, BaseSerializer):
    hostname = serializers.SerializerMethodField()
    class Meta:
        model = Ingredient
        fields = '__all__'
        depth = 1
