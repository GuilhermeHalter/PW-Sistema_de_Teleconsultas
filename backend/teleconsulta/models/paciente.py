from django.db import models
from .usuario import Usuario, UserRole

class Paciente(Usuario):
    # Atributos específicos do diagrama
    cpf = models.CharField(max_length=14, unique=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def save(self, *args, **kwargs):
        # Garante que ao criar um paciente, o role seja definido corretamente
        if not self.pk:
            self.role = UserRole.PACIENTE
        super().save(*args, **kwargs)

    def agendar_consulta(self):
        """
        Método placeholder conforme seu diagrama. 
        A lógica real será implementada no módulo de Consultas.
        """
        pass

    def cancelar_consulta(self):
        """
        Método placeholder conforme seu diagrama.
        """
        pass

    def __str__(self):
        return f"Paciente: {self.nomeCompleto} (CPF: {self.cpf})"