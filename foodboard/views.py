from datetime import timedelta, date
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.http import Http404
from .models import CookEvent, Ingredient, Recipe, User, IngredientUsage
from .forms import CookEventForm, NewUserForm
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def profile(request):
    return render(request, 'registration/profile.html')


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.data['registration_code'] != '42':
            return redirect('register')
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')

    form = NewUserForm()
    return render(request=request, template_name='registration/register.html', context={"form": form})


class IndexView(generic.TemplateView):
    template_name = 'foodboard/index.html'


class RecipeListView(generic.ListView):
    template_name = 'foodboard/recipes.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all()[:10]


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'foodboard/recipe_detail.html'


@login_required
def cook_events(request, year=0, month=0, day=0):
    if year == 0 or month == 0 or day == 0:
        start_date = date.today()
    else:
        try:
            start_date = date(year, month, day)
        except ValueError:
            raise Http404("Invalid date requested")

    week = []
    week.append(start_date)
    for day in range(1, 6):
        week.append(start_date + timedelta(days=day))

    cook_events = []

    for day in week:
        try:
            cook_event = CookEvent.objects.get(date=day)
            cook_events.append(cook_event)
        except:
            cook_events.append(CookEvent(date=day))

    next_date = start_date + timedelta(days=7)
    prev_date = start_date + timedelta(days=-7)

    ingredient_usages = []
    if request.GET.get('ingredients') == 'True':
        recipe_ids = [
            i.recipe.id for i in cook_events if i.recipe_id is not None]
        ingredient_usages = IngredientUsage.objects.filter(
            recipe__id__in=recipe_ids).order_by('ingredient__name')

    return render(request, 'foodboard/cook_events.html', {'cook_events': cook_events, 'current_date': start_date, 'next_date': next_date, 'prev_date': prev_date, 'ingredient_usages': ingredient_usages})


@login_required
def cook_event(request, pk=None):
    if request.method == 'POST':
        try:
            cook_event = CookEvent.objects.get(pk=pk)
        except ObjectDoesNotExist:
            cook_event = CookEvent()
        form = CookEventForm(request.POST, instance=cook_event)
        if form.is_valid():
            form.save()
            return redirect('foodboard:plan')

    elif pk is not None:
        event = get_object_or_404(CookEvent, pk=pk)
        form = CookEventForm(instance=event)
    else:
        if 'year' in request.GET:
            year = int(request.GET['year'])
            month = int(request.GET['month'])
            day = int(request.GET['day'])
            d = date(year, month, day)
            form = CookEventForm(initial={'date': d})
        else:
            form = CookEventForm()

    return render(request, 'foodboard/cook_event.html', {'form': form, 'pk': pk})


class IngredientView(generic.ListView):
    template_name = 'foodboard/ingredients.html'
    context_object_name = 'ingredient_list'

    def get_queryset(self):
        return Ingredient.objects.order_by('name')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
