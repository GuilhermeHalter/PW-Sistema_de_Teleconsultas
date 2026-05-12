from rest_framework import serializers
from teleconsulta.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Paciente
        fields = ['id', 'nomeCompleto', 'email', 'cpf', 'role', 'status', 'password']
        read_only_fields = ['id', 'role', 'status']

    def create(self, validated_data):
        # Usa o manager do Usuario para criar com senha criptografada
        return Paciente.objects.create_user(**validated_data)