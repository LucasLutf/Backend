from django.db import models
from core.models.participante import Participante


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    participantes = models.ManyToManyField(Participante, related_name="equipes")
    nota = models.IntegerField(default=0)


    def __str__(self):
        return self.nome