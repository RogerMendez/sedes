# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('centrosalud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('centro', models.ForeignKey(to='centrosalud.Centro')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['centro'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(verbose_name=b'Telefono/Celular')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Correo Electronico')),
                ('avatar', models.ImageField(upload_to=b'avatars', verbose_name=b'Seleccione Avatar')),
                ('usuario', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario'],
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'permissions': (('usuarios', 'Permiso de Usuarios'),),
            },
            bases=(models.Model,),
        ),
    ]
