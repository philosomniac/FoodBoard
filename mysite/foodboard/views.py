from datetime import datetime, timedelta, date
from django.db.models.base import Model
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import CookEvent, Ingredient, Recipe

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'foodboard/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all()[:10]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'foodboard/detail.html'


def cook_events(request, year=0, month=0, day=0):
    if year == 0 or month == 0 or day == 0:
        startdate = date.today()
    else:
        startdate = datetime(year, month, day)

    week = []
    week.append(startdate)
    for day in range(1, 6):
        week.append(startdate + timedelta(days=day))

    cook_events = []

    for day in week:
        try:
            cook_event = CookEvent.objects.get(date=day)
            cook_events.append(cook_event)
        except:
            cook_events.append(CookEvent(date=day))

    return render(request, 'foodboard/cook_events.html', {'cook_events': cook_events})


class IngredientView(generic.ListView):
    template_name = 'foodboard/ingredients.html'
    context_object_name = 'ingredient_list'

    def get_queryset(self):
        return Ingredient.objects.order_by('name')
