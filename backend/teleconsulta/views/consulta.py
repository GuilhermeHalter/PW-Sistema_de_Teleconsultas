import uuid
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from teleconsulta.models.consulta import Consulta, AppointmentStatus
from teleconsulta.models.horario import Horario
from teleconsulta.models.medico import Medico
from teleconsulta.models.paciente import Paciente
from teleconsulta.serializers.consulta import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN':
            return Consulta.objects.all().order_by('-created_at')

        try:
            medico = Medico.objects.get(id=user.id)
            return Consulta.objects.filter(medico=medico).order_by('-created_at')
        except Medico.DoesNotExist:
            pass

        try:
            paciente = Paciente.objects.get(id=user.id)
            return Consulta.objects.filter(paciente=paciente).order_by('-created_at')
        except Paciente.DoesNotExist:
            pass

        return Consulta.objects.none()

    def create(self, request, *args, **kwargs):
        try:
            paciente = Paciente.objects.get(id=request.user.id)
        except Paciente.DoesNotExist:
            return Response(
                {"error": "Apenas pacientes podem criar consultas."},
                status=status.HTTP_403_FORBIDDEN
            )

        medico_id = request.data.get('medico')
        horario_id = request.data.get('horario')

        if not medico_id or not horario_id:
            return Response(
                {"error": "medico e horario são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            horario = Horario.objects.get(id=horario_id, disponivel=True)
        except Horario.DoesNotExist:
            return Response(
                {"error": "Horário não disponível."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            medico = Medico.objects.get(id=medico_id)
        except Medico.DoesNotExist:
            return Response(
                {"error": "Médico não encontrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

        horario.disponivel = False
        horario.save()

        consulta = Consulta.objects.create(
            paciente=paciente,
            medico=medico,
            horario=horario,
            status=AppointmentStatus.AGUARDANDO_PAGAMENTO
        )

        serializer = self.get_serializer(consulta)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def confirmar_pagamento(self, request, pk=None):
        consulta = self.get_object()

        if consulta.status != AppointmentStatus.AGUARDANDO_PAGAMENTO:
            return Response(
                {"error": "Consulta não está aguardando pagamento."},
                status=status.HTTP_400_BAD_REQUEST
            )

        room_name = f"teleconsulta-{str(consulta.id).replace('-', '')}"
        consulta.link_video = f"https://meet.jit.si/{room_name}"
        consulta.codigo_acesso = str(uuid.uuid4())[:8].upper()
        consulta.status = AppointmentStatus.CONFIRMADA
        consulta.save()

        serializer = self.get_serializer(consulta)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def cancelar(self, request, pk=None):
        consulta = self.get_object()

        cancelable = [
            AppointmentStatus.RESERVADA,
            AppointmentStatus.AGUARDANDO_PAGAMENTO,
            AppointmentStatus.CONFIRMADA
        ]

        if consulta.status not in cancelable:
            return Response(
                {"error": "Esta consulta não pode ser cancelada."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if consulta.horario:
            consulta.horario.disponivel = True
            consulta.horario.save()

        consulta.status = AppointmentStatus.CANCELADA
        consulta.save()

        serializer = self.get_serializer(consulta)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def finalizar(self, request, pk=None):
        consulta = self.get_object()

        if consulta.status != AppointmentStatus.CONFIRMADA:
            return Response(
                {"error": "Apenas consultas confirmadas podem ser finalizadas."},
                status=status.HTTP_400_BAD_REQUEST
            )

        consulta.status = AppointmentStatus.FINALIZADA
        consulta.save()

        serializer = self.get_serializer(consulta)
        return Response(serializer.data)
