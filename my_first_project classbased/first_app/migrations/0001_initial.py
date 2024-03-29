# Generated by Django 5.0 on 2023-12-15 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Musician",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("instrument", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Album",
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
                ("name", models.CharField(max_length=100)),
                ("release_data", models.DateField()),
                (
                    "num_stars",
                    models.IntegerField(
                        choices=[
                            (1, "Worst"),
                            (2, "Bad"),
                            (3, "Not Bad"),
                            (4, "Good"),
                            (5, "Excellent!!!"),
                        ]
                    ),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="first_app.musician",
                    ),
                ),
            ],
        ),
    ]
