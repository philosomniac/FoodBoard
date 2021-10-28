
from recipe_scraper import persistence_handler
from recipe_scraper.models import recipe
import django


def setup():
    import os
    import sys
    sys.path.append('mysite')
    sys.path.append('foodboard')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    django.setup()
    print(os.getcwd())


if __name__ == "__main__":
    setup()
    from foodboard.models import Recipe as fbRecipe
    from foodboard.models import Ingredient as fbIngredient
    from foodboard.models import IngredientUsage as fbIngredientUsage
    from recipe_scraper.models.recipe import Recipe as scRecipe

    persistence = persistence_handler.PersistenceHandler()
    recipes = persistence.get_all_recipes()
    for recipe in recipes:
        r: fbRecipe
        created: bool
        r, created = fbRecipe.objects.get_or_create(url=recipe.url)
        r.name = recipe.name
        r.url = recipe.url
        r.img_url = recipe.img_url
        r.servings = recipe.servings
        r.prep_time = recipe.prep_time
        r.cook_time = recipe.cook_time

        try:
            r.save()
        except django.db.utils.IntegrityError:
            continue

        for ingredient in recipe.ingredient_set.ingredients:
            i: fbIngredient
            created2: bool
            i, created2 = fbIngredient.objects.get_or_create(
                name=ingredient.name)

            iu: fbIngredientUsage
            created3: bool
            iu, created3 = fbIngredientUsage.objects.get_or_create(
                recipe=r, ingredient=i)
            iu.amount = ingredient.amount
            iu.unit = ingredient.unit
            iu.price = ingredient.price
            iu.save()
