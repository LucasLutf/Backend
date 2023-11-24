from django.db import models
from uploader.models import Image


class Avaliador(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
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
    
    class Meta:
        verbose_name_plural = "Avaliadores"