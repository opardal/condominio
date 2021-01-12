from django.db import models

# Create your models here.


class Despesa(models.Model):
    titulo = models.CharField(max_length=200)
    valor = models.FloatField()
    