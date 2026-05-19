"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from teleconsulta.views.usuario import UsuarioViewSet 
from teleconsulta.views.paciente import PacienteViewSet
from teleconsulta.views.especialidade import EspecialidadeViewSet
from teleconsulta.views.medico import MedicoViewSet
from teleconsulta.views.horario import HorarioViewSet
from teleconsulta.views.consulta import ConsultaViewSet



router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'pacientes', PacienteViewSet, basename='paciente')
router.register(r'especialidades', EspecialidadeViewSet, basename='especialidade')
router.register(r'medicos', MedicoViewSet, basename='medico')
router.register(r'horarios', HorarioViewSet, basename='horarios')
router.register(r'consultas', ConsultaViewSet, basename='consultas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
