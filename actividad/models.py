from django.db import models
from centrosalud.models import Centro

class Actividad(models.Model):
    nombre = models.CharField(max_length=80, verbose_name='Nombre de la Actividad')
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'actividades'
        ordering = ['nombre']