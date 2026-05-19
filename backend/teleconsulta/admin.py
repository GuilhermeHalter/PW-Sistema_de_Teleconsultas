from django.contrib import admin
from .models.usuario import Usuario
from .models.paciente import Paciente
from .models.especialidade import Especialidade
from .models.medico import Medico
from .models.horario import Horario

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Horario)
