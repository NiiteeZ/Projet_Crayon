# Generated by Django 5.1.1 on 2024-09-25 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ville",
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
                ("nom", models.CharField(max_length=100)),
                ("code_postal", models.IntegerField(default=0)),
                ("prix", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Local",
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
                ("nom", models.CharField(max_length=100)),
                ("surface", models.IntegerField(default=0)),
                (
                    "ville",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.ville",
                    ),
                ),
            ],
        ),
    ]