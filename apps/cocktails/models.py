from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator


class Ingredient(models.Model):
    name = models.CharField(max_length=256, unique=True)
    units = models.CharField(max_length=128)
    abv = models.PositiveIntegerField(default=0,
                                      validators=[MaxValueValidator(100)])

    class Meta:
        db_table = 'ingredient'

    def __str__(self):
        return self.name


class Glass(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='glasses')

    class Meta:
        db_table = 'glass'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    ingredients = models.ManyToManyField(Ingredient, related_name='cocktails')
    glass = models.ForeignKey(Glass, on_delete=models.PROTECT)
    image = models.ImageField(blank=True, null=True, upload_to='cocktails')
    iba = models.BooleanField(default=False)
    color = ArrayField(models.CharField(max_length=6), default=list)
    garnish = ArrayField(models.CharField(max_length=128), default=list, blank=True)
    recipe = models.TextField()

    class Meta:
        db_table = 'cocktail'

    def __str__(self):
        return self.name
