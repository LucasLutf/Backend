from django.db import models
from core.models.avaliador import Avaliador
from core.models.equipe import Equipe
from core.models.criterio import Criterio

class Nota(models.Model):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.PROTECT, related_name="notas")
    criterio = models.ForeignKey(Criterio, on_delete=models.PROTECT, related_name="notas")
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="notas")
    nota = models.IntegerField(default=0)