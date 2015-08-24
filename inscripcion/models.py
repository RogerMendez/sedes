from django.db import models
from gestion.models import Gestion, Poblacion
from centrosalud.models import Centro
from actividad.models import Actividad
from grupo.models import Grupo

class Inscripcion(models.Model):
    gestion = models.ForeignKey(Gestion)
    centro = models.ForeignKey(Centro)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.centro.nombre
    def __str__(self):
        return self.centro.nombre
    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural =  'Inscripciones'
        ordering = ['gestion']
        permissions = (
            ('index_inscripcion', 'Index Incripciones'),
        )

class Actividad_Inscripcion(models.Model):
    actividad = models.ForeignKey(Actividad)
    inscripcion = models.ForeignKey(Inscripcion)
    fecha_asignacion = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.inscripcion.centro.nombre
    def __str__(self):
        return self.inscripcion.centro.nombre
    class Meta:
        verbose_name = 'Acctividad Asignada'
        verbose_name_plural = 'Actividades Asignadas'
        ordering = ['inscripcion']
        permissions = (
            ('index_asignacion', 'Index Asignaciones'),
        )

class Actividad_grupo_poblacion(models.Model):
    actividad_inscripcion = models.ForeignKey(Actividad_Inscripcion)
    grupo = models.ForeignKey(Grupo)
    poblacion = models.ForeignKey(Poblacion)
    def __unicode__(self):
        return self.actividad_inscripcion.actividad.nombre
    def __str__(self):
        return self.actividad_inscripcion.actividad.nombre
    class Meta:
        verbose_name = 'Actividad Grupo'
        verbose_name_plural = 'Actividades Grupo'
        ordering = ['actividad_inscripcion']
        permissions = (
        )