from django.db import models


class Frame(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
