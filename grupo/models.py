from django.db import models

class Grupo(models.Model):
    variable = models.CharField(max_length=100, verbose_name='Rango Poblacion')
    def __unicode__(self):
        return self.variable
    def __str__(self):
        return self.variable
    class Meta:
        verbose_name_plural = 'Grupos'
        verbose_name = 'Grupo'
        ordering = ['variable']