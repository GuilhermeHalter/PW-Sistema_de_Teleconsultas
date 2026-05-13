from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
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
        """
        RN04: Permite cadastro público de pacientes (POST), 
        mas exige login para as demais ações.
        """
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=['get', 'patch'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """
        Retorna ou atualiza os dados do paciente logado com base no Token JWT.
        """
        try:
            # Busca o paciente vinculado ao ID do usuário autenticado
            paciente = Paciente.objects.get(id=request.user.id)
        except Paciente.DoesNotExist:
            return Response({"error": "Perfil de paciente não encontrado para este usuário."}, status=status.HTTP_404_NOT_FOUND)

        # Lógica para buscar dados (GET)
        if request.method == 'GET':
            serializer = self.get_serializer(paciente)
            return Response(serializer.data)

        # Lógica para atualizar dados (PATCH)
        elif request.method == 'PATCH':
            # partial=True permite atualizar apenas os campos enviados no JSON do Vue.js
            serializer = self.get_serializer(paciente, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)