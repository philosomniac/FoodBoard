from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'foodboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('plan/', views.cook_events, name='plan'),
    path('plan/<int:year>/<int:month>/<int:day>/',
         views.cook_events, name='plan_from_date'),
    path('ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('plan/edit/<int:pk>/', views.cook_event, name='cook_event'),
    path('plan/edit/<int:pk>/save', views.cook_event, name='cook_event_save'),
    path('plan/add/', views.cook_event, name='cook_event_add'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('recipe_detail/<int:pk>/', views.recipe_detail, name='recipe_detail'),

]
 
urlpatterns = format_suffix_patterns(urlpatterns)