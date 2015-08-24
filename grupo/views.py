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

from django.db.models import Max

from sedes.log_usuarios import log_addition, log_change

from grupo.models import Grupo
from grupo.form import GrupoForm

def index_grupo(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupo/index.html', {
        'grupos':grupos,
    })

def new_grupo(request):
    if request.method == 'POST':
        formulario = GrupoForm(request.POST)
        if formulario.is_valid():
            g = formulario.save()
            a = Grupo.objects.all()
            g.ordenar = a.count() + 1
            g.save()
            log_addition(request, g, 'Grupo Creado')
            sms = 'Grupo Creado Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_grupo))
    else:
        formulario = GrupoForm()
    return render(request, 'grupo/new.html', {
        'formulario':formulario,
    })

def list_change_grupo(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupo/list_change.html', {
        'grupos':grupos,
    })

def update_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk = grupo_id)
    if request.method == 'POST':
        formulario = GrupoForm(request.POST, instance=grupo)
        if formulario.is_valid():
            g = formulario.save()
            log_change(request, g, 'Grupo Modificado')
            sms = 'Grupo Modificado Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(list_change_grupo))
    else:
        formulario = GrupoForm(instance=grupo)
    return render(request, 'grupo/update.html', {
        'formulario':formulario,
    })