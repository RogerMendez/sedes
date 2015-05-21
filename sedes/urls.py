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
    #url(r'^change/password/$', 'usuarios.views.change_password'),
    url(r'^user/$', 'users.views.info_usuario'),
    url(r'^user/new/profile/$', 'users.views.complete_profile'),
    url(r'^user/change/profile/$', 'users.views.change_profile'),

)
