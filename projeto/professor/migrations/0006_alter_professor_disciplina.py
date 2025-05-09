# Generated by Django 5.2 on 2025-05-02 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoescolar', '0004_alter_gestao_carga_horaria'),
        ('professor', '0005_alter_professor_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores', to='gestaoescolar.gestao', unique=True),
        ),
    ]
