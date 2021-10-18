from django.db import models
from django.utils import timezone

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=80, unique=True)
    is_vegetarian = models.BooleanField(null=True)
    is_vegan = models.BooleanField(null=True)


class Recipe(models.Model):
    url = models.URLField(unique=True, db_index=True)
    name = models.CharField(max_length=80, db_index=True)
    img_url = models.URLField()
    ingredients = models.ManyToManyField(Ingredient, through='IngredientUsage')
    servings = models.PositiveSmallIntegerField(default=1)
    prep_time = models.PositiveSmallIntegerField(default=0,
                                                 verbose_name="prep time (minutes)")
    cook_time = models.PositiveSmallIntegerField(default=0,
                                                 verbose_name="cook time (minutes)")

    def __str__(self):
        return self.name


class IngredientUsage(models.Model):
    class Meta:
        db_table = 'foodboard_ingredient_usage'

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    price = models.FloatField(null=True)
    modifier = models.CharField(max_length=20, null=True)


class CookEvent(models.Model):
    date = models.DateField(verbose_name="cook date")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
