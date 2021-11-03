from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import api_views

app_name = 'foodboard_api'
urlpatterns = [
    path('recipe_list/', api_views.RecipeList.as_view(), name='recipe_list'),
    path('recipe_detail/<int:pk>/', api_views.RecipeDetail.as_view(), name='recipe_detail'),

]
 
urlpatterns = format_suffix_patterns(urlpatterns)