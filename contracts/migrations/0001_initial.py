# Generated by Django 5.0.4 on 2024-09-13 17:26

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=200, verbose_name='Objeto de Contrato')),
                ('contract', models.CharField(max_length=200, verbose_name='Numero do Contrato')),
                ('company', models.CharField(max_length=200, verbose_name='Empresa')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('fiscais', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
