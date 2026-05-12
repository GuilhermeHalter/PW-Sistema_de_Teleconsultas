from rest_framework import serializers
from teleconsulta.models.medico import Medico
from teleconsulta.models.especialidade import Especialidade
from .especialidade import EspecialidadeSerializer

class MedicoSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # Mostra os detalhes das especialidades no GET
    especialidades_detalhes = EspecialidadeSerializer(source='especialidades', many=True, read_only=True)
    # Recebe os IDs das especialidades no POST/PUT
    especialidades_ids = serializers.PrimaryKeyRelatedField(
        queryset=Especialidade.objects.all(), 
        source='especialidades', 
        many=True, 
        write_only=True
    )

    class Meta:
        model = Medico
        fields = [
            'id', 'nomeCompleto', 'email', 'crm', 
            'especialidades_detalhes', 'especialidades_ids', 
            'role', 'status', 'password'
        ]
        read_only_fields = ['id', 'role', 'status']

    def create(self, validated_data):
        # Remove as especialidades antes de criar o usuário base
        especialidades = validated_data.pop('especialidades', [])
        medico = Medico.objects.create_user(**validated_data)
        # Adiciona as especialidades após o médico existir no banco
        medico.especialidades.set(especialidades)
        return medico