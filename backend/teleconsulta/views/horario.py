from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from teleconsulta.models.horario import Horario
from teleconsulta.models.medico import Medico
from teleconsulta.serializers.horario import HorarioSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN':
            medico_id = self.request.query_params.get('medico_id')
            if medico_id:
                return Horario.objects.filter(medicos__id=medico_id).order_by('data_hora_inicio')
            return Horario.objects.all().order_by('data_hora_inicio')

        medico_id = self.request.query_params.get('medico_id')

        try:
            medico = Medico.objects.get(id=user.id)
            return Horario.objects.filter(medicos=medico).order_by('data_hora_inicio')
        except Medico.DoesNotExist:
            pass

        if medico_id:
            return Horario.objects.filter(medicos__id=medico_id, disponivel=True).order_by('data_hora_inicio')

        return Horario.objects.filter(disponivel=True).order_by('data_hora_inicio')

    def perform_create(self, serializer):
        horario = serializer.save()
        try:
            medico = Medico.objects.get(id=self.request.user.id)
            horario.medicos.add(medico)
        except Medico.DoesNotExist:
            medico_id = self.request.data.get('medico_id')
            if medico_id:
                try:
                    medico = Medico.objects.get(id=medico_id)
                    horario.medicos.add(medico)
                except Medico.DoesNotExist:
                    pass

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def disponiveis(self, request):
        medico_id = request.query_params.get('medico_id')
        if not medico_id:
            return Response({'error': 'medico_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

        horarios = Horario.objects.filter(medicos__id=medico_id, disponivel=True).order_by('data_hora_inicio')
        serializer = self.get_serializer(horarios, many=True)
        return Response(serializer.data)
