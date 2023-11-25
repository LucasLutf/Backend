from django.db import models
from core.models.avaliador import Avaliador
from core.models.equipe import Equipe


class Nota(models.Model):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.PROTECT, related_name="notas")
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="notas")
    avaliacao = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.equipe}, {self.avaliacao}'

    class Meta:
        verbose_name_plural = "Notas"