#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404


from sedes.log_usuarios import log_addition, log_change

from centrosalud.models import Centro
from centrosalud.form import CentroForm

from actividad.models import Actividad


def home(request):
    return render(request, 'base.html', {
	})


def index(request):
    centros = Centro.objects.all()
    return render(request, 'centrosalud/index.html', {
        'centro':centros,
    })

@permission_required('centrosalud.add_centro',  login_url='/login')
def new_centro(request):
    if request.method == 'POST':
        formulario = CentroForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            log_addition(request, c, 'Centro Creado Correctamete')
            sms = 'Centro <strong>%s</strong> Creado Correctamente'% (c.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        formulario = CentroForm()
    return render(request, 'centrosalud/new_centrosalud.html', {
        'formulario':formulario,
    })

def mod_centro(request):
    centros = Centro.objects.all()
    return render(request, 'centrosalud/mod_centro.html',{
        'centro':centros
    })

def update_centro(request, centro_id):
    centro = get_object_or_404(Centro, pk = centro_id)
    if request.method == 'POST':
        formulario = CentroForm(request.POST, instance=centro)
        if formulario.is_valid():
            c = formulario.save()
            log_change(request, c, 'Centro de Salud Modificada')
            sms = 'Centro <strong>%s</strong> Modificada Correctamente'% (c.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(mod_centro))
    else:
        formulario = CentroForm(instance=centro)
    return render(request, 'centrosalud/update_centro.html', {
        'formulario':formulario,
        'centro':centro,
    })
def detalle_centro(request, centro_id):
    lista = get_object_or_404(Centro, pk = centro_id)
    return render(request, 'centrosalud/detail.html',{
        'centro':lista,
    })