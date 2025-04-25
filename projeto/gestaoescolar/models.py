from django.db import models

class Gestao(models.Model):
    disciplina = models.CharField(max_length=50, null=False, blank=False)
    carga_horaria = models.CharField(max_length=50, null=False, blank=False)

# Create your models here.
