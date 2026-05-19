from rest_framework import serializers
from teleconsulta.models.consulta import Consulta


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = '__all__'