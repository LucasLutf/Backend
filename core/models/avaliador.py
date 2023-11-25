from django.db import models
from core.models import User
from core.models.evento import Evento

class Avaliador(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT, related_name= "avaliadores")
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name="avaliadores")

    
    class Meta:
        verbose_name_plural = "Avaliadores"