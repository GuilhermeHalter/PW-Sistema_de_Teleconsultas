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

    def get_permissions(self):
        # RN04: Permite cadastro público de pacientes (POST), mas exige login para o resto.
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]