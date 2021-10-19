from django.urls import path

from . import views

app_name = 'foodboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('plan/', views.cook_events, name='plan'),
    path('ingredients/', views.IngredientView.as_view(), name='ingredients')
]
