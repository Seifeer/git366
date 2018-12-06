from __future__ import unicode_literals

from django.db import models

# Create your models here.
#1 modelo sobre contatos
class ItemAgenda(models.Model):
    data= models.DateField()
    hora= models.TimeField()
    titulo= models()
    descricao= models.TextField
    def __str__(self):
        return self.nome

