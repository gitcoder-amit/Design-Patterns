from django.db import models

class RecipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class Recipe(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 30)
    objects = RecipeManager()
    admin_objects = models.Manager()

    class Meta:
        indexes = [models.Index(fields = ['name', 'description']]