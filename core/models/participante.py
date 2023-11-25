from django.db import models
from core.models import User

class Participante(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT, related_name= "participantes")
