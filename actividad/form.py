from django.forms import ModelForm, TextInput

from actividad.models import Actividad

class ActiForm(ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
        #exclude = ['usuario']
