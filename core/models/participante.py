from django.db import models
from core.models import User
from core.models.equipe import Equipe

class Participante(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT, related_name= "participantes")
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="participantes")

