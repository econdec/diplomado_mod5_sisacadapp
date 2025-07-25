# Generated by Django 5.2.3 on 2025-07-14 00:03

import regacademico.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regacademico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='estado',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(max_length=100, validators=[regacademico.validators.validar_texto]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=100, validators=[regacademico.validators.validar_texto]),
        ),
    ]
