from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import CookEvent, Ingredient, Recipe

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'foodboard/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all()[:3]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'foodboard/detail.html'


def cook_events(request):
    cook_events = get_list_or_404(CookEvent)
    return render(request, 'foodboard/cook_events.html', {'cook_events': cook_events})


class IngredientView(generic.ListView):
    template_name = 'foodboard/ingredients.html'
    context_object_name = 'ingredient_list'

    def get_queryset(self):
        return Ingredient.objects.order_by('name')
