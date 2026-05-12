from rest_framework import serializers
from teleconsulta.models.usuario import Usuario, UserRole, AccountStatus

class UsuarioSerializer(serializers.ModelSerializer):
    # Definimos o campo de senha explicitamente para garantir segurança
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = Usuario
        fields = [
            'id', 
            'nomeCompleto', 
            'email', 
            'role', 
            'status', 
            'ativo', 
            'password'
        ]
        # Campos que o usuário não pode alterar via API comum
        read_only_fields = ['id', 'status']

    def validate_email(self, value):
        """
        Validação extra para garantir e-mail único (além do nível de DB).
        """
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está cadastrado.")
        return value

    def create(self, validated_data):
        """
        Sobrescrevemos o método create para usar o create_user do Manager,
        garantindo que a senha seja criptografada (RN02).
        """
        return Usuario.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Sobrescrevemos o update para tratar a atualização de senha, caso enviada.
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance