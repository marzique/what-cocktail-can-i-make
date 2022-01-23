import django_filters

from django.db.models import Count

from apps.cocktails.models import Cocktail, Ingredient


class CocktailsFilter(django_filters.FilterSet):
    ingredients = django_filters.CharFilter(method='has_ingredients')
    name = django_filters.CharFilter(lookup_expr='icontains')
    glass = django_filters.CharFilter(lookup_expr='icontains', field_name='glass__name')

    class Meta:
        model = Cocktail
        fields = ('ingredients', 'iba', 'name', 'glass')

    def has_ingredients(self, queryset, name, value):
        if value:
            ing_names = list(set([i.lower().strip() for i in value.split(',') if i]))
            ingredients_ids = Ingredient.objects.filter(name__in=ing_names).values_list('id', flat=True)
            for cocktail in queryset:
                cocktail_ingredients_ids = cocktail.ingredients.values_list('id', flat=True)
                if not set(cocktail_ingredients_ids).issubset(ingredients_ids):
                    queryset = queryset.exclude(id=cocktail.id)
        return queryset
