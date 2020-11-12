from django.db import models
from mainwebsite.models import User


class CrashPlayer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bet = models.IntegerField(default=0)
    attempt = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def money_in_attempt(self):
        return self.bet * self.attempt