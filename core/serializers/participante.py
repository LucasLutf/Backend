from rest_framework.serializers import ModelSerializer

from core.models import Participante


class ParticipanteSerializer(ModelSerializer):
    class Meta:
        model = Participante
        fields = "__all__"