from django.db import models
from core.models.instituicao import Instituicao
from core.models.avaliador import Avaliador
from core.models.equipe import Equipe
from core.models.evento import Evento

class Hackathon(models.Model):
    equipes = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="hackathon")
    avaliadores = models.ForeignKey(Avaliador, on_delete=models.PROTECT, related_name="hackathon")
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name="hackathon")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT, related_name="hackathon")

    def __str__(self):
        return self.evento