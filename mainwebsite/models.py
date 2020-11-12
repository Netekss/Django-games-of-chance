from django.db import models
from django.contrib.auth.models import User as UserModel


class User(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    money = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)

    def __str__(self):
        return self.username