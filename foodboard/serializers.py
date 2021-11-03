from foodboard import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['url', 'username', 'email', 'groups']
        
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ['url','name', 'img_url', 'ingredients', 'servings','prep_time','cook_time']