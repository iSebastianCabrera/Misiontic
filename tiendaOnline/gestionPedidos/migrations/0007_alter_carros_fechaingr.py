# Generated by Django 3.2.4 on 2021-06-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0006_rename_fechaingreso_carros_fechaingr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='fechaIngr',
            field=models.DateField(blank=True, null=True),
        ),
    ]
