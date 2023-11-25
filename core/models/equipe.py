from django.db import models
from uploader.models import Image
from core.models.evento import Evento


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    nota = models.IntegerField(default=0)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
    )
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name="equipes")


    def __str__(self):
        return self.nome