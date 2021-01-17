from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from cadastro.models import Economia
from datetime import datetime

# Create your models here.


class Competencia(models.Model):
    ano = models.PositiveSmallIntegerField(blank=False, null=False, default=datetime.today().year, validators=[MaxValueValidator(2100), MinValueValidator(2000)])
    mes = models.PositiveSmallIntegerField(blank=False, null=False, default=datetime.today().month, validators=[MaxValueValidator(12), MinValueValidator(1)])

    class Meta:
        unique_together = ("ano", "mes")

    def __str__(self):
        return str(self.ano)+str(self.mes).zfill(2) 


class Despesa(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    valor = models.FloatField()

    def get_absolute_url(self):
        return reverse('financeiro:despesa-detail', kwargs={'pk': self.pk})


class Boleto(models.Model):
    economia = models.ForeignKey(Economia, on_delete=models.CASCADE)

   