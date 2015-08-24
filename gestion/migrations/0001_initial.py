# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gestion', models.IntegerField(unique=True, max_length=b'4', verbose_name=b'Registro Gestion', choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['gestion'],
                'verbose_name_plural': 'Gestion',
                'permissions': (('index_gestion', 'Index Gestiones'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.CharField(max_length=b'1')),
                ('grupo_edad', models.CharField(max_length=b'100', verbose_name=b'Grupos de Edad')),
                ('hombre', models.PositiveIntegerField(default=b'0', verbose_name=b'Numero de Hombres')),
                ('mujer', models.PositiveIntegerField(default=b'0', verbose_name=b'Numero de Mujeres')),
                ('suma_problacion', models.BooleanField(default=True, verbose_name=b'Suma Poblacion')),
                ('poblacion_total', models.BooleanField(default=False, verbose_name=b'Poblacion Total')),
                ('gestion', models.ForeignKey(blank=True, to='gestion.Gestion', null=True)),
            ],
            options={
                'ordering': ['grupo'],
                'verbose_name': 'Poblacion',
                'verbose_name_plural': 'Poblaciones',
                'permissions': (('index_poblacion', 'Indes Poblaciones'),),
            },
            bases=(models.Model,),
        ),
    ]
