# Generated by Django 5.2 on 2025-05-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoescolar', '0002_gestao_carga_horaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestao',
            name='carga_horaria',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gestao',
            name='disciplina',
            field=models.CharField(max_length=100),
        ),
    ]
