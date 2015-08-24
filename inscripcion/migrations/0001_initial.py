# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0001_initial'),
        ('centrosalud', '0001_initial'),
        ('gestion', '0001_initial'),
        ('actividad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad_grupo_poblacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['actividad_inscripcion'],
                'verbose_name': 'Actividad Grupo',
                'verbose_name_plural': 'Actividades Grupo',
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Actividad_Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_asignacion', models.DateField(auto_now_add=True)),
                ('actividad', models.ForeignKey(to='actividad.Actividad')),
            ],
            options={
                'ordering': ['inscripcion'],
                'verbose_name': 'Acctividad Asignada',
                'verbose_name_plural': 'Actividades Asignadas',
                'permissions': (('index_asignacion', 'Index Asignaciones'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('centro', models.ForeignKey(to='centrosalud.Centro')),
                ('gestion', models.ForeignKey(to='gestion.Gestion')),
            ],
            options={
                'ordering': ['gestion'],
                'verbose_name': 'Inscripcion',
                'verbose_name_plural': 'Inscripciones',
                'permissions': (('index_inscripcion', 'Index Incripciones'),),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='actividad_inscripcion',
            name='inscripcion',
            field=models.ForeignKey(to='inscripcion.Inscripcion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad_grupo_poblacion',
            name='actividad_inscripcion',
            field=models.ForeignKey(to='inscripcion.Actividad_Inscripcion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad_grupo_poblacion',
            name='grupo',
            field=models.ForeignKey(to='grupo.Grupo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad_grupo_poblacion',
            name='poblacion',
            field=models.ForeignKey(to='gestion.Poblacion'),
            preserve_default=True,
        ),
    ]
