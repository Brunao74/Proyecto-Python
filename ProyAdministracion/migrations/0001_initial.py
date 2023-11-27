# Generated by Django 4.2.7 on 2023-11-26 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandaHoraria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('horario_inicio', models.DateTimeField()),
                ('horario_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('nota', models.IntegerField()),
                ('banda_horaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyAdministracion.bandahoraria')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyAdministracion.curso')),
            ],
        ),
    ]