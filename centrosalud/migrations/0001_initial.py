# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre del Centro')),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(verbose_name=b'Telefono/Celular')),
                ('responsable', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'centro_salud',
                'verbose_name_plural': 'centros_salud',
            },
            bases=(models.Model,),
        ),
    ]
