from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from teleconsulta.models.medico import Medico
from teleconsulta.serializers.medico import MedicoSerializer
from teleconsulta.permissions import IsAdmin


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=['get', 'patch'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        try:
            medico = Medico.objects.get(id=request.user.id)
        except Medico.DoesNotExist:
            return Response(
                {"error": "Perfil de médico não encontrado para este usuário."},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'GET':
            serializer = self.get_serializer(medico)
            return Response(serializer.data)

        serializer = self.get_serializer(medico, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
