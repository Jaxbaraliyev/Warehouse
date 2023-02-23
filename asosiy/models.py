from django.db import models
from userapp.models import Ombor

class Mahsulot(models.Model):
    nom = models.CharField(max_length=30)
    brend = models.CharField(max_length=30)
    miqdor = models.PositiveIntegerField()
    kelgan_narx = models.IntegerField()
    sotuv_narx = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nom} ({self.brend})"


class Client(models.Model):
    nom = models.CharField(max_length=30)
    dokon = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    manzil = models.CharField(max_length=40)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nom}  ({self.dokon})"



