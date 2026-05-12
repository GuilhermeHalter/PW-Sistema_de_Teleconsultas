from rest_framework import viewsets, permissions
from teleconsulta.models.especialidade import Especialidade
from teleconsulta.serializers.especialidade import EspecialidadeSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar as especialidades médicas.
    """
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

    def get_permissions(self):
        # Qualquer pessoa (mesmo não logada) pode listar as especialidades (ex: para busca)
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        # Apenas usuários logados (idealmente Admins) podem criar ou editar
        return [permissions.IsAuthenticated()]