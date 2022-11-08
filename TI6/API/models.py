from django.db import models
from djongo import models

# Create your models here.

class Mamografia(models.Model):
    _id = models.ObjectIdField()
    imagem = models.TextField()
    imagem_processada = models.TextField(blank=True)
    rotulo = models.CharField(max_length=255)
    processado = models.BooleanField(default=False)
    classificado = models.BooleanField(default=False)
    tem_tumor = models.BooleanField(blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    data_processamento = models.DateTimeField(blank=True)
    data_classificacao = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['data_envio']
        db_table = "mamografias"