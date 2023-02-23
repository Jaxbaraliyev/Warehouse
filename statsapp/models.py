from django.db import models
from userapp.models import Ombor
from asosiy.models import Client, Mahsulot


class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    sana = models.DateTimeField()
    miqdor = models.PositiveSmallIntegerField()
    umumiy = models.PositiveIntegerField(null=True)
    tolandi = models.PositiveIntegerField()
    nasiya = models.PositiveIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.mahsulot}, ({self.client})'


