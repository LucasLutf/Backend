from rest_framework.serializers import ModelSerializer

from core.models import Criterio


class CriterioSerializer(ModelSerializer):
    class Meta:
        model = Criterio
        fields = "__all__"
        