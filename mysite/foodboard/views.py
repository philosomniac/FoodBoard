from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Recipe

# Create your views here.


# def index(request):
#     recipe_list = Recipe.objects.all()[:10]
#     context = {
#         'recipe_list': recipe_list
#     }
#     return render(request, 'foodboard/index.html', context)

class IndexView(generic.ListView):
    template_name = 'foodboard/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all()[:20]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'foodboard/detail.html'


# def detail(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     return render(request, 'foodboard/detail.html', {'recipe': recipe})
