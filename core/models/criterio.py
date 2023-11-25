from django.db import models

from core.models import Evento

class Criterio(models.Model):
    evento = models.ForeignKey(Evento, on_delete = models.PROTECT, related_name = "criterios")
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.criterio