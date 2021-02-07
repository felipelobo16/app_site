from django.db import models

# Create your models here.

class Produtos(models.Model):
    produto = models.CharField(max_length=30)
    quantidade = models.FloatField(max_length=30)
    valor = models.FloatField(max_length=30)
    descricao = models.CharField(max_length=30)