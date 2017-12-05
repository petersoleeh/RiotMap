from django.db import models
import datetime as dt
from django.contrib.auth.models import User


# Create your models here.
class Riot(models.Model):
    location = models.CharField(max_length=255)
    riot_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    magnitude = models.CharField(max_length=30)


    def __str__(self):
        return self.location
