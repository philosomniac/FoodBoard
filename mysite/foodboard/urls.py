from django.urls import path

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


]
