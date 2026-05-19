from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from teleconsulta.models.horario import Horario
from teleconsulta.serializers.horario import HorarioSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]