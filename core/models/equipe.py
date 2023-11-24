from django.db import models
from core.models.participante import Participante
from uploader.models import Image


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    participantes = models.ManyToManyField(Participante, related_name="equipes")
    nota = models.IntegerField(default=0)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


    def __str__(self):
        return self.nome