# Generated by Django 5.1 on 2024-08-20 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_ride_dropoff_latitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ride",
            name="driver",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="driver",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="ride",
            name="rider",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rider",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
