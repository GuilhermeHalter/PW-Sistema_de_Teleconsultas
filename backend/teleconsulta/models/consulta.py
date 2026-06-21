from django.db import models
import uuid


class AppointmentStatus(models.TextChoices):
    DISPONIVEL = 'DISPONIVEL', 'Disponível'
    RESERVADA = 'RESERVADA', 'Reservada'
    AGUARDANDO_PAGAMENTO = 'AGUARDANDO_PAGAMENTO', 'Aguardando Pagamento'
    CONFIRMADA = 'CONFIRMADA', 'Confirmada'
    CANCELADA = 'CANCELADA', 'Cancelada'
    FINALIZADA = 'FINALIZADA', 'Finalizada'


class Consulta(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    status = models.CharField(
        max_length=30,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.DISPONIVEL
    )

    link_video = models.URLField(
        blank=True,
        null=True
    )

    codigo_acesso = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    paciente = models.ForeignKey(
        'Paciente',
        on_delete=models.CASCADE,
        related_name='consultas'
    )

    medico = models.ForeignKey(
        'Medico',
        on_delete=models.CASCADE,
        related_name='consultas'
    )

    horario = models.ForeignKey(
        'Horario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='consultas'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'consultas'

    def __str__(self):
        return f'Consulta {self.id}'

    def confirmar_consulta(self):
        self.status = AppointmentStatus.CONFIRMADA
        self.save()

    def cancelar_consulta(self):
        self.status = AppointmentStatus.CANCELADA
        self.save()

    def finalizar_consulta(self):
        self.status = AppointmentStatus.FINALIZADA
        self.save()