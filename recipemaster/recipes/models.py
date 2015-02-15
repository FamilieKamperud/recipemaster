from django.conf import settings
from django.db import models


class Recipe(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class RecipeCollection(models.Model):
    recipes = models.ManyToManyField(Recipe, related_name='collections')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
