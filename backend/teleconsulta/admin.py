from django.contrib import admin
from .models.usuario import Usuario
from .models.paciente import Paciente

admin.site.register(Usuario)
admin.site.register(Paciente)