from django.forms import ModelForm, TextInput

from grupo.models import Grupo

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'