from django.forms import ModelForm, TextInput

from users.models import Perfil

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        exclude = ['usuario']