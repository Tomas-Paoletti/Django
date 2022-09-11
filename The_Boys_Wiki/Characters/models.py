from django.db import models


class Character(models.Model):
    Name = models.CharField(max_length=150)
    Alias = models.CharField(max_length=200)
    Sexo = models.CharField(max_length=50)
    Power_And_Skills = models.CharField(max_length=400)
    Image = models.URLField(blank=True)
    Family = models.CharField(max_length=200)
