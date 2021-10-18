from django.contrib import admin

# Register your models here.
from .models import Recipe
from .models import Ingredient
from .models import IngredientUsage
from .models import CookEvent


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('URLS', {'fields': ['url', 'img_url']})
    ]
    list_display = ('name', 'url')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', "is_vegetarian", "is_vegan")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientUsage)
admin.site.register(CookEvent)
