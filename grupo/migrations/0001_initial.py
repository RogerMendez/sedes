# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variable', models.CharField(max_length=100, verbose_name=b'Rango Poblacion')),
            ],
            options={
                'ordering': ['variable'],
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
            bases=(models.Model,),
        ),
    ]
