from django.db import models

# Create your models here.


class Condominio(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.IntegerField()


class Economia(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    identificacao = models.CharField(max_length=200)
    area = models.FloatField()


class Proprietario(models.Model):
    pass


class StatusEconomia(models.Model):
    #docupada = 
    #morador =
    pass 


class FonteDeRecurso(models.Model):
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    pass


class Criterio(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    pass
