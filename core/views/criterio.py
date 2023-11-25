from rest_framework.viewsets import ModelViewSet

from core.models import Criterio
from core.serializers import CriterioSerializer


class CriterioViewSet(ModelViewSet):
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer
