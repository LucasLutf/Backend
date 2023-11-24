from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    idade = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.nome