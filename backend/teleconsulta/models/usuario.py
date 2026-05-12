import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# --- Enums (conforme o diagrama) ---

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    MEDICO = 'MEDICO', 'Médico'
    PACIENTE = 'PACIENTE', 'Paciente'

class AccountStatus(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    ATIVO = 'ATIVO', 'Ativo'
    BLOQUEADO = 'BLOQUEADO', 'Bloqueado'
    REJEITADO = 'REJEITADO', 'Rejeitado'

# --- Manager ---

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nomeCompleto, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, nomeCompleto=nomeCompleto, **extra_fields)
        user.set_password(password)  # Trata a senhaHash do diagrama com segurança
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nomeCompleto, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', UserRole.ADMIN)
        extra_fields.setdefault('status', AccountStatus.ATIVO)
        return self.create_user(email, nomeCompleto, password, **extra_fields)

# --- Model Principal ---

class Usuario(AbstractBaseUser, PermissionsMixin):
    # Atributos do Diagrama
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomeCompleto = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # senhaHash é herdado de AbstractBaseUser como 'password'
    role = models.CharField(
        max_length=10, 
        choices=UserRole.choices, 
        default=UserRole.PACIENTE
    )
    status = models.CharField(
        max_length=15, 
        choices=AccountStatus.choices, 
        default=AccountStatus.PENDENTE
    )
    ativo = models.BooleanField(default=True)

    # Campos necessários para o Django Admin/Auth
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # Mapeia para o seu 'ativo' se desejar

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nomeCompleto']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f"{self.nomeCompleto} ({self.email})"