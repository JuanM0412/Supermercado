# Generated by Django 4.2.1 on 2023-05-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_alter_factura_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(verbose_name='2023-05-24 09:21:37'),
        ),
    ]
