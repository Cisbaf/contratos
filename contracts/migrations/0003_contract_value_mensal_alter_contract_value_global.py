# Generated by Django 5.0.4 on 2024-10-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_rename_contract_contract_number_contract_cnpj_cpf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='value_mensal',
            field=models.CharField(default=1, max_length=200, verbose_name='Valor Mensal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='value_global',
            field=models.CharField(max_length=200, verbose_name='Valor Global'),
        ),
    ]
