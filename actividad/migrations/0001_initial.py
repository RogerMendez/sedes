# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80, verbose_name=b'Nombre de la Actividad')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'actividades',
            },
            bases=(models.Model,),
        ),
    ]
