# Generated by Django 5.0.6 on 2024-05-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuit', models.CharField(max_length=15, verbose_name='CUIT')),
                ('company_name', models.CharField(max_length=100, verbose_name='Razón Social')),
                ('activity_code', models.CharField(max_length=6, verbose_name='CLANAE')),
                ('city', models.CharField(max_length=50, verbose_name='Departamento')),
                ('contact', models.CharField(max_length=100, verbose_name='Datos de contacto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de última modificación')),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
                'ordering': ['company_name'],
            },
        ),
    ]
