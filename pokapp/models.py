from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    name = models.CharField(max_length=24)
    specie = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    photo = models.CharField(max_length=150)


    def __str__(self):
        return self.name



