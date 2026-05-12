from django.db import models
from .usuario import Usuario, UserRole
from .especialidade import Especialidade # Importando a nova tabela

class Medico(Usuario):
    crm = models.CharField(max_length=20, unique=True)
    # Mudança aqui: Relacionamento ManyToMany
    especialidades = models.ManyToManyField(Especialidade, related_name='medicos')

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = UserRole.MEDICO
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dr(a). {self.nomeCompleto} (CRM: {self.crm})"