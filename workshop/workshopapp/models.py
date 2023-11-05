from django.db import models
from django.contrib.auth.models import User


class Frame(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=1000, default="")
    cost = models.IntegerField(null=False)
    amount = models.IntegerField(default=0)

    def is_sold(self) -> bool:
        return self.amount == 0

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    content = models.CharField(max_length=1000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    text = models.CharField(max_length=2000)
