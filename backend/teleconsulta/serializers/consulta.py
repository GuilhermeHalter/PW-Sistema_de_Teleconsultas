from rest_framework import serializers
from teleconsulta.models.consulta import Consulta
from teleconsulta.models.horario import Horario


class ConsultaSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.SerializerMethodField(read_only=True)
    medico_nome = serializers.SerializerMethodField(read_only=True)
    horario_inicio = serializers.SerializerMethodField(read_only=True)
    horario_fim = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Consulta
        fields = [
            'id', 'status', 'link_video', 'codigo_acesso',
            'paciente', 'paciente_nome',
            'medico', 'medico_nome',
            'horario', 'horario_inicio', 'horario_fim',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'link_video', 'codigo_acesso', 'created_at', 'updated_at']

    def get_paciente_nome(self, obj):
        return obj.paciente.nomeCompleto if obj.paciente else None

    def get_medico_nome(self, obj):
        return obj.medico.nomeCompleto if obj.medico else None

    def get_horario_inicio(self, obj):
        return obj.horario.data_hora_inicio if obj.horario else None

    def get_horario_fim(self, obj):
        return obj.horario.data_hora_fim if obj.horario else None
