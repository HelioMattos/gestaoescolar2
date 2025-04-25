from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=50, null=False, blank=False)
# Create your models here.
