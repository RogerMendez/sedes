from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # Examples:
    url(r'^$', 'users.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    #USUARIOS
    url(r'^login/$', 'users.views.login_user'),
    url(r'^logout/$', 'users.views.logout_user'),
    url(r'^user/$', 'users.views.info_usuario'),
    url(r'^user/new/profile/$', 'users.views.complete_profile'),
    url(r'^user/change/profile/$', 'users.views.change_profile'),
    #CENTROS DE SALUD
    url(r'^centros/$', 'centrosalud.views.new_centro'),
    url(r'^centros/listar/$', 'centrosalud.views.index'),
    url(r'^centros/change/$', 'centrosalud.views.mod_centro'),
    url(r'^centro/(?P<centro_id>\d+)/update/$', 'centrosalud.views.update_centro'),
    url(r'^centro/(?P<centro_id>\d+)/detalle/$', 'centrosalud.views.detalle_centro'),

    #ACTIVIDADES
    url(r'^actividad/$', 'actividad.views.index_actividad'),
    url(r'^actividad/new/$', 'actividad.views.new_actividad'),
    url(r'^actividad/list/change/$', 'actividad.views.list_change_actividad'),
    url(r'^actividad/(?P<actividad_id>\d+)/update/$', 'actividad.views.update_actividad'),

    #ASIGNACIONES
    url(r'^asignacion/$', 'inscripcion.views.index_asignacion'),
    url(r'^asignacion/(?P<insc_id>\d+)/centro/list/actividades/$', 'inscripcion.views.inscripcion_actividad_asignar'),
    url(r'^asignacion/(?P<insc_id>\d+)/centro/(?P<actividad_id>\d+)/actividad/asignar/$', 'inscripcion.views.add_actividad_inscripcion'),
    url(r'^asignacion/(?P<asig_id>\d+)/remover/$', 'inscripcion.views.remove_asignacion'),

    #ASIGNACION GRUPO
    url(r'^asignacion/(?P<insc_id>\d+)/centro/add/actividades/$', 'inscripcion.views.list_actividades_add_grupo'),
    url(r'^asignacion/(?P<grupo_id>\d+)/grupo/centro/(?P<insc_acti_id>\d+)/add/(?P<poblacion_id>\d+)/poblacion/$', 'inscripcion.views.asignar_grupo_actividad_inscripcion'),
    url(r'^asignacion/(?P<grupo_id>\d+)/centro/remove/grupo/$', 'inscripcion.views.remove_grupo_actividad_inscripcion'),

    url(r'^asignacion/(?P<insc_acti_id>\d+)/list/grupos/ajax/$', 'inscripcion.views.ajax_list_grupos_add_actividad'),
    url(r'^asignacion/list/poblacion/grupo/ajax/$', 'inscripcion.views.ajax_list_poblacion_add_grupo'),
    url(r'^asignacion/list/grupo/asignados/ajax/$', 'inscripcion.views.ajax_list_grupos_asignados'),

    #GRUPO
    url(r'^grupo/$', 'grupo.views.index_grupo'),
    url(r'^grupo/new/$', 'grupo.views.new_grupo'),
    url(r'^grupo/list/change/$', 'grupo.views.list_change_grupo'),
    url(r'^grupo/(?P<grupo_id>\d+)/update/$', 'grupo.views.update_grupo'),

    #ADD USUARIOS
    url(r'^users/all/$', 'users.views.index_usuarios'),
    url(r'^users/centros/list/$', 'users.views.list_centros'),
    url(r'^users/centro/(?P<centro_id>\d+)/users/all/$', 'users.views.centro_asignar_usuario'),
    url(r'^users/centro/(?P<centro_id>\d+)/user/(?P<user_id>\d+)/add/$', 'users.views.add_usuario_centro'),
    url(r'^users/centros/all/$', 'users.views.list_centros_usuarios'),
    url(r'^users/centro/(?P<centro_id>\d+)/users/asig/all$', 'users.views.users_centro'),
    url(r'^users/new/$', 'users.views.new_user'),


    #GESTIONES
    url(r'^gestion/$', 'gestion.views.index_gestion'),
    url(r'^gestion/new/$', 'gestion.views.new_gestion'),

    #POBLACION
    url(r'^poblacion/$', 'gestion.views.index_poblacion'),
    url(r'^poblacion/total/new/$', 'gestion.views.new_poblacion_total'),
    url(r'^poblacion/new/$', 'gestion.views.new_poblacion'),

    #INSCRIPCIONES
    url(r'^insc/$', 'inscripcion.views.index_inscripcion'),
    url(r'^insc/centros/add/$', 'inscripcion.views.list_centros_inscribir'),
    url(r'^insc/new/(?P<centro_id>\d+)/centro/$', 'inscripcion.views.add_centro_inscripcion'),

)
