from django.contrib import admin

# Register your models here.
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('URLS', {'fields': ['url', 'img_url']})
    ]


admin.site.register(Recipe, RecipeAdmin)
