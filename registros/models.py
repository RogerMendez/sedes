from django.db import models

from inscripcion.models import Inscripcion
from gestion.models import Gestion

class Registros(models.Model):
    gestion = models.ForeignKey(Gestion)
    inscripcion = models.ForeignKey(Inscripcion)