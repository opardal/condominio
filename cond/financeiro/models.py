from django.db import models
from django.urls import reverse

# Create your models here.


class Despesa(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.FloatField()

    def get_absolute_url(self):
        return reverse('financeiro:despesa-detail', kwargs={'pk': self.pk})
   