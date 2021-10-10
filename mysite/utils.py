
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
    from recipe_scraper.models.recipe import Recipe as scRecipe

    persistence = persistence_handler.PersistenceHandler()
    recipes = persistence.get_all_recipes()
    for recipe in recipes:
        r = fbRecipe()
        r.name = recipe.name
        r.url = recipe.url
        r.img_url = recipe.img_url
        try:
            r.save()
        except django.db.utils.IntegrityError:
            continue
