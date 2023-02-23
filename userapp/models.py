from django.contrib.auth.models import User
from django.db import models


class Ombor(models.Model):
    ism = models.CharField(max_length=40)
    dokon_nomi = models.CharField(max_length=40)
    tel = models.CharField(max_length=40)
    manzil = models.CharField(max_length=80)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.ism} ({self.dokon_nomi})'

