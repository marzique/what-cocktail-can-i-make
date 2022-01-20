from django.contrib import admin

from .models import Ingredient, Category, Glass, Cocktail


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'abv')


@admin.register(Glass)
class GlassAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'ingredients_str')

    def ingredients_str(self, obj):
        return ', '.join([ingredient.name for ingredient in obj.ingredients.all()])
