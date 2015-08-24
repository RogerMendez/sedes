from django.forms import ModelForm, TextInput

from centrosalud.models import Centro

class CentroForm(ModelForm):
    class Meta:
        model = Centro
        fields = '__all__'
        #exclude = ['usuario']
