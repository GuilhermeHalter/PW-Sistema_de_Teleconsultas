from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from teleconsulta.models.usuario import Usuario
from teleconsulta.serializers.usuario import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o CRUD de Usuario.
    Implementa automaticamente:
    - GET /usuarios/ (lista todos)
    - POST /usuarios/ (cria novo)
    - GET /usuarios/{id}/ (detalhes)
    - PUT/PATCH /usuarios/{id}/ (atualiza)
    - DELETE /usuarios/{id}/ (remove)
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        """
        RN04 – O acesso às funcionalidades deve respeitar o nível de permissão.
        - Qualquer um pode se cadastrar (POST).
        - Apenas usuários autenticados (JWT) podem listar ou editar.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        """
        Sobrescrita opcional: Em sistemas de saúde, muitas vezes optamos por 
        desativar o usuário (soft delete) em vez de apagar do banco.
        """
        usuario = self.get_object()
        usuario.ativo = False
        usuario.save()
        return Response(status=status.HTTP_204_NO_CONTENT)