import django_filters

from django.db.models import Count

from apps.cocktails.models import Cocktail, Ingredient


class CocktailsFilter(django_filters.FilterSet):
    ingredients = django_filters.CharFilter(method='has_ingredients')

    class Meta:
        model = Cocktail
        fields = ('ingredients', 'iba', 'name', 'glass')

    def has_ingredients(self, queryset, name, value):
        if not value:
            return queryset

        ing_names = list(set([i.strip() for i in value.split(',') if i]))
        ingredients = Ingredient.objects.filter(name__in=ing_names)
        queryset = queryset.annotate(
            total_ingredients=Count('ingredients', distinct=True)
        ).filter(
            ingredients__in=ingredients
        ).filter(total_ingredients__lte=ingredients.count())
        return queryset


