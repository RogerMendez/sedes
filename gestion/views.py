#encoding:utf-8
from django import template
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from sedes.reportes import sms_gestion
from sedes.log_usuarios import log_addition, log_change

from gestion.models import Gestion, Poblacion
from centrosalud.models import Centro
from gestion.form import GestionForm, PoblacionForm, PoblacionTotalForm

register = template.Library()

@permission_required('gestion.index_gestion', login_url='/login')
def index_gestion(request):
    gestiones = Gestion.objects.all()
    return render(request, 'gestion/index.html', {
        'gestiones':gestiones,
    })

@permission_required('gestion.add_gestion', login_url='/login')
def new_gestion(request):
    if request.method == 'POST':
        formulario = GestionForm(request.POST)
        if formulario.is_valid():
            g = formulario.save()
            g.usuario = request.user
            g.save()
            log_addition(request, g, 'Gestion Creada')
            sms = 'Gestion Creada Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_gestion))
    else:
        formulario = GestionForm()
    return render(request, 'gestion/new.html', {
        'formulario':formulario,
    })

@permission_required('gestion.index_poblacion', login_url='/login')
def index_poblacion(request):
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    poblaciones = Poblacion.objects.filter(gestion = gestion)
    return render(request, 'poblacion/index.html', {
        'poblaciones':poblaciones,
        'gestion':gestion,
    })

@permission_required('gestion.add_poblacion', login_url='/login')
def new_poblacion_total(request):
    sms_gestion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    if request.method == 'POST':
        formulario = PoblacionTotalForm(request.POST)
        if formulario.is_valid():
            po = formulario.save()
            po.gestion = gestion
            po.poblacion_total = True
            po.poblacion = False
            po.save()
            log_addition(request, po, 'Poblacion Total Creada')
            sms = "Poblacion <strong>%s</strong> Creado correctamente"% (po.grupo_edad)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_poblacion))
    else:
        formulario = PoblacionTotalForm()
    return render(request, 'poblacion/new.html', {
        'formulario':formulario,
    })

@permission_required('gestion.add_poblacion', login_url='/login')
def new_poblacion(request):
    sms_gestion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    if request.method == 'POST':
        formulario = PoblacionForm(request.POST)
        if formulario.is_valid():
            po = formulario.save()
            po.gestion = gestion
            po.save()
            log_addition(request, po, 'Poblacion Creada')
            sms = "Poblacion <strong>%s</strong> Creado correctamente"% (po.grupo_edad)
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(index_poblacion))
    else:
        formulario = PoblacionForm()
    return render(request, 'poblacion/new.html', {
        'formulario':formulario,
    })