#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from sedes.reportes import sms_gestion
from sedes.log_usuarios import log_addition, log_change

from gestion.models import Gestion, Poblacion
from inscripcion.models import Inscripcion, Actividad_Inscripcion, Actividad_grupo_poblacion
from centrosalud.models import Centro
from actividad.models import Actividad
from grupo.models import Grupo

@permission_required('inscripcion.index_inscripcion', login_url='/login')
def index_inscripcion(request):
    sms_gestion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    inscripciones = Inscripcion.objects.filter(gestion = gestion)
    return render(request, 'inscripciones/index.html', {
        'inscripciones':inscripciones,
    })

@permission_required('inscripcion.add_inscripcion', login_url='/login')
def list_centros_inscribir(request):
    sms_gestion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    inscripciones = Inscripcion.objects.filter(gestion = gestion)
    centros = Centro.objects.exclude(id__in = inscripciones.values('centro_id'))

    return render(request, 'inscripciones/list_centros_asignar.html', {
        'centros':centros,
    })

@permission_required('inscripcion.add_inscripcion', login_url='/login')
def add_centro_inscripcion(request, centro_id):
    centro = get_object_or_404(Centro, pk = centro_id)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    insc = Inscripcion.objects.create(
        gestion = gestion,
        centro = centro,
    )
    log_addition(request, insc, 'Inscripcion Realizada')
    sms = "Centro <strong>%s</strong> Inscrito Correctamente"% (centro.nombre)
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(list_centros_inscribir))

@permission_required('inscripcion.index_activdad', login_url='/login')
def index_asignacion(request):
    sms_gestion(request)
    gestion = Gestion.objects.get(gestion = request.session['gestion'])
    inscripciones = Inscripcion.objects.filter(gestion = gestion)
    return render(request, 'asignaciones/index.html', {
        'inscripciones':inscripciones,
    })

@permission_required('inscripcion.add_actividad_inscripcion', login_url='/login')
def inscripcion_actividad_asignar(request, insc_id):
    sms_gestion(request)
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    asignados = Actividad_Inscripcion.objects.filter(inscripcion = inscripcion)
    actividades = Actividad.objects.exclude(id__in = asignados.values('actividad_id'))

    return render(request, 'asignaciones/inscripcion_asignacion.html', {
        'inscripcion':inscripcion,
        'asignados':asignados,
        'actividades':actividades,
    })

@permission_required('inscripcion.add_actividad_inscripcion', login_url='/login')
def add_actividad_inscripcion(request, insc_id, actividad_id):
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    actividad = get_object_or_404(Actividad, pk = actividad_id)
    a = Actividad_Inscripcion.objects.create(
        inscripcion = inscripcion,
        actividad = actividad,
    )
    log_addition(request, a, 'Actividad asignada')
    log_change(request, actividad, 'Asignacion realizada')
    sms = "Actividad <strong>%s</strong> Asignada Correctamente"% (actividad.nombre)
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(inscripcion_actividad_asignar, args={inscripcion.id, }))

@permission_required('inscripcion.add_actividad_inscripcion', login_url='/login')
def remove_asignacion(request, asig_id):
    asignacion = get_object_or_404(Actividad_Inscripcion, pk = asig_id)
    inscripcion = Inscripcion.objects.get(id = asignacion.inscripcion_id)
    asignacion.delete()
    sms = 'Asignacion Quitada Correctamente'
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(inscripcion_actividad_asignar, args={inscripcion.id, }))

@permission_required('inscripcion.add_actividad_grupo_poblacion', login_url='/login')
def list_actividades_add_grupo(request, insc_id):
    sms_gestion(request)
    inscripcion = get_object_or_404(Inscripcion, pk = insc_id)
    actividades_inscripcion = Actividad_Inscripcion.objects.filter(inscripcion = inscripcion)

    return render(request, 'asignaciones/list_actividades_add_grupo.html', {
        'inscripcion':inscripcion,
        'actividades_inscripcion':actividades_inscripcion,
    })

@permission_required('inscripcion.add_actividad_grupo_poblacion', login_url='/login')
def ajax_list_grupos_add_actividad(request, insc_acti_id):
    if request.is_ajax():
        inscripcion_actividad = get_object_or_404(Actividad_Inscripcion, pk = insc_acti_id)
        actividad_grupo = Actividad_grupo_poblacion.objects.filter(actividad_inscripcion = inscripcion_actividad)
        grupos = Grupo.objects.exclude(id__in = actividad_grupo.values('grupo_id'))
        #grupos = Grupo.objects.all()
        html = render_to_string('asignaciones/ajax_list_grupos_add_actividad.html', {
            'inscripcion_actividad':inscripcion_actividad,
            'grupos':grupos,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('inscripcion.add_actividad_grupo_poblacion', login_url='/login')
def ajax_list_poblacion_add_grupo(request):
    if request.is_ajax():
        grupo_id = request.GET['grupo']
        act_insc_id = request.GET['actividad_inscripcion']
        grupo = Grupo.objects.get(id = grupo_id)
        inscripcion_actividad = Actividad_Inscripcion.objects.get(id = act_insc_id)
        poblaciones = Poblacion.objects.all()
        html = render_to_string('asignaciones/ajax_list_poblacion_add_grupo.html', {
            'grupo':grupo,
            'poblaciones':poblaciones,
            'inscripcion_actividad':inscripcion_actividad,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('inscripcion.add_actividad_grupo_poblacion', login_url='/login')
def ajax_list_grupos_asignados(request):
    if request.is_ajax():
        insc_acti_id = request.GET['actividad_inscripcion']
        actividad_inscripcion = Actividad_Inscripcion.objects.get(id = insc_acti_id)
        grupos_asignados = Actividad_grupo_poblacion.objects.filter(actividad_inscripcion = actividad_inscripcion)
        html = render_to_string('asignaciones/ajax_list_grupos_asignados.html', {
            'grupos_asignados':grupos_asignados,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('inscripcion.add_actividad_grupo_poblacion', login_url='/login')
def asignar_grupo_actividad_inscripcion(request, grupo_id, insc_acti_id, poblacion_id):
    poblacion = get_object_or_404(Poblacion, pk = poblacion_id)
    grupo = get_object_or_404(Grupo, pk = grupo_id)
    actividad_inscripcion = get_object_or_404(Actividad_Inscripcion, pk = insc_acti_id)
    a_g_p = Actividad_grupo_poblacion.objects.create(
        actividad_inscripcion = actividad_inscripcion,
        grupo = grupo,
        poblacion = poblacion,
    )
    log_addition(request, a_g_p, 'Grupo Asignado Correctamete')
    sms = "Grupo <strong>%s</strong> asignado correctamente"% (grupo.variable)
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(list_actividades_add_grupo, args={actividad_inscripcion.inscripcion_id, }))

@permission_required('inscripcion.add_actividad_grupo_poblacion', login_url='/login')
def remove_grupo_actividad_inscripcion(request, grupo_id):
    g_p_i = get_object_or_404(Actividad_grupo_poblacion, pk = grupo_id)
    inscripcion = Inscripcion.objects.get(id = g_p_i.actividad_inscripcion.inscripcion_id)
    g_p_i.delete()
    sms = "Grupo Eliminado Corrsssectamente"
    messages.info(request, sms)
    return HttpResponseRedirect(reverse(list_actividades_add_grupo, args={inscripcion.id, }))