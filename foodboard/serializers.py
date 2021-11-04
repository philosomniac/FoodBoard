from foodboard import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['url', 'username', 'email', 'groups']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ['name', 'is_vegetarian', 'is_vegan', ]


class IngredientUsageSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = models.IngredientUsage
        fields = ['amount', 'unit', 'price', 'modifier', 'ingredient']


class RecipeSerializer(serializers.ModelSerializer):
    ingredientusage_set = IngredientUsageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recipe
        fields = ['url', 'name', 'img_url',
                  'ingredientusage_set',
                  'servings', 'prep_time', 'cook_time']
