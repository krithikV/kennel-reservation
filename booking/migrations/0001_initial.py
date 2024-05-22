# Generated by Django 5.0.6 on 2024-05-22 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Slot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(unique=True)),
                ("slots_available", models.IntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("owner_name", models.CharField(max_length=100)),
                ("pet_name", models.CharField(max_length=100)),
                ("contact_number", models.CharField(max_length=15)),
                (
                    "slot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booking.slot"
                    ),
                ),
            ],
        ),
    ]
