from django.forms import ModelForm

from gestion.models import Gestion, Poblacion

class GestionForm(ModelForm):
    class Meta:
        model = Gestion
        exclude = ['usuario']

class PoblacionForm(ModelForm):
    class Meta:
        model = Poblacion
        exclude = ['gestion', 'poblacion_total']

class PoblacionTotalForm(ModelForm):
    class Meta:
        model = Poblacion
        exclude = ['gestion', 'poblacion_total', 'suma_problacion']