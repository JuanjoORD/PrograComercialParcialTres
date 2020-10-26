# Generated by Django 3.1.2 on 2020-10-26 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('alcalde', models.CharField(max_length=80)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guatemala.departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guatemala.municipio')),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='municipios',
            field=models.ManyToManyField(through='guatemala.Relacion', to='guatemala.Municipio'),
        ),
    ]