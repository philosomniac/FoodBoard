from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipe

# Create your views here.


def index(request):
    recipe_list = Recipe.objects.all()[:10]
    context = {
        'recipe_list': recipe_list
    }
    return render(request, 'foodboard/index.html', context)


def detail(request, recipe_id):
    return HttpResponse("You're looking at recipe %s." % recipe_id)
