from rest_framework.viewsets import ModelViewSet

from core.models import Participante
from core.serializers import ParticipanteSerializer


class ParticipanteViewSet(ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer
