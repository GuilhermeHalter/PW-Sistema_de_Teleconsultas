from rest_framework import viewsets, permissions
from teleconsulta.models.medico import Medico
from teleconsulta.serializers.medico import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_permissions(self):
        # Seguindo a lógica: Cadastro pode ser aberto ou restrito ao Admin
        # Se for auto-cadastro:
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]