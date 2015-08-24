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
from sedes.reportes import sms_gestion, generar_pdf

from actividad.form import ActiForm
from actividad.models import Actividad

def index_actividad(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividades/index.html', {
        'actividades':actividades,
    })

def new_actividad(request):
    if request.method == 'POST':
        formulario = ActiForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            log_addition(request, c, 'Actividad Creada Correctamete')
            sms = ' Actividad <strong>%s</strong> Creada Correctamente'% (c.nombre)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_actividad))
    else:
        formulario = ActiForm()
    return render(request, 'actividades/new_actividad.html', {
        'formulario':formulario,
    })

def list_change_actividad(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividades/list_change.html', {
        'actividades':actividades,
    })

def update_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, pk = actividad_id)
    if request.method == 'POST':
        formulario = ActiForm(request.POST, instance=actividad)
        if formulario.is_valid():
            a = formulario.save()
            log_change(request, a, 'Actividad Modificada')
            sms = 'Actividad Modificada Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(list_change_actividad))
    else:
        formulario = ActiForm(instance=actividad)
    return render(request, 'actividades/update.html', {
        'formulario':formulario,
    })