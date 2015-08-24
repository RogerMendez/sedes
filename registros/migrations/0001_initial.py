# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
                ('inscripcion', models.ForeignKey(to='inscripcion.Inscripcion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
