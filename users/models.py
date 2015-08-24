from django.db import models

from django.contrib.auth.models import User
from centrosalud.models import Centro

class Perfil(models.Model):
    nombre = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField(verbose_name='Telefono/Celular')
    email = models.EmailField(verbose_name="Correo Electronico")
    avatar = models.ImageField(upload_to='avatars', verbose_name="Seleccione Avatar")
    usuario = models.OneToOneField(User, null=True)
    def __unicode__(self):
        return self.usuario.username
    def __str__(self):
        return self.usuario.username
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['usuario']
        permissions = (
            ('usuarios', 'Permiso de Usuarios'),
        )

class Centro_Usuario(models.Model):
    centro = models.ForeignKey(Centro)
    usuario = models.ForeignKey(User, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        ordering = ['centro']