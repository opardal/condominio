from django.db import models

# Create your models here.


class Despesa(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.FloatField()
   