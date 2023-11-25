from django.db import models
from uploader.models import Image
from core.models.evento import Evento
from core.models.participante import Participante


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name="equipes")
    membros = models.ManyToManyField(Participante, related_name="equipes")

    def __str__(self):
        return self.nome