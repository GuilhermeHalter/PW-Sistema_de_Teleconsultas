from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from teleconsulta.models.paciente import Paciente
from teleconsulta.serializers.paciente import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o CRUD de Paciente.
    Filtra automaticamente apenas usuários que possuem perfil de Paciente.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """
        Retorna os dados do paciente logado com base no Token JWT.
        """
        # O 'request.user' é preenchido automaticamente pelo Django via JWT
        try:
            paciente = Paciente.objects.get(id=request.user.id)
            serializer = self.get_serializer(paciente)
            return Response(serializer.data)
        except Paciente.DoesNotExist:
            return Response({"error": "Paciente não encontrado"}, status=404)

    def get_permissions(self):
        # RN04: Permite cadastro público de pacientes (POST), mas exige login para o resto.
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


        from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

   