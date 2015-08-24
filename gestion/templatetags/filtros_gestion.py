from django import template
from django.db.models import Q
register = template.Library()

from gestion.models import Gestion, Poblacion

@register.filter(name='poblacion_total')
def poblacion_total(gestion):
    g = Gestion.objects.get(gestion = gestion)
    if  Poblacion.objects.filter(gestion = g, poblacion_total = True):
        return True
    else:
        return False