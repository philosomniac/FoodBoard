from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import api_views


app_name = 'foodboard'

api_urls = [
    path('recipe_list/', api_views.RecipeList.as_view(), name='recipe_list'),
    path('recipe_detail/<int:pk>/',
         api_views.RecipeDetail.as_view(), name='recipe_detail'),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(),
         name='recipes_detail'),
    path('plan/', views.cook_events, name='plan'),
    path('plan/<int:year>/<int:month>/<int:day>/',
         views.cook_events, name='plan_from_date'),
    path('plan/edit/<int:pk>/', views.cook_event, name='cook_event'),
    path('plan/edit/<int:pk>/save', views.cook_event, name='cook_event_save'),
    path('plan/add/', views.cook_event, name='cook_event_add'),
    path('ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('api/', include(api_urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)
