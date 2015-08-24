# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from sedes.log_usuarios import log_addition, log_change

from users.models import Perfil, Centro_Usuario
from users.form import PerfilForm
from centrosalud.models import Centro
from gestion.models import Gestion

def home(request):

	return render(request, 'base.html', {
	})

def login_user(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(info_usuario))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if Perfil.objects.filter(usuario = acceso):
                        request.session['perfil'] = True
                    else:
                        request.session['perfil'] = False
                    if Gestion.objects.all():
                        gestion = Gestion.objects.last()
                        request.session['gestion'] = gestion.gestion
                    else:
                        request.session['gestion'] = None
                    c_u = Centro_Usuario.objects.get(usuario = acceso)
                    request.session['centro'] = c_u.centro_id
                    sms = 'Sesión Iniciada Correctamente'
                    messages.success(request, sms, )
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        return HttpResponseRedirect(reverse(info_usuario))
                else:
                    sms = 'Su Cuenta de Usuario No Esta Activada'
                    messages.warning(request, sms,)
                    return HttpResponseRedirect(reverse(login_user))
            else:
                sms = 'Usted No Es Usuario Registrado'
                messages.error(request, sms, 'alert')
                return HttpResponseRedirect(reverse(login_user))
    else:
        formulario = AuthenticationForm()
    return render(request, 'users/login.html',{
        'formulario':formulario,
    })

@login_required(login_url='/login')
def info_usuario(request):

    return render(request,'users/index.html',{

    })

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    sms = 'Sesión Terminada Correctamente'
    messages.add_message(request, messages.INFO, sms)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def complete_profile(request):
    if request.method == 'POST':
        formulario = PerfilForm(request.POST, request.FILES)
        if formulario.is_valid():
            p = formulario.save()
            p.usuario = request.user
            p.save()
            log_addition(request, p, 'Perfil Creado Correctamente')
            sms = 'Perfil Creado Correctamente'
            messages.info(request, sms)
            request.session['perfil'] = True
            return HttpResponseRedirect(reverse(info_usuario))
    else:
        formulario = PerfilForm()
    return render(request, 'users/new_perfil.html', {
        'formulario':formulario,
    })

@login_required(login_url='/login')
def change_profile(request):
    perfil = Perfil.objects.get(usuario = request.user)
    if request.method == 'POST':
        formulario = PerfilForm(request.POST, request.FILES, instance=perfil)
        if formulario.is_valid():
            p = formulario.save()
            p.usuario = request.user
            p.save()
            log_change(request, p, 'Perfil Modificado Correctamente')
            sms = 'Perfil Modificado Correctamente'
            messages.info(request, sms)
            request.session['perfil'] = True
            return HttpResponseRedirect(reverse(info_usuario))
    else:
        formulario = PerfilForm(instance=perfil)
    return render(request, 'users/change_perfil.html', {
        'formulario':formulario,
    })

def index_usuarios(request):
    centro_usuario = Centro_Usuario.objects.all()
    return render(request, 'add_users/index.html', {
        'centro_usuario':centro_usuario,
    })

def list_centros(request):
    centros = Centro.objects.all()
    return render(request, 'add_users/list_centros.html',  {
        'centros':centros,
    })

def centro_asignar_usuario(request, centro_id):
    centro = get_object_or_404(Centro, pk = centro_id)
    centro_usuario = Centro_Usuario.objects.all()
    usuarios = User.objects.exclude(id__in = centro_usuario.values('usuario_id'))
    return render(request, 'add_users/list_users.html', {
        'centro':centro,
        'usuarios':usuarios,
    })

def add_usuario_centro(request, centro_id, user_id):
    centro = get_object_or_404(Centro, pk = centro_id)
    user = get_object_or_404(User, pk = user_id)
    user.is_active = True
    user.save()
    c = Centro_Usuario.objects.create(
        centro = centro,
        usuario = user,
    )
    return HttpResponseRedirect(reverse(centro_asignar_usuario, args={centro.id}))

def list_centros_usuarios(request):
    centros = Centro.objects.all()
    return render(request, 'add_users/list_centros_usuarios.html', {
        'centros':centros,
    })

def users_centro(request, centro_id):
    centro = get_object_or_404(Centro, pk = centro_id)
    centro_usuario = Centro_Usuario.objects.filter(centro = centro)
    return render(request, 'add_users/users_centro.html', {
        'centro':centro,
        'centro_usuario':centro_usuario,
    })

def new_user(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            u = formulario.save()
            u.is_active = False
            u.save()
            msm = "Usuario Creado Correctamente"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect(reverse(index_usuarios))
    else:
        formulario = UserCreationForm()
    return render(request, 'add_users/new_user.html', {
        'formulario':formulario,
    })