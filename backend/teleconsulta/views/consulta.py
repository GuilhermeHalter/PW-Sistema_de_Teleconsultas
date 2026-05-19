from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from teleconsulta.models.consulta import Consulta
from teleconsulta.serializers.consulta import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]