from rest_framework import serializers
from teleconsulta.models.horario import Horario


class HorarioSerializer(serializers.ModelSerializer):
    medico_nome = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Horario
        fields = ['id', 'data_hora_inicio', 'data_hora_fim', 'disponivel', 'medicos', 'medico_nome', 'created_at']
        read_only_fields = ['id', 'created_at', 'medico_nome']
        extra_kwargs = {
            'medicos': {'required': False}
        }

    def get_medico_nome(self, obj):
        medico = obj.medicos.first()
        return medico.nomeCompleto if medico else None
