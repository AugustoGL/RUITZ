# Generated by Django 4.2.4 on 2023-10-14 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruitz', '0007_remove_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
    ]