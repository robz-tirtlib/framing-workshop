from django.db import models


class Frame(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=1000, default="")
    cost = models.IntegerField(null=False)
    amount = models.IntegerField(default=0)

    def is_sold(self) -> bool:
        return self.amount == 0

    def __str__(self) -> str:
        return self.name
