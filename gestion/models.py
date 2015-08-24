#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Gestion(models.Model):
    hoy = datetime.now()
    anho = hoy.strftime("%Y")
    a_ini = int(anho) - 5
    a_fin = int(anho) + 1
    anhos = ()
    for a in range(a_ini, a_fin):
        anhos += ((a, a),)
    gestion = models.IntegerField(max_length='4', verbose_name='Registro Gestion', choices=anhos, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
        return str(self.gestion)
    def __str__(self):
        return str(self.gestion)
    class Meta:
        ordering = ['gestion']
        verbose_name_plural = 'Gestion'
        permissions = (
            ('index_gestion', 'Index Gestiones'),
        )

class Poblacion(models.Model):
    grupo = models.CharField(max_length='1')
    grupo_edad = models.CharField(max_length='100', verbose_name='Grupos de Edad')
    hombre = models.PositiveIntegerField(verbose_name='Numero de Hombres', default='0')
    mujer = models.PositiveIntegerField(verbose_name='Numero de Mujeres', default='0')
    suma_problacion = models.BooleanField(default=True, verbose_name='Suma Poblacion')
    poblacion_total = models.BooleanField(default=False, verbose_name='Poblacion Total')
    gestion = models.ForeignKey(Gestion, null=True, blank=True)
    def total(self):
        return self.hombre + self.mujer
    def porcentaje(self):
        g = Gestion.objects.get(gestion = int(self.gestion.gestion))
        po = Poblacion.objects.get(gestion = g, poblacion_total = True)
        suma = po.hombre + po.mujer
        porcentaje = float(self.hombre + self.mujer)/suma
        return round(porcentaje*100, 1)
    def __unicode__(self):
        return self.grupo_edad
    def __str__(self):
        return self.grupo_edad
    class Meta:
        verbose_name = 'Poblacion'
        verbose_name_plural = 'Poblaciones'
        ordering = ['grupo']
        permissions = (
            ('index_poblacion', 'Indes Poblaciones'),
        )