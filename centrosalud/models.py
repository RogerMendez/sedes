from django.db import models

class Centro(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Centro')
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(verbose_name='Telefono/Celular')
    responsable = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'centro_salud'
        verbose_name_plural = 'centros_salud'
        ordering = ['nombre']