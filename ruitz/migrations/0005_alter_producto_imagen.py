# Generated by Django 4.2.4 on 2023-10-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruitz', '0004_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
