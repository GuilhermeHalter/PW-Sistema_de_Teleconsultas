from django.db import models
import uuid


class Horario(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()

    disponivel = models.BooleanField(default=True)

    medicos = models.ManyToManyField(
        'Medico',
        related_name='horarios'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'horarios'
        ordering = ['data_hora_inicio']

    def __str__(self):
        return f'{self.data_hora_inicio} - {self.data_hora_fim}'