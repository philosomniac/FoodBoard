from django.db import models

# Create your models here.


class Recipe(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=80)
    img_url = models.URLField()
