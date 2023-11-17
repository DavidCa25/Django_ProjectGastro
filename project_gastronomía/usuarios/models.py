from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico debe estar configurado.')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, apellido=apellido, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    TIPO_USUARIO_CHOICES = [
        ('admin', 'Administrador'),
        ('cliente', 'Usuario Cliente'),
        ('vendedor', 'Vendedor'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    tipoUsuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()


    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.email
